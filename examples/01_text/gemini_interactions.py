"""Book pages 13-24: Google Gemini Interactions API.

Official docs: https://ai.google.dev/gemini-api/docs
"""

from __future__ import annotations

import os


def live_example() -> str:
    from google import genai

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Return three risks of launching an AI API product without cost controls.",
    )
    return interaction.output_text


if os.getenv("AIAP_MODE", "mock") == "live":
    print(live_example())
else:
    print("MOCK: uncontrolled retries, unbounded context, and missing per-tenant budgets")
