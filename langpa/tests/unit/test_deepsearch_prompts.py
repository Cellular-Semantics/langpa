"""Unit tests for DeepSearch prompt template system."""

from __future__ import annotations

import pytest

from langpa.services.deepsearch_prompts import (
    PROMPT_TEMPLATES,
    format_prompt_template,
    get_prompt_template,
    list_available_templates,
)


@pytest.mark.unit
def test_prompt_templates_structure() -> None:
    """Test that PROMPT_TEMPLATES contains expected templates."""
    # Should have at least the gene_analysis_academic template
    assert "gene_analysis_academic" in PROMPT_TEMPLATES

    # Each template should be a dictionary with required fields
    for template_name, template in PROMPT_TEMPLATES.items():
        assert isinstance(template, dict)
        assert isinstance(template_name, str)
        assert len(template_name) > 0

        # Each template should have required fields
        assert "template" in template
        assert "supports_json_schema" in template
        assert "optimized_for" in template
        assert "description" in template

        # Validate field types
        assert isinstance(template["template"], str)
        assert isinstance(template["supports_json_schema"], bool)
        assert isinstance(template["optimized_for"], list)
        assert isinstance(template["description"], str)


@pytest.mark.unit
def test_gene_analysis_academic_template() -> None:
    """Test the gene_analysis_academic template configuration."""
    template = PROMPT_TEMPLATES["gene_analysis_academic"]

    assert template["supports_json_schema"] is True
    assert "perplexity" in template["optimized_for"]
    assert "academic" in template["description"].lower()

    # Template should contain placeholders for genes and context
    template_text = template["template"]
    assert "{genes}" in template_text
    assert "{context}" in template_text

    # Should contain key analysis elements from original prompt
    template_lower = template_text.lower()
    assert "literature analysis" in template_lower or "analysis" in template_lower
    assert "gene" in template_lower
    assert "biological" in template_lower


@pytest.mark.unit
def test_get_prompt_template_valid() -> None:
    """Test getting a valid prompt template."""
    template = get_prompt_template("gene_analysis_academic")

    assert isinstance(template, dict)
    assert "template" in template
    assert "supports_json_schema" in template


@pytest.mark.unit
def test_get_prompt_template_invalid() -> None:
    """Test getting an invalid prompt template raises appropriate error."""
    with pytest.raises(ValueError) as exc_info:
        get_prompt_template("nonexistent-template")

    assert "Unknown template" in str(exc_info.value)
    assert "nonexistent-template" in str(exc_info.value)


@pytest.mark.unit
def test_list_available_templates() -> None:
    """Test listing available prompt templates."""
    templates = list_available_templates()

    assert isinstance(templates, dict)
    assert len(templates) > 0
    assert "gene_analysis_academic" in templates

    # Each entry should map name to description
    for name, description in templates.items():
        assert isinstance(name, str)
        assert isinstance(description, str)
        assert len(name) > 0
        assert len(description) > 0


@pytest.mark.unit
def test_format_prompt_template() -> None:
    """Test formatting a prompt template with genes and context."""
    genes = ["TP53", "BRCA1"]
    context = "cancer tumor suppressor genes"

    formatted = format_prompt_template("gene_analysis_academic", genes, context)

    assert isinstance(formatted, str)
    assert len(formatted) > 100  # Should be substantial content

    # Should contain the provided genes and context
    assert "TP53" in formatted
    assert "BRCA1" in formatted
    assert "cancer tumor suppressor genes" in formatted

    # Should not contain unsubstituted placeholders
    assert "{genes}" not in formatted
    assert "{context}" not in formatted


@pytest.mark.unit
def test_format_prompt_template_genes_formatting() -> None:
    """Test that genes are properly formatted in templates."""
    genes = ["MYC", "EGFR", "KRAS"]
    context = "oncogenes"

    formatted = format_prompt_template("gene_analysis_academic", genes, context)

    # Genes should be joined properly (likely comma-separated)
    genes_str = ", ".join(genes)
    assert genes_str in formatted

    # Each gene should appear in the formatted text
    for gene in genes:
        assert gene in formatted


@pytest.mark.unit
def test_format_prompt_template_invalid_template() -> None:
    """Test formatting with invalid template name raises error."""
    with pytest.raises(ValueError):
        format_prompt_template("invalid-template", ["TP53"], "cancer")


@pytest.mark.unit
def test_template_placeholder_substitution() -> None:
    """Test that all placeholders in templates are properly substituted."""
    from langpa.services.deepsearch_prompts import get_template_metadata

    # Test with all templates to ensure they work
    genes = ["TEST1", "TEST2"]
    context = "test biological context"
    test_schema = {"type": "object", "properties": {"test": {"type": "string"}}}

    for template_name in PROMPT_TEMPLATES:
        # Check if template requires schema
        metadata = get_template_metadata(template_name)
        if metadata.get("requires_full_schema", False):
            # Provide schema for schema-embedded templates
            formatted = format_prompt_template(template_name, genes, context, schema=test_schema)
        else:
            # Legacy templates don't need schema
            formatted = format_prompt_template(template_name, genes, context)

        # Should not contain any unsubstituted placeholders
        assert "{genes}" not in formatted
        assert "{context}" not in formatted
        assert "{genes_json_array}" not in formatted
        assert "{schema}" not in formatted

        # Should contain the test values
        assert "TEST1" in formatted
        assert "test biological context" in formatted


