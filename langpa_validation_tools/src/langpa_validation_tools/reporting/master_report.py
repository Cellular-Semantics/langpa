"""Master validation report generation.

This module creates comprehensive markdown reports aggregating comparison
results across all queries in a DeepSearch project.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from langpa.services.output_manager import OutputManager


def build_master_report(
    project: str,
    matches_df: pd.DataFrame,
    output_path: Path | str,
    output_dir: Path = Path("outputs"),
    include_plots: bool = True,
    plot_dir: Path | None = None,
) -> None:
    """Generate master validation report for a project.

    Creates a comprehensive markdown report with:
    - Per-query comparison tables
    - Links to bubble plots (if available)
    - Links to individual run markdown reports
    - Summary statistics

    Args:
        project: Project name
        matches_df: DataFrame from compare_runs() with program matches
        output_path: Path to save markdown report
        output_dir: Base output directory (default: outputs/)
        include_plots: Whether to include bubble plot references (default: True)
        plot_dir: Directory containing plots (default: output_dir/project/analysis/heatmaps)

    .. code-block:: python

        from langpa_validation_tools.reporting import build_master_report
        from langpa_validation_tools.analysis import compare_runs
        import pandas as pd

        # Generate comparison
        matches_df = compare_runs("my_project")

        # Build master report
        build_master_report(
            project="my_project",
            matches_df=matches_df,
            output_path="validation_report.md"
        )
    """
    output_path = Path(output_path)
    manager = OutputManager(output_dir=str(output_dir))

    # Determine plot directory
    if plot_dir is None:
        plot_dir = output_dir / project / "analysis" / "heatmaps"

    # Start building report
    lines = [
        f"# Validation Report: {project}",
        "",
        "Master validation report comparing all DeepSearch runs across queries.",
        "",
        "## Summary",
        "",
    ]

    # Add summary statistics
    total_matches = len(matches_df)
    queries = matches_df["query"].unique() if "query" in matches_df.columns else []
    num_queries = len(queries)

    lines.extend([
        f"- **Total Matches**: {total_matches}",
        f"- **Queries**: {num_queries}",
        "",
    ])

    if total_matches > 0:
        avg_gene_jaccard = matches_df["gene_jaccard"].mean()
        avg_name_sim = matches_df["name_similarity"].mean()
        avg_combined = matches_df["combined_similarity"].mean()

        lines.extend([
            f"- **Average Gene Jaccard**: {avg_gene_jaccard:.3f}",
            f"- **Average Name Similarity**: {avg_name_sim:.3f}",
            f"- **Average Combined Similarity**: {avg_combined:.3f}",
            "",
        ])

    # Per-query sections
    if "query" in matches_df.columns and num_queries > 0:
        lines.append("## Per-Query Analysis")
        lines.append("")

        for query in sorted(queries):
            query_matches = matches_df[matches_df["query"] == query]

            lines.extend([
                f"### Query: {query}",
                "",
                f"**Matches**: {len(query_matches)}",
                "",
            ])

            # Comparison table
            if len(query_matches) > 0:
                lines.extend([
                    "#### Comparison Table",
                    "",
                    "| Run A | Run B | Program A | Program B | Gene Jaccard | Name Sim | Combined |",
                    "|-------|-------|-----------|-----------|--------------|----------|----------|",
                ])

                for _, row in query_matches.iterrows():
                    run_a = row.get("run_a", "N/A")
                    run_b = row.get("run_b", "N/A")
                    prog_a = row.get("program_a", "N/A")
                    prog_b = row.get("program_b", "N/A")
                    gene_j = row.get("gene_jaccard", 0.0)
                    name_s = row.get("name_similarity", 0.0)
                    combined = row.get("combined_similarity", 0.0)

                    lines.append(
                        f"| {run_a} | {run_b} | {prog_a} | {prog_b} | "
                        f"{gene_j:.3f} | {name_s:.3f} | {combined:.3f} |"
                    )

                lines.append("")

            # Bubble plot reference
            if include_plots:
                bubble_plot = plot_dir / f"bubble_plot_{query}.png"
                if bubble_plot.exists():
                    # Make path relative to report location
                    rel_path = bubble_plot.relative_to(output_path.parent)
                    lines.extend([
                        "#### Bubble Plot",
                        "",
                        f"![{query} Bubble Plot]({rel_path})",
                        "",
                    ])

            # Individual run reports
            lines.extend([
                "#### Individual Run Reports",
                "",
            ])

            # Find all markdown reports for this query
            query_dir = output_dir / project / query
            if query_dir.exists():
                md_reports = sorted(query_dir.glob("*/deepsearch_*.md"))
                if md_reports:
                    for report_path in md_reports:
                        run_id = report_path.parent.name
                        rel_path = report_path.relative_to(output_path.parent)
                        lines.append(f"- [{run_id}]({rel_path})")
                else:
                    lines.append("- No individual reports found")
            else:
                lines.append("- Query directory not found")

            lines.append("")

    # Write report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines))
