"""YAML-based configuration system for DeepSearch service.

This module provides configuration loading and validation for presets and templates
from YAML files with a clear loading hierarchy.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import jsonschema
import yaml


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


class ConfigurationError(Exception):
    """Raised when configuration loading or validation fails."""

    pass


class YAMLConfigManager:
    """Manages YAML-based configuration loading and validation."""

    def __init__(self, config_dir: str | None = None):
        """Initialize configuration manager.

        Args:
            config_dir: Optional custom config directory. If None, uses default hierarchy:
                       1. ./config/ (project config)
                       2. ~/.langpa/config/ (user config)
        """
        self.config_dir = Path(config_dir) if config_dir else None
        self._presets_cache: dict[str, dict[str, Any]] | None = None
        self._templates_cache: dict[str, dict[str, Any]] | None = None

    def _get_config_paths(self) -> list[Path]:
        """Get list of configuration directory paths in loading priority order.

        Returns:
            List of Path objects for config directories to check
        """
        paths = []

        if self.config_dir:
            # Custom config directory specified
            paths.append(self.config_dir)
        else:
            # Default hierarchy
            project_config = Path.cwd() / "config"
            user_config = Path.home() / ".langpa" / "config"

            # Add paths that exist
            for path in [project_config, user_config]:
                if path.exists():
                    paths.append(path)

        # Always include defaults from package
        package_defaults = Path(__file__).parent.parent.parent.parent / "config" / "defaults"
        if package_defaults.exists():
            paths.append(package_defaults)

        return paths

    def _load_yaml_file(self, filename: str) -> dict[str, Any]:
        """Load and merge YAML configuration from hierarchy of config directories.

        Args:
            filename: Name of YAML file to load (e.g., 'presets.yaml')

        Returns:
            Merged configuration dictionary

        Raises:
            ConfigurationError: If no valid config files found or YAML parsing fails
        """
        config_paths = self._get_config_paths()
        merged_config: dict[str, Any] = {}

        configs_found = 0
        for config_dir in reversed(config_paths):  # Start with defaults, overlay user configs
            config_file = config_dir / filename
            if config_file.exists():
                try:
                    with open(config_file) as f:
                        file_config = yaml.safe_load(f) or {}

                    # Merge configurations (later configs override earlier ones)
                    if isinstance(file_config, dict):
                        merged_config.update(file_config)
                        configs_found += 1
                except yaml.YAMLError as e:
                    raise ConfigurationError(f"Invalid YAML in {config_file}: {e}") from e
                except OSError as e:
                    raise ConfigurationError(f"Cannot read {config_file}: {e}") from e

        if configs_found == 0:
            raise ConfigurationError(f"No {filename} found in any config directory")

        return merged_config

    def _validate_config(self, config: dict[str, Any], schema_name: str) -> None:
        """Validate configuration against JSON schema.

        Args:
            config: Configuration dictionary to validate
            schema_name: Name of schema file (e.g., 'preset-schema.yaml')

        Raises:
            ConfigurationError: If validation fails
        """
        # Find schema file
        schema_paths = []
        for config_dir in self._get_config_paths():
            schema_dir = config_dir / "schemas"
            if schema_dir.exists():
                schema_paths.append(schema_dir)

        schema_file = None
        for schema_dir in schema_paths:
            potential_schema = schema_dir / schema_name
            if potential_schema.exists():
                schema_file = potential_schema
                break

        if not schema_file:
            # Schema validation is optional - warn but don't fail
            return

        try:
            with open(schema_file) as f:
                schema = yaml.safe_load(f)

            jsonschema.validate(instance=config, schema=schema)
        except jsonschema.ValidationError as e:
            raise ConfigurationError(f"Configuration validation failed: {e.message}") from e
        except (OSError, yaml.YAMLError) as e:
            raise ConfigurationError(f"Cannot load schema {schema_file}: {e}") from e

    def _load_presets(self) -> dict[str, dict[str, Any]]:
        """Load preset configurations from YAML files.

        Returns:
            Dictionary of preset configurations

        Raises:
            ConfigurationError: If loading or validation fails
        """
        if self._presets_cache is not None:
            return self._presets_cache

        config = self._load_yaml_file("presets.yaml")
        self._validate_config(config, "preset-schema.yaml")

        if "presets" not in config:
            raise ConfigurationError("Invalid presets.yaml: missing 'presets' key")

        self._presets_cache = config["presets"]
        return self._presets_cache

    def _load_templates(self) -> dict[str, dict[str, Any]]:
        """Load template configurations from YAML files.

        Returns:
            Dictionary of template configurations

        Raises:
            ConfigurationError: If loading or validation fails
        """
        if self._templates_cache is not None:
            return self._templates_cache

        config = self._load_yaml_file("templates.yaml")
        self._validate_config(config, "template-schema.yaml")

        if "templates" not in config:
            raise ConfigurationError("Invalid templates.yaml: missing 'templates' key")

        self._templates_cache = config["templates"]
        return self._templates_cache

    def get_preset_config(self, preset_name: str) -> DeepSearchConfig:
        """Get a configuration preset by name.

        Args:
            preset_name: Name of the preset to retrieve

        Returns:
            DeepSearchConfig object with the preset configuration

        Raises:
            ConfigurationError: If preset_name is not found
        """
        presets = self._load_presets()

        if preset_name not in presets:
            available = ", ".join(presets.keys())
            raise ConfigurationError(
                f"Unknown preset '{preset_name}'. Available presets: {available}"
            )

        preset_data = presets[preset_name]

        # Convert YAML data to DeepSearchConfig object
        return DeepSearchConfig(
            provider=preset_data["provider"],
            model=preset_data["model"],
            provider_params=copy.deepcopy(preset_data["provider_params"]),
            timeout=preset_data.get("timeout", 180),
            prompt_template=preset_data.get("prompt_template", "gene_analysis_academic"),
            description=preset_data.get("description", ""),
        )

    def list_available_presets(self) -> dict[str, str]:
        """List all available configuration presets.

        Returns:
            Dictionary mapping preset names to their descriptions
        """
        presets = self._load_presets()
        return {name: config.get("description", "") for name, config in presets.items()}

    def get_template(self, template_name: str) -> dict[str, Any]:
        """Get a prompt template by name.

        Args:
            template_name: Name of the template to retrieve

        Returns:
            Dictionary containing template configuration

        Raises:
            ConfigurationError: If template_name is not found
        """
        templates = self._load_templates()

        if template_name not in templates:
            available = ", ".join(templates.keys())
            raise ConfigurationError(
                f"Unknown template '{template_name}'. Available templates: {available}"
            )

        return copy.deepcopy(templates[template_name])

    def list_available_templates(self) -> dict[str, str]:
        """List all available prompt templates.

        Returns:
            Dictionary mapping template names to their descriptions
        """
        templates = self._load_templates()
        return {name: template.get("description", "") for name, template in templates.items()}

    def format_prompt_template(self, template_name: str, genes: list[str], context: str) -> str:
        """Format a prompt template with the provided genes and context.

        Args:
            template_name: Name of the template to use
            genes: List of gene symbols to analyze
            context: Biological context for the analysis

        Returns:
            Formatted prompt string ready for API call

        Raises:
            ConfigurationError: If template_name is not found
        """
        template_config = self.get_template(template_name)
        template_text = template_config["template"]

        # Format genes as comma-separated string
        genes_str = ", ".join(genes)

        # Substitute placeholders
        formatted_prompt = template_text.format(genes=genes_str, context=context)

        return formatted_prompt

    def get_template_metadata(self, template_name: str) -> dict[str, Any]:
        """Get metadata about a specific template.

        Args:
            template_name: Name of the template

        Returns:
            Dictionary with template metadata (supports_json_schema, optimized_for, description, schema_instruction)

        Raises:
            ConfigurationError: If template_name is not found
        """
        template_config = self.get_template(template_name)

        return {
            "supports_json_schema": template_config["supports_json_schema"],
            "optimized_for": template_config["optimized_for"],
            "description": template_config["description"],
            "schema_instruction": template_config.get("schema_instruction"),
        }

    def merge_config_overrides(
        self, base_config: DeepSearchConfig, overrides: dict[str, Any]
    ) -> DeepSearchConfig:
        """Merge configuration overrides into a base configuration.

        Args:
            base_config: Base configuration to start with
            overrides: Dictionary of field names to override values

        Returns:
            New DeepSearchConfig with overrides applied

        Raises:
            ConfigurationError: If unknown field names provided
        """
        # Start with a copy of the base config
        merged = copy.deepcopy(base_config)

        # Apply overrides
        for field_name, value in overrides.items():
            if hasattr(merged, field_name):
                setattr(merged, field_name, value)
            else:
                raise ConfigurationError(f"Unknown configuration field: {field_name}")

        return merged


# Global instance for backward compatibility
_global_config_manager: YAMLConfigManager | None = None


def get_config_manager(config_dir: str | None = None) -> YAMLConfigManager:
    """Get global configuration manager instance.

    Args:
        config_dir: Optional custom config directory

    Returns:
        YAMLConfigManager instance
    """
    global _global_config_manager

    if _global_config_manager is None or config_dir is not None:
        _global_config_manager = YAMLConfigManager(config_dir)

    return _global_config_manager


# Convenience functions for backward compatibility
def get_preset_config(preset_name: str) -> DeepSearchConfig:
    """Get a configuration preset by name."""
    return get_config_manager().get_preset_config(preset_name)


def list_available_presets() -> dict[str, str]:
    """List all available configuration presets."""
    return get_config_manager().list_available_presets()


def format_prompt_template(template_name: str, genes: list[str], context: str) -> str:
    """Format a prompt template with genes and context."""
    return get_config_manager().format_prompt_template(template_name, genes, context)


def list_available_templates() -> dict[str, str]:
    """List all available prompt templates."""
    return get_config_manager().list_available_templates()


def get_template_metadata(template_name: str) -> dict[str, Any]:
    """Get metadata about a specific template."""
    return get_config_manager().get_template_metadata(template_name)


def merge_config_overrides(
    base_config: DeepSearchConfig, overrides: dict[str, Any]
) -> DeepSearchConfig:
    """Merge configuration overrides into base configuration."""
    return get_config_manager().merge_config_overrides(base_config, overrides)
