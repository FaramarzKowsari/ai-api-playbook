"""Book pages 45-49: Mistral Document AI OCR via raw HTTP.

Official docs: https://docs.mistral.ai/studio-api/document-processing/basic_ocr
"""

from __future__ import annotations

import os

import httpx


def extract_pdf(document_url: str) -> dict:
    response = httpx.post(
        "https://api.mistral.ai/v1/ocr",
        headers={"Authorization": f"Bearer {os.environ['MISTRAL_API_KEY']}"},
        json={
            "model": "mistral-ocr-latest",
            "document": {"type": "document_url", "document_url": document_url},
            "include_image_base64": False,
        },
        timeout=90,
    )
    response.raise_for_status()
    return response.json()


if os.getenv("AIAP_MODE", "mock") == "live":
    print(extract_pdf("https://example.com/authorized-document.pdf").keys())
else:
    print({"pages": [{"index": 0, "markdown": "# Mock extracted document"}]})
