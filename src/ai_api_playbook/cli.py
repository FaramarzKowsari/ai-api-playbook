from __future__ import annotations

import argparse
import json

from .client import AIClient
from .config import Settings
from .economics import UnitEconomics
from .models import AIRequest
from .rag import chunk_text


def demo() -> None:
    settings = Settings.from_env()
    client = AIClient(settings)
    request = AIRequest.from_prompt(
        "Extract a product name and one measurable benefit.",
        provider=settings.provider,
        model="configured-model",
    )
    response = client.generate(request)
    chunks = chunk_text("AI APIs become valuable when they solve a recurring customer problem. " * 20)
    economics = UnitEconomics(price_usd=29, api_cost_usd=1.2, infrastructure_usd=0.8, support_usd=2)
    print(
        json.dumps(
            {
                "mode": settings.mode,
                "response": response.text,
                "request_id": response.request_id,
                "chunks": len(chunks),
                "gross_margin_percent": round(economics.gross_margin_percent, 1),
            },
            indent=2,
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="AI APIs in Practice companion CLI")
    parser.add_argument("command", choices=["demo"], nargs="?", default="demo")
    args = parser.parse_args()
    if args.command == "demo":
        demo()


if __name__ == "__main__":
    main()
