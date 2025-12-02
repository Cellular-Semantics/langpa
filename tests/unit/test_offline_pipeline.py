"""Offline pipeline integration test (markdown -> report + citations map)."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from langpa.services.markdown_citation_extractor import extract_citations_from_markdown


class FakeResolver:
    def __init__(self) -> None:
        self.calls: list[list[dict[str, str]]] = []

    def resolve(self, citations: list[dict[str, str]]) -> dict[str, object]:
        self.calls.append(citations)
        return {
            "citations": {
                c["source_id"]: {"id": c["source_id"], "URL": c["source_url"]} for c in citations
            },
            "stats": {"total": len(citations), "resolved": len(citations), "unresolved": 0},
            "failures": [],
        }


@pytest.mark.unit
def test_offline_markdown_pipeline_builds_container() -> None:
    """Parse markdown with bibliography, validate report, and build container with citation map."""
    from langpa.services.output_manager import OutputManager

    markdown = """
<think>reasoning...</think>

```json
{
  "context": {"cell_type": "astrocyte", "disease": "gliosis"},
  "input_genes": ["TP53"],
  "programs": [{
    "program_name": "Test",
    "description": "d",
    "predicted_cellular_impact": ["impact"],
    "evidence_summary": "ev",
    "significance_score": 0.5,
    "citations": [{"source_id": "1", "notes": "n"}],
    "supporting_genes": ["TP53"]
  }],
  "version": "1"
}
```

## Citations
1. https://paper-one
2. https://paper-two
"""

    citations = extract_citations_from_markdown(markdown)

    # simulate offline result carrying citations extracted from markdown
    class DummyResult:
        def __init__(self, markdown: str, citations: list[dict[str, str]]) -> None:
            self.markdown = markdown
            self.citations = citations
            self.provider = "offline"
            self.model = "offline"
            self.duration_seconds = None

    result = DummyResult(markdown, citations)

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)
        resolver = FakeResolver()

        processing = manager.process_and_save_structured_output(
            result,
            genes=["TP53"],
            context="gliosis",
            resolve_citations=True,
            resolver=resolver,
        )

        assert processing["success"] is True
        assert "container_file" in processing and processing["container_file"]
        container = json.loads(Path(processing["container_file"]).read_text())

        # Report should use source_id only; citation map holds URLs
        assert container["report"]["programs"][0]["citations"][0]["source_id"] == "1"
        assert "source_url" not in container["report"]["programs"][0]["citations"][0]

        assert container["citations"]["1"]["URL"] == "https://paper-one"
        assert container["citations"]["2"]["URL"] == "https://paper-two"
        # Resolver received normalized citations with numbering preserved
        assert resolver.calls[0][0]["source_id"] == "1"
        assert resolver.calls[0][1]["source_id"] == "2"
