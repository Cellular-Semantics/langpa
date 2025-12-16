"""Run comparison functionality for DeepSearch outputs.

This module orchestrates the comparison of gene programs across multiple
DeepSearch runs, generating similarity metrics and CSV outputs.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from langpa.services.output_manager import OutputManager
from langpa_validation_tools.comparison import match_programs


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
    and generates a DataFrame with similarity metrics.

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
            "combined_similarity"
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

                # Match programs
                matches = match_programs(
                    programs_a,
                    programs_b,
                    threshold=threshold,
                    return_unmatched=False
                )

                # Convert matches to DataFrame rows
                for match in matches:
                    genes_a = match.program_a["supporting_genes"]
                    genes_b = match.program_b["supporting_genes"]
                    overlap_count = len(set(genes_a) & set(genes_b))

                    all_matches.append({
                        "query": query_name,
                        "run_a": run_a,
                        "run_b": run_b,
                        "program_a": match.program_a["program_name"],
                        "program_b": match.program_b["program_name"],
                        "gene_jaccard": match.scores.gene_jaccard,
                        "name_similarity": match.scores.name_similarity,
                        "combined_similarity": match.scores.combined,
                        "overlap_count": overlap_count,
                        "genes_a_count": len(genes_a),
                        "genes_b_count": len(genes_b),
                    })

    # Create DataFrame
    df = pd.DataFrame(all_matches)

    # Save CSV files if requested
    if save_csv and csv_output_dir:
        csv_output_dir.mkdir(parents=True, exist_ok=True)

        # Save matches
        matches_path = csv_output_dir / "program_matches.csv"
        df.to_csv(matches_path, index=False)

        # For unmatched programs, we need to track which programs were matched
        # For now, create an empty unmatched file
        # TODO: Implement proper unmatched tracking in future iteration
        unmatched_path = csv_output_dir / "unmatched_programs.csv"
        unmatched_df = pd.DataFrame(columns=["query", "run", "program_name"])
        unmatched_df.to_csv(unmatched_path, index=False)

    return df
