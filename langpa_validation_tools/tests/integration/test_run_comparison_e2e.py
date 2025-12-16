"""End-to-end integration test for run comparison workflow."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest


@pytest.mark.integration
def test_run_comparison_e2e() -> None:
    """End-to-end test: compare multiple runs with realistic data."""
    from langpa_validation_tools.analysis import compare_runs

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create mock project with multiple queries and runs
        project = "test_project"

        # Query 1: Two runs
        query1 = "0_Gliosis"
        run1_dir = Path(temp_dir) / project / query1 / "20251209_120000"
        run2_dir = Path(temp_dir) / project / query1 / "20251209_130000"
        run1_dir.mkdir(parents=True)
        run2_dir.mkdir(parents=True)

        # Query 2: Two runs
        query2 = "1_Oligodendrocytes"
        run3_dir = Path(temp_dir) / project / query2 / "20251209_140000"
        run4_dir = Path(temp_dir) / project / query2 / "20251209_150000"
        run3_dir.mkdir(parents=True)
        run4_dir.mkdir(parents=True)

        # Create container files with programs
        containers = [
            (run1_dir / "deepsearch_container.json", {
                "metadata": {"timestamp": "2025-12-09 12:00:00"},
                "report": {
                    "programs": [
                        {
                            "program_name": "DNA Repair Mechanisms",
                            "supporting_genes": ["TP53", "BRCA1", "BRCA2", "ATM"]
                        },
                        {
                            "program_name": "Cell Cycle Regulation",
                            "supporting_genes": ["EGFR", "MYC", "CDK1", "CCND1"]
                        }
                    ]
                }
            }),
            (run2_dir / "deepsearch_container.json", {
                "metadata": {"timestamp": "2025-12-09 13:00:00"},
                "report": {
                    "programs": [
                        {
                            "program_name": "DNA Damage Response",
                            "supporting_genes": ["TP53", "BRCA1", "ATM", "CHEK2"]
                        },
                        {
                            "program_name": "Cell Division Control",
                            "supporting_genes": ["EGFR", "MYC", "CDK2"]
                        }
                    ]
                }
            }),
            (run3_dir / "deepsearch_container.json", {
                "metadata": {"timestamp": "2025-12-09 14:00:00"},
                "report": {
                    "programs": [
                        {
                            "program_name": "Myelination",
                            "supporting_genes": ["MBP", "PLP1", "MAG", "MOG"]
                        }
                    ]
                }
            }),
            (run4_dir / "deepsearch_container.json", {
                "metadata": {"timestamp": "2025-12-09 15:00:00"},
                "report": {
                    "programs": [
                        {
                            "program_name": "Oligodendrocyte Development",
                            "supporting_genes": ["MBP", "PLP1", "SOX10"]
                        }
                    ]
                }
            }),
        ]

        for path, data in containers:
            path.write_text(json.dumps(data))

        # Run comparison
        output_path = Path(temp_dir) / project / "analysis"
        df = compare_runs(
            project=project,
            output_dir=Path(temp_dir),
            threshold=0.25,  # Lower threshold to catch more matches
            save_csv=True,
            csv_output_dir=output_path
        )

        # Assertions
        assert len(df) > 0, "Should find at least one match"

        # Check columns
        expected_columns = [
            "query", "run_a", "run_b", "program_a", "program_b",
            "gene_jaccard", "name_similarity", "combined_similarity",
            "overlap_count", "genes_a_count", "genes_b_count", "is_match",
        ]
        for col in expected_columns:
            assert col in df.columns

        # Check that matches exist for both queries
        queries_in_results = set(df["query"].unique())
        assert query1 in queries_in_results
        assert query2 in queries_in_results

        # Check CSV files were created
        assert (output_path / "program_matches.csv").exists()
        assert (output_path / "unmatched_programs.csv").exists()

        # Verify similarity scores are valid
        assert all(df["gene_jaccard"] >= 0.0) and all(df["gene_jaccard"] <= 1.0)
        assert all(df["name_similarity"] >= 0.0) and all(df["name_similarity"] <= 1.0)
        assert all(df["combined_similarity"] >= 0.0) and all(df["combined_similarity"] <= 1.0)

        # Check specific expected matches
        # DNA Repair vs DNA Damage should match (high gene overlap)
        dna_matches = df[
            (df["program_a"].str.contains("DNA", na=False)) &
            (df["program_b"].str.contains("DNA", na=False))
        ]
        assert len(dna_matches) >= 1, "DNA repair programs should match"

        # Myelination vs Oligodendrocyte Development should match (shared genes)
        myelin_matches = df[
            (df["program_a"].str.contains("Myelin|Oligodendrocyte", na=False)) |
            (df["program_b"].str.contains("Myelin|Oligodendrocyte", na=False))
        ]
        assert len(myelin_matches) >= 1, "Myelination programs should match"