@pytest.mark.unit
def test_prompt_template_content_preservation() -> None:
    """Test that the current prompt content is preserved in gene_analysis_academic template."""
    template = get_prompt_template("gene_analysis_academic")
    template_text = template["template"]

    # Key elements from the original prompt should be preserved
    template_lower = template_text.lower()

    # Analysis strategy elements
    expected_elements = ["literature", "analysis", "gene", "biological", "program", "pathway"]

    found_elements = sum(1 for element in expected_elements if element in template_lower)
    assert found_elements >= 4, "Template should preserve key analysis concepts"


@pytest.mark.unit
def test_template_optimization_metadata() -> None:
    """Test that template optimization metadata is meaningful."""
    for _template_name, template in PROMPT_TEMPLATES.items():
        optimized_for = template["optimized_for"]

        # Should be optimized for at least one provider
        assert len(optimized_for) > 0

        # Provider names should be reasonable
        for provider in optimized_for:
            assert isinstance(provider, str)
            assert len(provider) > 0
            assert provider.lower() in ["perplexity", "openai", "edison", "consensus", "anthropic"]


@pytest.mark.unit
def test_json_schema_support_consistency() -> None:
    """Test that JSON schema support is consistently handled."""
    # All current templates should support JSON schema for structured output
    for template_name, template in PROMPT_TEMPLATES.items():
        # Current implementation should support JSON schema
        assert template["supports_json_schema"] is True, (
            f"Template {template_name} should support JSON schema"
        )


@pytest.mark.unit
def test_format_prompt_template_with_schema() -> None:
    """Test formatting a schema-embedded template with schema parameter."""
    genes = ["TP53", "BRCA1"]
    context = "cancer tumor suppressor genes"
    schema = {
        "type": "object",
        "properties": {
            "test": {"type": "string"}
        }
    }

    # This should work once we implement the new template
    formatted = format_prompt_template(
        "gene_analysis_schema_embedded",
        genes,
        context,
        schema=schema
    )

    assert isinstance(formatted, str)
    assert len(formatted) > 100

    # Should contain JSON array format for genes
    assert '["TP53", "BRCA1"]' in formatted

    # Should contain the schema as JSON string
    assert '"type": "object"' in formatted
    assert '"properties"' in formatted

    # Should not contain unsubstituted placeholders
    assert "{genes_json_array}" not in formatted
    assert "{schema}" not in formatted
    assert "{context}" not in formatted


@pytest.mark.unit
def test_format_prompt_template_schema_required_error() -> None:
    """Test that schema-embedded templates require schema parameter."""
    genes = ["TP53"]
    context = "cancer"

    # Should raise ValueError when schema is required but not provided
    with pytest.raises(ValueError) as exc_info:
        format_prompt_template("gene_analysis_schema_embedded", genes, context)

    assert "requires schema parameter" in str(exc_info.value).lower()


@pytest.mark.unit
def test_gene_analysis_schema_embedded_template() -> None:
    """Test the new gene_analysis_schema_embedded template configuration."""
    template = PROMPT_TEMPLATES["gene_analysis_schema_embedded"]

    assert template["supports_json_schema"] is True
    assert template["requires_full_schema"] is True
    assert "perplexity" in template["optimized_for"]
    assert "schema-embedded" in template["description"].lower()

    # Template should contain placeholders
    template_text = template["template"]
    assert "{genes_json_array}" in template_text
    assert "{context}" in template_text
    assert "{schema}" in template_text

    # Should contain key analysis elements
    template_lower = template_text.lower()
    assert "literature analysis" in template_lower or "analysis" in template_lower
    assert "gene" in template_lower
    assert "biological" in template_lower


@pytest.mark.unit
def test_get_template_metadata_new_field() -> None:
    """Test that get_template_metadata returns requires_full_schema field."""
    from langpa.services.deepsearch_prompts import get_template_metadata

    # Test with schema-embedded template
    metadata = get_template_metadata("gene_analysis_schema_embedded")
    assert "requires_full_schema" in metadata
    assert metadata["requires_full_schema"] is True
    assert metadata["supports_json_schema"] is True

    # Test with legacy template
    metadata_legacy = get_template_metadata("gene_analysis_academic")
    assert "requires_full_schema" in metadata_legacy
    assert metadata_legacy["requires_full_schema"] is False


@pytest.mark.unit
def test_format_prompt_template_genes_json_array() -> None:
    """Test that genes are formatted as JSON array in schema-embedded templates."""
    genes = ["MYC", "EGFR", "KRAS"]
    context = "oncogenes"
    schema = {"type": "object"}

    formatted = format_prompt_template(
        "gene_analysis_schema_embedded",
        genes,
        context,
        schema=schema
    )

    # Should contain genes as JSON array
    import json
    genes_json = json.dumps(genes)
    assert genes_json in formatted
    assert '["MYC", "EGFR", "KRAS"]' in formatted


@pytest.mark.unit
def test_legacy_templates_no_schema_required() -> None:
    """Test that legacy templates work without schema parameter."""
    genes = ["TP53"]
    context = "cancer"

    # Should work fine without schema parameter
    formatted = format_prompt_template("gene_analysis_academic", genes, context)

    assert isinstance(formatted, str)
    assert "TP53" in formatted
    assert "cancer" in formatted
