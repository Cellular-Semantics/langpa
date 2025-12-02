"""Normalize DeepSearch citation outputs into ordered source_id/source_url entries."""

from __future__ import annotations

from typing import Any


def normalize_citations(citations: list[Any]) -> list[dict[str, str]]:
    """Normalize DeepSearch citations to ordered {source_id, source_url} entries.

    - Accepts either raw URL strings or dicts containing source_id/source_url/url.
    - Preserves provided source_id values; fills missing ones using sequential numbering
      after the highest numeric source_id observed (default starting at 1).
    - Skips entries that lack a URL.
    """
    if not citations:
        return []

    max_numeric_id = 0
    for citation in citations:
        if not isinstance(citation, dict):
            continue
        source_id = citation.get("source_id")
        if source_id is None:
            continue
        source_id_str = str(source_id)
        if source_id_str.isdigit():
            max_numeric_id = max(max_numeric_id, int(source_id_str))

    next_id = max_numeric_id + 1 if max_numeric_id else 1
    normalized: list[dict[str, str]] = []

    for citation in citations:
        source_id: str | None = None
        source_url: str | None = None

        if isinstance(citation, str):
            source_url = citation
        elif isinstance(citation, dict):
            if citation.get("source_id") is not None:
                source_id = str(citation["source_id"])
            source_url = citation.get("source_url") or citation.get("url")
        else:
            continue  # Unsupported type; skip

        if source_url is None:
            continue

        if source_id is None:
            source_id = str(next_id)
            next_id += 1
        elif source_id.isdigit():
            parsed_id = int(source_id)
            if parsed_id >= next_id:
                next_id = parsed_id + 1

        normalized.append({"source_id": source_id, "source_url": source_url})

    return normalized
