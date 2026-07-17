from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _load_dotenv(path: Path = Path(".env")) -> None:
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


@dataclass(frozen=True, slots=True)
class Settings:
    mode: str = "mock"
    provider: str = "openai"
    timeout_seconds: float = 30.0
    max_retries: int = 3
    monthly_budget_usd: float = 25.0

    @classmethod
    def from_env(cls, *, load_dotenv: bool = True) -> "Settings":
        if load_dotenv:
            _load_dotenv()
        return cls(
            mode=os.getenv("AIAP_MODE", "mock").lower(),
            provider=os.getenv("AIAP_PROVIDER", "openai").lower(),
            timeout_seconds=float(os.getenv("AIAP_TIMEOUT_SECONDS", "30")),
            max_retries=int(os.getenv("AIAP_MAX_RETRIES", "3")),
            monthly_budget_usd=float(os.getenv("AIAP_MONTHLY_BUDGET_USD", "25")),
        )

    def require_live_key(self, env_name: str) -> str:
        value = os.getenv(env_name, "").strip()
        if self.mode == "live" and not value:
            raise RuntimeError(f"{env_name} is required in live mode")
        return value
