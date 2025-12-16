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
        self._validator = None  # Lazy-loaded validator

    def save_raw_response(
        self,
        result: Any,  # ResearchResult object
        genes: list[str],
        context: str,
        metadata: dict[str, Any] | None = None,
        filename: str | None = None,
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
        filename = filename or self._generate_filename(genes, context)
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
            candidates: list[dict[str, Any]] = []
            seen_blocks: set[str] = set()

            def add_candidate(json_text: str) -> None:
                """Parse and store a JSON block if valid and unseen."""
                cleaned = json_text.strip()
                if not cleaned or cleaned in seen_blocks:
                    return
                try:
                    parsed = json.loads(cleaned)
                except json.JSONDecodeError:
                    return
                if isinstance(parsed, dict):
                    parsed.pop("$schema", None)
                    candidates.append(parsed)
                    seen_blocks.add(cleaned)

            # Method 1: Look for JSON after </think> with optional fence or raw JSON
            think_pattern = r"</think>\s*(?:```json\s*\n(.*?)\n```|(\{.*\}))"
            match = re.search(think_pattern, markdown, re.DOTALL)
            if match:
                json_candidate = match.group(1) or match.group(2)
                if json_candidate:
                    add_candidate(json_candidate)

            # Method 2: Look for JSON code blocks
            json_pattern = r"```json\s*\n(.*?)\n```"
            for m in re.finditer(json_pattern, markdown, re.DOTALL):
                add_candidate(m.group(1))

            # Method 3: Standalone JSON blocks (after prompts like 'Here is the JSON')
            json_start_patterns = [
                r"</think>\s*\n\s*(\{.*\})",
                r"Here is the JSON[:\s]*\n\s*(\{.*\})",
                r"JSON[:\s]*\n\s*(\{.*\})",
                r"```\s*(\{.*\})\s*```",
                r'\n(\{[^}]*"context"[^}]*\}.*\})',
            ]
            for pattern in json_start_patterns:
                match = re.search(pattern, markdown, re.DOTALL | re.IGNORECASE)
                if match:
                    add_candidate(match.group(1))

            # Method 4: Find large JSON-like structures by brace matching
            brace_positions = []
            for i, char in enumerate(markdown):
                if char == "{":
                    brace_positions.append(("open", i))
                elif char == "}":
                    brace_positions.append(("close", i))

            stack: list[int] = []
            json_texts: list[tuple[str, int]] = []
            for brace_type, pos in brace_positions:
                if brace_type == "open":
                    stack.append(pos)
                elif brace_type == "close" and stack:
                    start_pos = stack.pop()
                    if not stack:
                        json_text = markdown[start_pos : pos + 1].strip()
                        if len(json_text) > 100:
                            json_texts.append((json_text, len(json_text)))

            for json_text, _ in sorted(json_texts, key=lambda x: x[1], reverse=True)[:3]:
                add_candidate(json_text)

            if not candidates:
                return None

            def is_schema_like(data: dict[str, Any]) -> bool:
                """Detect schema/definition blocks lacking result content."""
                if "programs" in data or "context" in data or "input_genes" in data:
                    return False
                schema_keys = {"definitions", "title", "description", "required", "type"}
                return bool(schema_keys & set(data.keys()))

            def score_candidate(data: dict[str, Any]) -> int:
                """Score candidates to prefer actual result payloads."""
                score = 0
                if "programs" in data:
                    score += 3
                    if data.get("programs"):
                        score += 1
                if "context" in data:
                    score += 2
                if "input_genes" in data:
                    score += 1
                if is_schema_like(data):
                    score -= 5
                return score

            scored = [(score_candidate(c), idx, c) for idx, c in enumerate(candidates)]
            scored.sort(key=lambda t: (t[0], -t[1]), reverse=True)
            best_score, _, best_candidate = scored[0]

            return best_candidate if best_score > 0 else None

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

    @property
    def validator(self):
        """Lazy-load DeepSearchValidator to avoid import overhead.

        Returns:
            DeepSearchValidator instance
        """
        if self._validator is None:
            from langpa.services.deepsearch_validator import DeepSearchValidator

            self._validator = DeepSearchValidator()
        return self._validator

    def validate_against_schema_v2(
        self,
        json_data: dict[str, Any],
        use_pydantic: bool = True,
        max_retries: int = 3,
    ) -> tuple[bool, str | None, dict[str, Any]]:
        """Validate JSON data with pydantic support and metadata.

        New validation method that supports both pydantic (via cellsem_llm_client)
        and legacy jsonschema validation for backward compatibility.

        Args:
            json_data: JSON data to validate
            use_pydantic: Use pydantic validation if True, jsonschema if False
            max_retries: Maximum retry attempts for pydantic validation

        Returns:
            Tuple of (is_valid, error_message, metadata)
            metadata includes: retry_count, validation_time_ms, corrections_applied

        .. code-block:: python

            is_valid, error, metadata = manager.validate_against_schema_v2(
                data,
                use_pydantic=True
            )
            if is_valid:
                print(f"Validated after {metadata['retry_count']} retries")
        """
        if not use_pydantic:
            # Fallback to legacy jsonschema
            is_valid, error_msg = self.validate_against_schema(json_data)
            return is_valid, error_msg, {}

        # Use pydantic validation with retry
        result = self.validator.validate_json_dict(json_data, max_retries)

        metadata = {
            "retry_count": result.retry_count,
            "validation_time_ms": result.validation_time_ms,
            "corrections_applied": result.retry_count > 0,
        }

        error_msg = str(result.error) if result.error else None

        return result.success, error_msg, metadata

    def process_and_save_structured_output(
        self,
        result: Any,  # ResearchResult object
        genes: list[str],
        context: str,
        raw_filepath: Path | None = None,
        resolve_citations: bool = False,
        resolver: CitationResolver | None = None,
        metadata: dict[str, Any] | None = None,
        filename_prefix: str | None = None,
        use_pydantic: bool = True,
        citation_style: str = "vancouver",
        citation_locale: str = "en-US",
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
            filename_prefix: Optional prefix for output filenames
            use_pydantic: Use Pydantic validation with extra field handling (default: True).
                         Pydantic validation is more robust for LLM outputs that may include
                         unexpected fields like schema metadata (title, description, type).
                         Set to False to use legacy jsonschema validation.
            citation_style: Citation style for compact bibliography (default: vancouver)
            citation_locale: Locale for citation formatting (default: en-US)

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
            if use_pydantic:
                is_valid, error_msg, val_metadata = self.validate_against_schema_v2(
                    extracted_json, use_pydantic=True
                )
                processing_result["validation_metadata"] = val_metadata
            else:
                is_valid, error_msg = self.validate_against_schema(extracted_json)

            processing_result["schema_valid"] = is_valid

            if not is_valid:
                processing_result["errors"].append(f"Schema validation failed: {error_msg}")
            else:
                processing_result["success"] = True

                # Save structured output
                structured_filename = (
                    f"{filename_prefix}_structured.json"
                    if filename_prefix
                    else self._generate_filename(genes, context, suffix="_structured")
                )
                structured_filepath = self.output_dir / structured_filename

                structured_output = {
                    "metadata": {
                        "timestamp": datetime.now().isoformat(),
                        "genes": genes,
                        "context": context,
                        "validation_status": "valid",
                        "raw_file_reference": str(raw_filepath) if raw_filepath else None,
                        **(metadata or {}),
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
                        filename_prefix=filename_prefix,
                        citation_style=citation_style,
                        citation_locale=citation_locale,
                    )
                    processing_result.update(citation_data)

        except Exception as e:
            processing_result["errors"].append(f"Processing error: {str(e)}")

        return processing_result

    def _generate_filename(
        self, genes: list[str], context: str, suffix: str = "", extension: str = ".json"
    ) -> str:
        """Generate a deterministic filename for output files.

        Args:
            genes: List of genes (unused; kept for backward compatibility)
            context: Biological context (unused; kept for backward compatibility)
            suffix: Optional suffix to add (include leading underscore)
            extension: File extension (default .json)

        Returns:
            Safe filename string (no embedded metadata or timestamps)
        """
        base = "deepsearch"
        filename = f"{base}{suffix}{extension}"
        return re.sub(r'[<>:"/\\|?*]', "_", filename)

    def list_container_files(
        self,
        project: str,
        query: str | None = None
    ) -> list[Path]:
        """List all container files for a project/query.

        Args:
            project: Project name
            query: Optional query name (if None, search all queries)

        Returns:
            List of paths to container JSON files

        .. code-block:: python

            manager = OutputManager(output_dir="outputs")
            containers = manager.list_container_files("glioblastoma", "0_Gliosis")
            for container in containers:
                print(container)
        """
        project_dir = self.output_dir / project

        if not project_dir.exists():
            return []

        containers = []

        if query:
            # Search specific query directory
            query_dir = project_dir / query
            if query_dir.exists():
                containers.extend(query_dir.glob("*/deepsearch_container.json"))
        else:
            # Search all queries
            containers.extend(project_dir.glob("*/*/deepsearch_container.json"))

        return sorted(containers)

    def load_container(self, container_path: str | Path) -> dict[str, Any]:
        """Load a container JSON file.

        Args:
            container_path: Path to container JSON

        Returns:
            Container data dict

        .. code-block:: python

            manager = OutputManager(output_dir="outputs")
            container = manager.load_container("outputs/project/query/run/container.json")
            programs = container["report"]["programs"]
        """
        with open(container_path, encoding="utf-8") as f:
            return json.load(f)

    def load_containers_for_query(
        self,
        project: str,
        query: str
    ) -> list[dict[str, Any]]:
        """Load all containers for a specific query.

        Args:
            project: Project name
            query: Query name

        Returns:
            List of container data dicts

        .. code-block:: python

            manager = OutputManager(output_dir="outputs")
            containers = manager.load_containers_for_query("glioblastoma", "0_Gliosis")
            print(f"Loaded {len(containers)} runs")
        """
        container_paths = self.list_container_files(project, query)
        return [self.load_container(path) for path in container_paths]

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
        filename_prefix: str | None,
        citation_style: str = "vancouver",
        citation_locale: str = "en-US",
    ) -> dict[str, Any]:
        """Resolve citations via url2ref and build container JSON with compact refs.

        Args:
            result: ResearchResult object
            structured_json: Validated structured output
            genes: Gene list
            context: Biological context
            resolver: CitationResolver instance (created if None)
            metadata: Optional metadata
            raw_filepath: Path to raw response file
            filename_prefix: Optional filename prefix
            citation_style: Citation style for compact bibliography (default: vancouver)
            citation_locale: Locale for formatting (default: en-US)

        Returns:
            Dict with container_file path and citation resolution details
        """
        citation_list = getattr(result, "citations", []) or []
        normalized_citations = normalize_citations(citation_list)

        if resolver is None:
            resolver = CitationResolver()

        # Use new method to get compact bibliography
        resolution = resolver.resolve_with_compact(
            normalized_citations,
            style=citation_style,
            locale=citation_locale,
        )

        container_filename = (
            f"{filename_prefix}_container.json"
            if filename_prefix
            else self._generate_filename(genes, context, suffix="_container")
        )
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
            "compact_bibliography": resolution["compact_bibliography"],
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
