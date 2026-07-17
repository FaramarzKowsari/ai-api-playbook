from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

Role = Literal["system", "developer", "user", "assistant", "tool"]


@dataclass(frozen=True, slots=True)
class Message:
    role: Role
    content: str


@dataclass(frozen=True, slots=True)
class ToolDefinition:
    name: str
    description: str
    input_schema: dict[str, Any]


@dataclass(frozen=True, slots=True)
class AIRequest:
    messages: tuple[Message, ...]
    model: str
    provider: str
    temperature: float = 0.2
    max_output_tokens: int = 800
    response_schema: dict[str, Any] | None = None
    tools: tuple[ToolDefinition, ...] = ()
    metadata: dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_prompt(cls, prompt: str, *, model: str, provider: str) -> "AIRequest":
        return cls(messages=(Message("user", prompt),), model=model, provider=provider)


@dataclass(frozen=True, slots=True)
class Usage:
    input_tokens: int = 0
    output_tokens: int = 0
    estimated_cost_usd: float = 0.0


@dataclass(frozen=True, slots=True)
class AIResponse:
    text: str
    provider: str
    model: str
    request_id: str
    latency_ms: int
    usage: Usage = Usage()
    structured: dict[str, Any] | None = None
    raw: dict[str, Any] = field(default_factory=dict)
