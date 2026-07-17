"""Book pages 13-24: OpenAI Responses API with structured output.

Official docs: https://developers.openai.com/api/docs/guides/migrate-to-responses
Set AIAP_MODE=live and OPENAI_API_KEY to run the live path.
"""

from __future__ import annotations

import json
import os

from ai_api_playbook import AIClient, AIRequest, AIResponse, Message, Settings
from ai_api_playbook.models import Usage


def openai_handler(request: AIRequest) -> AIResponse:
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.responses.create(
        model=request.model,
        input=[{"role": message.role, "content": message.content} for message in request.messages],
        text={"format": {"type": "json_schema", "name": "product", "schema": request.response_schema, "strict": True}},
    )
    parsed = json.loads(response.output_text)
    return AIResponse(
        text=response.output_text,
        structured=parsed,
        provider="openai",
        model=request.model,
        request_id=response.id,
        latency_ms=0,
        usage=Usage(
            input_tokens=getattr(response.usage, "input_tokens", 0),
            output_tokens=getattr(response.usage, "output_tokens", 0),
        ),
        raw={"status": getattr(response, "status", "completed")},
    )


settings = Settings.from_env()
client = AIClient(settings)
if settings.mode == "live":
    client.register_live_handler("openai", openai_handler)

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "benefit": {"type": "string"},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
    },
    "required": ["name", "benefit", "confidence"],
    "additionalProperties": False,
}

result = client.generate(
    AIRequest(
        provider="openai",
        model="gpt-5.6-terra",
        messages=(Message("user", "Extract the product and measurable benefit: Acme cuts review time by 42%."),),
        response_schema=schema,
    )
)
print(result.structured or result.text)
