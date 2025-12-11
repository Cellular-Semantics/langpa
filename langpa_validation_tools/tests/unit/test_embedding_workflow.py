"""Unit tests for embedding workflow."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest


@pytest.mark.unit
def test_extract_program_names() -> None:
    """Extract program names from container files."""
    from langpa_validation_tools.analysis.embedding_workflow import extract_program_names

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create mock containers
        project = "test_project"
        query = "test_query"
        run_dir = Path(temp_dir) / project / query / "run1"
        run_dir.mkdir(parents=True)

        container_data = {
            "metadata": {},
            "report": {
                "programs": [
                    {"program_name": "DNA Repair", "supporting_genes": ["TP53"]},
                    {"program_name": "Cell Cycle", "supporting_genes": ["MYC"]},
                ]
            }
        }

        (run_dir / "deepsearch_container.json").write_text(json.dumps(container_data))

        # Extract names
        names = extract_program_names(project, Path(temp_dir))

        assert len(names) == 2
        assert "DNA Repair" in names
        assert "Cell Cycle" in names


@pytest.mark.unit
def test_extract_program_names_deduplicates() -> None:
    """Extract program names deduplicates across runs."""
    from langpa_validation_tools.analysis.embedding_workflow import extract_program_names

    with tempfile.TemporaryDirectory() as temp_dir:
        project = "test_project"
        query = "test_query"

        # Run 1
        run1_dir = Path(temp_dir) / project / query / "run1"
        run1_dir.mkdir(parents=True)
        container1_data = {
            "metadata": {},
            "report": {
                "programs": [
                    {"program_name": "DNA Repair", "supporting_genes": ["TP53"]},
                ]
            }
        }
        (run1_dir / "deepsearch_container.json").write_text(json.dumps(container1_data))

        # Run 2 with same program name
        run2_dir = Path(temp_dir) / project / query / "run2"
        run2_dir.mkdir(parents=True)
        container2_data = {
            "metadata": {},
            "report": {
                "programs": [
                    {"program_name": "DNA Repair", "supporting_genes": ["BRCA1"]},
                    {"program_name": "Cell Cycle", "supporting_genes": ["MYC"]},
                ]
            }
        }
        (run2_dir / "deepsearch_container.json").write_text(json.dumps(container2_data))

        # Extract names
        names = extract_program_names(project, Path(temp_dir))

        # Should deduplicate "DNA Repair"
        assert len(names) == 2
        assert "DNA Repair" in names
        assert "Cell Cycle" in names


@pytest.mark.unit
def test_batch_generate_embeddings_caching() -> None:
    """Batch generate embeddings and save to cache."""
    from langpa_validation_tools.analysis.embedding_workflow import batch_generate_embeddings

    with tempfile.TemporaryDirectory() as temp_dir:
        program_names = ["DNA Repair", "Cell Cycle", "Apoptosis"]
        output_path = Path(temp_dir) / "embeddings"

        # Mock the embedding generator to avoid API calls
        class MockEmbeddingGenerator:
            def generate_embeddings(self, texts):
                # Return mock embeddings (3072 dimensions for text-embedding-3-large)
                return [[0.1] * 3072 for _ in texts]

        # This test would normally use mocked API
        # For now, just test the structure
        embeddings = batch_generate_embeddings(
            program_names,
            output_path,
            generator=MockEmbeddingGenerator()
        )

        assert len(embeddings) == 3
        assert "DNA Repair" in embeddings
        assert "Cell Cycle" in embeddings
        assert "Apoptosis" in embeddings

        # Check cache files exist
        assert (output_path.parent / f"{output_path.name}_index.csv").exists()
        assert (output_path.parent / f"{output_path.name}_vectors.npy").exists()


@pytest.mark.unit
def test_extract_program_names_empty_project() -> None:
    """Extract program names from empty project returns empty list."""
    from langpa_validation_tools.analysis.embedding_workflow import extract_program_names

    with tempfile.TemporaryDirectory() as temp_dir:
        names = extract_program_names("nonexistent", Path(temp_dir))

        assert names == []
