"""Output management for DeepSearch results."""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from jsonschema import ValidationError, validate

from langpa.schemas import load_schema
from langpa.services.citation_normalizer import normalize_citations
from langpa.services.citation_resolver import CitationResolver


class OutputManager:
    """Manages saving and processing of DeepSearch output files."""

    def __init__(self, output_dir: str | Path = "outputs") -> None:
        """Initialize the output manager.

        Args:
            output_dir: Directory to save outputs (default: "outputs")
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_raw_response(
        self,
        result: Any,  # ResearchResult object
        genes: list[str],
        context: str,
        metadata: dict[str, Any] | None = None,
    ) -> Path:
        """Save raw DeepSearch response to JSON file.

        Args:
            result: ResearchResult object from DeepSearch API
            genes: List of genes that were analyzed
            context: Biological context used for analysis
            metadata: Optional additional metadata to include

        Returns:
            Path to the saved file
        """
        # Generate filename
        filename = self._generate_filename(genes, context)
        filepath = self.output_dir / filename

        # Prepare data structure
        output_data = {
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "genes": genes,
                "context": context,
                "provider": getattr(result, "provider", "unknown"),
                "model": getattr(result, "model", "unknown"),
                **(metadata or {}),
            },
            "raw_response": {
                "markdown": getattr(result, "markdown", ""),
                "citations": getattr(result, "citations", []),
                "duration_seconds": getattr(result, "duration_seconds", None),
            },
        }

        # Save to file
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        return filepath

    def extract_json_from_markdown(self, markdown: str) -> dict[str, Any] | None:
        """Extract JSON content from markdown response.

        Args:
            markdown: Markdown content containing embedded JSON

        Returns:
            Parsed JSON dict or None if extraction/parsing fails
        """
        try:
            # Method 1: Look for JSON after </think> with optional fence or raw JSON
            think_pattern = r"</think>\s*(?:```json\s*\n(.*?)\n```|(\{.*\}))"
            match = re.search(think_pattern, markdown, re.DOTALL)
            if match:
                json_candidate = match.group(1) or match.group(2)
                if json_candidate:
                    json_candidate = json_candidate.strip()
                    try:
                        parsed = json.loads(json_candidate)
                        if isinstance(parsed, dict):
                            parsed.pop("$schema", None)
                        return parsed
                    except json.JSONDecodeError:
                        pass

            # Method 2: Look for JSON code blocks (prioritize ones containing "context")
            json_pattern = r"```json\s*\n(.*?)\n```"
            matches = re.finditer(json_pattern, markdown, re.DOTALL)
            for m in matches:
                json_content = m.group(1).strip()
                try:
                    parsed = json.loads(json_content)
                    if isinstance(parsed, dict):
                        parsed.pop("$schema", None)
                        # Prefer blocks that look like our schema (contain context/programs)
                        if "context" in parsed or "programs" in parsed:
                            return parsed
                        # If no better candidate is found, return the first successfully
                        # parsed block
                        return parsed
                except json.JSONDecodeError:
                    continue

            # Method 2: Look for standalone JSON blocks (often after thinking)
            # Common patterns: after </think>, or after "Here is the JSON:"
            json_start_patterns = [
                r"</think>\s*\n\s*(\{.*\})",
                r"Here is the JSON[:\s]*\n\s*(\{.*\})",
                r"JSON[:\s]*\n\s*(\{.*\})",
                r"```\s*(\{.*\})\s*```",
                r'\n(\{[^}]*"context"[^}]*\}.*\})',  # Look for our specific schema structure
            ]

            for pattern in json_start_patterns:
                match = re.search(pattern, markdown, re.DOTALL | re.IGNORECASE)
                if match:
                    json_content = match.group(1).strip()
                    try:
                        parsed = json.loads(json_content)
                        # Remove $schema field if present (causes validation issues)
                        if isinstance(parsed, dict):
                            parsed.pop("$schema", None)
                        return parsed
                    except json.JSONDecodeError:
                        continue

            # Method 3: Find largest JSON-like structure
            brace_positions = []
            for i, char in enumerate(markdown):
                if char == "{":
                    brace_positions.append(("open", i))
                elif char == "}":
                    brace_positions.append(("close", i))

            # Find properly nested JSON structures
            candidates = []
            stack = []

            for brace_type, pos in brace_positions:
                if brace_type == "open":
                    stack.append(pos)
                elif brace_type == "close" and stack:
                    start_pos = stack.pop()
                    if not stack:  # Complete JSON structure
                        json_text = markdown[start_pos : pos + 1].strip()
                        if len(json_text) > 100:  # Reasonable size filter
                            candidates.append((json_text, len(json_text)))

            # Try candidates from largest to smallest
            candidates.sort(key=lambda x: x[1], reverse=True)
            for json_text, _ in candidates[:3]:  # Try top 3 candidates
                try:
                    parsed = json.loads(json_text)
                    # Verify it looks like our schema
                    if isinstance(parsed, dict) and ("context" in parsed or "programs" in parsed):
                        # Remove $schema field if present (causes validation issues)
                        parsed.pop("$schema", None)
                        return parsed
                except json.JSONDecodeError:
                    continue

            return None

        except Exception:
            return None

    def validate_against_schema(
        self, json_data: dict[str, Any], schema_name: str = "deepsearch_results_schema.json"
    ) -> tuple[bool, str | None]:
        """Validate JSON data against the DeepSearch schema.

        Args:
            json_data: JSON data to validate
            schema_name: Name of schema file to validate against

        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            schema = load_schema(schema_name)
            validate(instance=json_data, schema=schema)
            return True, None

        except ValidationError as e:
            return False, str(e)

        except Exception as e:
            return False, f"Schema validation error: {str(e)}"

    def process_and_save_structured_output(
        self,
        result: Any,  # ResearchResult object
        genes: list[str],
        context: str,
        raw_filepath: Path | None = None,
        resolve_citations: bool = False,
        resolver: CitationResolver | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Extract JSON from response, validate it, and save processed version.

        Args:
            result: ResearchResult object from DeepSearch API
            genes: List of genes that were analyzed
            context: Biological context used for analysis
            raw_filepath: Optional path to raw file (for reference)
            resolve_citations: Whether to run url2ref resolution and build container output
            resolver: Optional CitationResolver instance; created if not provided
            metadata: Optional metadata to include in container

        Returns:
            Dictionary with processing results including validation status
        """
        processing_result: dict[str, Any] = {
            "success": False,
            "json_extracted": False,
            "schema_valid": False,
            "structured_data": None,
            "errors": [],
            "raw_file": str(raw_filepath) if raw_filepath else None,
            "container_file": None,
        }

        try:
            # Extract JSON from markdown
            markdown = getattr(result, "markdown", "")
            extracted_json = self.extract_json_from_markdown(markdown)

            if extracted_json is None:
                processing_result["errors"].append("Could not extract JSON from markdown response")
                return processing_result

            processing_result["json_extracted"] = True
            if isinstance(extracted_json, str):
                try:
                    extracted_json = json.loads(extracted_json)
                except json.JSONDecodeError as e:
                    processing_result["errors"].append(
                        f"Extracted JSON string failed to parse: {e}"
                    )
                    return processing_result

            processing_result["structured_data"] = extracted_json

            # Validate against schema
            is_valid, error_msg = self.validate_against_schema(extracted_json)
            processing_result["schema_valid"] = is_valid

            if not is_valid:
                processing_result["errors"].append(f"Schema validation failed: {error_msg}")
            else:
                processing_result["success"] = True

                # Save structured output
                structured_filename = self._generate_filename(genes, context, suffix="_structured")
                structured_filepath = self.output_dir / structured_filename

                structured_output = {
                    "metadata": {
                        "timestamp": datetime.now().isoformat(),
                        "genes": genes,
                        "context": context,
                        "validation_status": "valid",
                        "raw_file_reference": str(raw_filepath) if raw_filepath else None,
                    },
                    "structured_data": extracted_json,
                }

                with open(structured_filepath, "w", encoding="utf-8") as f:
                    json.dump(structured_output, f, indent=2, ensure_ascii=False)

                processing_result["structured_file"] = str(structured_filepath)

                if resolve_citations:
                    citation_data = self._resolve_and_package_citations(
                        result=result,
                        structured_json=extracted_json,
                        genes=genes,
                        context=context,
                        resolver=resolver,
                        metadata=metadata,
                        raw_filepath=raw_filepath,
                    )
                    processing_result.update(citation_data)

        except Exception as e:
            processing_result["errors"].append(f"Processing error: {str(e)}")

        return processing_result

    def _generate_filename(
        self, genes: list[str], context: str, suffix: str = "", extension: str = ".json"
    ) -> str:
        """Generate a safe filename for output files.

        Args:
            genes: List of genes (will be truncated if too long)
            context: Biological context (will be sanitized)
            suffix: Optional suffix to add
            extension: File extension

        Returns:
            Safe filename string
        """
        # Create timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Sanitize context (remove special characters, limit length)
        safe_context = re.sub(r"[^\w\s-]", "", context.strip())
        safe_context = re.sub(r"\s+", "_", safe_context)[:20]

        # Handle gene list (limit to avoid very long filenames)
        if len(genes) <= 3:
            genes_part = "_".join(genes)
        else:
            genes_part = f"{genes[0]}_{genes[1]}_and_{len(genes) - 2}_more"

        # Sanitize genes part
        genes_part = re.sub(r"[^\w-]", "_", genes_part)[:30]

        filename = f"deepsearch_{timestamp}_{genes_part}_{safe_context}{suffix}{extension}"

        # Final safety check - ensure filename is filesystem safe
        filename = re.sub(r'[<>:"/\\|?*]', "_", filename)

        return filename

    def _resolve_and_package_citations(
        self,
        *,
        result: Any,
        structured_json: dict[str, Any],
        genes: list[str],
        context: str,
        resolver: CitationResolver | None,
        metadata: dict[str, Any] | None,
        raw_filepath: Path | None,
    ) -> dict[str, Any]:
        """Resolve citations via url2ref and build container JSON."""
        citation_list = getattr(result, "citations", []) or []
        normalized_citations = normalize_citations(citation_list)

        if resolver is None:
            resolver = CitationResolver()

        resolution = resolver.resolve(normalized_citations)

        container_filename = self._generate_filename(genes, context, suffix="_container")
        container_filepath = self.output_dir / container_filename

        container_payload = {
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "genes": genes,
                "context": context,
                "provider": getattr(result, "provider", "unknown"),
                "model": getattr(result, "model", "unknown"),
                **(metadata or {}),
            },
            "deepsearch_raw": {
                "markdown": getattr(result, "markdown", ""),
                "citations": citation_list,
                "duration_seconds": getattr(result, "duration_seconds", None),
            },
            "report": structured_json,
            "citations": resolution["citations"],
            "bibliography_stats": resolution["stats"],
            "unresolved": resolution["failures"],
        }

        with open(container_filepath, "w", encoding="utf-8") as f:
            json.dump(container_payload, f, indent=2, ensure_ascii=False)

        return {
            "container_file": str(container_filepath),
            "citation_resolution": resolution,
            "normalized_citations": normalized_citations,
        }
