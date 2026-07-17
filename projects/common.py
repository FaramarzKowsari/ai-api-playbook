from __future__ import annotations

from dataclasses import asdict, dataclass

from ai_api_playbook.economics import UnitEconomics


@dataclass(frozen=True, slots=True)
class ProductBlueprint:
    name: str
    buyer: str
    pain: str
    measurable_outcome: str
    human_approval_gate: str
    price_usd: float
    estimated_api_cost_usd: float
    infrastructure_usd: float
    support_usd: float

    def report(self) -> dict:
        unit = UnitEconomics(
            self.price_usd,
            self.estimated_api_cost_usd,
            self.infrastructure_usd,
            self.support_usd,
        )
        return {
            **asdict(self),
            "gross_profit_usd": round(unit.gross_profit_usd, 2),
            "gross_margin_percent": round(unit.gross_margin_percent, 1),
        }
