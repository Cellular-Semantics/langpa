# Perplexity DeepSearch Integration Implementation Plan

## Overview
Implement a Perplexity DeepSearch service that takes gene lists and context as input, processes them through the DeepSearch API, and validates outputs against the existing schema at `src/langpa/schemas/deepsearch_results_schema.json`.

## Phase 1: Core DeepSearch Integration (Current PR)

### Step 1: Planning & Setup ✅
- [x] Create `planning/` directory
- [x] Write comprehensive implementation plan to `planning/deepsearch-integration.md`
- [ ] Create feature branch: `feature/perplexity-deepsearch-integration`

### Step 2: Early API Testing (Priority: High)
**Goal**: Validate API connectivity and response format before building complex logic

**Implementation**:
- Write integration tests FIRST using cheaper Perplexity calls
- Test DeepSearch client integration from `deep-research-client`
- Validate response format matches expected markdown structure
- Ensure API keys work and rate limits are understood

**Files**:
- `tests/integration/test_deepsearch_api.py`

**Deliverable**: Working API connection with real response samples

### Step 3: Core Service Implementation (TDD)
**Goal**: Basic gene list + context → API call functionality

**Implementation**:
- Write unit tests for service interface
- Implement `src/langpa/services/deepsearch_service.py`
- Use prompt template from cellsem-agent reference
- Handle API errors gracefully

**Files**:
- `tests/unit/test_deepsearch_service.py`
- `src/langpa/services/deepsearch_service.py`

**Deliverable**: Service class that makes API calls with proper error handling

### Step 4: Response Parser
**Goal**: Extract structured components from DeepSearch markdown response

**Implementation**:
- Write unit tests for markdown parsing logic
- Implement `src/langpa/services/deepsearch_parser.py`
- Extract components:
  - Input prompt
  - JSON results block
  - References list (IDs + URLs)
- Handle malformed responses gracefully

**Files**:
- `tests/unit/test_deepsearch_parser.py`
- `src/langpa/services/deepsearch_parser.py`

**Deliverable**: Parser that reliably extracts structured data from markdown

### Step 5: Basic Schema Validation
**Goal**: Validate parsed JSON against existing schema (NO correction yet)

**Implementation**:
- Simple validation against `deepsearch_results_schema.json`
- Clear error messages for validation failures
- **NO schema correction** in this phase
- Fail gracefully with detailed error info

**Files**:
- `tests/unit/test_schema_validation.py`
- `src/langpa/services/schema_validator.py`

**Deliverable**: Robust validation with clear failure reporting

### Step 6: Output Management
**Goal**: Structured file storage outside src/

**Implementation**:
- Save results to `outputs/` directory structure
- File naming: `deepsearch_YYYYMMDD_HHMMSS.json`
- Include metadata: timestamp, input genes, context, validation status
- Handle file system errors

**Files**:
- `tests/unit/test_output_manager.py`
- `src/langpa/services/output_manager.py`

**Deliverable**: Organized output storage with metadata

### Step 7: End-to-End Integration
**Goal**: Complete workflow testing

**Implementation**:
- Integration tests with real DeepSearch API calls (limited due to cost)
- Full workflow: gene list → API → parse → validate → save
- Performance and error handling validation

**Files**:
- `tests/integration/test_deepsearch_workflow.py`

**Deliverable**: Working end-to-end pipeline

## Phase 2: Agentic Schema Correction (Future PR)

### Goals
- LLM-based error detection and correction
- Retry logic with cheaper models (`cellsem_llm_client`)
- Advanced validation strategies
- Self-healing schema compliance

### Why Separate Phase
- Keeps Phase 1 focused on core functionality
- Allows testing and validation of base system first
- Schema correction adds complexity that could mask basic integration issues
- Enables iterative improvement of correction strategies

## Implementation Guidelines

### TDD Workflow (Mandatory)
1. Write failing tests FIRST
2. Implement minimal code to pass tests
3. Refactor while keeping tests green
4. Commit tests before implementation

### Quality Requirements
- 80% test coverage minimum
- Unit tests: `@pytest.mark.unit`
- Integration tests: `@pytest.mark.integration`
- Real API keys required for integration tests
- Run quality checks: `uv run ruff format`, `uv run ruff check --fix`, `uv run mypy`

### Review Points
- **Pause after each step** for manual review
- Validate API connectivity early (Step 2)
- Ensure schema compliance before moving to outputs
- Test error handling thoroughly

### API Cost Management
- Use cheaper Perplexity calls for most testing
- Limit expensive DeepSearch calls to final validation
- Mock responses for unit tests
- Cache responses during development when possible

## Risk Assessment

### Technical Risks
- **API costs during development**: Mitigated by using cheaper endpoints for testing
- **Schema complexity**: Addressed by simple validation first, correction later
- **Network timeouts**: Handled with retries and graceful failures
- **Prompt compatibility**: Validated early with real API calls

### Mitigation Strategies
- Early API testing to catch integration issues
- Comprehensive error handling at each step
- Separation of concerns (parsing, validation, output as separate modules)
- Extensive unit test coverage for offline development