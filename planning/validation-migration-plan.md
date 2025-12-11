# LangPA Validation Migration Plan

**REVISED PLAN - Monorepo Abandoned**

## Executive Summary

Migrate comparison and embedding functionality from `langpa_validation_tools` into the langpa ecosystem while keeping them as separate packages. Use langpa's existing markdown report generation for individual runs, and migrate master report generation to use langpa outputs.

**Timeline**: 8-10 days
**Approach**: Incremental migration with separate package architecture
**Key Change**: Abandon Makefile workflow, implement pure Python CLI

---

## Architecture Decision

### Package Structure

**Two separate packages:**
1. **langpa** (existing, enhanced)
   - Existing: DeepSearch API integration, markdown report generation, output management
   - New: Comparison utilities, embedding support, validation entry points

2. **langpa-validation** (new package, replaces langpa_validation_tools)
   - Depends on langpa (imports langpa.comparison, langpa.embeddings)
   - Pure Python CLI for validation workflows
   - Analysis and master report generation

### Benefits

- Clean separation: langpa = core functionality, langpa-validation = analysis layer
- Independent versioning and releases
- Users can install langpa alone or langpa + langpa-validation
- Easier maintenance and testing

---

## Output Structure (Langpa's Current System)

Using langpa's existing output organization:

```
outputs/
└── <project>/              # e.g., glioblastoma_ds_auto
    └── <query>/            # e.g., 0_Gliosis, 14_OPC_AC_like_2
        └── <timestamp>/    # e.g., 20251209_175141
            ├── deepsearch_raw.json          # Raw API response + metadata
            ├── deepsearch_structured.json   # Validated schema-compliant JSON
            ├── deepsearch_container.json    # Full package with citations
            └── deepsearch_<timestamp>.md    # Markdown report (langpa generates)
```

**Validation tools will:**
- Read from `outputs/<project>/<query>/*/deepsearch_container.json`
- Write analysis results to `outputs/<project>/analysis/`
- Write master report to `outputs/<project>/master_report.md`

---

## Functionality Migration Map

### MIGRATE TO LANGPA

| Functionality | Source File | Destination in langpa | Rationale |
|---------------|-------------|----------------------|-----------|
| **Similarity Metrics** | `process_deepsearch.py` | `src/langpa/comparison/metrics.py` | Core reusable utilities |
| **Program Matching** | `process_deepsearch.py` | `src/langpa/comparison/matching.py` | Algorithm logic |
| **Embedding Support** | `embed_*.py` | `src/langpa/embeddings/` | Core feature |
| **Comparison Data Models** | N/A (new) | `src/langpa/comparison/models.py` | Pydantic models for type safety |

### MIGRATE TO LANGPA-VALIDATION

| Functionality | Source File | Destination | Rationale |
|---------------|-------------|-------------|-----------|
| **Master Report** | `build_master_report.py` | `src/langpa_validation/reporting/master_report.py` | Analysis-specific |
| **Run Comparison** | `process_deepsearch.py` | `src/langpa_validation/analysis/run_comparison.py` | Uses langpa.comparison |
| **Heatmaps** | `generate_heatmaps.py` | `src/langpa_validation/visualization/heatmaps.py` | Analysis visualization |
| **Python CLI** | N/A (new) | `src/langpa_validation/cli.py` | Entry point |

### DO NOT MIGRATE (Excluded)

- GO coverage analysis (`plot_go_coverage()`)
- GO enrichment comparisons (`process_comparisons.py`)
- Table S10 spreadsheet parsing
- All Makefile infrastructure

---

## Implementation Phases

### Phase 1: Langpa Enhancements (Days 1-3)

**Goal**: Add comparison and embedding support to langpa

**Tasks**:

1. **Create `langpa/comparison/` module**
   - `metrics.py`: Gene Jaccard, name similarity, combined similarity
   - `matching.py`: Greedy program matching algorithm
   - `models.py`: Pydantic models (ProgramPair, SimilarityScores, etc.)

2. **Create `langpa/embeddings/` module**
   - `generator.py`: OpenAI embedding API wrapper
   - `loader.py`: Load/save embeddings with caching
   - `similarity.py`: Cosine similarity, rescaling utilities

