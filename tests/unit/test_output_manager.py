"""Unit tests for output management functionality."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, Mock

import pytest

# Mock deep_research_client for import issues
mock_deep_research_client = MagicMock()
mock_deep_research_client.DeepResearchClient = Mock
sys.modules["deep_research_client"] = mock_deep_research_client


# Mock ResearchResult for testing
class MockResearchResult:
    def __init__(self, markdown: str, citations: list = None, provider: str = "perplexity"):
        self.markdown = markdown
        self.citations = citations or []
        self.provider = provider
        self.model = "sonar-deep-research"


@pytest.mark.unit
def test_output_manager_import() -> None:
    """Test that output manager can be imported."""
    try:
        from langpa.services.output_manager import OutputManager

        assert OutputManager is not None
    except ImportError as e:
        pytest.fail(f"OutputManager should be importable: {e}")


@pytest.mark.unit
def test_output_manager_initialization() -> None:
    """Test output manager can be initialized with output directory."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)
        assert manager.output_dir == Path(temp_dir)
        assert manager.output_dir.exists()


@pytest.mark.unit
def test_output_manager_creates_directory() -> None:
    """Test output manager creates output directory if it doesn't exist."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = Path(temp_dir) / "outputs"
        assert not output_path.exists()

        OutputManager(output_dir=str(output_path))
        assert output_path.exists()


@pytest.mark.unit
def test_save_raw_response() -> None:
    """Test saving raw DeepSearch response to file."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        # Mock research result
        result = MockResearchResult(
            markdown="# Test Analysis\n\nSome analysis content",
            citations=["https://pubmed.ncbi.nlm.nih.gov/123456"],
        )

        genes = ["TP53", "BRCA1"]
        context = "cancer research"

        # Save raw response
        saved_path = manager.save_raw_response(result, genes, context)

        # Verify file was created
        assert saved_path.exists()
        assert saved_path.suffix == ".json"
        assert saved_path.name == "deepsearch.json"

        # Verify file contents
        with open(saved_path) as f:
            saved_data = json.load(f)

        assert saved_data["metadata"]["genes"] == genes
        assert saved_data["metadata"]["context"] == context
        assert saved_data["metadata"]["provider"] == "perplexity"
        assert saved_data["raw_response"]["markdown"] == result.markdown
        assert saved_data["raw_response"]["citations"] == result.citations


@pytest.mark.unit
def test_extract_json_from_markdown() -> None:
    """Test extracting JSON from markdown response."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        # Test markdown with embedded JSON
        markdown_with_json = """
# Analysis

Some text before JSON

```json
{
  "context": {
    "cell_type": "neural",
    "disease": "cancer"
  },
  "input_genes": ["TP53"],
  "programs": []
}
```

Some text after JSON
        """

        extracted_json = manager.extract_json_from_markdown(markdown_with_json)

        assert extracted_json is not None
        assert extracted_json["context"]["cell_type"] == "neural"
        assert extracted_json["input_genes"] == ["TP53"]


@pytest.mark.unit
def test_extract_json_after_think_and_code_fence() -> None:
    """Test extraction when JSON follows </think> with a code fence."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        markdown_with_think = """
<think>reasoning...</think>

```json
{
  "context": {"cell_type": "neural", "disease": "cancer"},
  "input_genes": ["TP53"],
  "programs": []
}
```
"""
        extracted_json = manager.extract_json_from_markdown(markdown_with_think)
        assert extracted_json is not None
        assert extracted_json["input_genes"] == ["TP53"]


@pytest.mark.unit
def test_extract_json_after_think_raw_object() -> None:
    """Test extraction when JSON follows </think> without a fence."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        markdown_with_think = """
