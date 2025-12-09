"""Configuration presets for DeepSearch service.

This module provides well-tested configuration presets that combine provider settings,
model selection, and optimized parameters for different use cases.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass
from typing import Any


@dataclass
class DeepSearchConfig:
    """Configuration for DeepSearch service with provider-specific settings.

    Args:
        provider: Research provider name (e.g., 'perplexity', 'openai')
        model: Model to use with the provider
        provider_params: Provider-specific parameters (dict or parameter object)
        timeout: Request timeout in seconds
        prompt_template: Name of prompt template to use
        description: Human-readable description of this configuration
    """

    provider: str
    model: str
    provider_params: dict[str, Any] | Any
    timeout: int = 180
    prompt_template: str = "gene_analysis_academic"
    description: str = ""


# Well-tested configuration presets
PRESET_CONFIGS: dict[str, DeepSearchConfig] = {
    "perplexity-sonar-pro": DeepSearchConfig(
        provider="perplexity",
        model="sonar-reasoning-pro",
        provider_params={
            "return_citations": True,
            "search_domain_filter": [
                "pubmed.ncbi.nlm.nih.gov",
                "ncbi.nlm.nih.gov/pmc/",
                "www.ncbi.nlm.nih.gov",
                "europepmc.org",
                "biorxiv.org",
                "nature.com",
                "cell.com",
                "science.org",
            ],
            "reasoning_effort": "high",
            "search_recency_filter": "month",
            "system_prompt": None,  # Will be set dynamically with JSON schema
        },
        timeout=180,
        prompt_template="gene_analysis_academic",
        description="Academic research optimized for Perplexity with high reasoning effort",
    ),
    "perplexity-sonar-schema-embedded": DeepSearchConfig(
        provider="perplexity",
        model="sonar-deep-research",
        provider_params={
            "return_citations": True,
            "search_domain_filter": [
                "pubmed.ncbi.nlm.nih.gov",
                "ncbi.nlm.nih.gov/pmc/",
                "www.ncbi.nlm.nih.gov",
                "europepmc.org",
                "biorxiv.org",
                "nature.com",
                "cell.com",
                "science.org",
            ],
            "reasoning_effort": "high",
            "search_recency_filter": "month",
            "system_prompt": None,  # Will be set dynamically to minimal prompt
        },
        timeout=180,
        prompt_template="gene_analysis_schema_embedded",
        description="Schema-embedded approach with full schema in user prompt - proven to work reliably with Perplexity for JSON output",
    ),
}


def get_preset_config(preset_name: str) -> DeepSearchConfig:
    """Get a configuration preset by name.

    Args:
        preset_name: Name of the preset to retrieve

    Returns:
        DeepSearchConfig object with the preset configuration

    Raises:
        ValueError: If preset_name is not found
    """
    if preset_name not in PRESET_CONFIGS:
        available = ", ".join(PRESET_CONFIGS.keys())
        raise ValueError(f"Unknown preset '{preset_name}'. Available presets: {available}")

    # Return a deep copy to prevent accidental modification of the original
    return copy.deepcopy(PRESET_CONFIGS[preset_name])


def list_available_presets() -> dict[str, str]:
    """List all available configuration presets.

    Returns:
        Dictionary mapping preset names to their descriptions
    """
    return {name: config.description for name, config in PRESET_CONFIGS.items()}


def merge_config_overrides(
    base_config: DeepSearchConfig, overrides: dict[str, Any]
) -> DeepSearchConfig:
    """Merge configuration overrides into a base configuration.

    Args:
        base_config: Base configuration to start with
        overrides: Dictionary of field names to override values

    Returns:
        New DeepSearchConfig with overrides applied
    """
    # Start with a copy of the base config
    merged = copy.deepcopy(base_config)

    # Apply overrides
    for field_name, value in overrides.items():
        if hasattr(merged, field_name):
            setattr(merged, field_name, value)
        else:
            raise ValueError(f"Unknown configuration field: {field_name}")

    return merged
