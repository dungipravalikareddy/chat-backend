from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List, Dict

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4o-mini"
    OPENAI_API_TYPE: str = "chat_completions"
    OPENAI_BASE_URL: str = "https://api.openai.com/v1"

    DEFAULT_TEMPERATURE: float = 0.7
    DEFAULT_PERSONA: str = "Default"

    PERSONA_DEFAULT: str = "You are a helpful, concise assistant."
    PERSONA_TUTOR: str = "You are a friendly tutor. Explain step-by-step with short examples."
    PERSONA_THERAPIST: str = "You are a supportive coach. Be empathetic, ask reflective questions, avoid medical advice."

    LOG_LEVEL: str = "INFO"
    CORS_ORIGINS: List[str] = Field(default_factory=lambda: ["*"])

    class Config:
        env_file = ".env"
        extra = "ignore"

    def personas(self) -> Dict[str, str]:
        return {
            "Default": self.PERSONA_DEFAULT,
            "Tutor": self.PERSONA_TUTOR,
            "Therapist": self.PERSONA_THERAPIST,
        }

@lru_cache
def get_settings() -> Settings:
    return Settings()
