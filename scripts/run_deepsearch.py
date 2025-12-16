#!/usr/bin/env python3
"""CLI to run DeepSearchService with file/arg inputs and capture outputs."""

from __future__ import annotations

import argparse
import json
import re
import time
from collections.abc import Sequence
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from langpa.schemas import load_schema
from langpa.services import CitationResolver, DeepSearchService, OutputManager
from langpa.services.markdown_reporter import MarkdownReportGenerator
from langpa.services.deepsearch_prompts import get_prompt_template, get_template_metadata
from langpa.services.markdown_citation_extractor import extract_citations_from_markdown
from langpa.utils.output_paths import build_run_directory, sanitize_name
from langpa.utils.csv_batch_parser import parse_csv_batch

# Ensure .env is loaded before instantiating clients
load_dotenv()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run DeepSearch over a gene list within a biological context."
    )

    parser.add_argument(
        "--project",
        default="default",
        help="Project name used to organize outputs (default: default).",
    )
    parser.add_argument(
        "--query",
        help=(
            "Query name used to organize outputs. If omitted, derived from input "
            "filename/folder or context/genes."
        ),
    )
    parser.add_argument(
        "--batch-csv",
        type=Path,
        help=(
            "CSV file with batch queries (columns: ID, name, gene_list, context, GSE). "
            "Each row triggers new deepsearch API calls. Requires --project."
        ),
    )
    parser.add_argument(
        "--batch-reprocess",
        action="store_true",
        help="Reprocess existing deepsearch.json files in project directory. Requires --project.",
    )
    parser.add_argument(
        "--num-runs",
        type=int,
        default=1,
        help="Number of times to run each query in CSV batch (default: 1). Only used with --batch-csv.",
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
        "--from-markdown",
        type=Path,
        help="Path to a markdown file containing a DeepSearch response to process offline.",
    )
    parser.add_argument(
        "--raw-input",
        type=Path,
        help=(
            "Path to a raw DeepSearch JSON (e.g., saved by OutputManager.save_raw_response) "
            "to process offline."
        ),
    )
    parser.add_argument(
        "--citations-file",
        type=Path,
        help=(
            "Optional path to a JSON file containing citation URLs or objects with "
            "source_id/source_url."
        ),
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
        "--resolve-citations",
        action="store_true",
        help="Resolve DeepSearch citations with url2ref and build container JSON.",
    )
    parser.add_argument(
        "--citation-validate",
        action="store_true",
        default=True,
        help="Enable API/metapub validation during citation resolution (default: on).",
    )
    parser.add_argument(
        "--citation-no-validate",
        dest="citation_validate",
        action="store_false",
        help="Disable API/metapub validation during citation resolution.",
    )
    parser.add_argument(
        "--citation-scrape",
        action="store_true",
        help="Enable web scraping/PDF extraction for unresolved citations (default: off).",
    )
    parser.add_argument(
        "--citation-no-pdf",
        dest="citation_pdf",
        action="store_false",
        default=True,
        help="Disable PDF extraction during citation resolution (default: on).",
    )
    parser.add_argument(
        "--citation-topic-validation",
        action="store_true",
        help="Enable topic validation during citation resolution (default: off).",
    )
    parser.add_argument(
        "--citation-style",
        default="vancouver",
        help=(
            "Citation style for compact bibliography (e.g., vancouver, apa, ieee, chicago). "
            "Default: vancouver. Only used when --resolve-citations is enabled."
        ),
    )
    parser.add_argument(
        "--citation-locale",
        default="en-US",
        help=(
            "Locale for citation formatting (e.g., en-US, en-GB, de-DE). "
            "Default: en-US. Only used when --resolve-citations is enabled."
        ),
    )
    parser.add_argument(
        "--cache",
        action="store_true",
        help="Enable DeepResearchClient result caching (default: off).",
    )
    parser.add_argument(
        "--no-stomp",
        action="store_true",
        help="Do not overwrite existing outputs; create versioned filenames instead.",
    )
    parser.add_argument(
        "--print-markdown",
        action="store_true",
        help="Echo the markdown/content returned by DeepSearch.",
    )
    parser.add_argument(
        "--generate-markdown",
        action="store_true",
        help="Generate a Markdown report from the structured/container output.",
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


def generate_markdown_report(
    *,
    container_path: Path,
    output_path: Path | None = None,
    strict_citations: bool = False,
) -> Path:
    """Generate a Markdown report from a container/structured JSON file.

    Args:
        container_path: Path to the container or structured JSON file.
        output_path: Optional explicit path for the rendered Markdown file. Defaults to
            the container path with a `.md` extension.
        strict_citations: Whether to fail on citation/reference mismatches (default: False).

    Returns:
        Path to the written Markdown file.
    """
    generator = MarkdownReportGenerator(strict_citations=strict_citations)
    markdown = generator.render_from_path(container_path)

    target_path = output_path or container_path.with_suffix(".md")
    target_path.write_text(markdown, encoding="utf-8")
    return target_path


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


def _query_slug_from_genes_context(genes: list[str], context: str) -> str:
    """Compose a query slug using the legacy filename recipe (genes + context)."""
    # Handle gene list (limit to avoid very long names)
    if len(genes) <= 3:
        genes_part = "_".join(genes)
    else:
        genes_part = f"{genes[0]}_{genes[1]}_and_{len(genes) - 2}_more"
    genes_part = re.sub(r"[^\w-]", "_", genes_part)[:30]

    # Sanitize context (remove special characters, limit length)
    safe_context = re.sub(r"[^\w\s-]", "", context.strip())
    safe_context = re.sub(r"\s+", "_", safe_context)[:20]

    parts = [part for part in (genes_part, safe_context) if part]
    return "_".join(parts) if parts else "default_query"


def derive_query_name(args: argparse.Namespace, input_path: Path | None) -> str:
    """Derive a query name from args or input paths."""
    if args.query:
        return sanitize_name(args.query)

    if input_path:
        # For output structure: outputs/{project}/{query}/{timestamp}/file
        # Check if immediate parent looks like a timestamp directory
        parent = input_path.parent

        # Timestamp pattern: YYYYMMDD_HHMMSS (e.g., 20251216_083514)
        import re
        timestamp_pattern = r'^\d{8}_\d{6}$'

        if parent.name and re.match(timestamp_pattern, parent.name):
            # Parent is timestamp, use grandparent as query name
            grandparent = parent.parent
            if grandparent.name and grandparent.name not in {"inputs", "outputs", args.project}:
                return sanitize_name(grandparent.name)

        # Otherwise use immediate parent if it's not a special directory
        if parent.name and parent.name not in {"inputs", "outputs", args.project}:
            return sanitize_name(parent.name)

        return sanitize_name(input_path.stem)

    # Fallback for live runs: use genes + context recipe
    if args.context or args.context_file:
        try:
            genes = load_genes(args)
        except Exception:
            genes = []
        try:
            context_text = load_context(args)
        except Exception:
            context_text = (args.context or "").strip()

        query_slug = _query_slug_from_genes_context(genes, context_text)
        return sanitize_name(query_slug)

    if args.genes:
        try:
            genes = load_genes(args)
        except Exception:
            genes = []
        query_slug = _query_slug_from_genes_context(genes, args.context or "")
        return sanitize_name(query_slug)

    return "default_query"


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

    except (ValueError, KeyError) as e:
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

    template_name = args.template or service.config.prompt_template
    template_metadata = get_template_metadata(template_name)
    provider_params = dict(service.config.provider_params)
    schema = load_schema("deepsearch_results_schema.json")

    # Resolve the system prompt using the same logic as the service
    provider_params["system_prompt"] = service._resolve_system_prompt(
        provider_params=provider_params,
        schema=schema,
        template_requires_schema=template_metadata.get("requires_full_schema", False),
    )

    # Show provider parameters
    print("Provider Parameters:")
    for key, value in provider_params.items():
        print(f"  {key}: {value}")
    print()

    # Construct and show the prompt
    if args.custom_prompt:
        prompt = args.custom_prompt
        print("Custom Prompt:")
    else:
        prompt = service.construct_prompt(genes, context, template_override=args.template)
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


def _versioned_prefix(run_dir: Path, base: str, no_stomp: bool) -> str:
    """Return a filename prefix honoring no-stomp."""
    if not no_stomp:
        return base
    if not (run_dir / f"{base}.json").exists():
        return base
    idx = 2
    while True:
        candidate = f"{base}_v{idx}"
        if not (run_dir / f"{candidate}.json").exists():
            return candidate
        idx += 1


def _discover_project_runs(project: str, output_dir: Path, query: str | None = None) -> list[tuple[str, Path, Path]]:
    """Find all deepsearch.json files under outputs/{project}/{query}/{run}/."""
    project_root = output_dir / project
    if not project_root.exists():
        raise SystemExit(f"[error] Project not found under {output_dir}: {project}")

    runs: list[tuple[str, Path, Path]] = []
    queries = [project_root / query] if query else [p for p in project_root.iterdir() if p.is_dir()]

    for qdir in queries:
        if not qdir.exists() or not qdir.is_dir():
            continue
        query_name = qdir.name
        for run_dir in sorted(p for p in qdir.iterdir() if p.is_dir()):
            raw_path = run_dir / "deepsearch.json"
            if raw_path.exists():
                runs.append((query_name, run_dir, raw_path))
    if not runs:
        raise SystemExit("[error] No deepsearch.json files found under project path.")
    return runs


def log_warning(warnings_file: Path, query_name: str, run_num: int, error: Exception) -> None:
    """Log a warning for a failed query run.

    Args:
        warnings_file: Path to warnings log file
        query_name: Name of the query that failed
        run_num: Run number that failed
        error: Exception that was raised
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Query: {query_name}, Run: {run_num}, Error: {error}\n"

    with open(warnings_file, "a", encoding="utf-8") as f:
        f.write(log_entry)


def run_query_with_retry(
    args: argparse.Namespace, query_name: str, genes: list[str], context: str, run_num: int
) -> None:
    """Run a single query with exponential backoff retry logic.

    Args:
        args: Command-line arguments namespace
        query_name: Name of the query
        genes: List of gene symbols
        context: Biological context
        run_num: Current run number (1-indexed)

    Raises:
        Exception: If all retry attempts fail
    """
    max_attempts = 3
    backoff_delays = [1, 2, 4]  # seconds

    for attempt in range(1, max_attempts + 1):
        try:
            print(f"[batch] Processing query '{query_name}' (run {run_num}/{args.num_runs})")

            # Create a copy of args with query-specific genes and context
            sub_args = argparse.Namespace(**vars(args))
            sub_args.query = query_name
            sub_args.genes = [[gene] for gene in genes]  # Format expected by load_genes
            sub_args.context = context

            # Run the query (will create its own timestamped directory)
            main_single_run(sub_args, fixed_run_dir=None, allow_print=False)
            return  # Success

        except Exception as e:
            if attempt < max_attempts:
                delay = backoff_delays[attempt - 1]
                print(f"[retry] Attempt {attempt}/{max_attempts} failed for '{query_name}' "
                      f"(run {run_num}): {e}")
                print(f"[retry] Retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Final attempt failed, re-raise
                print(f"[error] All {max_attempts} attempts failed for '{query_name}' (run {run_num})")
                raise


def process_csv_batch(args: argparse.Namespace) -> None:
    """Process CSV batch with multiple runs per query.

    Parses CSV file, validates queries, and executes each query the specified
    number of times with retry logic. Warnings are logged for failed runs.

    Args:
        args: Command-line arguments namespace. Must include:
            - batch_csv: Path to CSV file
            - project: Project name
            - num_runs: Number of times to run each query
            - context/context_file: Optional global context

    Raises:
        ValueError: If CSV parsing or validation fails
        SystemExit: If CSV file not found or other fatal errors
    """
    if not args.batch_csv.exists():
        raise SystemExit(f"[error] CSV file not found: {args.batch_csv}")

    # Load global context (may be None if all rows have per-row context)
    try:
        global_context = load_context(args)
    except ValueError:
        # No global context provided; will rely on per-row context
        global_context = None

    # Parse CSV
    print(f"[batch] Parsing CSV file: {args.batch_csv}")
    try:
        queries = parse_csv_batch(args.batch_csv, global_context)
    except ValueError as e:
        raise SystemExit(f"[error] CSV parsing failed: {e}") from e

    print(f"[batch] Found {len(queries)} queries, {args.num_runs} run(s) per query "
          f"= {len(queries) * args.num_runs} total executions")

    # Create warnings log file
    output_dir = Path(args.output_dir)
    warnings_file = output_dir / args.project / "batch_warnings.log"
    warnings_file.parent.mkdir(parents=True, exist_ok=True)

    # Execute each query num_runs times
    total_queries = len(queries)
    total_failures = 0

    for query_idx, query in enumerate(queries, start=1):
        for run_idx in range(1, args.num_runs + 1):
            try:
                print(f"[batch] Query {query_idx}/{total_queries}: {query.query_name}")
                run_query_with_retry(args, query.query_name, query.genes, query.context, run_idx)
            except Exception as e:
                total_failures += 1
                log_warning(warnings_file, query.query_name, run_idx, e)
                print(f"[warn] Query '{query.query_name}' run {run_idx} failed after retries: {e}")

    # Summary
    total_runs = len(queries) * args.num_runs
    total_successes = total_runs - total_failures
    print(f"\n[batch] Complete.")
    print(f"[batch] Total: {total_runs} runs, {total_successes} succeeded, {total_failures} failed")
    if total_failures > 0:
        print(f"[batch] Warnings logged to: {warnings_file}")


def process_project_batch(args: argparse.Namespace) -> None:
    """Batch process all deepsearch.json under outputs/{project}/{query}/{run}/."""
    output_dir = Path(args.output_dir)
    runs = _discover_project_runs(args.project, output_dir, args.query)
    for query_name, run_dir, raw_path in runs:
        sub_args = argparse.Namespace(**vars(args))
        sub_args.raw_input = raw_path
        sub_args.from_markdown = None
        sub_args.query = query_name
        sub_args.project = args.project
        sub_args.fixed_run_dir = run_dir
        print(f"[batch] Processing {raw_path} as query '{query_name}' (run: {run_dir.name})")
        main_single_run(sub_args, fixed_run_dir=run_dir, allow_print=False)
    print("[batch] Done.")


def main() -> None:
    args = parse_args()

    # Handle informational operations FIRST (no mode required)
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

    # Explicit mode: CSV batch (fresh API calls)
    if args.batch_csv:
        if not args.project:
            raise SystemExit("[error] --project is required with --batch-csv")
        process_csv_batch(args)
        return

    # Explicit mode: Batch reprocess (offline)
    if args.batch_reprocess:
        if not args.project:
            raise SystemExit("[error] --project is required with --batch-reprocess")
        process_project_batch(args)
        return

    # Default: Fresh deepsearch run (implicit mode)
    # This handles the common case: --genes + --context
    # Let main_single_run() handle validation (missing genes, context, etc.)
    main_single_run(args, fixed_run_dir=None, allow_print=True)


def main_single_run(args: argparse.Namespace, fixed_run_dir: Path | None = None, allow_print: bool = True) -> None:
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

    offline_input = args.from_markdown or args.raw_input
    genes: list[str] | None = None
    context: str | None = None

    # Derive query and project
    input_path: Path | None = args.from_markdown or args.raw_input
    query_name = derive_query_name(args, input_path)
    project_name = sanitize_name(args.project)

    # Load genes and context unless offline inputs will supply them
    if not offline_input:
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

    # Initialize service with preset support and overrides (only needed for live calls)
    service = None
    if not offline_input:
        if args.preset:
            from deep_research_client.models import CacheConfig  # type: ignore

            cache_config = CacheConfig(enabled=args.cache)
            service = DeepSearchService(preset=args.preset, cache_config=cache_config, **config_overrides)
        else:
            # Backward compatibility
            from deep_research_client.models import CacheConfig  # type: ignore

            cache_config = CacheConfig(enabled=args.cache)
            service = DeepSearchService(
                preferred_provider=args.preferred_provider,
                cache_config=cache_config,
                **config_overrides,
            )

    # Handle dry run
    if args.dry_run:
        show_dry_run(service, genes, context, args)
        return

    # Show configuration if requested
    if args.show_config:
        show_configuration(service, args)

    # Build or reuse run directory
    if fixed_run_dir is not None:
        run_dir = Path(fixed_run_dir)
    else:
        run_dir = build_run_directory(Path(args.output_dir), project_name, query_name)

    prefix = _versioned_prefix(run_dir, "deepsearch", getattr(args, "no_stomp", False))

    output_manager = OutputManager(output_dir=run_dir)
    resolver = None
    if args.resolve_citations:
        resolver = CitationResolver(
            validate=args.citation_validate,
            scrape=args.citation_scrape,
            pdf=args.citation_pdf,
            topic_validation=args.citation_topic_validation,
        )

    if args.raw_input:
        if not args.raw_input.exists():
            raise SystemExit(f"[error] Raw input file not found: {args.raw_input}")
        raw_payload = json.loads(args.raw_input.read_text(encoding="utf-8"))
        raw_resp = raw_payload.get("raw_response", {}) or {}
        markdown = raw_resp.get("markdown") or raw_payload.get("markdown") or ""
        citations = raw_resp.get("citations") or raw_payload.get("citations") or []
        if not citations and markdown:
            citations = extract_citations_from_markdown(markdown)
        metadata_src = raw_payload.get("metadata", {})
        genes = genes or metadata_src.get("genes") or []
        context = context or metadata_src.get("context") or ""

        class OfflineResult:
            def __init__(
                self,
                markdown: str,
                citations: list,
                provider: str,
                model: str,
                duration_seconds: float | None,
            ) -> None:
                self.markdown = markdown
                self.citations = citations
                self.provider = provider
                self.model = model
                self.duration_seconds = duration_seconds

        result = OfflineResult(
            markdown=markdown,
            citations=citations,
            provider=metadata_src.get("provider", "offline"),
            model=metadata_src.get("model", "offline"),
            duration_seconds=metadata_src.get("duration_seconds"),
        )
    elif args.from_markdown:
        if not args.from_markdown.exists():
            raise SystemExit(f"[error] Markdown file not found: {args.from_markdown}")
        markdown = args.from_markdown.read_text(encoding="utf-8")
        # Load citations if provided explicitly
        if args.citations_file:
            import json as _json

            citations_payload = _json.loads(args.citations_file.read_text(encoding="utf-8"))
            citations = citations_payload
        else:
            citations = extract_citations_from_markdown(markdown)

        class OfflineResult:
            def __init__(self, markdown: str, citations: list) -> None:
                self.markdown = markdown
                self.citations = citations
                self.provider = "offline"
                self.model = "offline"
                self.duration_seconds = None

        result = OfflineResult(markdown, citations)
    else:
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
    effective_provider = "offline" if offline_input else service.config.provider
    effective_model = "offline" if offline_input else service.config.model
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
        "effective_provider": effective_provider,
        "effective_model": effective_model,
        "project": project_name,
        "query": query_name,
        "source_tag": input_path.stem if input_path else None,
        "resolve_citations": args.resolve_citations,
        "citation_flags": {
            "validate": args.citation_validate,
            "scrape": args.citation_scrape,
            "pdf": args.citation_pdf,
            "topic_validation": args.citation_topic_validation,
        },
    }
    # Provide fallbacks for genes/context in offline flows
    genes_for_output = genes or ["unspecified_genes"]
    context_for_output = context or "unspecified_context"

    raw_path = output_manager.save_raw_response(
        result,
        genes_for_output,
        context_for_output,
        metadata=metadata,
        filename=f"{prefix}.json",
    )

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
            genes_for_output,
            context_for_output,
            raw_filepath=raw_path,
            resolve_citations=args.resolve_citations,
            resolver=resolver,
            metadata=metadata,
            citation_style=args.citation_style,
            citation_locale=args.citation_locale,
            filename_prefix=prefix,
        )

    print(f"[ok] Saved raw DeepSearch response to {raw_path}")

    # Configuration summary in output
    if offline_input:
        print("[config] Offline mode: processed existing input (markdown/raw).")
    else:
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

    if args.generate_markdown:
        if not structured_info:
            print("[error] Cannot generate Markdown report: structured/container output is missing. Ensure extraction/validation succeeded and try again.")
        else:
            container_file = structured_info.get("container_file")
            source_file = container_file or structured_info.get("structured_file")
            if not source_file:
                print("[warn] No container/structured file available for Markdown generation.")
            else:
                try:
                    output_md = generate_markdown_report(container_path=Path(source_file))
                    print(f"[ok] Markdown report written to {output_md}")
                except Exception as exc:
                    print(f"[warn] Markdown generation failed: {exc}")
    if allow_print and args.print_markdown:
        markdown = getattr(result, "markdown", None) or getattr(result, "content", "")
        divider = "-" * 40
        print(divider)
        print(markdown.strip())
        print(divider)


if __name__ == "__main__":
    main()
