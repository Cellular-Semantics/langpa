"""DeepSearch service for gene list contextual analysis."""

from __future__ import annotations

import json
from typing import Any

from deep_research_client import DeepResearchClient  # type: ignore
from dotenv import load_dotenv

from langpa.schemas import load_schema
from langpa.services.yaml_config import (
    DeepSearchConfig,
    get_config_manager,
)

# Load environment variables
load_dotenv()


class DeepSearchService:
    """Service for performing contextual gene list analysis using DeepSearch/Perplexity."""

    def __init__(
        self,
        preferred_provider: str | None = None,
        preset: str | None = None,
        config_dir: str | None = None,
        **config_overrides: Any,
    ) -> None:
        """Initialize the DeepSearch service.

        Args:
            preferred_provider: Preferred research provider (e.g., 'perplexity', 'openai')
                               If None, uses provider from preset. (Backward compatibility)
            preset: Configuration preset name (e.g., 'perplexity-sonar-pro')
                   If None, uses 'perplexity-sonar-pro' as default
            config_dir: Optional custom configuration directory
            **config_overrides: Override specific configuration fields
        """
        self.client = DeepResearchClient()
        self.config_manager = get_config_manager(config_dir)

        # Load base configuration from preset
        preset_name = preset or "perplexity-sonar-pro"  # Default preset
        self.config = self.config_manager.get_preset_config(preset_name)

        # Apply overrides - handle preferred_provider as special case for backward compatibility
        final_overrides = dict(config_overrides)
        if preferred_provider:
            final_overrides["provider"] = preferred_provider

        # Apply ALL overrides (fixes backward compatibility bug)
        if final_overrides:
            self.config = self.config_manager.merge_config_overrides(self.config, final_overrides)

        # Keep old attributes for backward compatibility
        self.preferred_provider = preferred_provider
        self._available_providers: list[str] | None = None

    @classmethod
    def get_available_presets(cls, config_dir: str | None = None) -> dict[str, str]:
        """Get list of available configuration presets.

        Args:
            config_dir: Optional custom configuration directory

        Returns:
            Dictionary mapping preset names to their descriptions
        """
        return get_config_manager(config_dir).list_available_presets()

    @classmethod
    def get_preset_config(cls, preset_name: str, config_dir: str | None = None) -> DeepSearchConfig:
        """Get a specific preset configuration.

        Args:
            preset_name: Name of the preset to retrieve
            config_dir: Optional custom configuration directory

        Returns:
            DeepSearchConfig object for the preset

        Raises:
            ConfigurationError: If preset_name is not found
        """
        return get_config_manager(config_dir).get_preset_config(preset_name)

    @classmethod
    def get_available_templates(cls, config_dir: str | None = None) -> dict[str, str]:
        """Get list of available prompt templates.

        Args:
            config_dir: Optional custom configuration directory

        Returns:
            Dictionary mapping template names to their descriptions
        """
        return get_config_manager(config_dir).list_available_templates()

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

    def _get_system_prompt_with_schema(self, prompt_template: str | None = None) -> str:
        """Generate system prompt with JSON schema injection.

        Args:
            prompt_template: Optional template name override

        Returns:
            System prompt with schema injected
        """
        # Load schema for response_format
        schema = load_schema("deepsearch_results_schema.json")

        # Get provider params for current config
        provider_params = dict(self.config.provider_params)

        # Determine schema instruction priority: preset system_prompt > template schema_instruction > default
        if provider_params.get("system_prompt"):
            # Preset has custom system_prompt - use it and substitute {schema} if present
            instruction = provider_params["system_prompt"]
        else:
            # Get template metadata to access schema instruction
            template_name = prompt_template or self.config.prompt_template
            template_metadata = self.config_manager.get_template_metadata(template_name)

            # Use template's schema instruction or default fallback
            if template_metadata.get("schema_instruction"):
                instruction = template_metadata["schema_instruction"]
            else:
                # Default fallback for templates without schema_instruction
                instruction = """You are an expert biologist. Analyze the provided genes in the given biological context.

CRITICAL: Respond ONLY with valid JSON that exactly follows this schema structure:
{schema}

Do not include any prose, markdown, explanatory text, or <think> tags. Only the JSON structure."""

        # Return system prompt with schema substitution
        return instruction.format(schema=json.dumps(schema, indent=2))

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

        # Format the prompt using the YAML template system
        return self.config_manager.format_prompt_template(template_name, genes, context)

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

        try:
            # Prepare provider params from config
            provider_params = dict(self.config.provider_params)  # Copy to avoid modifying original

            # Set system_prompt with schema injection
            provider_params["system_prompt"] = self._get_system_prompt_with_schema(prompt_template)

            # Use configuration-driven research call
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
