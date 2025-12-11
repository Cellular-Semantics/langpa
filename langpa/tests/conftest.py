"""Pytest configuration and fixtures for langpa tests.

Provides shared fixtures including test output saving functionality.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Add tests directory to path for importing utils
sys.path.insert(0, str(Path(__file__).parent))

from utils.test_output_saver import TestOutputSaver


def pytest_addoption(parser):
    """Add custom pytest options.

    Registers --save-outputs flag for optionally saving integration test outputs.
    """
    parser.addoption(
        "--save-outputs",
        action="store_true",
        default=False,
        help="Save integration test outputs to test_outputs/ for inspection"
    )


@pytest.fixture(scope="session")
def output_saver(request):
    """Session-scoped fixture for saving test outputs.

    Creates a TestOutputSaver instance with enabled status determined by
    --save-outputs flag. The saver is shared across all tests in the session.

    Returns:
        TestOutputSaver instance
    """
    enabled = request.config.getoption("--save-outputs")
    return TestOutputSaver(enabled=enabled)


@pytest.fixture
def save_test_output(request, output_saver):
    """Per-test fixture that provides output saving function.

    Provides a convenient function for saving test outputs with automatic
    test name and file extraction.

    Usage in tests:
        def test_foo(save_test_output):
            result = api_call()
            save_test_output(
                raw_response=result,
                extracted_json=extracted_data,
                genes=["GENE1"],
                context="cells"
            )

    Args:
        request: Pytest request object (automatic)
        output_saver: Session-scoped TestOutputSaver instance (automatic)

    Returns:
        Function that saves test output when called
    """
    test_name = request.node.name
    test_file = request.node.fspath.basename

    def _save(raw_response, extracted_json=None, validation_result=None, **context):
        """Save test output if --save-outputs flag is enabled.

        Args:
            raw_response: Raw API response object
            extracted_json: Extracted and parsed JSON (optional)
            validation_result: Validation metadata dict (optional)
            **context: Additional test context (genes, context, preset, etc.)

        Returns:
            Path to output directory if saved, None otherwise
        """
        return output_saver.save_test_output(
            test_name=test_name,
            test_file=test_file,
            raw_response=raw_response,
            extracted_json=extracted_json,
            validation_result=validation_result,
            test_context=context
        )

    return _save
