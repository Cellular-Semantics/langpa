#!/usr/bin/env python3
"""CLI to run DeepSearchService with file/arg inputs and capture outputs."""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from pathlib import Path

from dotenv import load_dotenv

from langpa.services import DeepSearchService, OutputManager

# Ensure .env is loaded before instantiating clients
load_dotenv()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run DeepSearch over a gene list within a biological context."
    )

    # List available options
    parser.add_argument(
        "--list-presets",
        action="store_true",
        help="List available configuration presets and exit.",
    )
    parser.add_argument(
        "--list-templates",
        action="store_true",
        help="List available prompt templates and exit.",
    )
    parser.add_argument(
        "--show-template",
        metavar="TEMPLATE_NAME",
        help="Show complete details for a specific template and exit.",
    )
    parser.add_argument(
        "--show-preset",
        metavar="PRESET_NAME",
        help="Show complete details for a specific preset and exit.",
    )
    parser.add_argument(
        "-g",
        "--genes",
        action="append",
        nargs="+",
        help="Gene symbols (space or comma separated). May repeat flag.",
    )
    parser.add_argument(
        "--genes-file",
        type=Path,
        help="Path to a file containing genes (comma or newline separated).",
    )
    parser.add_argument(
        "-c",
        "--context",
        help="Biological context description.",
    )
    parser.add_argument(
        "--context-file",
        type=Path,
        help="Path to a text file describing the biological context.",
    )
    parser.add_argument(
        "--provider",
        help="Override provider passed to DeepSearchService.research_gene_list.",
    )
    # Configuration options
    parser.add_argument(
        "--preset",
        help="Configuration preset to use (e.g., 'perplexity-sonar-pro'). Default: None (uses "
        "perplexity provider with academic template). Use --list-presets to see all options "
        "and --show-preset NAME for details.",
    )
    parser.add_argument(
        "--preferred-provider",
        help="Preferred provider when initializing DeepSearchService (for backward compatibility).",
    )
    parser.add_argument(
        "--template",
        help="Prompt template to use (e.g., 'gene_analysis_academic'). Default: preset's default "
        "template, or 'gene_analysis_academic' if no preset. Use --list-templates to see all "
        "options and --show-template NAME for details.",
    )
    parser.add_argument(
        "--custom-prompt",
        help="Custom prompt to use instead of templates. Overrides both preset and --template "
        "options.",
    )

    # Configuration overrides
    parser.add_argument(
        "--model",
        help="Override the model used by the provider (e.g., 'sonar-reasoning-pro'). Default: "
        "preset's model, or 'sonar-reasoning-pro' if no preset.",
    )
    parser.add_argument(
        "--reasoning-effort",
        choices=["low", "medium", "high"],
        help="Override reasoning effort level for Perplexity (low/medium/high). Default: "
        "preset's setting, or 'high' if no preset.",
    )
    parser.add_argument(
        "--search-recency",
        choices=["hour", "day", "week", "month", "year"],
        help="Override search recency filter (hour/day/week/month/year). Default: preset's "
        "setting, or 'month' if no preset.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=180,
        help="Timeout (seconds) for DeepSearch request. Default: 180.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs"),
        help="Directory to store DeepSearch outputs. Default: outputs/.",
    )
    parser.add_argument(
        "--skip-structured",
        action="store_true",
        help="Skip JSON extraction/validation step; only save raw response.",
    )
    parser.add_argument(
        "--debug-extraction",
        action="store_true",
        help="Dump extracted JSON to a file before validation (skips schema validation).",
    )
    parser.add_argument(
        "--print-markdown",
        action="store_true",
        help="Echo the markdown/content returned by DeepSearch.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show configuration and prompt that would be sent, but don't call API.",
    )
    parser.add_argument(
        "--show-config",
        action="store_true",
        help="Display effective configuration before making API call.",
    )
    return parser.parse_args()


def _split_tokens(tokens: Sequence[str]) -> list[str]:
    genes: list[str] = []
    for token in tokens:
        parts = [part.strip() for part in token.split(",") if part.strip()]
        genes.extend(parts)
    return genes


