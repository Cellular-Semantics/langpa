"""End-to-end integration test for visualization workflow."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pandas as pd
import pytest


@pytest.mark.integration
def test_visualization_workflow_e2e() -> None:
    """End-to-end test: generate bubble plot from matches DataFrame."""
    from langpa_validation_tools.visualization import generate_bubble_plot

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create sample matches DataFrame (as would come from compare_runs)
        matches_df = pd.DataFrame({
            "query": ["0_Gliosis", "0_Gliosis", "0_Gliosis", "1_OPC", "1_OPC"],
            "run_a": ["run1", "run1", "run1", "run1", "run1"],
            "run_b": ["run2", "run2", "run2", "run2", "run2"],
            "program_a": ["DNA Repair", "Cell Cycle", "Apoptosis", "Myelination", "Development"],
            "program_b": ["DNA Damage", "Cell Division", "Programmed Death", "Myelin Formation", "Cell Differentiation"],
            "gene_jaccard": [0.75, 0.60, 0.68, 0.82, 0.55],
            "name_similarity": [0.85, 0.65, 0.72, 0.78, 0.60],
            "combined_similarity": [0.78, 0.62, 0.69, 0.80, 0.57],
        })

        output_dir = Path(temp_dir) / "visualizations"
        output_dir.mkdir()

        # Generate overall bubble plot
        bubble_path = output_dir / "bubble_plot.png"
        generate_bubble_plot(matches_df, bubble_path)

        assert bubble_path.exists()
        assert bubble_path.stat().st_size > 0

        # Generate per-query bubble plots
        for query in ["0_Gliosis", "1_OPC"]:
            query_path = output_dir / f"bubble_plot_{query}.png"
            generate_bubble_plot(matches_df, query_path, query=query)

            assert query_path.exists()
            assert query_path.stat().st_size > 0


@pytest.mark.integration
def test_confusion_matrix_workflow_e2e() -> None:
    """End-to-end test: generate confusion matrix from embeddings."""
    from langpa_validation_tools.visualization import generate_confusion_matrix

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create sample embeddings (as would come from EmbeddingGenerator)
        # Using simplified 3D embeddings for testing
        embeddings = {
            "DNA Repair": [0.1, 0.2, 0.15],
            "DNA Damage Response": [0.12, 0.22, 0.14],
            "Cell Cycle Regulation": [0.8, 0.75, 0.82],
            "Cell Division Control": [0.78, 0.77, 0.80],
            "Apoptosis": [0.5, 0.45, 0.52],
            "Programmed Cell Death": [0.52, 0.47, 0.50],
        }

        labels = list(embeddings.keys())

        output_path = Path(temp_dir) / "confusion_matrix.png"
        generate_confusion_matrix(embeddings, labels, output_path)

        assert output_path.exists()
        assert output_path.stat().st_size > 0

        # Test without clustering
        output_path_no_cluster = Path(temp_dir) / "confusion_matrix_no_cluster.png"
        generate_confusion_matrix(embeddings, labels, output_path_no_cluster, cluster=False)

        assert output_path_no_cluster.exists()
        assert output_path_no_cluster.stat().st_size > 0


@pytest.mark.integration
def test_full_comparison_to_visualization_workflow() -> None:
    """End-to-end test: compare runs and visualize results."""
    import json
    from langpa_validation_tools.analysis import compare_runs
    from langpa_validation_tools.visualization import generate_bubble_plot

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create mock project
        project = "test_project"
        query = "test_query"

        run1_dir = Path(temp_dir) / project / query / "run1"
        run2_dir = Path(temp_dir) / project / query / "run2"
        run1_dir.mkdir(parents=True)
        run2_dir.mkdir(parents=True)

        # Create container files
        container1_data = {
            "metadata": {},
            "report": {
                "programs": [
                    {"program_name": "DNA Repair", "supporting_genes": ["TP53", "BRCA1", "ATM"]},
                    {"program_name": "Cell Cycle", "supporting_genes": ["MYC", "EGFR", "CDK1"]},
                ]
            }
        }

        container2_data = {
            "metadata": {},
            "report": {
                "programs": [
                    {"program_name": "DNA Damage", "supporting_genes": ["TP53", "BRCA1", "CHEK2"]},
                    {"program_name": "Cell Division", "supporting_genes": ["MYC", "EGFR", "CDK2"]},
                ]
            }
        }

        (run1_dir / "deepsearch_container.json").write_text(json.dumps(container1_data))
        (run2_dir / "deepsearch_container.json").write_text(json.dumps(container2_data))

        # Step 1: Compare runs
        matches_df = compare_runs(
            project=project,
            output_dir=Path(temp_dir),
            threshold=0.25
        )

        assert len(matches_df) > 0

        # Step 2: Generate visualizations
        viz_dir = Path(temp_dir) / "visualizations"
        viz_dir.mkdir()

        bubble_path = viz_dir / "bubble_plot.png"
        generate_bubble_plot(matches_df, bubble_path)

        assert bubble_path.exists()
        assert bubble_path.stat().st_size > 0

        # Verify the workflow produced meaningful results
        assert "gene_jaccard" in matches_df.columns
        assert "name_similarity" in matches_df.columns
        assert "combined_similarity" in matches_df.columns
