"""DeepSearch response validator using pydantic with retry logic.

This module wraps cellsem_llm_client's SchemaValidator to provide
validation of DeepSearch responses with intelligent retry and auto-correction.
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cellsem_llm_client.schema import SchemaValidationResult


class DeepSearchValidator:
    """Validates DeepSearch responses using pydantic with retry logic.

    Uses cellsem_llm_client's SchemaValidator for intelligent validation
    with automatic retry and correction of common LLM response issues.

    .. code-block:: python

        validator = DeepSearchValidator()
        result = validator.validate_markdown(markdown_response)

        if result.success:
            validated_model = result.validated_data
        else:
            print(f"Validation failed: {result.errors}")
            print(f"Retries attempted: {result.retry_count}")
    """

    def __init__(self) -> None:
        """Initialize the validator with SchemaValidator and OutputManager."""
        from cellsem_llm_client.schema import SchemaValidator

        from langpa.services.output_manager import OutputManager

        self.schema_validator = SchemaValidator()
        self.output_manager = OutputManager()  # For JSON extraction

    def validate_markdown(
        self, markdown: str, max_retries: int = 3
    ) -> SchemaValidationResult:
        """Extract and validate JSON from markdown response.

        Args:
            markdown: Markdown content containing embedded JSON
            max_retries: Maximum number of validation retry attempts

        Returns:
            SchemaValidationResult with:
                - success: bool (validation succeeded)
                - model_instance: BaseModel instance or None
                - error: Exception or None (validation error)
                - retry_count: int (number of retries performed)
                - validation_time_ms: float (time taken)

        .. code-block:: python

            result = validator.validate_markdown(llm_response)
            if result.success:
                data = result.model_instance
                print(f"Validated after {result.retry_count} retries")
        """
        from cellsem_llm_client.schema import SchemaValidationResult

        from langpa.services.pydantic_models import get_deepsearch_pydantic_model

        # Extract JSON using existing OutputManager logic
        json_data = self.output_manager.extract_json_from_markdown(markdown)

        if json_data is None:
            return SchemaValidationResult(
                success=False,
                model_instance=None,
                error=Exception("Failed to extract JSON from markdown"),
                retry_count=0,
                validation_time_ms=0.0,
            )

        # Get pydantic model
        model = get_deepsearch_pydantic_model()

        # Validate with retry
        return self.schema_validator.validate_with_retry(
            response_text=json.dumps(json_data),
            target_model=model,
            max_retries=max_retries,
        )

    def validate_json_dict(
        self, json_data: dict, max_retries: int = 3
    ) -> SchemaValidationResult:
        """Validate pre-extracted JSON dict.

        Args:
            json_data: JSON dictionary to validate
            max_retries: Maximum number of validation retry attempts

        Returns:
            SchemaValidationResult with validation details

        .. code-block:: python

            json_dict = {"context": {...}, "programs": [...]}
            result = validator.validate_json_dict(json_dict)
        """
        from langpa.services.pydantic_models import get_deepsearch_pydantic_model

        model = get_deepsearch_pydantic_model()

        return self.schema_validator.validate_with_retry(
            response_text=json.dumps(json_data),
            target_model=model,
            max_retries=max_retries,
        )


__all__ = ["DeepSearchValidator"]
