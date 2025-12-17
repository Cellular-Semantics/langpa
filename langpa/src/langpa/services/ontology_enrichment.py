"""Ontology enrichment service for deepsearch results.

This module provides functionality to enrich validated deepsearch results with
ontology mappings for atomic biological processes and cellular components.
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


class OntologyEnricher:
    """Enriches deepsearch results with ontology mappings.

    This service extracts atomic terms from validated deepsearch output,
    maps them to ontology identifiers using the ontology mapping agent,
    and injects the mappings back into the data structure.

    Example:
        .. code-block:: python

            from langpa.services.ontology_enrichment import OntologyEnricher
            from langpa.agents.ontology_mapping import build_ontology_mapping_agent
            from langpa.agents.ontology_mapping.config import OntologyMappingDependencies

            # Create enricher with default agent
            enricher = OntologyEnricher()

            # Or with custom agent
            agent = build_ontology_mapping_agent(model="openai:gpt-4o-mini")
            deps = OntologyMappingDependencies.from_env()
            enricher = OntologyEnricher(ontology_agent=(agent, deps))

            # Enrich deepsearch output
            enriched_data, metadata = enricher.enrich_deepsearch_output(validated_data)
    """

    def __init__(self, ontology_agent: tuple[Any, Any] | None = None):
        """Initialize with optional ontology agent.

        Args:
            ontology_agent: Optional tuple of (agent, deps). If None, creates
                default agent from environment configuration.
        """
        if ontology_agent is None:
            from langpa.agents.ontology_mapping import build_ontology_mapping_agent
            from langpa.agents.ontology_mapping.config import (
                OntologyMappingDependencies,
            )

            self.agent = build_ontology_mapping_agent()
            self.deps = OntologyMappingDependencies.from_env()
        else:
            self.agent, self.deps = ontology_agent

    def enrich_deepsearch_output(
        self, validated_data: dict[str, Any]
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """Enrich atomic terms with ontology mappings.

        This method processes validated deepsearch results and adds ontology
        mapping fields to all atomic_biological_processes and atomic_cellular_components.

        Args:
            validated_data: Validated deepsearch results (base schema)

        Returns:
            Tuple of (enriched_data, mapping_metadata) where:
                - enriched_data: Original data with ontology fields added to atomic terms
                - mapping_metadata: Statistics about mapping success/failure

        Example:
            .. code-block:: python

                enriched_data, metadata = enricher.enrich_deepsearch_output(validated_data)

                print(f"Mapped {metadata['mapped_processes']} processes")
                print(f"Mapped {metadata['mapped_components']} components")
                print(f"Failed: {len(metadata['failed_mappings'])}")
        """
        # Deep copy to avoid modifying original
        import copy

        enriched_data = copy.deepcopy(validated_data)

        metadata = {
            "total_processes": 0,
            "total_components": 0,
            "mapped_processes": 0,
            "mapped_components": 0,
            "failed_mappings": [],
        }

        # Process atomic biological processes and cellular components
        if "programs" in enriched_data:
            for program in enriched_data["programs"]:
                if "atomic_biological_processes" in program:
                    self._map_atomic_terms(
                        program["atomic_biological_processes"],
                        term_type="process",
                        metadata=metadata,
                    )

                if "atomic_cellular_components" in program:
                    self._map_atomic_terms(
                        program["atomic_cellular_components"],
                        term_type="component",
                        metadata=metadata,
                    )

        return enriched_data, metadata

    def _map_atomic_terms(
        self,
        atomic_terms: list[dict[str, Any]],
        term_type: str,
        metadata: dict[str, Any],
    ) -> None:
        """Map a list of atomic terms in-place.

        Args:
            atomic_terms: List of atomic term dictionaries to enrich
            term_type: Either "process" or "component"
            metadata: Metadata dictionary to update with statistics
        """
        from langpa.agents.ontology_mapping import map_terms_to_go

        # Extract term names
        term_names = [term["name"] for term in atomic_terms]

        if not term_names:
            return

        # Update metadata counts
        # Handle pluralization: process -> processes, component -> components
        plural_type = f"{term_type}es" if term_type == "process" else f"{term_type}s"
        count_key = f"total_{plural_type}"
        metadata[count_key] += len(term_names)

        # Call ontology mapping agent
        try:
            response = map_terms_to_go(term_names, self.agent, self.deps)

            # Inject mappings back into atomic terms
            for term, mapping in zip(atomic_terms, response.mappings):
                term["ontology_id"] = mapping.ontology_id
                term["ontology_label"] = mapping.ontology_label
                term["ontology_source"] = mapping.ontology_source
                term["confidence"] = mapping.confidence
                term["mapping_method"] = mapping.mapping_method

                # Track success
                if mapping.ontology_id:
                    mapped_key = f"mapped_{plural_type}"
                    metadata[mapped_key] += 1
                else:
                    metadata["failed_mappings"].append(
                        {"term": term["name"], "type": term_type}
                    )

        except Exception as e:
            # On error, set all fields to null
            logger.error(f"Ontology mapping failed for {term_type}s: {e}")
            for term in atomic_terms:
                term["ontology_id"] = None
                term["ontology_label"] = None
                term["ontology_source"] = None
                term["confidence"] = None
                term["mapping_method"] = None
                metadata["failed_mappings"].append(
                    {"term": term["name"], "type": term_type, "error": str(e)}
                )
