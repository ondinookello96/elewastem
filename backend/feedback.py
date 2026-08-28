"""
ElewaSTEM Multi-Stakeholder Feedback Engine & Continuous Improvement Loop
Collects, aggregates, and stores feedback from Learners, Parents, Teachers, Community Mentors, and Accessibility Advocates.
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from pydantic import BaseModel, Field

FEEDBACK_FILE = os.path.join(os.path.dirname(__file__), "stakeholder_feedback.json")


class StakeholderFeedback(BaseModel):
    id: str = Field(default_factory=lambda: f"fb_{int(datetime.now().timestamp() * 1000)}")
    stakeholder_type: str = "student"  # 'student', 'parent', 'teacher', 'community_mentor', 'accessibility_advocate'
    student_id: Optional[str] = "demo_student"
    region: str = "lake_basin"
    language: str = "sw"
    rating: int = 5  # 1 to 5 stars
    category: str = "content_clarity"  # 'content_clarity', 'local_analogy', 'accessibility', 'cbc_alignment', 'experiment_safety'
    comment: str = ""
    topic: Optional[str] = "General"
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())


class FeedbackManager:
    def __init__(self):
        self.feedback_list: List[Dict[str, Any]] = []
        self._load_feedback()

    def _load_feedback(self):
        if os.path.exists(FEEDBACK_FILE):
            try:
                with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
                    self.feedback_list = json.load(f)
            except Exception as e:
                print(f"[FeedbackManager] Load error: {e}")
                self._seed_default_feedback()
        else:
            self._seed_default_feedback()

    def _seed_default_feedback(self):
        self.feedback_list = [
            {
                "id": "fb_seed_1",
                "stakeholder_type": "student",
                "student_id": "demo_student",
                "region": "lake_basin",
                "language": "sw",
                "rating": 5,
                "category": "content_clarity",
                "comment": "Nimeelewa vizuri sana jinsi samaki Ngege wanavyopumua ziwani! Sauti ilikuwa wazi.",
                "topic": "Aquatic Biology & Respiration",
                "timestamp": datetime.now().isoformat()
            },
            {
                "id": "fb_seed_2",
                "stakeholder_type": "parent",
                "student_id": "demo_student",
                "region": "lake_basin",
                "language": "sw",
                "rating": 5,
                "category": "local_analogy",
                "comment": "Ujumbe wa SMS ulinisaidia kujua mtoto amesoma nini. Tulifanya jaribio la majani ya managu jikoni jioni!",
                "topic": "Photosynthesis",
                "timestamp": datetime.now().isoformat()
            },
            {
                "id": "fb_seed_3",
                "stakeholder_type": "teacher",
                "student_id": "tr_akinyi",
                "region": "lake_basin",
                "language": "sw",
                "rating": 5,
                "category": "cbc_alignment",
                "comment": "Mwongozo wa somo la Usanisinuru umeoana kikamilifu na mtaala wa CBC Grade 5 Science & Technology.",
                "topic": "Grade 5 Science Strand",
                "timestamp": datetime.now().isoformat()
            },
            {
                "id": "fb_seed_4",
                "stakeholder_type": "accessibility_advocate",
                "student_id": "spec_ed_nuru",
                "region": "lake_basin",
                "language": "sw",
                "rating": 5,
                "category": "accessibility",
                "comment": "Maelezo ya sauti ya kushika (tactile descriptions) yanawasaidia sana watoto wetu wasioona kushika majani na kuhisi mishipa.",
                "topic": "Tactile Biology for Blind Learners",
                "timestamp": datetime.now().isoformat()
            }
        ]
        self._save_feedback()

    def _save_feedback(self):
        try:
            with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
                json.dump(self.feedback_list, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[FeedbackManager] Save error: {e}")

    def add_feedback(self, feedback: StakeholderFeedback) -> Dict[str, Any]:
        item = feedback.model_dump()
        self.feedback_list.insert(0, item)
        self._save_feedback()
        return item

    def get_recent_feedback(self, limit: int = 15) -> List[Dict[str, Any]]:
        return self.feedback_list[:limit]

    def get_summary_metrics(self) -> Dict[str, Any]:
        total = len(self.feedback_list)
        if total == 0:
            return {"total_feedback": 0, "average_rating": 5.0, "by_stakeholder": {}}

        avg_rating = sum(fb.get("rating", 5) for fb in self.feedback_list) / total

        by_type: Dict[str, int] = {}
        by_category: Dict[str, int] = {}

        for fb in self.feedback_list:
            st = fb.get("stakeholder_type", "student")
            by_type[st] = by_type.get(st, 0) + 1

            cat = fb.get("category", "general")
            by_category[cat] = by_category.get(cat, 0) + 1

        return {
            "total_feedback": total,
            "average_rating": round(avg_rating, 2),
            "by_stakeholder": by_type,
            "by_category": by_category
        }


# Singleton feedback manager
feedback_manager = FeedbackManager()
