"""Response cache manager for DeepSearch API testing.

This module provides caching infrastructure to store and retrieve
DeepSearch API responses, minimizing expensive API calls during testing.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any


class ResponseCacheManager:
    """Manages cached DeepSearch API responses for testing.

    Provides deterministic caching of API responses based on preset,
    genes, and context. Cache keys are normalized to handle gene order
    and whitespace variations.

    .. code-block:: python

        cache = ResponseCacheManager()

        # Try to load from cache
        cached = cache.load(preset, genes, context)
        if cached:
            result = use_cached_response(cached)
        else:
            result = call_real_api()
            cache.save(preset, genes, context, result)
    """

    def __init__(self, cache_dir: str | Path | None = None) -> None:
        """Initialize the cache manager.

        Args:
            cache_dir: Directory for cache files. If None, uses
                      tests/fixtures/cached_responses
        """
        if cache_dir is None:
            # Default to tests/fixtures/cached_responses
            cache_dir = Path(__file__).parent.parent / "fixtures" / "cached_responses"

        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.metadata_file = self.cache_dir / "cache_metadata.json"

    def generate_cache_key(
        self,
        preset: str,
        genes: list[str],
        context: str
    ) -> str:
        """Generate deterministic cache key from inputs.

        Normalizes inputs to ensure consistent cache keys:
        - Genes are sorted and uppercased
        - Context is stripped and lowercased
        - Preset is used as-is

        Args:
            preset: Model preset name
            genes: List of gene symbols
            context: Biological context

        Returns:
            64-character SHA256 hash

        .. code-block:: python

            key1 = cache.generate_cache_key("preset", ["A", "B"], "context")
            key2 = cache.generate_cache_key("preset", ["B", "A"], " context ")
            assert key1 == key2  # Order and whitespace normalized
        """
        # Normalize inputs
        normalized_genes = sorted([g.strip().upper() for g in genes])
        normalized_context = context.strip().lower()

        # Create deterministic key
        key_data = f"{preset}:{','.join(normalized_genes)}:{normalized_context}"
        return hashlib.sha256(key_data.encode()).hexdigest()

    def _get_cache_filename(
        self,
        preset: str,
        genes: list[str],
        context: str
    ) -> str:
        """Generate human-readable filename with hash.

        Args:
            preset: Model preset name
            genes: List of gene symbols
            context: Biological context

        Returns:
            Filename like: tmem14e_cells_perplexity-sonar-pro_abc123.json
        """
        # Create readable prefix from genes and context
        genes_str = "_".join(sorted([g.lower() for g in genes]))[:40]
        context_str = context.replace(" ", "_").lower()[:20]

        # Add short hash for uniqueness
        cache_key = self.generate_cache_key(preset, genes, context)[:12]

        return f"{genes_str}_{context_str}_{preset}_{cache_key}.json"

    def save(
        self,
        preset: str,
        genes: list[str],
        context: str,
        response: dict[str, Any]
    ) -> Path:
        """Save response to cache.

        Args:
            preset: Model preset name
            genes: List of gene symbols
            context: Biological context
            response: API response to cache (should include markdown, citations, etc.)

        Returns:
            Path to saved cache file

        .. code-block:: python

            cache_path = cache.save(
                preset="perplexity-sonar-pro",
                genes=["TMEM14E"],
                context="cells",
                response={
                    "markdown": "...",
                    "citations": [...],
                    "provider": "perplexity",
                    "model": "sonar",
                    "duration_seconds": 5.0
                }
            )
        """
        filename = self._get_cache_filename(preset, genes, context)
        filepath = self.cache_dir / filename

        cache_data = {
            "preset": preset,
            "genes": genes,
            "context": context,
            "cache_key": self.generate_cache_key(preset, genes, context),
            "response": response,
            "cached_at": datetime.now().isoformat()
        }

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(cache_data, f, indent=2, ensure_ascii=False)

        return filepath

    def load(
        self,
        preset: str,
        genes: list[str],
        context: str
    ) -> dict[str, Any] | None:
        """Load response from cache if exists.

        Args:
            preset: Model preset name
            genes: List of gene symbols
            context: Biological context

        Returns:
            Cached response dict or None if not found

        .. code-block:: python

            cached = cache.load("preset", ["TMEM14E"], "cells")
            if cached:
                print(f"Using cached response: {cached['markdown'][:50]}")
        """
        filename = self._get_cache_filename(preset, genes, context)
        filepath = self.cache_dir / filename

        if not filepath.exists():
            return None

        with open(filepath, encoding="utf-8") as f:
            cache_data = json.load(f)

        return cache_data["response"]


__all__ = ["ResponseCacheManager"]