def load_genes(args: argparse.Namespace) -> list[str]:
    genes: list[str] = []

    if args.genes:
        for group in args.genes:
            genes.extend(_split_tokens(group))

    if args.genes_file:
        if not args.genes_file.exists():
            raise FileNotFoundError(f"Genes file not found: {args.genes_file}")
        file_tokens = []
        for line in args.genes_file.read_text(encoding="utf-8").splitlines():
            file_tokens.extend(line.strip().split())
        genes.extend(_split_tokens(file_tokens))

    cleaned = [gene.strip() for gene in genes if gene.strip()]
    if not cleaned:
        raise ValueError("No genes provided. Use --genes and/or --genes-file.")
    return cleaned


def load_context(args: argparse.Namespace) -> str:
    context_parts: list[str] = []

    if args.context:
        context_parts.append(args.context.strip())

    if args.context_file:
        if not args.context_file.exists():
            raise FileNotFoundError(f"Context file not found: {args.context_file}")
        context_parts.append(args.context_file.read_text(encoding="utf-8").strip())

    context = "\n".join(part for part in context_parts if part)
    if not context.strip():
        raise ValueError("Context is required via --context and/or --context-file.")
    return context


def list_presets() -> None:
    """Display available configuration presets with complete details."""
    print("Available configuration presets:")
    print("=" * 60)
    print()

    preset_descriptions = DeepSearchService.get_available_presets()
    for preset_name, description in preset_descriptions.items():
        # Get the actual configuration for detailed display
        config = DeepSearchService.get_preset_config(preset_name)

        print(f"{preset_name}")
        print(f"  Description: {description}")
        print(f"  Provider: {config.provider}")
        print(f"  Model: {config.model}")
        print(f"  Template: {config.prompt_template}")
        print(f"  Timeout: {config.timeout}s")

        # Show provider parameters in a clean format
        if config.provider_params:
            print("  Provider Parameters:")
            for key, value in config.provider_params.items():
                if key == "search_domain_filter" and isinstance(value, list):
                    # Truncate long domain lists for readability
                    if len(value) > 3:
                        domains_display = f"[{', '.join(value[:3])}, ... ({len(value)} total)]"
                    else:
                        domains_display = f"[{', '.join(value)}]"
                    print(f"    - {key}: {domains_display}")
                elif key == "system_prompt" and value is None:
                    print(f"    - {key}: [Set dynamically with JSON schema]")
                else:
                    print(f"    - {key}: {value}")

        print(f"  Use --show-preset {preset_name} for more details")
        print()


def list_templates() -> None:
    """Display available prompt templates with complete details."""
    print("Available prompt templates:")
    print("=" * 60)
    print()

    from langpa.services.deepsearch_prompts import get_template_metadata

    templates = DeepSearchService.get_available_templates()
    for template_name, description in templates.items():
        # Get template metadata for detailed display
        metadata = get_template_metadata(template_name)

        print(f"{template_name}")
        print(f"  Description: {description}")
        print(f"  Optimized for: {', '.join(metadata['optimized_for'])}")
        print(f"  Supports JSON schema: {'Yes' if metadata['supports_json_schema'] else 'No'}")
        print(f"  Use --show-template {template_name} for full template text")
        print()


def show_template(template_name: str) -> None:
    """Display complete details for a specific template."""
    from langpa.services.deepsearch_prompts import get_prompt_template, get_template_metadata

    try:
        # Get template metadata and content
        metadata = get_template_metadata(template_name)
        template_config = get_prompt_template(template_name)
        template_text = template_config["template"]

        print(f"Template Details: {template_name}")
        print("=" * 60)
        print()

        print(f"Description: {metadata['description']}")
        print(f"Optimized for: {', '.join(metadata['optimized_for'])}")
        print(f"Supports JSON schema: {'Yes' if metadata['supports_json_schema'] else 'No'}")
        print()

        print("Template Text:")
        print("-" * 40)
        # Show template with example substitutions
        example_genes = "TP53, BRCA1"
        example_context = "cancer research"
        example_output = template_text.format(genes=example_genes, context=example_context)
        print(example_output)
        print("-" * 40)
        print()

        print("Placeholders:")
        print("  {genes} - Comma-separated list of gene symbols")
        print("  {context} - Biological context description")
        print()

        print("Example usage:")
        print("  python scripts/run_deepsearch.py --genes TP53,BRCA1")
        print(f"    --context 'cancer research' --template {template_name}")

    except ValueError as e:
        print(f"Error: {e}")
        print("Use --list-templates to see available templates.")


