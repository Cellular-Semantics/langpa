"""Integration tests for ontology enrichment service.

These tests require real API keys (OPENAI_API_KEY or ANTHROPIC_API_KEY)
and will make actual calls to LLM providers and OLS.
"""

from __future__ import annotations

import pytest


@pytest.mark.integration
class TestOntologyEnrichmentIntegration:
    """Test end-to-end ontology enrichment with real APIs."""

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

    def test_end_to_end_enrichment(self, sample_deepsearch_data):
        """Test full enrichment with real ontology agent."""
        from langpa.services.ontology_enrichment import OntologyEnricher

        # Create enricher with real agent
        enricher = OntologyEnricher()

        # Run enrichment
        enriched_data, metadata = enricher.enrich_deepsearch_output(sample_deepsearch_data)

        # Check that enrichment completed
        assert enriched_data is not None
        assert metadata is not None

        # Check metadata counts
        assert metadata["total_processes"] == 2
        assert metadata["total_components"] == 1

        # At least some mappings should succeed
        total_mapped = metadata["mapped_processes"] + metadata["mapped_components"]
        assert total_mapped > 0

        # Check that ontology fields were added to atomic terms
        processes = enriched_data["programs"][0]["atomic_biological_processes"]
        components = enriched_data["programs"][0]["atomic_cellular_components"]

        # All terms should have ontology fields (even if null)
        for process in processes:
            assert "ontology_id" in process
            assert "ontology_label" in process
            assert "ontology_source" in process
            assert "confidence" in process
            assert "mapping_method" in process

            # Original fields should be preserved
            assert "name" in process
            assert "citations" in process
            assert "genes" in process

        for component in components:
            assert "ontology_id" in component
            assert "ontology_label" in component

    def test_enrichment_with_biological_processes(self):
        """Test enrichment of biological process terms."""
        from langpa.services.ontology_enrichment import OntologyEnricher

        data = {
            "context": {"cell_type": "test", "disease": "test"},
            "input_genes": ["GENE1"],
            "programs": [
                {
                    "program_name": "Test",
                    "description": "Test program",
                    "atomic_biological_processes": [
                        {
                            "name": "apoptosis",
                            "citations": [{"source_id": "1"}],
                            "genes": ["GENE1"]
                        }
                    ],
                    "predicted_cellular_impact": ["test"],
                    "evidence_summary": "test",
                    "significance_score": 0.5,
                    "citations": [{"source_id": "1"}],
                    "supporting_genes": ["GENE1"]
                }
            ],
            "version": "1.0"
        }

        enricher = OntologyEnricher()
        enriched_data, metadata = enricher.enrich_deepsearch_output(data)

        # Check that apoptosis was mapped (it's a common GO term)
        processes = enriched_data["programs"][0]["atomic_biological_processes"]
        assert len(processes) == 1

        # Should have some mapping (apoptosis is GO:0006915)
        if processes[0]["ontology_id"]:
            assert processes[0]["ontology_id"].startswith("GO:")
            assert processes[0]["ontology_source"] == "GO"
            assert processes[0]["confidence"] is not None
            assert 0.0 <= processes[0]["confidence"] <= 1.0

    def test_enrichment_with_cellular_components(self):
        """Test enrichment of cellular component terms."""
        from langpa.services.ontology_enrichment import OntologyEnricher

        data = {
            "context": {"cell_type": "test", "disease": "test"},
            "input_genes": ["GENE1"],
            "programs": [
                {
                    "program_name": "Test",
                    "description": "Test program",
                    "atomic_cellular_components": [
                        {
                            "name": "nucleus",
                            "citations": [{"source_id": "1"}],
                            "genes": ["GENE1"]
                        }
                    ],
                    "predicted_cellular_impact": ["test"],
                    "evidence_summary": "test",
                    "significance_score": 0.5,
                    "citations": [{"source_id": "1"}],
                    "supporting_genes": ["GENE1"]
                }
            ],
            "version": "1.0"
        }

        enricher = OntologyEnricher()
        enriched_data, metadata = enricher.enrich_deepsearch_output(data)

        # Check that nucleus was mapped (it's a common GO term)
        components = enriched_data["programs"][0]["atomic_cellular_components"]
        assert len(components) == 1

        # Should have mapping (nucleus is GO:0005634)
        if components[0]["ontology_id"]:
            assert components[0]["ontology_id"].startswith("GO:")
            assert components[0]["ontology_source"] == "GO"

    def test_enriched_schema_validation(self, sample_deepsearch_data):
        """Test that enriched data has all required ontology fields."""
        from langpa.services.ontology_enrichment import OntologyEnricher

        # Enrich the data
        enricher = OntologyEnricher()
        enriched_data, metadata = enricher.enrich_deepsearch_output(sample_deepsearch_data)

        # Verify all atomic terms have the required ontology fields
        for program in enriched_data["programs"]:
            for process in program.get("atomic_biological_processes", []):
                # Check all ontology fields are present
                assert "ontology_id" in process
                assert "ontology_label" in process
                assert "ontology_source" in process
                assert "confidence" in process
                assert "mapping_method" in process

            for component in program.get("atomic_cellular_components", []):
                # Check all ontology fields are present
                assert "ontology_id" in component
                assert "ontology_label" in component
                assert "ontology_source" in component
                assert "confidence" in component
                assert "mapping_method" in component

    def test_multiple_programs_enrichment(self):
        """Test enrichment with multiple programs."""
        from langpa.services.ontology_enrichment import OntologyEnricher

        data = {
            "context": {"cell_type": "test", "disease": "test"},
            "input_genes": ["GENE1", "GENE2"],
            "programs": [
                {
                    "program_name": "Program1",
                    "description": "First program",
                    "atomic_biological_processes": [
                        {
                            "name": "apoptosis",
                            "citations": [{"source_id": "1"}],
                            "genes": ["GENE1"]
                        }
                    ],
                    "predicted_cellular_impact": ["test"],
                    "evidence_summary": "test",
                    "significance_score": 0.5,
                    "citations": [{"source_id": "1"}],
                    "supporting_genes": ["GENE1"]
                },
                {
                    "program_name": "Program2",
                    "description": "Second program",
                    "atomic_biological_processes": [
                        {
                            "name": "cell division",
                            "citations": [{"source_id": "2"}],
                            "genes": ["GENE2"]
                        }
                    ],
                    "predicted_cellular_impact": ["test"],
                    "evidence_summary": "test",
                    "significance_score": 0.6,
                    "citations": [{"source_id": "2"}],
                    "supporting_genes": ["GENE2"]
                }
            ],
            "version": "1.0"
        }

        enricher = OntologyEnricher()
        enriched_data, metadata = enricher.enrich_deepsearch_output(data)

        # Both programs should be enriched
        assert metadata["total_processes"] == 2

        # Check both programs have ontology fields
        for program in enriched_data["programs"]:
            for process in program.get("atomic_biological_processes", []):
                assert "ontology_id" in process
                assert "ontology_label" in process
                assert "ontology_source" in process
