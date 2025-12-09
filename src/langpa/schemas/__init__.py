"""Registry pointing to JSON Schema documents housed in this package."""

from __future__ import annotations

from importlib import resources
from json import loads
from pathlib import Path
from typing import Any


def load_schema(name: str) -> dict[str, Any]:
    """Load a JSON schema file bundled in the `schemas` directory."""
    with resources.files(__package__).joinpath(name).open("r", encoding="utf-8") as handle:
        return loads(handle.read())


def get_schemas_dir() -> Path:
    """Get the path to the schemas directory.

    Returns:
        Path object pointing to the schemas directory
    """
    return Path(resources.files(__package__).joinpath(".").as_posix())


__all__ = ["load_schema", "get_schemas_dir"]
