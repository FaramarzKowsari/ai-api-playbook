from __future__ import annotations

import math
import re
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Chunk:
    id: str
    text: str
    start: int
    end: int


def chunk_text(text: str, *, target_chars: int = 800, overlap_chars: int = 120) -> list[Chunk]:
    if target_chars < 100:
        raise ValueError("target_chars must be at least 100")
    if not 0 <= overlap_chars < target_chars:
        raise ValueError("overlap_chars must be in [0, target_chars)")
    clean = re.sub(r"\s+", " ", text).strip()
    chunks: list[Chunk] = []
    start = 0
    while start < len(clean):
        tentative = min(len(clean), start + target_chars)
        end = tentative
        if tentative < len(clean):
            sentence = clean.rfind(". ", start, tentative)
            if sentence > start + target_chars // 2:
                end = sentence + 1
        chunks.append(Chunk(f"chunk-{len(chunks)+1:04d}", clean[start:end], start, end))
        if end >= len(clean):
            break
        next_start = max(start + 1, end - overlap_chars)
        boundary = clean.find(" ", next_start, end)
        start = boundary + 1 if boundary != -1 else next_start
    return chunks


def cosine_similarity(a: list[float], b: list[float]) -> float:
    if len(a) != len(b) or not a:
        raise ValueError("vectors must be non-empty and equal length")
    dot = sum(x * y for x, y in zip(a, b, strict=True))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def reciprocal_rank_fusion(rankings: list[list[str]], *, k: int = 60) -> list[tuple[str, float]]:
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, document_id in enumerate(ranking, start=1):
            scores[document_id] = scores.get(document_id, 0.0) + 1 / (k + rank)
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)
