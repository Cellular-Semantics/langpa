"""Utilities to extract citation URLs from DeepSearch markdown."""

from __future__ import annotations

import re
from collections.abc import Iterable


def extract_citations_from_markdown(markdown: str) -> list[dict[str, str]]:
    """Best-effort extraction of citation URLs from DeepSearch-style markdown.

    Strategy:
    - Ignore fenced code blocks (schema/JSON).
    - Prefer a contiguous bibliography block of `[n] URL` with sequential numbering starting at 1.
    - Otherwise gather footnotes, markdown links, then plain URLs (all sans fences), assigning
      source_id from footnote numbers when present; otherwise leave source_id unset.
    Returns a list of dicts with source_url and optional source_id, in order of appearance.
    """
    cleaned = _strip_code_fences(markdown)

    bibliography = _find_bibliography_block(cleaned)
    if bibliography:
        return [{"source_id": str(num), "source_url": url} for num, url in bibliography]

    # Fallback: footnotes, then links, then plain URLs
    seen: set[str] = set()
    citations: list[dict[str, str]] = []

    footnote_pattern = re.compile(r"^\s*\[(\d+)\]\s+(https?://\S+)", re.MULTILINE)
    for match in footnote_pattern.finditer(cleaned):
        num = match.group(1)
        url = _strip_trailing_punctuation(match.group(2))
        if url in seen:
            continue
        seen.add(url)
        citations.append({"source_id": num, "source_url": url})

    link_pattern = re.compile(r"\[[^\]]+\]\((https?://[^)\s]+)\)")
    for match in link_pattern.finditer(cleaned):
        url = _strip_trailing_punctuation(match.group(1))
        if url in seen:
            continue
        seen.add(url)
        citations.append({"source_url": url})

    plain_pattern = re.compile(r"(https?://[^\s)<>\]]+)")
    for match in plain_pattern.finditer(cleaned):
        url = _strip_trailing_punctuation(match.group(1))
        if url in seen:
            continue
        seen.add(url)
        citations.append({"source_url": url})

    return citations


def _strip_code_fences(markdown: str) -> str:
    """Remove fenced code blocks (``` ... ```) to avoid picking up schema/JSON URLs."""
    fence_pattern = re.compile(r"```.*?```", re.DOTALL)
    return fence_pattern.sub("", markdown)


def _find_bibliography_block(markdown: str) -> list[tuple[int, str]] | None:
    """Find a contiguous footnote block with sequential numbering starting at 1."""
    footnote_patterns = [
        re.compile(r"^\s*\[(\d+)\]\s+(https?://\S+)\s*$"),  # [1] URL
        re.compile(r"^\s*(\d+)[\.\)]\s+(https?://\S+)\s*$"),  # 1. URL or 1) URL
    ]
    lines = markdown.splitlines()

    best_block: list[tuple[int, str]] | None = None

    current: list[tuple[int, str]] = []
    for line in lines + [""]:  # sentinel to flush
        match = None
        for pattern in footnote_patterns:
            match = pattern.match(line)
            if match:
                num = int(match.group(1))
                url = _strip_trailing_punctuation(match.group(2))
                current.append((num, url))
                break
        if not match and current:
            is_sequential = _is_sequential_block(current)
            if is_sequential and (best_block is None or len(current) >= len(best_block)):
                # Prefer the last sequential block; if lengths tie, prefer later (end of doc)
                best_block = current
            current = []
    return best_block


def _is_sequential_block(block: Iterable[tuple[int, str]]) -> bool:
    """Check if block numbering starts at 1 and increments by 1."""
    numbers = [num for num, _ in block]
    if not numbers:
        return False
    return numbers[0] == 1 and numbers == list(range(1, len(numbers) + 1))


def _strip_trailing_punctuation(url: str) -> str:
    """Strip trailing punctuation that often sticks to URLs."""
    return url.rstrip(".,);]")
