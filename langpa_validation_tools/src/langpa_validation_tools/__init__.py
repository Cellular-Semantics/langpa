"""Validation and comparison tools for LangPA outputs."""

from langpa_validation_tools.comparison import (
    ProgramPair,
    SimilarityScores,
    compute_combined_similarity,
    compute_gene_jaccard,
    compute_name_similarity,
    match_programs,
)
from langpa_validation_tools.embeddings import (
    EmbeddingGenerator,
    compute_cosine_similarity,
    load_embeddings,
    rescale_similarity,
    save_embeddings,
)

__all__ = [
    # Comparison
    "SimilarityScores",
    "ProgramPair",
    "compute_gene_jaccard",
    "compute_name_similarity",
    "compute_combined_similarity",
    "match_programs",
    # Embeddings
    "EmbeddingGenerator",
    "compute_cosine_similarity",
    "rescale_similarity",
    "save_embeddings",
    "load_embeddings",
]
