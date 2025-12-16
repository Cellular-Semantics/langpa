"""Ontology mapping agent for mapping biological terms to standardized ontologies.

This module provides functionality to map atomic biological processes and
cellular components to Gene Ontology (GO) and other ontology terms.
"""

from __future__ import annotations

from .models import OntologyMapping, OntologyMappingResponse

__all__ = [
    "OntologyMapping",
    "OntologyMappingResponse",
]
