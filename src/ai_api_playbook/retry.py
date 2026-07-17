from __future__ import annotations

import random
import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def retry_with_backoff(
    operation: Callable[[], T],
    *,
    attempts: int = 3,
    base_delay_seconds: float = 0.25,
    max_delay_seconds: float = 4.0,
    retry_on: tuple[type[Exception], ...] = (TimeoutError, ConnectionError),
) -> T:
    """Retry transient failures with exponential backoff and full jitter."""
    if attempts < 1:
        raise ValueError("attempts must be at least 1")
    for attempt in range(attempts):
        try:
            return operation()
        except retry_on:
            if attempt == attempts - 1:
                raise
            ceiling = min(max_delay_seconds, base_delay_seconds * (2**attempt))
            time.sleep(random.uniform(0.0, ceiling))
    raise AssertionError("unreachable")