3. **Update `langpa/services/output_manager.py`**
   - Add method to list container files for a project
   - Add method to load multiple runs for comparison

4. **Add tests**
   - Unit tests for similarity metrics
   - Unit tests for embedding utilities
   - Integration tests for embedding API (requires OPENAI_API_KEY)

**Deliverables**:
- `src/langpa/comparison/{metrics,matching,models}.py`
- `src/langpa/embeddings/{generator,loader,similarity}.py`
- `tests/unit/test_comparison_metrics.py`
- `tests/unit/test_embeddings.py`
- `tests/integration/test_embedding_generation.py`

---

### Phase 2: Langpa-Validation Package Setup (Days 4-5)

**Goal**: Create new langpa-validation package structure

**Tasks**:

1. **Create package structure**
   ```
   langpa-validation/
   ├── pyproject.toml
   ├── README.md
   ├── src/
   │   └── langpa_validation/
   │       ├── __init__.py
   │       ├── cli.py                    # Main CLI entry point
   │       ├── analysis/
   │       │   ├── __init__.py
   │       │   └── run_comparison.py     # Run comparison orchestration
   │       ├── visualization/
   │       │   ├── __init__.py
   │       │   └── heatmaps.py           # Bubble plots, confusion matrices
   │       └── reporting/
   │           ├── __init__.py
   │           └── master_report.py      # Master report generation
   └── tests/
       ├── unit/
       └── integration/
   ```

2. **Create `pyproject.toml`**
   - Depends on langpa (via pip or git URL)
   - Additional deps: pandas, numpy, matplotlib, scipy, openai
   - Entry point: `langpa-validate` command

3. **Create stub CLI** (`cli.py`)
   - Subcommands: `compare`, `embed`, `report`
   - Use argparse or click

4. **Create README.md**
   - Installation instructions
   - Basic usage examples
   - Dependency on langpa

**Deliverables**:
- Complete package structure
- `pyproject.toml` with correct dependencies
- Stub CLI with command structure
- README with getting started guide

---

### Phase 3: Migrate Run Comparison (Days 6-7)

**Goal**: Migrate run comparison functionality

**Tasks**:

1. **Implement `analysis/run_comparison.py`**
   ```python
   from langpa.comparison import compute_similarity, match_programs
   from langpa.embeddings import load_embeddings
   from langpa.services.output_manager import list_containers

   def compare_runs(project: str, output_dir: Path) -> pd.DataFrame:
       """Compare all runs in a project, return matches DataFrame."""
       # Load all container JSONs
       # Compute similarities using langpa.comparison
       # Generate CSV outputs
   ```

2. **Port similarity algorithm**
   - Use langpa's metrics (already implemented in Phase 1)
   - Add greedy matching logic
   - Output: `program_matches.csv`, `unmatched_programs.csv`

3. **Implement embedding integration**
   - Load pre-generated embeddings (if available)
   - Compute name similarity using embeddings
   - Fallback to token-based similarity

4. **Add CLI command**: `langpa-validate compare`
   ```bash
   langpa-validate compare --project glioblastoma_ds_auto \
     --output-dir outputs/glioblastoma_ds_auto
   ```

5. **Write tests**
   - Unit tests for comparison logic
   - Integration test with sample outputs

**Deliverables**:
- `src/langpa_validation/analysis/run_comparison.py`
- CLI `compare` subcommand
- Tests for run comparison
- Sample output CSVs

---

### Phase 4: Migrate Heatmap Generation (Day 7)

**Goal**: Port bubble plot and confusion matrix generation

**Tasks**:

1. **Implement `visualization/heatmaps.py`**
   - `generate_bubble_plot(matches_df, output_path)`: Scatter plot with bubble sizes
   - `generate_confusion_matrix(embeddings, labels, output_path)`: Heatmap with clustering

2. **Port matplotlib code**
   - Bubble plot: program pairs with gene overlap size, similarity color
   - Confusion matrix: cosine similarity heatmap with dendrograms

3. **Add CLI command**: `langpa-validate visualize`
   ```bash
   langpa-validate visualize --project glioblastoma_ds_auto \
     --matches program_matches.csv \
     --output heatmaps/
   ```

