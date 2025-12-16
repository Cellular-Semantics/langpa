"""CSV batch parser for deepsearch queries.

This module provides functionality to parse CSV files containing batch deepsearch
queries with support for query naming, context handling, and validation.
"""

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class BatchQuery:
    """Represents a single query parsed from CSV batch file.

    Attributes:
        query_name: Generated query name from ID and/or name columns
        genes: List of gene symbols to analyze
        context: Biological context for the query (per-row or global)
        gse_terms: List of gene set enrichment terms (optional)
        row_number: CSV row number for error reporting (1-indexed)
    """

    query_name: str
    genes: list[str]
    context: str
    gse_terms: list[str]
    row_number: int


def parse_csv_batch(csv_path: Path, global_context: str | None) -> list[BatchQuery]:
    """Parse CSV file containing batch deepsearch queries.

    The CSV must contain columns for gene_list and at least one of ID or name.
    Optional columns: context, GSE.

    Query naming rules:
        - If both ID and name present: ``{ID}_{name}``
        - If only ID present: ``{ID}``
        - If only name present: ``{name}``

    Context handling:
        - Per-row context overrides global context
        - If no per-row context, global context is required
        - ValueError raised if neither provided

    Args:
        csv_path: Path to CSV file with batch queries
        global_context: Global context to use when per-row context is missing.
            If None and a row lacks context, ValueError is raised.

    Returns:
        List of BatchQuery objects parsed from CSV

    Raises:
        ValueError: If CSV validation fails (missing columns, empty required fields,
            duplicate query names, missing context, etc.)

    Example:
        .. code-block:: python

            queries = parse_csv_batch(
                Path("queries.csv"),
                global_context="General biological context"
            )
            for query in queries:
                print(f"Query: {query.query_name}, Genes: {query.genes}")
    """
    # Read CSV file with UTF-8 encoding
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []

        # Validate required columns
        if "gene_list" not in fieldnames:
            raise ValueError("Required column 'gene_list' not found in CSV")

        if "ID" not in fieldnames and "name" not in fieldnames:
            raise ValueError("CSV must contain at least one of 'ID' or 'name' columns")

        # Parse rows
        queries: list[BatchQuery] = []
        seen_query_names: dict[str, int] = {}  # query_name -> row_number

        for row_idx, row in enumerate(reader, start=1):
            # Generate query name
            id_val = row.get("ID", "").strip()
            name_val = row.get("name", "").strip()

            if not id_val and not name_val:
                raise ValueError(
                    f"Row {row_idx}: must have at least one of 'ID' or 'name'"
                )

            if id_val and name_val:
                query_name = f"{id_val}_{name_val}"
            elif id_val:
                query_name = id_val
            else:
                query_name = name_val

            # Check for duplicate query names
            if query_name in seen_query_names:
                raise ValueError(
                    f"Duplicate query name '{query_name}' found in rows "
                    f"{seen_query_names[query_name]} and {row_idx}"
                )
            seen_query_names[query_name] = row_idx

            # Parse gene list
            gene_list_str = row.get("gene_list", "").strip()
            if not gene_list_str:
                raise ValueError(f"Row {row_idx}: gene_list cannot be empty")

            genes = [gene.strip() for gene in gene_list_str.split(",") if gene.strip()]
            if not genes:
                raise ValueError(f"Row {row_idx}: gene_list cannot be empty")

            # Parse context (per-row overrides global)
            row_context = row.get("context", "").strip()
            if row_context:
                context = row_context
            elif global_context:
                context = global_context
            else:
                raise ValueError(
                    f"Row {row_idx}: No context provided (missing both per-row and global context)"
                )

            # Parse GSE terms (optional)
            gse_str = row.get("GSE", "").strip()
            if gse_str:
                gse_terms = [term.strip() for term in gse_str.split(",") if term.strip()]
            else:
                gse_terms = []

            # Create BatchQuery
            queries.append(
                BatchQuery(
                    query_name=query_name,
                    genes=genes,
                    context=context,
                    gse_terms=gse_terms,
                    row_number=row_idx,
                )
            )

    return queries
