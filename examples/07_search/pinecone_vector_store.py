"""Book pages 39-41: upsert and query vectors with Pinecone."""

from __future__ import annotations

import os


def query(vector: list[float]) -> dict:
    from pinecone import Pinecone

    index = Pinecone(api_key=os.environ["PINECONE_API_KEY"]).Index(os.environ["PINECONE_INDEX"])
    result = index.query(vector=vector, top_k=5, include_metadata=True, filter={"language": {"$eq": "en"}})
    return result.to_dict()


print("MOCK: five metadata-filtered candidates" if os.getenv("AIAP_MODE", "mock") != "live" else query([0.0] * 1536))
