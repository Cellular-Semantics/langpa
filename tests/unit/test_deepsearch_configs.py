"""Unit tests for DeepSearch configuration presets."""

from __future__ import annotations

import pytest

from langpa.services.deepsearch_configs import (
    PRESET_CONFIGS,
    DeepSearchConfig,
    get_preset_config,
    list_available_presets,
)


@pytest.mark.unit
def test_deepsearch_config_dataclass() -> None:
    """Test DeepSearchConfig dataclass structure and validation."""
    config = DeepSearchConfig(
        provider="test_provider",
        model="test_model",
        provider_params={"test_param": "test_value"},
        timeout=120,
        prompt_template="test_template",
        description="Test configuration",
    )

    assert config.provider == "test_provider"
    assert config.model == "test_model"
    assert config.provider_params == {"test_param": "test_value"}
    assert config.timeout == 120
    assert config.prompt_template == "test_template"
    assert config.description == "Test configuration"


@pytest.mark.unit
def test_preset_configs_structure() -> None:
    """Test that PRESET_CONFIGS contains expected presets."""
    # Should have at least the perplexity-sonar-pro preset
    assert "perplexity-sonar-pro" in PRESET_CONFIGS

    # Each preset should be a DeepSearchConfig
    for preset_name, config in PRESET_CONFIGS.items():
        assert isinstance(config, DeepSearchConfig)
        assert isinstance(preset_name, str)
        assert len(preset_name) > 0

        # Each config should have all required fields
        assert hasattr(config, "provider")
        assert hasattr(config, "model")
        assert hasattr(config, "provider_params")
        assert hasattr(config, "timeout")
        assert hasattr(config, "prompt_template")
        assert hasattr(config, "description")


@pytest.mark.unit
def test_perplexity_sonar_pro_preset() -> None:
    """Test the perplexity-sonar-pro preset configuration."""
    config = PRESET_CONFIGS["perplexity-sonar-pro"]

    assert config.provider == "perplexity"
    assert config.model == "sonar-reasoning-pro"
    assert config.timeout == 180
    assert config.prompt_template == "gene_analysis_academic"
    assert "perplexity" in config.description.lower()

    # Provider params should be dictionary with expected Perplexity settings
    params = config.provider_params
    assert isinstance(params, dict)
    assert "return_citations" in params
    assert "reasoning_effort" in params
    assert "search_recency_filter" in params
    assert "search_domain_filter" in params

    # Should have academic domain filters
    domain_filter = params["search_domain_filter"]
    assert isinstance(domain_filter, list)
    assert "pubmed.ncbi.nlm.nih.gov" in domain_filter
    assert "ncbi.nlm.nih.gov/pmc/" in domain_filter


@pytest.mark.unit
def test_get_preset_config_valid() -> None:
    """Test getting a valid preset configuration."""
    config = get_preset_config("perplexity-sonar-pro")

    assert isinstance(config, DeepSearchConfig)
    assert config.provider == "perplexity"
    assert config.model == "sonar-reasoning-pro"


@pytest.mark.unit
def test_get_preset_config_invalid() -> None:
    """Test getting an invalid preset raises appropriate error."""
    with pytest.raises(ValueError) as exc_info:
        get_preset_config("nonexistent-preset")

    assert "Unknown preset" in str(exc_info.value)
    assert "nonexistent-preset" in str(exc_info.value)


@pytest.mark.unit
def test_list_available_presets() -> None:
    """Test listing available presets returns correct structure."""
    presets = list_available_presets()

    assert isinstance(presets, dict)
    assert len(presets) > 0
    assert "perplexity-sonar-pro" in presets

    # Each entry should map name to description
    for name, description in presets.items():
        assert isinstance(name, str)
        assert isinstance(description, str)
        assert len(name) > 0
        assert len(description) > 0


@pytest.mark.unit
def test_preset_config_immutability() -> None:
    """Test that preset configs can be safely copied without side effects."""
    original_config = get_preset_config("perplexity-sonar-pro")

    # Modify the returned config
    original_config.timeout = 999
    original_config.provider_params["new_param"] = "new_value"

    # Getting the preset again should return unmodified version
    fresh_config = get_preset_config("perplexity-sonar-pro")
    assert fresh_config.timeout == 180  # Original value
    assert "new_param" not in fresh_config.provider_params


@pytest.mark.unit
def test_config_merge_functionality() -> None:
    """Test configuration merging for overrides."""
    from langpa.services.deepsearch_configs import merge_config_overrides

    base_config = DeepSearchConfig(
        provider="test",
        model="base_model",
        provider_params={"base_param": "base_value"},
        timeout=100,
        prompt_template="base_template",
        description="Base config",
    )

    overrides = {
        "model": "override_model",
        "timeout": 200,
        "provider_params": {"override_param": "override_value"},
    }

    merged = merge_config_overrides(base_config, overrides)

    assert merged.provider == "test"  # Unchanged
    assert merged.model == "override_model"  # Overridden
    assert merged.timeout == 200  # Overridden
    assert merged.provider_params == {"override_param": "override_value"}  # Replaced
    assert merged.prompt_template == "base_template"  # Unchanged
    assert merged.description == "Base config"  # Unchanged
