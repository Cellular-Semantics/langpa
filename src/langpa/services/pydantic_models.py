"""Pydantic model generation from JSON Schema using cellsem_llm_client.

This module provides dynamic generation of pydantic models from JSON Schema
files using cellsem_llm_client's SchemaManager. Models are cached for performance.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pydantic import BaseModel

    from cellsem_llm_client.schema import SchemaManager

# Global singletons for caching
_schema_manager: SchemaManager | None = None
_model_cache: dict[str, type[BaseModel]] = {}


def get_schema_manager() -> SchemaManager:
    """Get or create SchemaManager singleton.

    Returns:
        SchemaManager instance configured with langpa schemas directory

    .. code-block:: python

        manager = get_schema_manager()
        model = manager.get_pydantic_model("deepsearch_results_schema.json")
    """
    global _schema_manager

    if _schema_manager is None:
        from cellsem_llm_client.schema import SchemaManager

        from langpa.schemas import get_schemas_dir

        schemas_dir = get_schemas_dir()
        _schema_manager = SchemaManager(schema_directories=[str(schemas_dir)])

    return _schema_manager


def get_deepsearch_pydantic_model() -> type[BaseModel]:
    """Generate pydantic model from deepsearch_results_schema.json.

    Uses cellsem_llm_client's SchemaManager to dynamically generate a pydantic
    model from the JSON Schema. The model is cached for performance.

    Returns:
        Pydantic model class for deepsearch results validation

    Raises:
        SchemaNotFoundError: If deepsearch_results_schema.json cannot be loaded
        SchemaValidationError: If schema cannot be converted to pydantic model

    .. code-block:: python

        model = get_deepsearch_pydantic_model()
        instance = model(
            context={"cell_type": "neurons", "disease": "test"},
            input_genes=["TMEM14E"],
            programs=[...],
            version="1.0"
        )
    """
    cache_key = "deepsearch"

    if cache_key not in _model_cache:
        manager = get_schema_manager()
        _model_cache[cache_key] = manager.get_pydantic_model(
            "deepsearch_results_schema"  # Without .json extension
        )

    return _model_cache[cache_key]


__all__ = ["get_schema_manager", "get_deepsearch_pydantic_model"]
