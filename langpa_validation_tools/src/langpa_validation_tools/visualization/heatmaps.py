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
) -> None:
    """Generate bubble plot visualization of program matches.

    Creates a scatter plot where each point represents a matched program pair.
    The x-axis shows gene Jaccard similarity, y-axis shows name similarity,
    bubble size represents the number of overlapping genes, and color intensity
    shows the combined similarity score.

    Args:
        matches_df: DataFrame with program matches (from compare_runs)
        output_path: Path to save the PNG file
        query: Optional query name to filter results (default: all queries)
        figsize: Figure size as (width, height) tuple (default: (12, 8))

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
    """
    output_path = Path(output_path)

    # Filter by query if specified
    if query:
        df = matches_df[matches_df["query"] == query].copy()
    else:
        df = matches_df.copy()

    # Handle empty DataFrame
    if len(df) == 0:
        fig, ax = plt.subplots(figsize=figsize)
        ax.text(
            0.5, 0.5,
            "No matches to display",
            ha="center", va="center",
            fontsize=14,
            color="gray"
        )
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel("Gene Jaccard Similarity")
        ax.set_ylabel("Name Similarity")
        ax.set_title("Program Matches Bubble Plot")
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches="tight")
        plt.close()
        return

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)

    # Calculate bubble sizes (based on gene overlap)
    # We don't have overlap count directly, so use gene_jaccard as proxy
    # Scale it to reasonable bubble sizes (50-500)
    bubble_sizes = 50 + (df["gene_jaccard"] * 450)

    # Create scatter plot
    scatter = ax.scatter(
        df["gene_jaccard"],
        df["name_similarity"],
        s=bubble_sizes,
        c=df["combined_similarity"],
        cmap="viridis",
        alpha=0.6,
        edgecolors="black",
        linewidth=0.5,
    )

    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label("Combined Similarity", rotation=270, labelpad=15)

    # Labels and title
    ax.set_xlabel("Gene Jaccard Similarity", fontsize=12)
    ax.set_ylabel("Name Similarity", fontsize=12)

    title = "Program Matches Bubble Plot"
    if query:
        title += f" - {query}"
    ax.set_title(title, fontsize=14, fontweight="bold")

    # Set axis limits with padding
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)

    # Add grid
    ax.grid(True, alpha=0.3, linestyle="--")

    # Add reference lines at threshold (0.3)
    ax.axhline(y=0.3, color="red", linestyle="--", alpha=0.3, label="Threshold")
    ax.axvline(x=0.3, color="red", linestyle="--", alpha=0.3)

    ax.legend(loc="upper left")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()


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
