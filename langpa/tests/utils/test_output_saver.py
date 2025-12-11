"""Test output saver for integration test inspection.

Saves integration test outputs (raw API responses + extracted JSON) to disk
when --save-outputs flag is enabled.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


class TestOutputSaver:
    """Saves integration test outputs for inspection.

    Provides opt-in saving of test outputs via --save-outputs pytest flag.
    Outputs are organized by test file and test name with timestamps.

    .. code-block:: python

        saver = TestOutputSaver(enabled=True)
        output_dir = saver.save_test_output(
            test_name="test_foo",
            test_file="test_bar.py",
            raw_response=api_response,
            extracted_json=extracted_data,
            test_context={"genes": ["GENE1"], "context": "cells"}
        )
    """

    def __init__(self, enabled: bool = False, base_dir: str | Path = "test_outputs"):
        """Initialize the test output saver.

        Args:
            enabled: Whether to save outputs (controlled by --save-outputs flag)
            base_dir: Base directory for saving outputs
        """
        self.enabled = enabled
        self.base_dir = Path(base_dir)

    def save_test_output(
        self,
        test_name: str,
        test_file: str,
        raw_response: Any,
        extracted_json: dict | None = None,
        validation_result: dict | None = None,
        test_context: dict | None = None
    ) -> Path | None:
        """Save test output if enabled.

        Args:
            test_name: Name of test function (e.g., "test_foo")
            test_file: Test file name (e.g., "test_deepsearch.py")
            raw_response: Raw API response object
            extracted_json: Extracted and parsed JSON
            validation_result: Validation metadata
            test_context: Test parameters (genes, context, preset, etc.)

        Returns:
            Path to output directory if saved, None if disabled

        .. code-block:: python

            # Save complete output with all components
            output_dir = saver.save_test_output(
                test_name="test_deepsearch_e2e",
                test_file="test_integration.py",
                raw_response=result,
                extracted_json=extracted,
                validation_result={"success": True, "retry_count": 0},
                test_context={"genes": ["GENE1"], "context": "cells"}
            )
        """
        if not self.enabled:
            return None

        # Create output directory with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_file_clean = test_file.replace("test_", "").replace(".py", "")
        output_dir = self.base_dir / "integration" / test_file_clean / f"{test_name}_{timestamp}"
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save raw response
        raw_data = {
            "test_context": test_context or {},
            "response": {
                "markdown": getattr(raw_response, "markdown", None) or getattr(raw_response, "content", None),
                "citations": getattr(raw_response, "citations", []),
                "provider": getattr(raw_response, "provider", None),
                "model": getattr(raw_response, "model", None),
                "duration_seconds": getattr(raw_response, "duration_seconds", None)
            },
            "saved_at": datetime.now().isoformat()
        }

        with open(output_dir / "raw_response.json", "w", encoding="utf-8") as f:
            json.dump(raw_data, f, indent=2, ensure_ascii=False)

        # Save extracted JSON if provided
        if extracted_json is not None:
            with open(output_dir / "extracted_json.json", "w", encoding="utf-8") as f:
                json.dump(extracted_json, f, indent=2, ensure_ascii=False)

        # Save validation result if provided
        if validation_result is not None:
            with open(output_dir / "validation_result.json", "w", encoding="utf-8") as f:
                json.dump(validation_result, f, indent=2, ensure_ascii=False)

        return output_dir


__all__ = ["TestOutputSaver"]