<think>reasoning...</think>
{
  "context": {"cell_type": "neural", "disease": "cancer"},
  "input_genes": ["TP53"],
  "programs": []
}
"""
        extracted_json = manager.extract_json_from_markdown(markdown_with_think)
        assert extracted_json is not None
        assert extracted_json["context"]["disease"] == "cancer"


@pytest.mark.unit
def test_extract_json_prefers_after_think_over_schema_block() -> None:
    """Ensure schema code fences earlier don't overshadow the post-think JSON."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        markdown_with_schema_then_output = """
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Schema"
}
```

<think>reasoning...</think>

```json
{
  "context": {"cell_type": "neural", "disease": "glioblastoma"},
  "input_genes": ["TP53"],
  "programs": []
}
```
"""
        extracted_json = manager.extract_json_from_markdown(markdown_with_schema_then_output)
        assert extracted_json is not None
        assert extracted_json["context"]["disease"] == "glioblastoma"


@pytest.mark.unit
def test_extract_json_handles_malformed() -> None:
    """Test JSON extraction handles malformed JSON gracefully."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        # Test with malformed JSON
        malformed_markdown = """
```json
{
  "context": {
    "cell_type": "neural"
    // missing comma and closing brace
```
        """

        extracted_json = manager.extract_json_from_markdown(malformed_markdown)
        assert extracted_json is None


@pytest.mark.unit
def test_process_parses_stringified_json(monkeypatch: pytest.MonkeyPatch) -> None:
    """Ensure stringified JSON is parsed before validation/saving."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        class DummyResult:
            markdown = "{}"
            citations: list = []
            provider = "test"
            model = "test-model"
            duration_seconds = 1.0

        # Force extract_json_from_markdown to return a JSON string
        valid_payload = {
            "context": {"cell_type": "x", "disease": "y"},
            "input_genes": ["A"],
            "programs": [
                {
                    "program_name": "p",
                    "description": "d",
                    "predicted_cellular_impact": ["impact"],
                    "evidence_summary": "ev",
                    "significance_score": 0.5,
                    "citations": [{"source_id": "1"}],
                    "supporting_genes": ["A"],
                }
            ],
            "version": "1",
        }

        monkeypatch.setattr(
            manager, "extract_json_from_markdown", lambda _m: json.dumps(valid_payload)
        )

        processing = manager.process_and_save_structured_output(
            DummyResult(),
            genes=["A"],
            context="ctx",
        )

        assert processing["success"] is True
        assert processing["structured_data"] == valid_payload


@pytest.mark.unit
def test_validate_against_schema() -> None:
    """Test JSON validation against deepsearch schema."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        # Valid JSON that should pass schema validation
        valid_json = {
            "context": {
                "cell_type": "neural stem cells",
                "disease": "neurodevelopmental disorders",
                "tissue": "brain",
            },
            "input_genes": ["TP53", "BRCA1"],
            "programs": [
                {
                    "program_name": "Test Program",
                    "description": "A test program",
                    "predicted_cellular_impact": ["test impact"],
                    "evidence_summary": "test evidence",
                    "significance_score": 0.8,
                    "citations": [
                        {
                            "source_id": "PMID:12345678",
                            "notes": "Supporting evidence for test program",
                        }
                    ],
                    "supporting_genes": ["TP53"],
                }
            ],
            "version": "1.0",
        }

        is_valid, error_msg = manager.validate_against_schema(valid_json)
        assert is_valid is True
        assert error_msg is None


@pytest.mark.unit
def test_validate_rejects_invalid_schema() -> None:
    """Test schema validation rejects invalid JSON."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        # Invalid JSON missing required fields
        invalid_json = {
            "context": {"cell_type": "neural", "disease": ""},
            "input_genes": ["TP53"],
            # Missing required 'programs' and 'version'
        }

        is_valid, error_msg = manager.validate_against_schema(invalid_json)
        assert is_valid is False
        assert error_msg is not None
        assert "required" in error_msg.lower()


@pytest.mark.unit
def test_filename_generation() -> None:
    """Test proper filename generation with timestamps."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        genes = ["TP53", "BRCA1"]
        context = "cancer research"

        filename = manager._generate_filename(genes, context)

        # Fixed base name with no timestamp or metadata
        assert filename == "deepsearch.json"

        # Genes/context should not be embedded in filename
        assert "TP53" not in filename
        assert "BRCA1" not in filename
        assert "cancer" not in filename
        assert "research" not in filename

        # Should be safe for filesystem
        assert "/" not in filename
        assert "\\" not in filename

# Phase 3: Pydantic validation tests

@pytest.mark.unit
def test_validate_against_schema_v2_success() -> None:
    """Test new pydantic validation method with valid data."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        valid_data = {
            "context": {"cell_type": "cells", "disease": "test"},
            "input_genes": ["TMEM14E"],
            "programs": [{
                "program_name": "Test",
                "description": "Test program",
                "predicted_cellular_impact": ["test impact"],
                "evidence_summary": "test",
                "significance_score": 0.5,
                "citations": [{"source_id": "1"}],
                "supporting_genes": ["TMEM14E"]
            }],
            "version": "1.0"
        }

        is_valid, error_msg, metadata = manager.validate_against_schema_v2(
            valid_data,
            use_pydantic=True
        )

        assert is_valid is True
        assert error_msg is None
        assert metadata["retry_count"] == 0
        assert metadata["validation_time_ms"] > 0
        assert metadata["corrections_applied"] is False


@pytest.mark.unit
def test_validate_against_schema_v2_invalid() -> None:
    """Test pydantic validation with invalid data."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        # Missing required fields
        invalid_data = {
            "context": {"cell_type": "cells", "disease": "test"}
            # Missing input_genes, programs, version
        }

        is_valid, error_msg, metadata = manager.validate_against_schema_v2(
            invalid_data,
            use_pydantic=True,
            max_retries=1
        )

        assert is_valid is False
        assert error_msg is not None


@pytest.mark.unit
def test_validate_against_schema_v2_fallback_to_jsonschema() -> None:
    """Test that v2 can fallback to legacy jsonschema validation."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        valid_data = {
            "context": {"cell_type": "cells", "disease": "test"},
            "input_genes": ["TMEM14E"],
            "programs": [{
                "program_name": "Test",
                "description": "Test",
                "predicted_cellular_impact": ["impact"],
                "evidence_summary": "evidence",
                "significance_score": 0.5,
                "citations": [{"source_id": "1"}],
                "supporting_genes": ["TMEM14E"]
            }],
            "version": "1.0"
        }

        # Use fallback to jsonschema
        is_valid, error_msg, metadata = manager.validate_against_schema_v2(
            valid_data,
            use_pydantic=False
        )

        assert is_valid is True
        assert error_msg is None
        # No metadata when using fallback
        assert metadata == {}


@pytest.mark.unit
def test_backward_compatibility_validate_against_schema() -> None:
    """Test that legacy validation method still works."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        valid_data = {
            "context": {"cell_type": "cells", "disease": "test"},
            "input_genes": ["TMEM14E"],
            "programs": [{
                "program_name": "Test",
                "description": "Test",
                "predicted_cellular_impact": ["impact"],
                "evidence_summary": "evidence",
                "significance_score": 0.5,
                "citations": [{"source_id": "1"}],
                "supporting_genes": ["TMEM14E"]
            }],
            "version": "1.0"
        }

        # Old method should still work
        is_valid, error_msg = manager.validate_against_schema(valid_data)

        assert is_valid is True
        assert error_msg is None


@pytest.mark.unit
def test_process_and_save_with_pydantic() -> None:
    """Test process_and_save_structured_output with pydantic validation."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        # Valid JSON in markdown
        markdown = '''
```json
{
    "context": {"cell_type": "cells", "disease": "test"},
    "input_genes": ["TMEM14E"],
    "programs": [{
        "program_name": "Test",
        "description": "Test",
        "predicted_cellular_impact": ["impact"],
        "evidence_summary": "evidence",
        "significance_score": 0.5,
        "citations": [{"source_id": "1"}],
        "supporting_genes": ["TMEM14E"]
    }],
    "version": "1.0"
}
```
        '''

        result = MockResearchResult(markdown=markdown)

        processing = manager.process_and_save_structured_output(
            result=result,
            genes=["TMEM14E"],
            context="cells",
            use_pydantic=True
        )

        assert processing["success"] is True
        assert processing["json_extracted"] is True
        assert processing["schema_valid"] is True
        assert "validation_metadata" in processing
        assert processing["validation_metadata"]["retry_count"] >= 0


@pytest.mark.unit
def test_validator_lazy_loading() -> None:
    """Test that validator is lazy-loaded to avoid import overhead."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        # Validator should not be initialized yet
        assert manager._validator is None

        # Access validator property
        validator = manager.validator

        # Now it should be initialized
        assert validator is not None
        assert manager._validator is not None

        # Second access should return same instance
        validator2 = manager.validator
        assert validator is validator2
