"""Tests for CitationResolver wrapper."""

from __future__ import annotations

from typing import Any

import pytest

from langpa.services.citation_resolver import CitationResolver


class DummyResolutionResult:
    """Simple stand-in for url2ref's CitationResolutionResult."""

    def __init__(self, citations: dict[str, dict[str, Any]]) -> None:
        self.citations = citations
        self.stats = {"total": len(citations), "resolved": len(citations), "unresolved": 0}
        self.failures: list[str] = []


@pytest.mark.unit
def test_resolver_passes_bibliography(monkeypatch: pytest.MonkeyPatch) -> None:
    """Ensure CitationResolver maps source_url to url2ref bibliography and returns dict."""
    calls: list[dict[str, Any]] = []

    def fake_resolve_bibliography(bibliography: list[dict[str, str]], **kwargs: Any) -> DummyResolutionResult:
        calls.append({"bibliography": bibliography, "kwargs": kwargs})
        return DummyResolutionResult({"1": {"id": "1", "URL": bibliography[0]["url"]}})

    monkeypatch.setattr(
        "langpa.services.citation_resolver.resolve_bibliography", fake_resolve_bibliography
    )

    resolver = CitationResolver(validate=False, scrape=True, pdf=False, topic_validation=True)
    citations = [{"source_id": "1", "source_url": "https://paper"}]

    result = resolver.resolve(citations)

    assert calls, "resolve_bibliography should be invoked"
    assert calls[0]["bibliography"] == [{"source_id": "1", "url": "https://paper"}]
    assert calls[0]["kwargs"]["validate"] is False
    assert calls[0]["kwargs"]["scrape"] is True
    assert calls[0]["kwargs"]["pdf"] is False
    assert calls[0]["kwargs"]["topic_validation"] is True

    assert result["citations"]["1"]["URL"] == "https://paper"
    assert result["stats"]["resolved"] == 1
    assert result["failures"] == []


@pytest.mark.unit
def test_resolver_skips_missing_urls(monkeypatch: pytest.MonkeyPatch) -> None:
    """Citations without source_url should be ignored."""
    calls: list[list[dict[str, str]]] = []

    def fake_resolve_bibliography(bibliography: list[dict[str, str]], **kwargs: Any) -> DummyResolutionResult:
        calls.append(bibliography)
        return DummyResolutionResult({})

    monkeypatch.setattr(
        "langpa.services.citation_resolver.resolve_bibliography", fake_resolve_bibliography
    )

    resolver = CitationResolver()
    citations = [
        {"source_id": "1", "source_url": "https://paper"},
        {"source_id": "2"},  # missing source_url, should be skipped
    ]

    result = resolver.resolve(citations)

    assert calls[0] == [{"source_id": "1", "url": "https://paper"}]
    assert result["citations"] == {}
