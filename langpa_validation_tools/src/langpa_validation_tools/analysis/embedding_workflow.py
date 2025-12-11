"""Embedding workflow for batch generating embeddings from DeepSearch outputs.

This module provides functionality to extract program names from DeepSearch
container files and batch-generate embeddings for them.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from langpa.services.output_manager import OutputManager
from langpa_validation_tools.embeddings import EmbeddingGenerator, save_embeddings


def extract_program_names(
    project: str,
    output_dir: Path = Path("outputs")
) -> list[str]:
    """Extract unique program names from all DeepSearch runs in a project.

    Args:
        project: Project name (directory under output_dir)
        output_dir: Base output directory containing project folders

    Returns:
        List of unique program names across all runs

    .. code-block:: python

        from langpa_validation_tools.analysis.embedding_workflow import extract_program_names
        from pathlib import Path

        # Extract all program names from a project
        names = extract_program_names("glioblastoma_ds_auto", Path("outputs"))
        print(f"Found {len(names)} unique programs")
    """
    manager = OutputManager(output_dir=str(output_dir))

    # Get all container files
    container_paths = manager.list_container_files(project)

    if not container_paths:
        return []

    # Collect all program names
    program_names = set()

    for container_path in container_paths:
        container_data = manager.load_container(container_path)

        # Extract programs
        programs = container_data.get("report", {}).get("programs", [])

        for program in programs:
            if "program_name" in program:
                program_names.add(program["program_name"])

    return sorted(program_names)


def batch_generate_embeddings(
    program_names: list[str],
    output_path: Path | str,
    generator: EmbeddingGenerator | None = None,
) -> dict[str, list[float]]:
    """Batch generate embeddings for program names and save to cache.

    Args:
        program_names: List of program names to embed
        output_path: Path for cache files (without extension)
        generator: Optional EmbeddingGenerator instance (creates new if None)

    Returns:
        Dictionary mapping program names to embedding vectors

    .. code-block:: python

        from langpa_validation_tools.analysis.embedding_workflow import (
            extract_program_names,
            batch_generate_embeddings
        )
        from pathlib import Path

        # Extract program names
        names = extract_program_names("my_project")

        # Generate embeddings
        embeddings = batch_generate_embeddings(
            names,
            Path("embeddings/programs")
        )

        print(f"Generated {len(embeddings)} embeddings")
    """
    output_path = Path(output_path)

    # Create generator if not provided
    if generator is None:
        generator = EmbeddingGenerator()

    # Batch generate embeddings
    print(f"Generating embeddings for {len(program_names)} programs...")
    embedding_vectors = generator.generate_embeddings(program_names)

    # Create embeddings dictionary
    embeddings = {
        name: vector
        for name, vector in zip(program_names, embedding_vectors)
    }

    # Save to cache
    print(f"Saving embeddings to cache: {output_path}")
    save_embeddings(embeddings, output_path)

    return embeddings


def generate_project_embeddings(
    project: str,
    output_dir: Path = Path("outputs"),
    embeddings_output: Path | None = None,
) -> dict[str, list[float]]:
    """Complete workflow: extract program names and generate embeddings.

    Convenience function that combines extract_program_names and
    batch_generate_embeddings.

    Args:
        project: Project name
        output_dir: Base output directory (default: outputs/)
        embeddings_output: Path for embedding cache (default: output_dir/project/embeddings/programs)

    Returns:
        Dictionary mapping program names to embedding vectors

    .. code-block:: python

        from langpa_validation_tools.analysis.embedding_workflow import generate_project_embeddings
        from pathlib import Path

        # One-step embedding generation
        embeddings = generate_project_embeddings("glioblastoma_ds_auto")
    """
    # Extract program names
    print(f"Extracting program names from project: {project}")
    program_names = extract_program_names(project, output_dir)

    if not program_names:
        print(f"No programs found in project: {project}")
        return {}

    print(f"Found {len(program_names)} unique programs")

    # Determine output path
    if embeddings_output is None:
        embeddings_output = output_dir / project / "embeddings" / "programs"

    # Ensure parent directory exists
    embeddings_output.parent.mkdir(parents=True, exist_ok=True)

    # Generate embeddings
    embeddings = batch_generate_embeddings(program_names, embeddings_output)

    return embeddings
