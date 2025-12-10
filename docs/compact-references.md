# Compact Bibliography References

This guide explains how to use langpa's compact bibliography feature to generate human-readable citation strings alongside structured CSL-JSON citations.

## Overview

When resolving citations with url2ref (`--resolve-citations`), langpa can generate compact, human-readable reference strings in addition to the standard CSL-JSON format. These compact strings are formatted according to standard citation styles (Vancouver, APA, IEEE, Chicago, etc.) and are ideal for:

- Display in user interfaces
- Quick human scanning of references
- Inclusion in reports and documentation
- Citation verification and QA

## Quick Start

### CLI Usage

Enable compact bibliography generation when running DeepSearch:

```bash
python scripts/run_deepsearch.py \
  --genes TMEM14E GFAP \
  --context "astrocyte activation in gliosis" \
  --resolve-citations \
  --citation-style apa \
  --citation-locale en-GB
```

### Python API Usage

Use `CitationResolver` directly in your code:

```python
from langpa.services.citation_resolver import CitationResolver

resolver = CitationResolver(validate=True, pdf=True)

citations = [
    {"source_id": "1", "source_url": "https://pubmed.ncbi.nlm.nih.gov/37674083/"},
    {"source_id": "2", "source_url": "https://doi.org/10.1038/s41586-023-06221-2"}
]

result = resolver.resolve_with_compact(
    citations,
    style="vancouver",
    locale="en-US"
)

# Access compact strings
for entry in result["compact_bibliography"]["entries"]:
    print(entry)
# Output:
# [1] Author A, Author B. Title of paper. Journal Name. 2024;123(4):567-90.
# [2] Smith J, et al. Another paper title. Nature. 2023;456:123-456.

# Access CSL-JSON for structured data
csl_json = result["citations"]["1"]
print(csl_json["title"])
```

## Container JSON Structure

When `--resolve-citations` is enabled, the container JSON includes a `compact_bibliography` field:

```json
{
  "metadata": {
    "timestamp": "2025-01-15T10:30:00",
    "genes": ["TMEM14E", "GFAP"],
    "context": "astrocyte activation"
  },
  "deepsearch_raw": {
    "markdown": "...",
    "citations": [...]
  },
  "report": {
    "context": {...},
    "programs": [...]
  },
  "citations": {
    "1": {
      "id": "1",
      "type": "article-journal",
      "title": "Paper title",
      "author": [...],
      "DOI": "10.1234/example"
    }
  },
  "compact_bibliography": {
    "entries": [
      "[1] Author A, Author B. Paper title. Journal. 2024;123:456-789."
    ],
    "style": "vancouver",
    "locale": "en-US",
    "renderer": "citeproc-py",
    "error": null
  },
  "bibliography_stats": {
    "total": 1,
    "resolved": 1,
    "unresolved": 0
  },
  "unresolved": []
}
```

### Field Descriptions

- **`entries`**: Array of formatted citation strings, ordered by source_id
- **`style`**: Citation style used for rendering (e.g., "vancouver", "apa")
- **`locale`**: Locale used for formatting (e.g., "en-US", "en-GB")
- **`renderer`**: Renderer used - either "citeproc-py" (full) or "fallback" (simple)
- **`error`**: Error message if fallback renderer was used (null otherwise)

## Citation Styles

Compact bibliography supports multiple citation styles via citeproc-py. Common styles include:

### Vancouver (Default)

Numeric citation style commonly used in biomedical journals.

```
[1] Smith J, Jones A, Brown B. Title of the paper. Nature. 2024;456:123-456.
[2] Author A, et al. Another paper title. Cell. 2023;234(5):678-90.
```

**CLI**: `--citation-style vancouver`

### APA (American Psychological Association)

Author-date style used in psychology and social sciences.

```
[1] Smith, J., Jones, A., & Brown, B. (2024). Title of the paper. Nature, 456, 123-456.
[2] Author, A., et al. (2023). Another paper title. Cell, 234(5), 678-690.
```

**CLI**: `--citation-style apa`

### IEEE

Numeric style used in engineering and computer science.

```
[1] J. Smith, A. Jones, and B. Brown, "Title of the paper," Nature, vol. 456, pp. 123-456, 2024.
[2] A. Author et al., "Another paper title," Cell, vol. 234, no. 5, pp. 678-690, 2023.
```

**CLI**: `--citation-style ieee`

### Chicago

Author-date style with flexible formatting options.

```
[1] Smith, John, Alice Jones, and Bob Brown. 2024. "Title of the Paper." Nature 456: 123–456.
[2] Author, A., et al. 2023. "Another Paper Title." Cell 234 (5): 678–690.
```

**CLI**: `--citation-style chicago`

## Locales

Locales affect date formatting, language-specific punctuation, and term translations:

- **`en-US`** (default): American English
- **`en-GB`**: British English (uses "et al." positioning differences)
- **`de-DE`**: German (uses German date formats and terms)
- **`fr-FR`**: French
- **`es-ES`**: Spanish

Example:

```bash
python scripts/run_deepsearch.py \
  --genes TP53 \
  --context cancer \
  --resolve-citations \
  --citation-style apa \
  --citation-locale de-DE
```

