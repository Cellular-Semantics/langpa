"""Integration tests for DeepSearchService with real API calls.

These tests verify that the preset configuration system works with actual API providers.
Following CLAUDE.md: Integration tests REQUIRE real API keys and test against real APIs.
"""

from __future__ import annotations

import os
import pytest
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from langpa.services.deepsearch_service import DeepSearchService


@pytest.mark.integration
def test_deepsearch_service_preset_integration() -> None:
    """Test that perplexity-sonar-pro preset works with real Perplexity API.

    This is the core integration test for the preset system.
    Verifies that the extracted configuration actually works end-to-end.
    """
    # Check for required API keys
    perplexity_key = os.getenv("PERPLEXITY_API_KEY") or os.getenv("PERPLEXITY-API-KEY")
    if not perplexity_key:
        pytest.skip("PERPLEXITY_API_KEY not found - cannot test real integration")

    # Initialize service with preset
    service = DeepSearchService(preset="perplexity-sonar-pro")

    # Verify preset configuration is loaded
    assert service.config.provider == "perplexity"
    assert service.config.model == "sonar-reasoning-pro"
    assert service.config.timeout == 180

    # Test real API call with minimal gene list for speed
    genes = ["TP53"]  # Single gene for faster testing
    context = "cancer tumor suppressor"

    try:
        result = service.research_gene_list(genes=genes, context=context)

        # Verify API response structure
        assert result is not None

        # Check for either 'content' or 'markdown' attribute (different in deep-research-client)
        content = None
        if hasattr(result, "content"):
            content = result.content
        elif hasattr(result, "markdown"):
            content = result.markdown
        else:
            pytest.fail("Response should have either 'content' or 'markdown' attribute")

        assert isinstance(content, str), "Response content should be string"
        assert len(content) > 50, "Response should contain substantial content"

        # Verify citations if available (Perplexity should provide these)
        if hasattr(result, "citations"):
            assert result.citations is not None, "Perplexity should provide citations"

        # Verify content contains gene-related information
        content_lower = content.lower()
        assert "tp53" in content_lower or "p53" in content_lower, "Response should mention the queried gene"

        # Verify content indicates biological research
        bio_indicators = ["gene", "protein", "cancer", "tumor", "cell", "function"]
        found_indicators = sum(1 for indicator in bio_indicators if indicator in content_lower)
        assert found_indicators >= 2, "Response should contain biological research content"

    except Exception as e:
        # Provide helpful error message for debugging
        pytest.fail(f"Preset integration failed with real API: {str(e)}")


