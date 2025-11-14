"""Unit tests for DeepSearch service."""

from __future__ import annotations

import sys
from unittest.mock import MagicMock, Mock, patch

import pytest


# Mock ResearchResult for testing
class MockResearchResult:
    def __init__(self, content: str, citations: list = None):
        self.content = content
        self.citations = citations or []


# Mock the deep_research_client module at import time
mock_deep_research_client = MagicMock()
mock_deep_research_client.DeepResearchClient = Mock
sys.modules["deep_research_client"] = mock_deep_research_client


@pytest.mark.unit
def test_deepsearch_service_import() -> None:
    """Test that we can import the DeepSearch service."""
    try:
        from langpa.services.deepsearch_service import DeepSearchService

        assert DeepSearchService is not None
    except ImportError as e:
        pytest.fail(f"DeepSearchService should be importable: {e}")


@pytest.mark.unit
def test_deepsearch_service_initialization() -> None:
    """Test DeepSearch service can be initialized."""
    from langpa.services.deepsearch_service import DeepSearchService

    service = DeepSearchService()
    assert service is not None
    assert hasattr(service, "research_gene_list"), "Service should have research_gene_list method"


@pytest.mark.unit
@patch("langpa.services.deepsearch_service.DeepResearchClient")
def test_deepsearch_service_interface(mock_client_class: Mock) -> None:
    """Test DeepSearch service interface and method signatures."""
    from langpa.services.deepsearch_service import DeepSearchService

    # Mock the client instance
    mock_client = Mock()
    mock_client.get_available_providers.return_value = ["perplexity", "openai"]
    mock_client.research.return_value = MockResearchResult(
        content="Test research content about TP53 gene function",
        citations=[{"url": "https://example.com/paper1", "title": "Test paper"}],
    )
    mock_client_class.return_value = mock_client

    service = DeepSearchService()

    # Test the main research method interface
    genes = ["TP53", "BRCA1"]
    context = "tumor suppressor genes in cancer"

    result = service.research_gene_list(genes=genes, context=context)

    # Verify result structure
    assert result is not None
    assert hasattr(result, "content"), "Result should have content"
    assert hasattr(result, "citations"), "Result should have citations"
    assert isinstance(result.content, str), "Content should be string"
    assert len(result.content) > 0, "Content should not be empty"


@pytest.mark.unit
@patch("langpa.services.deepsearch_service.DeepResearchClient")
def test_deepsearch_service_prompt_construction(mock_client_class: Mock) -> None:
    """Test that service constructs proper prompts for gene research."""
    from langpa.services.deepsearch_service import DeepSearchService

    mock_client = Mock()
    mock_client.get_available_providers.return_value = ["perplexity", "openai"]
    mock_client.research.return_value = MockResearchResult(content="Research content")
    mock_client_class.return_value = mock_client

    service = DeepSearchService()

    genes = ["EGFR", "KRAS"]
    context = "oncogenes in lung cancer"

    service.research_gene_list(genes=genes, context=context)

    # Verify the client was called with proper query
    mock_client.research.assert_called_once()
    call_args = mock_client.research.call_args

    query = call_args[1]["query"] if "query" in call_args[1] else call_args[0][0]

    # Query should contain all genes
    for gene in genes:
        assert gene in query, f"Query should contain gene {gene}"

    # Query should contain context
    assert context in query, "Query should contain biological context"

    # Query should request structured analysis
    assert any(
        keyword in query.lower()
        for keyword in ["analyze", "function", "program", "pathway", "biological"]
    ), "Query should request biological analysis"


@pytest.mark.unit
@patch("langpa.services.deepsearch_service.DeepResearchClient")
def test_deepsearch_service_error_handling(mock_client_class: Mock) -> None:
    """Test DeepSearch service handles API errors gracefully."""
    from langpa.services.deepsearch_service import DeepSearchService

    mock_client = Mock()
    mock_client.get_available_providers.return_value = ["perplexity"]
    mock_client.research.side_effect = Exception("API Error: Rate limit exceeded")
    mock_client_class.return_value = mock_client

    service = DeepSearchService()

    genes = ["TP53"]
    context = "cancer"

    # Should handle API errors gracefully
    with pytest.raises(Exception) as exc_info:
        service.research_gene_list(genes=genes, context=context)

    # Should re-raise with context or handle gracefully
    assert "DeepSearch API error" in str(exc_info.value)


@pytest.mark.unit
@patch("langpa.services.deepsearch_service.DeepResearchClient")
def test_deepsearch_service_empty_input_validation(mock_client_class: Mock) -> None:
    """Test service validates input parameters."""
    from langpa.services.deepsearch_service import DeepSearchService

    service = DeepSearchService()

    # Test empty gene list
    with pytest.raises(ValueError) as exc_info:
        service.research_gene_list(genes=[], context="cancer")

    assert "genes" in str(exc_info.value).lower()

    # Test empty context
    with pytest.raises(ValueError) as exc_info:
        service.research_gene_list(genes=["TP53"], context="")

    assert "context" in str(exc_info.value).lower()


@pytest.mark.unit
@patch("langpa.services.deepsearch_service.DeepResearchClient")
def test_deepsearch_service_provider_configuration(mock_client_class: Mock) -> None:
    """Test service can be configured with different providers."""
    from langpa.services.deepsearch_service import DeepSearchService

    mock_client = Mock()
    mock_client.get_available_providers.return_value = ["perplexity", "openai"]
    mock_client.research.return_value = MockResearchResult(content="test content")
    mock_client_class.return_value = mock_client

    # Test default provider selection
    service = DeepSearchService()
    service.research_gene_list(genes=["TP53"], context="cancer")

    # Should call research with appropriate provider
    call_args = mock_client.research.call_args[1]
    assert "provider" in call_args, "Should specify provider"

    # Test explicit provider specification
    service = DeepSearchService(preferred_provider="openai")
    service.research_gene_list(genes=["TP53"], context="cancer")

    call_args = mock_client.research.call_args[1]
    assert call_args["provider"] == "openai", "Should use specified provider"
