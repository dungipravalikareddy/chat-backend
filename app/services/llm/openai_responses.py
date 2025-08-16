import requests, backoff
from typing import List, Tuple, Dict, Any
from app.services.interfaces.llm_client import LLMClient
from app.models.schemas import Message
from app.core.config import get_settings

class OpenAIResponsesClient(LLMClient):
    def __init__(self):
        self.settings = get_settings()
        self.session = requests.Session()
        self.url = f"{self.settings.OPENAI_BASE_URL}/responses"
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
        # Convert chat history into a single prompt (simple strategy)
        # You can also send as "input": [{"role":..., "content":[{"type":"text","text":...}]}]
        text = "\n".join(f"{m.role.upper()}: {m.content}" for m in messages)
        payload = {
            "model": self.settings.OPENAI_MODEL,
            "input": text,
            "temperature": temperature,
        }
        out = self._post(payload)
        # Responses API returns output (may be in a nested format depending on tools)
        reply = out["output"][0]["content"][0]["text"] if "output" in out else out["response"]
        usage = out.get("usage", {})
        return reply, usage
