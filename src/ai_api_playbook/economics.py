from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class UnitEconomics:
    price_usd: float
    api_cost_usd: float
    infrastructure_usd: float = 0.0
    support_usd: float = 0.0
    payment_fees_usd: float = 0.0

    @property
    def variable_cost_usd(self) -> float:
        return self.api_cost_usd + self.infrastructure_usd + self.support_usd + self.payment_fees_usd

    @property
    def gross_profit_usd(self) -> float:
        return self.price_usd - self.variable_cost_usd

    @property
    def gross_margin_percent(self) -> float:
        if self.price_usd <= 0:
            return 0.0
        return 100 * self.gross_profit_usd / self.price_usd

    @property
    def break_even_jobs(self) -> int | None:
        if self.gross_profit_usd <= 0:
            return None
        return 1
