"""Integration-style test for project/query output layout."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from langpa.services.markdown_citation_extractor import extract_citations_from_markdown
from langpa.services.output_manager import OutputManager
from langpa.utils.output_paths import build_run_directory


@pytest.mark.unit  # lightweight integration-style using filesystem only
def test_outputs_land_in_project_query_run_dir() -> None:
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
"""

    citations = extract_citations_from_markdown(markdown)

    class DummyResult:
        def __init__(self, markdown: str, citations: list) -> None:
            self.markdown = markdown
            self.citations = citations
            self.provider = "offline"
            self.model = "offline"
            self.duration_seconds = None

    result = DummyResult(markdown, citations)

    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        project = "proj"
        query = "query"
        run_dir = build_run_directory(base, project, query)

        manager = OutputManager(output_dir=run_dir)
        processing = manager.process_and_save_structured_output(
            result,
            genes=["TP53"],
            context="gliosis",
            resolve_citations=False,
            metadata={"project": project, "query": query},
            filename_prefix="deepsearch",
        )

        # Raw file should exist under run_dir
        raw_files = list(run_dir.glob("*.json"))
        assert raw_files, "No JSON files written to run_dir"
        assert {p.name for p in raw_files} == {"deepsearch_structured.json"}

        # Structured file present and under the run_dir
        assert processing["structured_file"]
        structured_path = Path(processing["structured_file"])
        assert structured_path.parent == run_dir
        assert structured_path.name == "deepsearch_structured.json"

        payload = json.loads(structured_path.read_text())
        assert payload["metadata"]["project"] == project
        assert payload["metadata"]["context"] == "gliosis"
