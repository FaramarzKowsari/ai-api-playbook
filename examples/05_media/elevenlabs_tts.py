"""Book pages 53-60: ElevenLabs text-to-speech using raw HTTP."""

from __future__ import annotations

import os
from pathlib import Path

import httpx


def synthesize(text: str, voice_id: str, destination: Path) -> None:
    response = httpx.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"]},
        params={"output_format": "mp3_44100_128"},
        json={"text": text, "model_id": "eleven_multilingual_v2"},
        timeout=60,
    )
    response.raise_for_status()
    destination.write_bytes(response.content)


if os.getenv("AIAP_MODE", "mock") == "live":
    synthesize("Welcome to the visual AI API playbook.", os.environ["ELEVENLABS_VOICE_ID"], Path("output.mp3"))
else:
    print("MOCK: TTS request accepted; consent and disclosure required for cloned voices")
