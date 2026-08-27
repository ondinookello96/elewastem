"""
ElewaSTEM Persistent Student Memory & Concept Mastery Bank
Tracks student profile, grade level, language preference, topic mastery, and misconceptions.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
PROFILES_FILE = os.path.join(DATA_DIR, "student_profiles.json")


class TopicMastery(BaseModel):
    topic: str
    subject: str  # Physics, Chemistry, Biology, Math, Computing
    mastery_score: int = 0  # 0 to 100
    times_explored: int = 0
    last_studied: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    misconceptions: List[str] = Field(default_factory=list)
    quizzes_taken: int = 0
    quizzes_passed: int = 0


class StudentProfile(BaseModel):
    student_id: str
    name: str = "Mwanafunzi"
    grade_level: str = "Grade 6 (Upper Primary)"  # e.g., Grade 4, Grade 6, Grade 8, Form 1
    preferred_language: str = "swahili"  # "english", "swahili", "sheng"
    learning_style: str = "analogies_and_experiments"
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    mastery_graph: Dict[str, TopicMastery] = Field(default_factory=dict)
    badges: List[str] = Field(default_factory=list)
    recent_interactions: List[dict] = Field(default_factory=list)


class MemoryBank:
    def __init__(self, storage_path: str = PROFILES_FILE):
        self.storage_path = storage_path
        self._ensure_storage()
        self.profiles: Dict[str, StudentProfile] = self._load_profiles()

    def _ensure_storage(self):
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump({}, f)

    def _load_profiles(self) -> Dict[str, StudentProfile]:
        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return {k: StudentProfile(**v) for k, v in data.items()}
        except Exception:
            return {}

    def _save_profiles(self):
        with open(self.storage_path, "w", encoding="utf-8") as f:
            data = {k: v.model_dump() for k, v in self.profiles.items()}
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_or_create_profile(self, student_id: str, name: Optional[str] = None, language: Optional[str] = None) -> StudentProfile:
        if student_id not in self.profiles:
            profile = StudentProfile(
                student_id=student_id,
                name=name or "Mwanafunzi",
                preferred_language=language or "swahili",
                badges=["🌟 Mwanzo Bora (Great Start)"]
            )
            self.profiles[student_id] = profile
            self._save_profiles()
        else:
            if name:
                self.profiles[student_id].name = name
            if language:
                self.profiles[student_id].preferred_language = language
            self._save_profiles()
        return self.profiles[student_id]

    def update_topic_interaction(self, student_id: str, topic: str, subject: str, score_delta: int = 5, misconception: Optional[str] = None):
        profile = self.get_or_create_profile(student_id)
        if topic not in profile.mastery_graph:
            profile.mastery_graph[topic] = TopicMastery(
                topic=topic,
                subject=subject,
                mastery_score=min(100, max(0, 20 + score_delta)),
                times_explored=1
            )
        else:
            entry = profile.mastery_graph[topic]
            entry.times_explored += 1
            entry.mastery_score = min(100, max(0, entry.mastery_score + score_delta))
            entry.last_studied = datetime.utcnow().isoformat()
            if misconception and misconception not in entry.misconceptions:
                entry.misconceptions.append(misconception)

        # Award Badges based on milestones
        if len(profile.mastery_graph) >= 3 and "🔬 Mvumbuzi Chipukizi (Junior Explorer)" not in profile.badges:
            profile.badges.append("🔬 Mvumbuzi Chipukizi (Junior Explorer)")
        if any(m.mastery_score >= 80 for m in profile.mastery_graph.values()) and "⚡ Bingwa wa Sayansi (Science Champ)" not in profile.badges:
            profile.badges.append("⚡ Bingwa wa Sayansi (Science Champ)")

        self._save_profiles()

    def record_quiz_result(self, student_id: str, topic: str, passed: bool, score: int):
        profile = self.get_or_create_profile(student_id)
        if topic in profile.mastery_graph:
            m = profile.mastery_graph[topic]
            m.quizzes_taken += 1
            if passed:
                m.quizzes_passed += 1
                m.mastery_score = min(100, m.mastery_score + 15)
            else:
                m.mastery_score = max(0, m.mastery_score - 5)
        self._save_profiles()

    def add_interaction_history(self, student_id: str, role: str, content: str, language: str):
        profile = self.get_or_create_profile(student_id)
        profile.recent_interactions.append({
            "timestamp": datetime.utcnow().isoformat(),
            "role": role,
            "content": content,
            "language": language
        })
        # Keep last 15 interactions in persistent state
        if len(profile.recent_interactions) > 15:
            profile.recent_interactions = profile.recent_interactions[-15:]
        self._save_profiles()


# Singleton memory instance
student_memory = MemoryBank()
