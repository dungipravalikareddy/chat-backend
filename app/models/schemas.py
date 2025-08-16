from pydantic import BaseModel, Field, constr
from typing import List, Literal, Optional, Dict, Any

Role = Literal["system","user","assistant"]

class Message(BaseModel):
    role: Role
    content: constr(strip_whitespace=True, min_length=1)

class ChatRequest(BaseModel):
    message: constr(strip_whitespace=True, min_length=1)
    persona: Optional[Literal["Tutor", "Therapist", "Default"]] = "Default"
    history: List[Message] = Field(default_factory=list)
    temperature: float = 0.7

class ChatResponse(BaseModel):
    reply: str
    persona: str
    temperature: float
    usage: Optional[Dict[str, Any]] = None
