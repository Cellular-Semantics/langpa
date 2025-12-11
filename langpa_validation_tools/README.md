# langpa-validation-tools

Validation and comparison tools for LangPA DeepSearch outputs.

## Features

- **Comparison**: Compare gene programs across multiple runs
- **Embeddings**: Semantic similarity using OpenAI embeddings
- **Visualization**: Heatmaps and bubble plots (coming in Phase 4)
- **Reporting**: Master validation reports (coming in Phase 6)
- **CLI**: Command-line interface for validation workflows

## Installation

### From UV Workspace (Development)

From the langpa repo root:
```bash
uv sync  # Installs both langpa and langpa-validation-tools
```

### As Standalone Package (Future)

```bash
pip install langpa-validation-tools
```

## CLI Usage

The package provides a `langpa-validate` command with several subcommands:

### Compare Runs

Compare gene programs across multiple DeepSearch runs:

```bash
langpa-validate compare --project glioblastoma_ds_auto
```

Options:
- `--project`: Project name (directory under outputs/)
- `--output-dir`: Base output directory (default: outputs/)
- `--embeddings`: Path to pre-generated embeddings (optional)
- `--threshold`: Minimum similarity threshold (default: 0.3)

### Generate Embeddings

Generate embeddings for program names:

```bash
langpa-validate embed \
  --project glioblastoma_ds_auto \
  --type programs \
  --output embeddings/
```

Options:
- `--project`: Project name
- `--type`: Type of embeddings (programs or components)
- `--output`: Output directory for embeddings
- `--components-file`: Component mapping CSV (for --type components)

### Create Visualizations

Generate heatmaps and bubble plots:

```bash
langpa-validate visualize \
  --project glioblastoma_ds_auto \
  --matches program_matches.csv \
  --output heatmaps/
```

Options:
- `--project`: Project name
- `--matches`: Path to program matches CSV
- `--output`: Output directory (default: heatmaps/)

### Generate Master Report

Create a comprehensive validation report:

```bash
langpa-validate report \
  --project glioblastoma_ds_auto \
  --matches program_matches.csv \
  --output master_report.md
```

Options:
- `--project`: Project name
- `--matches`: Path to program matches CSV
- `--output`: Output file path (default: master_report.md)

### Run Full Pipeline

Execute the complete validation workflow:

```bash
langpa-validate pipeline \
  --project glioblastoma_ds_auto \
  --use-embeddings
```

Options:
- `--project`: Project name
- `--use-embeddings`: Generate and use embeddings for name similarity
- `--output-dir`: Base output directory (default: outputs/)

## Python API Usage

You can also use the modules directly in Python:

```python
from langpa_validation_tools.comparison import compute_gene_jaccard, match_programs
from langpa_validation_tools.embeddings import EmbeddingGenerator

# Compare gene sets
jaccard = compute_gene_jaccard(["TP53", "BRCA1"], ["TP53", "EGFR"])
# Returns: 0.333 (1 overlap / 3 total)

# Match programs between two runs
matches = match_programs(programs_a, programs_b, threshold=0.3)

# Generate embeddings
gen = EmbeddingGenerator()
embedding = gen.generate_embedding("DNA Repair")
# Returns: list of 3072 floats (text-embedding-3-large)
```

## Development Status

### Phase 1: Core Functionality ✅ COMPLETE
- ✅ Comparison metrics (Jaccard, name similarity, combined)
- ✅ Program matching algorithm
- ✅ Embedding generation and caching
- ✅ Cosine similarity utilities
- ✅ All tests passing (31 unit tests)

### Phase 2: CLI and Package Setup ✅ COMPLETE
- ✅ Package structure
- ✅ CLI entry point with all subcommands
- ✅ Dependencies configured
- ✅ README documentation

### Phase 3: Run Comparison ✅ COMPLETE
- ✅ Orchestration logic
- ✅ CSV output generation
- ✅ Integration with OutputManager
- ✅ Compare CLI command functional
- ✅ All tests passing (4 unit + 1 integration)

### Phase 4: Heatmap Generation ✅ COMPLETE
- ✅ Bubble plots
- ✅ Confusion matrices
- ✅ Visualization CLI command functional
- ✅ Per-query filtering
- ✅ All tests passing (5 unit + 3 integration)

### Phase 5: Embedding Workflow ✅ COMPLETE
- ✅ Batch embedding generation
- ✅ Embed CLI command functional
- ✅ Program name extraction from containers
- ✅ Caching to CSV + NPY format
- ✅ All tests passing (4 unit tests)

### Phase 6: Master Report ✅ COMPLETE
- ✅ Report generation with per-query sections
- ✅ Integration with langpa markdown reports
- ✅ Full pipeline command (compare → visualize → report)
- ✅ All CLI commands functional

## Dependencies

- **langpa**: Core DeepSearch functionality (workspace dependency)
- **openai**: Embedding generation
- **numpy**: Numerical operations
- **pandas**: Data manipulation (Phase 3+)
- **matplotlib**: Visualization (Phase 4+)
- **scipy**: Scientific computing (Phase 4+)

## Requirements

- Python 3.11+
- OpenAI API key (for embeddings)

## Environment Variables

```bash
# Required for embedding generation
export OPENAI_API_KEY=your-key-here

# Optional: specify embedding model
export OPENAI_EMBEDDING_MODEL=text-embedding-3-large  # default
```

## Testing

Run unit tests:
```bash
cd langpa_validation_tools
uv run pytest -m unit
```

Run integration tests (requires OPENAI_API_KEY):
```bash
uv run pytest -m integration
```

## Contributing

This package follows the development workflow defined in the main langpa repository:
- TDD (Test-Driven Development)
- Google-style docstrings
- RST syntax in docstrings
- 80%+ test coverage requirement

## License

Same as langpa (see main repository)
