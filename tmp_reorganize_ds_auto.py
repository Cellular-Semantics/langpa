#!/usr/bin/env python3
"""
One-off script to reorganize glioblastoma_ds_auto files.
Converts run_N.md files to deepsearch.json in timestamped directories.
"""

import yaml
import json
import re
from pathlib import Path
from typing import Any


def extract_gene_list(markdown: str) -> list[str]:
    """Extract gene list from markdown content."""
    # Look for **Gene List**: ["gene1", "gene2", ...]
    match = re.search(r'\*\*Gene List\*\*:\s*\[(.*?)\]', markdown, re.DOTALL)
    if match:
        genes_str = match.group(1)
        # Parse as JSON array
        try:
            genes = json.loads('[' + genes_str + ']')
            return [g.strip('"') for g in genes if g.strip()]
        except:
            # Fallback: split by comma and clean
            genes = [g.strip().strip('"') for g in genes_str.split(',')]
            return [g for g in genes if g]
    return []


def extract_context(markdown: str) -> str:
    """Extract biological context from markdown."""
    # Look for **Biological Context**: context_text
    match = re.search(r'\*\*Biological Context\*\*:\s*(.+?)(?:\n|$)', markdown)
    if match:
        return match.group(1).strip()
    return ""


def extract_citations(markdown: str) -> list[str]:
    """Extract citations from embedded JSON in markdown."""
    # Look for "citations": [...] in the embedded JSON
    match = re.search(r'"citations":\s*\[(.*?)\]', markdown, re.DOTALL)
    if match:
        citations_str = match.group(1)
        try:
            citations = json.loads('[' + citations_str + ']')
            return [c.strip('"') for c in citations if isinstance(c, str)]
        except:
            # Fallback: extract URLs manually
            urls = re.findall(r'"(https?://[^"]+)"', citations_str)
            return urls
    return []


def process_run_md(md_file: Path, query_name: str) -> dict[str, Any]:
    """Parse a run_N.md file and extract data for deepsearch.json."""
    content = md_file.read_text(encoding='utf-8')

    # Split YAML frontmatter from markdown
    # Content structure: \n---\nYAML\n---\nMarkdown
    if content.startswith('\\---'):
        # Handle escaped format
        content = content[1:]  # Remove leading backslash

    parts = content.split('---', 2)
    if len(parts) < 3:
        raise ValueError(f"Invalid format in {md_file}: expected YAML frontmatter")

    yaml_str = parts[1].strip()
    markdown = parts[2].strip()

    # Parse YAML
    metadata = yaml.safe_load(yaml_str)

    # Extract information from markdown
    genes = extract_gene_list(markdown)
    context = extract_context(markdown)
    citations = extract_citations(markdown)

    # Build deepsearch.json structure
    return {
        "metadata": {
            "timestamp": metadata.get('start_time', ''),
            "genes": genes,
            "context": context,
            "provider": metadata.get('provider', ''),
            "model": metadata.get('model', ''),
            "cached": metadata.get('cached', False),
            "project": "glioblastoma_ds_auto",
            "query": query_name,
            "source": "reorganization_script",
            "provider_config": metadata.get('provider_config', {}),
            "citation_count": metadata.get('citation_count', len(citations))
        },
        "raw_response": {
            "markdown": markdown,
            "citations": citations,
            "duration_seconds": metadata.get('duration_seconds', 0)
        }
    }


def format_timestamp_for_dirname(iso_timestamp: str) -> str:
    """Convert ISO timestamp to directory name format: YYYYMMDD_HHMMSS"""
    # Example: '2025-11-26T12:52:38.414203' -> '20251126_125238'
    cleaned = iso_timestamp.replace('-', '').replace(':', '').replace('T', '_')
    # Take first 15 chars: YYYYMMDD_HHMMSS
    return cleaned[:15]


def reorganize_project(base_path: Path, dry_run: bool = False):
    """Reorganize all query folders in the project."""

    if not base_path.exists():
        print(f"Error: Base path does not exist: {base_path}")
        return

    processed_count = 0
    error_count = 0

    # Get all query directories
    query_dirs = sorted([d for d in base_path.iterdir() if d.is_dir()])

    print(f"Found {len(query_dirs)} query directories to process")
    print()

    for query_dir in query_dirs:
        query_name = query_dir.name
        print(f"Processing query: {query_name}")

        # Find all run_*.md files
        run_files = sorted(query_dir.glob("run_*.md"))

        if not run_files:
            print(f"  No run_*.md files found, skipping")
            continue

        for run_file in run_files:
            try:
                print(f"  Processing {run_file.name}...")

                # Parse and create deepsearch.json data
                data = process_run_md(run_file, query_name)

                # Create timestamped directory
                timestamp_str = data['metadata']['timestamp']
                timestamp_dirname = format_timestamp_for_dirname(timestamp_str)
                run_dir = query_dir / timestamp_dirname

                if dry_run:
                    print(f"    [DRY RUN] Would create: {run_dir}/deepsearch.json")
                    print(f"    [DRY RUN] Extracted {len(data['metadata']['genes'])} genes")
                    print(f"    [DRY RUN] Context: {data['metadata']['context']}")
                else:
                    # Create directory
                    run_dir.mkdir(exist_ok=True)

                    # Write deepsearch.json
                    output_file = run_dir / "deepsearch.json"
                    output_file.write_text(
                        json.dumps(data, indent=2, ensure_ascii=False),
                        encoding='utf-8'
                    )

                    print(f"    ✓ Created: {run_dir.relative_to(base_path)}/deepsearch.json")
                    print(f"      Genes: {len(data['metadata']['genes'])}, Citations: {len(data['raw_response']['citations'])}")

                processed_count += 1

            except Exception as e:
                print(f"    ✗ Error processing {run_file.name}: {e}")
                error_count += 1

        print()

    print("=" * 60)
    print(f"Summary:")
    print(f"  Successfully processed: {processed_count} files")
    print(f"  Errors: {error_count} files")
    if dry_run:
        print(f"\n  This was a DRY RUN - no files were created")
        print(f"  Run with dry_run=False to actually create files")


if __name__ == "__main__":
    import sys

    base = Path("outputs/glioblastoma_ds_auto")

    # Check for --dry-run flag
    dry_run = "--dry-run" in sys.argv

    print("="*60)
    print("glioblastoma_ds_auto Reorganization Script")
    print("="*60)
    print()

    if dry_run:
        print("DRY RUN - Testing conversion logic...")
        print()
        reorganize_project(base, dry_run=True)
    else:
        print("ACTUAL RUN - Creating files...")
        print()
        reorganize_project(base, dry_run=False)
        print()
        print("Done! Original run_*.md files have been kept for backup.")
