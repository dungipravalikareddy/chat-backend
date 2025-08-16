from fastapi import APIRouter, Depends
from app.core.auth import get_current_user
from app.services.analytics_service import get_summary

router = APIRouter()

@router.get("/summary", summary="Get analytics summary for user")
async def analytics_summary(user: str = Depends(get_current_user)):
    return get_summary(user)
