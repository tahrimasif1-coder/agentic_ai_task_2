"""
Simple JSON-based persistent memory module for Social Media Agent.
Stores user inputs and generated results to provide contextual awareness across sessions.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional

DEFAULT_MEMORY_PATH = os.path.join("outputs", "memory.json")


class MemoryManager:
    """Manages persistent JSON memory for the Social Media Agent."""

    def __init__(self, memory_file_path: str = DEFAULT_MEMORY_PATH):
        self.memory_file_path = memory_file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        """Ensures the directory and memory JSON file exist."""
        os.makedirs(os.path.dirname(self.memory_file_path), exist_ok=True)
        if not os.path.exists(self.memory_file_path):
            with open(self.memory_file_path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=2)

    def load_memory(self) -> List[Dict[str, Any]]:
        """Loads all records from JSON memory file."""
        try:
            with open(self.memory_file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_record(
        self,
        topic: str,
        platform: str,
        tone: str,
        output_type: str,
        selected_idea: str,
        hook: str,
        saved_file_path: str
    ) -> Dict[str, Any]:
        """Saves a new generation result to JSON memory."""
        records = self.load_memory()
        new_entry = {
            "id": len(records) + 1,
            "timestamp": datetime.now().isoformat(),
            "topic": topic,
            "platform": platform,
            "tone": tone,
            "output_type": output_type,
            "selected_idea": selected_idea,
            "hook": hook,
            "saved_file_path": saved_file_path
        }
        records.append(new_entry)
        
        with open(self.memory_file_path, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2, ensure_ascii=False)
            
        return new_entry

    def get_recent_context(self, current_topic: str = "", limit: int = 2) -> str:
        """
        Retrieves relevant context from previous agent runs to inform the LLM.
        Looks for topic similarity or returns the latest N records.
        """
        records = self.load_memory()
        if not records:
            return ""

        # Filter relevant records (same topic substring or recent)
        relevant = [
            r for r in records
            if current_topic and current_topic.lower() in r.get("topic", "").lower()
        ]
        
        # If no direct match, take the latest N records
        if not relevant:
            relevant = records[-limit:]
        else:
            relevant = relevant[-limit:]

        context_lines = []
        for r in relevant:
            context_lines.append(
                f"- Past Topic: '{r.get('topic')}' on {r.get('platform')} (Tone: {r.get('tone')}) -> Angle: {r.get('selected_idea')}"
            )

        return "\n".join(context_lines)
