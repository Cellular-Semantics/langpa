"""Unit tests for run_deepsearch helpers."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from types import SimpleNamespace
from typing import Any
from unittest.mock import Mock

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.run_deepsearch import derive_query_name


@pytest.mark.unit
def test_derive_query_name_prefers_parent_folder(tmp_path: Path) -> None:
    project = "proj"
    query_dir = tmp_path / project / "inputs" / "my_query"
    query_dir.mkdir(parents=True)
    input_path = query_dir / "run_1.md"
    input_path.write_text("content", encoding="utf-8")

    args = SimpleNamespace(
        query=None,
        project=project,
        context=None,
        genes=None,
        from_markdown=None,
        raw_input=None,
    )

    derived = derive_query_name(args, input_path)
    assert derived == "my_query"


@pytest.mark.unit
def test_derive_query_name_fallback_to_context() -> None:
    args = SimpleNamespace(
        query=None,
        project="proj",
        context="gliosis reactive astrocytes study",
        genes=[["TP53", "BRCA1", "EGFR", "MYC"]],
        genes_file=None,
        context_file=None,
        from_markdown=None,
        raw_input=None,
    )
    derived = derive_query_name(args, None)
    assert derived == "TP53_BRCA1_and_2_more_gliosis_reactive_ast"


@pytest.mark.unit
def test_derive_query_name_uses_path_when_no_genes_or_context(tmp_path: Path) -> None:
    project = "proj"
    query_dir = tmp_path / project / "inputs" / "my_query"
    query_dir.mkdir(parents=True)
    input_path = query_dir / "run_1.md"
    input_path.write_text("content", encoding="utf-8")

    args = SimpleNamespace(
        query=None,
        project=project,
        context=None,
        genes=None,
        from_markdown=None,
        raw_input=None,
    )

    derived = derive_query_name(args, input_path)
    assert derived == "my_query"


@pytest.mark.unit
def test_generate_markdown_report_creates_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Generating markdown from a container file should write to output."""
    from scripts import run_deepsearch

    container_payload = {
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
                }
            ],
            "version": "1.0",
        },
        "citations": [{"source_id": "1", "source_url": "https://example.com/one"}],
    }

    container_path = tmp_path / "sample_container.json"
    container_path.write_text(run_deepsearch.json.dumps(container_payload), encoding="utf-8")

    rendered_path = tmp_path / "rendered.md"

    class FakeGenerator:
        def __init__(self) -> None:
            self.calls = []

        def render_from_path(self, container_path: Path) -> str:
            data = json.loads(container_path.read_text(encoding="utf-8"))
            return self.render_from_container(data)

        def render_from_container(self, data: dict) -> str:
            self.calls.append(data)
            return "# report"

    fake_generator = FakeGenerator()

    def factory(**kwargs: Any) -> FakeGenerator:
        return fake_generator

    monkeypatch.setattr(run_deepsearch, "MarkdownReportGenerator", factory)

    output_path = run_deepsearch.generate_markdown_report(
        container_path=container_path, output_path=rendered_path
    )

    assert output_path == rendered_path
    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == "# report"


@pytest.mark.unit
def test_show_dry_run_constructs_prompt(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    """Test that show_dry_run can construct and display the prompt."""
    from scripts import run_deepsearch

    # Create a mock service with construct_prompt method
    mock_service = Mock()
    mock_service.config = Mock()
    mock_service.config.provider_params = {"return_citations": True, "search_domain_filter": ["pubmed.ncbi.nlm.nih.gov"]}
    mock_service.config.provider = "perplexity"
    mock_service.config.model = "sonar-deep-research"
    mock_service.config.prompt_template = "gene_analysis_schema_embedded"
    mock_service.config.timeout = 180
    mock_service.construct_prompt.return_value = "Test prompt for CCDC92 in context of obesity"

    # Create args namespace
    args = argparse.Namespace(
        preset="perplexity-sonar-schema-embedded",
        model="sonar-deep-research",
        custom_prompt=None,
        template=None,
        timeout=180,
        reasoning_effort=None,
        search_recency=None,
    )

    genes = ["CCDC92"]
    context = "obesity"

    # Call show_dry_run
    run_deepsearch.show_dry_run(mock_service, genes, context, args)

    # Verify construct_prompt was called
    mock_service.construct_prompt.assert_called_once_with(genes, context, template_override=None)

    # Check output contains the prompt
    captured = capsys.readouterr()
    assert "Test prompt for CCDC92 in context of obesity" in captured.out
    assert "DRY RUN MODE" in captured.out
    assert "No actual API call made (dry run mode)" in captured.out
