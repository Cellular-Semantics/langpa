"""Integration tests for DeepSearch API connectivity and response format."""

from __future__ import annotations

import os

import pytest
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


@pytest.mark.integration
def test_deepsearch_api_keys_present() -> None:
    """Ensure developers have API keys configured for DeepSearch integration."""
    # Check for Perplexity API key (primary) and OpenAI as backup
    perplexity_key = os.getenv("PERPLEXITY_API_KEY") or os.getenv("PERPLEXITY-API-KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    assert perplexity_key or openai_key, (
        "Missing API keys: need either PERPLEXITY_API_KEY or OPENAI_API_KEY for DeepSearch integration"
    )


@pytest.mark.integration
def test_deepsearch_client_import() -> None:
    """Verify we can import the DeepSearch client dependency."""
    try:
        from deep_research_client import DeepResearchClient  # type: ignore
    except ImportError as e:
        pytest.fail(f"Cannot import DeepResearchClient: {e}")


@pytest.mark.integration
def test_deepsearch_basic_connectivity() -> None:
    """Test basic connectivity to DeepSearch API with simple query."""
    from deep_research_client import DeepResearchClient  # type: ignore

    client = DeepResearchClient()

    # Verify providers are available
    providers = client.get_available_providers()
    assert len(providers) > 0, "No research providers available"

    # Use perplexity if available, otherwise use first available provider
    provider = "perplexity" if "perplexity" in providers else providers[0]

    # Simple test query with minimal gene list
    test_genes = ["TP53"]  # Reduced to one gene for faster testing
    test_context = "cancer"

    # This should return a ResearchResult object
    response = client.research(
        query=f"What is the {test_genes[0]} gene role in {test_context}?", provider=provider
    )

    assert response is not None
    # Check if response has expected attributes (ResearchResult object)
    assert hasattr(response, "content"), "Response should have content attribute"
    assert isinstance(response.content, str), "Response content should be string"
    assert len(response.content) > 0, "Response content should not be empty"


@pytest.mark.integration
def test_deepsearch_response_format() -> None:
    """Test that DeepSearch returns expected markdown format with citations."""
    from deep_research_client import DeepResearchClient  # type: ignore

    client = DeepResearchClient()
    providers = client.get_available_providers()
    provider = "perplexity" if "perplexity" in providers else providers[0]

    # Test with a simple gene that should have good literature coverage
    response = client.research(query="What is the TP53 gene function in cancer?", provider=provider)

    # Verify response structure
    content = response.content
    assert isinstance(content, str), "Response content should be string"
    assert len(content) > 100, "Response should be substantial"

    # Check if response has citations (ResearchResult should have citations)
    if hasattr(response, "citations"):
        assert response.citations is not None, "Response should have citations"
        assert len(response.citations) > 0, "Should have at least some citations"

    # Look for common patterns that indicate research content
    content_lower = content.lower()
    research_indicators = ["gene", "protein", "function", "cancer", "tumor", "suppressor"]
    found_indicators = sum(1 for indicator in research_indicators if indicator in content_lower)
    assert found_indicators >= 2, (
        f"Response should contain research content about genes. Found: {found_indicators}"
    )


@pytest.mark.integration
def test_deepsearch_error_handling() -> None:
    """Test DeepSearch API error handling with invalid input."""
    from deep_research_client import DeepResearchClient  # type: ignore

    client = DeepResearchClient()
    providers = client.get_available_providers()
    provider = "perplexity" if "perplexity" in providers else providers[0]

    # Test with empty query - should handle gracefully
    try:
        response = client.research(query="", provider=provider)
        # If it doesn't raise an error, check if response indicates the issue
        if response and response.content:
            content = response.content.lower()
            # Some APIs might return content explaining the issue
            assert len(content) == 0 or any(
                term in content for term in ["error", "invalid", "empty"]
            )
    except Exception as e:
        # API client should raise appropriate exceptions for invalid input
        error_msg = str(e).lower()
        assert any(term in error_msg for term in ["query", "empty", "invalid", "required"])
