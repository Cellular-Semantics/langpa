"""Tests for DeepSearch citation normalization."""

from __future__ import annotations

import pytest

from langpa.services.citation_normalizer import normalize_citations


@pytest.mark.unit
def test_normalize_urls_to_source_ids() -> None:
    """Normalize an array of citation URLs into ordered source_id entries."""
    citations = [
        "https://pubmed.ncbi.nlm.nih.gov/123/",
        "https://example.com/ref2",
    ]

    normalized = normalize_citations(citations)

    assert normalized == [
        {"source_id": "1", "source_url": "https://pubmed.ncbi.nlm.nih.gov/123/"},
        {"source_id": "2", "source_url": "https://example.com/ref2"},
    ]


@pytest.mark.unit
def test_preserves_existing_source_ids_and_fills_missing() -> None:
    """Keep provided source_ids and assign sequential ids for missing ones."""
    citations = [
        {"source_id": "5", "url": "https://first"},
        {"url": "https://second"},
    ]

    normalized = normalize_citations(citations)

    assert normalized == [
        {"source_id": "5", "source_url": "https://first"},
        {"source_id": "6", "source_url": "https://second"},
    ]


@pytest.mark.unit
def test_handles_empty_list() -> None:
    """Return empty list when no citations are provided."""
    assert normalize_citations([]) == []
