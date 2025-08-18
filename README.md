# 🧠 Chat Backend (FastAPI)

This is the **backend service** for the Chat App, built with **FastAPI**.  
It provides authentication, chat handling with multiple personas, history management, and analytics.

---

## 🚀 Features

- **User Authentication**
  - JWT-based login (`/api/v1/auth/login`)
  - Get current user (`/api/v1/auth/me`)

- **Chat System**
  - Multiple personas (Default, Tutor, Therapist)
  - Adjustable temperature
  - Maintains per-persona history
  - Endpoints to chat, view history, and clear history

- **Analytics**
  - Tracks total chats per user
  - Finds most used persona
  - Stores & ranks top prompts

- **Containerized**
  - Runs inside Docker
  - Works with frontend (Streamlit)

---

## 📂 Project Structure

```
CHAT-BACKEND/
│── .venv/                    # Python virtual environment (ignored in Git)
│── .vscode/                  # VS Code configs
│
│── app/                      # Main FastAPI application
│   ├── api_v1/endpoints/     # API route definitions
│   │   ├── __init__.py
│   │   ├── analytics.py      # Analytics endpoints (/analytics)
│   │   ├── auth.py           # Authentication endpoints (/auth)
│   │   ├── chat.py           # Chat endpoints (/chat)
│   │   └── healthy.py        # Health-check endpoint (/health)
│   │
│   ├── core/                 # Core utilities
│   │   ├── __init__.py
│   │   ├── auth.py           # JWT & password hashing
│   │   ├── config.py         # Config values (personas, settings)
│   │   ├── logging_config.py # Logging configuration
│   │   └── storage.py        # JSON / file storage utils
│   │
│   ├── middlewares/          # Middlewares (extra request handlers)
│   │   ├── __init__.py
│   │   └── timing.py         # Request timing middleware
│   │
│   ├── models/               # Data models / schemas
│   │   └── schemas.py        # Pydantic schemas (User, Chat, Analytics)
│   │
│   ├── services/             # Business logic
│   │   ├── __init__.py
│   │   ├── interfaces/       # Interfaces for future DB/service layers
│   │   ├── analytics_service.py # Analytics logic
│   │   ├── chat_service.py   # Chat + persona logic
│   │   └── history.py        # Chat history management
│   │
│   ├── __init__.py
│   └── main.py               # FastAPI entrypoint
│
│── data/                     # Storage/data folder
│   ├── histories/            # Persona chat history files
│   ├── logs/                 # Log files
│   └── chat_logs.json        # JSON storage for chats
│
│── test/                     # Unit tests
│   └── test_chat.py          # Example test case
│
│── .env                      # Environment variables
│── .gitignore                # Ignored files for Git
│── Dockerfile                # Containerization for backend
│── Procfile                  # Deployment file (Heroku/Railway)
│── README.md                 # Documentation
│── render.yaml               # Render deployment config
│── requirements.txt          # Python dependencies
│── run.py                    # Alternative entrypoint

```

---

## 🛠️ Installation & Running Locally

### 1. Clone repository

```bash
git clone https://github.com/yourusername/chat-backend.git
cd chat-backend
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run FastAPI app

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Now visit 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive API docs.

---

## 🔑 Authentication

* **Login**

  ```
  POST /api/v1/auth/login
  ```

  Example request:

  ```json
  {
    "username": "test@example.com",
    "password": "password123"
  }
  ```

  Example response:

  ```json
  {
    "access_token": "JWT_TOKEN_HERE",
    "token_type": "bearer"
  }
  ```

* Use the token in all further requests:

  ```
  Authorization: Bearer <token>
  ```

* **Get Current User**

  ```
  GET /api/v1/auth/me
  ```

🚨 Currently uses a **dummy user store** (`fake_users_db`).  
Replace with a real DB in production.

---

## 💬 Chat Endpoints

* **Send message**

  ```
  POST /api/v1/chat/
  ```

  Example request:

  ```json
  {
    "message": "What is E=mc^2?",
    "persona": "Tutor",
    "history": [],
    "temperature": 0.7
  }
  ```

  Example response:

  ```json
  {
    "reply": "E=mc^2 means energy equals mass times the speed of light squared..."
  }
  ```

* **Get history**

  ```
  GET /api/v1/chat/history/{persona}
  ```

* **Clear history**

  ```
  DELETE /api/v1/chat/history/{persona}
  ```

---

## 📊 Analytics Endpoints

* **Get summary**

  ```
  GET /api/v1/analytics/summary
  ```

  Example response:

  ```json
  {
    "total_chats": 3,
    "most_used_persona": "Default",
    "top_prompts": [
      "what is orange",
      "what is mango",
      "what is e=mc^2"
    ]
  }
  ```

---

## 🐳 Docker Deployment

### Build and Run with Docker

```bash
docker build -t chat-backend .
docker run -d -p 8000:8000 chat-backend
```

Backend is live at [http://localhost:8000](http://localhost:8000).

### Useful Docker Commands
# List running containers
docker ps

# View container logs (live stream)
docker logs -f <container_id_or_name>

# Example
docker logs -f priceless_stonebraker

# Stop a running container
docker stop <container_id_or_name>

# Example
docker stop priceless_stonebraker


## ☁️ Cloud Deployment

The backend is live on:

- **Railway** → [https://chat-backend-production-bbdf.up.railway.app/docs#/](https://chat-backend-production-bbdf.up.railway.app/docs#/)  
- **Render** → [https://chat-backend-qrmn.onrender.com/docs#/](https://chat-backend-qrmn.onrender.com/docs#/)

📌 Both provide the full interactive **Swagger UI** where you can test all endpoints.

---

## ✅ Testing

* Visit Swagger docs at:

  * Local: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  * Deployed: `https://<your-backend-url>/docs`

* Try logging in with:

```txt
Username: test@example.com
Password: password123
```

---

## 🔮 Personas

Available personas:

* **Default** → Helpful assistant  
* **Tutor** → Step-by-step explanations  
* **Therapist** → Supportive, empathetic coach  

---

## 📌 Notes

* Uses a JSON file for storage (`data/chat_logs.json`).  
* Replace with real DB (Postgres/MongoDB) in production.  
* Authentication currently uses a **dummy user store** (`fake_users_db`).  

---
