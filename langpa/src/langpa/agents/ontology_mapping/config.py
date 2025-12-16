"""Configuration and dependencies for the ontology mapping agent.

This module provides configuration management for the ontology mapping agent,
including environment variable loading and dependency injection.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import List

from dotenv import load_dotenv


@dataclass
class OntologyMappingDependencies:
    """Dependencies available to the ontology mapping agent during execution.

    This dataclass follows the pydantic-ai dependency injection pattern, providing
    configuration and runtime dependencies to the agent.

    Attributes:
        target_ontologies: List of ontology names to search (e.g., ["GO", "CL"])
        workdir: Working directory for outputs and cache

    Example:
        .. code-block:: python

            from dotenv import load_dotenv
            load_dotenv()

            deps = OntologyMappingDependencies.from_env()
            print(deps.target_ontologies)  # ['GO', 'CL', 'UBERON', 'ChEBI']
    """

    target_ontologies: List[str]
    workdir: Path

    @classmethod
    def from_env(cls) -> "OntologyMappingDependencies":
        """Load configuration from environment variables.

        Loads environment variables from .env file if present and creates
        configuration with sensible defaults.

        Environment variables:
            WORKDIR: Working directory for outputs (default: ./workdir)
            TARGET_ONTOLOGIES: Comma-separated ontology list (default: GO,CL,UBERON,ChEBI)

        Returns:
            OntologyMappingDependencies instance with loaded configuration

        Example:
            .. code-block:: python

                # With .env file containing:
                # WORKDIR=/tmp/ontology
                # TARGET_ONTOLOGIES=GO,CL

                deps = OntologyMappingDependencies.from_env()
                assert deps.workdir == Path("/tmp/ontology")
                assert deps.target_ontologies == ["GO", "CL"]
        """
        load_dotenv()

        workdir = Path(os.getenv("WORKDIR", "./workdir"))
        workdir.mkdir(exist_ok=True, parents=True)

        ontologies = os.getenv("TARGET_ONTOLOGIES", "GO,CL,UBERON,ChEBI").split(",")

        return cls(
            target_ontologies=[o.strip() for o in ontologies],
            workdir=workdir
        )
