"""Unit tests for YAML configuration system."""

from __future__ import annotations

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

from langpa.services.yaml_config import (
    ConfigurationError,
    DeepSearchConfig,
    YAMLConfigManager,
    format_prompt_template,
    get_config_manager,
    get_preset_config,
    list_available_presets,
    list_available_templates,
)


@pytest.mark.unit
def test_yaml_config_manager_init() -> None:
    """Test YAMLConfigManager initialization."""
    # Test with no config directory
    manager = YAMLConfigManager()
    assert manager.config_dir is None

    # Test with custom config directory
    with tempfile.TemporaryDirectory() as temp_dir:
        manager = YAMLConfigManager(temp_dir)
        assert manager.config_dir == Path(temp_dir)


@pytest.mark.unit
def test_load_presets_from_yaml() -> None:
    """Test loading presets from YAML configuration."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        presets_file = config_dir / "presets.yaml"

        # Create test presets YAML
        preset_config = {
            "presets": {
                "test-preset": {
                    "description": "Test preset",
                    "provider": "perplexity",
                    "model": "sonar-reasoning-pro",
                    "timeout": 180,
                    "prompt_template": "gene_analysis_academic",
                    "provider_params": {
                        "return_citations": True,
                        "reasoning_effort": "high",
                    },
                }
            }
        }

        with open(presets_file, "w") as f:
            yaml.dump(preset_config, f)

        manager = YAMLConfigManager(str(config_dir))
        config = manager.get_preset_config("test-preset")

        assert config.provider == "perplexity"
        assert config.model == "sonar-reasoning-pro"
        assert config.timeout == 180
        assert config.prompt_template == "gene_analysis_academic"
        assert config.provider_params["reasoning_effort"] == "high"


@pytest.mark.unit
def test_load_templates_from_yaml() -> None:
    """Test loading templates from YAML configuration."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        templates_file = config_dir / "templates.yaml"

        # Create test templates YAML
        template_config = {
            "templates": {
                "test-template": {
                    "description": "Test template",
                    "optimized_for": ["perplexity"],
                    "supports_json_schema": True,
                    "template": "Analyze genes: {genes} in context: {context}",
                }
            }
        }

        with open(templates_file, "w") as f:
            yaml.dump(template_config, f)

        manager = YAMLConfigManager(str(config_dir))
        template = manager.get_template("test-template")

        assert template["description"] == "Test template"
        assert template["optimized_for"] == ["perplexity"]
        assert template["supports_json_schema"] is True
        assert template["template"] == "Analyze genes: {genes} in context: {context}"


@pytest.mark.unit
def test_config_hierarchy_loading() -> None:
    """Test configuration loading hierarchy (user > project > defaults)."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create base config
        base_dir = Path(temp_dir) / "base"
        base_dir.mkdir()
        base_presets = base_dir / "presets.yaml"

        base_config = {
            "presets": {
                "test-preset": {
                    "description": "Base preset",
                    "provider": "perplexity",
                    "model": "sonar-small",
                    "timeout": 120,
                    "prompt_template": "gene_analysis_academic",
                    "provider_params": {"reasoning_effort": "low"},
                }
            }
        }

        with open(base_presets, "w") as f:
            yaml.dump(base_config, f)

        # Mock the _get_config_paths to return our test directory
        manager = YAMLConfigManager()
        with patch.object(manager, "_get_config_paths", return_value=[base_dir]):
            config = manager.get_preset_config("test-preset")
            assert config.model == "sonar-small"
            assert config.provider_params["reasoning_effort"] == "low"


@pytest.mark.unit
def test_preset_not_found_error() -> None:
    """Test appropriate error when preset is not found."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        presets_file = config_dir / "presets.yaml"

        # Create empty presets file
        with open(presets_file, "w") as f:
            yaml.dump({"presets": {}}, f)

        manager = YAMLConfigManager(str(config_dir))

        with pytest.raises(ConfigurationError) as exc_info:
            manager.get_preset_config("nonexistent-preset")

        assert "Unknown preset 'nonexistent-preset'" in str(exc_info.value)


@pytest.mark.unit
def test_template_not_found_error() -> None:
    """Test appropriate error when template is not found."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        templates_file = config_dir / "templates.yaml"

        # Create empty templates file
        with open(templates_file, "w") as f:
            yaml.dump({"templates": {}}, f)

        manager = YAMLConfigManager(str(config_dir))

        with pytest.raises(ConfigurationError) as exc_info:
            manager.get_template("nonexistent-template")

        assert "Unknown template 'nonexistent-template'" in str(exc_info.value)


@pytest.mark.unit
def test_format_prompt_template() -> None:
    """Test prompt template formatting with genes and context."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        templates_file = config_dir / "templates.yaml"

        template_config = {
            "templates": {
                "test-template": {
                    "description": "Test template",
                    "optimized_for": ["perplexity"],
                    "supports_json_schema": True,
                    "template": "Analyze {genes} in {context} context.",
                }
            }
        }

        with open(templates_file, "w") as f:
            yaml.dump(template_config, f)

        manager = YAMLConfigManager(str(config_dir))
        formatted = manager.format_prompt_template("test-template", ["TP53", "BRCA1"], "cancer")

        assert formatted == "Analyze TP53, BRCA1 in cancer context."


