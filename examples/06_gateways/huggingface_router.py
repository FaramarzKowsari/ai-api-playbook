"""Book page 24: unified model routing with Hugging Face Inference Providers."""

from __future__ import annotations

import os


def run() -> str:
    from huggingface_hub import InferenceClient

    client = InferenceClient(api_key=os.environ["HF_TOKEN"])
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b:fastest",
        messages=[{"role": "user", "content": "Explain provider routing in one sentence."}],
    )
    return completion.choices[0].message.content


print(run() if os.getenv("AIAP_MODE", "mock") == "live" else "MOCK: one token, multiple inference providers")
