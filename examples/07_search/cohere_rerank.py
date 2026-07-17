"""Book pages 42-44: rerank retrieved passages with Cohere."""

from __future__ import annotations

import os


def rerank(query: str, documents: list[str]) -> list[int]:
    import cohere

    client = cohere.ClientV2(api_key=os.environ["COHERE_API_KEY"])
    response = client.rerank(model="rerank-v3.5", query=query, documents=documents, top_n=3)
    return [item.index for item in response.results]


documents = ["Vector search finds candidates.", "Reranking improves final ordering.", "Caching reduces repeated cost."]
print(rerank("How do I improve result order?", documents) if os.getenv("AIAP_MODE", "mock") == "live" else [1, 0, 2])
