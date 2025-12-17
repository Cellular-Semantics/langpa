"""Integration tests for ontology mapping agent.

These tests require real API keys (OPENAI_API_KEY or ANTHROPIC_API_KEY)
and will make actual calls to LLM providers and OLS.
"""

import pytest


@pytest.mark.integration
class TestOntologyMappingIntegration:
    """Test end-to-end ontology mapping with real APIs."""

    def test_build_agent(self):
        """Test that agent can be built successfully."""
        from langpa.agents.ontology_mapping.agent import build_ontology_mapping_agent

        agent = build_ontology_mapping_agent()

        assert agent is not None
        # Agent model is an object, not string - just check it exists
        assert agent.model is not None

    def test_map_biological_processes_to_go(self):
        """Test mapping biological process terms to GO with real API."""
        from langpa.agents.ontology_mapping.agent import (
            build_ontology_mapping_agent,
            map_terms_to_go
        )
        from langpa.agents.ontology_mapping.config import OntologyMappingDependencies

        # Setup
        agent = build_ontology_mapping_agent()
        deps = OntologyMappingDependencies.from_env()

        # Test data - biological processes
        terms = [
            "neutrophil chemotaxis",
            "cell migration"
        ]

        # Execute
        response = map_terms_to_go(terms, agent, deps)

        # Assertions
        assert len(response.mappings) == 2

        # Check all mappings have required fields
        for mapping in response.mappings:
            assert mapping.term in terms
            assert mapping.ontology_source in ["GO", None]

            # If mapping was successful, check GO ID format
            if mapping.ontology_id:
                assert mapping.ontology_id.startswith("GO:")
                assert mapping.ontology_label is not None

            # If confidence is provided, check range
            if mapping.confidence is not None:
                assert 0.0 <= mapping.confidence <= 1.0

    def test_map_cellular_components_to_go(self):
        """Test mapping cellular component terms to GO."""
        from langpa.agents.ontology_mapping.agent import (
            build_ontology_mapping_agent,
            map_terms_to_go
        )
        from langpa.agents.ontology_mapping.config import OntologyMappingDependencies

        agent = build_ontology_mapping_agent()
        deps = OntologyMappingDependencies.from_env()

        terms = [
            "cytosol",
            "plasma membrane"
        ]

        response = map_terms_to_go(terms, agent, deps)

        assert len(response.mappings) == 2

        # At least one should map successfully
        successful_mappings = [m for m in response.mappings if m.ontology_id]
        assert len(successful_mappings) > 0

    def test_map_with_no_matches(self):
        """Test mapping handles terms with no good matches."""
        from langpa.agents.ontology_mapping.agent import (
            build_ontology_mapping_agent,
            map_terms_to_go
        )
        from langpa.agents.ontology_mapping.config import OntologyMappingDependencies

        agent = build_ontology_mapping_agent()
        deps = OntologyMappingDependencies.from_env()

        terms = [
            "completely made up biological term xyz123"
        ]

        response = map_terms_to_go(terms, agent, deps)

        assert len(response.mappings) == 1
        # Should return the term but may not have a mapping
        assert response.mappings[0].term == terms[0]

    def test_agent_with_custom_model(self):
        """Test agent can be built with custom model."""
        from langpa.agents.ontology_mapping.agent import build_ontology_mapping_agent

        agent = build_ontology_mapping_agent(model="openai:gpt-4o-mini")

        # Agent built successfully with custom model
        assert agent.model is not None
