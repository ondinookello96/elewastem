"""
ElewaSTEM (Mwalimu STEM) - Gemini Agent Engine
Engineered on AIM, MAP, and OCEAN Cognitive Architecture Frameworks with Socratic Pedagogy,
Hyper-Local Regional Grounding, Universal Special Needs Accessibility, and Empathetic Friendship.
"""

import os
import json
from typing import Dict, Any, Optional
from memory import student_memory, StudentProfile
from tools import find_offline_topic, REGIONS

# Optional google-genai SDK import
try:
    from google import genai
    from google.genai import types
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False


SYSTEM_INSTRUCTION = """
You are "ElewaSTEM" (Mwalimu STEM), a world-class, deeply caring AI STEM mentor and loyal friend to African children.

================================================================================
1. THE AIM FRAMEWORK (Core Architecture)
================================================================================
- [A] ACTOR: An affectionate, enthusiastic African STEM mentor and best friend who believes every child is a natural genius.
- [I] INPUT: Dynamic learner context including geographic eco-region (Lake Basin, Coast, Highlands, Arid, Urban), grade level, language/dialect, special needs accessibility profile, and mastery history.
- [M] MISSION: Deliver Socratic, engaging, step-by-step STEM mastery using culturally and ecologically grounded African analogies, fostering a growth mindset ("Usimeze, Elewa!").

================================================================================
2. THE OCEAN FRAMEWORK (Human Taste & Storytelling)
================================================================================
- [O] ORIGINAL: Reject generic Western textbook tropes (snow, baseball, subway trains). Use indigenous African phenomena (Lake Victoria Tilapia Ngege respiration, Dunga beach papyrus, acacia transpiration in Turkana).
- [C] CONCRETE: Use specific local places, vernacular species names, tangible numbers, and everyday household materials (Osuga/Managu, Minazi, Mikoko, 12V fishing lights).
- [E] EVIDENT: Show the underlying scientific logic step-by-step; provide a safe, zero-cost at-home mini-experiment so the child can prove the concept with their own hands.
- [A] ASSERTIVE: Take an affirmative, encouraging stance. Normalize mistakes with unconditional warmth: "Makosa ndio ngazi ya kwanza ya ugunduzi!"
- [N] NARRATIVE: Wrap scientific insights in warm cultural stories and affectionate terms of endearment across 16+ African languages:
  * Swahili: "Rafiki yangu mpendwa!", "Mwanasayansi wangu hodari!"
  * English: "My dear friend!", "What a brilliant and thoughtful question!"
  * Sheng: "Manze rafiki yangu wa ukweli!", "Uko na akili mob sana!"
  * Nigerian Pidgin: "My sharp friend!", "You get big brain well well!"
  * Yoruba: "Ọ̀rẹ́ mi ọ̀wọ́n! Inú mi dùn sí ọ púpọ̀!"
  * Hausa: "Abokina na kusa! Ina alfahari da kai!"
  * Igbo: "Enyi m mara mma! Ị na-eme nke ọma!"
  * isiZulu: "Mngane wami omuhle! Ngiyaziqhenya kakhulu ngawe!"

================================================================================
3. PEDAGOGICAL TRACKING & REASONING (Chain-of-Thought & Verifier Pattern)
================================================================================
- Chain-of-Thought: Break complex concepts down logically (Observation ➔ Mechanism ➔ Local Analogy ➔ Home Practice).
- Verifier Probing: Engage the child's curiosity by asking an intuitive guiding question before diving into definitions.
- Special Needs Layer:
  * Visually Impaired / Blind: Include tactile audio descriptions ("Shika jani bichi... hisi mishipa midogo...").
  * Hearing Impaired / Deaf: Provide visual sign language cues (KSL) and structured flowcharts.

================================================================================
4. REQUIRED RESPONSE STRUCTURE
================================================================================
1. Loving & Caring Greeting with Genuine Praise
2. Relatable Step-by-Step Explanation (Chain-of-Thought)
3. "💡 Mfano Halisi wa Eneo Lako / Local Eco-Analogy" (Concrete & Original)
4. "📚 Kamusi ya Sayansi / Science Glossary" (Bilingual Concept Pairs)
5. "🧪 Jaribu Hili Nyumbani / Fun Friendly Activity" (Evident Proof)
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
        simplify: bool = False
    ) -> Dict[str, Any]:
        """
        Generates an adaptive, multilingual response implementing the AIM, MAP, and OCEAN frameworks.
        """
        # [M] MEMORY & [A] ASSETS retrieval
        profile = student_memory.get_or_create_profile(student_id, language=target_language, region=region)
        region_info = REGIONS.get(region, REGIONS["lake_basin"])
        topic_data = find_offline_topic(message)
        
        mastery_summary = ", ".join([f"{k} ({v.mastery_score}% mastery)" for k, v in profile.mastery_graph.items()]) or "New curious learner"
        recent_history = "\n".join([f"{item['role'].upper()}: {item['content']}" for item in profile.recent_interactions[-4:]])
        
        # [P] PROMPT ORCHESTRATION
        user_prompt = f"""
Student Name: {profile.name}
Grade Level: {profile.grade_level}
Preferred Language: {target_language.upper()}
Learner's Eco-Region: {region_info['name_en']} ({region_info['name_sw']})
Local Ecosystem Highlights (Concrete Assets): {region_info['key_ecosystems']}
Recent Mastery Context (Memory Bank): {mastery_summary}
Simplify Mode: {"YES (Explain to a 9-year-old in very simple, loving terms)" if simplify else "STANDARD (Warm, Engaging, Socratic)"}

Recent Conversation History:
{recent_history}

Student Question:
"{message}"

Apply AIM, MAP, and OCEAN principles: be original, concrete, evident, and narrative with affectionate encouragement.
"""

        # Try Gemini API if available
        if self.client:
            try:
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        temperature=0.7,
                    )
                )
                response_text = response.text
                
                # Update memory
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
                    "source": "gemini-2.5-flash",
                    "text": response_text,
                    "language": target_language,
                    "region": region,
                    "topic": detected_topic["topic"],
                    "subject": detected_topic["subject"],
                    "tactile_description": topic_data.get("tactile_audio_description_sw", ""),
                    "sign_cues": topic_data.get("sign_language_visual_cues_sw", ""),
                    "quiz_data": topic_data.get("quiz"),
                    "student_profile": student_memory.get_or_create_profile(student_id).model_dump()
                }
            except Exception as e:
                print(f"[ElewaAgent] Gemini API call error: {e}. Falling back to regional offline engine.")

        # Offline fallback applying the exact same AIM, MAP, and OCEAN structure
        return self._generate_offline_response(student_id, message, target_language, region, simplify)

    def _generate_offline_response(self, student_id: str, message: str, language: str, region: str, simplify: bool) -> Dict[str, Any]:
        """Generates rich, pre-compiled educational responses grounded in AIM, MAP, and OCEAN."""
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
            "tactile_description": topic_data.get("tactile_audio_description_sw", ""),
            "sign_cues": topic_data.get("sign_language_visual_cues_sw", ""),
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
