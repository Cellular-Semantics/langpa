# Output organization & query naming plan

## Goals
- Organize outputs by project/query with timestamped run folders.
- Derive sensible query names from input files/folders; allow explicit override.
- Keep raw/structured/container outputs co-located; record source metadata.

## Output layout
- Root: `outputs/<project>/<query>/<timestamp>/`
- Files inside a run:
  - `deepsearch_raw.json` (raw markdown/citations + metadata)
  - `deepsearch_structured.json` (parsed/validated report) when validation succeeds
  - `deepsearch_container.json` (report + citation map + stats) when `resolve_citations` is enabled
  - Optional `metadata.json` summary (project/query/source_tag/flags)

## Query naming
- Explicit flag: `--query` overrides everything (sanitized).
- Derive when not provided:
  - For `--from-markdown` / `--raw-input`: prefer the parent folder name if under `projects/<project>/inputs/<query>/`; otherwise use input basename (no extension).
  - For gene/context files: if they reside under a common folder, use that folder; else fallback to a basename or a derived name like `genes_<first>`.
  - Live runs (no files): derive from context (first 3–5 tokens) or genes (e.g., `genes_<first>_...`) if no `--query` provided.

## Project handling
- New `--project` flag; defaults to something like `default` if not provided.
- Batch mode: `--batch-dir projects/<project>/inputs` treats each immediate subfolder as a query; processes files inside, writing to `outputs/<project>/<query>/<timestamp>/`.

## Filename tags
- Prefer directory structure over long filenames. Inside run dir, keep simple names (`deepsearch_raw.json`, etc.).
- Record `source_tag` (input basename) in metadata; optionally include it in filenames if helpful (e.g., `deepsearch_raw_run1.json`), but not required.

## Metadata
- Store `project`, `query`, `source_tag`, resolver flags, and source paths in `metadata` for all outputs.

## Implementation notes
- CLI: add `--project`, `--query`, `--batch-dir`; derive query when absent as above.
- OutputManager: accept a base output dir (run dir) and write standard filenames there; keep legacy `_generate_filename` for fallback.
- Tests: unit test deriving query/project/run dir; fixture to ensure outputs are placed under `outputs/<project>/<query>/<timestamp>/` with metadata recording the source.
