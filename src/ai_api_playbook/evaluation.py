from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EvaluationResult:
    groundedness: float
    completeness: float
    format_validity: float
    safety: float
    latency_ms: int
    cost_usd: float

    @property
    def quality_score(self) -> float:
        return round(
            0.35 * self.groundedness
            + 0.30 * self.completeness
            + 0.20 * self.format_validity
            + 0.15 * self.safety,
            3,
        )


def keyword_coverage(answer: str, required_terms: set[str]) -> float:
    if not required_terms:
        return 1.0
    normalized = answer.casefold()
    hits = sum(term.casefold() in normalized for term in required_terms)
    return hits / len(required_terms)
