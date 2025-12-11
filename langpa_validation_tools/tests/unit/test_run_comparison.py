"""Unit tests for run comparison module."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest


@pytest.mark.unit
def test_compare_runs_returns_dataframe() -> None:
    """compare_runs returns a pandas DataFrame."""
    from langpa_validation_tools.analysis.run_comparison import compare_runs
    import pandas as pd

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create mock container files
        project = "test_project"
        query = "test_query"

        # Create directory structure
        run1_dir = Path(temp_dir) / project / query / "run1"
        run2_dir = Path(temp_dir) / project / query / "run2"
        run1_dir.mkdir(parents=True)
        run2_dir.mkdir(parents=True)

        # Create container files
        container1 = run1_dir / "deepsearch_container.json"
        container2 = run2_dir / "deepsearch_container.json"

        container1_data = {
            "metadata": {"timestamp": "2025-01-01"},
            "report": {
                "programs": [
                    {"program_name": "DNA Repair", "supporting_genes": ["TP53", "BRCA1"]}
                ]
            }
        }

        container2_data = {
            "metadata": {"timestamp": "2025-01-02"},
            "report": {
                "programs": [
                    {"program_name": "DNA Damage", "supporting_genes": ["TP53", "ATM"]}
                ]
            }
        }

        container1.write_text(json.dumps(container1_data))
        container2.write_text(json.dumps(container2_data))

        # Run comparison
        result = compare_runs(project=project, output_dir=Path(temp_dir))

        assert isinstance(result, pd.DataFrame)


@pytest.mark.unit
def test_compare_runs_includes_required_columns() -> None:
    """compare_runs DataFrame has required columns."""
    from langpa_validation_tools.analysis.run_comparison import compare_runs

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create mock data
        project = "test_project"
        query = "test_query"

        run1_dir = Path(temp_dir) / project / query / "run1"
        run2_dir = Path(temp_dir) / project / query / "run2"
        run1_dir.mkdir(parents=True)
        run2_dir.mkdir(parents=True)

        container1 = run1_dir / "deepsearch_container.json"
        container2 = run2_dir / "deepsearch_container.json"

        container1_data = {
            "metadata": {},
            "report": {
                "programs": [
                    {"program_name": "P1", "supporting_genes": ["G1", "G2"]}
                ]
            }
        }

        container2_data = {
            "metadata": {},
            "report": {
                "programs": [
                    {"program_name": "P2", "supporting_genes": ["G1", "G3"]}
                ]
            }
        }

        container1.write_text(json.dumps(container1_data))
        container2.write_text(json.dumps(container2_data))

        result = compare_runs(project=project, output_dir=Path(temp_dir), threshold=0.2)

        required_columns = [
            "query",
            "run_a",
            "run_b",
            "program_a",
            "program_b",
            "gene_jaccard",
            "name_similarity",
            "combined_similarity"
        ]

        for col in required_columns:
            assert col in result.columns


@pytest.mark.unit
def test_compare_runs_empty_project() -> None:
    """compare_runs returns empty DataFrame for empty project."""
    from langpa_validation_tools.analysis.run_comparison import compare_runs
    import pandas as pd

    with tempfile.TemporaryDirectory() as temp_dir:
        result = compare_runs(project="nonexistent", output_dir=Path(temp_dir))

        assert isinstance(result, pd.DataFrame)
        assert len(result) == 0


@pytest.mark.unit
def test_compare_runs_saves_csv_files() -> None:
    """compare_runs saves matches and unmatched CSV files."""
    from langpa_validation_tools.analysis.run_comparison import compare_runs

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create mock data
        project = "test_project"
        query = "test_query"

        run1_dir = Path(temp_dir) / project / query / "run1"
        run2_dir = Path(temp_dir) / project / query / "run2"
        run1_dir.mkdir(parents=True)
        run2_dir.mkdir(parents=True)

        container1 = run1_dir / "deepsearch_container.json"
        container2 = run2_dir / "deepsearch_container.json"

        container1_data = {
            "metadata": {},
            "report": {
                "programs": [
                    {"program_name": "P1", "supporting_genes": ["G1", "G2"]}
                ]
            }
        }

        container2_data = {
            "metadata": {},
            "report": {
                "programs": [
                    {"program_name": "P2", "supporting_genes": ["G1", "G3"]}
                ]
            }
        }

        container1.write_text(json.dumps(container1_data))
        container2.write_text(json.dumps(container2_data))

        output_path = Path(temp_dir) / project / "analysis"
        compare_runs(
            project=project,
            output_dir=Path(temp_dir),
            save_csv=True,
            csv_output_dir=output_path
        )

        # Check CSV files were created
        assert (output_path / "program_matches.csv").exists()
        assert (output_path / "unmatched_programs.csv").exists()
