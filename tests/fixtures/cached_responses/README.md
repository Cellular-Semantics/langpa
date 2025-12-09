# Cached DeepSearch API Responses

This directory contains cached API responses for integration testing.

## Purpose

- **Avoid expensive repeated API calls** during test execution
- **Enable fast test execution** after initial cache population
- **Reduce testing costs by 75-85%** compared to uncached testing
- **Support deterministic testing** with reproducible responses

## Cache Strategy

### Cache Key Generation

Cache keys are deterministic hashes of:
```python
hash(preset_name, sorted(genes), normalized_context)
```

**Normalization rules:**
- Genes: Sorted alphabetically, uppercased
- Context: Whitespace stripped, lowercased
- Preset: Used as-is

This ensures:
- `["A", "B"]` and `["B", "A"]` produce the same key
- `"cells"` and `" cells "` produce the same key

### File Naming

Files are named for human readability:
```
{genes}_{context}_{preset}_{hash}.json
```

Example:
```
tmem14e_cells_perplexity-sonar-pro_abc123456789.json
```

## Test Gene Sets

### MINIMAL (ultra-short responses)
```python
genes = ["TMEM14E"]
context = "cells"
```
- **Purpose:** First integration tests, basic validation, cache creation
- **Expected tokens:** ~200-500
- **Cost:** ~$0.001-0.002 per call

### MODERATE (short responses)
```python
genes = ["C9orf72", "C21orf91"]
context = "neural cells"
```
- **Purpose:** E2E pipeline, preset comparison, correction tests
- **Expected tokens:** ~800-1500
- **Cost:** ~$0.003-0.006 per call

### Cost Comparison

| Approach | Genes | Tokens/call | Cost/call | Savings |
|----------|-------|-------------|-----------|---------|
| Old | TP53, BRCA1, PTEN, etc. | 3000-8000 | $0.012-0.032 | - |
| New MINIMAL | TMEM14E | 200-500 | $0.001-0.002 | **85-94%** |
| New MODERATE | C9orf72, C21orf91 | 800-1500 | $0.003-0.006 | **75-81%** |

## Cache Usage

### In Tests

```python
from utils.cache_manager import ResponseCacheManager

cache = ResponseCacheManager()

# Try to load from cache
cached_response = cache.load(preset, genes, context)

if cached_response:
    # Use cached response (no API call)
    result = MockResult(**cached_response)
else:
    # Call real API
    service = DeepSearchService(preset=preset)
    result = service.research_gene_list(genes, context)

    # Save to cache for next time
    cache.save(preset, genes, context, {
        "markdown": result.markdown,
        "citations": result.citations,
        "provider": result.provider,
        "model": result.model,
        "duration_seconds": result.duration_seconds
    })
```

### Cache Hit Workflow

1. **First run (cache miss):**
   - Integration test calls real API
   - Response is cached to disk
   - Test validates response
   - **Time:** ~5-15 seconds per test
   - **Cost:** $0.001-0.006 per test

2. **Subsequent runs (cache hit):**
   - Integration test loads from cache
   - No API call made
   - Test validates cached response
   - **Time:** <1 second per test
   - **Cost:** $0

## Cache Maintenance

### When to Regenerate

Regenerate cache when:
- **Schema changes** (new required fields, structure changes)
- **Prompt changes significantly** (may produce different response format)
- **Testing new presets** (each preset has its own cache)
- **Cache becomes stale** (>30 days old, for freshness)

### How to Regenerate

```bash
# Delete all cache files
rm tests/fixtures/cached_responses/*.json

# Run integration tests (will populate cache)
uv run pytest -m integration
```

### How to Regenerate Specific Cache

```bash
# Delete specific cached response
rm tests/fixtures/cached_responses/tmem14e_cells_*.json

# Run specific test
uv run pytest tests/integration/test_name.py -k specific_test
```

## Cache File Structure

Each cache file contains:

```json
{
  "preset": "perplexity-sonar-schema-embedded",
  "genes": ["TMEM14E"],
  "context": "cells",
  "cache_key": "abc123...",
  "response": {
    "markdown": "...",
    "citations": [...],
    "provider": "perplexity",
    "model": "sonar-deep-research",
    "duration_seconds": 5.2
  },
  "cached_at": "2025-12-09T10:30:00"
}
```

## Best Practices

1. **Commit cache files** to version control for CI/CD
2. **Use minimal gene sets** to reduce API costs
3. **Check cache before adding new tests** - reuse if possible
4. **Document cache dependencies** in test docstrings
5. **Regenerate periodically** to ensure freshness

## CI/CD Considerations

### GitHub Actions

```yaml
# Run unit tests only (no API calls)
- name: Run unit tests
  run: uv run pytest -m unit

# Integration tests use cached responses (no API calls in CI)
- name: Run integration tests (cached)
  run: uv run pytest -m integration
  # These will use committed cache files
  # No PERPLEXITY_API_KEY needed
```

### Local Development

```bash
# Full suite with API (populates cache)
export PERPLEXITY_API_KEY=your_key
uv run pytest

# After cache populated, fast runs
uv run pytest  # Uses cache, <10 seconds
```

## Troubleshooting

### Cache Not Loading

**Problem:** Tests making API calls even though cache exists

**Solutions:**
- Check gene normalization (TMEM14E vs tmem14e)
- Check context normalization (whitespace)
- Verify preset name matches exactly
- Check cache_key in file matches generated key

### Cache Miss After Code Changes

**Problem:** Modifying code invalidates cache

**Impact:** Only happens if:
- JSON extraction logic changes
- Schema structure changes
- Preset configuration changes

**Solution:** Regenerate cache for affected tests

## Statistics

Expected cache hit rates:
- **Unit tests:** 0% (no cache, no API calls)
- **Integration tests (first run):** 0% (populates cache)
- **Integration tests (subsequent runs):** 95-100%
- **CI/CD:** 100% (uses committed cache)

Target test execution times:
- **Unit tests:** <5 seconds (total)
- **Integration tests (cached):** <30 seconds (total)
- **Integration tests (uncached):** 2-5 minutes (total)
