"""
ElewaSTEM Internal Architectural & Ethical AI Design Frameworks (Proprietary)
Implements ElewaSTEM's custom design frameworks (ETHOS, TRACK, OASIS, PRIDE, and HORIZON) 
for Responsible AI engineering in African education. 
NOTE: These are internal platform design & governance protocols, distinct from national statutory DPAs.
"""

from typing import Dict, List, Any

ETHICAL_FRAMEWORKS = {
    "ETHOS": {
        "title": "The ETHOS Framework (ElewaSTEM Ethical Guardrails Design)",
        "acronym": "ETHOS",
        "framework_type": "ElewaSTEM Internal Design Framework (Proprietary)",
        "pillars": {
            "E": {
                "name": "Empathy (Harm Prevention)",
                "description": "Who might be harmed by this output? Filters out dangerous at-home experiment procedures (e.g. high-voltage mains electricity, toxic chemicals) and ensures age-appropriate safety for 8-16 year olds."
            },
            "T": {
                "name": "Transparency (Traceability)",
                "description": "Can you trace how the AI reached this conclusion? Every explanation provides the scientific chain-of-thought, CBC curriculum strand reference, and source glossary."
            },
            "H": {
                "name": "Human Impact (Real-World Consequences)",
                "description": "Fosters genuine conceptual understanding and curiosity rather than exam cramming or spoon-fed answers ('Usimeze, Elewa!')."
            },
            "O": {
                "name": "Ownership (Accountability)",
                "description": "Clear accountability protocols: Teachers and parents have final pedagogical oversight, with explicit developer and institutional contact channels."
            },
            "S": {
                "name": "Sovereignty (Cultural & Digital Dignity)",
                "description": "Respects African cultural wisdom, indigenous ecological knowledge (e.g., Lake Victoria water patterns, drought-resilient crops), and child privacy."
            }
        }
    },
    "TRACK": {
        "title": "The TRACK Framework (ElewaSTEM Bias Mitigation & Inclusion Design)",
        "acronym": "TRACK",
        "framework_type": "ElewaSTEM Internal Design Framework (Proprietary)",
        "pillars": {
            "T": {
                "name": "Training Data Diversity",
                "description": "Directly counters Western-centric LLM biases by grounding model prompts and offline vaults in African NLP benchmarks (Masakhane, Lelapa AI, AfriSpeech)."
            },
            "R": {
                "name": "Representation of Marginalized Groups",
                "description": "Ensures visually impaired learners (Screen Reader & Audio Description Mode), deaf learners (visual concept & flowchart cues), and rural pastoralists (ASAL biomes) are first-class participants."
            },
            "A": {
                "name": "Amplification Prevention",
                "description": "Eliminates gender and socioeconomic stereotypes in STEM by showcasing diverse African boys, girls, and community inventors in all problem sets."
            },
            "C": {
                "name": "Counterfactual Scenarios across Identities",
                "description": "Tests concepts across diverse African geographies (e.g., how photosynthesis is explained in lush highlands vs arid Turkana vs coastal mangroves)."
            },
            "K": {
                "name": "Kill Switch & Human Override",
                "description": "Provides instant teacher and parent override mechanisms to pause AI output or correct misconceptions."
            }
        }
    },
    "OASIS": {
        "title": "The OASIS Protocol (ElewaSTEM Local-First Privacy Design)",
        "acronym": "OASIS",
        "framework_type": "ElewaSTEM Internal Design Framework (Proprietary)",
        "pillars": {
            "O": {
                "name": "Opt-in by Design",
                "description": "Never assumes consent. Explicit, plain-language parental consent modals (supporting Kenya DPA Section 29, Nigeria NDPA Section 31, POPIA Section 34)."
            },
            "A": {
                "name": "Anonymization Depth & Data Minimization",
                "description": "Applies client-side data minimization; raw GPS coordinates are mapped to coarse regional eco-zones locally, and live AI queries transmit only necessary pedagogical context."
            },
            "S": {
                "name": "Sovereignty & Local-First Custody",
                "description": "Local-first storage by default; when online AI or SMS features are utilized, data is transmitted over encrypted channels under applicable African data protection frameworks."
            },
            "I": {
                "name": "Intentional Retention",
                "description": "Zero data hoarding. Temporary session memory is stored in browser localStorage with a 1-click statutory 'Futa Data (Erase All)' button."
            },
            "S": {
                "name": "Security as Ritual",
                "description": "Client-side encrypted memory banks and TLS/HTTPS transport for all remote parent dispatches."
            }
        }
    },
    "PRIDE": {
        "title": "The PRIDE Loop (ElewaSTEM Human-in-the-Loop Governance Design)",
        "acronym": "PRIDE",
        "framework_type": "ElewaSTEM Internal Design Framework (Proprietary)",
        "pillars": {
            "P": {
                "name": "Pause Points",
                "description": "Mandatory human pause points before high-stakes quiz certifications or curriculum advancement."
            },
            "R": {
                "name": "Review Cadence",
                "description": "Scheduled weekly community feedback audits aggregated in the Stakeholder Hub."
            },
            "I": {
                "name": "Interpretability for Village Elders",
                "description": "Demands scientific explanations in plain, relatable language that a non-technical grandparent or village elder can understand and enjoy."
            },
            "D": {
                "name": "Disagreement Rights",
                "description": "Students and teachers can challenge any AI answer with one tap ('Toa Maoni / Pinga Jibu') without penalty."
            },
            "E": {
                "name": "Elders Council Governance",
                "description": "Governed by a multi-stakeholder triangle of Parents, CBC Teachers, and Community Mentors rather than tech engineers alone."
            }
        }
    },
    "HORIZON": {
        "title": "The HORIZON Scan (ElewaSTEM Ecological & Future Stewardship Design)",
        "acronym": "HORIZON",
        "framework_type": "ElewaSTEM Internal Design Framework (Proprietary)",
        "pillars": {
            "H": {
                "name": "Historical Harm Prevention",
                "description": "Celebrates ancient and modern African STEM innovators, countering historical biases."
            },
            "O": {
                "name": "Opportunity Cost Awareness",
                "description": "Prevents cognitive atrophy by fostering critical thinking and hands-on experiments rather than passive copy-pasting."
            },
            "R": {
                "name": "Ripple Effects on Community Dynamics",
                "description": "Strengthens family bonds through weekend parent-child kitchen science challenges and community STEM club activities."
            },
            "I": {
                "name": "Intergenerational Wisdom",
                "description": "Preserves indigenous African botanical and aquatic knowledge for future generations across 16+ languages."
            },
            "Z": {
                "name": "Zero-Sum Trap Avoidance",
                "description": "Ensures high-tech AI does not leave rural learners behind: core learning modules remain accessible offline after installation, complemented by 2G SMS modes."
            },
            "O": {
                "name": "Open Futures & Human Agency",
                "description": "Empowers children to see themselves as future African scientists, engineers, and problem-solvers."
            },
            "N": {
                "name": "Non-Human Stakeholders & Ecology",
                "description": "Deeply respects African rivers, lakes (Lake Victoria water hyacinth / Tilapia habitats), wildlife, soil, and forests in all biology modules."
            }
        }
    }
}


def get_all_ethics_frameworks() -> Dict[str, Any]:
    return ETHICAL_FRAMEWORKS


def audit_ethical_safety(prompt: str) -> Dict[str, Any]:
    """Safety filter ensuring experiments and advice adhere to the ETHOS harm-prevention protocol."""
    dangerous_keywords = [
        "acid", "poison", "petrol", "kerosene", "knife", "blade", "fire", "moto mkali",
        "mains electricity", "240v", "shock", "explosive", "gunpowder", "bleach"
    ]
    p_lower = prompt.lower()
    for kw in dangerous_keywords:
        if kw in p_lower:
            return {
                "safe": False,
                "flagged_keyword": kw,
                "warning_sw": "⚠️ Tahadhari ya Usalama: Jaribio hili linahitaji usimamizi mkali wa mzazi au mwalimu. Tumia vifaa salama vya nyumbani pekee.",
                "warning_en": "⚠️ Safety Warning: This experiment requires strict adult/teacher supervision. Only safe, zero-hazard materials are permitted."
            }
    return {"safe": True}
