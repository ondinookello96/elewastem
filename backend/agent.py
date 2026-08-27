"""
ElewaSTEM (Mwalimu STEM) - Gemini Agent Engine
Orchestrates Gemini 3.5/2.5 multimodal models with Socratic pedagogy, code-switching, and cultural analogies.
"""

import os
import json
from typing import Dict, Any, Optional
from memory import student_memory, StudentProfile
from tools import find_offline_topic

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
Help African students truly understand (Elewa) complex Science, Technology, Engineering, and Mathematics concepts rather than memorizing dry textbook definitions.

KEY PEDAGOGICAL PRINCIPLES:
1. Multilingual & Code-Switching Mastery:
   - Fluidly converse in English, Swahili (Kiswahili Sanifu), or natural youth code-switching (Sheng/conversational bilingual mix).
   - If the student asks in Swahili, explain primarily in warm, clear Swahili, but ALWAYS highlight the key English scientific terms so they can pass formal national exams (e.g. "Usanisinuru (Photosynthesis)").
   - If the student asks in English, explain in clear English and provide the Swahili terms and analogies for deeper conceptual grounding.

2. Culturally Grounded African Analogies:
   - Ground abstract concepts in relatable African daily life, agriculture, nature, and everyday technologies:
     * Current & Voltage -> Water flowing from an elevated tank (tenki la maji) through irrigation pipes.
     * Heat Transfer & Energy -> Cooking on a jiko, sun drying maize/cassava, solar lanterns.
     * Biology & Cells -> Bricks forming a homestead, village community roles, acacia trees and drought adaptation.
     * Gravity & Friction -> Ripened mangoes falling from a tree, braking a bicycle on a red dirt road.
     * Math & Fractions -> Slicing and sharing chapatis, counting cattle in herds, market trading.

3. Socratic & Encouraging Tone:
   - Be patient, celebratory ("Hongera sana!", "Vizuri mno!", "Great thinking!"), and never dismissive.
   - Break down complex formulas into easy intuitive steps.
   - Suggest safe, hands-on mini-experiments using everyday household items (bottles, salt, water, sunlight, coins).

4. Output Format:
   Always structure your response cleanly with:
   - Main Explanation (conversational, engaging, formatted with bolding and bullet points).
   - "💡 Mfano Halisi / Everyday Analogy" (the relatable local metaphor).
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
        simplify: bool = False
    ) -> Dict[str, Any]:
        """Generates an adaptive, multilingual response for the student."""
        profile = student_memory.get_or_create_profile(student_id, language=target_language)
        
        # Build student context memory
        mastery_summary = ", ".join([f"{k} ({v.mastery_score}% mastery)" for k, v in profile.mastery_graph.items()]) or "New student"
        recent_history = "\n".join([f"{item['role'].upper()}: {item['content']}" for item in profile.recent_interactions[-4:]])
        
        user_prompt = f"""
Student Name: {profile.name}
Grade Level: {profile.grade_level}
Preferred Language: {target_language.upper()}
Recent Mastery Context: {mastery_summary}
Simplify Mode: {"YES (Explain to a 9-year-old in very simple terms)" if simplify else "STANDARD (Engaging & Clear)"}

Recent Conversation:
{recent_history}

Student Question:
"{message}"

Provide a comprehensive, empathetic, and culturally rich STEM explanation following your instructions.
"""

        # Try Gemini API if client available
        if self.client:
            try:
                # Use Gemini 2.5 Flash for high-speed, cost-effective reasoning
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
                
                # Detect topic and update mastery graph
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
                    "topic": detected_topic["topic"],
                    "subject": detected_topic["subject"],
                    "student_profile": student_memory.get_or_create_profile(student_id).model_dump()
                }
            except Exception as e:
                print(f"[ElewaAgent] Gemini API call error: {e}. Falling back to offline engine.")

        # High quality offline fallback generator
        return self._generate_offline_response(student_id, message, target_language, simplify)

    def _generate_offline_response(self, student_id: str, message: str, language: str, simplify: bool) -> Dict[str, Any]:
        """Generates rich, pre-compiled educational responses for offline / zero-connection mode."""
        topic_data = find_offline_topic(message)
        is_sw = (language.lower() == "swahili")

        title = topic_data["title_sw"] if is_sw else topic_data["title_en"]
        summary = topic_data["summary_sw"] if is_sw else topic_data["summary_en"]
        analogy = topic_data["analogy_sw"] if is_sw else topic_data["analogy_en"]
        exp = topic_data["experiment"]
        quiz = topic_data["quiz"]

        if simplify:
            intro = "Habari! Tutaifanya iwe rahisi kabisa:" if is_sw else "Hello! Let's make this super simple:"
        else:
            intro = "Karibu kwenye darasa la sayansi! Hebu tuchunguze hili pamoja:" if is_sw else "Welcome to science class! Let's explore this together:"

        terms_formatted = "\n".join([f"• **{t['en']}** ➔ {t['sw']}" for t in topic_data["key_terms"]])

        text = f"""### 🔬 {title}

{intro}

{summary}

---

#### 💡 Mfano Halisi (Everyday Analogy)
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
            "topic": topic_data["title_en"],
            "subject": topic_data["subject"],
            "quiz_data": quiz,
            "student_profile": student_memory.get_or_create_profile(student_id).model_dump()
        }

    def _extract_topic(self, user_msg: str, bot_response: str) -> Dict[str, str]:
        """Identifies STEM subject and topic from text."""
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
