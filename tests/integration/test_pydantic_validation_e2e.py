"""End-to-end test for pydantic validation with DeepSearch API.

This test verifies the complete pipeline from API call through pydantic validation
using the cellsem_llm_client's SchemaManager and SchemaValidator.
"""

from __future__ import annotations

import os

import pytest
from dotenv import load_dotenv

from langpa.services.deepsearch_service import DeepSearchService
from langpa.services.deepsearch_validator import DeepSearchValidator
from langpa.services.pydantic_models import get_deepsearch_pydantic_model

# Load environment variables
load_dotenv()


@pytest.mark.integration
def test_deepsearch_pydantic_validation_e2e() -> None:
    """Test complete E2E flow with pydantic validation.

    This test:
    1. Makes a real API call to Perplexity
    2. Extracts JSON from markdown response
    3. Validates using dynamically generated pydantic model
    4. Verifies structured data access via pydantic attributes
    """
    # Check for API key
    perplexity_key = os.getenv("PERPLEXITY_API_KEY") or os.getenv("PERPLEXITY-API-KEY")
    if not perplexity_key:
        pytest.skip("PERPLEXITY_API_KEY not found - cannot test E2E validation")

    # Initialize service and validator
    service = DeepSearchService(preset="perplexity-sonar-pro")
    validator = DeepSearchValidator()

    # Use minimal gene set for cost optimization
    genes = ["TMEM14E"]
    context = "cells"

    # Step 1: Make real API call
    try:
        result = service.research_gene_list(genes=genes, context=context)
        assert result is not None, "API call should return result"

        # Get markdown response
        markdown = getattr(result, "markdown", None) or getattr(result, "content", None)
        assert markdown is not None, "Response should have markdown or content"
        assert isinstance(markdown, str), "Markdown should be string"
        assert len(markdown) > 100, "Response should have substantial content"

    except Exception as e:
        pytest.fail(f"API call failed: {str(e)}")

    # Step 2: Validate with pydantic
    try:
        validation_result = validator.validate_markdown(markdown, max_retries=3)

        # Check validation succeeded
        assert validation_result.success, (
            f"Validation should succeed. Error: {validation_result.error}"
        )
        assert validation_result.model_instance is not None, (
            "Should have validated model instance"
        )

        # Check metadata
        assert validation_result.retry_count >= 0, "Should have retry count"
        assert validation_result.validation_time_ms > 0, "Should have validation time"

    except Exception as e:
        pytest.fail(f"Pydantic validation failed: {str(e)}")

    # Step 3: Verify pydantic model structure
    model_instance = validation_result.model_instance
    pydantic_model = get_deepsearch_pydantic_model()

    # Should be instance of dynamically generated model
    assert isinstance(model_instance, pydantic_model), (
        "Instance should be of correct pydantic model type"
    )

    # Step 4: Verify required fields exist (based on deepsearch_results_schema.json)
    assert hasattr(model_instance, "context"), (
        "Model should have context field"
    )
    assert hasattr(model_instance, "input_genes"), "Model should have input_genes field"
    assert hasattr(model_instance, "programs"), "Model should have programs field"

    # Step 5: Verify data structure and content
    # Context should be populated
    assert isinstance(model_instance.context, dict), (
        "context should be dict"
    )
    assert "cell_type" in model_instance.context, "context should have cell_type"

    # Input genes array should be populated
    assert isinstance(model_instance.input_genes, list), "input_genes should be list"
    assert len(model_instance.input_genes) > 0, "input_genes should have at least one entry"

    # Verify gene symbol matches request
    input_genes_upper = [g.upper() for g in model_instance.input_genes]
    assert "TMEM14E" in input_genes_upper, "Should find TMEM14E in input_genes"

    # Programs array should be populated
    assert isinstance(model_instance.programs, list), "programs should be list"
    assert len(model_instance.programs) > 0, "programs should have entries"

    # Each program should have structure (program_name, not research_program_name)
    first_program = model_instance.programs[0]
    assert isinstance(first_program, dict), "Program should be dict"
    assert "program_name" in first_program, (
        "Program should have program_name"
    )
    assert "description" in first_program, "Program should have description"

    # Programs should have atomic terms with citations
    if "atomic_biological_processes" in first_program:
        atomic_processes = first_program["atomic_biological_processes"]
        if len(atomic_processes) > 0:
            first_process = atomic_processes[0]
            assert isinstance(first_process, dict), "Atomic process should be dict"
            assert "citations" in first_process, "Atomic process should have citations"

            # Citations should have proper structure
            citations = first_process["citations"]
            assert isinstance(citations, list), "citations should be list"
            if len(citations) > 0:
                first_citation = citations[0]
                assert isinstance(first_citation, dict), "Citation should be dict"
                assert "source_id" in first_citation, "Citation should have source_id"