4. **Tests**
   - Unit test for plot generation (mock matplotlib)
   - Integration test generates actual PNGs

**Deliverables**:
- `src/langpa_validation/visualization/heatmaps.py`
- CLI `visualize` subcommand
- Tests for visualization

---

### Phase 5: Migrate Embedding Workflow (Day 8)

**Goal**: Implement embedding generation workflow

**Tasks**:

1. **Leverage langpa's embedding module**
   - Already created in Phase 1
   - Wrap for CLI convenience

2. **Add CLI command**: `langpa-validate embed`
   ```bash
   # Embed program names
   langpa-validate embed --project glioblastoma_ds_auto \
     --type programs \
     --output embeddings/

   # Embed component names
   langpa-validate embed --project glioblastoma_ds_auto \
     --type components \
     --components-file component_mapping.csv \
     --output embeddings/
   ```

3. **Implement batch embedding**
   - Read program names from container JSONs
   - Batch API calls (efficient token usage)
   - Cache embeddings as `embeddings_index.csv` + `embeddings_name.npy`

4. **Tests**
   - Mock OpenAI API for unit tests
   - Integration test with real API (requires key)

**Deliverables**:
- `langpa-validate embed` CLI command
- Embedding cache infrastructure
- Tests for embedding workflow

---

### Phase 6: Migrate Master Report (Days 9-10)

**Goal**: Port master report generation using langpa's markdown reports

**Tasks**:

1. **Implement `reporting/master_report.py`**
   ```python
   from langpa.services.markdown_reporter import MarkdownReportGenerator

   def build_master_report(
       project: str,
       matches_df: pd.DataFrame,
       output_path: Path
   ) -> None:
       """Generate master report aggregating all runs."""
       # Load individual markdown reports (generated by langpa)
       # Add comparison tables
       # Add bubble plots
       # Write master_report.md
   ```

2. **Master report structure**
   ```markdown
   # Project: glioblastoma_ds_auto

   ## Summary
   [User-provided intro if available]

   ## Analysis Overview
   - Total runs: X
   - Total programs: Y
   - Matched programs: Z

   ## Per-Query Analysis

   ### Query: 0_Gliosis

   #### Comparison Table
   | Run A | Run B | Program A | Program B | Gene Jaccard | Name Sim | Combined |
   |-------|-------|-----------|-----------|--------------|----------|----------|
   | ...   | ...   | ...       | ...       | ...          | ...      | ...      |

   #### Bubble Plot
   ![](analysis/heatmaps/0_Gliosis_bubble.png)

   #### Individual Run Reports
   - [Run 1](0_Gliosis/20251209_175141/deepsearch_20251209_175141.md)
   - [Run 2](0_Gliosis/20251210_093022/deepsearch_20251210_093022.md)
   ```

3. **Use langpa's markdown reports**
   - Link to individual run markdown files
   - Do NOT regenerate them
   - Master report references existing `.md` files

4. **Add CLI command**: `langpa-validate report`
   ```bash
   langpa-validate report --project glioblastoma_ds_auto \
     --matches program_matches.csv \
     --output master_report.md
   ```

5. **Tests**
   - Unit test for report structure
   - Integration test generates full report

**Deliverables**:
- `src/langpa_validation/reporting/master_report.py`
- CLI `report` subcommand
- Sample master report
- Tests for master report

---

## Python CLI Design

### Command Structure

```bash
# Main command
langpa-validate --help

# Subcommands
langpa-validate compare --project <name> [--embeddings <path>]
langpa-validate embed --project <name> --type {programs,components}
langpa-validate visualize --project <name> --matches <csv>
langpa-validate report --project <name> --matches <csv>

# Full pipeline (convenience)
langpa-validate pipeline --project <name> [--use-embeddings]
```

### Implementation (cli.py)

