"""
ElewaSTEM Curriculum Master Package
Aggregates all 50 Official Pan-African Curriculum Modules across:
- Biology (12 Topics)
- Physics (10 Topics)
- Chemistry (10 Topics)
- Mathematics (10 Topics)
- Computer Science & Digital Tech (8 Topics)
"""

from typing import List, Dict, Any
from .biology import BIOLOGY_TOPICS
from .physics import PHYSICS_TOPICS
from .chemistry import CHEMISTRY_TOPICS
from .mathematics import MATHEMATICS_TOPICS
from .computer_science import COMPUTER_SCIENCE_TOPICS

ALL_CURRICULUM_TOPICS: List[Dict[str, Any]] = (
    BIOLOGY_TOPICS +
    PHYSICS_TOPICS +
    CHEMISTRY_TOPICS +
    MATHEMATICS_TOPICS +
    COMPUTER_SCIENCE_TOPICS
)

CURRICULUM_BY_ID: Dict[str, Dict[str, Any]] = {
    topic["id"]: topic for topic in ALL_CURRICULUM_TOPICS
}

CURRICULUM_BY_SUBJECT: Dict[str, List[Dict[str, Any]]] = {
    "Biology": BIOLOGY_TOPICS,
    "Physics": PHYSICS_TOPICS,
    "Chemistry": CHEMISTRY_TOPICS,
    "Mathematics": MATHEMATICS_TOPICS,
    "Computer Science": COMPUTER_SCIENCE_TOPICS
}
