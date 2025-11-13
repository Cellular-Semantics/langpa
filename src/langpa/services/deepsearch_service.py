"""DeepSearch service for gene list contextual analysis."""

from __future__ import annotations

from typing import Any, Dict, List, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import will be mocked in unit tests
from deep_research_client import DeepResearchClient  # type: ignore


class DeepSearchService:
    """Service for performing contextual gene list analysis using DeepSearch/Perplexity."""

    def __init__(self, preferred_provider: Optional[str] = None) -> None:
        """Initialize the DeepSearch service.

        Args:
            preferred_provider: Preferred research provider (e.g., 'perplexity', 'openai')
                               If None, uses first available provider.
        """
        self.client = DeepResearchClient()
        self.preferred_provider = preferred_provider
        self._available_providers: Optional[List[str]] = None

    @property
    def available_providers(self) -> List[str]:
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

    def _construct_prompt(self, genes: List[str], context: str) -> str:
        """Construct the research prompt for gene list analysis.

        Based on the prompt template from cellsem-agent for contextual gene analysis.

        Args:
            genes: List of gene symbols to analyze
            context: Biological context for the analysis

        Returns:
            Formatted prompt for DeepSearch API
        """
        genes_str = ", ".join(genes)

        prompt = f"""Perform a comprehensive literature-based functional analysis of the gene list: {genes_str}

Biological Context: {context}

Analysis Requirements:
1. Search scientific literature for each gene's functional roles and interactions
2. Identify gene clusters or programs - groups of genes acting together in pathways, processes, or cellular states
3. For each program identified, predict functional implications in the specified biological context
4. Prioritize well-established functions with strong literature support
5. Highlight emerging evidence if contextually relevant
6. Rank predictions higher when:
   - Multiple genes from the input list act in the same process
   - Most/all required pathway components are present

Analysis Strategy:
- Anchor predictions in normal physiology or disease-specific alterations as appropriate for the context
- Connect gene-level roles to program-level implications
- Consider gene interactions and regulatory networks
- Highlight collective evidence that supports coordinated gene function
- Ensure all claims are backed by experimental evidence

Please provide a systematic analysis that identifies biological programs and their predicted cellular impacts within the given context. Focus on evidence-based interpretation of how these genes work together to influence cellular behavior."""

        return prompt

    def research_gene_list(
        self,
        genes: List[str],
        context: str,
        provider: Optional[str] = None
    ) -> Any:
        """Perform contextual research analysis of a gene list.

        Args:
            genes: List of gene symbols to analyze (e.g., ["TP53", "BRCA1"])
            context: Biological context for analysis (e.g., "cancer", "tumor suppressor genes")
            provider: Optional override for research provider

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
            # Perform research
            result = self.client.research(
                query=prompt,
                provider=research_provider
            )
            return result

        except Exception as e:
            # Re-raise with context
            raise Exception(f"DeepSearch API error: {str(e)}") from e