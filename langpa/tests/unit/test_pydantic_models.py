"""Unit tests for pydantic model generation from JSON Schema.

Tests the dynamic generation of pydantic models from JSON Schema files
using cellsem_llm_client's SchemaManager.
"""

from __future__ import annotations

import pytest
from pydantic import BaseModel


@pytest.mark.unit
def test_get_deepsearch_pydantic_model() -> None:
    """Test generating pydantic model from deepsearch schema."""
    from langpa.services.pydantic_models import get_deepsearch_pydantic_model

    model = get_deepsearch_pydantic_model()

    # Verify it's a valid pydantic model
    assert issubclass(model, BaseModel)

    # Verify required fields exist
    assert "context" in model.model_fields
    assert "input_genes" in model.model_fields
    assert "programs" in model.model_fields
    assert "version" in model.model_fields


@pytest.mark.unit
def test_model_caching() -> None:
    """Test that model generation is cached for performance."""
    from langpa.services.pydantic_models import get_deepsearch_pydantic_model

    # Get model twice
    model1 = get_deepsearch_pydantic_model()
    model2 = get_deepsearch_pydantic_model()

    # Should return same cached instance
    assert model1 is model2


@pytest.mark.unit
def test_nested_definitions_handling() -> None:
    """Test that $ref definitions (citation, atomic_term) are resolved.

    Note: cellsem_llm_client's SchemaManager uses a basic implementation
    that creates dicts for nested objects rather than nested pydantic models.
    This is acceptable for our validation use case.
    """
    from langpa.services.pydantic_models import get_deepsearch_pydantic_model

    model = get_deepsearch_pydantic_model()

    # Create minimal valid instance
    minimal_data = {
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

    # Should instantiate without errors
    instance = model(**minimal_data)

    # Verify nested structures (as dicts due to SchemaManager's basic implementation)
    assert instance.programs[0]["citations"][0]["source_id"] == "1"
    assert instance.input_genes[0] == "TMEM14E"


@pytest.mark.unit
def test_schema_manager_initialization() -> None:
    """Test that SchemaManager is properly initialized with schema directory."""
    from langpa.services.pydantic_models import get_schema_manager

    manager = get_schema_manager()

    # Should be a SchemaManager instance
    assert manager is not None
    assert hasattr(manager, "get_pydantic_model")


@pytest.mark.unit
def test_model_with_optional_fields() -> None:
    """Test model handles optional fields correctly."""
    from langpa.services.pydantic_models import get_deepsearch_pydantic_model

    model = get_deepsearch_pydantic_model()

    # Create instance with only required fields
    minimal_data = {
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

    instance = model(**minimal_data)

    # Verify required fields present (context is dict due to SchemaManager's basic implementation)
    assert instance.context["cell_type"] == "cells"
    assert len(instance.programs) == 1


@pytest.mark.unit
def test_model_validation_errors() -> None:
    """Test that model properly validates and raises errors for invalid data."""
    from langpa.services.pydantic_models import get_deepsearch_pydantic_model
    from pydantic import ValidationError

    model = get_deepsearch_pydantic_model()

    # Missing required field
    invalid_data = {
        "context": {"cell_type": "cells", "disease": "test"},
        # Missing input_genes, programs, version
    }

    with pytest.raises(ValidationError) as exc_info:
        model(**invalid_data)

    # Should mention missing required fields
    assert "input_genes" in str(exc_info.value) or "required" in str(exc_info.value).lower()
