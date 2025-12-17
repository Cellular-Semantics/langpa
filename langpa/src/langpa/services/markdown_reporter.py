"""Markdown report generator for DeepSearch schema outputs."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

# Ensure environment variables are loaded for any downstream dependencies
load_dotenv()


@dataclass
class Bibliography:
    """Normalized bibliography entries keyed by source_id."""

    order: list[str]
    entries: dict[str, dict[str, Any]]
    compact_entries: list[str] | None = None


class MarkdownReportGenerator:
    """Render Markdown from structured DeepSearch outputs."""

    def __init__(self, *, strict_citations: bool = True) -> None:
        self.strict_citations = strict_citations
        self.warnings: list[str] = []

    def render_from_path(self, path: Path) -> str:
        """Load container/structured JSON from disk and render Markdown.

        Args:
            path: Path to a container or structured JSON file.

        Returns:
            Rendered Markdown string.
        """
        data = json.loads(path.read_text(encoding="utf-8"))
        return self.render_from_container(data)

    def render_from_container(self, container: dict[str, Any]) -> str:
        """Render Markdown from an in-memory container/structured payload.

        Args:
            container: Parsed JSON output containing a `report` (or `structured_data`)
                section and citation metadata.

        Returns:
            Markdown string.

        Raises:
            ValueError: If citation references do not align with bibliography entries.
        """
        structured = (
            container.get("report")
            or container.get("structured_data")
            or container.get("deepsearch_output")
            or {}
        )
        if not structured:
            raise ValueError("No structured report found in container payload.")

        bibliography = self._normalize_bibliography(container)
        cited_ids = self._collect_cited_ids(structured)
        self._validate_citations(cited_ids, bibliography)

        lines: list[str] = []
        lines.append("# Gene Program Markdown Report")
        context = structured.get("context", {})
        lines.append("")
        lines.append("## Context")
        lines.append(
            f"- Cell type: {context.get('cell_type', 'n/a')}"
            f"\n- Disease: {context.get('disease', 'n/a')}"
            f"\n- Tissue: {context.get('tissue', 'n/a')}"
        )

        input_genes = structured.get("input_genes") or []
        lines.append("")
        lines.append("## Input Genes")
        genes_preview = ", ".join(input_genes[:25])
        if len(input_genes) > 25:
            genes_preview += f", ... ({len(input_genes)} total)"
        lines.append(genes_preview or "None provided")

        programs = structured.get("programs") or []
        for program in programs:
            lines.extend(self._render_program(program))

        lines.append("")
        lines.append("## Bibliography")
        if bibliography.compact_entries:
            # Compact entries already have numbers, render as-is
            for entry in bibliography.compact_entries:
                lines.append(entry)
        else:
            # Fallback to manual rendering if no compact entries
            for source_id in bibliography.order:
                entry = bibliography.entries.get(source_id, {})
                title = entry.get("title") or entry.get("Title") or entry.get("id") or ""
                url = entry.get("URL") or entry.get("source_url") or entry.get("url") or ""
                label = entry.get("id") or source_id
                compact = entry.get("compact") or title
                composed = compact.strip() if isinstance(compact, str) else str(compact)
                suffix = f" {url}" if url else ""
                lines.append(f"{label}. [{source_id}] {composed}{suffix}")

        return "\n".join(lines).strip() + "\n"

    def _render_program(self, program: dict[str, Any]) -> list[str]:
        """Render a single program section."""
        lines: list[str] = []
        name = program.get("program_name", "Unnamed Program")
        lines.append("")
        lines.append(f"## Program: {name}")
        if program.get("description"):
            lines.append(program["description"])
        impacts = program.get("predicted_cellular_impact") or []
        if impacts:
            lines.append("")
            lines.append("**Predicted impacts**")
            for impact in impacts:
                lines.append(f"- {impact}")
        if program.get("evidence_summary"):
            lines.append("")
            lines.append("**Evidence summary**")
            lines.append(program["evidence_summary"])

        lines.extend(self._render_atomic_terms(program))
        lines.extend(self._render_required_genes(program))

        citations = program.get("citations") or []
        if citations:
            lines.append("")
            lines.append("**Program citations**")
            for citation in citations:
                sid = citation.get("source_id")
                if not sid:
                    continue
                note = citation.get("notes", "")
                note_part = f": {note}" if note else ""
                lines.append(f"- [{sid}]{note_part}")
        return lines

    def _render_atomic_terms(self, program: dict[str, Any]) -> list[str]:
        """Render atomic biological processes and cellular components."""
        lines: list[str] = []

        def render_block(title: str, terms: list[dict[str, Any]]) -> None:
            if not terms:
                return
            lines.append("")
            lines.append(f"**{title}**")
            for term in terms:
                name = term.get("name", "Unnamed")
                genes = term.get("genes") or []
                genes_part = f" Genes: {', '.join(genes)}" if genes else ""
                lines.append(f"- {name}.{genes_part}")
                citations = term.get("citations") or []
                for citation in citations:
                    sid = citation.get("source_id")
                    if not sid:
                        continue
                    note = citation.get("notes", "")
                    note_part = f": {note}" if note else ""
                    lines.append(f"  - [{sid}]{note_part}")

        render_block("Atomic biological processes", program.get("atomic_biological_processes") or [])
        render_block(
            "Atomic cellular components", program.get("atomic_cellular_components") or []
        )

        return lines

    def _render_required_genes(self, program: dict[str, Any]) -> list[str]:
        """Render required genes not in input with citations."""
        required = program.get("required_genes_not_in_input") or {}
        genes = required.get("genes") or []
        citations = required.get("citations") or []

        if not genes and not citations:
            return []

        lines: list[str] = []
        lines.append("")
        lines.append("**Required genes (not in input)**")
        if genes:
            lines.append(f"- Genes: {', '.join(genes)}")
        for citation in citations:
            sid = citation.get("source_id")
            if not sid:
                continue
            note = citation.get("notes", "")
            note_part = f": {note}" if note else ""
            lines.append(f"  - [{sid}]{note_part}")

        return lines

    def _normalize_bibliography(self, container: dict[str, Any]) -> Bibliography:
        """Normalize bibliography input."""
        compact_entries = None
        if container.get("compact_bibliography"):
            compact_entries = container["compact_bibliography"].get("entries")

        citations_raw = container.get("citations") or []
        order: list[str] = []
        entries: dict[str, dict[str, Any]] = {}

        if isinstance(citations_raw, dict):
            for key, value in citations_raw.items():
                entries[str(key)] = value if isinstance(value, dict) else {"id": str(key)}
            # Preserve numeric ordering if possible; fallback to insertion order
            try:
                order = sorted(entries.keys(), key=lambda x: int(x))
            except ValueError:
                order = list(entries.keys())
        elif isinstance(citations_raw, list):
            for item in citations_raw:
                if isinstance(item, dict) and item.get("source_id"):
                    source_id = str(item["source_id"])
                    entries[source_id] = item
                    order.append(source_id)
        else:
            order = []

        return Bibliography(order=order, entries=entries, compact_entries=compact_entries)

    def _collect_cited_ids(self, structured: dict[str, Any]) -> set[str]:
        """Collect all source_id strings referenced in the structured payload."""
        cited: set[str] = set()

        def walk(node: Any) -> None:
            if isinstance(node, dict):
                if "source_id" in node:
                    cited.add(str(node["source_id"]))
                for value in node.values():
                    walk(value)
            elif isinstance(node, list):
                for item in node:
                    walk(item)

        walk(structured)
        return cited

    def _validate_citations(self, cited_ids: set[str], bibliography: Bibliography) -> None:
        """Validate that every citation has a corresponding bibliography entry."""
        missing = sorted(cid for cid in cited_ids if cid not in bibliography.entries)
        if missing:
            message = f"Missing bibliography entries for source_id(s): {', '.join(missing)}"
            if self.strict_citations:
                raise ValueError(message)
            self.warnings.append(message)

        if bibliography.order:
            # Ensure order list contains only known entries
            extra = sorted(cid for cid in bibliography.order if cid not in bibliography.entries)
            if extra:
                message = (
                    f"Bibliography order references unknown source_id(s): {', '.join(extra)}"
                )
                if self.strict_citations:
                    raise ValueError(message)
                self.warnings.append(message)
