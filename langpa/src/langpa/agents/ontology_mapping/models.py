"""Pydantic data models for ontology mapping agent.

This module defines the input and output schemas for mapping biological terms
to standardized ontology identifiers (GO, CL, UBERON, ChEBI).
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class OntologyMapping(BaseModel):
    """Single ontology mapping result.

    Represents the mapping of a biological term to a standardized ontology
    identifier with confidence scoring and method tracking.

    Attributes:
        term: The input biological term exactly as provided
        ontology_id: The matched ontology term ID (e.g., "GO:0008150") or None if no match
        ontology_label: The official label from the ontology or None if no match
        ontology_source: The ontology name ("GO", "CL", "UBERON", "ChEBI") or None
        confidence: Match quality score from 0.0 to 1.0, or None if no match
        mapping_method: Description of how the match was found (e.g., "exact_match",
            "partial_match", "synonym_match") or None if no match

    Example:
        .. code-block:: python

            mapping = OntologyMapping(
                term="neutrophil chemotaxis",
                ontology_id="GO:0030593",
                ontology_label="neutrophil chemotaxis",
                ontology_source="GO",
                confidence=1.0,
                mapping_method="exact_match"
            )
    """

    term: str
    ontology_id: Optional[str] = None
    ontology_label: Optional[str] = None
    ontology_source: Optional[str] = None
    confidence: Optional[float] = None
    mapping_method: Optional[str] = None


class OntologyMappingResponse(BaseModel):
    """Collection of ontology mapping results.

    Container for multiple mapping results with optional metadata about
    the mapping operation.

    Attributes:
        mappings: List of individual ontology mappings
        metadata: Optional metadata about the mapping operation (e.g., timestamp,
            model used, total terms processed)

    Example:
        .. code-block:: python

            response = OntologyMappingResponse(
                mappings=[
                    OntologyMapping(term="test1", ontology_id="GO:0001"),
                    OntologyMapping(term="test2", ontology_id="GO:0002")
                ],
                metadata={"model": "gpt-4o", "timestamp": "2024-01-01"}
            )
    """

    mappings: List[OntologyMapping]
    metadata: Dict[str, Any] = Field(default_factory=dict)
