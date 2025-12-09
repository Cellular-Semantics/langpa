"""Unit tests for TestOutputSaver utility.

Tests the test output saving infrastructure for integration test inspection.
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

import pytest

# Add tests directory to path for importing utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.test_output_saver import TestOutputSaver


class MockResponse:
    """Mock API response for testing."""

    def __init__(
        self,
        markdown: str = "Test markdown",
        citations: list | None = None,
        provider: str = "test",
        model: str = "test-model",
        duration_seconds: float = 1.0
    ):
        self.markdown = markdown
        self.citations = citations or []
        self.provider = provider
        self.model = model
        self.duration_seconds = duration_seconds


@pytest.mark.unit
def test_output_saver_disabled() -> None:
    """Test that outputs are not saved when disabled."""
    saver = TestOutputSaver(enabled=False)

    mock_response = MockResponse()
    result = saver.save_test_output(
        test_name="test_foo",
        test_file="test_bar.py",
        raw_response=mock_response,
        test_context={"genes": ["TEST"]}
    )

    assert result is None  # No output saved when disabled


@pytest.mark.unit
def test_output_saver_enabled() -> None:
    """Test that outputs are saved when enabled."""
    

    with tempfile.TemporaryDirectory() as temp_dir:
        saver = TestOutputSaver(enabled=True, base_dir=temp_dir)

        mock_response = MockResponse(
            markdown="Test markdown response",
            citations=[{"source_id": "1", "notes": "Test citation"}],
            provider="perplexity"
        )

        output_dir = saver.save_test_output(
            test_name="test_foo",
            test_file="test_bar.py",
            raw_response=mock_response,
            test_context={"genes": ["TEST"], "context": "test context"}
        )

        # Verify output directory created
        assert output_dir is not None
        assert output_dir.exists()
        assert output_dir.is_dir()

        # Verify raw response file created
        assert (output_dir / "raw_response.json").exists()


@pytest.mark.unit
def test_output_structure() -> None:
    """Test output file structure and content."""
    

    with tempfile.TemporaryDirectory() as temp_dir:
        saver = TestOutputSaver(enabled=True, base_dir=temp_dir)

        mock_response = MockResponse(
            markdown="Test markdown",
            citations=[{"source_id": "1"}],
            provider="test_provider",
            model="test_model",
            duration_seconds=2.5
        )
        extracted_json = {
            "context": {"cell_type": "test cells", "disease": ""},
            "input_genes": ["TEST"],
            "programs": []
        }

        output_dir = saver.save_test_output(
            test_name="test_foo",
            test_file="test_bar.py",
            raw_response=mock_response,
            extracted_json=extracted_json,
            test_context={"genes": ["TEST"], "context": "test"}
        )

        # Check raw response structure
        with open(output_dir / "raw_response.json") as f:
            raw_data = json.load(f)
            assert "test_context" in raw_data
            assert "response" in raw_data
            assert "saved_at" in raw_data

            # Check response data
            response = raw_data["response"]
            assert response["markdown"] == "Test markdown"
            assert response["provider"] == "test_provider"
            assert response["model"] == "test_model"
            assert response["duration_seconds"] == 2.5
            assert len(response["citations"]) == 1

            # Check test context
            context = raw_data["test_context"]
            assert context["genes"] == ["TEST"]
            assert context["context"] == "test"

        # Check extracted JSON structure
        with open(output_dir / "extracted_json.json") as f:
            extracted_data = json.load(f)
            assert "context" in extracted_data
            assert "input_genes" in extracted_data
            assert extracted_data["input_genes"] == ["TEST"]


@pytest.mark.unit
def test_output_directory_naming() -> None:
    """Test output directory naming convention."""
    

    with tempfile.TemporaryDirectory() as temp_dir:
        saver = TestOutputSaver(enabled=True, base_dir=temp_dir)

        mock_response = MockResponse()
        output_dir = saver.save_test_output(
            test_name="test_foo_bar",
            test_file="test_integration_example.py",
            raw_response=mock_response,
            test_context={}
        )

        # Check directory structure
        assert output_dir is not None

        # Should be: base_dir/integration/<cleaned_filename>/<testname>_<timestamp>/
        parts = output_dir.parts
        assert "integration" in parts
        assert "integration_example" in str(output_dir)  # test_ removed
        assert "test_foo_bar_" in str(output_dir.name)  # test name with timestamp


@pytest.mark.unit
def test_validation_result_saving() -> None:
    """Test saving validation results."""
    

    with tempfile.TemporaryDirectory() as temp_dir:
        saver = TestOutputSaver(enabled=True, base_dir=temp_dir)

        mock_response = MockResponse()
        validation_result = {
            "success": True,
            "retry_count": 0,
            "validation_time_ms": 125.5,
            "error": None
        }

        output_dir = saver.save_test_output(
            test_name="test_validation",
            test_file="test_pydantic.py",
            raw_response=mock_response,
            validation_result=validation_result,
            test_context={"genes": ["GENE1"]}
        )

        # Verify validation result file
        validation_file = output_dir / "validation_result.json"
        assert validation_file.exists()

        with open(validation_file) as f:
            saved_validation = json.load(f)
            assert saved_validation["success"] is True
            assert saved_validation["retry_count"] == 0
            assert saved_validation["validation_time_ms"] == 125.5
            assert saved_validation["error"] is None


@pytest.mark.unit
def test_multiple_test_outputs_different_directories() -> None:
    """Test that multiple test outputs go to different directories."""
    
    import time

    with tempfile.TemporaryDirectory() as temp_dir:
        saver = TestOutputSaver(enabled=True, base_dir=temp_dir)

        mock_response = MockResponse()

        # Save first output
        output_dir1 = saver.save_test_output(
            test_name="test_one",
            test_file="test_example.py",
            raw_response=mock_response,
            test_context={}
        )

        # Small delay to ensure different timestamps
        time.sleep(1)

        # Save second output
        output_dir2 = saver.save_test_output(
            test_name="test_two",
            test_file="test_example.py",
            raw_response=mock_response,
            test_context={}
        )

        # Directories should be different
        assert output_dir1 != output_dir2
        assert output_dir1.exists()
        assert output_dir2.exists()
        assert "test_one" in str(output_dir1)
        assert "test_two" in str(output_dir2)


@pytest.mark.unit
def test_response_without_citations() -> None:
    """Test handling responses without citations attribute."""
    

    with tempfile.TemporaryDirectory() as temp_dir:
        saver = TestOutputSaver(enabled=True, base_dir=temp_dir)

        # Mock response without citations
        class MinimalResponse:
            def __init__(self):
                self.markdown = "Minimal response"
                self.provider = "test"

        minimal_response = MinimalResponse()

        output_dir = saver.save_test_output(
            test_name="test_minimal",
            test_file="test_minimal.py",
            raw_response=minimal_response,
            test_context={}
        )

        # Should still save successfully
        assert output_dir is not None
        assert (output_dir / "raw_response.json").exists()

        with open(output_dir / "raw_response.json") as f:
            raw_data = json.load(f)
            # Citations should default to empty list
            assert raw_data["response"]["citations"] == []


@pytest.mark.unit
def test_output_with_all_components() -> None:
    """Test saving output with all components (raw, extracted, validation)."""
    

    with tempfile.TemporaryDirectory() as temp_dir:
        saver = TestOutputSaver(enabled=True, base_dir=temp_dir)

        mock_response = MockResponse()
        extracted_json = {"context": {}, "input_genes": ["GENE1"], "programs": []}
        validation_result = {"success": True, "retry_count": 1}

        output_dir = saver.save_test_output(
            test_name="test_complete",
            test_file="test_e2e.py",
            raw_response=mock_response,
            extracted_json=extracted_json,
            validation_result=validation_result,
            test_context={"genes": ["GENE1"], "context": "cells", "preset": "test-preset"}
        )

        # Verify all three files exist
        assert (output_dir / "raw_response.json").exists()
        assert (output_dir / "extracted_json.json").exists()
        assert (output_dir / "validation_result.json").exists()

        # Verify test context is complete
        with open(output_dir / "raw_response.json") as f:
            raw_data = json.load(f)
            context = raw_data["test_context"]
            assert context["genes"] == ["GENE1"]
            assert context["context"] == "cells"
            assert context["preset"] == "test-preset"
