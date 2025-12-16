#!/usr/bin/env python3
"""One-off script to fix corrupted deepsearch.json files with missing citations.

This script finds deepsearch.json files where raw_response.citations is empty
but the markdown contains a "## Citations" section, and extracts the citations
from markdown into the citations field.

Usage:
    # Dry run (preview only)
    python scripts/cleanup_corrupted_citations.py outputs/glioblastoma_ds_auto --dry-run

    # Execute with backups
    python scripts/cleanup_corrupted_citations.py outputs/glioblastoma_ds_auto

    # Execute without backups (not recommended)
    python scripts/cleanup_corrupted_citations.py outputs/glioblastoma_ds_auto --no-backup
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

# Add parent directory to path to import langpa modules
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from langpa.services.markdown_citation_extractor import extract_citations_from_markdown


def find_corrupted_files(base_dir: Path) -> list[Path]:
    """Find deepsearch.json files with empty citations but markdown citations.

    Args:
        base_dir: Base directory to search

    Returns:
        List of paths to corrupted files
    """
    corrupted_files = []

    for json_file in base_dir.rglob("deepsearch.json"):
        try:
            with open(json_file) as f:
                data = json.load(f)

            raw_response = data.get("raw_response", {})
            citations = raw_response.get("citations", [])
            markdown = raw_response.get("markdown", "")

            # Check if corrupted: empty citations but has "## Citations" in markdown
            if not citations and "## Citations" in markdown:
                corrupted_files.append(json_file)

        except Exception as e:
            print(f"Warning: Could not read {json_file}: {e}", file=sys.stderr)
            continue

    return corrupted_files


def extract_and_fix_citations(
    file_path: Path,
    dry_run: bool = False,
    backup: bool = True
) -> dict:
    """Extract citations from markdown and update file.

    Args:
        file_path: Path to deepsearch.json file
        dry_run: If True, don't modify the file
        backup: If True, create .backup file

    Returns:
        Dict with success status and details
    """
    try:
        with open(file_path) as f:
            data = json.load(f)
    except Exception as e:
        return {
            "success": False,
            "reason": f"error: {e}",
            "file_path": file_path,
        }

    raw_response = data.get("raw_response", {})
    citations = raw_response.get("citations", [])
    markdown = raw_response.get("markdown", "")

    # Skip if already has citations
    if citations:
        return {
            "success": False,
            "reason": "already_has_citations",
            "file_path": file_path,
        }

    # Skip if no markdown
    if not markdown:
        return {
            "success": False,
            "reason": "missing_markdown",
            "file_path": file_path,
        }

    # Extract citations from markdown
    extracted_citations = extract_citations_from_markdown(markdown)

    if not extracted_citations:
        return {
            "success": False,
            "reason": "no_citations_in_markdown",
            "file_path": file_path,
        }

    # Dry run: just report what would be done
    if dry_run:
        return {
            "success": True,
            "citations_extracted": len(extracted_citations),
            "file_path": file_path,
            "dry_run": True,
        }

    # Create backup if requested
    if backup:
        backup_path = file_path.with_suffix(file_path.suffix + ".backup")
        shutil.copy2(file_path, backup_path)

    # Update citations in data
    data["raw_response"]["citations"] = extracted_citations

    # Write updated file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return {
        "success": True,
        "citations_extracted": len(extracted_citations),
        "file_path": file_path,
        "backup_created": backup,
    }


def main():
    """Main cleanup workflow."""
    parser = argparse.ArgumentParser(
        description="Fix corrupted deepsearch.json files with missing citations"
    )
    parser.add_argument(
        "directory",
        type=Path,
        help="Directory to search for corrupted files",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Don't create .backup files (not recommended)",
    )

    args = parser.parse_args()

    if not args.directory.exists():
        print(f"Error: Directory not found: {args.directory}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning {args.directory} for corrupted files...")
    corrupted_files = find_corrupted_files(args.directory)

    if not corrupted_files:
        print("No corrupted files found!")
        return

    print(f"Found {len(corrupted_files)} corrupted file(s)")

    if args.dry_run:
        print("\n=== DRY RUN MODE - No changes will be made ===\n")

    success_count = 0
    error_count = 0

    for file_path in corrupted_files:
        result = extract_and_fix_citations(
            file_path,
            dry_run=args.dry_run,
            backup=not args.no_backup,
        )

        if result["success"]:
            success_count += 1
            status = "[DRY-RUN]" if args.dry_run else "[FIXED]"
            rel_path = file_path.relative_to(args.directory)
            print(f"{status} {rel_path}: {result['citations_extracted']} citations extracted")
        else:
            error_count += 1
            print(f"[SKIP] {file_path.relative_to(args.directory)}: {result['reason']}")

    print(f"\n=== Summary ===")
    print(f"Successfully processed: {success_count}")
    print(f"Skipped/Errors: {error_count}")

    if args.dry_run:
        print("\nTo execute changes, run without --dry-run flag")


if __name__ == "__main__":
    main()
