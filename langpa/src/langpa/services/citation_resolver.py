"""Wrapper for resolving DeepSearch citations with url2ref."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Any

from lit_agent.identifiers.api import (  # type: ignore[import-untyped]
    CitationResolutionResult,
    render_bibliography_to_strings,
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

    def resolve_with_compact(
        self,
        citations: Iterable[dict[str, str]],
        *,
        style: str = "vancouver",
        locale: str = "en-US",
        metadata_lookup: Callable[[Any, str], dict[str, Any] | None] | None = None,
    ) -> dict[str, Any]:
        """Resolve citations and generate compact bibliography strings.

        Args:
            citations: Iterable of dictionaries containing ``source_id`` and ``source_url``.
            style: Citation style for rendering (default: vancouver).
            locale: Locale for formatting (default: en-US).
            metadata_lookup: Optional callable passed to url2ref for metadata enrichment.

        Returns:
            Dict with ``citations``, ``stats``, ``failures``, and ``compact_bibliography``.

            The ``compact_bibliography`` dict includes:

            - entries: List of rendered citation strings
            - style: Citation style used
            - locale: Locale used
            - renderer: Renderer used (citeproc-py or fallback)
            - error: Error message if fallback was used (optional)

        Example:

            .. code-block:: python

                resolver = CitationResolver()
                result = resolver.resolve_with_compact(
                    [{"source_id": "1", "source_url": "https://pubmed.ncbi.nlm.nih.gov/123456"}],
                    style="apa",
                    locale="en-GB"
                )
                print(result["compact_bibliography"]["entries"][0])
                # "[1] Author et al. Title 2024 123456"
        """
        # Resolve citations using existing method
        resolution = self.resolve(citations, metadata_lookup=metadata_lookup)

        # Generate compact strings using url2ref renderer
        compact_strings, compact_meta = render_bibliography_to_strings(
            resolution["resolution_result"],
            style=style,
            locale=locale,
        )

        return {
            "citations": resolution["citations"],
            "stats": resolution["stats"],
            "failures": resolution["failures"],
            "compact_bibliography": {
                "entries": compact_strings,
                "style": style,
                "locale": locale,
                "renderer": compact_meta.get("renderer"),
                "error": compact_meta.get("error"),  # Present if fallback was used
            },
        }
