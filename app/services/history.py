import os
import json

DATA_DIR = "data/histories"
os.makedirs(DATA_DIR, exist_ok=True)

def _get_file(user: str, persona: str) -> str:
    return os.path.join(DATA_DIR, f"{user}_{persona}.json")

def get_history(user: str, persona: str):
    file = _get_file(user, persona)
    if not os.path.exists(file):
        return []
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def save_history(user: str, persona: str, history: list):
    file = _get_file(user, persona)
    with open(file, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)

def clear_history(user: str, persona: str):
    file = _get_file(user, persona)
    if os.path.exists(file):
        os.remove(file)