```python
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        prog="langpa-validate",
        description="Validation and analysis tools for LangPA outputs"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Compare command
    compare_parser = subparsers.add_parser("compare", help="Compare runs")
    compare_parser.add_argument("--project", required=True)
    compare_parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    compare_parser.add_argument("--embeddings", type=Path)

    # Embed command
    embed_parser = subparsers.add_parser("embed", help="Generate embeddings")
    embed_parser.add_argument("--project", required=True)
    embed_parser.add_argument("--type", choices=["programs", "components"], required=True)
    embed_parser.add_argument("--output", type=Path, required=True)

    # Visualize command
    viz_parser = subparsers.add_parser("visualize", help="Generate visualizations")
    viz_parser.add_argument("--project", required=True)
    viz_parser.add_argument("--matches", type=Path, required=True)
    viz_parser.add_argument("--output", type=Path, default=Path("heatmaps"))

    # Report command
    report_parser = subparsers.add_parser("report", help="Generate master report")
    report_parser.add_argument("--project", required=True)
    report_parser.add_argument("--matches", type=Path, required=True)
    report_parser.add_argument("--output", type=Path, default=Path("master_report.md"))

    # Pipeline command (convenience)
    pipeline_parser = subparsers.add_parser("pipeline", help="Run full pipeline")
    pipeline_parser.add_argument("--project", required=True)
    pipeline_parser.add_argument("--use-embeddings", action="store_true")

    args = parser.parse_args()

    if args.command == "compare":
        from langpa_validation.analysis.run_comparison import compare_runs
        compare_runs(args.project, args.output_dir, args.embeddings)

    elif args.command == "embed":
        from langpa_validation.analysis.embedding_workflow import generate_embeddings
        generate_embeddings(args.project, args.type, args.output)

    elif args.command == "visualize":
        from langpa_validation.visualization.heatmaps import generate_visualizations
        generate_visualizations(args.project, args.matches, args.output)

    elif args.command == "report":
        from langpa_validation.reporting.master_report import build_master_report
        build_master_report(args.project, args.matches, args.output)

    elif args.command == "pipeline":
        run_full_pipeline(args.project, args.use_embeddings)

if __name__ == "__main__":
    main()
```

---

## Dependencies

### Langpa (Enhanced)

**New dependencies**:
- None (uses existing: pydantic, jsonschema, openai, python-dotenv)

**New modules**:
- `langpa.comparison.*`
- `langpa.embeddings.*`

### Langpa-Validation (New Package)

**Dependencies**:
```toml
[project]
dependencies = [
    "langpa",  # Core dependency
    "pandas>=2.0.0",
    "numpy>=1.24.0",
    "matplotlib>=3.7.0",
    "scipy>=1.10.0",
    "openai>=1.0.0",
]
```

**Python version**: 3.11+ (match langpa)

---

## Testing Strategy

### Langpa Tests

**Unit tests** (new):
- `tests/unit/test_comparison_metrics.py`: Jaccard, name similarity, combined
- `tests/unit/test_comparison_matching.py`: Greedy matching algorithm
- `tests/unit/test_embeddings_similarity.py`: Cosine, rescaling
- `tests/unit/test_embeddings_loader.py`: Cache load/save

**Integration tests** (new):
- `tests/integration/test_embedding_api.py`: Real OpenAI API calls

### Langpa-Validation Tests

**Unit tests**:
- `tests/unit/test_run_comparison.py`: Comparison orchestration logic
- `tests/unit/test_heatmaps.py`: Plot generation (mocked matplotlib)
- `tests/unit/test_master_report.py`: Report structure

**Integration tests**:
- `tests/integration/test_full_pipeline.py`: End-to-end with sample data

---

## Migration Checklist

### Phase 1: Langpa Enhancements
- [ ] Create `src/langpa/comparison/metrics.py`
- [ ] Create `src/langpa/comparison/matching.py`
- [ ] Create `src/langpa/comparison/models.py`
- [ ] Create `src/langpa/embeddings/generator.py`
- [ ] Create `src/langpa/embeddings/loader.py`
- [ ] Create `src/langpa/embeddings/similarity.py`
- [ ] Update `output_manager.py` with list/load methods
- [ ] Write unit tests for comparison
- [ ] Write unit tests for embeddings
- [ ] Write integration test for embedding API

### Phase 2: Package Setup
- [ ] Create langpa-validation directory structure
- [ ] Create `pyproject.toml`
- [ ] Create stub `cli.py`
- [ ] Create README.md
- [ ] Set up tests/ structure

