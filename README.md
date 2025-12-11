# LangPA

[![Tests](https://github.com/Cellular-Semantics/langpa/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/Cellular-Semantics/langpa/actions/workflows/test.yml)
[![Coverage](https://raw.githubusercontent.com/Cellular-Semantics/langpa/main/.github/badges/coverage.svg)](https://github.com/Cellular-Semantics/langpa/actions/workflows/test.yml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

LLM AgeNt for Gene Program Annotation

## 📦 Repository Structure

This repository uses a **UV workspace** containing two packages:

### 1. **[langpa](langpa/)** - Core DeepSearch Engine
The main LangPA package for gene program annotation and literature analysis.
- DeepSearch service integration
- Citation resolution and normalization
- Markdown report generation
- Output management and validation
- [📖 Full Documentation](langpa/README.md)

### 2. **[langpa-validation-tools](langpa_validation_tools/)** - Validation & Analysis Tools
Companion package for comparing and analyzing DeepSearch outputs across multiple runs.
- Program comparison with Jaccard similarity
- Semantic similarity using OpenAI embeddings
- Visualization (bubble plots, confusion matrices)
- Master validation reports
- CLI: `langpa-validate` command
- [📖 Full Documentation](langpa_validation_tools/README.md)

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Cellular-Semantics/langpa.git
cd langpa

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install both packages (langpa + langpa-validation-tools)
uv sync --dev

# Set up pre-commit hooks (optional but recommended)
uv run pre-commit install

# Use repo-provided git hooks for consistent checks
git config core.hooksPath .githooks
```

The UV workspace automatically installs both packages and links them together. The `langpa-validation-tools` package imports from `langpa` as a workspace dependency.

### Environment Setup

Create a `.env` file in the project root (never commit secrets). `cellsem_llm_client` automatically loads this file via `python-dotenv`, so once the keys are present you can rely on the client (and the rest of the stack) to access them without extra wiring:

```bash
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

As long as that `.env` file lives at the repo root, `cellsem_llm_client` (and the bootstrapping in `src/langpa`) will call `load_dotenv()` and expose those keys to agents, services, and tests automatically—no manual export required.

### Basic Usage

```python
from langpa import bootstrap

# Load environment + perform any required startup tasks
bootstrap()
```

## 📚 Documentation

Documentation lives in `docs/` and is built with Sphinx + MyST. Run `python scripts/check-docs.py` to build with warnings-as-errors before each commit. Publish the rendered HTML via GitHub Pages or your preferred static host.

## ✨ Current Features

- ✅ **Agentic workflow scaffold** with strict TDD guardrails (`CLAUDE.md`)
- ✅ **Unit & integration test suites** pre-configured with pytest markers
- ✅ **Docs + automation scripts** for Sphinx builds
- ✅ **Environment bootstrap** handled via `python-dotenv`
- ✅ **uv-first packaging** (`pyproject.toml` with Ruff, MyPy, pytest config)
- ✅ **Integrated clients**: [`cellsem_llm_client`](https://github.com/Cellular-Semantics/cellsem_llm_client) for LLMs and [`deep-research-client`](https://github.com/monarch-initiative/deep-research-client) for Deepsearch workflows
- ✅ **Pydantic AI graph orchestration**: `pydantic-ai` agent surfaces graph nodes safely with typed deps

## 🏗️ Architecture

This is a **UV workspace** with two packages:

```
langpa/                                    # Repository root
├── pyproject.toml                         # Workspace configuration
├── langpa/                                # Core package
│   ├── pyproject.toml                     # Core package config
│   ├── src/langpa/
│   │   ├── agents/                        # Agent classes coordinating workflows
│   │   ├── graphs/                        # Optional workflow graphs powered by Pydantic
│   │   ├── schemas/                       # Shared IO models and contracts
│   │   ├── services/                      # LLM + Deepsearch integration layers
│   │   └── utils/                         # Repo-specific tooling/helpers
│   └── tests/
│       ├── unit/                          # Fast, isolated tests
│       └── integration/                   # Real API + IO validation (no mocks)
├── langpa_validation_tools/               # Validation tools package
│   ├── pyproject.toml                     # Validation tools config
│   ├── src/langpa_validation_tools/
│   │   ├── analysis/                      # Run comparison & embedding workflows
│   │   ├── comparison/                    # Similarity metrics & matching
│   │   ├── embeddings/                    # OpenAI embedding generation
│   │   ├── visualization/                 # Heatmaps & bubble plots
│   │   ├── reporting/                     # Master report generation
│   │   └── cli.py                         # langpa-validate CLI
│   └── tests/
│       ├── unit/                          # Validation tools unit tests
│       └── integration/                   # Validation tools integration tests
├── docs/                                  # Sphinx configuration and content
└── scripts/                               # Tooling helpers (docs, CLI, etc.)
```

### Package Details

**langpa** - Core functionality:
- Agent entrypoints coordinating services and schemas
- Optional workflow graphs powered by Pydantic + pydantic-ai
- JSON Schema contracts describing outputs + business rules
- Concrete integrations (CellSem LLM client, Deepsearch)
- Citation resolution and markdown report generation

**langpa-validation-tools** - Analysis & validation:
- Comparison metrics (Jaccard, name similarity, embeddings)
- Batch embedding generation with caching
- Visualization generation (bubble plots, confusion matrices)
- Master validation reports aggregating multiple runs
- CLI interface for validation workflows

## DeepSearch CLI & Outputs

The CLI `scripts/run_deepsearch.py` supports live API runs and offline processing of saved DeepSearch markdown/raw JSON. Key flags:

- `--project` / `--query`: organize outputs under `outputs/<project>/<query>/<timestamp>/`.
- `--from-markdown` / `--raw-input`: process saved responses without calling the API.
- `--resolve-citations`: normalize/resolve citations via url2ref and write a container with CSL-JSON.
- `--citation-style`: citation style for compact bibliography (e.g., vancouver, apa, ieee, chicago). Default: vancouver.
- `--citation-locale`: locale for citation formatting (e.g., en-US, en-GB, de-DE). Default: en-US.
- `--batch-dir`: iterate query subfolders (e.g., `projects/<proj>/inputs/<query>/*`) and process each file as a separate query.

Output files per run (when validation succeeds) live under `outputs/<project>/<query>/<timestamp>/` and use fixed filenames (identity comes from the folder path):
- `deepsearch.json`: raw markdown + original citations + metadata.
- `deepsearch_structured.json`: parsed/validated DeepSearch report (source_id-only citations).
- `deepsearch_container.json`: structured report + citation map (CSL-JSON keyed by source_id) + stats + **compact bibliography strings**.
- `deepsearch_extracted_debug.json`: optional debug dump when `--debug-extraction` is used.

#### Compact Bibliography

When `--resolve-citations` is enabled, the container JSON includes human-readable compact reference strings alongside CSL-JSON:

```bash
python scripts/run_deepsearch.py \
  --genes TMEM14E \
  --context "cellular function" \
  --resolve-citations \
  --citation-style apa \
  --citation-locale en-GB
```

The container will include a `compact_bibliography` field:

```json
{
  "compact_bibliography": {
    "entries": [
      "[1] Author, A., & Author, B. (2024). Paper title. Journal Name, 123(4), 567-890.",
      "[2] Smith, J. et al. (2023). Another paper. Nature, 456, 123-456."
    ],
    "style": "apa",
    "locale": "en-GB",
    "renderer": "citeproc-py"
  }
}
```

Supported styles: vancouver, apa, ieee, chicago, and others supported by citeproc-py. See [docs/compact-references.md](docs/compact-references.md) for details.

### Graph Agents with pydantic-ai

```python
from langpa.graphs import WorkflowGraph, GraphNode, build_graph_agent, GraphDependencies

graph = WorkflowGraph(
    name="triage",
    entrypoint="collect",
    nodes=[
        GraphNode(id="collect", description="collect context", service="collect_service", next=["summarize"]),
        GraphNode(id="summarize", description="summarize findings", service="summary_service"),
    ],
)

agent = build_graph_agent()
result = agent.run_sync(
    "pick next node",
    deps=GraphDependencies(graph=graph),
    # optional additional instructions/payload
)
```

The `pydantic-ai` agent validates all outputs against `GraphNode`, while dependency injection hands it the validated `WorkflowGraph` for safe routing.

### JSON Schemas for Business Logic

```python
from jsonschema import validate
from langpa.schemas import load_schema

schema = load_schema("workflow_output.schema.json")
payload = {
    "status": "completed",
    "summary": "Gathered literature and synthesized insights.",
    "actions": [{"name": "deepsearch.query", "details": "Retrieved 25 documents"}],
}

validate(instance=payload, schema=schema)
```

Schemas stay in JSON so downstream services (Python, JS, workflows) can share the same contract without importing Pydantic models.

## 📋 Requirements

- **Python**: 3.11+
- **Dependencies**: Managed via `uv sync --dev`
- **API Keys**: OpenAI + Anthropic keys for integration tests (hard fail if missing)

## 🤝 Contributing

1. Follow the rules in `CLAUDE.md` (TDD-first, tests before code, dotenv usage)
2. Write failing tests, then implement the smallest fix
3. Keep coverage ≥80% and never skip failing tests
4. Run the full quality suite (Ruff, MyPy, pytest, docs) before pushing

### 🧪 Testing Strategy

- **Unit Tests** (`@pytest.mark.unit`): no network, deterministic, fast
- **Integration Tests** (`@pytest.mark.integration`): real APIs, fail hard if env vars missing
- **Coverage**: target ≥80%, monitored via the coverage badge (currently 94%)
- **CI Policy**: GitHub Actions runs only `uv run pytest -m unit`; run `uv run pytest -m integration` locally with real API keys before pushing
- **Hooks**: `.githooks/pre-commit` runs lint, unit tests, and integration tests (skips integration if API keys missing)

### Development Workflow

```bash
# Run tests for both packages
uv run pytest langpa/tests -m unit                          # langpa unit tests
uv run pytest langpa_validation_tools/tests -m unit         # validation tools unit tests
uv run pytest langpa/tests -m integration                   # langpa integration tests
uv run pytest langpa_validation_tools/tests -m integration  # validation tools integration tests

# Run all unit tests
uv run pytest langpa/tests/unit langpa_validation_tools/tests/unit -m unit

# Code quality
uv run ruff check --fix langpa/src/ langpa/tests/
uv run ruff format langpa/src/ langpa/tests/
uv run mypy langpa/src/

# Docs
python scripts/check-docs.py

# Validation tools CLI
uv run langpa-validate --help
uv run langpa-validate compare --project my_project
uv run langpa-validate pipeline --project my_project --use-embeddings
```

## 📄 License

MIT License - see `LICENSE` for details.
