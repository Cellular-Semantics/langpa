"""Ontology search tools using OAKlib for the mapping agent.

This module provides search functions for querying various ontologies
(GO, CL, UBERON, ChEBI) via the Ontology Lookup Service (OLS).
"""

from __future__ import annotations

import logging
from typing import List, Tuple

from oaklib import get_adapter
from pydantic_ai import RunContext

from .config import OntologyMappingDependencies

logger = logging.getLogger(__name__)


def search_go(ctx: RunContext[OntologyMappingDependencies], term: str) -> List[Tuple[str, str]]:
    """Search the Gene Ontology for a term.

    Uses OAKlib to search the Gene Ontology via OLS (Ontology Lookup Service).
    Returns up to 10 matching terms with their IDs and labels.

    Args:
        ctx: The run context with dependencies (required by pydantic-ai)
        term: The biological term to search for

    Returns:
        A list of tuples, each containing a GO ID and its label.
        Returns empty list if search fails.

    Example:
        .. code-block:: python

            # Called automatically by the agent
            results = search_go(ctx, "neutrophil chemotaxis")
            # Returns: [("GO:0030593", "neutrophil chemotaxis"), ...]
    """
    try:
        adapter = get_adapter("ols:go")
        results = adapter.basic_search(term)
        labels = list(adapter.labels(results))
        logger.info(f"GO search for '{term}' returned {len(labels)} results")
        return labels[:10]  # Limit to top 10 results
    except Exception as e:
        logger.error(f"Error searching GO for term '{term}': {e}")
        return []


def search_cl(ctx: RunContext[OntologyMappingDependencies], term: str) -> List[Tuple[str, str]]:
    """Search the Cell Ontology for a term.

    Uses OAKlib to search the Cell Ontology via OLS.

    Args:
        ctx: The run context with dependencies
        term: The cell type or cellular structure term to search for

    Returns:
        A list of tuples, each containing a CL ID and its label.
        Returns empty list if search fails.

    Example:
        .. code-block:: python

            results = search_cl(ctx, "neuron")
            # Returns: [("CL:0000540", "neuron"), ...]
    """
    try:
        adapter = get_adapter("ols:cl")
        results = adapter.basic_search(term)
        labels = list(adapter.labels(results))
        logger.info(f"CL search for '{term}' returned {len(labels)} results")
        return labels[:10]
    except Exception as e:
        logger.error(f"Error searching CL for term '{term}': {e}")
        return []


def search_uberon(ctx: RunContext[OntologyMappingDependencies], term: str) -> List[Tuple[str, str]]:
    """Search the UBERON anatomy ontology for a term.

    Uses OAKlib to search UBERON via OLS.

    Args:
        ctx: The run context with dependencies
        term: The anatomical structure or tissue term to search for

    Returns:
        A list of tuples, each containing a UBERON ID and its label.
        Returns empty list if search fails.

    Example:
        .. code-block:: python

            results = search_uberon(ctx, "brain")
            # Returns: [("UBERON:0000955", "brain"), ...]
    """
    try:
        adapter = get_adapter("ols:uberon")
        results = adapter.basic_search(term)
        labels = list(adapter.labels(results))
        logger.info(f"UBERON search for '{term}' returned {len(labels)} results")
        return labels[:10]
    except Exception as e:
        logger.error(f"Error searching UBERON for term '{term}': {e}")
        return []


def search_chebi(ctx: RunContext[OntologyMappingDependencies], term: str) -> List[Tuple[str, str]]:
    """Search the ChEBI chemical ontology for a term.

    Uses OAKlib to search ChEBI via OLS.

    Args:
        ctx: The run context with dependencies
        term: The chemical compound or molecular entity term to search for

    Returns:
        A list of tuples, each containing a ChEBI ID and its label.
        Returns empty list if search fails.

    Example:
        .. code-block:: python

            results = search_chebi(ctx, "glucose")
            # Returns: [("CHEBI:17234", "glucose"), ...]
    """
    try:
        adapter = get_adapter("ols:chebi")
        results = adapter.basic_search(term)
        labels = list(adapter.labels(results))
        logger.info(f"ChEBI search for '{term}' returned {len(labels)} results")
        return labels[:10]
    except Exception as e:
        logger.error(f"Error searching ChEBI for term '{term}': {e}")
        return []
