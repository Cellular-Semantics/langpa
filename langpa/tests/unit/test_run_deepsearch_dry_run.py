"""Tests for dry-run output in scripts/run_deepsearch.py."""

from __future__ import annotations

import argparse

import pytest

from scripts.run_deepsearch import show_dry_run


class DummyConfig:
    def __init__(self, provider_params: dict, prompt_template: str) -> None:
        self.provider = "perplexity"
        self.model = "sonar-reasoning-pro"
        self.provider_params = provider_params
        self.prompt_template = prompt_template


class DummyService:
    def __init__(self, provider_params: dict, prompt_template: str) -> None:
        self.config = DummyConfig(provider_params, prompt_template)

    def construct_prompt(self, genes, context, template_override=None):
        return f"PROMPT for {','.join(genes)} in {context} using {template_override or self.config.prompt_template}"

    # Reuse the real resolution logic via monkeypatching load_schema in tests
    def _resolve_system_prompt(self, provider_params, schema, template_requires_schema):
        from langpa.services.deepsearch_service import DeepSearchService

        # use a real service instance to run the resolution logic
        resolver = object.__new__(DeepSearchService)
        resolver.config = self.config  # type: ignore[attr-defined]
        return DeepSearchService._resolve_system_prompt(
            resolver,
            provider_params=provider_params,
            schema=schema,
            template_requires_schema=template_requires_schema,
        )


@pytest.fixture(autouse=True)
def patch_schema(monkeypatch):
    monkeypatch.setattr("scripts.run_deepsearch.load_schema", lambda _: {"type": "object"})


@pytest.mark.unit
def test_dry_run_shows_schema_embedded_system_prompt(capsys):
    service = DummyService(
        provider_params={
            "search_recency_filter": "month",
            "system_prompt": (
                "You are an expert researcher providing comprehensive, well-cited information."
            ),
        },
        prompt_template="gene_analysis_schema_embedded"
    )
    args = argparse.Namespace(
        preset=None,
        template="gene_analysis_schema_embedded",
        timeout=180,
        reasoning_effort=None,
        search_recency=None,
        custom_prompt=None,
        model=None,
    )

    show_dry_run(service, ["TP53"], "cancer", args)
    out = capsys.readouterr().out

    assert "You are an expert researcher providing comprehensive, well-cited information." in out
    assert "gene_analysis_schema_embedded" in out


@pytest.mark.unit
def test_dry_run_shows_legacy_schema_in_system_prompt(capsys):
    service = DummyService(
        provider_params={
            "search_recency_filter": "month",
            "system_prompt": (
                "You are an expert biologist. Analyze the provided genes.\n"
                "CRITICAL: Respond ONLY with valid JSON that exactly follows this schema structure:\n"
                "{schema}\n"
            ),
        },
        prompt_template="gene_analysis_academic"
    )
    args = argparse.Namespace(
        preset=None,
        template=None,
        timeout=180,
        reasoning_effort=None,
        search_recency=None,
        custom_prompt=None,
        model=None,
    )

    show_dry_run(service, ["TP53"], "cancer", args)
    out = capsys.readouterr().out

    assert "CRITICAL: Respond ONLY with valid JSON" in out
    assert '"type"' in out  # schema should be embedded


@pytest.mark.unit
def test_dry_run_respects_custom_system_prompt(capsys):
    custom_prompt = "CUSTOM SYSTEM PROMPT"
    service = DummyService(
        provider_params={"system_prompt": custom_prompt},
        prompt_template="gene_analysis_academic"
    )
    args = argparse.Namespace(
        preset=None,
        template=None,
        timeout=180,
        reasoning_effort=None,
        search_recency=None,
        custom_prompt=None,
        model=None,
    )

    show_dry_run(service, ["TP53"], "cancer", args)
    out = capsys.readouterr().out

    assert custom_prompt in out
    # Should not overwrite with schema text
    assert "CRITICAL: Respond ONLY with valid JSON" not in out
