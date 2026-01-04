"""Unit tests for MarkdownReportGenerator with GO term rendering."""

import pytest

from langpa.services.markdown_reporter import MarkdownReportGenerator


@pytest.fixture
def reporter():
    """Create a markdown reporter instance."""
    return MarkdownReportGenerator(strict_citations=False)


@pytest.fixture
def minimal_container():
    """Minimal container with structured data and bibliography."""
    return {
        "structured_data": {
            "context": {
                "cell_type": "T cell",
                "disease": "None",
                "tissue": "Blood",
            },
            "input_genes": ["GENE1", "GENE2"],
            "programs": [],
        },
        "citations": {},
    }


def test_render_atomic_terms_with_go_mappings(reporter, minimal_container):
    """Test that GO mappings are correctly rendered."""
    # Add program with GO-mapped atomic terms
    minimal_container["structured_data"]["programs"] = [
        {
            "program_name": "Test Program",
            "atomic_biological_processes": [
                {
                    "name": "neutrophil chemotaxis",
                    "genes": ["CXCR2", "IL8"],
                    "ontology_id": "GO:0030593",
                    "ontology_label": "neutrophil chemotaxis",
                    "ontology_source": "GO",
                    "confidence": 0.95,
                    "mapping_method": "exact_match",
                    "citations": [],
                }
            ],
        }
    ]

    result = reporter.render_from_container(minimal_container)

    # Check that term name and genes are present
    assert "neutrophil chemotaxis" in result
    assert "Genes: CXCR2, IL8" in result

    # Check that GO mapping is present with all details
    assert "GO: GO:0030593 (neutrophil chemotaxis)" in result
    assert "confidence: 0.95" in result
    assert "method: exact_match" in result


def test_render_atomic_terms_unmapped(reporter, minimal_container):
    """Test that unmapped terms show explicit indicator."""
    # Add program with unmapped atomic term
    minimal_container["structured_data"]["programs"] = [
        {
            "program_name": "Test Program",
            "atomic_biological_processes": [
                {
                    "name": "cell migration",
                    "genes": ["CXCR4"],
                    "citations": [],
                }
            ],
        }
    ]

    result = reporter.render_from_container(minimal_container)

    # Check that term name and genes are present
    assert "cell migration" in result
    assert "Genes: CXCR4" in result

    # Check that unmapped indicator is present
    assert "GO: unmapped" in result


def test_render_atomic_terms_backwards_compatible(reporter, minimal_container):
    """Test that rendering works without ontology fields (backwards compatibility)."""
    # Add program with old-style atomic term (no ontology fields)
    minimal_container["structured_data"]["programs"] = [
        {
            "program_name": "Test Program",
            "atomic_biological_processes": [
                {
                    "name": "some process",
                    "genes": ["GENE1"],
                    "citations": [],
                }
            ],
        }
    ]

    # Should not raise an error
    result = reporter.render_from_container(minimal_container)

    # Check that term is rendered
    assert "some process" in result
    assert "GO: unmapped" in result


def test_confidence_formatting(reporter, minimal_container):
    """Test that confidence is formatted to 2 decimal places."""
    # Add program with various confidence values
    minimal_container["structured_data"]["programs"] = [
        {
            "program_name": "Test Program",
            "atomic_biological_processes": [
                {
                    "name": "process1",
                    "genes": [],
                    "ontology_id": "GO:0000001",
                    "ontology_label": "process1",
                    "confidence": 1.0,
                    "mapping_method": "exact_match",
                    "citations": [],
                },
                {
                    "name": "process2",
                    "genes": [],
                    "ontology_id": "GO:0000002",
                    "ontology_label": "process2",
                    "confidence": 0.857,
                    "mapping_method": "partial_match",
                    "citations": [],
                },
            ],
        }
    ]

    result = reporter.render_from_container(minimal_container)

    # Check confidence formatting
    assert "confidence: 1.00" in result
    assert "confidence: 0.86" in result  # Should round 0.857 to 0.86


def test_method_display(reporter, minimal_container):
    """Test that all mapping methods are rendered correctly."""
    methods = ["exact_match", "partial_match", "synonym_match"]

    for i, method in enumerate(methods):
        minimal_container["structured_data"]["programs"] = [
            {
                "program_name": "Test Program",
                "atomic_biological_processes": [
                    {
                        "name": f"process{i}",
                        "genes": [],
                        "ontology_id": f"GO:000000{i}",
                        "ontology_label": f"process{i}",
                        "confidence": 0.9,
                        "mapping_method": method,
                        "citations": [],
                    }
                ],
            }
        ]

        result = reporter.render_from_container(minimal_container)
        assert f"method: {method}" in result


def test_cellular_components_with_go(reporter, minimal_container):
    """Test that cellular components also display GO mappings."""
    # Add program with GO-mapped cellular component
    minimal_container["structured_data"]["programs"] = [
        {
            "program_name": "Test Program",
            "atomic_cellular_components": [
                {
                    "name": "nucleus",
                    "genes": ["GENE1"],
                    "ontology_id": "GO:0005634",
                    "ontology_label": "nucleus",
                    "ontology_source": "GO",
                    "confidence": 1.0,
                    "mapping_method": "exact_match",
                    "citations": [],
                }
            ],
        }
    ]

    result = reporter.render_from_container(minimal_container)

    # Check that GO mapping is present for cellular component
    assert "nucleus" in result
    assert "GO: GO:0005634 (nucleus)" in result
    assert "confidence: 1.00" in result


def test_citations_after_go_line(reporter, minimal_container):
    """Test that citations are rendered correctly after GO line."""
    # Add bibliography
    minimal_container["citations"] = {
        "1": {"id": "1", "title": "Test Paper", "URL": "http://example.com"}
    }

    # Add program with GO-mapped term and citation
    minimal_container["structured_data"]["programs"] = [
        {
            "program_name": "Test Program",
            "atomic_biological_processes": [
                {
                    "name": "test process",
                    "genes": ["GENE1"],
                    "ontology_id": "GO:0000001",
                    "ontology_label": "test process",
                    "confidence": 0.9,
                    "mapping_method": "exact_match",
                    "citations": [{"source_id": "1", "notes": "Supporting evidence"}],
                }
            ],
        }
    ]

    result = reporter.render_from_container(minimal_container)

    # Check GO line comes before citation
    go_pos = result.find("GO: GO:0000001")
    citation_pos = result.find("[1]")

    assert go_pos > 0
    assert citation_pos > 0
    assert go_pos < citation_pos  # GO line should come before citation


def test_multiple_terms_mixed_mapping(reporter, minimal_container):
    """Test rendering multiple terms with mix of mapped and unmapped."""
    minimal_container["structured_data"]["programs"] = [
        {
            "program_name": "Test Program",
            "atomic_biological_processes": [
                {
                    "name": "mapped process",
                    "genes": ["GENE1"],
                    "ontology_id": "GO:0000001",
                    "ontology_label": "mapped process",
                    "confidence": 0.95,
                    "mapping_method": "exact_match",
                    "citations": [],
                },
                {
                    "name": "unmapped process",
                    "genes": ["GENE2"],
                    "citations": [],
                },
            ],
        }
    ]

    result = reporter.render_from_container(minimal_container)

    # Check both terms rendered correctly
    assert "mapped process" in result
    assert "GO: GO:0000001 (mapped process)" in result
    assert "confidence: 0.95" in result

    assert "unmapped process" in result
    assert "GO: unmapped" in result
