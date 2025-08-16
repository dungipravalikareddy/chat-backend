from fastapi import APIRouter, HTTPException, Depends
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from app.core.auth import get_current_user
from app.services.history import get_history, save_history, clear_history
from app.core.storage import append_log
from datetime import datetime
from app.services.analytics_service import log_chat

router = APIRouter()

@router.post("/", response_model=ChatResponse, summary="Chat with LLM")
async def chat(request: ChatRequest, user: str = Depends(get_current_user)):
    try:
        # Call LLM
        result = ChatService.get_response(request)

        # Convert existing history to plain dicts
        history_dicts = [
            {"role": h.role, "content": h.content}
            if hasattr(h, "role") else h
            for h in request.history
        ]

        # Append new user + assistant messages
        new_history = history_dicts + [
            {"role": "user", "content": request.message},
            {"role": "assistant", "content": result["reply"]},
        ]

        # Save only dicts (JSON serializable)
        save_history(user, request.persona, new_history)

        log_chat(
            user=user,
            persona=request.persona,
            temperature=result["temperature"],
            prompt=request.message,
            response=result["reply"],
        )

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history/{persona}", summary="Get chat history for persona")
async def get_chat_history(persona: str, user: str = Depends(get_current_user)):
    return {"history": get_history(user, persona)}

@router.delete("/history/{persona}", summary="Clear chat history for persona")
async def delete_chat_history(persona: str, user: str = Depends(get_current_user)):
    clear_history(user, persona)
    return {"status": "cleared"}
