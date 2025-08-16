from functools import lru_cache
from app.core.config import get_settings
from app.services.llm.openai_chat_completions import OpenAIChatCompletionsClient
from app.services.llm.openai_responses import OpenAIResponsesClient
from app.services.interfaces.llm_client import LLMClient

@lru_cache
def get_llm_client() -> LLMClient:
    api_type = get_settings().OPENAI_API_TYPE.lower()
    if api_type == "responses":
        return OpenAIResponsesClient()
    return OpenAIChatCompletionsClient()
