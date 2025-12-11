"""End-to-end integration test for comparison workflow."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest


@pytest.mark.integration
def test_comparison_workflow_e2e() -> None:
    """End-to-end test: compare two runs with real data."""
    from langpa_validation_tools.comparison.matching import match_programs
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create mock runs
        manager = OutputManager(output_dir=temp_dir)

        # Run 1 container
        run1_dir = Path(temp_dir) / "project" / "query" / "run1"
        run1_dir.mkdir(parents=True)
        run1_container = run1_dir / "deepsearch_container.json"
        run1_data = {
            "metadata": {},
            "report": {
                "programs": [
                    {
                        "program_name": "DNA Repair",
                        "supporting_genes": ["TP53", "BRCA1"]
                    },
                    {
                        "program_name": "Cell Cycle",
                        "supporting_genes": ["EGFR", "MYC"]
                    }
                ]
            }
        }
        run1_container.write_text(json.dumps(run1_data))

        # Run 2 container
        run2_dir = Path(temp_dir) / "project" / "query" / "run2"
        run2_dir.mkdir(parents=True)
        run2_container = run2_dir / "deepsearch_container.json"
        run2_data = {
            "metadata": {},
            "report": {
                "programs": [
                    {
                        "program_name": "DNA Damage Repair",
                        "supporting_genes": ["TP53", "BRCA1", "ATM"]
                    },
                    {
                        "program_name": "Cell Division",
                        "supporting_genes": ["EGFR", "CDK1"]
                    }
                ]
            }
        }
        run2_container.write_text(json.dumps(run2_data))

        # Load containers
        containers = manager.list_container_files("project", "query")
        assert len(containers) == 2

        data1 = manager.load_container(containers[0])
        data2 = manager.load_container(containers[1])

        # Match programs
        matches = match_programs(
            data1["report"]["programs"],
            data2["report"]["programs"],
            threshold=0.3
        )

        assert len(matches) >= 1
        assert matches[0].scores.gene_jaccard > 0.0
        assert matches[0].scores.name_similarity > 0.0
        assert matches[0].scores.combined > 0.0
