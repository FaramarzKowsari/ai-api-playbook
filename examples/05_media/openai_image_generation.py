"""Book pages 50-52: OpenAI image generation through Responses."""

from __future__ import annotations

import os


def generate() -> None:
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.responses.create(
        model="gpt-5.6-terra",
        input="Create a clean editorial product illustration of an AI API pipeline.",
        tools=[{"type": "image_generation"}],
    )
    image_calls = [item for item in response.output if item.type == "image_generation_call"]
    print(f"generated images: {len(image_calls)}")


print("MOCK: image generation request validated" if os.getenv("AIAP_MODE", "mock") != "live" else "")
if os.getenv("AIAP_MODE", "mock") == "live":
    generate()
