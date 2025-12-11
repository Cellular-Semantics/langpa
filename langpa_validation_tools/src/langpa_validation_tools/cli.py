"""Command-line interface for langpa-validation-tools.

Provides commands for comparing DeepSearch runs, generating embeddings,
creating visualizations, and building master reports.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser with all subcommands.

    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        prog="langpa-validate",
        description="Validation and analysis tools for LangPA DeepSearch outputs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Compare all runs in a project
  langpa-validate compare --project glioblastoma_ds_auto

  # Generate embeddings for program names
  langpa-validate embed --project glioblastoma_ds_auto --type programs

  # Create visualizations
  langpa-validate visualize --project glioblastoma_ds_auto

  # Generate master report
  langpa-validate report --project glioblastoma_ds_auto

  # Run full pipeline
  langpa-validate pipeline --project glioblastoma_ds_auto
        """
    )

    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # Compare command
    compare_parser = subparsers.add_parser(
        "compare",
        help="Compare gene programs across multiple DeepSearch runs"
    )
    compare_parser.add_argument(
        "--project",
        required=True,
        help="Project name (directory under outputs/)"
    )
    compare_parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs"),
        help="Base output directory (default: outputs/)"
    )
    compare_parser.add_argument(
        "--embeddings",
        type=Path,
        help="Path to pre-generated embeddings file (optional)"
    )
    compare_parser.add_argument(
        "--threshold",
        type=float,
        default=0.3,
        help="Minimum similarity threshold for matching (default: 0.3)"
    )

    # Embed command
    embed_parser = subparsers.add_parser(
        "embed",
        help="Generate embeddings for program or component names"
    )
    embed_parser.add_argument(
        "--project",
        required=True,
        help="Project name"
    )
    embed_parser.add_argument(
        "--type",
        choices=["programs", "components"],
        required=True,
        help="Type of embeddings to generate"
    )
    embed_parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output directory for embeddings"
    )
    embed_parser.add_argument(
        "--components-file",
        type=Path,
        help="Path to component mapping CSV (required for --type components)"
    )

    # Visualize command
    viz_parser = subparsers.add_parser(
        "visualize",
        help="Generate heatmaps and bubble plots"
    )
    viz_parser.add_argument(
        "--project",
        required=True,
        help="Project name"
    )
    viz_parser.add_argument(
        "--matches",
        type=Path,
        required=True,
        help="Path to program matches CSV file"
    )
    viz_parser.add_argument(
        "--output",
        type=Path,
        default=Path("heatmaps"),
        help="Output directory for visualizations (default: heatmaps/)"
    )

    # Report command
    report_parser = subparsers.add_parser(
        "report",
        help="Generate master validation report"
    )
    report_parser.add_argument(
        "--project",
        required=True,
        help="Project name"
    )
    report_parser.add_argument(
        "--matches",
        type=Path,
        required=True,
        help="Path to program matches CSV file"
    )
    report_parser.add_argument(
        "--output",
        type=Path,
        default=Path("master_report.md"),
        help="Output path for master report (default: master_report.md)"
    )

    # Pipeline command (convenience)
    pipeline_parser = subparsers.add_parser(
        "pipeline",
        help="Run full validation pipeline (compare + visualize + report)"
    )
    pipeline_parser.add_argument(
        "--project",
        required=True,
        help="Project name"
    )
    pipeline_parser.add_argument(
        "--use-embeddings",
        action="store_true",
        help="Generate and use embeddings for name similarity"
    )
    pipeline_parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs"),
        help="Base output directory (default: outputs/)"
    )

    return parser


