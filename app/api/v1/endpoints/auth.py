from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from datetime import timedelta
from app.core.auth import create_access_token, verify_password, get_password_hash, ACCESS_TOKEN_EXPIRE_MINUTES
from app.core.auth import create_access_token, verify_password, get_password_hash, get_current_user

router = APIRouter()

# Dummy user DB (replace with real DB later)
fake_users_db = {
    "test@example.com": {
        "email": "test@example.com",
        "hashed_password": get_password_hash("password123"),
    },
    "alice@example.com": {
        "email": "alice@example.com",
        "hashed_password": get_password_hash("alicepass"),
    },
    "bob@example.com": {
        "email": "bob@example.com",
        "hashed_password": get_password_hash("bobpass123"),
    }
}
class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(request: LoginRequest):
    user = fake_users_db.get(request.username)
    if not user or not verify_password(request.password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": request.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me")
def read_users_me(current_user: str = Depends(get_current_user)):
    return {"username": current_user}