def show_preset(preset_name: str) -> None:
    """Display complete details for a specific preset."""
    try:
        # Get preset configuration
        config = DeepSearchService.get_preset_config(preset_name)
        preset_descriptions = DeepSearchService.get_available_presets()
        description = preset_descriptions.get(preset_name, "No description available")

        print(f"Preset Details: {preset_name}")
        print("=" * 60)
        print()

        print(f"Description: {description}")
        print()

        print("Configuration:")
        print(f"  Provider: {config.provider}")
        print(f"  Model: {config.model}")
        print(f"  Default Template: {config.prompt_template}")
        print(f"  Timeout: {config.timeout} seconds")
        print()

        # Show all provider parameters in detail
        if config.provider_params:
            print("Provider Parameters:")
            for key, value in config.provider_params.items():
                if key == "search_domain_filter" and isinstance(value, list):
                    print(f"  {key}:")
                    for domain in value:
                        print(f"    - {domain}")
                elif key == "system_prompt" and value is None:
                    print(f"  {key}: [Set dynamically with JSON schema]")
                else:
                    print(f"  {key}: {value}")
            print()

        print("Usage Examples:")
        print("  # Use this preset:")
        print("  python scripts/run_deepsearch.py --genes TP53,BRCA1")
        print(f"    --context 'cancer' --preset {preset_name}")
        print()
        print("  # Override template:")
        print(f"  python scripts/run_deepsearch.py --preset {preset_name}")
        print("    --template gene_analysis_structured")
        print()
        print("  # Override model:")
        print(f"  python scripts/run_deepsearch.py --preset {preset_name} --model sonar-small")

    except ValueError as e:
        print(f"Error: {e}")
        print("Use --list-presets to see available presets.")


def show_configuration(
    service: DeepSearchService, args: argparse.Namespace, title: str = "Configuration"
) -> None:
    """Display the effective configuration."""
    print(f"=== {title.upper()} ===")
    print()
    print("Configuration:")
    print(f"  Preset: {args.preset or 'None (using backward compatibility)'}")
    print(f"  Provider: {service.config.provider}")
    print(f"  Model: {service.config.model}{' (overridden)' if args.model else ''}")
    template_name = args.template or service.config.prompt_template
    template_suffix = " (overridden)" if args.template else ""
    print(f"  Template: {template_name}{template_suffix}")
    print(f"  Timeout: {args.timeout}s")

    if args.reasoning_effort or args.search_recency:
        print("  Overrides applied:")
        if args.reasoning_effort:
            print(f"    Reasoning effort: {args.reasoning_effort}")
        if args.search_recency:
            print(f"    Search recency: {args.search_recency}")
    print()


def show_dry_run(
    service: DeepSearchService, genes: list[str], context: str, args: argparse.Namespace
) -> None:
    """Display configuration and prompt for dry run."""
    show_configuration(service, args, title="DRY RUN MODE")

    # Show provider parameters
    print("Provider Parameters:")
    for key, value in service.config.provider_params.items():
        if key == "system_prompt" and value:
            print(f"  {key}: [JSON schema system prompt - truncated]")
        else:
            print(f"  {key}: {value}")
    print()

    # Construct and show the prompt
    if args.custom_prompt:
        prompt = args.custom_prompt
        print("Custom Prompt:")
    else:
        prompt = service._construct_prompt(genes, context, template_override=args.template)
        print("Generated Prompt:")

    print("-" * 60)
    print(prompt)
    print("-" * 60)
    print()

    print("Genes to analyze:", ", ".join(genes))
    print("Context:", context)
    print()
    print("API call would be made to:", service.config.provider)
    print("No actual API call made (dry run mode)")


