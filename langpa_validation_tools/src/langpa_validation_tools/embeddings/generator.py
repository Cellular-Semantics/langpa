"""Embedding generation using OpenAI API."""

from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv

load_dotenv()


class EmbeddingGenerator:
    """Generate embeddings using OpenAI API."""

    def __init__(
        self,
        model: str | None = None,
        api_key: str | None = None
    ) -> None:
        """Initialize embedding generator.

        Args:
            model: OpenAI embedding model (default: text-embedding-3-large)
            api_key: OpenAI API key (default: from OPENAI_API_KEY env var)

        .. code-block:: python

            from langpa.embeddings.generator import EmbeddingGenerator

            gen = EmbeddingGenerator()
            embedding = gen.generate_embedding("DNA Repair")
        """
        self.model = model or os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-large")
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self._client = None  # Lazy-loaded

    @property
    def client(self) -> Any:
        """Lazy-load OpenAI client."""
        if self._client is None:
            try:
                from openai import OpenAI
            except ImportError as e:
                raise ImportError(
                    "OpenAI library not installed. Install with: uv add openai"
                ) from e

            if not self.api_key:
                raise ValueError(
                    "OPENAI_API_KEY not found in environment or constructor"
                )

            self._client = OpenAI(api_key=self.api_key)

        return self._client

    def generate_embedding(self, text: str) -> list[float]:
        """Generate embedding for a single text.

        Args:
            text: Text to embed

        Returns:
            Embedding vector

        .. code-block:: python

            from langpa.embeddings.generator import EmbeddingGenerator

            gen = EmbeddingGenerator()
            embedding = gen.generate_embedding("DNA Repair")
            print(len(embedding))  # 3072
        """
        response = self.client.embeddings.create(
            input=[text],
            model=self.model
        )
        return response.data[0].embedding

    def generate_embeddings(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings for multiple texts (batched).

        Args:
            texts: List of texts to embed

        Returns:
            List of embedding vectors

        .. code-block:: python

            from langpa.embeddings.generator import EmbeddingGenerator

            gen = EmbeddingGenerator()
            texts = ["DNA Repair", "Cell Cycle"]
            embeddings = gen.generate_embeddings(texts)
            print(len(embeddings))  # 2
        """
        response = self.client.embeddings.create(
            input=texts,
            model=self.model
        )
        return [item.embedding for item in response.data]
