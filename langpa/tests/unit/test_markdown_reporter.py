"""Unit tests for Markdown report generation from structured/container JSON."""

from __future__ import annotations

from pathlib import Path

import pytest

from langpa.services.markdown_reporter import MarkdownReportGenerator


@pytest.mark.unit
def test_markdown_preserves_reference_order_and_citations() -> None:
    """Bibliography order should follow input citations and in-text citations must align."""
    container = {
        "report": {
            "context": {"cell_type": "astrocyte", "disease": "glioma", "tissue": "brain"},
            "input_genes": ["FOO1", "BAR2"],
            "programs": [
                {
                    "program_name": "Test Program",
                    "description": "Desc",
                    "predicted_cellular_impact": ["impact"],
                    "evidence_summary": "evidence",
                    "significance_score": 0.5,
                    "citations": [{"source_id": "1"}, {"source_id": "2"}],
                    "supporting_genes": ["FOO1"],
                }
            ],
            "version": "1.0",
        },
        "citations": [
            {"source_id": "1", "source_url": "https://example.com/one"},
            {"source_id": "2", "source_url": "https://example.com/two"},
        ],
    }

    generator = MarkdownReportGenerator()
    markdown = generator.render_from_container(container)

    assert "[1]" in markdown and "[2]" in markdown
    bibliography_section = markdown.split("Bibliography", maxsplit=1)[-1]
    first_ref_index = bibliography_section.index("1.")
    second_ref_index = bibliography_section.index("2.")
    assert first_ref_index < second_ref_index
    assert "https://example.com/one" in markdown
    assert "https://example.com/two" in markdown


@pytest.mark.unit
def test_missing_reference_raises_error(tmp_path: Path) -> None:
    """If a citation is referenced but missing in bibliography, raise ValueError."""
    container = {
        "report": {
            "context": {"cell_type": "astrocyte", "disease": "glioma", "tissue": "brain"},
            "input_genes": ["FOO1"],
            "programs": [
                {
                    "program_name": "Test Program",
                    "description": "Desc",
                    "predicted_cellular_impact": ["impact"],
                    "evidence_summary": "evidence",
                    "significance_score": 0.5,
                    "citations": [{"source_id": "3"}],
                    "supporting_genes": ["FOO1"],
                }
            ],
            "version": "1.0",
        },
        "citations": [{"source_id": "1", "source_url": "https://example.com/one"}],
    }

    generator = MarkdownReportGenerator()
    with pytest.raises(ValueError):
        generator.render_from_container(container)


@pytest.mark.unit
def test_uses_compact_bibliography_when_available(tmp_path: Path) -> None:
    """If compact bibliography entries exist, they should be used verbatim."""
    container = {
        "report": {
            "context": {"cell_type": "astrocyte", "disease": "glioma", "tissue": "brain"},
            "input_genes": ["FOO1"],
            "programs": [
                {
                    "program_name": "Test Program",
                    "description": "Desc",
                    "predicted_cellular_impact": ["impact"],
                    "evidence_summary": "evidence",
                    "significance_score": 0.5,
                    "citations": [{"source_id": "1"}],
                    "supporting_genes": ["FOO1"],
                    "atomic_biological_processes": [
                        {
                            "name": "Process A",
                            "genes": ["FOO1"],
                            "citations": [{"source_id": "1", "notes": "note A"}],
                        }
                    ],
                    "atomic_cellular_components": [
                        {
                            "name": "Component X",
                            "genes": ["FOO1"],
                            "citations": [{"source_id": "1", "notes": "note X"}],
                        }
                    ],
                }
            ],
            "version": "1.0",
        },
        "citations": {"1": {"id": "1", "URL": "https://example.com/one"}},
        "compact_bibliography": {"entries": ["[1] Custom Ref https://example.com/one"]},
    }

    generator = MarkdownReportGenerator()
    markdown = generator.render_from_container(container)

    assert "[1] Custom Ref" in markdown
    assert "https://example.com/one" in markdown
    assert "Process A" in markdown
    assert "note A" in markdown
    assert "Component X" in markdown


@pytest.mark.unit
def test_required_genes_rendering() -> None:
    """Required genes section should render genes and citation notes."""
    container = {
        "report": {
            "context": {"cell_type": "astrocyte", "disease": "glioma"},
            "input_genes": ["FOO1"],
            "programs": [
                {
                    "program_name": "Program",
                    "description": "Desc",
                    "predicted_cellular_impact": ["impact"],
                    "evidence_summary": "evidence",
                    "significance_score": 0.5,
                    "citations": [{"source_id": "1"}],
                    "supporting_genes": ["FOO1"],
                    "required_genes_not_in_input": {
                        "genes": ["REQ1", "REQ2"],
                        "citations": [{"source_id": "2", "notes": "needed"}],
                    },
                }
            ],
            "version": "1.0",
        },
        "citations": [
            {"source_id": "1", "source_url": "https://example.com/one"},
            {"source_id": "2", "source_url": "https://example.com/two"},
        ],
    }

    generator = MarkdownReportGenerator()
    markdown = generator.render_from_container(container)

    assert "Required genes" in markdown
    assert "REQ1" in markdown and "REQ2" in markdown
    assert "[2]" in markdown and "needed" in markdown


@pytest.mark.unit
def test_compact_bibliography_rendering_no_double_numbering() -> None:
    """Compact bibliography entries should be rendered as-is without extra numbering."""
    container = {
        "report": {
            "context": {"cell_type": "astrocyte"},
            "input_genes": ["FOO1"],
            "programs": [
                {
                    "program_name": "Test",
                    "description": "Desc",
                    "predicted_cellular_impact": ["impact"],
                    "evidence_summary": "evidence",
                    "significance_score": 0.5,
                    "citations": [{"source_id": "1"}],
                    "supporting_genes": ["FOO1"],
                }
            ],
            "version": "1.0",
        },
        "citations": {"1": {"id": "1", "URL": "https://example.com/one"}},
        "compact_bibliography": {
            "entries": [
                "[1] Doe J, Smith A. Example Paper. Nature 2024. 10.1038/example",
                "[2] Jones B. Another Paper. Science 2023. PMID:12345"
            ]
        },
    }

    generator = MarkdownReportGenerator()
    markdown = generator.render_from_container(container)

    # Should NOT have double numbering
    assert "1. [1]" not in markdown
    assert "2. [2]" not in markdown

    # Should have clean entries
    assert "[1] Doe J, Smith A. Example Paper" in markdown
    assert "[2] Jones B. Another Paper" in markdown
