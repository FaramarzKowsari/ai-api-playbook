"""Book pages 53-60: Deepgram prerecorded transcription via raw HTTP."""

from __future__ import annotations

import os
from pathlib import Path

import httpx


def transcribe(audio_path: Path) -> dict:
    with audio_path.open("rb") as audio:
        response = httpx.post(
            "https://api.deepgram.com/v1/listen",
            headers={"Authorization": f"Token {os.environ['DEEPGRAM_API_KEY']}", "Content-Type": "audio/mpeg"},
            params={"smart_format": "true", "diarize": "true"},
            content=audio.read(),
            timeout=120,
        )
    response.raise_for_status()
    return response.json()


print("MOCK: transcript with timestamps and speakers" if os.getenv("AIAP_MODE", "mock") != "live" else transcribe(Path("sample.mp3")))
