"""Unit tests for README generator functionality."""

import json
from pathlib import Path
from datetime import datetime
import pytest

from langpa.utils.readme_generator import (
    generate_batch_readme,
    collect_project_data,
    format_readme_markdown,
    ProjectData,
    QueryData,
    RunData,
    ProgramSummary,
)


@pytest.fixture
def temp_project_dir(tmp_path: Path) -> Path:
    """Create a temporary project directory structure for testing."""
    project_dir = tmp_path / "test_project"
    project_dir.mkdir()

    # Create about.md
    about_path = project_dir / "about.md"
    about_path.write_text("## Test Project\nThis is a test project for README generation.")

    # Create input.csv
    input_csv_path = project_dir / "input.csv"
    input_csv_path.write_text("ID,name,gene_list,context\n0,Query1,GENE1;GENE2;GENE3,Test context")

    # Create query directory with runs
    query_dir = project_dir / "0_Query1"
    query_dir.mkdir()

    # Create first run
    run1_dir = query_dir / "20251201_120000"
    run1_dir.mkdir()

    # Create deepsearch_structured.json for run1
    run1_structured = {
        "metadata": {
            "timestamp": "2025-12-01T12:00:00",
            "genes": ["GENE1", "GENE2", "GENE3"],
            "context": {
                "cell_type": "test cells",
                "disease": "test disease",
                "tissue": "test tissue"
            }
        },
        "programs": [
            {
                "name": "Test Program 1",
                "genes": ["GENE1", "GENE2"],
                "citations": [{"source_id": 1}, {"source_id": 2}]
            },
            {
                "name": "Test Program 2",
                "genes": ["GENE2", "GENE3"],
                "citations": [{"source_id": 3}]
            }
        ]
    }
    (run1_dir / "deepsearch_structured.json").write_text(json.dumps(run1_structured))
    (run1_dir / "deepsearch_container.md").write_text("# Test Report 1")

    # Create second run
    run2_dir = query_dir / "20251201_130000"
    run2_dir.mkdir()

    run2_structured = {
        "metadata": {
            "timestamp": "2025-12-01T13:00:00",
            "genes": ["GENE1", "GENE2", "GENE3"],
            "context": {
                "cell_type": "test cells",
                "disease": "test disease",
                "tissue": "test tissue"
            }
        },
        "programs": [
            {
                "name": "Test Program 1",
                "genes": ["GENE1", "GENE2"],
                "citations": [{"source_id": 4}]
            }
        ]
    }
    (run2_dir / "deepsearch_structured.json").write_text(json.dumps(run2_structured))
    (run2_dir / "deepsearch_container.md").write_text("# Test Report 2")

    return project_dir


def test_collect_project_data_basic(temp_project_dir: Path):
    """Test basic project data collection."""
    project_data = collect_project_data(temp_project_dir)

    assert project_data.project_name == "test_project"
    assert project_data.about_text is not None
    assert "Test Project" in project_data.about_text
    assert project_data.input_csv_path is not None
    assert len(project_data.queries) == 1


def test_collect_project_data_query_details(temp_project_dir: Path):
    """Test that query details are collected correctly."""
    project_data = collect_project_data(temp_project_dir)

    query = project_data.queries[0]
    assert query.query_name == "0_Query1"
    assert query.context == "cell_type: test cells, disease: test disease, tissue: test tissue"
    assert query.num_genes == 3
    assert len(query.runs) == 2


def test_collect_project_data_program_aggregation(temp_project_dir: Path):
    """Test that programs are aggregated correctly across runs."""
    project_data = collect_project_data(temp_project_dir)

    query = project_data.queries[0]
    programs = query.programs

    # Should have 2 unique programs
    assert len(programs) == 2

    # Test Program 1 should have aggregated stats from both runs
    prog1 = next(p for p in programs if p.name == "Test Program 1")
    assert prog1.total_genes == 2
    assert prog1.total_citations == 3  # 2 from run1, 1 from run2

    # Test Program 2 should only have stats from run1
    prog2 = next(p for p in programs if p.name == "Test Program 2")
    assert prog2.total_genes == 2
    assert prog2.total_citations == 1


