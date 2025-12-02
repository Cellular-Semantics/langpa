"""Unit tests for container assembly with citation resolution."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

# Mock deep_research_client for import issues
import sys
from unittest.mock import Mock, MagicMock

mock_deep_research_client = MagicMock()
mock_deep_research_client.DeepResearchClient = Mock
sys.modules["deep_research_client"] = mock_deep_research_client


class MockResearchResult:
    def __init__(self, markdown: str, citations: list, provider: str = "perplexity"):
        self.markdown = markdown
        self.citations = citations
        self.provider = provider
        self.model = "sonar-deep-research"
        self.duration_seconds = 12.5


@pytest.mark.unit
def test_container_builds_with_resolution(monkeypatch: pytest.MonkeyPatch) -> None:
    """Container includes raw, report, citations map, and stats."""
    from langpa.services.output_manager import OutputManager

    fake_resolution = {
        "citations": {"1": {"id": "1", "URL": "https://paper"}},
        "stats": {"total": 1, "resolved": 1, "unresolved": 0},
        "failures": [],
    }

    def fake_resolve(_citations):
        return fake_resolution

    class FakeResolver:
        def resolve(self, citations):
            return fake_resolve(citations)

    result = MockResearchResult(
        markdown="""```json
{
  "context": {"cell_type": "neural", "disease": "cancer"},
  "input_genes": ["TP53"],
  "programs": [{
    "program_name": "Test",
    "description": "desc",
    "predicted_cellular_impact": ["impact"],
    "evidence_summary": "evidence",
    "significance_score": 0.5,
    "citations": [{"source_id": "1"}],
    "supporting_genes": ["TP53"]
  }],
  "version": "1.0"
}
```""",
        citations=["https://paper"],
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        manager = OutputManager(output_dir=temp_dir)

        processing_result = manager.process_and_save_structured_output(
            result=result,
            genes=["TP53"],
            context="cancer",
            resolve_citations=True,
            resolver=FakeResolver(),
            metadata={"run_id": "123"},
        )

        assert processing_result["success"] is True
        assert processing_result["container_file"] is not None
        container_path = Path(processing_result["container_file"])
        assert container_path.exists()

        payload = json.loads(container_path.read_text())
        assert payload["citations"] == fake_resolution["citations"]
        assert payload["bibliography_stats"] == fake_resolution["stats"]
        assert payload["deepsearch_raw"]["citations"] == ["https://paper"]
        assert payload["report"]["programs"][0]["citations"][0]["source_id"] == "1"
        assert "source_url" not in payload["report"]["programs"][0]["citations"][0]

        # Normalized citations captured for debugging
        assert processing_result["normalized_citations"] == [
            {"source_id": "1", "source_url": "https://paper"}
        ]
