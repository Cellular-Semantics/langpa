"""Unit tests for embeddings cache functionality."""

from __future__ import annotations

import pytest


@pytest.mark.unit
def test_save_and_load_embeddings(tmp_path) -> None:
    """Save embeddings to CSV index + NPY vectors, then load."""
    from langpa_validation_tools.embeddings.cache import load_embeddings, save_embeddings

    embeddings = {
        "DNA Repair": [0.1, 0.2, 0.3],
        "Cell Cycle": [0.4, 0.5, 0.6]
    }

    cache_path = tmp_path / "embeddings"
    save_embeddings(embeddings, cache_path)

    # Verify files created
    assert (cache_path.parent / "embeddings_index.csv").exists()
    assert (cache_path.parent / "embeddings_vectors.npy").exists()

    # Load and verify
    loaded = load_embeddings(cache_path)
    assert loaded["DNA Repair"] == [0.1, 0.2, 0.3]
    assert loaded["Cell Cycle"] == [0.4, 0.5, 0.6]


@pytest.mark.unit
def test_save_embeddings_creates_files(tmp_path) -> None:
    """Verify save_embeddings creates index and vectors files."""
    from langpa_validation_tools.embeddings.cache import save_embeddings

    embeddings = {"Test": [1.0, 2.0]}
    cache_path = tmp_path / "test_cache"

    save_embeddings(embeddings, cache_path)

    index_file = tmp_path / "test_cache_index.csv"
    vectors_file = tmp_path / "test_cache_vectors.npy"

    assert index_file.exists()
    assert vectors_file.exists()


@pytest.mark.unit
def test_load_embeddings_empty(tmp_path) -> None:
    """Load embeddings handles empty cache."""
    from langpa_validation_tools.embeddings.cache import load_embeddings, save_embeddings

    embeddings = {}
    cache_path = tmp_path / "empty_cache"

    save_embeddings(embeddings, cache_path)
    loaded = load_embeddings(cache_path)

    assert loaded == {}
