"""
ElewaSTEM (Mwalimu STEM) - Gemini Agent Engine with Hyper-Local Regional Adaptation
Orchestrates Gemini 2.5/3.5 Flash models with Socratic pedagogy, code-switching, and regional eco-zone context.
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
You are "ElewaSTEM" (Mwalimu STEM), a friendly, culturally grounded, and inspiring AI STEM tutor for children and young students in Africa.

YOUR MISSION:
Help African students truly understand (Elewa) complex Science, Technology, Engineering, and Mathematics concepts through intuitive, regionally adapted analogies in their own language.

KEY PEDAGOGICAL & REGIONAL PRINCIPLES:
1. Multilingual & Code-Switching Mastery:
   - Fluidly converse in English, Swahili (Kiswahili Sanifu), or natural youth code-switching (Sheng/conversational mix).
   - If asked in Swahili, explain in warm, clear Swahili, but ALWAYS highlight key English scientific terms (e.g. "Usanisinuru (Photosynthesis)").
   - If asked in English, explain clearly and provide the Swahili terms and analogies for deeper conceptual grounding.

2. Hyper-Local Regional Adaptation (Geo-Context):
   Tailor your examples, crops, physical phenomena, and analogies to the student's specific geographic region:
   * COASTAL (Pwani): Use coconut palms (minazi), mangroves (mikoko), ocean tides & gravity, solar evaporation in salt pans, sea breezes.
   * HIGHLANDS (Nyanda za Juu): Use tea/maize farming, cascading mountain rivers, hydroelectric dams, terracing against soil erosion, cool mountain climates.
   * LAKE BASIN (Ziwa Victoria): Use lake breeze convection, tilapia/fish oxygenation, lake transport, flash thunderstorms.
   * ARID & PASTORALIST (Ukame / ASAL): Use intense solar PV energy, borehole water pumping, acacia/cactus drought adaptations, camel heat regulation.
   * URBAN (Mijini): Use solar streetlights, vehicle friction & tire treads, electronics in matatus, stormwater drainage.

3. Socratic & Encouraging Tone:
   - Be patient, celebratory ("Hongera sana!", "Vizuri mno!", "Great thinking!"), and never dismissive.
   - Break down complex formulas into easy intuitive steps.
   - Suggest safe, hands-on mini-experiments using everyday household items.

4. Output Format:
   Always structure your response cleanly with:
   - Main Explanation (conversational, engaging, formatted with bolding and bullet points).
   - "💡 Mfano Halisi wa Eneo Lako / Local Analogy" (the relatable regional metaphor).
   - "📚 Kamusi ya Sayansi / Science Glossary" (Key English terms with Swahili explanations).
   - "🧪 Jaribu Hili Nyumbani / Try This At Home" (a safe 2-minute experiment).
   - "🎯 Swali la Jaribio / Quick Check" (a fun question to test their understanding).
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
        region: str = "highlands",
        simplify: bool = False
    ) -> Dict[str, Any]:
        """Generates an adaptive, multilingual, region-specific response."""
        profile = student_memory.get_or_create_profile(student_id, language=target_language, region=region)
        region_info = REGIONS.get(region, REGIONS["highlands"])
        
        # Build student context memory
        mastery_summary = ", ".join([f"{k} ({v.mastery_score}% mastery)" for k, v in profile.mastery_graph.items()]) or "New student"
        recent_history = "\n".join([f"{item['role'].upper()}: {item['content']}" for item in profile.recent_interactions[-4:]])
        
        user_prompt = f"""
Student Name: {profile.name}
Grade Level: {profile.grade_level}
Preferred Language: {target_language.upper()}
Learner's Eco-Region: {region_info['name_en']} ({region_info['name_sw']})
Local Ecosystem Highlights: {region_info['key_ecosystems']}
Recent Mastery Context: {mastery_summary}
Simplify Mode: {"YES (Explain to a 9-year-old in very simple terms)" if simplify else "STANDARD (Engaging & Clear)"}

Recent Conversation:
{recent_history}

Student Question:
"{message}"

Provide a comprehensive, empathetic, and culturally rich STEM explanation grounded in the student's eco-region ({region_info['name_en']}).
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
                    "student_profile": student_memory.get_or_create_profile(student_id).model_dump()
                }
            except Exception as e:
                print(f"[ElewaAgent] Gemini API call error: {e}. Falling back to regional offline engine.")

        # High quality offline fallback generator with regional adaptations
        return self._generate_offline_response(student_id, message, target_language, region, simplify)

    def _generate_offline_response(self, student_id: str, message: str, language: str, region: str, simplify: bool) -> Dict[str, Any]:
        """Generates rich, pre-compiled educational responses adapted to the learner's region."""
        topic_data = find_offline_topic(message)
        region_key = region if region in topic_data.get("regional_analogies", {}) else "highlands"
        region_info = REGIONS.get(region, REGIONS["highlands"])
        is_sw = (language.lower() != "english")

        title = topic_data["title_sw"] if is_sw else topic_data["title_en"]
        summary = topic_data["summary_sw"] if is_sw else topic_data["summary_en"]
        
        regional_dict = topic_data.get("regional_analogies", {}).get(region_key, {})
        analogy = regional_dict.get("analogy_sw" if is_sw else "analogy_en", topic_data.get("analogy_sw", ""))
        
        exp = topic_data["experiment"]
        quiz = topic_data["quiz"]

        intro = f"Habari kutoka **{region_info['icon']} {region_info['name_sw']}**! Hebu tuchunguze hili pamoja:" if is_sw else f"Hello from the **{region_info['icon']} {region_info['name_en']}**! Let's explore this together:"

        terms_formatted = "\n".join([f"• **{t['en']}** ➔ {t['sw']}" for t in topic_data["key_terms"]])

        text = f"""### 🔬 {title}

{intro}

{summary}

---

#### 💡 Mfano Halisi wa Eneo Lako ({region_info['icon']} {region_info['name_sw'] if is_sw else region_info['name_en']})
{analogy}

---

#### 📚 Kamusi ya Sayansi (Key Science Terms)
{terms_formatted}

---

#### 🧪 Jaribu Hili Nyumbani ({exp['title_sw'] if is_sw else exp['title_en']})
**Vifaa:** {exp['materials_sw'] if is_sw else exp['materials_en']}
**Hatua:**
{exp['steps_sw'] if is_sw else exp['steps_en']}

---

#### 🎯 Swali la Haraka (Quick Check)
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
            "quiz_data": quiz,
            "student_profile": student_memory.get_or_create_profile(student_id).model_dump()
        }

    def _extract_topic(self, user_msg: str, bot_response: str) -> Dict[str, str]:
        combined = (user_msg + " " + bot_response).lower()
        if any(w in combined for w in ["plant", "mmea", "leaf", "jani", "photo", "cell", "uhai", "biology"]):
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
