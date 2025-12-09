"""Unit tests for DeepSearchValidator with retry logic.

Tests the validator wrapper that uses cellsem_llm_client's SchemaValidator
for pydantic validation with intelligent retry logic.
"""

from __future__ import annotations

import json

import pytest


@pytest.mark.unit
def test_validate_markdown_success() -> None:
    """Test validating markdown with embedded JSON."""
    from langpa.services.deepsearch_validator import DeepSearchValidator

    validator = DeepSearchValidator()

    # Valid markdown with JSON
    markdown = '''
<think>Analyzing genes...</think>

```json
{
    "context": {
        "cell_type": "cells",
        "disease": "test disease"
    },
    "input_genes": ["TMEM14E"],
    "programs": [
        {
            "program_name": "Test Program",
            "description": "Test description",
            "predicted_cellular_impact": ["test impact"],
            "evidence_summary": "test evidence",
            "significance_score": 0.5,
            "citations": [{"source_id": "1"}],
            "supporting_genes": ["TMEM14E"]
        }
    ],
    "version": "1.0"
}
```
    '''

    result = validator.validate_markdown(markdown)

    assert result.success is True
    assert result.model_instance is not None
    assert result.retry_count == 0
    assert result.validation_time_ms > 0


@pytest.mark.unit
def test_validate_json_dict_success() -> None:
    """Test validating pre-extracted JSON dict."""
    from langpa.services.deepsearch_validator import DeepSearchValidator

    validator = DeepSearchValidator()

    valid_data = {
        "context": {
            "cell_type": "cells",
            "disease": "test"
        },
        "input_genes": ["TMEM14E"],
        "programs": [
            {
                "program_name": "Test",
                "description": "Test",
                "predicted_cellular_impact": ["impact"],
                "evidence_summary": "evidence",
                "significance_score": 0.5,
                "citations": [{"source_id": "1"}],
                "supporting_genes": ["TMEM14E"]
            }
        ],
        "version": "1.0"
    }

    result = validator.validate_json_dict(valid_data)

    assert result.success is True
    assert result.model_instance is not None
    assert result.error is None


@pytest.mark.unit
def test_validate_markdown_extraction_failure() -> None:
    """Test handling when JSON extraction fails."""
    from langpa.services.deepsearch_validator import DeepSearchValidator

    validator = DeepSearchValidator()

    # Markdown with no JSON
    markdown = "This is just text with no JSON content"

    result = validator.validate_markdown(markdown)

    assert result.success is False
    assert result.error is not None
    assert "Failed to extract JSON" in str(result.error)


@pytest.mark.unit
def test_validate_invalid_json() -> None:
    """Test validation with invalid JSON structure."""
    from langpa.services.deepsearch_validator import DeepSearchValidator

    validator = DeepSearchValidator()

    # Missing required fields
    invalid_data = {
        "context": {"cell_type": "cells", "disease": "test"}
        # Missing input_genes, programs, version
    }

    result = validator.validate_json_dict(invalid_data, max_retries=1)

    assert result.success is False
    assert result.error is not None


@pytest.mark.unit
def test_validator_initialization() -> None:
    """Test that validator initializes correctly."""
    from langpa.services.deepsearch_validator import DeepSearchValidator

    validator = DeepSearchValidator()

    assert validator is not None
    assert hasattr(validator, "validate_markdown")
    assert hasattr(validator, "validate_json_dict")
    assert validator.schema_validator is not None


@pytest.mark.unit
def test_validate_markdown_with_schema_field() -> None:
    """Test that $schema field is stripped during validation.

    The $schema field in JSON responses causes validation failures
    and should be automatically removed.
    """
    from langpa.services.deepsearch_validator import DeepSearchValidator

    validator = DeepSearchValidator()

    # JSON with $schema field (common LLM mistake)
    markdown = '''
```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "context": {
        "cell_type": "cells",
        "disease": "test"
    },
    "input_genes": ["TMEM14E"],
    "programs": [
        {
            "program_name": "Test",
            "description": "Test",
            "predicted_cellular_impact": ["impact"],
            "evidence_summary": "evidence",
            "significance_score": 0.5,
            "citations": [{"source_id": "1"}],
            "supporting_genes": ["TMEM14E"]
        }
    ],
    "version": "1.0"
}
```
    '''

    result = validator.validate_markdown(markdown)

    # Should succeed - OutputManager.extract_json_from_markdown removes $schema
    assert result.success is True


@pytest.mark.unit
def test_validate_with_max_retries() -> None:
    """Test that max_retries parameter is respected."""
    from langpa.services.deepsearch_validator import DeepSearchValidator

    validator = DeepSearchValidator()

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

    # Valid data should succeed on first try regardless of max_retries
    result = validator.validate_json_dict(valid_data, max_retries=5)

    assert result.success is True
    assert result.retry_count == 0  # No retries needed for valid data
