"""Heatmap and bubble plot generation for program comparisons.

This module provides visualization functions for comparing DeepSearch runs,
including bubble plots for program matches and confusion matrices for embeddings.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform


def generate_bubble_plot(
    matches_df: pd.DataFrame,
    output_path: Path | str,
    query: str | None = None,
    figsize: tuple[int, int] = (12, 8),
    return_fig: bool = False,
) -> None | tuple[Any, Any]:
    """Generate bubble plot visualization of program comparisons.

    Creates a scatter plot where each point represents a program pair (full
    pairwise matrix). The x-axis is the program index from run A, the y-axis is
    the program index from run B. Bubble size represents the number of
    overlapping genes, and color intensity shows the combined similarity score.
    Axes are numbered and annotated with gene counts; a legend maps numbers to
    program names.

    .. code-block:: python

        from langpa_validation_tools.visualization import generate_bubble_plot
        from pathlib import Path
        import pandas as pd

        # Load matches
        df = pd.read_csv("program_matches.csv")

        # Generate bubble plot
        generate_bubble_plot(df, Path("bubble_plot.png"))

        # Filter by query
        generate_bubble_plot(df, Path("query1_plot.png"), query="0_Gliosis")
    Args:
        matches_df: DataFrame with full program comparisons (from compare_runs)
                   Required columns: program_a, program_b, combined_similarity,
                   overlap_count, genes_a_count, genes_b_count
        output_path: Path to save the PNG file
        query: Optional query name to filter results (default: all queries)
        figsize: Figure size as (width, height) tuple (default: (12, 8))
        return_fig: If True, return (fig, ax) without closing (useful for tests)
    """
    output_path = Path(output_path)

    # Filter by query if specified
    if query:
        df = matches_df[matches_df["query"] == query].copy()
    else:
        df = matches_df.copy()

    # Drop pairs with zero overlap (no dot should be shown)
    if "overlap_count" in df:
        df = df[df["overlap_count"] > 0]
    else:
        df = df.copy()
        df["overlap_count"] = 0
        df = df[df["overlap_count"] > 0]

    # Handle empty DataFrame
    if len(df) == 0:
        fig, ax = plt.subplots(figsize=figsize)
        ax.text(
            0.5, 0.5,
            "No overlaps to display",
            ha="center", va="center",
            fontsize=14,
            color="gray"
        )
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel("Programs (Run A)")
        ax.set_ylabel("Programs (Run B)")
        ax.set_title("Program Matches Bubble Plot")
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches="tight")
        if not return_fig:
            plt.close()
        else:
            return fig, ax  # type: ignore[return-value]
        return

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)

    # Build program index mappings with gene counts
    run_a_programs: dict[str, tuple[int, int]] = {}
    run_b_programs: dict[str, tuple[int, int]] = {}

    genes_a_counts = df["genes_a_count"] if "genes_a_count" in df else pd.Series([0] * len(df))
    genes_b_counts = df["genes_b_count"] if "genes_b_count" in df else pd.Series([0] * len(df))

    for prog, count in zip(df["program_a"], genes_a_counts):
        if prog not in run_a_programs:
            run_a_programs[prog] = (len(run_a_programs) + 1, int(count) if pd.notna(count) else 0)

    for prog, count in zip(df["program_b"], genes_b_counts):
        if prog not in run_b_programs:
            run_b_programs[prog] = (len(run_b_programs) + 1, int(count) if pd.notna(count) else 0)

    # Map programs to numeric positions
    df["x_idx"] = df["program_a"].map(lambda p: run_a_programs[p][0])
    df["y_idx"] = df["program_b"].map(lambda p: run_b_programs[p][0])

    # Bubble sizes based on overlap count (scale for visibility)
    overlap = df.get("overlap_count", pd.Series([0] * len(df)))
    max_overlap = max(overlap.max(), 1)
    bubble_sizes = 50 + (overlap / max_overlap) * 450

    # Create scatter plot
    norm = plt.Normalize(vmin=0, vmax=1)
    scatter = ax.scatter(
        df["x_idx"],
        df["y_idx"],
        s=bubble_sizes,
        c=df["combined_similarity"],
        cmap="viridis",
        norm=norm,
        alpha=0.7,
        edgecolors="black",
        linewidth=0.5,
    )

    # Colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label("Combined Similarity", rotation=270, labelpad=15)
    cbar.set_ticks(np.linspace(0, 1, 6))

    # Axis labels and ticks
    ax.set_xlabel("Programs (Run A)", fontsize=12)
    ax.set_ylabel("Programs (Run B)", fontsize=12)

    x_ticks, x_labels = zip(*[
        (idx, f"{idx} ({count})")
        for prog, (idx, count) in run_a_programs.items()
    ]) if run_a_programs else ([], [])

    y_ticks, y_labels = zip(*[
        (idx, f"{idx} ({count})")
        for prog, (idx, count) in run_b_programs.items()
    ]) if run_b_programs else ([], [])

    ax.set_xticks(list(x_ticks))
    ax.set_xticklabels(list(x_labels), rotation=45, ha="right")
    ax.set_yticks(list(y_ticks))
    ax.set_yticklabels(list(y_labels))

    # Titles
    title = "Program Matches Bubble Plot"
    if query:
        title += f" - {query}"
    ax.set_title(title, fontsize=14, fontweight="bold")

    # Limits and grid
    ax.set_xlim(0.5, len(run_a_programs) + 0.5)
    ax.set_ylim(0.5, len(run_b_programs) + 0.5)
    ax.grid(True, alpha=0.3, linestyle="--")

    # Add legend mapping numbers to program names
    legend_lines = ["Run A programs:"]
    for prog, (idx, count) in run_a_programs.items():
        legend_lines.append(f"{idx}: {prog} (n={count})")

    legend_lines.append("")
    legend_lines.append("Run B programs:")
    for prog, (idx, count) in run_b_programs.items():
        legend_lines.append(f"{idx}: {prog} (n={count})")

    legend_text = "\n".join(legend_lines)
    # Place legend to the right of the colorbar dynamically
    fig.canvas.draw_idle()
    cbar_pos = cbar.ax.get_position()
    legend_x = cbar_pos.x1 + 0.02
    legend_y = 0.5
    fig.text(
        legend_x,
        legend_y,
        legend_text,
        va="center",
        ha="left",
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.4", facecolor="white", alpha=0.8, edgecolor="gray"),
    )

    # Adjust right margin to fit legend
    fig.subplots_adjust(right=min(0.9, legend_x + 0.15))

    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    if not return_fig:
        plt.close()
    else:
        return fig, ax  # type: ignore[return-value]


def generate_confusion_matrix(
    embeddings: dict[str, list[float]],
    labels: list[str],
    output_path: Path | str,
    figsize: tuple[int, int] = (10, 8),
    cluster: bool = True,
) -> None:
    """Generate confusion matrix heatmap from embeddings.

    Creates a heatmap showing cosine similarity between all program pairs.
    Optionally applies hierarchical clustering to group similar programs together.

    Args:
        embeddings: Dictionary mapping program names to embedding vectors
        labels: List of program names (must be keys in embeddings dict)
        output_path: Path to save the PNG file
        figsize: Figure size as (width, height) tuple (default: (10, 8))
        cluster: Whether to apply hierarchical clustering (default: True)

    .. code-block:: python

        from langpa_validation_tools.visualization import generate_confusion_matrix
        from langpa_validation_tools.embeddings import EmbeddingGenerator
        from pathlib import Path

        # Generate embeddings
        gen = EmbeddingGenerator()
        programs = ["DNA Repair", "DNA Damage", "Cell Cycle"]
        embeddings = {p: gen.generate_embedding(p) for p in programs}

        # Generate confusion matrix
        generate_confusion_matrix(
            embeddings,
            programs,
            Path("confusion_matrix.png")
        )
    """
    from langpa_validation_tools.embeddings import compute_cosine_similarity

    output_path = Path(output_path)

    # Build similarity matrix
    n = len(labels)
    similarity_matrix = np.zeros((n, n))

    for i, label_i in enumerate(labels):
        for j, label_j in enumerate(labels):
            if i == j:
                similarity_matrix[i, j] = 1.0
            else:
                sim = compute_cosine_similarity(
                    embeddings[label_i],
                    embeddings[label_j]
                )
                similarity_matrix[i, j] = sim

    # Apply clustering if requested and we have enough data
    if cluster and n > 2:
        # Convert similarity to distance for clustering
        distance_matrix = 1 - similarity_matrix

        # Ensure distance matrix is valid for clustering
        # Make it symmetric and convert to condensed form
        distance_matrix = (distance_matrix + distance_matrix.T) / 2
        np.fill_diagonal(distance_matrix, 0)

        # Convert to condensed distance matrix
        condensed_dist = squareform(distance_matrix, checks=False)

        # Perform hierarchical clustering
        linkage = hierarchy.linkage(condensed_dist, method="average")
        dendro = hierarchy.dendrogram(linkage, no_plot=True)

        # Reorder labels and matrix based on clustering
        idx = dendro["leaves"]
        labels = [labels[i] for i in idx]
        similarity_matrix = similarity_matrix[idx, :][:, idx]

    # Create heatmap
    fig, ax = plt.subplots(figsize=figsize)

    im = ax.imshow(similarity_matrix, cmap="YlOrRd", aspect="auto", vmin=0, vmax=1)

    # Set ticks and labels
    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
    ax.set_yticklabels(labels, fontsize=8)

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label("Cosine Similarity", rotation=270, labelpad=15)

    # Add text annotations for each cell
    for i in range(n):
        for j in range(n):
            text = ax.text(
                j, i, f"{similarity_matrix[i, j]:.2f}",
                ha="center", va="center",
                color="black" if similarity_matrix[i, j] < 0.5 else "white",
                fontsize=6 if n > 10 else 8
            )

    ax.set_title("Program Similarity Matrix", fontsize=14, fontweight="bold")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
