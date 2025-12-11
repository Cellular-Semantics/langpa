"""Embeddings support for semantic similarity."""

from langpa_validation_tools.embeddings.cache import load_embeddings, save_embeddings
from langpa_validation_tools.embeddings.generator import EmbeddingGenerator
from langpa_validation_tools.embeddings.similarity import compute_cosine_similarity, rescale_similarity

__all__ = [
    "EmbeddingGenerator",
    "compute_cosine_similarity",
    "rescale_similarity",
    "save_embeddings",
    "load_embeddings",
]
