"""Generate README.md files for batch deepsearch projects.

This module provides functionality to automatically generate comprehensive README.md
files that summarize batch deepsearch project results, including query details,
gene program summaries, and links to detailed results.
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass
class ProgramSummary:
    """Summary of a gene program across multiple runs.

    Attributes:
        name: Program name
        total_genes: Total number of unique genes in this program
        total_citations: Total number of citations across all runs
    """

    name: str
    total_genes: int
    total_citations: int


@dataclass
class RunData:
    """Data for a single deepsearch run.

    Attributes:
        timestamp: Timestamp of the run
        run_dir: Directory path for this run
        deepsearch_container_path: Path to deepsearch_container.md
        deepsearch_structured_path: Path to deepsearch_structured.json
    """

    timestamp: datetime
    run_dir: Path
    deepsearch_container_path: Path
    deepsearch_structured_path: Path


@dataclass
class QueryData:
    """Data for a single query in the batch project.

    Attributes:
        query_name: Name of the query (directory name)
        context: Biological context description
        num_genes: Total number of genes in the input list
        num_genes_covered: Number of genes covered by programs
        programs: List of program summaries
        runs: List of run data
    """

    query_name: str
    context: str
    num_genes: int
    num_genes_covered: int
    programs: list[ProgramSummary] = field(default_factory=list)
    runs: list[RunData] = field(default_factory=list)


@dataclass
class ProjectData:
    """Complete data for a batch deepsearch project.

    Attributes:
        project_name: Name of the project (directory name)
        about_text: Content from about.md if present
        input_csv_path: Path to input.csv if present
        queries: List of query data
    """

    project_name: str
    about_text: str | None = None
    input_csv_path: Path | None = None
    queries: list[QueryData] = field(default_factory=list)


def collect_project_data(project_dir: Path) -> ProjectData:
    """Collect all data from a batch project directory.

    Scans the project directory structure to extract metadata, query information,
    run details, and program summaries.

    Args:
        project_dir: Path to the batch project directory

    Returns:
        ProjectData object containing all collected information

    Example:
        .. code-block:: python

            from pathlib import Path
            from langpa.utils.readme_generator import collect_project_data

            project_data = collect_project_data(Path("outputs/my_project"))
            print(f"Project: {project_data.project_name}")
            print(f"Queries: {len(project_data.queries)}")
    """
    project_name = project_dir.name

    # Check for about.md
    about_path = project_dir / "about.md"
    about_text = about_path.read_text() if about_path.exists() else None

    # Check for input.csv
    input_csv_path = project_dir / "input.csv"
    if not input_csv_path.exists():
        input_csv_path = None

    # Collect query directories
    queries: list[QueryData] = []

    for query_dir in sorted(project_dir.iterdir()):
        # Skip non-directories and special directories
        if not query_dir.is_dir():
            continue
        if query_dir.name in {"analysis", "embeddings", ".git"}:
            continue

        # Extract query name
        query_name = query_dir.name

        # Collect runs for this query
        runs: list[RunData] = []
        program_data: dict[str, dict[str, set]] = defaultdict(
            lambda: {"genes": set(), "citations": set()}
        )
        all_input_genes: set[str] = set()
        context_str = ""

        for run_dir in sorted(query_dir.iterdir()):
            # Skip non-directories and markdown files
            if not run_dir.is_dir():
                continue

            # Look for deepsearch_structured.json
            structured_path = run_dir / "deepsearch_structured.json"
            container_path = run_dir / "deepsearch_container.md"

            if not structured_path.exists():
                continue

            try:
                # Parse structured JSON
                with open(structured_path) as f:
                    data = json.load(f)

                # Extract timestamp
                timestamp_str = data.get("metadata", {}).get("timestamp", "")
                try:
                    timestamp = datetime.fromisoformat(timestamp_str)
                except (ValueError, TypeError):
                    # Fallback to directory name
                    timestamp = datetime.strptime(run_dir.name, "%Y%m%d_%H%M%S")

                # Collect input genes from first run
                if not all_input_genes:
                    all_input_genes = set(data.get("metadata", {}).get("genes", []))

                # Extract context from first run
                if not context_str:
                    context = data.get("metadata", {}).get("context", {})
                    if isinstance(context, dict):
                        parts = []
                        if "cell_type" in context:
                            parts.append(f"cell_type: {context['cell_type']}")
                        if "disease" in context:
                            parts.append(f"disease: {context['disease']}")
                        if "tissue" in context:
                            parts.append(f"tissue: {context['tissue']}")
                        context_str = ", ".join(parts)
                    elif isinstance(context, str):
                        context_str = context

                # Aggregate program data
                for program in data.get("programs", []):
                    prog_name = program.get("name", "")
                    if not prog_name:
                        continue

                    # Add genes
                    prog_genes = program.get("genes", [])
                    program_data[prog_name]["genes"].update(prog_genes)

                    # Add citations
                    citations = program.get("citations", [])
                    for cit in citations:
                        if isinstance(cit, dict) and "source_id" in cit:
                            program_data[prog_name]["citations"].add(cit["source_id"])
                        elif isinstance(cit, str):
                            program_data[prog_name]["citations"].add(cit)

                # Create run data
                run_data = RunData(
                    timestamp=timestamp,
                    run_dir=run_dir,
                    deepsearch_container_path=container_path,
                    deepsearch_structured_path=structured_path,
                )
                runs.append(run_data)

            except (json.JSONDecodeError, KeyError, ValueError):
                # Skip malformed files
                continue

        # Skip query if no valid runs found
        if not runs:
            continue

        # Create program summaries
        programs = [
            ProgramSummary(
                name=prog_name,
                total_genes=len(prog_data["genes"]),
                total_citations=len(prog_data["citations"]),
            )
            for prog_name, prog_data in program_data.items()
        ]

        # Calculate gene coverage
        covered_genes = set()
        for prog_data in program_data.values():
            covered_genes.update(prog_data["genes"])
        num_genes_covered = len(covered_genes & all_input_genes)

        # Create query data
        query_data = QueryData(
            query_name=query_name,
            context=context_str,
            num_genes=len(all_input_genes),
            num_genes_covered=num_genes_covered,
            programs=programs,
            runs=runs,
        )
        queries.append(query_data)

    return ProjectData(
        project_name=project_name,
        about_text=about_text,
        input_csv_path=input_csv_path,
        queries=queries,
    )


def format_readme_markdown(project_data: ProjectData) -> str:
    """Format project data as README markdown.

    Creates a formatted README with project title, about section, input CSV link,
    and detailed results for each query including program tables and run links.

    Args:
        project_data: Collected project data

    Returns:
        Formatted README content as markdown string

    Example:
        .. code-block:: python

            from langpa.utils.readme_generator import collect_project_data, format_readme_markdown

            project_data = collect_project_data(Path("outputs/my_project"))
            readme_content = format_readme_markdown(project_data)
            print(readme_content)
    """
    lines = []

    # Title
    lines.append(f"# {project_data.project_name}")
    lines.append("")

    # About section
    if project_data.about_text:
        lines.append(project_data.about_text.strip())
        lines.append("")

    # Input CSV link
    if project_data.input_csv_path:
        lines.append("**Input data**: [input.csv](input.csv)")
        lines.append("")

    # Results section
    lines.append("## Results")
    lines.append("")

    # Process each query
    for query in project_data.queries:
        lines.append(f"### {query.query_name}")
        lines.append("")

        # Context and gene info
        if query.context:
            lines.append(f"**Context**: {query.context}")
            lines.append("")

        coverage_pct = (
            round(100 * query.num_genes_covered / query.num_genes)
            if query.num_genes > 0
            else 0
        )
        lines.append(
            f"**Genes**: {query.num_genes} total, "
            f"{query.num_genes_covered} covered by programs ({coverage_pct}%)"
        )
        lines.append("")

        # Programs section in details fold
        if query.programs:
            lines.append("#### Details")
            lines.append("")
            lines.append("<details>")
            lines.append("<summary>Gene Programs</summary>")
            lines.append("")

            # Program table
            lines.append("| Program Name | Genes | Citations |")
            lines.append("|---|---|---|")
            for program in query.programs:
                lines.append(
                    f"| {program.name} | {program.total_genes} | {program.total_citations} |"
                )
            lines.append("")
            lines.append("</details>")
            lines.append("")

        # Runs section
        lines.append("#### Runs")
        lines.append("")

        for run in sorted(query.runs, key=lambda r: r.timestamp, reverse=True):
            run_name = run.run_dir.name
            rel_container = f"{query.query_name}/{run_name}/deepsearch_container.md"
            rel_structured = f"{query.query_name}/{run_name}/deepsearch_structured.json"

            lines.append(
                f"- **{run_name}**: "
                f"[deepsearch_container.md]({rel_container}) | "
                f"[deepsearch_structured.json]({rel_structured})"
            )

        lines.append("")

    return "\n".join(lines)


def generate_batch_readme(project_dir: Path) -> Path:
    """Generate README.md file for a batch project directory.

    This is the main entry point for README generation. It collects all project
    data and writes a formatted README.md file to the project directory.

    Args:
        project_dir: Path to the batch project directory

    Returns:
        Path to the generated README.md file

    Example:
        .. code-block:: python

            from pathlib import Path
            from langpa.utils.readme_generator import generate_batch_readme

            readme_path = generate_batch_readme(Path("outputs/my_project"))
            print(f"README generated at: {readme_path}")
    """
    project_data = collect_project_data(project_dir)
    readme_content = format_readme_markdown(project_data)

    readme_path = project_dir / "README.md"
    readme_path.write_text(readme_content)

    return readme_path
