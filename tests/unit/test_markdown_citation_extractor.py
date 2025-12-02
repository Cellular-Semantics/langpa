"""Tests for markdown citation extraction."""

from __future__ import annotations

from langpa.services.markdown_citation_extractor import extract_citations_from_markdown


def test_bibliography_block_with_numbering_skips_schema_url() -> None:
    markdown = """
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

Some text.

1. https://paper-one
2. https://paper-two
"""
    citations = extract_citations_from_markdown(markdown)
    assert citations == [
        {"source_id": "1", "source_url": "https://paper-one"},
        {"source_id": "2", "source_url": "https://paper-two"},
    ]


def test_fallback_links_assign_sequential_without_numbers() -> None:
    markdown = """
Some text with [link](https://paper-a) and another https://paper-b
"""
    citations = extract_citations_from_markdown(markdown)
    urls = [c["source_url"] for c in citations]
    assert urls == ["https://paper-a", "https://paper-b"]
    assert all("source_id" not in c for c in citations)


def test_mixed_footnotes_and_links_prefers_numbered_ids() -> None:
    markdown = """
[3] https://paper-c
[4] https://paper-d
Additional link [note](https://paper-e)
"""
    citations = extract_citations_from_markdown(markdown)
    assert citations[0]["source_id"] == "3"
    assert citations[1]["source_id"] == "4"
    assert citations[2]["source_url"] == "https://paper-e"
