#!/usr/bin/env python3
"""CLI to run DeepSearchService with file/arg inputs and capture outputs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Sequence
import json

from dotenv import load_dotenv

# Ensure .env is loaded before instantiating clients
load_dotenv()

from langpa.services import DeepSearchService, OutputManager


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run DeepSearch over a gene list within a biological context."
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
    parser.add_argument(
        "--preferred-provider",
        help="Preferred provider when initializing DeepSearchService.",
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
    return parser.parse_args()


def _split_tokens(tokens: Sequence[str]) -> List[str]:
    genes: List[str] = []
    for token in tokens:
        parts = [part.strip() for part in token.split(",") if part.strip()]
        genes.extend(parts)
    return genes


def load_genes(args: argparse.Namespace) -> List[str]:
    genes: List[str] = []

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
    context_parts: List[str] = []

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


def main() -> None:
    args = parse_args()

    try:
        genes = load_genes(args)
        context = load_context(args)
    except Exception as exc:
        raise SystemExit(f"[error] {exc}") from exc

    service = DeepSearchService(preferred_provider=args.preferred_provider)

    try:
        result = service.research_gene_list(
            genes=genes,
            context=context,
            provider=args.provider,
            timeout=args.timeout,
        )
    except Exception as exc:
        raise SystemExit(f"[error] DeepSearch call failed: {exc}") from exc

    output_manager = OutputManager(output_dir=args.output_dir)
    metadata = {
        "source": "scripts/run_deepsearch.py",
        "provider_override": args.provider,
        "timeout_seconds": args.timeout,
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
