"""Output management for DeepSearch results."""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from jsonschema import validate, ValidationError

from langpa.schemas import load_schema


class OutputManager:
    """Manages saving and processing of DeepSearch output files."""

    def __init__(self, output_dir: Union[str, Path] = "outputs") -> None:
        """Initialize the output manager.

        Args:
            output_dir: Directory to save outputs (default: "outputs")
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_raw_response(
        self,
        result: Any,  # ResearchResult object
        genes: List[str],
        context: str,
        metadata: Optional[Dict[str, Any]] = None
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
                "provider": getattr(result, 'provider', 'unknown'),
                "model": getattr(result, 'model', 'unknown'),
                **(metadata or {})
            },
            "raw_response": {
                "markdown": getattr(result, 'markdown', ''),
                "citations": getattr(result, 'citations', []),
                "duration_seconds": getattr(result, 'duration_seconds', None),
            }
        }

        # Save to file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        return filepath

    def extract_json_from_markdown(self, markdown: str) -> Optional[Dict[str, Any]]:
        """Extract JSON content from markdown response.

        Args:
            markdown: Markdown content containing embedded JSON

        Returns:
            Parsed JSON dict or None if extraction/parsing fails
        """
        try:
            # Method 1: Look for JSON code blocks
            json_pattern = r'```json\s*\n(.*?)\n```'
            match = re.search(json_pattern, markdown, re.DOTALL)

            if match:
                json_content = match.group(1).strip()
                parsed = json.loads(json_content)
                # Remove $schema field if present (causes validation issues)
                if isinstance(parsed, dict):
                    parsed.pop('$schema', None)
                return parsed

            # Method 2: Look for standalone JSON blocks (often after thinking)
            # Common patterns: after </think>, or after "Here is the JSON:"
            json_start_patterns = [
                r'</think>\s*\n\s*(\{.*\})',
                r'Here is the JSON[:\s]*\n\s*(\{.*\})',
                r'JSON[:\s]*\n\s*(\{.*\})',
                r'```\s*(\{.*\})\s*```',
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
                            parsed.pop('$schema', None)
                        return parsed
                    except json.JSONDecodeError:
                        continue

            # Method 3: Find largest JSON-like structure
            brace_positions = []
            for i, char in enumerate(markdown):
                if char == '{':
                    brace_positions.append(('open', i))
                elif char == '}':
                    brace_positions.append(('close', i))

            # Find properly nested JSON structures
            candidates = []
            stack = []

            for brace_type, pos in brace_positions:
                if brace_type == 'open':
                    stack.append(pos)
                elif brace_type == 'close' and stack:
                    start_pos = stack.pop()
                    if not stack:  # Complete JSON structure
                        json_text = markdown[start_pos:pos+1].strip()
                        if len(json_text) > 100:  # Reasonable size filter
                            candidates.append((json_text, len(json_text)))

            # Try candidates from largest to smallest
            candidates.sort(key=lambda x: x[1], reverse=True)
            for json_text, _ in candidates[:3]:  # Try top 3 candidates
                try:
                    parsed = json.loads(json_text)
                    # Verify it looks like our schema
                    if isinstance(parsed, dict) and ('context' in parsed or 'programs' in parsed):
                        # Remove $schema field if present (causes validation issues)
                        parsed.pop('$schema', None)
                        return parsed
                except json.JSONDecodeError:
                    continue

            return None

        except Exception as e:
            return None

    def validate_against_schema(
        self,
        json_data: Dict[str, Any],
        schema_name: str = "deepsearch_results_schema.json"
    ) -> Tuple[bool, Optional[str]]:
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
        genes: List[str],
        context: str,
        raw_filepath: Optional[Path] = None
    ) -> Dict[str, Any]:
        """Extract JSON from response, validate it, and save processed version.

        Args:
            result: ResearchResult object from DeepSearch API
            genes: List of genes that were analyzed
            context: Biological context used for analysis
            raw_filepath: Optional path to raw file (for reference)

        Returns:
            Dictionary with processing results including validation status
        """
        processing_result = {
            "success": False,
            "json_extracted": False,
            "schema_valid": False,
            "structured_data": None,
            "errors": [],
            "raw_file": str(raw_filepath) if raw_filepath else None
        }

        try:
            # Extract JSON from markdown
            markdown = getattr(result, 'markdown', '')
            extracted_json = self.extract_json_from_markdown(markdown)

            if extracted_json is None:
                processing_result["errors"].append("Could not extract JSON from markdown response")
                return processing_result

            processing_result["json_extracted"] = True
            processing_result["structured_data"] = extracted_json

            # Validate against schema
            is_valid, error_msg = self.validate_against_schema(extracted_json)
            processing_result["schema_valid"] = is_valid

            if not is_valid:
                processing_result["errors"].append(f"Schema validation failed: {error_msg}")
            else:
                processing_result["success"] = True

                # Save structured output
                structured_filename = self._generate_filename(
                    genes, context, suffix="_structured"
                )
                structured_filepath = self.output_dir / structured_filename

                structured_output = {
                    "metadata": {
                        "timestamp": datetime.now().isoformat(),
                        "genes": genes,
                        "context": context,
                        "validation_status": "valid",
                        "raw_file_reference": str(raw_filepath) if raw_filepath else None
                    },
                    "structured_data": extracted_json
                }

                with open(structured_filepath, 'w', encoding='utf-8') as f:
                    json.dump(structured_output, f, indent=2, ensure_ascii=False)

                processing_result["structured_file"] = str(structured_filepath)

        except Exception as e:
            processing_result["errors"].append(f"Processing error: {str(e)}")

        return processing_result

    def _generate_filename(
        self,
        genes: List[str],
        context: str,
        suffix: str = "",
        extension: str = ".json"
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
        safe_context = re.sub(r'[^\w\s-]', '', context.strip())
        safe_context = re.sub(r'\s+', '_', safe_context)[:20]

        # Handle gene list (limit to avoid very long filenames)
        if len(genes) <= 3:
            genes_part = "_".join(genes)
        else:
            genes_part = f"{genes[0]}_{genes[1]}_and_{len(genes)-2}_more"

        # Sanitize genes part
        genes_part = re.sub(r'[^\w-]', '_', genes_part)[:30]

        filename = f"deepsearch_{timestamp}_{genes_part}_{safe_context}{suffix}{extension}"

        # Final safety check - ensure filename is filesystem safe
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)

        return filename