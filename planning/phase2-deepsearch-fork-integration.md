# Phase 2: DeepSearch Fork Integration & JSON Reliability

**Status**: Ready to start after Phase 1 completion ✅
**Previous Phase**: Perplexity DeepSearch integration with sonar-reasoning-pro completed and merged

## Overview

Upgrade the DeepSearch integration to use a forked version of the deep-research-client library that has native support for sonar-reasoning-pro model with direct JSON response format, eliminating the need for complex JSON extraction from `<think>` tags.

## Goals

1. **Improved Reliability**: Direct JSON response without parsing complexity
2. **Better Performance**: Native JSON format support reduces processing overhead
3. **Cleaner Architecture**: Remove custom JSON extraction workarounds
4. **Schema Compliance**: Ensure consistent schema validation with potential agentic fixes

## Phase 2 Tasks

### 1. Switch to Fork of deep-research-client

**Objective**: Update dependency to use forked version with sonar-reasoning-pro JSON support

**Implementation**:
- Update `pyproject.toml` to point to fork repository
- Verify fork has native `response_format` support for sonar-reasoning-pro
- Test compatibility with current DeepSearchService interface

**Acceptance Criteria**:
- Fork successfully installs and imports
- sonar-reasoning-pro model returns direct JSON (no `<think>` wrapper)
- Existing unit tests pass with fork

### 2. Update DeepSearchService for Fork Integration

**Objective**: Modify service to leverage native JSON response format

**Implementation**:
- Update `research_gene_list()` to use native `response_format` parameter
- **Keep existing `<think>` tag removal code** as fallback for reliability
- Add detection logic: try direct JSON first, fall back to extraction if needed
- Update system prompts to request pure JSON without reasoning tags

**Code Changes**:
```python
# Try direct JSON response first
if hasattr(result, 'structured_data') and result.structured_data:
    return result.structured_data

# Fallback to existing extraction logic
extracted_json = output_manager.extract_json_from_markdown(result.markdown)
```

**Acceptance Criteria**:
- Service works with both JSON response modes
- Graceful fallback to extraction if direct JSON fails
- All existing functionality maintained

### 3. Add JSON Schema Compliance Testing

**Objective**: Comprehensive schema validation testing to identify reliability issues

**Implementation**:
- Add integration test specifically for schema compliance
- Test with multiple gene lists and contexts
- Measure schema compliance rate (target: >95%)
- Document common schema violation patterns

**Test Structure**:
```python
@pytest.mark.integration
def test_schema_compliance_rate():
    """Test schema compliance across multiple gene lists."""
    test_cases = [
        (["TP53", "BRCA1"], "cancer"),
        (["FOXP1", "SOX9"], "neural development"),
        # ... more test cases
    ]
    compliance_rate = measure_schema_compliance(test_cases)
    assert compliance_rate >= 0.95
```

### 4. Plan Agentic Schema Correction (If Needed)

**Objective**: Design automated schema correction system for unreliable responses

**Trigger Conditions**:
- Schema compliance rate < 95%
- Frequent validation failures in production
- Consistent patterns in schema violations

**Agentic Correction Strategy**:
- **Schema Repair Agent**: LLM-based agent to fix malformed JSON
- **Validation Loop**: Iterative correction with retry limit
- **Fallback Mechanisms**: Progressive degradation of requirements
- **Learning Component**: Track and learn from common fixes

**Implementation Plan**:
```
Phase 2a: Schema compliance measurement
Phase 2b: Agentic correction design (if needed)
Phase 2c: Correction agent implementation
Phase 2d: Production testing and refinement
```

## Success Metrics

- **JSON Extraction**: Direct JSON response working >90% of time
- **Schema Compliance**: >95% of responses validate correctly
- **Performance**: Response processing time reduced by >50%
- **Reliability**: End-to-end workflow success rate >98%
- **Maintainability**: Reduced complexity in output parsing logic

## Risk Assessment

**Low Risk**:
- Fork integration (can revert to current approach)
- Schema testing additions

**Medium Risk**:
- Changes to core DeepSearchService logic
- Potential regressions in JSON extraction

**High Risk**:
- Agentic correction complexity (only if needed)
- Production reliability with new approach

## Dependencies

- Fork of deep-research-client with sonar-reasoning-pro JSON support
- Existing schema validation infrastructure
- Current test suite as regression safety net

## Timeline Estimate

- **Week 1**: Fork integration and service updates
- **Week 2**: Schema compliance testing and measurement
- **Week 3**: Decision point on agentic correction need
- **Week 4+**: Agentic correction implementation (if required)

---

*Next Phase Planning Document*
*Generated: November 14, 2025*
*Previous Phase: [deepsearch-integration.md](deepsearch-integration.md)*