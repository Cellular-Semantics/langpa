"""Wrapper for resolving DeepSearch citations with url2ref."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Any

from lit_agent.identifiers.api import (  # type: ignore[import-untyped]
    CitationResolutionResult,
    resolve_bibliography,
)


class CitationResolver:
    """Resolve citation URLs into CSL-JSON entries keyed by source_id."""

    def __init__(
        self,
        *,
        validate: bool = True,
        scrape: bool = False,
        pdf: bool = True,
        topic_validation: bool = False,
    ) -> None:
        """Configure resolution strategy."""
        self.validate = validate
        self.scrape = scrape
        self.pdf = pdf
        self.topic_validation = topic_validation

    def resolve(
        self,
        citations: Iterable[dict[str, str]],
        *,
        metadata_lookup: Callable[[Any, str], dict[str, Any] | None] | None = None,
    ) -> dict[str, Any]:
        """Resolve citations.

        Args:
            citations: Iterable of dictionaries containing ``source_id`` and ``source_url``.
            metadata_lookup: Optional callable passed to url2ref for metadata enrichment.

        Returns:
            Dict with ``citations``, ``stats``, ``failures``, and ``resolution_result``.
        """
        bibliography = [
            {"source_id": citation["source_id"], "url": citation["source_url"]}
            for citation in citations
            if citation.get("source_url")
        ]

        result: CitationResolutionResult = resolve_bibliography(
            bibliography,
            validate=self.validate,
            scrape=self.scrape,
            pdf=self.pdf,
            topic_validation=self.topic_validation,
            metadata_lookup=metadata_lookup,
        )

        return {
            "citations": result.citations,
            "stats": result.stats,
            "failures": result.failures,
            "resolution_result": result,
        }
