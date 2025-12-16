"""Ontology mapping agent using pydantic-ai.

This module provides the main agent for mapping biological terms to
standardized ontology identifiers (GO, CL, UBERON, ChEBI).
"""

from __future__ import annotations

import json
from typing import List

from pydantic_ai import Agent

from .config import OntologyMappingDependencies
from .models import OntologyMappingResponse
from .tools import search_chebi, search_cl, search_go, search_uberon

SYSTEM_PROMPT = """
You are an expert bioinformatics specialist focused on mapping biological terms to Gene Ontology (GO).

Your task is to map atomic biological processes and cellular components to appropriate GO terms:
- **Biological processes** -> GO biological process (e.g., "neutrophil chemotaxis" -> GO:0030593)
- **Cellular components** -> GO cellular component (e.g., "neutrophil cytosol" -> GO:0005829)
- **Molecular functions** -> GO molecular function (e.g., "kinase activity" -> GO:0016301)

**For each input term, you must**:
1. Search GO using the available search tools
2. Select the best match based on semantic similarity and biological accuracy
3. Assign confidence scores (0.0-1.0) based on match quality
4. Document the mapping method used (e.g., "exact_match", "partial_match", "synonym_match")

**Search Strategy**:
- Try multiple search variations if initial search fails
- Convert plurals to singular
- Try alternative phrasings (e.g., "X of Y" vs "Y X")
- Break down compound terms if no direct match found
- If no suitable match found, set ontology_id to None

**Output Format**:
For each input term, create an OntologyMapping with:
- `term`: The input term exactly as provided
- `ontology_id`: The matched GO term ID (e.g., "GO:0008150") or None
- `ontology_label`: The official label from GO or None
- `ontology_source`: "GO"
- `confidence`: Float from 0.0 to 1.0
- `mapping_method`: Description of how the match was found

Available tools: search_go, search_cl, search_uberon, search_chebi
"""


def build_ontology_mapping_agent(
    model: str = "openai:gpt-4o"
) -> Agent[OntologyMappingDependencies, OntologyMappingResponse]:
    """Build an ontology mapping agent using pydantic-ai.

    Creates a pydantic-ai agent configured for mapping biological terms to
    ontology identifiers. The agent uses OAKlib tools to search multiple
    ontologies and an LLM to intelligently select the best matches.

    Args:
        model: LLM model to use (default: openai:gpt-4o).
            Supports any pydantic-ai model string format.

    Returns:
        Configured pydantic-ai Agent instance ready for mapping

    Example:
        .. code-block:: python

            agent = build_ontology_mapping_agent()
            deps = OntologyMappingDependencies.from_env()
            result = agent.run_sync(
                "Map these terms: neutrophil chemotaxis, cell migration",
                deps=deps
            )
            print(result.data.mappings)
    """
    agent = Agent(
        model,
        deps_type=OntologyMappingDependencies,
        output_type=OntologyMappingResponse,
        system_prompt=SYSTEM_PROMPT,
    )

    # Register OAKlib search tools
    agent.tool(search_go)
    agent.tool(search_cl)
    agent.tool(search_uberon)
    agent.tool(search_chebi)

    return agent


def map_terms_to_go(
    terms: List[str],
    agent: Agent,
    deps: OntologyMappingDependencies
) -> OntologyMappingResponse:
    """Map biological terms to GO identifiers.

    Convenience function that formats the input terms and runs the agent
    to perform ontology mapping.

    Args:
        terms: List of biological terms to map
        agent: pydantic-ai agent instance (from build_ontology_mapping_agent)
        deps: Dependencies for the agent (from OntologyMappingDependencies.from_env)

    Returns:
        OntologyMappingResponse with mappings for each input term

    Example:
        .. code-block:: python

            agent = build_ontology_mapping_agent()
            deps = OntologyMappingDependencies.from_env()
            response = map_terms_to_go(
                ["neutrophil chemotaxis", "NF-�B pathway"],
                agent,
                deps
            )

            for mapping in response.mappings:
                print(f"{mapping.term} � {mapping.ontology_id}")
    """
    # Format terms as JSON for the agent
    user_prompt = f"Map these biological terms to GO: {json.dumps(terms)}"

    # Run agent with dependencies
    result = agent.run_sync(user_prompt, deps=deps)

    return result.data
