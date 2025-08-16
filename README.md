Got it 👍 You need a **detailed README.md** for your backend (FastAPI app).
Here’s a production-ready `README.md` you can drop inside your `chat-backend/` folder:

---

```markdown
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

chat-backend/
│── app/
│   ├── main.py                # FastAPI entrypoint
│   ├── core/
│   │   ├── auth.py            # JWT auth & password utils
│   │   └── config.py          # Config & constants (personas, settings)
│   ├── services/
│   │   ├── chat\_service.py    # Chat logic + history
│   │   └── analytics\_service.py # Analytics summary
│   ├── endpoints/
│   │   ├── auth.py            # /auth routes
│   │   ├── chat.py            # /chat routes
│   │   └── analytics.py       # /analytics routes
│   └── **init**.py
│
│── data/
│   └── chat\_logs.json         # Stored chats (auto-created)
│
│── requirements.txt
│── Dockerfile
│── README.md                  # (this file)

````

---

## 🛠️ Installation & Running Locally

### 1. Clone repository

```bash
git clone https://github.com/yourusername/chat-backend.git
cd chat-backend
````

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

Now backend is live at [http://localhost:8000](http://localhost:8000).

---

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
* Authentication currently uses a **dummy user store** (fake\_users\_db).


