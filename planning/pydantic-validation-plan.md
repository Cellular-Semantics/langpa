# Pydantic-based DeepSearch validation plan (using SchemaValidator.validate_with_retry)

## Goals
- Replace jsonschema validation with `cellsem_llm_client.schema.validators.SchemaValidator` and a Pydantic model for DeepSearch results.
- Leverage retry/cleanup to handle common LLM formatting issues.
- Keep visibility into retries and validation time.

## Steps
1) Pydantic model
   - Implement a Pydantic model mirroring `deepsearch_results_schema.json` (source_id-only citations; citations arrays in programs/atomic terms; `atomic_term.citations` required).
   - Place in a suitable module (e.g., `schemas/` or `services/validators.py`).

2) Validator wrapper
   - Add a helper (e.g., `DeepSearchValidator`) that:
     - Accepts markdown/JSON text and runs `SchemaValidator.validate_with_retry` against the Pydantic model.
     - Applies existing cleanup (strip fences, pick post-`</think>`, remove `$schema`) before validation.
     - Optionally supplies a custom retry handler for common fixes (minimal; avoid auto-filling missing required fields unless intentional).
     - Returns success flag, validated dict (`model_instance`), errors, and `retry_count`.

3) Integrate into OutputManager
   - Swap `validate_against_schema` to use the validator wrapper instead of `jsonschema`.
   - Feed the raw JSON string (post-extraction) to the validator; on success, use the validated dict for saving/containers.
   - Record `retry_count` and `validation_time_ms` in structured/metadata for observability.
   - Optional feature flag to fall back to `jsonschema` if needed.

4) Retry strategy
   - Cleanup before first attempt: strip code fences, select post-`</think>` JSON, drop `$schema`.
   - Configure `max_retries` (e.g., 2–3); allow custom handler injection if needed.

5) Tests
   - Unit: valid payload passes; malformed JSON with fences/prose is fixed by cleanup+retry; missing required fields fail cleanly with error info.
   - Integration-style: run `process_and_save_structured_output` on sample markdown with post-`</think>` JSON; ensure validated structured file is written and retries are reported.

6) Compatibility
   - Keep an optional toggle to use legacy `jsonschema` validation if needed; default to Pydantic + SchemaValidator with retry.
