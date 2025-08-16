import requests, backoff
from typing import List, Tuple, Dict, Any
from app.services.interfaces.llm_client import LLMClient
from app.models.schemas import Message
from app.core.config import get_settings

class OpenAIChatCompletionsClient(LLMClient):
    def __init__(self):
        self.settings = get_settings()
        self.session = requests.Session()
        self.url = f"{self.settings.OPENAI_BASE_URL}/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.settings.OPENAI_API_KEY}",
            "Content-Type": "application/json",
        }

    @backoff.on_exception(backoff.expo, (requests.RequestException,), max_tries=3)
    def _post(self, payload):
        resp = self.session.post(self.url, headers=self.headers, json=payload, timeout=60)
        resp.raise_for_status()
        return resp.json()

    def complete(self, messages: List[Message], temperature: float = 0.7) -> Tuple[str, Dict[str, Any]]:
        data = {
            "model": self.settings.OPENAI_MODEL,
            "messages": [m.model_dump() for m in messages],
            "temperature": temperature,
        }
        out = self._post(data)
        reply = out["choices"][0]["message"]["content"]
        usage = out.get("usage", {})
        return reply, usage