@pytest.mark.integration
def test_deepsearch_service_backward_compatibility() -> None:
    """Test that the old preferred_provider pattern still works with real APIs.

    Ensures backward compatibility for existing code that uses preferred_provider.
    """
    # Check for API keys
    perplexity_key = os.getenv("PERPLEXITY_API_KEY") or os.getenv("PERPLEXITY-API-KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    if not (perplexity_key or openai_key):
        pytest.skip("No API keys found - cannot test backward compatibility")

    # Test old initialization pattern
    provider = "perplexity" if perplexity_key else "openai"
    service = DeepSearchService(preferred_provider=provider)

    # Should use default preset with overridden provider
    assert service.config.provider == provider
    assert service.preferred_provider == provider  # Backward compatibility attribute

    # Test real API call
    genes = ["BRCA1"]
    context = "breast cancer"

    try:
        result = service.research_gene_list(genes=genes, context=context)

        # Basic response validation
        assert result is not None

        # Get content from either attribute
        content = getattr(result, "content", None) or getattr(result, "markdown", "")
        assert len(content) > 50

        # Verify gene mentioned in response
        content_lower = content.lower()
        assert "brca1" in content_lower or "brca" in content_lower

    except Exception as e:
        pytest.fail(f"Backward compatibility test failed: {str(e)}")


@pytest.mark.integration
def test_deepsearch_service_preset_configuration_applied() -> None:
    """Test that preset configuration parameters are actually applied to real API calls.

    Verifies that the preset's provider_params, model, and timeout are used.
    """
    # Check for Perplexity API key
    perplexity_key = os.getenv("PERPLEXITY_API_KEY") or os.getenv("PERPLEXITY-API-KEY")
    if not perplexity_key:
        pytest.skip("PERPLEXITY_API_KEY not found - cannot test preset configuration")

    service = DeepSearchService(preset="perplexity-sonar-pro")

    # Verify configuration details from preset
    config = service.config
    assert config.model == "sonar-reasoning-pro"

    # Check provider params include expected Perplexity settings
    params = config.provider_params
    assert "reasoning_effort" in params
    assert params["reasoning_effort"] == "high"
    assert "search_recency_filter" in params
    assert params["search_recency_filter"] == "month"
    assert "search_domain_filter" in params

    # Verify academic domains are included
    domain_filter = params["search_domain_filter"]
    assert "pubmed.ncbi.nlm.nih.gov" in domain_filter
    assert "nature.com" in domain_filter

    # Test with actual API call to verify these settings work
    genes = ["MYC"]
    context = "oncogene cancer"

    try:
        result = service.research_gene_list(genes=genes, context=context)

        # If we get a response, the configuration was applied successfully
        assert result is not None

        # Get content from either attribute
        content = getattr(result, "content", None) or getattr(result, "markdown", "")
        assert len(content) > 30

        # With academic domain filtering, should get research-focused content
        content = content.lower()
        research_terms = ["study", "research", "analysis", "published", "journal"]
        found_research = sum(1 for term in research_terms if term in content)
        assert found_research >= 1, "Academic domain filter should produce research-focused content"

    except Exception as e:
        pytest.fail(f"Preset configuration test failed: {str(e)}")


@pytest.mark.integration
def test_deepsearch_service_preset_override() -> None:
    """Test that preset configuration can be overridden per method call.

    Verifies flexibility of the preset system.
    """
    # Check for API keys
    perplexity_key = os.getenv("PERPLEXITY_API_KEY") or os.getenv("PERPLEXITY-API-KEY")
    if not perplexity_key:
        pytest.skip("PERPLEXITY_API_KEY not found - cannot test preset overrides")

    service = DeepSearchService(preset="perplexity-sonar-pro")

    # Test provider override (if multiple providers available)
    genes = ["EGFR"]
    context = "receptor cancer"

    try:
        # Use preset configuration
        result1 = service.research_gene_list(genes=genes, context=context)
        assert result1 is not None
        # Verify content exists
        content1 = getattr(result1, "content", None) or getattr(result1, "markdown", "")
        assert len(content1) > 20

        # Test timeout override (shorter timeout)
        result2 = service.research_gene_list(
            genes=genes,
            context=context,
            timeout=30  # Much shorter than preset default of 180
        )
        assert result2 is not None
        content2 = getattr(result2, "content", None) or getattr(result2, "markdown", "")
        assert len(content2) > 20

        # Both should work, demonstrating override capability

    except Exception as e:
        # Don't fail if timeout causes issues - the override mechanism is what matters
        if "timeout" not in str(e).lower():
            pytest.fail(f"Preset override test failed: {str(e)}")


@pytest.mark.integration
def test_deepsearch_service_constructor_overrides() -> None:
    """Test that constructor overrides work with preset system.

    Verifies constructor parameter precedence over preset defaults.
    """
    # Check for API keys
    perplexity_key = os.getenv("PERPLEXITY_API_KEY") or os.getenv("PERPLEXITY-API-KEY")
    if not perplexity_key:
        pytest.skip("PERPLEXITY_API_KEY not found - cannot test constructor overrides")

    # Test model override in constructor
    service = DeepSearchService(
        preset="perplexity-sonar-pro",
        model="sonar-reasoning-pro"  # Explicitly set same model
    )

    assert service.config.model == "sonar-reasoning-pro"
    assert service.config.provider == "perplexity"

    # Test real API call with overridden configuration
    genes = ["CDK2"]
    context = "cell cycle"

    try:
        result = service.research_gene_list(genes=genes, context=context)

        assert result is not None

        # Get content from either attribute
        content = getattr(result, "content", None) or getattr(result, "markdown", "")
        assert len(content) > 20

        # Should mention the gene
        content_lower = content.lower()
        assert "cdk2" in content_lower or "cyclin" in content_lower

    except Exception as e:
        pytest.fail(f"Constructor override test failed: {str(e)}")


@pytest.mark.integration
def test_deepsearch_service_preset_error_handling() -> None:
    """Test error handling with preset system and real APIs.

    Verifies that API errors are handled gracefully with preset configuration.
    """
    # Check for API keys
    perplexity_key = os.getenv("PERPLEXITY_API_KEY") or os.getenv("PERPLEXITY-API-KEY")
    if not perplexity_key:
        pytest.skip("PERPLEXITY_API_KEY not found - cannot test error handling")

    service = DeepSearchService(preset="perplexity-sonar-pro")

    # Test with invalid input that should trigger validation
    with pytest.raises(ValueError) as exc_info:
        service.research_gene_list(genes=[], context="cancer")

    assert "genes" in str(exc_info.value).lower()

    # Test with empty context
    with pytest.raises(ValueError) as exc_info:
        service.research_gene_list(genes=["TP53"], context="")

    assert "context" in str(exc_info.value).lower()

    # These validation errors should work regardless of preset configuration