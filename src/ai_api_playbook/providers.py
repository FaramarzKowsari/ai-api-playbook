from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProviderSpec:
    name: str
    key_env: str
    api_family: str
    default_model: str
    supports_structured_output: bool = True
    supports_tools: bool = True
    supports_streaming: bool = True


PROVIDERS: dict[str, ProviderSpec] = {
    "openai": ProviderSpec("OpenAI", "OPENAI_API_KEY", "responses", "gpt-5.6-terra"),
    "gemini": ProviderSpec("Google Gemini", "GEMINI_API_KEY", "interactions", "gemini-3.5-flash"),
    "anthropic": ProviderSpec("Anthropic", "ANTHROPIC_API_KEY", "messages", "claude-sonnet-5"),
    "mistral": ProviderSpec("Mistral", "MISTRAL_API_KEY", "chat", "mistral-medium-latest"),
    "foundry": ProviderSpec("Microsoft Foundry", "AZURE_OPENAI_API_KEY", "model-inference", "deployment-name"),
    "huggingface": ProviderSpec("Hugging Face", "HF_TOKEN", "inference-providers", "provider/model"),
}


def get_provider(name: str) -> ProviderSpec:
    try:
        return PROVIDERS[name.lower()]
    except KeyError as exc:
        raise ValueError(f"Unknown provider: {name}") from exc
