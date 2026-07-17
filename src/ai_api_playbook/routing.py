from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ModelCandidate:
    provider: str
    model: str
    quality: float
    latency_ms: int
    cost_per_million_output_tokens: float
    available: bool = True


def choose_model(candidates: list[ModelCandidate], *, strategy: str = "balanced") -> ModelCandidate:
    available = [candidate for candidate in candidates if candidate.available]
    if not available:
        raise RuntimeError("No model candidate is available")
    if strategy == "quality":
        return max(available, key=lambda item: item.quality)
    if strategy == "latency":
        return min(available, key=lambda item: item.latency_ms)
    if strategy == "cost":
        return min(available, key=lambda item: item.cost_per_million_output_tokens)
    if strategy != "balanced":
        raise ValueError("strategy must be quality, latency, cost, or balanced")

    def score(item: ModelCandidate) -> float:
        latency_penalty = min(item.latency_ms / 10_000, 1)
        cost_penalty = min(item.cost_per_million_output_tokens / 100, 1)
        return 0.65 * item.quality - 0.20 * latency_penalty - 0.15 * cost_penalty

    return max(available, key=score)
