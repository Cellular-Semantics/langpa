# Test Outputs

This directory contains saved outputs from integration tests for inspection and debugging.

## Purpose

Integration tests make real API calls which are expensive and time-consuming. The `--save-outputs` flag allows you to save these responses for later inspection without re-running tests.

## Usage

### Saving Test Outputs

Run integration tests with the `--save-outputs` flag:

```bash
# Save outputs from all integration tests
pytest -m integration --save-outputs

# Save outputs from specific test file
pytest tests/integration/test_pydantic_validation_e2e.py --save-outputs

# Save outputs from specific test
pytest tests/integration/test_pydantic_validation_e2e.py::test_deepsearch_pydantic_validation_e2e --save-outputs
```

### Running Without Saving

By default, tests run normally without saving outputs:

```bash
# No outputs saved (default behavior)
pytest -m integration
```

## Directory Structure

Outputs are organized by test file and test name with timestamps:

```
test_outputs/
└── integration/
    ├── deepsearch_service_integration/
    │   ├── test_deepsearch_service_preset_integration_20231209_143052/
    │   │   ├── raw_response.json
    │   │   └── extracted_json.json
    │   └── test_deepsearch_service_backward_compatibility_20231209_143105/
    │       └── raw_response.json
    └── pydantic_validation_e2e/
        ├── test_deepsearch_pydantic_validation_e2e_20231209_143210/
        │   ├── raw_response.json
        │   ├── extracted_json.json
        │   └── validation_result.json
        └── test_deepsearch_pydantic_validation_with_moderate_genes_20231209_143245/
            ├── raw_response.json
            ├── extracted_json.json
            └── validation_result.json
```

### Output Files

Each test run creates up to 3 JSON files:

#### 1. `raw_response.json`

Contains the full API response with metadata:

```json
{
  "test_context": {
    "genes": ["TMEM14E"],
    "context": "cells",
    "preset": "perplexity-sonar-pro"
  },
  "response": {
    "markdown": "# Research Results\n\n...",
    "citations": [
      {
        "source_id": "1",
        "notes": "PubMed article..."
      }
    ],
    "provider": "perplexity",
    "model": "sonar-reasoning-pro",
    "duration_seconds": 45.2
  },
  "saved_at": "2023-12-09T14:32:10.123456"
}
```

#### 2. `extracted_json.json` (when available)

Contains the extracted and parsed JSON from the API response:

```json
{
  "context": {
    "cell_type": "cells",
    "disease": "",
    "tissue": ""
  },
  "input_genes": ["TMEM14E"],
  "programs": [
    {
      "program_name": "Example Program",
      "description": "Program description",
      "atomic_biological_processes": [],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": []
    }
  ],
  "version": "1.0"
}
```

#### 3. `validation_result.json` (when available)

Contains pydantic validation metadata:

```json
{
  "success": true,
  "retry_count": 0,
  "validation_time_ms": 12.5,
  "error": null
}
```

## Use Cases

### 1. Debug Validation Failures

When a test fails validation, inspect the saved outputs:

```bash
# Run test with output saving
pytest tests/integration/test_pydantic_validation_e2e.py::test_deepsearch_pydantic_validation_e2e --save-outputs

# Inspect the extracted JSON
cat test_outputs/integration/pydantic_validation_e2e/test_deepsearch_pydantic_validation_e2e_*/extracted_json.json | jq .

# Check validation errors
cat test_outputs/integration/pydantic_validation_e2e/test_deepsearch_pydantic_validation_e2e_*/validation_result.json | jq .
```

### 2. Compare API Responses

Save outputs from different test runs to compare:

```bash
# Run with different presets
pytest tests/integration/test_deepsearch_service_integration.py --save-outputs

# Compare responses
diff test_outputs/integration/deepsearch_service_integration/test_*_preset_*/raw_response.json
```

### 3. Inspect Citations

Review citation quality without re-running expensive API calls:

```bash
# Extract citations from saved output
cat test_outputs/integration/*/test_*/raw_response.json | jq '.response.citations'
```

### 4. Performance Analysis

Analyze API response times:

```bash
# Extract duration from all saved outputs
find test_outputs -name "raw_response.json" -exec jq -r '.response.duration_seconds' {} \;
```

## Notes

- Outputs are **NOT committed to git** (excluded via `.gitignore`)
- Each test run creates a **new timestamped directory** (outputs never overwrite)
- Directory is **only created when `--save-outputs` is used**
- Test performance is **not impacted** when flag is not used
- Outputs contain **real API responses** - do not commit if they contain sensitive data

## Implementation Details

The output saving infrastructure consists of:

- **`tests/utils/test_output_saver.py`**: Core utility class for saving outputs
- **`tests/conftest.py`**: Pytest fixtures providing the `save_test_output` function
- **Integration tests**: Updated to call `save_test_output()` when fixture is available

See `tests/unit/test_output_saver.py` for unit tests of the output saving infrastructure.
