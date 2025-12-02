# Citation extraction hardening plan

## Goals
- Make JSON extraction from DeepSearch markdown robust: always return a parsed dict (not a string) from the post-`</think>` block.
- Harden citation extraction to avoid schema/JSON fence noise and preserve numbering from bibliography blocks.

## Actions
1. JSON extraction & typing
   - Ensure `extract_json_from_markdown` returns a parsed dict for the post-`</think>` JSON block (fenced or raw).
   - In `process_and_save_structured_output`, if the extracted payload is a string, `json.loads` it before validation/saving so `report` is always a dict.

2. Citation extraction hardened (deterministic, no agents)
   - Skip all code fences when scanning for citations to avoid schema URLs and fenced JSON.
   - Detect a bibliography block: contiguous lines (near the end) of `[n] http(s)://…` with sequential numbering starting at 1. If found, use only that block and set `source_id` from the numbers.
   - Fallback when no clean block:
     - Still skip fenced content.
     - Prefer numbered footnotes `[n] URL` for `source_id`.
     - Only assign sequential IDs when no numbers are present.
   - If a citations list is provided (e.g., `--raw-input` contains `citations`), use it directly and skip markdown extraction.

3. Integration
   - Apply the hardened extractor in the offline CLI path (`--from-markdown`), so citations come from the bibliography block when present; then run `normalize_citations` to preserve numbering.
   - Keep existing resolver flow (`CitationResolver`) for URL expansion into CSL-JSON.

4. Tests to add
   - Markdown with schema fence + post-`</think>` JSON + numbered bibliography block: verify parsed dict (not string), citations keyed 1..N matching the block, schema URL ignored.
   - Markdown without a bibliography block but with links: fenced URLs skipped; sequential IDs assigned only when no numbering exists.
   - Stringified JSON payload is parsed before validation/saving.
