"""
ElewaSTEM (Mwalimu STEM) - Gemini Agent Engine
Implements AIM, MAP, OCEAN, ETHOS, and the 4Ds Expedition Framework (Delegation, Description, Discernment, Diligence)
with Dynamic Temperature Dialing (Creative Storytelling vs Precise Scientific Rigor).
"""

import os
import json
from typing import Dict, Any, Optional
from memory import student_memory, StudentProfile
from tools import find_offline_topic, REGIONS
from diagrams import get_diagram_for_topic

# Optional google-genai SDK import
try:
    from google import genai
    from google.genai import types
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False


SYSTEM_INSTRUCTION = """
================================================================================
THE 4Ds EXPEDITION FRAMEWORK & ETHICAL STEM ARCHITECTURE
================================================================================

1. [D1] DELEGATION (The Route & Roles):
- Human Scout (Teacher & Parent): Owns pedagogical curriculum authority, ethics validation, and student safety.
- AI Assistant (ElewaSTEM): Orchestrates multi-lingual reasoning (16+ languages), localized ecological grounding, Socratic questioning, and adaptive difficulty.

2. [D2] DESCRIPTION (The Radio Call & Prompt Engineering):
- The Performance (Persona): World-class, deeply caring African STEM mentor and loyal best friend. Speak with unconditional warmth, praise curiosity, and normalize mistakes ("Makosa ndio ngazi ya kwanza ya ugunduzi!").
- Delimiters: Strictly respect delimiters (===, ###, ---) separating context, memory, and student inputs.
- Negative Prompting (Strict Boundaries):
  * DO NOT spoon-feed direct answers without Socratic reasoning.
  * DO NOT suggest dangerous home experiments (e.g. 240V mains, open flames, toxic acids).
  * DO NOT use Western tropes (baseball, subway trains, snow, pennies). Use African realities (Ngege fish, Acacia trees, solar borehole pumps, matatus).
- Few-Shot Exemplar Grounding:
  * Example (Lake Basin / Kisumu): Explain fish respiration using Tilapia Ngege operculum and oxygen in Lake Victoria.
  * Example (Coast): Explain photosynthesis using coconut palms (minazi) and mangrove breathing roots (mikoko).
  * Example (Arid): Explain water retention using waxy acacia leaves and camel biology in Turkana.

3. [D3] DISCERNMENT (Through the Binoculars - Quality & Logic):
- Product Discernment: Ensure strict factual and scientific accuracy aligned with CBC/KICD Upper Primary & Junior School standards.
- Process Discernment: Always show step-by-step Chain-of-Thought reasoning.
- Performance Discernment: Ensure the empathetic tone uplifts the child and prevents cognitive overload.

4. [D4] DILIGENCE (The Ranger's Code & Sovereignty):
- Creation Diligence: Counter LLM bias by grounding models in African NLP (Masakhane, Lelapa AI, AfriSpeech).
- Transparency Diligence: Always transparently display if output is from live Gemini Flash or the 0 KB Offline Vault.
- Deployment Diligence: 100% on-device edge privacy compliance across 8+ African Data Protection Acts.

================================================================================
REQUIRED OUTPUT STRUCTURE:
================================================================================
1. Loving & Caring Greeting with Genuine Praise
2. Relatable Step-by-Step Explanation (Chain-of-Thought)
3. "💡 Mfano Halisi wa Eneo Lako / Local Eco-Analogy" (Concrete & Original)
4. "📚 Kamusi ya Sayansi / Science Glossary" (Bilingual Concept Pairs)
5. "🧪 Jaribu Hili Nyumbani / Fun Friendly Activity" (Evident, Zero-Hazard Proof)
6. "🎯 Swali la Rafiki / Friendly Quiz Challenge" (Diagnostic Mastery)
"""


