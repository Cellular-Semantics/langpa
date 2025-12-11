"""Integration tests for embeddings API."""

from __future__ import annotations

import os

import pytest
from dotenv import load_dotenv


@pytest.mark.integration
def test_generate_embedding_real_api() -> None:
    """Generate real embedding via OpenAI API."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        pytest.skip("OPENAI_API_KEY not available")

    from langpa_validation_tools.embeddings.generator import EmbeddingGenerator

    gen = EmbeddingGenerator()
    embedding = gen.generate_embedding("DNA Repair")

    assert isinstance(embedding, list)
    assert len(embedding) == 3072  # text-embedding-3-large dimension
    assert all(isinstance(x, float) for x in embedding)


@pytest.mark.integration
def test_generate_embeddings_batch() -> None:
    """Generate embeddings for multiple texts."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        pytest.skip("OPENAI_API_KEY not available")

    from langpa_validation_tools.embeddings.generator import EmbeddingGenerator

    gen = EmbeddingGenerator()
    texts = ["DNA Repair", "Cell Cycle", "Apoptosis"]
    embeddings = gen.generate_embeddings(texts)

    assert len(embeddings) == 3
    assert all(len(emb) == 3072 for emb in embeddings)
