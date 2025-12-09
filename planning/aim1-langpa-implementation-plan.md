# Aim 1 – langpa implementation plan (standalone)

## Goal
Integrate url2ref into langpa so DeepSearch outputs are paired with a citation map keyed by the original reference numbers. Produce a container JSON that keeps the DeepSearch report plus CSL-JSON citations and stats. Numbering must mirror DeepSearch order.

## Chosen citation schema
- Use **CSL-JSON** entries keyed by `ref_id` (stringified integer matching DeepSearch numbering). Keep `id = ref_id` inside each citation.
- Include identifiers when present (`DOI`, `PMID`, `PMCID`) and a custom `resolution` block (`confidence`, `methods`, `validation`, `errors`, `source_url`).

## Data flow
1) DeepSearch call (`DeepSearchService`) returns markdown + `citations` URLs (numbered).
2) Normalize citations into `[{"ref_id": "1", "url": "..."}]` preserving order.
3) Call url2ref wrapper to resolve URLs → `citations: dict[ref_id -> CSL-JSON citation]` plus stats/failures.
4) Update structured DeepSearch payload to reference `ref_id` (not raw URLs) in all citation slots.
5) Emit container JSON:
   ```json
   {
     "metadata": {... run info ...},
     "deepsearch_raw": {...original result incl. URLs...},
     "report": {...deepsearch_results_schema-compliant, using ref_id...},
     "citations": {...CSL-JSON map...},
     "bibliography_stats": {...}
   }
   ```
   Keep backward-compatible raw DeepSearch data alongside the new structures.

## Work packages
1) **Citation normalization**  
   - Add a small adapter to capture DeepSearch `citations` as ordered `{ref_id, url}`.  
   - Fixtures for sample DeepSearch responses to lock structure.

2) **url2ref wrapper**  
   - New `CitationResolver` service in langpa calling `url2ref.resolve_bibliography` (flags for scraping/PDF/topic validation).  
   - Map `CitationResolutionResult` into langpa types (or plain dict) but preserve `ref_id` and `resolution` details.

3) **Schema + prompt updates**  
   - Extend `deepsearch_results_schema.json` to accept `ref_id` fields referencing the citation map (no raw URLs in `citation` objects).  
   - Update DeepSearch prompt template to instruct the model to emit `ref_id` values corresponding to provider numbering.

4) **Container assembly**  
   - In `OutputManager` (or a new orchestration module), build and save the container JSON (path under `outputs/` TBD).  
   - Add summary stats for resolved/unresolved and validation outcomes.

5) **Error handling**  
   - Per-ref graceful failure: keep unresolved refs with original URL and `resolution.status = "unresolved"`.  
   - Avoid renumbering even if duplicates appear; optionally add `canonical_id` if dedup is later needed.

6) **Tests**  
   - Unit tests for citation normalization and container assembly using stubbed url2ref outputs.  
   - Schema validation test for the updated DeepSearch schema and the container JSON.  
   - Integration test (fixture-based) that runs the pipeline on a small DeepSearch sample → citation map → validated container.

## Defaults/assumptions
- Default to CSL-JSON payloads with identifiers and metadata when available.  
- Default url2ref flags can be tuned for cost (e.g., scraping off by default if costly); must be configurable.  
- Directory naming under `outputs/` is deferred; keep code ready to accept an `output_dir` parameter.