def test_collect_project_data_run_details(temp_project_dir: Path):
    """Test that run details are collected correctly."""
    project_data = collect_project_data(temp_project_dir)

    query = project_data.queries[0]
    runs = query.runs

    # Check run timestamps are parsed correctly
    assert all(isinstance(run.timestamp, datetime) for run in runs)

    # Check file paths are set correctly
    assert all(run.deepsearch_container_path.exists() for run in runs)
    assert all(run.deepsearch_structured_path.exists() for run in runs)


def test_format_readme_markdown_structure(temp_project_dir: Path):
    """Test that README markdown is formatted correctly."""
    project_data = collect_project_data(temp_project_dir)
    readme_content = format_readme_markdown(project_data)

    # Check title
    assert "# test_project" in readme_content

    # Check about section
    assert "Test Project" in readme_content

    # Check input CSV link
    assert "[input.csv](input.csv)" in readme_content

    # Check Results section
    assert "## Results" in readme_content

    # Check query subsection
    assert "### 0_Query1" in readme_content

    # Check context info
    assert "test cells" in readme_content
    assert "3 total" in readme_content

    # Check programs in details
    assert "<details>" in readme_content
    assert "Test Program 1" in readme_content
    assert "Test Program 2" in readme_content

    # Check run links
    assert "20251201_120000" in readme_content
    assert "[deepsearch_container.md]" in readme_content
    assert "[deepsearch_structured.json]" in readme_content


def test_format_readme_markdown_program_table(temp_project_dir: Path):
    """Test that program table is formatted correctly."""
    project_data = collect_project_data(temp_project_dir)
    readme_content = format_readme_markdown(project_data)

    # Check table headers
    assert "| Program Name | Genes | Citations |" in readme_content
    assert "|---|---|---|" in readme_content

    # Check program rows
    assert "| Test Program 1 | 2 | 3 |" in readme_content
    assert "| Test Program 2 | 2 | 1 |" in readme_content


def test_generate_batch_readme(temp_project_dir: Path):
    """Test end-to-end README generation."""
    readme_path = generate_batch_readme(temp_project_dir)

    assert readme_path.exists()
    assert readme_path.name == "README.md"
    assert readme_path.parent == temp_project_dir

    content = readme_path.read_text()
    assert "# test_project" in content
    assert "## Results" in content


def test_collect_project_data_no_about(tmp_path: Path):
    """Test project data collection when about.md is missing."""
    project_dir = tmp_path / "no_about_project"
    project_dir.mkdir()

    project_data = collect_project_data(project_dir)
    assert project_data.about_text is None


def test_collect_project_data_no_input_csv(tmp_path: Path):
    """Test project data collection when input.csv is missing."""
    project_dir = tmp_path / "no_csv_project"
    project_dir.mkdir()

    project_data = collect_project_data(project_dir)
    assert project_data.input_csv_path is None


def test_collect_project_data_no_queries(tmp_path: Path):
    """Test project data collection when no query directories exist."""
    project_dir = tmp_path / "no_queries_project"
    project_dir.mkdir()

    project_data = collect_project_data(project_dir)
    assert len(project_data.queries) == 0


def test_collect_project_data_malformed_json(tmp_path: Path):
    """Test that malformed JSON files are handled gracefully."""
    project_dir = tmp_path / "malformed_project"
    project_dir.mkdir()

    query_dir = project_dir / "0_TestQuery"
    query_dir.mkdir()

    run_dir = query_dir / "20251201_120000"
    run_dir.mkdir()

    # Create malformed JSON
    (run_dir / "deepsearch_structured.json").write_text("{ invalid json }")

    project_data = collect_project_data(project_dir)

    # Queries with no valid runs are skipped entirely
    assert len(project_data.queries) == 0


def test_format_readme_gene_coverage(temp_project_dir: Path):
    """Test that gene coverage percentage is calculated correctly."""
    project_data = collect_project_data(temp_project_dir)
    readme_content = format_readme_markdown(project_data)

    # All 3 genes are covered by programs
    assert "3 total" in readme_content
    # Calculate expected percentage: 3 unique genes covered / 3 total = 100%
    # But based on the programs, GENE1 and GENE2 appear in Program 1, GENE2 and GENE3 in Program 2
    # So all 3 genes are covered
    assert "100%" in readme_content or "3 covered" in readme_content
