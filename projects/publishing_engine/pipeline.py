from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path

from ai_api_playbook.rag import chunk_text


@dataclass(frozen=True, slots=True)
class BookMetadata:
    title: str
    subtitle: str
    author: str
    language: str
    description: str
    keywords: tuple[str, ...]


def validate_source(text: str) -> None:
    if len(text.strip()) < 100:
        raise ValueError("source is too short for a publishing package")
    if "BEGIN PRIVATE KEY" in text or "api_key=" in text.lower():
        raise ValueError("source appears to contain a secret")


def build_package(text: str) -> dict:
    validate_source(text)
    fingerprint = hashlib.sha256(text.encode()).hexdigest()[:16]
    chunks = chunk_text(text, target_chars=700, overlap_chars=100)
    metadata = BookMetadata(
        title="AI APIs in Practice",
        subtitle="A Visual Guide to Multimodal, Agentic, and Revenue-Ready Applications",
        author="Faramarz Kowsari",
        language="en",
        description="A practical visual guide to building reliable AI API products.",
        keywords=("AI APIs", "agents", "RAG", "multimodal AI", "voice AI"),
    )
    return {
        "source_fingerprint": fingerprint,
        "metadata": asdict(metadata),
        "rag_manifest": [{"id": chunk.id, "start": chunk.start, "end": chunk.end} for chunk in chunks],
        "review_gates": [
            "metadata factual review",
            "rights and consent review",
            "privacy and secret scan",
            "cost approval",
            "final publication approval",
        ],
    }


if __name__ == "__main__":
    sample = " ".join(
        [
            "AI APIs create commercial value when a measurable customer problem is solved reliably.",
            "A production system validates structured output, records evidence, controls cost, and protects data.",
        ]
        * 15
    )
    package = build_package(sample)
    output = Path("publishing-package.json")
    output.write_text(json.dumps(package, indent=2), encoding="utf-8")
    print(output.resolve())