def main() -> int:
    """Main CLI entry point.

    Returns:
        Exit code (0 for success, non-zero for errors)
    """
    parser = create_parser()
    args = parser.parse_args()

    try:
        if args.command == "compare":
            from langpa_validation_tools.analysis import compare_runs

            print(f"[compare] Project: {args.project}")
            print(f"[compare] Output directory: {args.output_dir}")
            print(f"[compare] Threshold: {args.threshold}")

            if args.embeddings:
                print(f"[compare] Using embeddings from: {args.embeddings}")
                print("⚠️  Embeddings integration not yet implemented (Phase 5)")

            # Run comparison
            print("\nComparing runs...")
            df = compare_runs(
                project=args.project,
                output_dir=args.output_dir,
                threshold=args.threshold,
                embeddings_path=args.embeddings,
                save_csv=True,
                csv_output_dir=args.output_dir / args.project / "analysis"
            )

            print(f"\n✓ Comparison complete!")
            print(f"  - Found {len(df)} program matches")
            print(f"  - Results saved to: {args.output_dir / args.project / 'analysis'}")
            print(f"    • program_matches.csv")
            print(f"    • unmatched_programs.csv")

            return 0

        elif args.command == "embed":
            from langpa_validation_tools.analysis import generate_project_embeddings

            print(f"[embed] Project: {args.project}")
            print(f"[embed] Type: {args.type}")
            print(f"[embed] Output: {args.output}")

            if args.type == "components":
                if not args.components_file:
                    print("❌ Error: --components-file required for --type components")
                    return 1
                print("\n⚠️  Component embeddings not yet implemented")
                print("Currently only 'programs' type is supported")
                return 1

            # Generate embeddings for programs
            print(f"\nGenerating embeddings for programs in project: {args.project}")
            print("This may take a while depending on the number of programs...")

            try:
                embeddings = generate_project_embeddings(
                    project=args.project,
                    embeddings_output=args.output
                )

                if not embeddings:
                    print("\n⚠️  No programs found in project")
                    return 1

                print(f"\n✓ Embedding generation complete!")
                print(f"  - Generated {len(embeddings)} embeddings")
                print(f"  - Saved to: {args.output.parent}")
                print(f"    • {args.output.name}_index.csv")
                print(f"    • {args.output.name}_vectors.npy")

                return 0

            except Exception as e:
                print(f"\n❌ Error generating embeddings: {e}")
                return 1

        elif args.command == "visualize":
            from langpa_validation_tools.visualization import generate_bubble_plot
            import pandas as pd

            print(f"[visualize] Project: {args.project}")
            print(f"[visualize] Matches file: {args.matches}")
            print(f"[visualize] Output directory: {args.output}")

            # Check if matches file exists
            if not args.matches.exists():
                print(f"\n❌ Error: Matches file not found: {args.matches}")
                print("Run 'langpa-validate compare' first to generate matches.")
                return 1

            # Create output directory
            args.output.mkdir(parents=True, exist_ok=True)

            # Load matches
            print("\nLoading program matches...")
            matches_df = pd.read_csv(args.matches)
            print(f"  - Loaded {len(matches_df)} program matches")

            # Generate bubble plot
            print("\nGenerating bubble plot...")
            bubble_path = args.output / "bubble_plot.png"
            generate_bubble_plot(matches_df, bubble_path)
            print(f"  ✓ Saved to: {bubble_path}")

            # Generate per-query bubble plots
            if "query" in matches_df.columns:
                queries = matches_df["query"].unique()
                print(f"\nGenerating per-query bubble plots ({len(queries)} queries)...")
                for query in queries:
                    query_bubble_path = args.output / f"bubble_plot_{query}.png"
                    generate_bubble_plot(matches_df, query_bubble_path, query=query)
                    print(f"  ✓ {query}: {query_bubble_path}")

            print(f"\n✓ Visualization complete!")
            print(f"  - Output directory: {args.output}")
            print("\n⚠️  Note: Confusion matrix requires embeddings (coming in Phase 5)")

            return 0

        elif args.command == "report":
            from langpa_validation_tools.reporting import build_master_report
            import pandas as pd

            print(f"[report] Project: {args.project}")
            print(f"[report] Matches: {args.matches}")
            print(f"[report] Output: {args.output}")

            # Check if matches file exists
            if not args.matches.exists():
                print(f"\n❌ Error: Matches file not found: {args.matches}")
                print("Run 'langpa-validate compare' first to generate matches.")
                return 1

            # Load matches
            print("\nLoading program matches...")
            matches_df = pd.read_csv(args.matches)
            print(f"  - Loaded {len(matches_df)} program matches")

            # Generate master report
            print("\nGenerating master validation report...")
            build_master_report(
                project=args.project,
                matches_df=matches_df,
                output_path=args.output,
            )

            print(f"\n✓ Master report generated!")
            print(f"  - Output: {args.output}")
            return 0

        elif args.command == "pipeline":
            from langpa_validation_tools.analysis import compare_runs, generate_project_embeddings
            from langpa_validation_tools.visualization import generate_bubble_plot
            from langpa_validation_tools.reporting import build_master_report
            import pandas as pd

            print(f"[pipeline] Project: {args.project}")
            print(f"[pipeline] Use embeddings: {args.use_embeddings}")
            print(f"[pipeline] Output directory: {args.output_dir}")
            print("\nRunning full validation pipeline...")

            # Setup paths
            analysis_dir = args.output_dir / args.project / "analysis"
            heatmaps_dir = analysis_dir / "heatmaps"
            matches_csv = analysis_dir / "program_matches.csv"
            report_path = analysis_dir / "validation_report.md"

            # Step 1: Generate embeddings (if requested)
            embeddings_path = None
            if args.use_embeddings:
                print("\n[1/4] Generating embeddings...")
                embeddings_output = args.output_dir / args.project / "embeddings" / "programs"
                try:
                    embeddings = generate_project_embeddings(
                        project=args.project,
                        output_dir=args.output_dir,
                        embeddings_output=embeddings_output
                    )
                    if embeddings:
                        embeddings_path = embeddings_output
                        print(f"  ✓ Generated {len(embeddings)} embeddings")
                    else:
                        print("  ⚠️  No programs found for embeddings")
                except Exception as e:
                    print(f"  ⚠️  Embedding generation failed: {e}")
                    print("  Continuing without embeddings...")
            else:
                print("\n[1/4] Skipping embeddings (use --use-embeddings to enable)")

            # Step 2: Compare runs
            print("\n[2/4] Comparing runs...")
            df = compare_runs(
                project=args.project,
                output_dir=args.output_dir,
                threshold=0.3,
                embeddings_path=embeddings_path,
                save_csv=True,
                csv_output_dir=analysis_dir
            )
            print(f"  ✓ Found {len(df)} program matches")

            # Step 3: Generate visualizations
            print("\n[3/4] Generating visualizations...")
            heatmaps_dir.mkdir(parents=True, exist_ok=True)

            # Overall bubble plot
            bubble_path = heatmaps_dir / "bubble_plot.png"
            generate_bubble_plot(df, bubble_path)
            print(f"  ✓ Overall bubble plot: {bubble_path.name}")

            # Per-query bubble plots
            if "query" in df.columns:
                queries = df["query"].unique()
                for query in queries:
                    query_bubble_path = heatmaps_dir / f"bubble_plot_{query}.png"
                    generate_bubble_plot(df, query_bubble_path, query=query)
                print(f"  ✓ Per-query plots: {len(queries)} queries")

            # Step 4: Generate master report
            print("\n[4/4] Generating master report...")
            build_master_report(
                project=args.project,
                matches_df=df,
                output_path=report_path,
                output_dir=args.output_dir,
                include_plots=True,
                plot_dir=heatmaps_dir
            )
            print(f"  ✓ Master report: {report_path.name}")

            print(f"\n{'='*60}")
            print("✓ Pipeline complete!")
            print(f"{'='*60}")
            print(f"  - Matches: {len(df)} program matches")
            print(f"  - Visualizations: {heatmaps_dir}")
            print(f"  - Master report: {report_path}")
            print(f"\nView the master report at: {report_path}")

            return 0

        else:
            parser.print_help()
            return 1

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
