"""Utilities for building project/query-aware output paths."""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path


def sanitize_name(name: str) -> str:
    """Make a filesystem-safe name."""
    sanitized = re.sub(r"[^\w.-]+", "_", name.strip())[:50]
    return sanitized.strip("_")


def build_run_directory(base_output: Path, project: str, query: str) -> Path:
    """Create outputs/<project>/<query>/<timestamp> and return the path."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = base_output / sanitize_name(project) / sanitize_name(query) / timestamp
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir
