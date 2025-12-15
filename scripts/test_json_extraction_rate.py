#!/usr/bin/env python3
"""Test JSON extraction success rate for perplexity-sonar-schema-embedded preset.

This script runs multiple API calls with the same minimal test case to measure
how reliably JSON can be extracted and validated from the responses.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from dotenv import load_dotenv

from langpa.services import DeepSearchService, OutputManager

# Load environment variables
load_dotenv()

# Test configuration
GENES = ["CCDC92", "C21orf91_obesity"]
CONTEXT = "obesity"
PRESET = "perplexity-sonar-schema-embedded"
NUM_RUNS = 4


def run_single_test(run_num: int, run_dir: Path) -> dict:
    """Execute one API call and capture extraction metrics.

    Args:
        run_num: Run number (1-indexed)
        run_dir: Directory to save artifacts for this run

    Returns:
        Dict with metrics about extraction success and response characteristics
    """
    print(f"\n{'='*60}")
    print(f"Run {run_num}/{NUM_RUNS}")
    print(f"{'='*60}")

    # Initialize service and output manager
    service = DeepSearchService(preset=PRESET)
    output_manager = OutputManager(output_dir=run_dir)

    # Make API call
    print(f"Calling API with genes={GENES}, context='{CONTEXT}'...")
    result = service.research_gene_list(GENES, CONTEXT)
    print(f"✓ API call completed (duration: {result.duration_seconds:.1f}s)")

    # Save raw response
    raw_file = output_manager.save_raw_response(
        result,
        GENES,
        CONTEXT,
        metadata={
            "test_run": run_num,
            "test_timestamp": datetime.now().isoformat(),
        },
    )
    print(f"✓ Saved raw response: {raw_file}")

    # Analyze response characteristics
    markdown = result.markdown
    metrics = {
        "run": run_num,
        "timestamp": datetime.now().isoformat(),
        "response_length": len(markdown),
        "has_think_tags": "</think>" in markdown,
        "has_json_fence": "```json" in markdown,
        "raw_file": str(raw_file),
    }

    # Try JSON extraction
    print("Attempting JSON extraction...")
    extracted = output_manager.extract_json_from_markdown(markdown)
    metrics["extraction_success"] = extracted is not None

    if extracted:
        print("✓ JSON extracted successfully")

        # Save extracted JSON
        extracted_file = run_dir / "extracted.json"
        with open(extracted_file, "w", encoding="utf-8") as f:
            json.dump(extracted, f, indent=2, ensure_ascii=False)
        metrics["extracted_file"] = str(extracted_file)

        # Try schema validation
        print("Validating against schema...")
        is_valid, error = output_manager.validate_against_schema(extracted)
        metrics["schema_valid"] = is_valid

        if is_valid:
            print("✓ Schema validation passed")
            metrics["program_count"] = len(extracted.get("programs", []))
            metrics["validation_error"] = None
        else:
            print(f"✗ Schema validation failed: {error}")
            metrics["program_count"] = 0
            metrics["validation_error"] = str(error)
    else:
        print("✗ JSON extraction failed")
        metrics["schema_valid"] = False
        metrics["validation_error"] = "Extraction failed"
        metrics["program_count"] = 0
        metrics["extracted_file"] = None

    # Save extraction log
    log_file = run_dir / "extraction_log.txt"
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"Run {run_num} - {datetime.now().isoformat()}\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Genes: {GENES}\n")
        f.write(f"Context: {CONTEXT}\n")
        f.write(f"Preset: {PRESET}\n\n")
        f.write("Response Characteristics:\n")
        f.write(f"  Length: {metrics['response_length']} characters\n")
        f.write(f"  Has <think> tags: {metrics['has_think_tags']}\n")
        f.write(f"  Has ```json fence: {metrics['has_json_fence']}\n\n")
        f.write("Extraction Results:\n")
        f.write(f"  Extraction success: {metrics['extraction_success']}\n")
        f.write(f"  Schema valid: {metrics['schema_valid']}\n")
        f.write(f"  Program count: {metrics['program_count']}\n")
        if metrics["validation_error"]:
            f.write(f"  Error: {metrics['validation_error']}\n")

    metrics["log_file"] = str(log_file)

    # Print summary
    status = "✓ SUCCESS" if metrics["extraction_success"] and metrics["schema_valid"] else "✗ FAILURE"
    print(f"\n{status}")
    print(f"  Extraction: {metrics['extraction_success']}")
    print(f"  Validation: {metrics['schema_valid']}")
    print(f"  Programs: {metrics['program_count']}")

    return metrics


def generate_summary(all_metrics: list[dict], output_dir: Path) -> None:
    """Generate summary report from all test runs.

    Args:
        all_metrics: List of metrics dicts from all runs
        output_dir: Directory to save summary files
    """
    # Calculate aggregate statistics
    total_runs = len(all_metrics)
    extraction_successes = sum(1 for m in all_metrics if m["extraction_success"])
    validation_successes = sum(1 for m in all_metrics if m["schema_valid"])
    full_successes = sum(
        1 for m in all_metrics if m["extraction_success"] and m["schema_valid"]
    )

    # Analyze response characteristics
    has_think = sum(1 for m in all_metrics if m["has_think_tags"])
    has_fence = sum(1 for m in all_metrics if m["has_json_fence"])
    avg_length = sum(m["response_length"] for m in all_metrics) / total_runs
    avg_programs = (
        sum(m["program_count"] for m in all_metrics if m["program_count"] > 0)
        / full_successes
        if full_successes > 0
        else 0
    )

    # Save JSON summary
    summary_data = {
        "test_config": {
            "genes": GENES,
            "context": CONTEXT,
            "preset": PRESET,
            "num_runs": NUM_RUNS,
        },
        "summary": {
            "total_runs": total_runs,
            "extraction_successes": extraction_successes,
            "validation_successes": validation_successes,
            "full_successes": full_successes,
            "extraction_rate": extraction_successes / total_runs,
            "validation_rate": validation_successes / total_runs,
            "full_success_rate": full_successes / total_runs,
        },
        "response_characteristics": {
            "has_think_tags_count": has_think,
            "has_json_fence_count": has_fence,
            "avg_response_length": avg_length,
            "avg_program_count": avg_programs,
        },
        "runs": all_metrics,
    }

    summary_json = output_dir / "summary.json"
    with open(summary_json, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2, ensure_ascii=False)

    # Generate text summary
    summary_text = output_dir / "summary.txt"
    with open(summary_text, "w", encoding="utf-8") as f:
        f.write("JSON Extraction Success Rate Test Results\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Test Configuration:\n")
        f.write(f"  Genes: {', '.join(GENES)}\n")
        f.write(f"  Context: {CONTEXT}\n")
        f.write(f"  Preset: {PRESET}\n")
        f.write(f"  Number of runs: {total_runs}\n\n")

        f.write("Success Rates:\n")
        f.write(f"  Extraction:  {extraction_successes}/{total_runs} ({extraction_successes/total_runs*100:.1f}%)\n")
        f.write(f"  Validation:  {validation_successes}/{total_runs} ({validation_successes/total_runs*100:.1f}%)\n")
        f.write(f"  Full Success: {full_successes}/{total_runs} ({full_successes/total_runs*100:.1f}%)\n\n")

        f.write("Response Characteristics:\n")
        f.write(f"  Responses with <think> tags: {has_think}/{total_runs} ({has_think/total_runs*100:.1f}%)\n")
        f.write(f"  Responses with ```json fence: {has_fence}/{total_runs} ({has_fence/total_runs*100:.1f}%)\n")
        f.write(f"  Average response length: {avg_length:.0f} characters\n")
        f.write(f"  Average program count (successful): {avg_programs:.1f}\n\n")

        f.write("Assessment:\n")
        success_rate = full_successes / total_runs
        if success_rate >= 0.9:
            assessment = "✓ EXCELLENT - Success rate meets target (≥90%)"
        elif success_rate >= 0.8:
            assessment = "⚠ ACCEPTABLE - Success rate acceptable (≥80%)"
        else:
            assessment = "✗ CONCERNING - Success rate below acceptable threshold (<80%)"
        f.write(f"  {assessment}\n\n")

        # List failures if any
        failures = [m for m in all_metrics if not (m["extraction_success"] and m["schema_valid"])]
        if failures:
            f.write(f"Failed Runs ({len(failures)}):\n")
            for m in failures:
                f.write(f"  Run {m['run']}: {m['validation_error']}\n")
        else:
            f.write("All runs succeeded!\n")

    print(f"\n✓ Summary saved:")
    print(f"  JSON: {summary_json}")
    print(f"  Text: {summary_text}")


def main():
    """Main test execution."""
    print("JSON Extraction Success Rate Test")
    print("=" * 60)
    print(f"Test Configuration:")
    print(f"  Genes: {', '.join(GENES)}")
    print(f"  Context: {CONTEXT}")
    print(f"  Preset: {PRESET}")
    print(f"  Number of runs: {NUM_RUNS}")
    print()
    print(f"Expected cost: $0.50-1.50")
    print(f"Expected time: 30-50 minutes")
    print()

    # Create timestamped output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(f"test_results/json_extraction_test_{timestamp}")
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {output_dir}")

    # Run all tests
    all_metrics = []
    try:
        for i in range(1, NUM_RUNS + 1):
            run_dir = output_dir / f"run_{i:03d}"
            run_dir.mkdir(exist_ok=True)

            metrics = run_single_test(i, run_dir)
            all_metrics.append(metrics)

        # Generate summary
        print("\n" + "=" * 60)
        print("GENERATING SUMMARY")
        print("=" * 60)
        generate_summary(all_metrics, output_dir)

        # Print final results
        full_successes = sum(
            1 for m in all_metrics if m["extraction_success"] and m["schema_valid"]
        )
        print(f"\n{'='*60}")
        print("FINAL RESULTS")
        print(f"{'='*60}")
        print(f"Total runs: {NUM_RUNS}")
        print(f"Successful: {full_successes}/{NUM_RUNS} ({full_successes/NUM_RUNS*100:.1f}%)")
        print(f"Output: {output_dir}")
        print(f"{'='*60}")

    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        if all_metrics:
            print(f"Completed {len(all_metrics)} runs before interruption")
            generate_summary(all_metrics, output_dir)
        sys.exit(1)
    except Exception as e:
        print(f"\n\nError during test: {e}")
        if all_metrics:
            print(f"Completed {len(all_metrics)} runs before error")
            generate_summary(all_metrics, output_dir)
        raise


if __name__ == "__main__":
    main()
