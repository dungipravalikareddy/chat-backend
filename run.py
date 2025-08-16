import os
import uvicorn
from app.main import app  # adjust if your FastAPI entrypoint is different

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Railway will inject $PORT automatically
    uvicorn.run(app, host="0.0.0.0", port=port)
