import pytest

from langpa.services.output_manager import OutputManager


@pytest.mark.unit
def test_extract_prefers_result_over_schema_block(tmp_path):
    output_manager = OutputManager(output_dir=tmp_path)
    markdown = """
Intro text
```json
{"title": "Gene Program Functional Analysis", "type": "object", "definitions": {}, "required": ["context", "input_genes", "programs", "version"]}
```
More narrative
```json
{
  "context": {"cell_type": "astrocyte", "disease": "glioma"},
  "input_genes": ["GENE1"],
  "programs": [{
    "program_name": "Example",
    "description": "desc",
    "predicted_cellular_impact": "impact",
    "evidence_summary": "summary",
    "significance_score": 0.1,
    "citations": [],
    "supporting_genes": []
  }],
  "version": "1.0"
}
```
"""

    extracted = output_manager.extract_json_from_markdown(markdown)

    assert isinstance(extracted, dict)
    assert extracted.get("programs"), "Should return the result JSON block, not the schema block"


@pytest.mark.unit
def test_extract_schema_only_returns_none(tmp_path):
    output_manager = OutputManager(output_dir=tmp_path)
    markdown = """
Only schema
```json
{"title": "Schema", "type": "object", "definitions": {}, "required": ["context", "input_genes", "programs", "version"]}
```
"""

    extracted = output_manager.extract_json_from_markdown(markdown)

    assert extracted is None


@pytest.mark.unit
def test_extract_selects_best_candidate_with_programs(tmp_path):
    output_manager = OutputManager(output_dir=tmp_path)
    markdown = """
```json
{"unrelated": true}
```
```json
{"programs": [{"program_name": "X", "description": "d", "predicted_cellular_impact": "i", "evidence_summary": "e", "significance_score": 0.2, "citations": [], "supporting_genes": []}], "context": {"cell_type": "c", "disease": "d"}, "input_genes": ["A"], "version": "1.0"}
```
"""

    extracted = output_manager.extract_json_from_markdown(markdown)

    assert isinstance(extracted, dict)
    assert extracted.get("programs"), "Should choose the candidate that contains programs"


@pytest.mark.unit
def test_extract_returns_none_when_no_json(tmp_path):
    output_manager = OutputManager(output_dir=tmp_path)
    markdown = "Plain text without any JSON content."

    extracted = output_manager.extract_json_from_markdown(markdown)

    assert extracted is None
