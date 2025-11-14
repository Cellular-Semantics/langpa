"""DeepSearch service for gene list contextual analysis."""

from __future__ import annotations

from typing import Any

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import will be mocked in unit tests
import json

from deep_research_client import DeepResearchClient  # type: ignore

from langpa.schemas import load_schema


class DeepSearchService:
    """Service for performing contextual gene list analysis using DeepSearch/Perplexity."""

    def __init__(self, preferred_provider: str | None = None) -> None:
        """Initialize the DeepSearch service.

        Args:
            preferred_provider: Preferred research provider (e.g., 'perplexity', 'openai')
                               If None, uses first available provider.
        """
        self.client = DeepResearchClient()
        self.preferred_provider = preferred_provider
        self._available_providers: list[str] | None = None

    @property
    def available_providers(self) -> list[str]:
        """Get list of available research providers."""
        if self._available_providers is None:
            self._available_providers = self.client.get_available_providers()
        return self._available_providers

    def _get_provider(self) -> str:
        """Get the provider to use for research."""
        providers = self.available_providers

        if not providers:
            raise ValueError("No research providers available. Check API key configuration.")

        if self.preferred_provider and self.preferred_provider in providers:
            return self.preferred_provider

        # Default preference order: perplexity first (cheaper), then others
        if "perplexity" in providers:
            return "perplexity"

        return providers[0]

    def _construct_prompt(self, genes: list[str], context: str) -> str:
        """Construct the research prompt for gene list analysis.

        Uses exact cellsem-agent template with embedded schema for JSON output.

        Args:
            genes: List of gene symbols to analyze
            context: Biological context for the analysis

        Returns:
            Formatted prompt for DeepSearch API with embedded schema
        """
        genes_str = ", ".join(genes)

        prompt = f"""Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: {genes_str}

**Biological Context**: {context}

**Analysis Strategy**:
1. Search current scientific literature for functional roles of each gene in the input list
2. Identify clusters of genes that act together in pathways, processes, or cellular states
3. Treat each cluster as a potential gene program within the list
4. Interpret findings in light of both normal physiological roles and disease-specific alterations
5. Prioritize well-established functions with strong literature support, but highlight emerging evidence if contextually relevant

**Guidelines**:
* Anchor all predictions in either the normal physiology and development of the cell type and tissue specified in the context OR the alterations and dysregulations characteristic of the specified disease
* Connect gene-level roles to program-level implications
* Consider gene interactions, regulatory networks, and pathway dynamics
* Highlight cases where multiple genes collectively strengthen evidence
* Ensure all claims are backed by experimental evidence with proper attribution

Provide a structured analysis identifying biological programs and their predicted cellular impacts within the given context."""

        return prompt

    def research_gene_list(
        self, genes: list[str], context: str, provider: str | None = None, timeout: int = 180
    ) -> Any:
        """Perform contextual research analysis of a gene list.

        Args:
            genes: List of gene symbols to analyze (e.g., ["TP53", "BRCA1"])
            context: Biological context for analysis (e.g., "cancer", "tumor suppressor genes")
            provider: Optional override for research provider
            timeout: Timeout in seconds for the API call (default 180s)

        Returns:
            ResearchResult object with content and citations

        Raises:
            ValueError: If genes list is empty or context is empty
            Exception: If API call fails
        """
        # Input validation
        if not genes:
            raise ValueError("Genes list cannot be empty")

        if not context or not context.strip():
            raise ValueError("Context cannot be empty")

        # Construct research query
        prompt = self._construct_prompt(genes, context)

        # Determine provider
        research_provider = provider or self._get_provider()

        try:
            # Load schema for response_format
            schema = load_schema("deepsearch_results_schema.json")

            # Try Option 2: Use sonar-reasoning-pro with enhanced parameters
            result = self.client.research(
                query=prompt,
                provider=research_provider,
                model="sonar-reasoning-pro",  # Different model for better JSON compliance
                provider_params={
                    "return_citations": True,
                    "search_domain_filter": [
                        "pubmed.ncbi.nlm.nih.gov",
                        "ncbi.nlm.nih.gov/pmc/",
                        "www.ncbi.nlm.nih.gov",
                        "europepmc.org",
                        "biorxiv.org",
                        "nature.com",
                        "cell.com",
                        "science.org",
                    ],
                    "reasoning_effort": "high",  # Increase reasoning depth
                    "search_recency_filter": "month",  # Focus on recent research
                    "system_prompt": f"""You are an expert biologist. Analyze the provided genes in the given biological context.

CRITICAL: Respond ONLY with valid JSON that exactly follows this schema structure:
{json.dumps(schema, indent=2)}

Do not include any prose, markdown, explanatory text, or <think> tags. Only the JSON structure.""",
                },
            )
            return result

        except Exception as e:
            # Re-raise with context
            raise Exception(f"DeepSearch API error: {str(e)}") from e
