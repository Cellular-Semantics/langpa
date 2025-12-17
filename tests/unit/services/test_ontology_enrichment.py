"""Unit tests for ontology enrichment service."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from langpa.agents.ontology_mapping.models import (
    OntologyMapping,
    OntologyMappingResponse,
)


@pytest.mark.unit
class TestOntologyEnricher:
    """Unit tests for OntologyEnricher service."""

    @pytest.fixture
    def sample_deepsearch_data(self):
        """Sample validated deepsearch output."""
        return {
            "context": {
                "cell_type": "neutrophil",
                "disease": "inflammation"
            },
            "input_genes": ["CXCR2", "CXCR4"],
            "programs": [
                {
                    "program_name": "Chemotaxis",
                    "description": "Neutrophil chemotaxis program",
                    "atomic_biological_processes": [
                        {
                            "name": "neutrophil chemotaxis",
                            "citations": [{"source_id": "1"}],
                            "genes": ["CXCR2"]
                        },
                        {
                            "name": "cell migration",
                            "citations": [{"source_id": "2"}],
                            "genes": ["CXCR4"]
                        }
                    ],
                    "atomic_cellular_components": [
                        {
                            "name": "cytosol",
                            "citations": [{"source_id": "3"}],
                            "genes": ["CXCR2", "CXCR4"]
                        }
                    ],
                    "predicted_cellular_impact": ["enhanced migration"],
                    "evidence_summary": "Strong evidence",
                    "significance_score": 0.9,
                    "citations": [{"source_id": "1"}],
                    "supporting_genes": ["CXCR2", "CXCR4"]
                }
            ],
            "version": "1.0"
        }

    @pytest.fixture
    def mock_ontology_agent(self):
        """Mock ontology mapping agent."""
        agent = MagicMock()

        # Mock run_sync to return successful mappings
        mock_result = MagicMock()
        mock_result.output = OntologyMappingResponse(
            mappings=[
                OntologyMapping(
                    term="neutrophil chemotaxis",
                    ontology_id="GO:0030593",
                    ontology_label="neutrophil chemotaxis",
                    ontology_source="GO",
                    confidence=0.95,
                    mapping_method="exact_match"
                ),
                OntologyMapping(
                    term="cell migration",
                    ontology_id="GO:0016477",
                    ontology_label="cell migration",
                    ontology_source="GO",
                    confidence=0.90,
                    mapping_method="exact_match"
                )
            ]
        )
        agent.run_sync.return_value = mock_result

        return agent

    @pytest.fixture
    def mock_deps(self):
        """Mock OntologyMappingDependencies."""
        return MagicMock()

    def test_enrich_atomic_processes(self, sample_deepsearch_data, mock_ontology_agent, mock_deps):
        """Test enrichment of atomic biological processes."""
        from langpa.services.ontology_enrichment import OntologyEnricher

        # Create enricher with mocked agent
        enricher = OntologyEnricher(ontology_agent=(mock_ontology_agent, mock_deps))

        # Enrich the data
        enriched_data, metadata = enricher.enrich_deepsearch_output(sample_deepsearch_data)

        # Check that atomic processes were enriched
        processes = enriched_data["programs"][0]["atomic_biological_processes"]

        assert len(processes) == 2

        # First process should have ontology mapping
        assert processes[0]["name"] == "neutrophil chemotaxis"
        assert processes[0]["ontology_id"] == "GO:0030593"
        assert processes[0]["ontology_label"] == "neutrophil chemotaxis"
        assert processes[0]["ontology_source"] == "GO"
        assert processes[0]["confidence"] == 0.95
        assert processes[0]["mapping_method"] == "exact_match"

        # Second process should have ontology mapping
        assert processes[1]["name"] == "cell migration"
        assert processes[1]["ontology_id"] == "GO:0016477"

    def test_enrich_atomic_components(self, sample_deepsearch_data, mock_ontology_agent, mock_deps):
        """Test enrichment of atomic cellular components."""
        from langpa.services.ontology_enrichment import OntologyEnricher

        # Update mock to return component mappings
        mock_result = MagicMock()
        mock_result.output = OntologyMappingResponse(
            mappings=[
                OntologyMapping(
                    term="cytosol",
                    ontology_id="GO:0005829",
                    ontology_label="cytosol",
                    ontology_source="GO",
                    confidence=0.99,
                    mapping_method="exact_match"
                )
            ]
        )
        mock_ontology_agent.run_sync.return_value = mock_result

        enricher = OntologyEnricher(ontology_agent=(mock_ontology_agent, mock_deps))
        enriched_data, metadata = enricher.enrich_deepsearch_output(sample_deepsearch_data)

        # Check that atomic components were enriched
        components = enriched_data["programs"][0]["atomic_cellular_components"]

        assert len(components) == 1
        assert components[0]["name"] == "cytosol"
        assert components[0]["ontology_id"] == "GO:0005829"
        assert components[0]["ontology_label"] == "cytosol"
        assert components[0]["ontology_source"] == "GO"

    def test_failed_mapping_handling(self, sample_deepsearch_data, mock_ontology_agent, mock_deps):
        """Test that failed mappings result in null values."""
        from langpa.services.ontology_enrichment import OntologyEnricher

        # Mock response with failed mapping for processes (no ontology_id)
        mock_result_processes = MagicMock()
        mock_result_processes.output = OntologyMappingResponse(
            mappings=[
                OntologyMapping(
                    term="neutrophil chemotaxis",
                    ontology_id=None,  # Failed mapping
                    ontology_label=None,
                    ontology_source=None,
                    confidence=None,
                    mapping_method=None
                ),
                OntologyMapping(
                    term="cell migration",
                    ontology_id="GO:0016477",
                    ontology_label="cell migration",
                    ontology_source="GO",
                    confidence=0.90,
                    mapping_method="exact_match"
                )
            ]
        )

        # Mock response with successful mapping for components
        mock_result_components = MagicMock()
        mock_result_components.output = OntologyMappingResponse(
            mappings=[
                OntologyMapping(
                    term="cytosol",
                    ontology_id="GO:0005829",
                    ontology_label="cytosol",
                    ontology_source="GO",
                    confidence=0.99,
                    mapping_method="exact_match"
                )
            ]
        )

        # Configure mock to return different results for different calls
        mock_ontology_agent.run_sync.side_effect = [mock_result_processes, mock_result_components]

        enricher = OntologyEnricher(ontology_agent=(mock_ontology_agent, mock_deps))
        enriched_data, metadata = enricher.enrich_deepsearch_output(sample_deepsearch_data)

        # Check failed mapping has null values
        processes = enriched_data["programs"][0]["atomic_biological_processes"]

        assert processes[0]["name"] == "neutrophil chemotaxis"
        assert processes[0]["ontology_id"] is None
        assert processes[0]["ontology_label"] is None
        assert processes[0]["ontology_source"] is None
        assert processes[0]["confidence"] is None
        assert processes[0]["mapping_method"] is None

        # Check successful mapping still works
        assert processes[1]["ontology_id"] == "GO:0016477"

        # Check metadata tracks failed mappings (only the process, component was successful)
        assert len(metadata["failed_mappings"]) == 1
        assert metadata["failed_mappings"][0]["term"] == "neutrophil chemotaxis"
        assert metadata["failed_mappings"][0]["type"] == "process"

    def test_metadata_tracking(self, sample_deepsearch_data, mock_ontology_agent, mock_deps):
        """Test mapping metadata is correctly tracked."""
        from langpa.services.ontology_enrichment import OntologyEnricher

        # Mock successful mappings for processes
        mock_result_processes = MagicMock()
        mock_result_processes.output = OntologyMappingResponse(
            mappings=[
                OntologyMapping(
                    term="neutrophil chemotaxis",
                    ontology_id="GO:0030593",
                    ontology_label="neutrophil chemotaxis",
                    ontology_source="GO",
                    confidence=0.95,
                    mapping_method="exact_match"
                ),
                OntologyMapping(
                    term="cell migration",
                    ontology_id="GO:0016477",
                    ontology_label="cell migration",
                    ontology_source="GO",
                    confidence=0.90,
                    mapping_method="exact_match"
                )
            ]
        )

        # Mock successful mapping for components
        mock_result_components = MagicMock()
        mock_result_components.output = OntologyMappingResponse(
            mappings=[
                OntologyMapping(
                    term="cytosol",
                    ontology_id="GO:0005829",
                    ontology_label="cytosol",
                    ontology_source="GO",
                    confidence=0.99,
                    mapping_method="exact_match"
                )
            ]
        )

        # Configure mock to return different results for different calls
        mock_ontology_agent.run_sync.side_effect = [mock_result_processes, mock_result_components]

        enricher = OntologyEnricher(ontology_agent=(mock_ontology_agent, mock_deps))
        enriched_data, metadata = enricher.enrich_deepsearch_output(sample_deepsearch_data)

        # Check metadata counts
        assert metadata["total_processes"] == 2
        assert metadata["mapped_processes"] == 2
        assert metadata["total_components"] == 1
        assert metadata["mapped_components"] == 1
        assert len(metadata["failed_mappings"]) == 0

    def test_exception_handling(self, sample_deepsearch_data, mock_ontology_agent, mock_deps):
        """Test that exceptions during mapping result in null values."""
        from langpa.services.ontology_enrichment import OntologyEnricher

        # Mock agent to raise exception
        mock_ontology_agent.run_sync.side_effect = Exception("OLS service unavailable")

        enricher = OntologyEnricher(ontology_agent=(mock_ontology_agent, mock_deps))
        enriched_data, metadata = enricher.enrich_deepsearch_output(sample_deepsearch_data)

        # All mappings should have null values
        processes = enriched_data["programs"][0]["atomic_biological_processes"]
        components = enriched_data["programs"][0]["atomic_cellular_components"]

        for process in processes:
            assert process["ontology_id"] is None
            assert process["ontology_label"] is None
            assert process["ontology_source"] is None
            assert process["confidence"] is None
            assert process["mapping_method"] is None

        for component in components:
            assert component["ontology_id"] is None

        # Check metadata tracks errors
        assert len(metadata["failed_mappings"]) == 3  # 2 processes + 1 component
        assert "error" in metadata["failed_mappings"][0]

    def test_empty_atomic_terms(self):
        """Test handling of programs with no atomic terms."""
        from langpa.services.ontology_enrichment import OntologyEnricher

        data = {
            "context": {"cell_type": "test", "disease": "test"},
            "input_genes": ["GENE1"],
            "programs": [
                {
                    "program_name": "Test",
                    "description": "Test program",
                    "atomic_biological_processes": [],  # Empty
                    "atomic_cellular_components": [],  # Empty
                    "predicted_cellular_impact": ["test"],
                    "evidence_summary": "test",
                    "significance_score": 0.5,
                    "citations": [{"source_id": "1"}],
                    "supporting_genes": ["GENE1"]
                }
            ],
            "version": "1.0"
        }

        enricher = OntologyEnricher(ontology_agent=(MagicMock(), MagicMock()))
        enriched_data, metadata = enricher.enrich_deepsearch_output(data)

        # Should complete without errors
        assert metadata["total_processes"] == 0
        assert metadata["total_components"] == 0
        assert metadata["mapped_processes"] == 0
        assert metadata["mapped_components"] == 0

    def test_original_data_preserved(self, sample_deepsearch_data, mock_ontology_agent, mock_deps):
        """Test that original fields in atomic terms are preserved."""
        from langpa.services.ontology_enrichment import OntologyEnricher

        enricher = OntologyEnricher(ontology_agent=(mock_ontology_agent, mock_deps))
        enriched_data, metadata = enricher.enrich_deepsearch_output(sample_deepsearch_data)

        # Check that original fields are still present
        processes = enriched_data["programs"][0]["atomic_biological_processes"]

        assert processes[0]["name"] == "neutrophil chemotaxis"
        assert processes[0]["citations"] == [{"source_id": "1"}]
        assert processes[0]["genes"] == ["CXCR2"]

        # And new fields are added
        assert "ontology_id" in processes[0]
        assert "ontology_label" in processes[0]
