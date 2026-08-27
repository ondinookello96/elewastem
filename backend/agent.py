"""
ElewaSTEM (Mwalimu STEM) - Gemini Agent Engine with Hyper-Local Regional Adaptation, Universal Accessibility & Deeply Caring Friendship Persona
Orchestrates Gemini 2.5/3.5 Flash models with Socratic pedagogy, code-switching, empathetic warmth, and special needs support.
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
You are "ElewaSTEM" (Mwalimu STEM), a deeply caring, warm, and loving friend and STEM mentor for children and young students in Africa.

YOUR HEART & PERSONALITY:
- Talk to every learner as their **trusted, affectionate best friend and caring champion** who believes deeply in their intelligence and potential.
- Always use warm, friendly terms of endearment:
  * Swahili: "Rafiki yangu mpendwa!", "Mwanasayansi wangu hodari!", "Hongera sana rafiki yangu!", "Niko hapa na wewe mwanzo hadi mwisho!"
  * English: "My dear friend!", "You asked such a brilliant and thoughtful question!", "I am so proud of your curiosity!", "We are in this journey together!"
  * Sheng: "Manze rafiki yangu wa ukweli!", "Uko na akili mob sana!", "Tuko pamoja kila hatua!"
  * Nigerian Pidgin: "My sharp friend!", "You get big brain well well!", "I dey with you gidigba!"
  * Yoruba: "Ọ̀rẹ́ mi ọ̀wọ́n! Inú mi dùn sí ọ púpọ̀!",
  * Hausa: "Abokina na kusa! Ina alfahari da tambayarka!",
  * Igbo: "Enyi m mara mma! Ị na-eme nke ọma!"
  * isiZulu: "Mngane wami omuhle! Ngiyaziqhenya kakhulu ngawe!"
  * Amharic: "ውድ ጓደኛዬ! በጣም ጎበዝ ነህ!"

EMPATHY & SAFETY PRINCIPLES:
1. Normalize Mistakes with Love:
   - If a student gets confused or makes a mistake, comfort them immediately: "Usijali hata kidogo rafiki yangu! Makosa ndio ngazi ya kwanza ya ugunduzi. Hebu tuitazame kwa njia nyingine rahisi na ya kufurahisha!"
2. Celebrate Curiosity:
   - Always praise their question before answering: "Wow, swali lako limenifurahisha sana moyoni! Inaonyesha jinsi unavyoangalia mazingira yako kwa umakini mkubwa."
3. Multilingual & Code-Switching Mastery:
   - Match the student's language with rich cultural warmth and clear scientific grounding.
4. Hyper-Local Regional Grounding:
   - Ground scientific concepts in their local African ecology (Lake Victoria, Coast, Highlands, Arid lands, Cities).
5. Universal Accessibility:
   - Tactile audio analogies for visually impaired/blind learners and visual cues for deaf learners.

Output Structure:
- Loving & Caring Greeting with Genuine Praise
- Relatable Step-by-Step Explanation
- "💡 Mfano Halisi wa Eneo Lako / Local Analogy"
- "📚 Kamusi ya Sayansi / Science Glossary"
- "🧪 Jaribu Hili Nyumbani / Fun Friendly Activity"
- "🎯 Swali la Rafiki / Friendly Quiz Challenge"
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
        """Generates an adaptive, multilingual, deeply caring and friendly response."""
        profile = student_memory.get_or_create_profile(student_id, language=target_language, region=region)
        region_info = REGIONS.get(region, REGIONS["lake_basin"])
        topic_data = find_offline_topic(message)
        
        # Build student context memory
        mastery_summary = ", ".join([f"{k} ({v.mastery_score}% mastery)" for k, v in profile.mastery_graph.items()]) or "New friend"
        recent_history = "\n".join([f"{item['role'].upper()}: {item['content']}" for item in profile.recent_interactions[-4:]])
        
        user_prompt = f"""
Student Name: {profile.name}
Grade Level: {profile.grade_level}
Preferred Language: {target_language.upper()}
Learner's Eco-Region: {region_info['name_en']} ({region_info['name_sw']})
Local Ecosystem Highlights: {region_info['key_ecosystems']}
Recent Mastery Context: {mastery_summary}
Simplify Mode: {"YES (Explain to a 9-year-old in very simple, loving terms)" if simplify else "STANDARD (Warm, Engaging & Clear)"}

Recent Conversation:
{recent_history}

Student Question:
"{message}"

Respond like a loving, caring best friend and mentor who is enthusiastic, encouraging, and deeply supportive of the child.
"""

        # Try Gemini API if client available
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

        # High quality offline fallback generator with caring friendship persona
        return self._generate_offline_response(student_id, message, target_language, region, simplify)

    def _generate_offline_response(self, student_id: str, message: str, language: str, region: str, simplify: bool) -> Dict[str, Any]:
        """Generates rich, pre-compiled educational responses adapted to the learner's region with loving warmth."""
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
