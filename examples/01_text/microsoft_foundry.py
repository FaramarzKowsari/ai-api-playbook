"""OpenAI-compatible chat request through a Microsoft Foundry deployment.

Set FOUNDRY_BASE_URL to the deployment's OpenAI-compatible root. Endpoint shapes
vary by deployment type, so copy the current base URL from the Foundry portal.
"""

from __future__ import annotations

import os

from openai import OpenAI


def main() -> None:
    endpoint = os.environ["FOUNDRY_BASE_URL"].rstrip("/")
    client = OpenAI(base_url=endpoint, api_key=os.environ["FOUNDRY_API_KEY"])
    response = client.chat.completions.create(
        model=os.environ["FOUNDRY_MODEL"],
        messages=[
            {"role": "system", "content": "Return concise, source-aware answers."},
            {"role": "user", "content": "Give three production checks for an AI API."},
        ],
        temperature=0.2,
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
