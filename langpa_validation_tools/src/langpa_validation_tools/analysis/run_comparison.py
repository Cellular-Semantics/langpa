"""Run comparison functionality for DeepSearch outputs.

This module orchestrates the comparison of gene programs across multiple
DeepSearch runs, generating similarity metrics and CSV outputs.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from langpa.services.output_manager import OutputManager
from langpa_validation_tools.comparison.metrics import (
    compute_combined_similarity,
    compute_gene_jaccard,
    compute_name_similarity,
)


def compare_runs(
    project: str,
    output_dir: Path = Path("outputs"),
    threshold: float = 0.3,
    embeddings_path: Path | None = None,
    save_csv: bool = False,
    csv_output_dir: Path | None = None,
) -> pd.DataFrame:
    """Compare all DeepSearch runs in a project.

    Loads all container files for the project, compares programs across runs,
    and generates a **full pairwise similarity matrix** (not just matched
    pairs). A boolean ``is_match`` column flags rows whose combined similarity
    meets or exceeds ``threshold``; bubble plots can then render the complete
    matrix while reports can still filter to matches.

    Args:
        project: Project name (directory under output_dir)
        output_dir: Base output directory containing project folders
        threshold: Minimum similarity threshold for matching (default: 0.3)
        embeddings_path: Path to pre-generated embeddings (optional)
        save_csv: Whether to save results to CSV files (default: False)
        csv_output_dir: Directory to save CSV files (default: output_dir/project/analysis)

    Returns:
        pandas DataFrame with columns:
            - query: Query name
            - run_a: Run A identifier
            - run_b: Run B identifier
            - program_a: Program A name
            - program_b: Program B name
            - gene_jaccard: Gene Jaccard similarity
            - name_similarity: Program name similarity
            - combined_similarity: Combined similarity score
            - overlap_count: Number of shared genes
            - genes_a_count / genes_b_count: Gene counts per program
            - is_match: True if combined_similarity >= threshold

    .. code-block:: python

        from pathlib import Path
        from langpa_validation_tools.analysis import compare_runs

        # Compare all runs in a project
        df = compare_runs(
            project="glioblastoma_ds_auto",
            output_dir=Path("outputs"),
            threshold=0.3
        )

        # Save results to CSV
        df = compare_runs(
            project="glioblastoma_ds_auto",
            save_csv=True,
            csv_output_dir=Path("outputs/glioblastoma_ds_auto/analysis")
        )
    """
    manager = OutputManager(output_dir=str(output_dir))

    # Get all container files for the project
    container_paths = manager.list_container_files(project)

    if not container_paths:
        # Return empty DataFrame with correct columns
        return pd.DataFrame(columns=[
            "query",
            "run_a",
            "run_b",
            "program_a",
            "program_b",
            "gene_jaccard",
            "name_similarity",
            "combined_similarity",
            "overlap_count",
            "genes_a_count",
            "genes_b_count",
            "is_match",
        ])

    # Group containers by query
    containers_by_query: dict[str, list[tuple[Path, dict[str, Any]]]] = {}

    for container_path in container_paths:
        # Extract query name from path
        # Expected: output_dir/project/query/run/deepsearch_container.json
        parts = container_path.parts
        try:
            # Find project index
            project_idx = parts.index(project)
            query_name = parts[project_idx + 1]
            run_name = parts[project_idx + 2]
        except (ValueError, IndexError):
            # Skip if path structure doesn't match
            continue

        # Load container
        container_data = manager.load_container(container_path)

        if query_name not in containers_by_query:
            containers_by_query[query_name] = []

        containers_by_query[query_name].append((container_path, container_data))

    # Compare runs within each query
    columns = [
        "query",
        "run_a",
        "run_b",
        "program_a",
        "program_b",
        "gene_jaccard",
        "name_similarity",
        "combined_similarity",
        "overlap_count",
        "genes_a_count",
        "genes_b_count",
        "is_match",
    ]

    all_matches = []

    for query_name, containers in containers_by_query.items():
        # Need at least 2 runs to compare
        if len(containers) < 2:
            continue

        # Compare each pair of runs
        for i in range(len(containers)):
            for j in range(i + 1, len(containers)):
                path_a, data_a = containers[i]
                path_b, data_b = containers[j]

                # Extract run names
                run_a = path_a.parts[-2]  # Parent directory name
                run_b = path_b.parts[-2]

                # Get programs
                programs_a = data_a.get("report", {}).get("programs", [])
                programs_b = data_b.get("report", {}).get("programs", [])

                if not programs_a or not programs_b:
                    continue

                # Full pairwise similarity matrix (no greedy matching)
                for prog_a in programs_a:
                    for prog_b in programs_b:
                        genes_a = prog_a.get("supporting_genes", [])
                        genes_b = prog_b.get("supporting_genes", [])

                        overlap_count = len(set(genes_a) & set(genes_b))
                        gene_jac = compute_gene_jaccard(genes_a, genes_b)
                        name_sim = compute_name_similarity(
                            prog_a.get("program_name", ""),
                            prog_b.get("program_name", "")
                        )
                        combined = compute_combined_similarity(gene_jac, name_sim)

                        all_matches.append({
                            "query": query_name,
                            "run_a": run_a,
                            "run_b": run_b,
                            "program_a": prog_a.get("program_name", "N/A"),
                            "program_b": prog_b.get("program_name", "N/A"),
                            "gene_jaccard": gene_jac,
                            "name_similarity": name_sim,
                            "combined_similarity": combined,
                            "overlap_count": overlap_count,
                            "genes_a_count": len(genes_a),
                            "genes_b_count": len(genes_b),
                            "is_match": combined >= threshold,
                        })

    # Create DataFrame
    df = pd.DataFrame(all_matches, columns=columns)

    # Save CSV files if requested
    if save_csv and csv_output_dir:
        csv_output_dir.mkdir(parents=True, exist_ok=True)

        # Save full pairwise matrix (still called program_matches for compatibility)
        matches_path = csv_output_dir / "program_matches.csv"
        df.to_csv(matches_path, index=False)

        # Track programs with no matches above threshold (per run)
        unmatched_records: list[dict[str, str]] = []
        if not df.empty:
            # Programs from run_a perspective
            for (query, run, program), has_match in (
                df.groupby(["query", "run_a", "program_a"])["is_match"].any().items()
            ):
                if not has_match:
                    unmatched_records.append(
                        {"query": query, "run": run, "program_name": program}
                    )
            # Programs from run_b perspective
            for (query, run, program), has_match in (
                df.groupby(["query", "run_b", "program_b"])["is_match"].any().items()
            ):
                if not has_match:
                    unmatched_records.append(
                        {"query": query, "run": run, "program_name": program}
                    )

        unmatched_path = csv_output_dir / "unmatched_programs.csv"
        unmatched_df = pd.DataFrame(unmatched_records or [], columns=["query", "run", "program_name"])
        unmatched_df.to_csv(unmatched_path, index=False)

    return df
