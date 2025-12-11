# Markdown Report Generation Plan

## Goal
Generate deterministic Markdown reports from schema-compliant JSON outputs (DeepSearch gene program analyses) that mirror the original content, include in-text citations keyed by `source_id`, and render a bibliography whose numbering and order exactly match the source JSON (preserving provided URLs).

## Current Assets and Constraints
- JSON schema: `src/langpa/schemas/deepsearch_results_schema.json` defines `context`, `input_genes`, `programs`, and citation objects with `source_id`.
- Example data: multiple structured and container outputs in `outputs/` (e.g., `deepsearch_20251126_203524_*_structured.json` and `_container.json`) show citation ordering and bibliography lists.
- Services: `OutputManager` handles JSON extraction/validation; citation utilities exist (`markdown_citation_extractor`, citation resolver + compact bibliography plan) and should be reused instead of duplicating functionality.
- Requirement from user: reference ordering must remain as in the original JSON; `source_id` corresponds to the reference number. Need explicit validation of citation ↔ bibliography correspondence.

## Requirements/Behaviors
- Input: accept validated structured JSON (schema result) or container JSON with `citations`/`compact_bibliography` sections; reject malformed inputs early.
- Ordering: bibliography order must follow the input order; no re-sorting or deduping beyond what the JSON provides.
- Mapping checks: every cited `source_id` in programs/atomic terms must exist in the bibliography list; every bibliography entry should be reachable from `source_id`; raise/record mismatches.
- Rendering: include query/context summary, gene list snapshot, each program (description, atomic processes/components, predicted impacts, evidence summary, significance), supporting/required genes, and in-text citations `[n]` aligned to `source_id`.
- Bibliography: compact reference lines with original URLs; if `compact_bibliography` is present, use it; otherwise derive compact strings from `citations` while keeping original numbering and URLs.

## Approach
1. **Input loader + validator**: Load JSON, validate against `deepsearch_results_schema` (or container shape), and normalize citation structures; ensure dotenv load before any env use.
2. **Reference index + checks**: Build ordered list keyed by `source_id` from input bibliography, verify sequential mapping against cited IDs, and surface gaps/extra refs before rendering.
3. **Markdown layout**: Define deterministic sections (title, metadata/context, input genes summary, programs with nested bullets/tables, evidence summaries, required genes, and notes). Insert citations as `[source_id]` tokens that align with the reference index.
4. **Bibliography rendering**: Emit numbered list in the original order, including compact citation string plus original URL. Prefer existing compact strings if available; otherwise generate minimally formatted lines while preserving IDs and URLs.
5. **CLI/entry point**: Optional thin wrapper to accept JSON path and output Markdown to stdout/file while running validation checks.

## Testing (TDD)
- Unit tests: citation/reference correspondence (missing/extra/gap detection), ordering preservation, Markdown rendering of a small synthetic JSON, fallback when `compact_bibliography` absent.
- Integration-style test: use a real sample from `outputs/` to render end-to-end Markdown and assert reference ordering and `source_id` alignment.
- Failure-mode tests: detect missing bibliography entries for cited IDs and unused bibliography entries; ensure errors are raised or reported.

## MVP
CLI or callable function that takes a schema-valid JSON (e.g., from `outputs/`), validates citation/reference alignment, and emits Markdown with program details and a bibliography whose numbering and URLs exactly match the input `source_id` order (using compact strings when available).

## Critique/Risks
- Legacy outputs might have non-sequential or partial `source_id` coverage; strict validation could block rendering—may need configurable tolerance while still reporting issues.
- Large programs/gene lists could produce very long Markdown; might require pagination or tables later.
- If compact refs are missing and citation metadata is sparse, derived compact strings may be low fidelity; may need to coordinate with citation resolver to ensure titles/IDs are available. 
