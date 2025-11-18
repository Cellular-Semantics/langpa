"""Prompt templates for DeepSearch service.

This module provides reusable prompt templates for different analysis approaches
and provider optimizations.
"""

from __future__ import annotations


# Registry of available prompt templates
PROMPT_TEMPLATES: dict[str, dict[str, any]] = {
    "gene_analysis_academic": {
        "template": """Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: {genes}

**Biological Context**: {context}

**Analysis Strategy**:
1. Search current scientific literature for functional roles of each gene in the input list
2. Identify clusters of genes that act together in pathways, processes, or cellular states
3. Treat each cluster as a potential gene program within the list
4. Interpret findings in light of both normal physiological roles and disease-specific alterations
5. Prioritize well-established functions with strong literature support, but highlight emerging evidence if contextually relevant

**Guidelines**:
* Anchor all predictions in either the normal physiology and development of the cell type and tissue specified in the context OR the alterations and dysregulations characteristic of the specified disease
* Connect gene-level roles to program-level implications
* Consider gene interactions, regulatory networks, and pathway dynamics
* Highlight cases where multiple genes collectively strengthen evidence
* Ensure all claims are backed by experimental evidence with proper attribution

Provide a structured analysis identifying biological programs and their predicted cellular impacts within the given context.""",
        "supports_json_schema": True,
        "optimized_for": ["perplexity", "consensus"],
        "description": "Academic research-focused analysis with comprehensive literature review strategy"
    },

    "gene_analysis_structured": {
        "template": """Analyze the following genes in the specified biological context and provide structured findings.

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
        "description": "Structured analysis optimized for clear, systematic gene program identification"
    }
}


def get_prompt_template(template_name: str) -> dict[str, any]:
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


def format_prompt_template(template_name: str, genes: list[str], context: str) -> str:
    """Format a prompt template with the provided genes and context.

    Args:
        template_name: Name of the template to use
        genes: List of gene symbols to analyze
        context: Biological context for the analysis

    Returns:
        Formatted prompt string ready for API call

    Raises:
        ValueError: If template_name is not found
    """
    template_config = get_prompt_template(template_name)
    template_text = template_config["template"]

    # Format genes as comma-separated string
    genes_str = ", ".join(genes)

    # Substitute placeholders
    formatted_prompt = template_text.format(genes=genes_str, context=context)

    return formatted_prompt


def get_template_metadata(template_name: str) -> dict[str, any]:
    """Get metadata about a specific template.

    Args:
        template_name: Name of the template

    Returns:
        Dictionary with template metadata (supports_json_schema, optimized_for, description)

    Raises:
        ValueError: If template_name is not found
    """
    template_config = get_prompt_template(template_name)

    return {
        "supports_json_schema": template_config["supports_json_schema"],
        "optimized_for": template_config["optimized_for"],
        "description": template_config["description"]
    }