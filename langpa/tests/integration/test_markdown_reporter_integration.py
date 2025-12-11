"""Integration test rendering Markdown from a real container output."""

from __future__ import annotations

from pathlib import Path

import pytest

from langpa.services.markdown_reporter import MarkdownReportGenerator


@pytest.mark.integration
def test_render_from_real_container() -> None:
    """Render Markdown from an existing container and ensure required sections appear."""
    container_path = Path("outputs/deepsearch_20251126_203731_unspecified_genes_unspecified_context_container.json")
    if not container_path.exists():
        raise AssertionError(f"Container fixture missing: {container_path}")

    generator = MarkdownReportGenerator(strict_citations=False)
    markdown = generator.render_from_path(container_path)

    assert "Bibliography" in markdown
    # Check that at least one required genes section from fixture is present
    assert "Required genes" in markdown
    # Ensure citation numbering appears
    assert "[1]" in markdown
    assert any("Missing bibliography entries" in warn for warn in generator.warnings)
