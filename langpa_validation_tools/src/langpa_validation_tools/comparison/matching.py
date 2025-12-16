"""Program matching algorithms."""

from __future__ import annotations

from typing import Any

from langpa_validation_tools.comparison.metrics import (
    compute_combined_similarity,
    compute_gene_jaccard,
    compute_name_similarity,
)
from langpa_validation_tools.comparison.models import ProgramPair, SimilarityScores


def match_programs(
    programs_a: list[dict[str, Any]],
    programs_b: list[dict[str, Any]],
    threshold: float = 0.3,
    return_unmatched: bool = False,
) -> list[ProgramPair] | tuple[list[ProgramPair], list[dict], list[dict]]:
    """Match programs between two runs using greedy algorithm.

    Args:
        programs_a: Programs from first run
        programs_b: Programs from second run
        threshold: Minimum combined similarity to consider a match
        return_unmatched: Return unmatched programs if True

    Returns:
        List of ProgramPair objects (or tuple with unmatched if requested)

    .. code-block:: python

        matches = match_programs(run1_programs, run2_programs, threshold=0.5)
        for match in matches:
            print(f"{match.program_a['program_name']} -> {match.scores.combined}")
    """
    # Calculate all similarities
    candidates = []
    for i, prog_a in enumerate(programs_a):
        for j, prog_b in enumerate(programs_b):
            genes_a = prog_a["supporting_genes"]
            genes_b = prog_b["supporting_genes"]
            overlap_count = len(set(genes_a) & set(genes_b))
            gene_jac = compute_gene_jaccard(genes_a, genes_b)
            name_sim = compute_name_similarity(
                prog_a["program_name"],
                prog_b["program_name"]
            )
            combined = compute_combined_similarity(gene_jac, name_sim)

            if combined >= threshold:
                candidates.append((i, j, gene_jac, name_sim, combined, overlap_count))

    # Sort by combined similarity (descending)
    candidates.sort(key=lambda x: x[4], reverse=True)

    # Greedy matching
    matched_a = set()
    matched_b = set()
    matches = []

    for i, j, gene_jac, name_sim, combined, overlap_count in candidates:
        if i not in matched_a and j not in matched_b:
            matches.append(
                ProgramPair(
                    program_a=programs_a[i],
                    program_b=programs_b[j],
                    scores=SimilarityScores(
                        gene_jaccard=gene_jac,
                        name_similarity=name_sim,
                        combined=combined,
                        overlap_count=overlap_count,
                    )
                )
            )
            matched_a.add(i)
            matched_b.add(j)

    if return_unmatched:
        unmatched_a = [p for i, p in enumerate(programs_a) if i not in matched_a]
        unmatched_b = [p for i, p in enumerate(programs_b) if i not in matched_b]
        return matches, unmatched_a, unmatched_b

    return matches
