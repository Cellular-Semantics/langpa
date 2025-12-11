"""Unit tests for OutputManager extensions."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest


@pytest.mark.unit
def test_list_container_files() -> None:
    """List all container files for a project/query."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create mock container files
        project_dir = Path(temp_dir) / "project1" / "query1"
        run1_dir = project_dir / "20251209_120000"
        run2_dir = project_dir / "20251209_130000"
        run1_dir.mkdir(parents=True)
        run2_dir.mkdir(parents=True)

        container1 = run1_dir / "deepsearch_container.json"
        container2 = run2_dir / "deepsearch_container.json"
        container1.write_text('{"metadata": {}}')
        container2.write_text('{"metadata": {}}')

        manager = OutputManager(output_dir=temp_dir)
        containers = manager.list_container_files("project1", "query1")

        assert len(containers) == 2
        assert all(c.name == "deepsearch_container.json" for c in containers)


@pytest.mark.unit
def test_list_container_files_all_queries() -> None:
    """List container files for all queries in a project."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create containers in multiple queries
        project_dir = Path(temp_dir) / "project1"
        query1 = project_dir / "query1" / "run1"
        query2 = project_dir / "query2" / "run1"
        query1.mkdir(parents=True)
        query2.mkdir(parents=True)

        (query1 / "deepsearch_container.json").write_text('{}')
        (query2 / "deepsearch_container.json").write_text('{}')

        manager = OutputManager(output_dir=temp_dir)
        containers = manager.list_container_files("project1")  # No query specified

        assert len(containers) == 2


@pytest.mark.unit
def test_list_container_files_nonexistent_project() -> None:
    """List container files for nonexistent project returns empty list."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)
        containers = manager.list_container_files("nonexistent")

        assert containers == []


@pytest.mark.unit
def test_load_container() -> None:
    """Load a single container JSON."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        container_path = Path(temp_dir) / "deepsearch_container.json"
        container_data = {
            "metadata": {"timestamp": "2025-12-09"},
            "report": {"programs": []}
        }
        container_path.write_text(json.dumps(container_data))

        manager = OutputManager(output_dir=temp_dir)
        loaded = manager.load_container(container_path)

        assert loaded["metadata"]["timestamp"] == "2025-12-09"
        assert "report" in loaded


@pytest.mark.unit
def test_load_containers_for_query() -> None:
    """Load all containers for a specific query."""
    from langpa.services.output_manager import OutputManager

    with tempfile.TemporaryDirectory() as temp_dir:
        project_dir = Path(temp_dir) / "project1" / "query1"
        run1_dir = project_dir / "run1"
        run2_dir = project_dir / "run2"
        run1_dir.mkdir(parents=True)
        run2_dir.mkdir(parents=True)

        container1 = run1_dir / "deepsearch_container.json"
        container2 = run2_dir / "deepsearch_container.json"
        container1.write_text('{"metadata": {"run": 1}}')
        container2.write_text('{"metadata": {"run": 2}}')

        manager = OutputManager(output_dir=temp_dir)
        containers = manager.load_containers_for_query("project1", "query1")

        assert len(containers) == 2
        run_ids = {c["metadata"]["run"] for c in containers}
        assert run_ids == {1, 2}
