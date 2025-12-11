"""Unit tests for embeddings generator."""

from __future__ import annotations

import pytest


@pytest.mark.unit
def test_embeddings_generator_initialization() -> None:
    """EmbeddingGenerator can be initialized."""
    from langpa_validation_tools.embeddings.generator import EmbeddingGenerator

    gen = EmbeddingGenerator()
    assert gen.model == "text-embedding-3-large"

    gen_custom = EmbeddingGenerator(model="text-embedding-3-small")
    assert gen_custom.model == "text-embedding-3-small"


@pytest.mark.unit
def test_embeddings_generator_lazy_client() -> None:
    """OpenAI client is lazy-loaded."""
    from langpa_validation_tools.embeddings.generator import EmbeddingGenerator

    gen = EmbeddingGenerator()
    assert gen._client is None  # Not initialized yet