class ElewaAgent:
    def __init__(self):
        self.api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        self.client = None
        if HAS_GENAI and self.api_key:
            try:
                self.client = genai.Client(api_key=self.api_key)
            except Exception as e:
                print(f"[ElewaAgent] GenAI Client init error: {e}")

    def generate_response(
        self,
        student_id: str,
        message: str,
        target_language: str = "swahili",
        region: str = "lake_basin",
        simplify: bool = False,
        mode: str = "creative"  # 'creative' (Temp 0.75) or 'precise' (Temp 0.2)
    ) -> Dict[str, Any]:
        """
        Generates an adaptive Socratic response implementing the 4Ds Framework with Dynamic Temperature Dialing.
        """
        profile = student_memory.get_or_create_profile(student_id, language=target_language, region=region)
        region_info = REGIONS.get(region, REGIONS["lake_basin"])
        topic_data = find_offline_topic(message)
        
        mastery_summary = ", ".join([f"{k} ({v.mastery_score}% mastery)" for k, v in profile.mastery_graph.items()]) or "New curious learner"
        recent_history = "\n".join([f"{item['role'].upper()}: {item['content']}" for item in profile.recent_interactions[-4:]])
        
        # Temperature Dial: Higher for storytelling/analogies (0.75), Lower for exact calculations/science formulas (0.2)
        temperature = 0.2 if mode == "precise" else 0.75
        
        user_prompt = f"""
=== LEARNER CONTEXT (MAP ASSETS & MEMORY) ===
Student Name: {profile.name}
Grade Level: {profile.grade_level}
Target Language: {target_language.upper()}
Eco-Region: {region_info['name_en']} ({region_info['name_sw']})
Local Species & Ecosystem Assets: {region_info['key_ecosystems']}
Recent Mastery Context: {mastery_summary}
Simplify Mode: {"YES (Explain to a 9-year-old in very simple, loving terms)" if simplify else "STANDARD (Warm, Engaging, Socratic)"}
Reasoning Mode: {mode.upper()} (Temperature: {temperature})

=== RECENT INTERACTION HISTORY ===
{recent_history}

=== STUDENT QUESTION ===
"{message}"

Apply the 4Ds Framework: Deliver a concrete, evident, step-by-step answer with warm African friendship persona.
"""

        # Try Gemini API if client available
        if self.client:
            try:
                # Primary: Google Gemini 3.7 Flash (Hybrid Reasoning Model)
                model_name = os.getenv("GEMINI_MODEL", "gemini-3.7-flash")
                try:
                    response = self.client.models.generate_content(
                        model=model_name,
                        contents=user_prompt,
                        config=types.GenerateContentConfig(
                            system_instruction=SYSTEM_INSTRUCTION,
                            temperature=temperature,
                        )
                    )
                except Exception as model_err:
                    print(f"[ElewaAgent] Primary model {model_name} error: {model_err}. Trying gemini-2.0-flash fallback.")
                    model_name = "gemini-2.0-flash"
                    response = self.client.models.generate_content(
                        model=model_name,
                        contents=user_prompt,
                        config=types.GenerateContentConfig(
                            system_instruction=SYSTEM_INSTRUCTION,
                            temperature=temperature,
                        )
                    )
                response_text = response.text
                
                # Update memory bank
                student_memory.add_interaction_history(student_id, "user", message, target_language)
                student_memory.add_interaction_history(student_id, "assistant", response_text, target_language)
                
                detected_topic = self._extract_topic(message, response_text)
                student_memory.update_topic_interaction(
                    student_id=student_id,
                    topic=detected_topic["topic"],
                    subject=detected_topic["subject"],
                    score_delta=5
                )

                return {
                    "source": "gemini-3.7-flash",
                    "text": response_text,
                    "language": target_language,
                    "region": region,
                    "topic": detected_topic["topic"],
                    "subject": detected_topic["subject"],
                    "mode": mode,
                    "temperature": temperature,
                    "tactile_description": topic_data.get("tactile_audio_description_sw", ""),
                    "sign_cues": topic_data.get("sign_language_visual_cues_sw", ""),
                    "diagram": get_diagram_for_topic(message) or get_diagram_for_topic(detected_topic["topic"]),
                    "quiz_data": topic_data.get("quiz"),
                    "student_profile": student_memory.get_or_create_profile(student_id).model_dump()
                }
            except Exception as e:
                print(f"[ElewaAgent] Gemini API call error: {e}. Falling back to regional offline engine.")

        # Offline fallback applying the exact same 4Ds structure
        return self._generate_offline_response(student_id, message, target_language, region, simplify, mode)

    def _generate_offline_response(self, student_id: str, message: str, language: str, region: str, simplify: bool, mode: str = "creative") -> Dict[str, Any]:
        """Generates rich offline responses executing the 4Ds Framework."""
        topic_data = find_offline_topic(message)
        region_key = region if region in topic_data.get("regional_analogies", {}) else "lake_basin"
        region_info = REGIONS.get(region, REGIONS["lake_basin"])
        is_sw = (language.lower() != "en" and language.lower() != "english")

        title = topic_data["title_sw"] if is_sw else topic_data["title_en"]
        summary = topic_data["summary_sw"] if is_sw else topic_data["summary_en"]
        
        regional_dict = topic_data.get("regional_analogies", {}).get(region_key, {})
        analogy = regional_dict.get("analogy_sw" if is_sw else "analogy_en", topic_data.get("analogy_sw", ""))
        
        exp = topic_data["experiment"]
        quiz = topic_data["quiz"]

        intro = (
            f"Hujambo rafiki yangu mpendwa! 🌟 Nimefurahi sana kusikia swali lako zuri kuhusu eneo letu zuri la **{region_info['icon']} {region_info['name_sw']}**! "
            f"Wewe ni mwanafunzi hodari na mwenye akili nyingi. Hebu tuchunguze jambo hili la kusisimua pamoja kama marafiki:"
            if is_sw else
            f"Hello my dear friend! 🌟 I am so proud of your wonderful question about our beautiful **{region_info['icon']} {region_info['name_en']}**! "
            f"You have such a sharp and curious mind. Let's explore this exciting concept together step-by-step:"
        )

        terms_formatted = "\n".join([f"• **{t['en']}** ➔ {t['sw']}" for t in topic_data["key_terms"]])

        text = f"""### 🔬 {title}

{intro}

{summary}

---

#### 💡 Mfano Halisi wa Eneo Lako ({region_info['icon']} {region_info['name_sw'] if is_sw else region_info['name_en']})
{analogy}

---

#### 📚 Kamusi ya Sayansi (Maneno ya Kujivunia Kujua!)
{terms_formatted}

---

#### 🧪 Jaribu Hili Nyumbani ({exp['title_sw'] if is_sw else exp['title_en']})
**Vifaa:** {exp['materials_sw'] if is_sw else exp['materials_en']}
**Hatua:**
{exp['steps_sw'] if is_sw else exp['steps_en']}

---

#### 🎯 Swali la Kirafiki la Kujipima (Unaweza Kujaribu Bila Wasiwasi!)
**{quiz['question_sw'] if is_sw else quiz['question_en']}**
{chr(10).join(quiz['options_sw'] if is_sw else quiz['options_en'])}
"""

        student_memory.add_interaction_history(student_id, "user", message, language)
        student_memory.add_interaction_history(student_id, "assistant", text, language)
        student_memory.update_topic_interaction(
            student_id=student_id,
            topic=topic_data["title_en"],
            subject=topic_data["subject"],
            score_delta=5
        )

        return {
            "source": "offline_knowledge_vault",
            "text": text,
            "language": language,
            "region": region,
            "topic": topic_data["title_en"],
            "subject": topic_data["subject"],
            "mode": mode,
            "temperature": 0.2 if mode == "precise" else 0.75,
            "tactile_description": topic_data.get("tactile_audio_description_sw", ""),
            "sign_cues": topic_data.get("sign_language_visual_cues_sw", ""),
            "diagram": get_diagram_for_topic(message) or get_diagram_for_topic(topic_data["id"]),
            "quiz_data": quiz,
            "student_profile": student_memory.get_or_create_profile(student_id).model_dump()
        }

    def _extract_topic(self, user_msg: str, bot_response: str) -> Dict[str, str]:
        combined = (user_msg + " " + bot_response).lower()
        if any(w in combined for w in ["fish", "samaki", "gills", "mashavu", "lake", "ziwa", "ngege", "mbuta"]):
            return {"topic": "Aquatic Biology & Respiration", "subject": "Biology"}
        elif any(w in combined for w in ["plant", "mmea", "leaf", "jani", "photo", "cell", "uhai", "biology"]):
            return {"topic": "Photosynthesis & Plant Biology", "subject": "Biology"}
        elif any(w in combined for w in ["electric", "umeme", "circuit", "saketi", "wire", "battery", "betri"]):
            return {"topic": "Electricity & Circuits", "subject": "Physics"}
        elif any(w in combined for w in ["gravity", "grabiti", "force", "nguvu", "friction", "msuguano", "motion"]):
            return {"topic": "Forces & Gravity", "subject": "Physics"}
        elif any(w in combined for w in ["fraction", "sehemu", "math", "hesabu", "divide", "gawanya", "number"]):
            return {"topic": "Fractions & Proportions", "subject": "Mathematics"}
        elif any(w in combined for w in ["solar", "jua", "energy", "nishati", "sun"]):
            return {"topic": "Solar Energy & Heat", "subject": "Physics"}
        else:
            return {"topic": "General STEM Exploration", "subject": "General Science"}


# Singleton Agent
elewa_agent = ElewaAgent()
