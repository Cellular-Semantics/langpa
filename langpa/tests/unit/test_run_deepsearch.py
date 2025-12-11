"""Unit tests for run_deepsearch helpers."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.run_deepsearch import derive_query_name, process_batch


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
def test_process_batch_invokes_main_per_query(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    batch_root = tmp_path / "inputs"
    (batch_root / "q1").mkdir(parents=True)
    (batch_root / "q2").mkdir(parents=True)
    (batch_root / "q1" / "a.md").write_text("md1", encoding="utf-8")
    (batch_root / "q2" / "b.json").write_text("{}", encoding="utf-8")

    calls: list[dict[str, Any]] = []

    def fake_main_single_run(call_args: argparse.Namespace) -> None:
        calls.append(
            {
                "query": call_args.query,
                "from_markdown": call_args.from_markdown,
                "raw_input": call_args.raw_input,
            }
        )

    monkeypatch.setattr("scripts.run_deepsearch.main_single_run", fake_main_single_run)

    args = SimpleNamespace(
        batch_dir=batch_root,
        project="proj",
        query=None,
        from_markdown=None,
        raw_input=None,
        output_dir="outputs",
        resolve_citations=False,
        citations_file=None,
        preset=None,
        preferred_provider=None,
        model=None,
        reasoning_effort=None,
        search_recency=None,
        timeout=180,
        genes=None,
        context=None,
        context_file=None,
        genes_file=None,
        list_presets=False,
        list_templates=False,
        show_template=None,
        show_preset=None,
        provider=None,
        template=None,
        custom_prompt=None,
        dry_run=False,
        show_config=False,
        skip_structured=False,
        debug_extraction=False,
        print_markdown=False,
        citation_validate=True,
        citation_scrape=False,
        citation_pdf=True,
        citation_topic_validation=False,
    )

    process_batch(args)

    assert len(calls) == 2
    queries = {c["query"] for c in calls}
    assert queries == {"q1", "q2"}
    assert any(c["from_markdown"] and c["from_markdown"].name == "a.md" for c in calls)
    assert any(c["raw_input"] and c["raw_input"].name == "b.json" for c in calls)
