"""Unit tests for comparison matching algorithm."""

from __future__ import annotations

import pytest


@pytest.mark.unit
def test_match_programs_greedy() -> None:
    """Greedy matching selects highest similarity pairs first."""
    from langpa_validation_tools.comparison.matching import match_programs

    programs_a = [
        {"program_name": "P1", "supporting_genes": ["TP53", "BRCA1"]},
        {"program_name": "P2", "supporting_genes": ["EGFR"]},
    ]
    programs_b = [
        {"program_name": "P1_similar", "supporting_genes": ["TP53", "BRCA1", "MYC"]},
        {"program_name": "P2_similar", "supporting_genes": ["EGFR", "KRAS"]},
    ]

    matches = match_programs(programs_a, programs_b)

    assert len(matches) == 2
    assert matches[0].program_a["program_name"] == "P1"
    assert matches[0].program_b["program_name"] == "P1_similar"
    assert matches[0].scores.gene_jaccard > 0.5


@pytest.mark.unit
def test_match_programs_unmatched() -> None:
    """Unmatched programs are returned separately."""
    from langpa_validation_tools.comparison.matching import match_programs

    programs_a = [
        {"program_name": "P1", "supporting_genes": ["TP53"]},
        {"program_name": "P2", "supporting_genes": ["BRCA1"]},
    ]
    programs_b = [
        {"program_name": "P1_similar", "supporting_genes": ["TP53"]},
        # P2 has no match
    ]

    matches, unmatched_a, unmatched_b = match_programs(
        programs_a, programs_b, return_unmatched=True
    )

    assert len(matches) == 1
    assert len(unmatched_a) == 1
    assert unmatched_a[0]["program_name"] == "P2"
    assert len(unmatched_b) == 0


@pytest.mark.unit
def test_match_programs_threshold() -> None:
    """Programs below threshold are not matched."""
    from langpa_validation_tools.comparison.matching import match_programs

    programs_a = [
        {"program_name": "DNA Repair", "supporting_genes": ["TP53", "BRCA1"]},
    ]
    programs_b = [
        {"program_name": "Cell Cycle", "supporting_genes": ["EGFR", "MYC"]},
    ]

    # Default threshold should exclude this match (low similarity)
    matches = match_programs(programs_a, programs_b, threshold=0.5)
    assert len(matches) == 0

    # Lower threshold should include it
    matches = match_programs(programs_a, programs_b, threshold=0.0)
    assert len(matches) == 1


@pytest.mark.unit
def test_match_programs_empty() -> None:
    """Matching handles empty program lists."""
    from langpa_validation_tools.comparison.matching import match_programs

    programs_a = []
    programs_b = [{"program_name": "P1", "supporting_genes": ["TP53"]}]

    matches = match_programs(programs_a, programs_b)
    assert len(matches) == 0

    matches, unmatched_a, unmatched_b = match_programs(
        programs_a, programs_b, return_unmatched=True
    )
    assert len(matches) == 0
    assert len(unmatched_a) == 0
    assert len(unmatched_b) == 1
