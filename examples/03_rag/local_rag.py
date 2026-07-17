"""Book pages 35-44: a deterministic, dependency-free RAG teaching example."""

from __future__ import annotations

import re
from collections import Counter

from ai_api_playbook.rag import chunk_text, cosine_similarity


def embed(text: str, vocabulary: list[str]) -> list[float]:
    tokens = Counter(re.findall(r"[a-z]+", text.lower()))
    return [float(tokens[word]) for word in vocabulary]


document = """
RAG combines retrieval with generation. Chunking controls the evidence unit.
Metadata filters constrain the search space. Reranking improves the final order.
Answers should retain source identifiers so claims can be audited.
"""
query = "How can a RAG answer be audited?"
chunks = chunk_text(document, target_chars=120, overlap_chars=20)
vocabulary = sorted(set(re.findall(r"[a-z]+", (document + query).lower())))
query_vector = embed(query, vocabulary)
ranked = sorted(
    ((chunk, cosine_similarity(query_vector, embed(chunk.text, vocabulary))) for chunk in chunks),
    key=lambda item: item[1],
    reverse=True,
)
for chunk, score in ranked[:2]:
    print(chunk.id, round(score, 3), chunk.text)
