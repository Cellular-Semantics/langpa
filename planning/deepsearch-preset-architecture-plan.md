# DeepSearch Preset Architecture Plan

## Problem Analysis
- **Major Duplication**: DeepSearchService hardcodes functionality that `deep-research-client` already provides
- **Inflexible Configuration**: Hardcoded model (`sonar-reasoning-pro`) and Perplexity-specific parameters
- **No Preset System**: Each usage requires full configuration specification

## Goal: Package-First Preset System
Create well-tested configuration presets that can be used programmatically in workflows and exposed via CLI.

## Architecture Design

### Core Package Structure (`src/langpa/services/`)

#### 1. Configuration Module (`deepsearch_configs.py`)
```python
@dataclass
class DeepSearchConfig:
    provider: str
    model: str
    provider_params: BaseProviderParams
    timeout: int
    prompt_template: str  # References prompt in registry
    description: str

PRESET_CONFIGS = {
    "perplexity-sonar-pro": DeepSearchConfig(
        provider="perplexity",
        model="sonar-reasoning-pro",
        provider_params=PerplexityParams(...),
        prompt_template="gene_analysis_academic",
        description="Academic research optimized for Perplexity"
    )
}
```

#### 2. Prompt Templates Module (`deepsearch_prompts.py`)
```python
PROMPT_TEMPLATES = {
    "gene_analysis_academic": {
        "template": "Perform comprehensive literature analysis for {genes}...",
        "supports_json_schema": True,
        "optimized_for": ["perplexity", "consensus"]
    },
    "gene_analysis_structured": {
        "template": "Analyze genes {genes} and return structured data...",
        "supports_json_schema": True,
        "optimized_for": ["openai", "edison"]
    }
}
```

#### 3. Enhanced DeepSearchService
```python
class DeepSearchService:
    def __init__(self, preset: str | None = "perplexity-sonar-pro", **overrides):
        # Load preset config (with prompts)

    def _construct_prompt(self, genes: list[str], context: str, template: str) -> str:
        # Use template from prompt registry

    @classmethod
    def get_available_presets(cls) -> dict[str, str]:
        # Return presets with descriptions
```

## Implementation Phases

### Phase 1: Core Configuration System (TDD)
**Goal**: Create preset configuration without breaking existing functionality

**Tasks**:
1. Write tests for preset loading
2. Create `DeepSearchConfig` dataclass
3. Extract current hardcoded configuration as "perplexity-sonar-pro" preset
4. Preserve current prompt template exactly
5. Update DeepSearchService to use preset system
6. Ensure backward compatibility

**Exit Criteria**: All existing tests pass, current functionality preserved

### Phase 2: Prompt Template System (TDD)
**Goal**: Add flexible prompt templating while preserving current prompt

**Tasks**:
1. Write tests for prompt templating
2. Create `deepsearch_prompts.py` module
3. Extract current prompt as "gene_analysis_academic" template
4. Update service to use prompt templates
5. Add prompt override capabilities

**Exit Criteria**: Current prompt behavior unchanged, template system functional

### Phase 3: CLI Enhancement
**Goal**: Expose preset system via command line

**Tasks**:
1. Add `--preset` argument to runner script
2. Add `--list-presets` and `--list-prompts` commands
3. Add `--prompt-template` override option
4. Maintain backward compatibility with existing args
5. Update help documentation

**Exit Criteria**: CLI supports presets, existing commands work unchanged

### Phase 4: Additional Presets (Gradual)
**Goal**: Add more well-tested configurations

**Tasks**:
1. Research optimal configurations for other providers
2. Write integration tests for each new preset
3. Add presets one by one with full testing
4. Document preset characteristics and use cases

## Programmatic Usage Examples
```python
# Use preset (includes tested prompt)
service = DeepSearchService(preset="perplexity-sonar-pro")

# Override prompt template within preset
service = DeepSearchService(
    preset="perplexity-sonar-pro",
    prompt_template="gene_analysis_structured"
)

# Custom prompt entirely
result = service.research_gene_list(
    genes=["TP53"],
    context="cancer",
    custom_prompt="Your custom prompt here: {genes} in {context}"
)
```

## CLI Usage Examples
```bash
# Use preset (includes prompt)
python scripts/run_deepsearch.py --preset perplexity-sonar-pro

# Override prompt template
python scripts/run_deepsearch.py --preset perplexity-sonar-pro --prompt-template gene_analysis_structured

# List available presets and prompts
python scripts/run_deepsearch.py --list-presets
python scripts/run_deepsearch.py --list-prompts
```

## Benefits
- **Prompt-Provider Co-optimization**: Each preset includes tested prompt
- **Flexible Override**: Change prompts within presets
- **Prompt Reuse**: Templates work across multiple presets
- **Battle-tested Combinations**: Integration tests verify prompt+provider pairs
- **Easy Discovery**: List available presets and their optimized prompts
- **Package-First**: Workflows use presets programmatically, CLI exposes functionality

## Risks and Mitigations
- **Breaking Changes**: Maintain backward compatibility in all phases
- **Test Dependencies**: Integration tests require real API keys (following CLAUDE.md)
- **Configuration Complexity**: Start simple, expand gradually
- **Prompt Regressions**: Preserve exact current prompt behavior

## Success Criteria
1. Current functionality preserved throughout
2. Preset system available programmatically
3. CLI exposes all preset functionality
4. Integration tests verify each preset works
5. Documentation covers all usage patterns