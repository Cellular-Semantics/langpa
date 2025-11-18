# YAML Configuration System for DeepSearch - Planning Document

## Overview
Create a separate configuration management script alongside the existing `run_deepsearch.py` to provide a flexible YAML-based system for managing presets and templates without overloading the existing analysis script.

## Problem Statement
The current hardcoded Python configuration system makes it difficult to:
- Experiment with DeepSearch parameters (reasoning effort, search domains, recency filters)
- Create new presets without code changes
- Edit templates without touching Python files
- Share configurations between team members
- Version control configurations separately from code
- Document configuration rationale with comments

## Solution Architecture

### Script Separation
```
scripts/
├── run_deepsearch.py          # Existing script (unchanged)
├── manage_config.py           # New configuration management script
└── validate_config.py         # New configuration validation script (optional)
```

### Configuration File Structure
```
config/
├── presets.yaml               # Configuration presets
├── templates.yaml             # Prompt templates
└── schemas/
    ├── preset-schema.yaml     # Validation schema for presets
    └── template-schema.yaml   # Validation schema for templates
```

## manage_config.py - Dedicated Configuration Management

### Core Commands
```bash
# Discovery
python scripts/manage_config.py list-presets
python scripts/manage_config.py list-templates

# Creation
python scripts/manage_config.py create-preset cancer-research
python scripts/manage_config.py create-template pathway-focused

# Editing
python scripts/manage_config.py edit-preset perplexity-sonar-pro
python scripts/manage_config.py edit-template gene_analysis_academic

# Management
python scripts/manage_config.py copy-preset source-name target-name
python scripts/manage_config.py delete-preset old-preset
python scripts/manage_config.py rename-preset old-name new-name

# Validation
python scripts/manage_config.py validate
python scripts/manage_config.py validate-preset cancer-research

# Information
python scripts/manage_config.py show-preset cancer-research
python scripts/manage_config.py show-template pathway-focused
```

## Configuration File Examples

### config/presets.yaml Structure
```yaml
# DeepSearch Configuration Presets
# Edit this file to customize or add new presets

presets:
  perplexity-sonar-pro:
    description: "Academic research optimized for Perplexity with high reasoning effort"
    provider: perplexity
    model: sonar-reasoning-pro
    timeout: 180
    prompt_template: gene_analysis_academic
    provider_params:
      return_citations: true
      reasoning_effort: high  # low, medium, high
      search_recency_filter: month  # hour, day, week, month, year
      search_domain_filter:
        - "pubmed.ncbi.nlm.nih.gov"
        - "ncbi.nlm.nih.gov/pmc/"
        # ... other domains

  perplexity-fast:
    description: "Fast analysis with lower reasoning effort for quick experiments"
    provider: perplexity
    model: sonar-small
    timeout: 60
    prompt_template: gene_analysis_structured
    provider_params:
      return_citations: true
      reasoning_effort: low
      search_recency_filter: week
```

### config/templates.yaml Structure
```yaml
# DeepSearch Prompt Templates
# Edit this file to customize or add new templates

templates:
  gene_analysis_academic:
    description: "Academic research-focused analysis with comprehensive literature review strategy"
    optimized_for: [perplexity, consensus]
    supports_json_schema: true
    template: |
      Perform comprehensive literature analysis for the following gene list...
      # Multi-line template with proper YAML formatting

  pathway_focused:
    description: "Pathway-centric analysis focusing on regulatory networks"
    optimized_for: [perplexity]
    supports_json_schema: true
    template: |
      Focus on pathway analysis for the following genes...
```

## Integration Strategy

### Configuration Loading Priority
1. `--config-dir` specified directory
2. `./config/` (project config)
3. `~/.langpa/config/` (user config)
4. Built-in hardcoded configs (fallback)

### Backward Compatibility
- `run_deepsearch.py` remains unchanged in terms of CLI interface
- YAML configs supplement hardcoded configs (no breaking changes)
- Existing workflows continue to work without modification

## Implementation Benefits

### User Benefits
1. **Easy Experimentation**: Change parameters without code edits
2. **Documentation**: YAML comments explain configuration choices
3. **Sharing**: Easy to share configurations via files
4. **Version Control**: Track configuration changes separately
5. **Validation**: Schema validation prevents invalid configurations

### Developer Benefits
1. **Separation of Concerns**: Configuration management in dedicated script
2. **Flexibility**: New providers/models without code changes
3. **Testing**: Easy A/B testing of configurations
4. **Maintenance**: Configuration bugs don't require code releases

## Example User Workflow
```bash
# 1. Explore available configurations
python scripts/manage_config.py list-presets

# 2. Create custom configuration for research
python scripts/manage_config.py copy-preset perplexity-sonar-pro my-cancer-research
python scripts/manage_config.py edit-preset my-cancer-research

# 3. Validate configuration
python scripts/manage_config.py validate-preset my-cancer-research

# 4. Use in analysis (existing script unchanged)
python scripts/run_deepsearch.py --preset my-cancer-research --genes TP53,BRCA1 --context "cancer"
```

## Key Design Principles
- **No CLI overload**: Keep `run_deepsearch.py` focused on analysis
- **User-friendly**: YAML is easier to edit than Python code
- **Backward compatible**: No breaking changes to existing workflows
- **Validation**: Schema validation prevents configuration errors
- **Discoverable**: Easy to find and understand available options
- **Shareable**: Configuration files can be version controlled and shared

This approach provides powerful configuration management while keeping the analysis script clean and focused on its primary purpose.