# Output Management & DeepSearch CLI

## Run modes
- **Live API**: call DeepSearch via `scripts/run_deepsearch.py` with genes/context; optional citation resolution (`--resolve-citations`).
- **Offline**: process saved responses (`--from-markdown` for markdown, `--raw-input` for raw JSON). Citations are extracted from markdown if not provided.
- **Batch**: `--batch-dir` iterates query subfolders (e.g., `projects/<proj>/inputs/<query>/*`) and processes each file as a query.

## Project/query organization
Outputs are written under `outputs/<project>/<query>/<timestamp>/` (base override via `--output-dir`). Filenames are fixed; identity comes from the folder path:
- `deepsearch.json`: raw markdown + original citations + metadata (includes project/query/source_tag).
- `deepsearch_structured.json`: parsed/validated DeepSearch report (citations with `source_id` only).
- `deepsearch_container.json`: structured report + CSL-JSON citation map (keyed by `source_id`) + resolution stats.
- `deepsearch_extracted_debug.json`: optional debug dump when `--debug-extraction` is used.

Query naming:
- `--query` overrides; otherwise derived from input folder/basename or context/genes for live runs.
- `--project` defaults to `default` if not supplied; names are sanitized for filesystem safety.

## Citation handling
- Raw citations come from DeepSearch or markdown extraction; normalized to `{source_id, source_url}` preserving numbering.
- Resolver (`CitationResolver`) calls url2ref and produces CSL-JSON entries keyed by `source_id`; report stays source_id-only.
- Container includes both report and citation map; raw response is retained for traceability.
