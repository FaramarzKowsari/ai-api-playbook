from __future__ import annotations

import json
import os
import time
import uuid
from collections.abc import Callable

from .config import Settings
from .models import AIRequest, AIResponse, Usage
from .providers import get_provider

LiveHandler = Callable[[AIRequest], AIResponse]


class AIClient:
    """Provider-neutral entry point with explicit mock/live behavior."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or Settings.from_env()
        self._handlers: dict[str, LiveHandler] = {}

    def register_live_handler(self, provider: str, handler: LiveHandler) -> None:
        get_provider(provider)
        self._handlers[provider] = handler

    def generate(self, request: AIRequest) -> AIResponse:
        started = time.perf_counter()
        spec = get_provider(request.provider)
        if self.settings.mode == "mock":
            return self._mock_response(request, started)
        if not os.getenv(spec.key_env):
            raise RuntimeError(f"Missing {spec.key_env}; use mock mode or configure the key")
        if request.provider not in self._handlers:
            raise RuntimeError(
                f"No live handler registered for {request.provider}. "
                "Use the focused provider example to register one."
            )
        return self._handlers[request.provider](request)

    @staticmethod
    def _mock_response(request: AIRequest, started: float) -> AIResponse:
        prompt = request.messages[-1].content if request.messages else ""
        structured = None
        if request.response_schema is not None:
            properties = request.response_schema.get("properties", {})
            structured = {key: f"mock-{key}" for key in properties}
            text = json.dumps(structured, ensure_ascii=False)
        else:
            text = f"Mock response for: {prompt[:120]}"
        return AIResponse(
            text=text,
            provider=request.provider,
            model=request.model,
            request_id=f"mock-{uuid.uuid4().hex[:12]}",
            latency_ms=max(1, int((time.perf_counter() - started) * 1000)),
            usage=Usage(input_tokens=max(1, len(prompt) // 4), output_tokens=max(1, len(text) // 4)),
            structured=structured,
            raw={"mode": "mock"},
        )
