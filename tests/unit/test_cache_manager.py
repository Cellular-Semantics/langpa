"""Unit tests for ResponseCacheManager.

Tests the caching infrastructure for DeepSearch API responses
to minimize expensive API calls during testing.
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

import pytest

# Add tests directory to path for importing utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.cache_manager import ResponseCacheManager


@pytest.mark.unit
def test_cache_manager_initialization() -> None:
    """Test ResponseCacheManager can be initialized with custom directory."""

    with tempfile.TemporaryDirectory() as temp_dir:
        cache = ResponseCacheManager(cache_dir=temp_dir)

        assert cache.cache_dir == Path(temp_dir)
        assert cache.cache_dir.exists()
        assert cache.metadata_file == Path(temp_dir) / "cache_metadata.json"


@pytest.mark.unit
def test_cache_manager_default_directory() -> None:
    """Test ResponseCacheManager uses default directory if not specified."""

    cache = ResponseCacheManager()

    # Should use tests/fixtures/cached_responses
    assert cache.cache_dir.exists()
    assert "cached_responses" in str(cache.cache_dir)


@pytest.mark.unit
def test_generate_cache_key_deterministic() -> None:
    """Test cache key generation is deterministic."""

    cache = ResponseCacheManager()

    # Same inputs should produce same key
    key1 = cache.generate_cache_key(
        preset="perplexity-sonar-pro",
        genes=["TMEM14E"],
        context="cells"
    )

    key2 = cache.generate_cache_key(
        preset="perplexity-sonar-pro",
        genes=["TMEM14E"],
        context="cells"
    )

    assert key1 == key2
    assert len(key1) == 64  # SHA256 hash


@pytest.mark.unit
def test_generate_cache_key_normalizes_genes() -> None:
    """Test that gene order doesn't affect cache key."""

    cache = ResponseCacheManager()

    key1 = cache.generate_cache_key(
        preset="test-preset",
        genes=["C9orf72", "C21orf91"],
        context="neural cells"
    )

    # Different order
    key2 = cache.generate_cache_key(
        preset="test-preset",
        genes=["C21orf91", "C9orf72"],
        context="neural cells"
    )

    assert key1 == key2


@pytest.mark.unit
def test_generate_cache_key_normalizes_context() -> None:
    """Test that whitespace in context doesn't affect cache key."""

    cache = ResponseCacheManager()

    key1 = cache.generate_cache_key(
        preset="test-preset",
        genes=["TMEM14E"],
        context="neural cells"
    )

    # Extra whitespace
    key2 = cache.generate_cache_key(
        preset="test-preset",
        genes=["TMEM14E"],
        context=" neural cells "
    )

    assert key1 == key2


@pytest.mark.unit
def test_save_and_load_response() -> None:
    """Test saving and loading cached responses."""

    with tempfile.TemporaryDirectory() as temp_dir:
        cache = ResponseCacheManager(cache_dir=temp_dir)

        # Mock response
        mock_response = {
            "markdown": "Test analysis for TMEM14E",
            "citations": [{"url": "https://example.com", "title": "Test"}],
            "provider": "perplexity",
            "model": "sonar-deep-research",
            "duration_seconds": 5.0
        }

        # Save
        cache_path = cache.save(
            preset="perplexity-sonar-pro",
            genes=["TMEM14E"],
            context="cells",
            response=mock_response
        )

        assert cache_path.exists()
        assert cache_path.suffix == ".json"

        # Load
        loaded = cache.load(
            preset="perplexity-sonar-pro",
            genes=["TMEM14E"],
            context="cells"
        )

        assert loaded is not None
        assert loaded["markdown"] == "Test analysis for TMEM14E"
        assert loaded["provider"] == "perplexity"


@pytest.mark.unit
def test_load_nonexistent_cache() -> None:
    """Test loading from cache when file doesn't exist."""

    with tempfile.TemporaryDirectory() as temp_dir:
        cache = ResponseCacheManager(cache_dir=temp_dir)

        loaded = cache.load(
            preset="nonexistent-preset",
            genes=["FAKE_GENE"],
            context="fake context"
        )

        assert loaded is None


@pytest.mark.unit
def test_cache_filename_generation() -> None:
    """Test human-readable cache filename generation."""

    with tempfile.TemporaryDirectory() as temp_dir:
        cache = ResponseCacheManager(cache_dir=temp_dir)

        mock_response = {
            "markdown": "test",
            "citations": [],
            "provider": "perplexity",
            "model": "sonar",
            "duration_seconds": 1.0
        }

        cache_path = cache.save(
            preset="perplexity-sonar-pro",
            genes=["TMEM14E"],
            context="cells",
            response=mock_response
        )

        filename = cache_path.name

        # Should contain gene and preset info
        assert "tmem14e" in filename.lower()
        assert "perplexity-sonar-pro" in filename.lower()
        # Should have hash for uniqueness
        assert len(filename) > 20


@pytest.mark.unit
def test_cache_preserves_metadata() -> None:
    """Test that cached data includes metadata."""

    with tempfile.TemporaryDirectory() as temp_dir:
        cache = ResponseCacheManager(cache_dir=temp_dir)

        mock_response = {
            "markdown": "test",
            "citations": [],
            "provider": "perplexity",
            "model": "sonar",
            "duration_seconds": 1.0
        }

        cache_path = cache.save(
            preset="test-preset",
            genes=["TMEM14E"],
            context="cells",
            response=mock_response
        )

        # Read raw file to check structure
        with open(cache_path) as f:
            cache_data = json.load(f)

        assert "preset" in cache_data
        assert "genes" in cache_data
        assert "context" in cache_data
        assert "cache_key" in cache_data
        assert "response" in cache_data
        assert "cached_at" in cache_data


@pytest.mark.unit
def test_multiple_presets_different_caches() -> None:
    """Test that different presets create different cache files."""

    with tempfile.TemporaryDirectory() as temp_dir:
        cache = ResponseCacheManager(cache_dir=temp_dir)

        mock_response = {
            "markdown": "test",
            "citations": [],
            "provider": "perplexity",
            "model": "sonar",
            "duration_seconds": 1.0
        }

        # Save with preset 1
        path1 = cache.save(
            preset="perplexity-sonar-pro",
            genes=["TMEM14E"],
            context="cells",
            response=mock_response
        )

        # Save with preset 2 (same genes/context)
        path2 = cache.save(
            preset="perplexity-sonar-schema-embedded",
            genes=["TMEM14E"],
            context="cells",
            response=mock_response
        )

        # Should create different files
        assert path1 != path2
        assert path1.exists()
        assert path2.exists()