### Phase 3: Run Comparison
- [ ] Implement `analysis/run_comparison.py`
- [ ] Add `compare` CLI subcommand
- [ ] Port similarity algorithms
- [ ] Integrate embeddings
- [ ] Write tests

### Phase 4: Heatmaps
- [ ] Implement `visualization/heatmaps.py`
- [ ] Add `visualize` CLI subcommand
- [ ] Port bubble plot code
- [ ] Port confusion matrix code
- [ ] Write tests

### Phase 5: Embeddings
- [ ] Add `embed` CLI subcommand
- [ ] Implement batch embedding
- [ ] Set up caching
- [ ] Write tests

### Phase 6: Master Report
- [ ] Implement `reporting/master_report.py`
- [ ] Add `report` CLI subcommand
- [ ] Integrate langpa markdown reports
- [ ] Add comparison tables
- [ ] Add bubble plot references
- [ ] Write tests

### Final Integration
- [ ] Test full pipeline end-to-end
- [ ] Update langpa README (mention validation package)
- [ ] Update langpa-validation README (complete examples)
- [ ] Create migration guide from old Makefile workflow

---

## File Mapping Reference

### From validation_tools → langpa

| Source | Destination | Lines | Purpose |
|--------|-------------|-------|---------|
| `process_deepsearch.py:144-170` | `langpa/comparison/metrics.py` | ~50 | Similarity metrics |
| `process_deepsearch.py:230-280` | `langpa/comparison/matching.py` | ~60 | Greedy matching |
| `embed_programs.py` | `langpa/embeddings/generator.py` | ~80 | Embedding generation |
| `embed_programs.py:load` | `langpa/embeddings/loader.py` | ~40 | Cache management |

### From validation_tools → langpa-validation

| Source | Destination | Lines | Purpose |
|--------|-------------|-------|---------|
| `build_master_report.py` | `langpa_validation/reporting/master_report.py` | ~200 | Master report |
| `generate_heatmaps.py` | `langpa_validation/visualization/heatmaps.py` | ~150 | Visualizations |
| `process_deepsearch.py:main` | `langpa_validation/analysis/run_comparison.py` | ~100 | Orchestration |

---

## Success Criteria

### MVP Success (End of Phase 6)

- [ ] `langpa.comparison` module fully functional with tests
- [ ] `langpa.embeddings` module fully functional with tests
- [ ] `langpa-validation` package installable via pip
- [ ] All 4 CLI subcommands working (compare, embed, visualize, report)
- [ ] Sample project processed end-to-end
- [ ] Master report generated successfully
- [ ] All tests passing (unit + integration)

### Full Success

- [ ] Migration guide published
- [ ] Documentation updated
- [ ] Test coverage >80%
- [ ] Performance benchmarks validated
- [ ] User feedback collected

---

## Risk Mitigation

### Risk 1: Embedding API Costs

**Risk**: Generating embeddings for all programs could be expensive

**Mitigation**:
- Implement caching (already planned)
- Batch API calls for efficiency
- Make embeddings optional (fallback to token-based similarity)
- Add `--dry-run` flag to estimate costs
- **Note**: Cost should be minimal for program name strings only

### Risk 2: Breaking Changes in Langpa

**Risk**: Langpa's output format might change

**Mitigation**:
- Use schema validation
- Version langpa-validation with langpa version constraints
- Add compatibility tests

### Risk 3: Complex Master Report Logic

**Risk**: Master report aggregation could be fragile

**Mitigation**:
- Start simple (basic tables + links)
- Add features incrementally
- Extensive integration testing with real data
- Keep report generation pure (no side effects)

---

## Summary

This plan migrates core validation functionality into the langpa ecosystem while maintaining clean separation between packages. The pure Python CLI approach provides better cross-platform support and easier maintenance than Make. Using langpa's existing markdown report generation for individual runs eliminates code duplication and ensures consistency.

**Key Principles**:
- Separate packages with clear responsibilities
- Reuse langpa's output structure and markdown generation
- Pure Python for better maintainability
- Incremental migration with tests at each phase
- No monorepo complexity
- Follow langpa's TDD development rules (CLAUDE.md)
- Do not modify files in langpa_validation_tools repository
