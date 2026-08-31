"""
ElewaSTEM African Pedagogical & Learning Theories Matrix
Maps foundational and modern learning theories directly to the socio-cultural realities of the African child.
"""

from typing import Dict, List, Any

LEARNING_THEORIES = {
    "Constructivism": {
        "theorists": "Jean Piaget, Jerome Bruner",
        "swahili_title": "Ujengaji wa Maarifa (Active Discovery)",
        "core_principle": "Learners construct their own understanding through hands-on discovery and active inquiry rather than passive reception.",
        "african_context": "Zero-cost kitchen experiments using everyday household objects (e.g. testing seed germination in used plastic cups, building water filters with cooking charcoal and river sand). Eliminates rote memorization ('Usimeze, Elewa!')."
    },
    "SocialConstructivism": {
        "theorists": "Lev Vygotsky (Zone of Proximal Development & Ubuntu Pedagogy)",
        "swahili_title": "Nadharia ya Kijamii & Falsafa ya Utu / Ubuntu",
        "core_principle": "Learning occurs within the Zone of Proximal Development (ZPD) through social mediation, scaffolding, and dialogue with a More Knowledgeable Other (MKO).",
        "african_context": "Rooted in the African philosophy of Ubuntu ('Mtu ni mtu kupitia watu wengine' / 'I am because we are'). The AI acts as a caring peer and mentor, scaffolding concepts alongside village peers, teachers, and parents."
    },
    "ExperientialLearning": {
        "theorists": "David Kolb",
        "swahili_title": "Mafunzo ya Uzoefu na Mazingira Halisi",
        "core_principle": "Four-stage learning cycle: Concrete Experience ➔ Reflective Observation ➔ Abstract Conceptualization ➔ Active Experimentation.",
        "african_context": "Grounded in local African biomes: observing Tilapia Ngege breathing in Lake Victoria ➔ reflecting on why fish perish without water ➔ conceptualizing dissolved oxygen and gill counter-current gas exchange ➔ testing home water bubble experiments."
    },
    "CulturallyResponsive": {
        "theorists": "Gloria Ladson-Billings, Bame Nsamenang (Afrocentric Developmental Psychology)",
        "swahili_title": "Elimu Inayozingatia Utamaduni na Maarifa ya Asili",
        "core_principle": "Academic success and cultural competence are reinforced when learning validates the student's lived cultural identity and indigenous knowledge.",
        "african_context": "Integrates indigenous African botanical wisdom (Osuga, Mitoo, Moringa), historical metallurgy and astronomy, and codeswitches seamlessly across 16+ African languages (Kiswahili, Sheng, Yoruba, Hausa, Zulu, Pidgin)."
    },
    "MultipleIntelligences": {
        "theorists": "Howard Gardner",
        "swahili_title": "Uwezo wa Akili Nyingi (Multi-Sensory Inclusivity)",
        "core_principle": "Intelligence is multi-dimensional across linguistic, logical, spatial, bodily-kinesthetic, naturalistic, and interpersonal domains.",
        "african_context": "Provides Tactile Audio Descriptions for visually impaired learners (Naturalistic/Kinesthetic), visual sign cues for deaf learners (Spatial), and voice-first oral storytelling honoring Africa's rich oral tradition (Linguistic)."
    },
    "CognitiveLoadTheory": {
        "theorists": "John Sweller, Allan Paivio (Dual Coding)",
        "swahili_title": "Kupunguza Mzigo wa Akili & Uwasilishaji wa Picha na Sauti",
        "core_principle": "Working memory is limited. Multi-channel dual coding (visual flowcharts + auditory narration) and chunking prevent cognitive overload.",
        "african_context": "The '💡 Rahisisha Zaidi' (Simplify) feature instantly breaks complex STEM concepts into bite-sized, non-intimidating chunks for learners needing focused cognitive pacing (ADHD) and clear visual reading formats (Dyslexia)."
    },
    "GrowthMindset": {
        "theorists": "Carol Dweck, B.F. Skinner (Positive Reinforcement)",
        "swahili_title": "Mtazamo wa Kukuza Akili & Kuthamini Makosa",
        "core_principle": "Intelligence is malleable through effort, strategy, and supportive encouragement. Mistakes are celebrated as vital learning data.",
        "african_context": "Counters punitive colonial rote-learning cultures with affectionate, loving affirmation: 'Makosa ndio ngazi ya kwanza ya ugunduzi!' (Mistakes are the first stepping stones to discovery!)."
    },
    "Connectivism": {
        "theorists": "George Siemens, Stephen Downes",
        "swahili_title": "Mtandao wa Kujifunza Katika Zama za Kidijitali",
        "core_principle": "Knowledge is distributed across human and technological networks; learning is the process of navigating and connecting these nodes.",
        "african_context": "The 360-degree Stakeholder Loop connects the Child (PWA Vault) ➔ Remote Parent (2G SMS) ➔ CBC Teacher (Lesson Plans) ➔ Community Mentor (STEM Club Guides)."
    }
}


def get_all_learning_theories() -> Dict[str, Any]:
    return LEARNING_THEORIES
