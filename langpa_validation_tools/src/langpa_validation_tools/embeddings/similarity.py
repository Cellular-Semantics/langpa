"""Similarity functions for embeddings."""

from __future__ import annotations

import math


def compute_cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """Calculate cosine similarity between two vectors.

    Args:
        vec_a: First embedding vector
        vec_b: Second embedding vector

    Returns:
        Cosine similarity (-1.0 to 1.0)

    Raises:
        ValueError: If vectors have different lengths

    .. code-block:: python

        from langpa.embeddings.similarity import compute_cosine_similarity

        vec_a = [1.0, 0.0, 0.0]
        vec_b = [1.0, 0.0, 0.0]
        sim = compute_cosine_similarity(vec_a, vec_b)
        # Returns: 1.0
    """
    if len(vec_a) != len(vec_b):
        raise ValueError("Vectors must have same length")

    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    magnitude_a = math.sqrt(sum(a * a for a in vec_a))
    magnitude_b = math.sqrt(sum(b * b for b in vec_b))

    if magnitude_a == 0.0 or magnitude_b == 0.0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def rescale_similarity(similarity: float) -> float:
    """Rescale similarity from [-1, 1] to [0, 1].

    Args:
        similarity: Cosine similarity in [-1, 1]

    Returns:
        Rescaled similarity in [0, 1]

    .. code-block:: python

        from langpa.embeddings.similarity import rescale_similarity

        rescaled = rescale_similarity(0.5)
        # Returns: 0.75
    """
    return (similarity + 1.0) / 2.0