@pytest.mark.unit
def test_merge_config_overrides() -> None:
    """Test merging configuration overrides."""
    base_config = DeepSearchConfig(
        provider="perplexity",
        model="sonar-small",
        provider_params={"reasoning_effort": "low"},
        timeout=120,
    )

    manager = YAMLConfigManager()
    overrides = {"model": "sonar-reasoning-pro", "timeout": 180}

    merged = manager.merge_config_overrides(base_config, overrides)

    assert merged.provider == "perplexity"  # Unchanged
    assert merged.model == "sonar-reasoning-pro"  # Overridden
    assert merged.timeout == 180  # Overridden
    assert merged.provider_params == {"reasoning_effort": "low"}  # Unchanged


@pytest.mark.unit
def test_merge_config_invalid_field() -> None:
    """Test error when merging unknown configuration field."""
    base_config = DeepSearchConfig(
        provider="perplexity",
        model="sonar-small",
        provider_params={},
    )

    manager = YAMLConfigManager()
    overrides = {"invalid_field": "value"}

    with pytest.raises(ConfigurationError) as exc_info:
        manager.merge_config_overrides(base_config, overrides)

    assert "Unknown configuration field: invalid_field" in str(exc_info.value)


@pytest.mark.unit
def test_list_available_presets() -> None:
    """Test listing available presets."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        presets_file = config_dir / "presets.yaml"

        preset_config = {
            "presets": {
                "preset1": {
                    "description": "First preset",
                    "provider": "perplexity",
                    "model": "test",
                },
                "preset2": {"description": "Second preset", "provider": "openai", "model": "test"},
            }
        }

        with open(presets_file, "w") as f:
            yaml.dump(preset_config, f)

        manager = YAMLConfigManager(str(config_dir))
        presets = manager.list_available_presets()

        assert len(presets) == 2
        assert presets["preset1"] == "First preset"
        assert presets["preset2"] == "Second preset"


@pytest.mark.unit
def test_list_available_templates() -> None:
    """Test listing available templates."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        templates_file = config_dir / "templates.yaml"

        template_config = {
            "templates": {
                "template1": {"description": "First template", "optimized_for": ["perplexity"]},
                "template2": {"description": "Second template", "optimized_for": ["openai"]},
            }
        }

        with open(templates_file, "w") as f:
            yaml.dump(template_config, f)

        manager = YAMLConfigManager(str(config_dir))
        templates = manager.list_available_templates()

        assert len(templates) == 2
        assert templates["template1"] == "First template"
        assert templates["template2"] == "Second template"


@pytest.mark.unit
def test_invalid_yaml_error() -> None:
    """Test error handling for invalid YAML files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        presets_file = config_dir / "presets.yaml"

        # Write invalid YAML
        with open(presets_file, "w") as f:
            f.write("invalid: yaml: content: [")

        manager = YAMLConfigManager(str(config_dir))

        with pytest.raises(ConfigurationError) as exc_info:
            manager.list_available_presets()

        assert "Invalid YAML" in str(exc_info.value)


@pytest.mark.unit
def test_missing_config_section_error() -> None:
    """Test error when configuration file is missing required sections."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        presets_file = config_dir / "presets.yaml"

        # Write YAML without 'presets' key
        with open(presets_file, "w") as f:
            yaml.dump({"other_key": "value"}, f)

        manager = YAMLConfigManager(str(config_dir))

        # Mock _get_config_paths to only return our test directory (no fallback to defaults)
        with patch.object(manager, "_get_config_paths", return_value=[config_dir]):
            with pytest.raises(ConfigurationError) as exc_info:
                manager.list_available_presets()

            assert "missing 'presets' key" in str(exc_info.value)


@pytest.mark.unit
def test_global_config_manager_functions() -> None:
    """Test global convenience functions work with default config."""
    # These functions should work with the built-in default configs
    # even if no custom config directory is provided
    presets = list_available_presets()
    assert isinstance(presets, dict)
    assert "perplexity-sonar-pro" in presets

    templates = list_available_templates()
    assert isinstance(templates, dict)
    assert "gene_analysis_academic" in templates

    # Test getting a default preset
    config = get_preset_config("perplexity-sonar-pro")
    assert config.provider == "perplexity"
    assert config.model == "sonar-reasoning-pro"

    # Test formatting with default template
    formatted = format_prompt_template("gene_analysis_academic", ["TP53"], "cancer")
    assert "TP53" in formatted
    assert "cancer" in formatted


