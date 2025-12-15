"""DeepSearch service for gene list contextual analysis."""

from __future__ import annotations

import json
import warnings
from typing import Any

from deep_research_client import DeepResearchClient  # type: ignore
from deep_research_client.models import CacheConfig  # type: ignore
from dotenv import load_dotenv

from langpa.schemas import load_schema
from langpa.services.deepsearch_configs import (
    DeepSearchConfig,
    get_preset_config,
    list_available_presets,
    merge_config_overrides,
)
from langpa.services.deepsearch_prompts import (
    format_prompt_template,
    get_template_metadata,
    list_available_templates,
)

# Load environment variables
load_dotenv()


class DeepSearchService:
    """Service for performing contextual gene list analysis using DeepSearch/Perplexity."""

    def __init__(
        self,
        preferred_provider: str | None = None,
        preset: str | None = None,
        cache_config: CacheConfig | None = None,
        **config_overrides: Any,
    ) -> None:
        """Initialize the DeepSearch service.

        Args:
            preferred_provider: Preferred research provider (e.g., 'perplexity', 'openai')
                               If None, uses first available provider. (Backward compatibility)
            preset: Configuration preset name (e.g., 'perplexity-sonar-pro')
                   If None, uses 'perplexity-sonar-pro' as default
            cache_config: Cache configuration for DeepResearchClient (default: disabled)
            **config_overrides: Override specific configuration fields
        """
        # Default to disabling client cache unless explicitly provided
        if cache_config is None:
            cache_config = CacheConfig(enabled=False)

        self.client = DeepResearchClient(cache_config=cache_config)

        # Load configuration (preset takes precedence over preferred_provider for new pattern)
        if preset is not None:
            self.config = get_preset_config(preset)
            if config_overrides:
                self.config = merge_config_overrides(self.config, config_overrides)
        else:
            # Backward compatibility: use preferred_provider with default preset
            self.config = get_preset_config("perplexity-sonar-pro")
            if preferred_provider:
                # Override provider in default config for backward compatibility
                self.config = merge_config_overrides(self.config, {"provider": preferred_provider})

        # Keep old attributes for backward compatibility
        self.preferred_provider = preferred_provider
        self._available_providers: list[str] | None = None

    @classmethod
    def get_available_presets(cls) -> dict[str, str]:
        """Get list of available configuration presets.

        Returns:
            Dictionary mapping preset names to their descriptions
        """
        return list_available_presets()

    @classmethod
    def get_preset_config(cls, preset_name: str) -> DeepSearchConfig:
        """Get a specific preset configuration.

        Args:
            preset_name: Name of the preset to retrieve

        Returns:
            DeepSearchConfig object for the preset

        Raises:
            ValueError: If preset_name is not found
        """
        return get_preset_config(preset_name)

    @classmethod
    def get_available_templates(cls) -> dict[str, str]:
        """Get list of available prompt templates.

        Returns:
            Dictionary mapping template names to their descriptions
        """
        return list_available_templates()

    @property
    def available_providers(self) -> list[str]:
        """Get list of available research providers."""
        if self._available_providers is None:
            self._available_providers = self.client.get_available_providers()
        return self._available_providers

    def _get_provider(self) -> str:
        """Get the provider to use for research."""
        providers = self.available_providers

        if not providers:
            raise ValueError("No research providers available. Check API key configuration.")

        if self.preferred_provider and self.preferred_provider in providers:
            return self.preferred_provider

        # Default preference order: perplexity first (cheaper), then others
        if "perplexity" in providers:
            return "perplexity"

        return providers[0]

    def _construct_prompt(
        self, genes: list[str], context: str, template_override: str | None = None
    ) -> str:
        """Construct the research prompt for gene list analysis.

        Uses configurable prompt templates for different analysis approaches.

        Args:
            genes: List of gene symbols to analyze
            context: Biological context for the analysis
            template_override: Optional template name to override config default

        Returns:
            Formatted prompt for DeepSearch API
        """
        # Determine which template to use
        template_name = template_override or self.config.prompt_template

        # Check if template requires schema embedding in user prompt
        template_metadata = get_template_metadata(template_name)
        schema = None
        if template_metadata.get("requires_full_schema", False):
            # Load schema for embedding in user prompt
            schema = load_schema("deepsearch_results_schema.json")

        # Format the prompt using the template system
        return format_prompt_template(template_name, genes, context, schema=schema)

    def construct_prompt(
        self, genes: list[str], context: str, template_override: str | None = None
    ) -> str:
        """Public method to construct the research prompt for gene list analysis.

        Uses configurable prompt templates for different analysis approaches.

        Args:
            genes: List of gene symbols to analyze
            context: Biological context for the analysis
            template_override: Optional template name to override config default

        Returns:
            Formatted prompt for DeepSearch API
        """
        return self._construct_prompt(genes, context, template_override)

    def _resolve_system_prompt(
        self,
        provider_params: dict[str, Any],
        schema: dict[str, Any],
        template_requires_schema: bool,
    ) -> str:
        """Resolve the system prompt to use, enforcing explicit selection."""
        system_prompt = provider_params.get("system_prompt")
        if not system_prompt:
            raise ValueError(
                "system_prompt must be specified in provider_params; "
                "update the preset to set an explicit system prompt."
            )

        # Replace schema placeholder if present
        if "{schema}" in system_prompt:
            system_prompt = system_prompt.format(schema=json.dumps(schema, indent=2))

        # Warn about known incompatibility: sonar-deep-research with JSON-focused prompts
        if self.config.model == "sonar-deep-research" and "json" in system_prompt.lower():
            warnings.warn(
                "sonar-deep-research is known to ignore or fail with JSON-enforcing system prompts; "
                "consider using a non-JSON system prompt for this model.",
                UserWarning,
            )

        # If template requires schema in user prompt, prefer non-JSON system prompts,
        # but we keep the explicit selection made in the preset to honor user choice.
        return system_prompt

    def research_gene_list(
        self,
        genes: list[str],
        context: str,
        provider: str | None = None,
        timeout: int = 180,
        custom_prompt: str | None = None,
        prompt_template: str | None = None,
    ) -> Any:
        """Perform contextual research analysis of a gene list.

        Args:
            genes: List of gene symbols to analyze (e.g., ["TP53", "BRCA1"])
            context: Biological context for analysis (e.g., "cancer", "tumor suppressor genes")
            provider: Optional override for research provider
            timeout: Timeout in seconds for the API call (default 180s)
            custom_prompt: Optional custom prompt to use instead of templates
            prompt_template: Optional template name to override config default

        Returns:
            ResearchResult object with content and citations

        Raises:
            ValueError: If genes list is empty or context is empty
            Exception: If API call fails
        """
        # Input validation
        if not genes:
            raise ValueError("Genes list cannot be empty")

        if not context or not context.strip():
            raise ValueError("Context cannot be empty")

        # Construct research query
        if custom_prompt:
            # Use custom prompt directly
            prompt = custom_prompt
        else:
            # Use template system
            prompt = self._construct_prompt(genes, context, template_override=prompt_template)

        # Determine provider (support both new preset system and backward compatibility)
        research_provider = provider or self.config.provider

        # Use timeout from config or method parameter (method parameter takes precedence)
        # Note: timeout parameter is used for backward compatibility but not currently applied

        # Load schema for response_format
        schema = load_schema("deepsearch_results_schema.json")

        # Prepare provider params from config
        provider_params = dict(self.config.provider_params)  # Copy to avoid modifying original

        # Determine system prompt strategy based on preset/template choice
        template_name = prompt_template or self.config.prompt_template
        template_metadata = get_template_metadata(template_name)

        provider_params["system_prompt"] = self._resolve_system_prompt(
            provider_params=provider_params,
            schema=schema,
            template_requires_schema=template_metadata.get("requires_full_schema", False),
        )

        # Use configuration-driven research call
        try:
            result = self.client.research(
                query=prompt,
                provider=research_provider,
                model=self.config.model,
                provider_params=provider_params,
            )
            return result
        except Exception as e:
            # Re-raise with context
            raise Exception(f"DeepSearch API error: {str(e)}") from e
