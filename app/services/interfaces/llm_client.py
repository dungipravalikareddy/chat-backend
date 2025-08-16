from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, Any
from app.models.schemas import Message

class LLMClient(ABC):
    @abstractmethod
    def complete(self, messages: List[Message], temperature: float = 0.7) -> Tuple[str, Dict[str, Any]]:
        """Return (reply, usage)."""
        raise NotImplementedError
