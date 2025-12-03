"""Tests for output path utilities."""

from __future__ import annotations

from pathlib import Path

import pytest

from langpa.utils.output_paths import build_run_directory, sanitize_name


@pytest.mark.unit
def test_sanitize_name() -> None:
    assert sanitize_name("My Project!") == "My_Project"
    assert sanitize_name(" spaced  name ") == "spaced_name"


@pytest.mark.unit
def test_build_run_directory(tmp_path: Path) -> None:
    run_dir = build_run_directory(tmp_path, "proj!", "query@123")
    assert run_dir.exists()
    parts = run_dir.relative_to(tmp_path).parts
    assert parts[0] == "proj"
    assert parts[1] == "query_123"
    assert len(parts[2]) > 0  # timestamp