## Renderer Behavior

### citeproc-py (Primary Renderer)

When `citeproc-py` is available, it provides full citation style support:

- Accurate formatting for 100+ citation styles
- Proper locale support
- Complex formatting rules (e.g., et al. thresholds, abbreviations)

Example output:

```json
{
  "renderer": "citeproc-py",
  "error": null
}
```

### Fallback Renderer

If `citeproc-py` is unavailable or fails, a simple fallback renderer generates basic citations:

```json
{
  "renderer": "fallback",
  "error": "ImportError: No module named 'citeproc'"
}
```

Fallback format example:

```
[1] Author A, Author B. Title. DOI: 10.1234/example
```

The fallback ensures citations are always available, even without citeproc-py installed.

## Advanced Usage

### Using with OutputManager

When processing DeepSearch results programmatically:

```python
from langpa.services.output_manager import OutputManager
from langpa.services.citation_resolver import CitationResolver

output_manager = OutputManager(output_dir="outputs")
resolver = CitationResolver(validate=True, pdf=True)

processing_result = output_manager.process_and_save_structured_output(
    result=deepsearch_result,
    genes=["TMEM14E"],
    context="cellular function",
    resolve_citations=True,
    resolver=resolver,
    citation_style="apa",
    citation_locale="en-GB"
)

container_path = processing_result["container_file"]
```

### Customizing Resolution Behavior

Configure `CitationResolver` for different resolution strategies:

```python
# Minimal resolution (fastest)
resolver = CitationResolver(
    validate=False,  # Skip API validation
    scrape=False,    # No web scraping
    pdf=False        # No PDF extraction
)

# Maximum resolution (most complete, slowest)
resolver = CitationResolver(
    validate=True,   # Full API validation
    scrape=True,     # Enable web scraping
    pdf=True,        # Extract metadata from PDFs
    topic_validation=True  # Validate paper relevance
)
```

## Backward Compatibility

The compact bibliography feature is fully backward-compatible:

1. **Optional**: Only generated when `--resolve-citations` is enabled
2. **Non-breaking**: Existing container JSON structure unchanged
3. **Defaults**: Uses sensible defaults (vancouver, en-US) if not specified
4. **CSL-JSON preserved**: Full CSL-JSON citations still included in `citations` field

Containers without compact bibliography remain valid:

```json
{
  "citations": {...},
  "bibliography_stats": {...}
  // No compact_bibliography field - still valid
}
```

## Troubleshooting

### Empty Compact Bibliography

If `compact_bibliography.entries` is empty:

1. Check that citations were resolved: verify `bibliography_stats.resolved > 0`
2. Ensure `--resolve-citations` is enabled
3. Check url2ref is properly installed: `uv sync --dev`

### Fallback Renderer Used

If `renderer: "fallback"` appears:

1. Install citeproc-py: `pip install citeproc-py`
2. Check the `error` field for the specific failure reason
3. Fallback still provides usable citations - only formatting is simplified

### Style Not Applied

If custom style isn't reflected:

1. Verify the style name is correct (lowercase, hyphenated)
2. Check citeproc-py is installed (fallback ignores style)
3. Common styles: vancouver, apa, ieee, chicago, nature, science

## Performance Considerations

Compact bibliography generation adds minimal overhead:

- **Citation resolution**: ~0.5-2s per citation (url2ref API calls)
- **Rendering**: ~10-50ms for citeproc-py, ~1ms for fallback
- **File size**: ~100-200 bytes per compact entry

For large bibliographies (>50 citations), consider:

- Using `--citation-no-validate` to skip API validation
- Caching resolved citations for repeated queries
- Running batch processing during off-peak hours

## Examples

### Complete CLI Example

```bash
python scripts/run_deepsearch.py \
  --genes TP53 MDM2 CDKN2A \
  --context "p53 pathway in cancer" \
  --resolve-citations \
  --citation-style nature \
  --citation-locale en-GB \
  --citation-validate \
  --citation-pdf \
  --project cancer-research \
  --query p53-pathway
```

Output location: `outputs/cancer-research/p53-pathway/<timestamp>/deepsearch_container.json`

### Python API Example

```python
from pathlib import Path
import json
from langpa.services.citation_resolver import CitationResolver

# Resolve with compact strings
resolver = CitationResolver()
citations = [
    {"source_id": "1", "source_url": "https://pubmed.ncbi.nlm.nih.gov/37674083/"}
]

result = resolver.resolve_with_compact(
    citations,
    style="nature",
    locale="en-US"
)

# Save compact references to text file
output_path = Path("references.txt")
with output_path.open("w") as f:
    f.write("# References\n\n")
    for entry in result["compact_bibliography"]["entries"]:
        f.write(f"{entry}\n")

print(f"Compact references saved to {output_path}")
```

## See Also

- [url2ref documentation](https://github.com/Cellular-Semantics/url2ref) - Citation resolution engine
- [citeproc-py](https://github.com/brechtm/citeproc-py) - Citation style processor
- [Citation Style Language](https://citationstyles.org/) - CSL specification
