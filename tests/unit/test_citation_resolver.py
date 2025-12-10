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

    def fake_resolve_bibliography(
        bibliography: list[dict[str, str]], **kwargs: Any
    ) -> DummyResolutionResult:
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

    def fake_resolve_bibliography(
        bibliography: list[dict[str, str]], **kwargs: Any
    ) -> DummyResolutionResult:
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


@pytest.mark.unit
def test_resolver_returns_resolution_result(monkeypatch: pytest.MonkeyPatch) -> None:
    """Ensure resolve() returns the resolution_result for downstream rendering."""

    def fake_resolve_bibliography(
        bibliography: list[dict[str, str]], **kwargs: Any
    ) -> DummyResolutionResult:
        return DummyResolutionResult({"1": {"id": "1", "URL": "https://example.com"}})

    monkeypatch.setattr(
        "langpa.services.citation_resolver.resolve_bibliography",
        fake_resolve_bibliography
    )

    resolver = CitationResolver()
    citations = [{"source_id": "1", "source_url": "https://example.com"}]

    result = resolver.resolve(citations)

    # New assertion: resolution_result should be included
    assert "resolution_result" in result
    assert hasattr(result["resolution_result"], "citations")
    assert hasattr(result["resolution_result"], "stats")
    assert hasattr(result["resolution_result"], "failures")


@pytest.mark.unit
def test_resolve_with_compact_returns_compact_bibliography(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test resolve_with_compact() generates compact bibliography strings."""

    def fake_resolve_bibliography(
        bibliography: list[dict[str, str]], **kwargs: Any
    ) -> DummyResolutionResult:
        return DummyResolutionResult(
            {"1": {"id": "1", "title": "Test Paper", "URL": "https://example.com"}}
        )

    def fake_render_bibliography_to_strings(
        resolution_result: Any, style: str = "vancouver", locale: str = "en-US"
    ) -> tuple[list[str], dict[str, Any]]:
        return (
            ["[1] Author Test Paper 2024 https://example.com"],
            {"renderer": "citeproc-py", "style": style, "locale": locale}
        )

    monkeypatch.setattr(
        "langpa.services.citation_resolver.resolve_bibliography",
        fake_resolve_bibliography
    )
    monkeypatch.setattr(
        "langpa.services.citation_resolver.render_bibliography_to_strings",
        fake_render_bibliography_to_strings
    )

    resolver = CitationResolver()
    citations = [{"source_id": "1", "source_url": "https://example.com"}]

    result = resolver.resolve_with_compact(citations, style="apa", locale="en-GB")

    # Check structure includes compact_bibliography
    assert "citations" in result
    assert "stats" in result
    assert "failures" in result
    assert "compact_bibliography" in result

    # Check compact bibliography structure
    compact = result["compact_bibliography"]
    assert "entries" in compact
    assert isinstance(compact["entries"], list)
    assert len(compact["entries"]) == 1
    assert compact["entries"][0].startswith("[1]")

    # Check metadata
    assert compact["style"] == "apa"
    assert compact["locale"] == "en-GB"
    assert compact["renderer"] == "citeproc-py"
