"""Unit tests for comparison models."""

from __future__ import annotations

import pytest


@pytest.mark.unit
def test_similarity_scores_model() -> None:
    """Verify SimilarityScores Pydantic model."""
    from langpa_validation_tools.comparison.models import SimilarityScores

    scores = SimilarityScores(
        gene_jaccard=0.85,
        name_similarity=0.92,
        combined=0.885
    )
    assert scores.gene_jaccard == 0.85
    assert scores.name_similarity == 0.92
    assert scores.combined == 0.885
    assert 0.0 <= scores.combined <= 1.0


@pytest.mark.unit
def test_similarity_scores_validation() -> None:
    """Test SimilarityScores validates ranges."""
    from langpa_validation_tools.comparison.models import SimilarityScores
    from pydantic import ValidationError

    # Valid scores
    scores = SimilarityScores(
        gene_jaccard=0.0,
        name_similarity=1.0,
        combined=0.5
    )
    assert scores.gene_jaccard == 0.0
    assert scores.name_similarity == 1.0

    # Invalid score > 1.0
    with pytest.raises(ValidationError):
        SimilarityScores(
            gene_jaccard=1.5,
            name_similarity=0.9,
            combined=1.2
        )

    # Invalid score < 0.0
    with pytest.raises(ValidationError):
        SimilarityScores(
            gene_jaccard=-0.1,
            name_similarity=0.9,
            combined=0.4
        )


@pytest.mark.unit
def test_program_pair_model() -> None:
    """Verify ProgramPair model with programs and scores."""
    from langpa_validation_tools.comparison.models import ProgramPair, SimilarityScores

    pair = ProgramPair(
        program_a={"program_name": "DNA Repair", "supporting_genes": ["TP53"]},
        program_b={"program_name": "DNA Damage", "supporting_genes": ["TP53", "BRCA1"]},
        scores=SimilarityScores(gene_jaccard=0.5, name_similarity=0.9, combined=0.7)
    )
    assert pair.program_a["program_name"] == "DNA Repair"
    assert pair.program_b["program_name"] == "DNA Damage"
    assert pair.scores.combined == 0.7


@pytest.mark.unit
def test_program_pair_requires_fields() -> None:
    """Test ProgramPair validates required program fields."""
    from langpa_validation_tools.comparison.models import ProgramPair, SimilarityScores
    from pydantic import ValidationError

    scores = SimilarityScores(gene_jaccard=0.5, name_similarity=0.9, combined=0.7)

    # Missing program_name
    with pytest.raises(ValidationError, match="program_name"):
        ProgramPair(
            program_a={"supporting_genes": ["TP53"]},
            program_b={"program_name": "P2", "supporting_genes": ["BRCA1"]},
            scores=scores
        )

    # Missing supporting_genes
    with pytest.raises(ValidationError, match="supporting_genes"):
        ProgramPair(
            program_a={"program_name": "P1", "supporting_genes": ["TP53"]},
            program_b={"program_name": "P2"},
            scores=scores
        )
