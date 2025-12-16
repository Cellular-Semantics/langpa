"""Unit tests for ontology mapping agent models and configuration."""

import pytest
from pydantic import ValidationError


@pytest.mark.unit
class TestOntologyMappingModels:
    """Test data model validation."""

    def test_ontology_mapping_basic(self):
        """Test basic OntologyMapping creation."""
        from langpa.agents.ontology_mapping.models import OntologyMapping

        mapping = OntologyMapping(
            term="neutrophil chemotaxis",
            ontology_id="GO:0030593",
            ontology_label="neutrophil chemotaxis",
            ontology_source="GO",
            confidence=1.0,
            mapping_method="exact_match"
        )

        assert mapping.term == "neutrophil chemotaxis"
        assert mapping.ontology_id == "GO:0030593"
        assert mapping.ontology_label == "neutrophil chemotaxis"
        assert mapping.ontology_source == "GO"
        assert mapping.confidence == 1.0
        assert mapping.mapping_method == "exact_match"

    def test_ontology_mapping_optional_fields(self):
        """Test OntologyMapping with optional fields as None."""
        from langpa.agents.ontology_mapping.models import OntologyMapping

        mapping = OntologyMapping(term="unknown term")

        assert mapping.term == "unknown term"
        assert mapping.ontology_id is None
        assert mapping.ontology_label is None
        assert mapping.ontology_source is None
        assert mapping.confidence is None
        assert mapping.mapping_method is None

    def test_ontology_mapping_response_empty(self):
        """Test OntologyMappingResponse with empty mappings."""
        from langpa.agents.ontology_mapping.models import OntologyMappingResponse

        response = OntologyMappingResponse(mappings=[])

        assert response.mappings == []
        assert response.metadata == {}

    def test_ontology_mapping_response_with_mappings(self):
        """Test OntologyMappingResponse with multiple mappings."""
        from langpa.agents.ontology_mapping.models import (
            OntologyMapping,
            OntologyMappingResponse
        )

        mappings = [
            OntologyMapping(
                term="neutrophil chemotaxis",
                ontology_id="GO:0030593",
                ontology_source="GO",
                confidence=1.0
            ),
            OntologyMapping(
                term="cell migration",
                ontology_id="GO:0016477",
                ontology_source="GO",
                confidence=0.95
            )
        ]

        response = OntologyMappingResponse(mappings=mappings)

        assert len(response.mappings) == 2
        assert response.mappings[0].term == "neutrophil chemotaxis"
        assert response.mappings[1].term == "cell migration"

    def test_ontology_mapping_response_with_metadata(self):
        """Test OntologyMappingResponse with custom metadata."""
        from langpa.agents.ontology_mapping.models import OntologyMappingResponse

        metadata = {
            "timestamp": "2024-01-01T00:00:00",
            "model": "gpt-4o",
            "total_terms": 5
        }

        response = OntologyMappingResponse(mappings=[], metadata=metadata)

        assert response.metadata == metadata
        assert response.metadata["model"] == "gpt-4o"

    def test_ontology_mapping_confidence_range(self):
        """Test that confidence scores are in valid range."""
        from langpa.agents.ontology_mapping.models import OntologyMapping

        # Valid confidence scores
        mapping1 = OntologyMapping(term="test", confidence=0.0)
        assert mapping1.confidence == 0.0

        mapping2 = OntologyMapping(term="test", confidence=1.0)
        assert mapping2.confidence == 1.0

        mapping3 = OntologyMapping(term="test", confidence=0.5)
        assert mapping3.confidence == 0.5
