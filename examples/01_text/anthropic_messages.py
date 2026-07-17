"""Book pages 13-24: Anthropic Messages API."""

from __future__ import annotations

import os


def live_example() -> str:
    import anthropic

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=500,
        system="Answer as a concise API architecture reviewer.",
        messages=[{"role": "user", "content": "Review a RAG system with no citation tracking."}],
    )
    return "".join(block.text for block in message.content if block.type == "text")


print(live_example() if os.getenv("AIAP_MODE", "mock") == "live" else "MOCK: add source IDs and citation spans.")
