from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any

SECRET_PATTERNS = (
    re.compile(r"(?i)(bearer\s+)[a-z0-9._~-]+"),
    re.compile(r"(?i)(api[_-]?key\s*[=:]\s*)[^\s,;]+"),
    re.compile(r"(?i)(authorization\s*[=:]\s*)[^\s,;]+"),
)
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE = re.compile(r"(?<!\d)(?:\+?\d[\d .()-]{7,}\d)(?!\d)")


def redact_text(text: str) -> str:
    result = text
    for pattern in SECRET_PATTERNS:
        result = pattern.sub(r"\1[REDACTED]", result)
    result = EMAIL.sub("[EMAIL]", result)
    result = PHONE.sub("[PHONE]", result)
    return result


def redact_mapping(data: Mapping[str, Any]) -> dict[str, Any]:
    sensitive = {"authorization", "api_key", "apikey", "token", "secret", "cookie"}
    result: dict[str, Any] = {}
    for key, value in data.items():
        if key.lower() in sensitive:
            result[key] = "[REDACTED]"
        elif isinstance(value, str):
            result[key] = redact_text(value)
        elif isinstance(value, Mapping):
            result[key] = redact_mapping(value)
        else:
            result[key] = value
    return result


def contains_prompt_injection(text: str) -> bool:
    signals = (
        "ignore previous instructions",
        "reveal the system prompt",
        "exfiltrate",
        "send the api key",
        "override your rules",
    )
    normalized = text.casefold()
    return any(signal in normalized for signal in signals)
