"""Unit tests for embeddings similarity functions."""

from __future__ import annotations

import pytest


@pytest.mark.unit
def test_compute_cosine_similarity_identical() -> None:
    """Cosine similarity = 1.0 for identical vectors."""
    from langpa_validation_tools.embeddings.similarity import compute_cosine_similarity

    vec_a = [1.0, 0.0, 0.0]
    vec_b = [1.0, 0.0, 0.0]
    sim = compute_cosine_similarity(vec_a, vec_b)
    assert sim == 1.0


@pytest.mark.unit
def test_compute_cosine_similarity_orthogonal() -> None:
    """Cosine similarity = 0.0 for orthogonal vectors."""
    from langpa_validation_tools.embeddings.similarity import compute_cosine_similarity

    vec_a = [1.0, 0.0, 0.0]
    vec_b = [0.0, 1.0, 0.0]
    sim = compute_cosine_similarity(vec_a, vec_b)
    assert sim == 0.0


@pytest.mark.unit
def test_compute_cosine_similarity_opposite() -> None:
    """Cosine similarity = -1.0 for opposite vectors."""
    from langpa_validation_tools.embeddings.similarity import compute_cosine_similarity

    vec_a = [1.0, 0.0, 0.0]
    vec_b = [-1.0, 0.0, 0.0]
    sim = compute_cosine_similarity(vec_a, vec_b)
    assert sim == -1.0


@pytest.mark.unit
def test_compute_cosine_similarity_different_lengths() -> None:
    """Cosine similarity raises error for vectors of different lengths."""
    from langpa_validation_tools.embeddings.similarity import compute_cosine_similarity

    vec_a = [1.0, 0.0, 0.0]
    vec_b = [1.0, 0.0]

    with pytest.raises(ValueError, match="same length"):
        compute_cosine_similarity(vec_a, vec_b)


@pytest.mark.unit
def test_compute_cosine_similarity_zero_vector() -> None:
    """Cosine similarity = 0.0 when one vector is zero."""
    from langpa_validation_tools.embeddings.similarity import compute_cosine_similarity

    vec_a = [1.0, 2.0, 3.0]
    vec_b = [0.0, 0.0, 0.0]
    sim = compute_cosine_similarity(vec_a, vec_b)
    assert sim == 0.0


@pytest.mark.unit
def test_rescale_similarity() -> None:
    """Rescale similarity from [-1, 1] to [0, 1]."""
    from langpa_validation_tools.embeddings.similarity import rescale_similarity

    assert rescale_similarity(-1.0) == 0.0
    assert rescale_similarity(0.0) == 0.5
    assert rescale_similarity(1.0) == 1.0
    assert rescale_similarity(0.5) == 0.75
    assert rescale_similarity(-0.5) == 0.25
