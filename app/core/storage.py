import os
import json
from typing import Dict, Any, List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "logs")
os.makedirs(DATA_DIR, exist_ok=True)

def _user_file(user_id: str) -> str:
    """Return path to a user’s log file"""
    safe_id = user_id.replace("@", "_at_")
    return os.path.join(DATA_DIR, f"{safe_id}.json")

def load_logs(user_id: str) -> List[Dict[str, Any]]:
    file_path = _user_file(user_id)
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_logs(user_id: str, logs: List[Dict[str, Any]]) -> None:
    file_path = _user_file(user_id)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)

def append_log(user_id: str, entry: Dict[str, Any]) -> None:
    logs = load_logs(user_id)
    logs.append(entry)
    save_logs(user_id, logs)

def clear_logs(user_id: str) -> None:
    file_path = _user_file(user_id)
    if os.path.exists(file_path):
        os.remove(file_path)
