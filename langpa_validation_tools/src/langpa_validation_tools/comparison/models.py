"""Pydantic models for comparison results."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, field_validator


class SimilarityScores(BaseModel):
    """Similarity scores between two programs."""

    gene_jaccard: float = Field(ge=0.0, le=1.0, description="Gene set Jaccard similarity")
    name_similarity: float = Field(ge=0.0, le=1.0, description="Program name similarity")
    combined: float = Field(ge=0.0, le=1.0, description="Combined weighted similarity")


class ProgramPair(BaseModel):
    """A pair of matched programs with similarity scores."""

    program_a: dict[str, Any] = Field(description="First program")
    program_b: dict[str, Any] = Field(description="Second program")
    scores: SimilarityScores = Field(description="Similarity scores")

    @field_validator("program_a", "program_b")
    @classmethod
    def validate_program(cls, v: dict[str, Any]) -> dict[str, Any]:
        """Validate program has required fields."""
        if "program_name" not in v:
            raise ValueError("Program must have 'program_name' field")
        if "supporting_genes" not in v:
            raise ValueError("Program must have 'supporting_genes' field")
        return v
