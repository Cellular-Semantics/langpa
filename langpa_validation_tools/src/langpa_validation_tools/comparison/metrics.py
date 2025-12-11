"""Similarity metrics for comparing gene programs."""

from __future__ import annotations


def compute_gene_jaccard(genes_a: list[str], genes_b: list[str]) -> float:
    """Calculate Jaccard similarity between two gene sets.

    Args:
        genes_a: First gene list
        genes_b: Second gene list

    Returns:
        Jaccard similarity (0.0 to 1.0)

    .. code-block:: python

        jaccard = compute_gene_jaccard(["TP53", "BRCA1"], ["TP53", "EGFR"])
        # Returns: 0.333 (1 overlap / 3 total)
    """
    set_a = set(genes_a)
    set_b = set(genes_b)

    if not set_a and not set_b:
        return 1.0

    intersection = len(set_a & set_b)
    union = len(set_a | set_b)

    return intersection / union if union > 0 else 0.0


def compute_name_similarity(
    name_a: str,
    name_b: str,
    embedding_a: list[float] | None = None,
    embedding_b: list[float] | None = None
) -> float:
    """Calculate similarity between program names.

    Uses token-based Jaccard if embeddings not provided, otherwise cosine similarity.

    Args:
        name_a: First program name
        name_b: Second program name
        embedding_a: Optional embedding vector for name_a
        embedding_b: Optional embedding vector for name_b

    Returns:
        Name similarity (0.0 to 1.0)

    .. code-block:: python

        sim = compute_name_similarity("DNA Repair", "DNA Damage")
        # Returns: 0.5 (token-based Jaccard)
    """
    if embedding_a is not None and embedding_b is not None:
        from langpa_validation_tools.embeddings.similarity import compute_cosine_similarity
        return compute_cosine_similarity(embedding_a, embedding_b)

    # Token-based fallback
    tokens_a = set(name_a.lower().split())
    tokens_b = set(name_b.lower().split())

    if not tokens_a and not tokens_b:
        return 1.0

    intersection = len(tokens_a & tokens_b)
    union = len(tokens_a | tokens_b)

    return intersection / union if union > 0 else 0.0


def compute_combined_similarity(
    gene_jaccard: float,
    name_similarity: float,
    gene_weight: float = 0.7,
    name_weight: float = 0.3
) -> float:
    """Calculate weighted average of gene and name similarities.

    Args:
        gene_jaccard: Gene Jaccard similarity
        name_similarity: Name similarity
        gene_weight: Weight for gene similarity (default 0.7)
        name_weight: Weight for name similarity (default 0.3)

    Returns:
        Combined similarity score (0.0 to 1.0)

    .. code-block:: python

        combined = compute_combined_similarity(
            gene_jaccard=0.8,
            name_similarity=0.6
        )
        # Returns: 0.74 (0.8*0.7 + 0.6*0.3)
    """
    return gene_jaccard * gene_weight + name_similarity * name_weight
