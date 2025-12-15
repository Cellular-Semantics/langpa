"""Unit tests for heatmap generation."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pandas as pd
import pytest


@pytest.mark.unit
def test_generate_bubble_plot_creates_file() -> None:
    """generate_bubble_plot creates a PNG file."""
    from langpa_validation_tools.visualization import generate_bubble_plot

    # Create sample matches DataFrame
    matches_df = pd.DataFrame({
        "query": ["query1", "query1", "query1"],
        "run_a": ["run1", "run1", "run1"],
        "run_b": ["run2", "run2", "run2"],
        "program_a": ["DNA Repair", "Cell Cycle", "Apoptosis"],
        "program_b": ["DNA Damage", "Cell Division", "Programmed Death"],
        "gene_jaccard": [0.8, 0.6, 0.7],
        "name_similarity": [0.9, 0.7, 0.8],
        "combined_similarity": [0.82, 0.63, 0.73],
        "overlap_count": [4, 3, 2],
        "genes_a_count": [6, 5, 4],
        "genes_b_count": [7, 5, 4],
    })

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = Path(temp_dir) / "bubble_plot.png"
        generate_bubble_plot(matches_df, output_path)

        assert output_path.exists()
        assert output_path.stat().st_size > 0


@pytest.mark.unit
def test_generate_bubble_plot_uses_program_axes_and_overlap_sizes(tmp_path: Path) -> None:
    """Bubble plot should map programs to numbered axes and scale by overlap_count."""
    from langpa_validation_tools.visualization import generate_bubble_plot
    import matplotlib

    matplotlib.use("Agg")

    matches_df = pd.DataFrame({
        "query": ["q1", "q1"],
        "run_a": ["run1", "run1"],
        "run_b": ["run2", "run2"],
        "program_a": ["ProgA", "ProgB"],
        "program_b": ["ProgX", "ProgY"],
        "gene_jaccard": [0.8, 0.5],
        "name_similarity": [0.7, 0.6],
        "combined_similarity": [0.75, 0.55],
        "overlap_count": [1, 3],
        "genes_a_count": [4, 5],
        "genes_b_count": [6, 7],
    })

    fig, ax = generate_bubble_plot(matches_df, tmp_path / "axes_plot.png", return_fig=True)  # type: ignore[assignment]

    sizes = ax.collections[0].get_sizes()
    # Second match has higher overlap, should produce larger bubble size
    assert sizes[1] > sizes[0]

    xticklabels = [tick.get_text() for tick in ax.get_xticklabels()]
    yticklabels = [tick.get_text() for tick in ax.get_yticklabels()]

    # Labels should show numbering with gene counts in parentheses
    assert "1 (" in xticklabels[0]
    assert "1 (" in yticklabels[0]

    legend_texts = [t.get_text() for t in fig.texts]
    assert any("ProgA" in text for text in legend_texts)
    assert any("ProgX" in text for text in legend_texts)

    import matplotlib.pyplot as plt
    plt.close(fig)


@pytest.mark.unit
def test_generate_bubble_plot_empty_dataframe() -> None:
    """generate_bubble_plot handles empty DataFrame gracefully."""
    from langpa_validation_tools.visualization import generate_bubble_plot

    empty_df = pd.DataFrame(columns=[
        "query", "run_a", "run_b", "program_a", "program_b",
        "gene_jaccard", "name_similarity", "combined_similarity",
        "overlap_count", "genes_a_count", "genes_b_count"
    ])

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = Path(temp_dir) / "empty_plot.png"

        # Should not raise an error
        generate_bubble_plot(empty_df, output_path)


@pytest.mark.unit
def test_generate_confusion_matrix_creates_file() -> None:
    """generate_confusion_matrix creates a PNG file."""
    from langpa_validation_tools.visualization import generate_confusion_matrix

    # Create sample embeddings and labels
    embeddings = {
        "DNA Repair": [0.1, 0.2, 0.3],
        "DNA Damage": [0.15, 0.22, 0.28],
        "Cell Cycle": [0.9, 0.8, 0.7],
        "Cell Division": [0.85, 0.82, 0.75],
    }

    labels = ["DNA Repair", "DNA Damage", "Cell Cycle", "Cell Division"]

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = Path(temp_dir) / "confusion_matrix.png"
        generate_confusion_matrix(embeddings, labels, output_path)

        assert output_path.exists()
        assert output_path.stat().st_size > 0


@pytest.mark.unit
def test_generate_confusion_matrix_minimal_data() -> None:
    """generate_confusion_matrix works with minimal data."""
    from langpa_validation_tools.visualization import generate_confusion_matrix

    # Just 2 programs
    embeddings = {
        "Program A": [0.1, 0.2],
        "Program B": [0.9, 0.8],
    }

    labels = ["Program A", "Program B"]

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = Path(temp_dir) / "minimal_matrix.png"

        # Should not raise an error
        generate_confusion_matrix(embeddings, labels, output_path)

        assert output_path.exists()


@pytest.mark.unit
def test_bubble_plot_query_filtering() -> None:
    """generate_bubble_plot can filter by query."""
    from langpa_validation_tools.visualization import generate_bubble_plot

    matches_df = pd.DataFrame({
        "query": ["query1", "query1", "query2"],
        "run_a": ["run1", "run1", "run1"],
        "run_b": ["run2", "run2", "run2"],
        "program_a": ["P1", "P2", "P3"],
        "program_b": ["P1b", "P2b", "P3b"],
        "gene_jaccard": [0.8, 0.6, 0.7],
        "name_similarity": [0.9, 0.7, 0.8],
        "combined_similarity": [0.82, 0.63, 0.73],
        "overlap_count": [2, 1, 3],
        "genes_a_count": [5, 4, 6],
        "genes_b_count": [4, 3, 5],
    })

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = Path(temp_dir) / "query_filtered.png"

        # Should be able to pass query parameter
        generate_bubble_plot(matches_df, output_path, query="query1")

        assert output_path.exists()
