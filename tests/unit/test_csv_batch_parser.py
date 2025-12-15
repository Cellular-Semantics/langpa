"""Unit tests for CSV batch parser.

Tests the parsing and validation of CSV files for batch deepsearch queries.
"""

import csv
from pathlib import Path
from io import StringIO

import pytest

from langpa.utils.csv_batch_parser import BatchQuery, parse_csv_batch


@pytest.mark.unit
def test_parse_csv_with_id_and_name(tmp_path):
    """Test CSV parsing when both ID and name columns are present.

    Query name should be formatted as {ID}_{name}.
    """
    csv_content = """ID,name,gene_list,context
0,Gliosis,"GFAP,S100B","Astrocyte activation"
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    queries = parse_csv_batch(csv_file, global_context=None)

    assert len(queries) == 1
    assert queries[0].query_name == "0_Gliosis"
    assert queries[0].genes == ["GFAP", "S100B"]
    assert queries[0].context == "Astrocyte activation"
    assert queries[0].row_number == 1


@pytest.mark.unit
def test_parse_csv_with_id_only(tmp_path):
    """Test CSV parsing when only ID column has value.

    Query name should be just the ID.
    """
    csv_content = """ID,name,gene_list,context
2,,"TP53,MDM2","Tumor suppressor pathways"
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    queries = parse_csv_batch(csv_file, global_context=None)

    assert len(queries) == 1
    assert queries[0].query_name == "2"
    assert queries[0].genes == ["TP53", "MDM2"]
    assert queries[0].context == "Tumor suppressor pathways"


@pytest.mark.unit
def test_parse_csv_with_name_only(tmp_path):
    """Test CSV parsing when only name column has value.

    Query name should be just the name.
    """
    csv_content = """ID,name,gene_list,context
,OPC_like,"SOX10,OLIG2","Oligodendrocyte precursor cells"
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    queries = parse_csv_batch(csv_file, global_context=None)

    assert len(queries) == 1
    assert queries[0].query_name == "OPC_like"
    assert queries[0].genes == ["SOX10", "OLIG2"]


@pytest.mark.unit
def test_parse_csv_with_per_row_context(tmp_path):
    """Test that per-row context is used when present in CSV."""
    csv_content = """ID,name,gene_list,context
0,Test,"GENE1,GENE2","Per-row context here"
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    global_context = "Global context that should be ignored"
    queries = parse_csv_batch(csv_file, global_context)

    assert len(queries) == 1
    assert queries[0].context == "Per-row context here"


@pytest.mark.unit
def test_parse_csv_with_global_context(tmp_path):
    """Test that global context is used when per-row context is empty."""
    csv_content = """ID,name,gene_list,context
0,Test,"GENE1,GENE2",
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    global_context = "Global context fallback"
    queries = parse_csv_batch(csv_file, global_context)

    assert len(queries) == 1
    assert queries[0].context == "Global context fallback"


@pytest.mark.unit
def test_parse_csv_missing_context(tmp_path):
    """Test that missing context (both per-row and global) raises ValueError."""
    csv_content = """ID,name,gene_list,context
0,Test,"GENE1,GENE2",
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    with pytest.raises(ValueError, match="Row 1.*context"):
        parse_csv_batch(csv_file, global_context=None)


@pytest.mark.unit
def test_parse_csv_duplicate_query_names(tmp_path):
    """Test that duplicate query names raise ValueError."""
    csv_content = """ID,name,gene_list,context
0,Gliosis,"GFAP,S100B","Context 1"
0,Gliosis,"VIM,AQP4","Context 2"
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    with pytest.raises(ValueError, match="Duplicate query name.*0_Gliosis.*row 2"):
        parse_csv_batch(csv_file, global_context=None)


@pytest.mark.unit
def test_parse_csv_empty_gene_list(tmp_path):
    """Test that empty gene_list raises ValueError."""
    csv_content = """ID,name,gene_list,context
0,Test,"","Some context"
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    with pytest.raises(ValueError, match="Row 1.*gene_list.*empty"):
        parse_csv_batch(csv_file, global_context=None)


@pytest.mark.unit
def test_parse_csv_with_gse_terms(tmp_path):
    """Test that GSE column is parsed correctly."""
    csv_content = """ID,name,gene_list,context,GSE
0,Test,"GENE1,GENE2","Some context","GO:0001234,GO:0005678"
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    queries = parse_csv_batch(csv_file, global_context=None)

    assert len(queries) == 1
    assert queries[0].gse_terms == ["GO:0001234", "GO:0005678"]


@pytest.mark.unit
def test_parse_csv_missing_required_columns(tmp_path):
    """Test that missing required columns (gene_list) raises ValueError."""
    csv_content = """ID,name,context
0,Test,"Some context"
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    with pytest.raises(ValueError, match="Required column.*gene_list"):
        parse_csv_batch(csv_file, global_context=None)


@pytest.mark.unit
def test_parse_csv_missing_id_and_name(tmp_path):
    """Test that missing both ID and name raises ValueError."""
    csv_content = """ID,name,gene_list,context
,,"GENE1,GENE2","Some context"
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    with pytest.raises(ValueError, match="Row 1.*must have.*ID.*name"):
        parse_csv_batch(csv_file, global_context=None)


@pytest.mark.unit
def test_parse_csv_whitespace_trimming(tmp_path):
    """Test that whitespace is trimmed from gene names and other fields."""
    csv_content = """ID,name,gene_list,context
0,Test," GENE1 , GENE2 , GENE3 ","  Context with spaces  "
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    queries = parse_csv_batch(csv_file, global_context=None)

    assert queries[0].genes == ["GENE1", "GENE2", "GENE3"]
    assert queries[0].context == "Context with spaces"


@pytest.mark.unit
def test_parse_csv_no_gse_column(tmp_path):
    """Test that GSE column is optional and defaults to empty list."""
    csv_content = """ID,name,gene_list,context
0,Test,"GENE1,GENE2","Some context"
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    queries = parse_csv_batch(csv_file, global_context=None)

    assert len(queries) == 1
    assert queries[0].gse_terms == []