@pytest.mark.unit
def test_template_metadata() -> None:
    """Test getting template metadata."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        templates_file = config_dir / "templates.yaml"

        template_config = {
            "templates": {
                "test-template": {
                    "description": "Test template for metadata",
                    "optimized_for": ["perplexity", "openai"],
                    "supports_json_schema": True,
                    "schema_instruction": "Please format as JSON: {schema}",
                    "template": "Test template: {genes} {context}",
                }
            }
        }

        with open(templates_file, "w") as f:
            yaml.dump(template_config, f)

        manager = YAMLConfigManager(str(config_dir))
        metadata = manager.get_template_metadata("test-template")

        assert metadata["description"] == "Test template for metadata"
        assert metadata["optimized_for"] == ["perplexity", "openai"]
        assert metadata["supports_json_schema"] is True
        assert metadata["schema_instruction"] == "Please format as JSON: {schema}"


@pytest.mark.unit
def test_template_metadata_without_schema_instruction() -> None:
    """Test getting template metadata when schema_instruction is missing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        templates_file = config_dir / "templates.yaml"

        template_config = {
            "templates": {
                "test-template": {
                    "description": "Test template without schema instruction",
                    "optimized_for": ["perplexity"],
                    "supports_json_schema": True,
                    "template": "Test template: {genes} {context}",
                    # Note: no schema_instruction field
                }
            }
        }

        with open(templates_file, "w") as f:
            yaml.dump(template_config, f)

        manager = YAMLConfigManager(str(config_dir))
        metadata = manager.get_template_metadata("test-template")

        assert metadata["description"] == "Test template without schema instruction"
        assert metadata["optimized_for"] == ["perplexity"]
        assert metadata["supports_json_schema"] is True
        assert metadata["schema_instruction"] is None


@pytest.mark.unit
def test_schema_instruction_with_placeholder() -> None:
    """Test that schema instruction properly handles {schema} placeholder."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        templates_file = config_dir / "templates.yaml"

        template_config = {
            "templates": {
                "test-template": {
                    "description": "Test template with schema placeholder",
                    "optimized_for": ["perplexity"],
                    "supports_json_schema": True,
                    "schema_instruction": """Custom instruction for schema compliance.

Please format your response as JSON following this structure:
{schema}

Ensure all fields are complete.""",
                    "template": "Test template: {genes} {context}",
                }
            }
        }

        with open(templates_file, "w") as f:
            yaml.dump(template_config, f)

        manager = YAMLConfigManager(str(config_dir))
        metadata = manager.get_template_metadata("test-template")

        instruction = metadata["schema_instruction"]
        assert "{schema}" in instruction
        assert "Custom instruction" in instruction
        assert "Please format your response as JSON" in instruction


@pytest.mark.unit
def test_deepsearch_config_dataclass() -> None:
    """Test DeepSearchConfig dataclass behavior."""
    config = DeepSearchConfig(
        provider="perplexity",
        model="sonar-reasoning-pro",
        provider_params={"reasoning_effort": "high"},
    )

    # Test default values
    assert config.timeout == 180
    assert config.prompt_template == "gene_analysis_academic"
    assert config.description == ""

    # Test explicit values
    assert config.provider == "perplexity"
    assert config.model == "sonar-reasoning-pro"
    assert config.provider_params == {"reasoning_effort": "high"}


@pytest.mark.unit
def test_configuration_caching() -> None:
    """Test that configuration is cached for performance."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir)
        presets_file = config_dir / "presets.yaml"

        preset_config = {
            "presets": {
                "test-preset": {
                    "description": "Cached preset",
                    "provider": "perplexity",
                    "model": "sonar-small",
                    "timeout": 120,
                    "prompt_template": "gene_analysis_academic",
                    "provider_params": {},
                }
            }
        }

        with open(presets_file, "w") as f:
            yaml.dump(preset_config, f)

        manager = YAMLConfigManager(str(config_dir))

        # First call should load and cache
        presets1 = manager._load_presets()
        # Second call should return cached result
        presets2 = manager._load_presets()

        # Should be the same object (cached)
        assert presets1 is presets2


@pytest.mark.unit
def test_config_manager_global_instance() -> None:
    """Test global config manager instance management."""
    # Get default instance
    manager1 = get_config_manager()
    manager2 = get_config_manager()

    # Should be same instance
    assert manager1 is manager2

    # Getting with config_dir should create new instance
    with tempfile.TemporaryDirectory() as temp_dir:
        manager3 = get_config_manager(temp_dir)
        assert manager3 is not manager1
        assert manager3.config_dir == Path(temp_dir)
