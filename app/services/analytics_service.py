import os
import json
from datetime import datetime
from collections import Counter

DATA_FILE = "data/chat_logs.json"
os.makedirs("data", exist_ok=True)

def log_chat(user: str, persona: str, temperature: float, prompt: str, response: str):
    entry = {
        "user": user,
        "persona": persona,
        "temperature": temperature,
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response,
    }
    logs = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)

    logs.append(entry)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)

def get_summary(user: str):
    if not os.path.exists(DATA_FILE):
        return {"total_chats": 0, "most_used_persona": None, "top_prompts": []}

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        logs = json.load(f)

    user_logs = [log for log in logs if log["user"] == user]
    total = len(user_logs)

    if total == 0:
        return {"total_chats": 0, "most_used_persona": None, "top_prompts": []}

    persona_counter = Counter([log["persona"] for log in user_logs])
    most_used = persona_counter.most_common(1)[0][0]

    prompt_counter = Counter([log["prompt"] for log in user_logs])
    top_prompts = [p for p, _ in prompt_counter.most_common(5)]

    return {
        "total_chats": total,
        "most_used_persona": most_used,
        "top_prompts": top_prompts,
    }
