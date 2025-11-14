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

        manager = OutputManager(output_dir=str(output_path))
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
        assert "deepsearch" in saved_path.name

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

        # Should contain timestamp
        assert "_" in filename
        assert filename.startswith("deepsearch_")
        assert filename.endswith(".json")

        # Should be safe for filesystem
        assert "/" not in filename
        assert "\\" not in filename