def main() -> None:
    args = parse_args()

    # Handle informational operations first
    if args.list_presets:
        list_presets()
        return

    if args.list_templates:
        list_templates()
        return

    if args.show_template:
        show_template(args.show_template)
        return

    if args.show_preset:
        show_preset(args.show_preset)
        return

    # Load genes and context
    try:
        genes = load_genes(args)
        context = load_context(args)
    except Exception as exc:
        raise SystemExit(f"[error] {exc}") from exc

    # Build configuration overrides
    config_overrides = {}

    if args.model:
        config_overrides["model"] = args.model

    if args.reasoning_effort or args.search_recency:
        provider_params = {}
        if args.reasoning_effort:
            provider_params["reasoning_effort"] = args.reasoning_effort
        if args.search_recency:
            provider_params["search_recency_filter"] = args.search_recency
        config_overrides["provider_params"] = provider_params

    # Initialize service with preset support and overrides
    if args.preset:
        service = DeepSearchService(preset=args.preset, **config_overrides)
    else:
        # Backward compatibility
        service = DeepSearchService(preferred_provider=args.preferred_provider, **config_overrides)

    # Handle dry run
    if args.dry_run:
        show_dry_run(service, genes, context, args)
        return

    # Show configuration if requested
    if args.show_config:
        show_configuration(service, args)

    try:
        result = service.research_gene_list(
            genes=genes,
            context=context,
            provider=args.provider,
            timeout=args.timeout,
            custom_prompt=args.custom_prompt,
            prompt_template=args.template,
        )
    except Exception as exc:
        raise SystemExit(f"[error] DeepSearch call failed: {exc}") from exc

    output_manager = OutputManager(output_dir=args.output_dir)
    metadata = {
        "source": "scripts/run_deepsearch.py",
        "preset": args.preset,
        "template": args.template,
        "custom_prompt_used": bool(args.custom_prompt),
        "provider_override": args.provider,
        "model_override": args.model,
        "reasoning_effort_override": args.reasoning_effort,
        "search_recency_override": args.search_recency,
        "timeout_seconds": args.timeout,
        "effective_provider": service.config.provider,
        "effective_model": service.config.model,
    }
    raw_path = output_manager.save_raw_response(result, genes, context, metadata=metadata)

    debug_file = None
    if args.debug_extraction:
        markdown = getattr(result, "markdown", None) or getattr(result, "content", "")
        extracted_json = output_manager.extract_json_from_markdown(markdown)
        if extracted_json is None:
            print("[warn] Debug extraction failed: no JSON detected in response.")
        else:
            debug_filename = output_manager._generate_filename(
                genes,
                context,
                suffix="_extracted_debug",
            )
            debug_file = output_manager.output_dir / debug_filename
            with open(debug_file, "w", encoding="utf-8") as f:
                json.dump(extracted_json, f, indent=2, ensure_ascii=False)
            print(f"[ok] Debug extracted JSON saved to {debug_file}")

    structured_info = None
    if not args.skip_structured and not args.debug_extraction:
        structured_info = output_manager.process_and_save_structured_output(
            result,
            genes,
            context,
            raw_filepath=raw_path,
        )

    print(f"[ok] Saved raw DeepSearch response to {raw_path}")

    # Configuration summary in output
    config_summary = f"[config] Used {service.config.provider}/{service.config.model}"
    if args.preset:
        config_summary += f" (preset: {args.preset})"
    if args.template:
        config_summary += f" (template: {args.template})"
    if args.custom_prompt:
        config_summary += " (custom prompt)"
    print(config_summary)

    if structured_info:
        if structured_info.get("success"):
            structured_file = structured_info.get("structured_file")
            print(f"[ok] Structured JSON extracted + validated: {structured_file}")
        else:
            print("[warn] Structured extraction failed:")
            for err in structured_info.get("errors", []):
                print(f"  - {err}")
    elif args.debug_extraction:
        print("[info] Validation skipped due to --debug-extraction; rerun without it to validate.")

    if args.print_markdown:
        markdown = getattr(result, "markdown", None) or getattr(result, "content", "")
        divider = "-" * 40
        print(divider)
        print(markdown.strip())
        print(divider)


if __name__ == "__main__":
    main()
