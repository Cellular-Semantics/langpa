"""Caching for embeddings."""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np


def save_embeddings(
    embeddings: dict[str, list[float]],
    cache_path: str | Path
) -> None:
    """Save embeddings to CSV index + NPY vectors.

    Args:
        embeddings: Dict mapping names to embedding vectors
        cache_path: Base path for cache files (without extension)

    .. code-block:: python

        from langpa.embeddings.cache import save_embeddings

        embeddings = {"DNA Repair": [0.1, 0.2, 0.3]}
        save_embeddings(embeddings, "cache/embeddings")
        # Creates: cache/embeddings_index.csv, cache/embeddings_vectors.npy
    """
    cache_path = Path(cache_path)
    cache_path.parent.mkdir(parents=True, exist_ok=True)

    index_path = cache_path.parent / f"{cache_path.name}_index.csv"
    vectors_path = cache_path.parent / f"{cache_path.name}_vectors.npy"

    if not embeddings:
        # Handle empty embeddings
        with open(index_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "index"])
        np.save(vectors_path, np.array([]))
        return

    names = list(embeddings.keys())
    vectors = np.array([embeddings[name] for name in names])

    # Save index
    with open(index_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "index"])
        for i, name in enumerate(names):
            writer.writerow([name, i])

    # Save vectors
    np.save(vectors_path, vectors)


def load_embeddings(cache_path: str | Path) -> dict[str, list[float]]:
    """Load embeddings from CSV index + NPY vectors.

    Args:
        cache_path: Base path for cache files (without extension)

    Returns:
        Dict mapping names to embedding vectors

    .. code-block:: python

        from langpa.embeddings.cache import load_embeddings

        embeddings = load_embeddings("cache/embeddings")
        print(embeddings["DNA Repair"])
    """
    cache_path = Path(cache_path)
    index_path = cache_path.parent / f"{cache_path.name}_index.csv"
    vectors_path = cache_path.parent / f"{cache_path.name}_vectors.npy"

    # Load vectors
    vectors = np.load(vectors_path, allow_pickle=True)

    # Load index
    embeddings = {}
    with open(index_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            index = int(row["index"])
            if len(vectors) > 0:
                embeddings[name] = vectors[index].tolist()

    return embeddings
