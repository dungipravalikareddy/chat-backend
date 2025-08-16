from typing import List, Tuple, Dict, Any
from app.models.schemas import Message, ChatRequest
from app.services.interfaces.llm_client import LLMClient
from app.core.config import get_settings
from app.services.llm.factory import get_llm_client

class ChatService:
    _instance = None

    def __init__(self, llm: LLMClient):
        self.llm = llm
        self.settings = get_settings()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = ChatService(llm=get_llm_client())
        return cls._instance

    def build_messages(self, req: ChatRequest) -> list[Message]:
        persona = req.persona or self.settings.DEFAULT_PERSONA
        persona_prompts = self.settings.personas()
        system_prompt = persona_prompts.get(
            persona, persona_prompts[self.settings.DEFAULT_PERSONA]
        )

        system = Message(role="system", content=system_prompt)

        return [system, *req.history, Message(role="user", content=req.message)]


    def chat(self, req: ChatRequest) -> Tuple[str, str, float]:
        persona = req.persona or self.settings.DEFAULT_PERSONA
        temperature = (
            req.temperature
            if req.temperature is not None
            else self.settings.DEFAULT_TEMPERATURE
        )
        messages = self.build_messages(req)
        response, _ = self.llm.complete(messages, temperature=temperature)
        return response, persona, temperature

    @classmethod
    def get_response(cls, req: ChatRequest) -> dict:
        response, persona, temperature = cls.instance().chat(req)
        return {
            "reply": response,
            "persona": persona,
            "temperature": temperature,
    }

