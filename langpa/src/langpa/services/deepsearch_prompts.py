"""Prompt templates for DeepSearch service.

This module provides reusable prompt templates for different analysis approaches
and provider optimizations.
"""

from __future__ import annotations

from typing import Any

# Registry of available prompt templates
PROMPT_TEMPLATES: dict[str, dict[str, Any]] = {
    "gene_analysis_academic": {
        "template": """Perform comprehensive literature analysis for the following gene list in the
specified biological context.

**Gene List**: {genes}

**Biological Context**: {context}

**Analysis Strategy**:
1. Search current scientific literature for functional roles of each gene in the input list
2. Identify clusters of genes that act together in pathways, processes, or cellular states
3. Treat each cluster as a potential gene program within the list
4. Interpret findings in light of both normal physiological roles and disease-specific alterations
5. Prioritize well-established functions with strong literature support, but highlight emerging
   evidence if contextually relevant

**Guidelines**:
* Anchor all predictions in either the normal physiology and development of the cell type and
  tissue specified in the context OR the alterations and dysregulations characteristic of the
  specified disease
* Connect gene-level roles to program-level implications
* Consider gene interactions, regulatory networks, and pathway dynamics
* Highlight cases where multiple genes collectively strengthen evidence
* Ensure all claims are backed by experimental evidence with proper attribution

Provide a structured analysis identifying biological programs and their predicted cellular
impacts within the given context.""",
        "supports_json_schema": True,
        "optimized_for": ["perplexity", "consensus"],
        "description": "Academic research-focused analysis with comprehensive literature review "
        "strategy",
    },
    "gene_analysis_structured": {
        "template": """Analyze the following genes in the specified biological context and provide
structured findings.

**Genes to Analyze**: {genes}

**Context**: {context}

**Required Analysis**:
1. For each gene, identify its primary biological functions
2. Group genes by common pathways or biological processes
3. Identify potential gene programs (clusters of functionally related genes)
4. Assess the relevance to the specified biological context

**Output Requirements**:
- Focus on well-established, peer-reviewed findings
- Prioritize recent research when available
- Include pathway and process associations
- Highlight gene-gene interactions where relevant

Provide a systematic analysis organized by biological programs and functional clusters.""",
        "supports_json_schema": True,
        "optimized_for": ["openai", "edison"],
        "description": "Structured analysis optimized for clear, systematic gene program "
        "identification",
    },
    "gene_analysis_schema_embedded": {
        "template": """Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: {genes_json_array}

**Biological Context**: {context}

**Analysis Strategy**:
1. Search current scientific literature for functional roles of each gene in the input list
2. Identify clusters of genes that act together in pathways, processes, or cellular states
3. Treat each cluster as a potential gene program within the list
4. Interpret findings in light of both normal physiological roles and disease-specific alterations
5. Prioritize well-established functions with strong literature support, but highlight emerging evidence if contextually relevant.

**Guidelines**:
* Anchor all predictions in either the normal physiology and development of the cell type and tissue specified in the context OR the alterations and dysregulations characteristic of the specified disease
* Connect gene-level roles to program-level implications
* Consider gene interactions, regulatory networks, and pathway dynamics
* Highlight cases where multiple genes collectively strengthen evidence
* Ensure all claims are backed by experimental evidence with proper attribution

**Output**: Respond with JSON conforming to the provided schema - no prose, no markdown. If you are unable to respond with JSON alone, make sure the text includes tables or fragments of schema compliant that unambiguously capture the elements and their associations that would be captured if returning JSON schema.

```json
{schema}
```
""",
        "supports_json_schema": True,
        "requires_full_schema": True,
        "optimized_for": ["perplexity"],
        "description": "Schema-embedded prompt with full JSON schema in user message (proven to work reliably with Perplexity)",
    },
}


def get_prompt_template(template_name: str) -> dict[str, Any]:
    """Get a prompt template by name.

    Args:
        template_name: Name of the template to retrieve

    Returns:
        Dictionary containing template configuration

    Raises:
        ValueError: If template_name is not found
    """
    if template_name not in PROMPT_TEMPLATES:
        available = ", ".join(PROMPT_TEMPLATES.keys())
        raise ValueError(f"Unknown template '{template_name}'. Available templates: {available}")

    return PROMPT_TEMPLATES[template_name].copy()


def list_available_templates() -> dict[str, str]:
    """List all available prompt templates.

    Returns:
        Dictionary mapping template names to their descriptions
    """
    return {name: template["description"] for name, template in PROMPT_TEMPLATES.items()}


def format_prompt_template(
    template_name: str,
    genes: list[str],
    context: str,
    schema: dict[str, Any] | None = None
) -> str:
    """Format a prompt template with genes, context, and optional schema.

    Args:
        template_name: Name of the template to use
        genes: List of gene symbols to analyze
        context: Biological context for the analysis
        schema: Optional JSON schema dict (required for schema-embedded templates)

    Returns:
        Formatted prompt string ready for API call

    Raises:
        ValueError: If template_name is not found or schema is required but not provided
    """
    import json

    template_config = get_prompt_template(template_name)
    template_text = template_config["template"]

    # Format genes as comma-separated string (default/legacy)
    genes_str = ", ".join(genes)

    # Format genes as JSON array (for schema-embedded templates)
    genes_json_array = json.dumps(genes)

    # Prepare substitution dict
    format_dict = {
        "genes": genes_str,
        "genes_json_array": genes_json_array,
        "context": context
    }

    # Add schema if template requires it
    if template_config.get("requires_full_schema", False):
        if schema is None:
            raise ValueError(
                f"Template '{template_name}' requires schema parameter. "
                "Schema must be provided when using schema-embedded templates."
            )
        format_dict["schema"] = json.dumps(schema, indent=2)

    # Substitute placeholders
    formatted_prompt = template_text.format(**format_dict)

    return formatted_prompt


def get_template_metadata(template_name: str) -> dict[str, Any]:
    """Get metadata about a specific template.

    Args:
        template_name: Name of the template

    Returns:
        Dictionary with template metadata

    Raises:
        ValueError: If template_name is not found
    """
    template_config = get_prompt_template(template_name)

    return {
        "supports_json_schema": template_config.get("supports_json_schema", False),
        "requires_full_schema": template_config.get("requires_full_schema", False),
        "optimized_for": template_config.get("optimized_for", []),
        "description": template_config.get("description", ""),
    }
