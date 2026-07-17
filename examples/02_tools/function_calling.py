"""Book pages 25-28: validate a tool call before execution."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: dict[str, Any]


ALLOWED_CURRENCIES = {"USD", "EUR", "TRY"}


def quote_price(product_id: str, currency: str) -> dict[str, str | float]:
    if not product_id.startswith("prod_"):
        raise ValueError("invalid product_id")
    if currency not in ALLOWED_CURRENCIES:
        raise ValueError("unsupported currency")
    return {"product_id": product_id, "currency": currency, "price": 29.0}


def execute(call: ToolCall) -> dict[str, str | float]:
    if call.name != "quote_price":
        raise PermissionError("tool is not allow-listed")
    return quote_price(str(call.arguments["product_id"]), str(call.arguments["currency"]))


print(execute(ToolCall("quote_price", {"product_id": "prod_book", "currency": "USD"})))
