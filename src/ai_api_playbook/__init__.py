"""Production-minded, provider-neutral patterns for modern AI APIs."""

from .client import AIClient
from .config import Settings
from .models import AIRequest, AIResponse, Message

__all__ = ["AIClient", "AIRequest", "AIResponse", "Message", "Settings"]
__version__ = "1.0.0"
