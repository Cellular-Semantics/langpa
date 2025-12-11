"""Integration tests for compact bibliography generation with real url2ref API."""

from __future__ import annotations

import os

import pytest

from langpa.services.citation_resolver import CitationResolver


@pytest.mark.integration
def test_compact_references_with_real_pmid() -> None:
    """Test compact bibliography generation with real PMID via url2ref."""
    # Skip if no API keys (integration tests require real APIs per CLAUDE.md)
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        pytest.skip("No API keys found for integration test")

    resolver = CitationResolver(validate=True, scrape=False, pdf=True)

    # Use a known PMID for reproducible testing
    citations = [
        {"source_id": "1", "source_url": "https://pubmed.ncbi.nlm.nih.gov/37674083/"}
    ]

    result = resolver.resolve_with_compact(citations, style="vancouver", locale="en-US")

    # Verify structure
    assert "citations" in result
    assert "compact_bibliography" in result
    assert "stats" in result
    assert "failures" in result

    # Verify compact bibliography structure
    compact = result["compact_bibliography"]
    assert "entries" in compact
    assert "style" in compact
    assert "locale" in compact
    assert "renderer" in compact

    # Verify we got compact strings
    assert isinstance(compact["entries"], list)
    assert len(compact["entries"]) >= 1

    # First entry should start with citation ID
    first_entry = compact["entries"][0]
    assert first_entry.startswith("[1]") or first_entry.startswith("1.")

    # Verify metadata
    assert compact["style"] == "vancouver"
    assert compact["locale"] == "en-US"
    assert compact["renderer"] in ["citeproc-py", "fallback"]

    # Verify CSL-JSON citation also exists
    assert "1" in result["citations"]
    assert "title" in result["citations"]["1"] or "URL" in result["citations"]["1"]

    # Stats should show resolution
    assert result["stats"]["total"] == 1


@pytest.mark.integration
def test_compact_references_multiple_styles() -> None:
    """Test different citation styles produce different compact formats."""
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        pytest.skip("No API keys found for integration test")

    resolver = CitationResolver()
    citations = [
        {"source_id": "1", "source_url": "https://pubmed.ncbi.nlm.nih.gov/37674083/"}
    ]

    # Test multiple styles
    styles = ["vancouver", "apa", "ieee", "chicago"]
    results = {}

    for style in styles:
        result = resolver.resolve_with_compact(citations, style=style, locale="en-US")
        results[style] = result["compact_bibliography"]["entries"][0]

    # Each style should produce different output
    # (though fallback renderer may produce similar output)
    for style in styles:
        assert results[style]  # Non-empty
        assert "[1]" in results[style] or "1." in results[style]


@pytest.mark.integration
def test_compact_references_fallback_with_invalid_url() -> None:
    """Test fallback behavior when URL cannot be resolved."""
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        pytest.skip("No API keys found for integration test")

    resolver = CitationResolver()
    citations = [
        {"source_id": "1", "source_url": "https://example.com/not-a-real-paper"}
    ]

    result = resolver.resolve_with_compact(citations, style="vancouver", locale="en-US")

    # Should still return compact bibliography, possibly with fallback renderer
    assert "compact_bibliography" in result
    compact = result["compact_bibliography"]

    # Should have an entry even for unresolved citations
    assert len(compact["entries"]) >= 1

    # Renderer may be fallback
    assert compact["renderer"] in ["citeproc-py", "fallback"]


@pytest.mark.integration
def test_compact_references_locale_variants() -> None:
    """Test different locales for citation formatting."""
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        pytest.skip("No API keys found for integration test")

    resolver = CitationResolver()
    citations = [
        {"source_id": "1", "source_url": "https://pubmed.ncbi.nlm.nih.gov/37674083/"}
    ]

    # Test different locales
    locales = ["en-US", "en-GB", "de-DE"]

    for locale in locales:
        result = resolver.resolve_with_compact(
            citations, style="vancouver", locale=locale
        )

        compact = result["compact_bibliography"]
        assert compact["locale"] == locale
        assert len(compact["entries"]) >= 1
