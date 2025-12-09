# DeepSearch citations structure & parsing plan

## Requirements
- Structured report (DeepSearch JSON) must use citation objects with `source_id` only. No `source_url` in the report schema to avoid prompt hallucinations.
- Citation URLs and metadata live in a separate citation map (CSL-JSON) keyed by `source_id` inside the container JSON.
- Container includes both blobs: `report` (source_id-only) and `citations` map (with URL/metadata).

## Actions
1) Schema alignment
   - Update `schemas/deepsearch_results_schema.json`: citation requires only `source_id`; remove `source_url` from required/properties.
   - Prompt stays focused on source_id in report; URLs handled downstream.

2) Citation extraction (deterministic)
   - Skip fenced code blocks entirely when scanning markdown.
   - Detect bibliography block with numbering forms: `1. URL`, `1) URL`, `[1] URL`, contiguous, starting at 1. Use this block exclusively and preserve `source_id`.
   - Fallback: footnotes/links/plain URLs (still skipping fences). Use footnote numbers for source_id when present; otherwise leave source_id unset for normalization.
   - If citations list is provided (raw input), use it directly.

3) Pipeline flow
   - Extract and parse JSON (report) -> validate against updated schema (source_id-only).
   - Normalize citations from `result.citations` or extracted markdown bibliography; preserve numbering.
   - Resolve citations -> CSL map keyed by `source_id` (includes URL/metadata) for container.
   - Container: `report` (source_id-only), `citations` map, stats, raw response, metadata. Do not inject URLs into the report.

4) Tests
   - Schema validation passes with source_id-only citations.
   - Extractor: markdown with schema fence + `1. URL` bibliography -> citations keyed 1..N; schema URL ignored.
   - Pipeline offline fixture: markdown + bibliography -> report validates, normalized citations preserve numbering, container has CSL map with URLs/metadata.
