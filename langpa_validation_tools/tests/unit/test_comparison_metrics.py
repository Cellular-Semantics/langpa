"""Unit tests for comparison metrics."""

from __future__ import annotations

import pytest


@pytest.mark.unit
def test_compute_gene_jaccard_identical() -> None:
    """Gene Jaccard = 1.0 for identical gene sets."""
    from langpa_validation_tools.comparison.metrics import compute_gene_jaccard

    genes_a = ["TP53", "BRCA1", "EGFR"]
    genes_b = ["TP53", "BRCA1", "EGFR"]
    jaccard = compute_gene_jaccard(genes_a, genes_b)
    assert jaccard == 1.0


@pytest.mark.unit
def test_compute_gene_jaccard_no_overlap() -> None:
    """Gene Jaccard = 0.0 for disjoint gene sets."""
    from langpa_validation_tools.comparison.metrics import compute_gene_jaccard

    genes_a = ["TP53", "BRCA1"]
    genes_b = ["EGFR", "MYC"]
    jaccard = compute_gene_jaccard(genes_a, genes_b)
    assert jaccard == 0.0


@pytest.mark.unit
def test_compute_gene_jaccard_partial() -> None:
    """Gene Jaccard calculates correctly for partial overlap."""
    from langpa_validation_tools.comparison.metrics import compute_gene_jaccard

    genes_a = ["TP53", "BRCA1", "EGFR"]  # 3 genes
    genes_b = ["TP53", "BRCA1", "MYC"]   # 3 genes, 2 overlap
    # Jaccard = 2 / (3 + 3 - 2) = 2/4 = 0.5
    jaccard = compute_gene_jaccard(genes_a, genes_b)
    assert jaccard == 0.5


@pytest.mark.unit
def test_compute_gene_jaccard_empty() -> None:
    """Gene Jaccard handles empty gene sets."""
    from langpa_validation_tools.comparison.metrics import compute_gene_jaccard

    # Both empty should return 1.0 (identical)
    assert compute_gene_jaccard([], []) == 1.0

    # One empty should return 0.0
    assert compute_gene_jaccard(["TP53"], []) == 0.0
    assert compute_gene_jaccard([], ["TP53"]) == 0.0


@pytest.mark.unit
def test_compute_name_similarity_token_based() -> None:
    """Token-based name similarity uses token overlap."""
    from langpa_validation_tools.comparison.metrics import compute_name_similarity

    name_a = "DNA Repair Program"
    name_b = "DNA Damage Repair"
    sim = compute_name_similarity(name_a, name_b)
    # Tokens: {dna, repair, program} vs {dna, damage, repair}
    # Overlap: {dna, repair} = 2 tokens
    # Union: 4 tokens
    # Jaccard: 2/4 = 0.5
    assert sim == 0.5


@pytest.mark.unit
def test_compute_name_similarity_identical() -> None:
    """Name similarity = 1.0 for identical names."""
    from langpa_validation_tools.comparison.metrics import compute_name_similarity

    name = "DNA Repair"
    sim = compute_name_similarity(name, name)
    assert sim == 1.0


@pytest.mark.unit
def test_compute_name_similarity_no_overlap() -> None:
    """Name similarity = 0.0 for completely different names."""
    from langpa_validation_tools.comparison.metrics import compute_name_similarity

    name_a = "DNA Repair"
    name_b = "Cell Cycle"
    sim = compute_name_similarity(name_a, name_b)
    assert sim == 0.0


@pytest.mark.unit
def test_compute_name_similarity_case_insensitive() -> None:
    """Name similarity is case-insensitive."""
    from langpa_validation_tools.comparison.metrics import compute_name_similarity

    name_a = "DNA REPAIR"
    name_b = "dna repair"
    sim = compute_name_similarity(name_a, name_b)
    assert sim == 1.0


@pytest.mark.unit
def test_compute_name_similarity_empty() -> None:
    """Name similarity handles empty strings."""
    from langpa_validation_tools.comparison.metrics import compute_name_similarity

    # Both empty should return 1.0
    assert compute_name_similarity("", "") == 1.0

    # One empty should return 0.0
    assert compute_name_similarity("DNA Repair", "") == 0.0
    assert compute_name_similarity("", "DNA Repair") == 0.0


@pytest.mark.unit
def test_compute_combined_similarity() -> None:
    """Combined similarity uses weighted average."""
    from langpa_validation_tools.comparison.metrics import compute_combined_similarity

    combined = compute_combined_similarity(
        gene_jaccard=0.8,
        name_similarity=0.6,
        gene_weight=0.7,
        name_weight=0.3
    )
    # 0.8*0.7 + 0.6*0.3 = 0.56 + 0.18 = 0.74
    assert combined == 0.74


@pytest.mark.unit
def test_compute_combined_similarity_default_weights() -> None:
    """Combined similarity uses default weights (0.7, 0.3)."""
    from langpa_validation_tools.comparison.metrics import compute_combined_similarity

    combined = compute_combined_similarity(
        gene_jaccard=0.8,
        name_similarity=0.6
    )
    # Default: 0.8*0.7 + 0.6*0.3 = 0.74
    assert combined == 0.74


@pytest.mark.unit
def test_compute_combined_similarity_equal_weights() -> None:
    """Combined similarity with equal weights."""
    from langpa_validation_tools.comparison.metrics import compute_combined_similarity

    combined = compute_combined_similarity(
        gene_jaccard=0.8,
        name_similarity=0.4,
        gene_weight=0.5,
        name_weight=0.5
    )
    # 0.8*0.5 + 0.4*0.5 = 0.4 + 0.2 = 0.6
    assert abs(combined - 0.6) < 1e-10  # Handle floating point precision