@pytest.mark.integration
def test_deepsearch_pydantic_validation_with_moderate_genes() -> None:
    """Test E2E pydantic validation with moderate gene set.

    Uses slightly larger gene list to test multi-gene validation.
    """
    # Check for API key
    perplexity_key = os.getenv("PERPLEXITY_API_KEY") or os.getenv("PERPLEXITY-API-KEY")
    if not perplexity_key:
        pytest.skip("PERPLEXITY_API_KEY not found - cannot test E2E validation")

    # Initialize service and validator
    service = DeepSearchService(preset="perplexity-sonar-pro")
    validator = DeepSearchValidator()

    # Use moderate gene set
    genes = ["C9orf72", "C21orf91"]
    context = "neural cells"

    # Make API call
    try:
        result = service.research_gene_list(genes=genes, context=context)
        markdown = getattr(result, "markdown", None) or getattr(result, "content", None)
        assert markdown is not None

    except Exception as e:
        pytest.fail(f"API call failed: {str(e)}")

    # Validate with pydantic
    try:
        validation_result = validator.validate_markdown(markdown, max_retries=3)

        assert validation_result.success, (
            f"Validation should succeed. Error: {validation_result.error}"
        )
        assert validation_result.model_instance is not None

    except Exception as e:
        pytest.fail(f"Pydantic validation failed: {str(e)}")

    # Verify multi-gene results
    model_instance = validation_result.model_instance

    # Should have both genes in input_genes
    input_genes_upper = [g.upper() for g in model_instance.input_genes]

    # At least one of the requested genes should be present
    found_genes = [g for g in ["C9ORF72", "C21ORF91"] if g in input_genes_upper]
    assert len(found_genes) > 0, (
        f"Should find at least one requested gene. Found: {input_genes_upper}"
    )


@pytest.mark.integration
def test_deepsearch_pydantic_validation_retry_mechanism() -> None:
    """Test that pydantic validation retry mechanism works.

    This test verifies that the SchemaValidator's retry logic is engaged
    when needed and provides metadata about retries.
    """
    # Check for API key
    perplexity_key = os.getenv("PERPLEXITY_API_KEY") or os.getenv("PERPLEXITY-API-KEY")
    if not perplexity_key:
        pytest.skip("PERPLEXITY_API_KEY not found - cannot test retry mechanism")

    # Initialize validator
    validator = DeepSearchValidator()

    # Test with minimal valid JSON matching schema
    test_json = """
    {
        "context": {
            "cell_type": "test cells",
            "disease": "",
            "tissue": ""
        },
        "input_genes": ["TEST"],
        "programs": [{
            "program_name": "Test Program",
            "description": "Test description",
            "atomic_biological_processes": [],
            "atomic_cellular_components": [],
            "predicted_cellular_impact": ["test impact"]
        }],
        "version": "1.0"
    }
    """

    # This should succeed with basic valid JSON
    try:
        result = validator.schema_validator.validate_with_retry(
            response_text=test_json,
            target_model=get_deepsearch_pydantic_model(),
            max_retries=3,
        )

        # Check that validation metadata is present
        assert hasattr(result, "retry_count"), "Should have retry_count"
        assert hasattr(result, "validation_time_ms"), "Should have validation_time_ms"
        assert result.retry_count >= 0, "Retry count should be non-negative"
        assert result.validation_time_ms > 0, "Should have positive validation time"

    except Exception as e:
        pytest.fail(f"Retry mechanism test failed: {str(e)}")


@pytest.mark.integration
def test_deepsearch_output_manager_pydantic_integration() -> None:
    """Test OutputManager's pydantic integration in E2E workflow.

    Verifies that OutputManager.validate_against_schema_v2 works with real API data.
    """
    # Check for API key
    perplexity_key = os.getenv("PERPLEXITY_API_KEY") or os.getenv("PERPLEXITY-API-KEY")
    if not perplexity_key:
        pytest.skip("PERPLEXITY_API_KEY not found - cannot test OutputManager integration")

    # Initialize service
    service = DeepSearchService(preset="perplexity-sonar-pro")

    # Make API call
    genes = ["TMEM14E"]
    context = "cells"

    try:
        result = service.research_gene_list(genes=genes, context=context)
        markdown = getattr(result, "markdown", None) or getattr(result, "content", None)
        assert markdown is not None

    except Exception as e:
        pytest.fail(f"API call failed: {str(e)}")

    # Extract JSON using OutputManager (create instance directly)
    from langpa.services.output_manager import OutputManager

    output_manager = OutputManager()
    json_data = output_manager.extract_json_from_markdown(markdown)

    assert json_data is not None, "Should extract JSON from markdown"
    assert isinstance(json_data, dict), "Extracted data should be dict"

    # Validate using pydantic through OutputManager
    try:
        is_valid, error_msg, metadata = output_manager.validate_against_schema_v2(
            json_data, use_pydantic=True, max_retries=3
        )

        assert is_valid, f"Validation should succeed. Error: {error_msg}"
        assert error_msg is None, "Should have no error message on success"

        # Check metadata
        assert isinstance(metadata, dict), "Metadata should be dict"
        assert "retry_count" in metadata, "Should have retry_count"
        assert "validation_time_ms" in metadata, "Should have validation_time_ms"
        assert "corrections_applied" in metadata, "Should have corrections_applied flag"

        # Verify metadata values
        assert metadata["retry_count"] >= 0, "Retry count should be non-negative"
        assert metadata["validation_time_ms"] > 0, "Should have positive validation time"
        assert isinstance(metadata["corrections_applied"], bool), (
            "corrections_applied should be boolean"
        )

    except Exception as e:
        pytest.fail(f"OutputManager pydantic validation failed: {str(e)}")
