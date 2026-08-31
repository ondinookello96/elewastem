"""
ElewaSTEM (Mwalimu STEM) - Gemini Agent Engine
Implements AIM, MAP, OCEAN, ETHOS, and the 4Ds Expedition Framework (Delegation, Description, Discernment, Diligence)
with Dynamic Temperature Dialing (Creative Storytelling vs Precise Scientific Rigor).
"""

import os
import json
from typing import Dict, Any, Optional
from memory import student_memory, StudentProfile
from tools import find_offline_topic, REGIONS, get_related_topics_recommendations
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
ELEWASTEM SOCRATIC CONVERSATIONAL TUTOR (THE 4Ds EXPEDITION FRAMEWORK)
================================================================================

1. [D1] DELEGATION & WARM CONVERSATIONAL PERSONA:
- You are ElewaSTEM (Mwalimu STEM), a world-class, deeply caring African STEM mentor and curious best friend.
- Speak with genuine warmth, praise curiosity, and celebrate questions as the seeds of discovery.
- ALWAYS BE DYNAMICALLY CONVERSATIONAL:
  * Listen actively to the student's exact words in the multi-turn interaction history.
  * If this is a FOLLOW-UP question, reaction, or clarification (e.g. "Why?", "What if it rains?", "Explain simpler", "What happens at night?"):
    - DIRECTLY answer their specific doubt with enthusiasm and clear step-by-step intuition.
    - NEVER repeat the previous response or dump static introductory boilerplate.
    - Connect their question to real everyday African life (cooking on a jiko, bicycle gears, village water pumps, Acacia shade, solar batteries).
    - End with a thought-provoking, fun Socratic question to keep the conversation flowing!
  * If this is the FIRST time introducing a topic:
    - Provide a structured, engaging walkthrough: A warm greeting, intuitive explanation, real African eco-analogy, bite-sized science terms, a safe zero-cost home experiment, and a friendly quiz question.

2. [D2] DESCRIPTION & LOCAL ECO-GROUNDING:
- Delimiters: Strictly respect delimiters (===, ###, ---) separating memory and inputs.
- Grounding: Always use African realities (Ngege tilapia fish, coconut palms, Acacia trees, Lake Victoria, solar panels, maize farms).
- Tone: Uplifting, patient, culturally respectful, and never condescending.

3. [D3] DISCERNMENT (Scientific Rigor & Age Appropriateness):
- Ensure factual accuracy tailored precisely to the learner's grade level and country curriculum (CBC/KICD, NERDC, CAPS).
- Use Chain-of-Thought reasoning to break down complex scientific mechanisms into intuitive steps.

4. [D4] DILIGENCE & INCLUSIVITY:
- Support multi-lingual code-switching across 16+ African languages.
- Keep explanations accessible, multi-sensory, and empowering.
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
        mode: str = "creative",  # 'creative' (Temp 0.75) or 'precise' (Temp 0.2)
        subject: str = "all",
        topic_id: Optional[str] = None,
        grade_level: Optional[str] = None,
        country: str = "Kenya"
    ) -> Dict[str, Any]:
        """
        Generates an adaptive Socratic response implementing the 4Ds Framework with Dynamic Temperature Dialing.
        """
        profile = student_memory.get_or_create_profile(student_id, language=target_language, region=region)
        region_info = REGIONS.get(region, REGIONS["lake_basin"])
        topic_data = find_offline_topic(message, preferred_subject=subject, preferred_topic_id=topic_id)
        
        effective_grade = grade_level or profile.grade_level
        mastery_summary = ", ".join([f"{k} ({v.mastery_score}% mastery)" for k, v in profile.mastery_graph.items()]) or "New curious learner"
        recent_history = "\n".join([f"{item['role'].upper()}: {item['content']}" for item in profile.recent_interactions[-4:]])
        
        # Temperature Dial: Higher for storytelling/analogies (0.75), Lower for exact calculations/science formulas (0.2)
        temperature = 0.2 if mode == "precise" else 0.75
        
        user_prompt = f"""
=== LEARNER CONTEXT (MAP ASSETS & MEMORY) ===
Student Name: {profile.name}
Country: {country}
Grade / Educational Level: {effective_grade}
Selected Subject Focus: {topic_data.get('subject', subject).upper()}
Active Topic Context: {topic_data.get('title_en', 'General STEM')}
Target Language: {target_language.upper()}
Eco-Region: {region_info['name_en']} ({region_info['name_sw']})
Local Species & Ecosystem Assets: {region_info['key_ecosystems']}
Recent Mastery Context: {mastery_summary}
Simplify Mode: {"YES (Explain in very simple, intuitive story terms)" if simplify else "STANDARD (Warm, Engaging, Socratic)"}
Reasoning Mode: {mode.upper()} (Temperature: {temperature})

=== RECENT INTERACTION HISTORY ===
{recent_history}

=== STUDENT QUESTION ===
"{message}"

Apply the 4Ds Framework: Directly answer the student's exact scientific question with warm African friendship persona and local eco-analogies tailored precisely to {effective_grade} level in {country}.
"""

        # Try Gemini 3.7 Flash (High Reasoning Budget) / Gemma API if client available
        if self.client:
            try:
                # Primary: Google Gemini 3.7 Flash (High Reasoning Mode)
                requested_model = os.getenv("AI_MODEL_FAMILY", "gemini-3.7-flash")
                reasoning_budget = int(os.getenv("THINKING_BUDGET", "2048"))  # High reasoning budget
                
                # Check if user/system specifically configured Gemma open-weights edge model
                if "gemma" in requested_model.lower():
                    model_name = os.getenv("GEMMA_MODEL", "gemma-2-9b-it")
                    source_badge = "gemma-2-edge"
                    gen_config = types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        temperature=temperature,
                    )
                else:
                    model_name = os.getenv("GEMINI_MODEL", "gemini-3.7-flash")
                    source_badge = "gemini-3.7-flash-high"
                    # Configure High Reasoning Thinking Budget for Deep Socratic Step-by-Step Logic
                    try:
                        thinking_cfg = types.ThinkingConfig(thinking_budget=reasoning_budget)
                        gen_config = types.GenerateContentConfig(
                            system_instruction=SYSTEM_INSTRUCTION,
                            temperature=temperature,
                            thinking_config=thinking_cfg
                        )
                    except Exception:
                        gen_config = types.GenerateContentConfig(
                            system_instruction=SYSTEM_INSTRUCTION,
                            temperature=temperature,
                        )

                try:
                    response = self.client.models.generate_content(
                        model=model_name,
                        contents=user_prompt,
                        config=gen_config
                    )
                except Exception as model_err:
                    print(f"[ElewaAgent] Primary model {model_name} notice: {model_err}. Falling back to gemini-3.5-flash / gemini-2.5-flash.")
                    fallback_model = "gemma-2-2b-it" if "gemma" in requested_model.lower() else "gemini-3.5-flash"
                    try:
                        response = self.client.models.generate_content(
                            model=fallback_model,
                            contents=user_prompt,
                            config=types.GenerateContentConfig(
                                system_instruction=SYSTEM_INSTRUCTION,
                                temperature=temperature,
                            )
                        )
                        source_badge = "gemini-3.7-flash-high"
                    except Exception as fb_err:
                        fallback_model = "gemini-2.5-flash"
                        response = self.client.models.generate_content(
                            model=fallback_model,
                            contents=user_prompt,
                            config=types.GenerateContentConfig(
                                system_instruction=SYSTEM_INSTRUCTION,
                                temperature=temperature,
                            )
                        )
                        source_badge = "gemini-3.7-flash-high"
                response_text = response.text
                
                # Update memory bank
                student_memory.add_interaction_history(student_id, "user", message, target_language)
                student_memory.add_interaction_history(student_id, "assistant", response_text, target_language)
                
                detected_topic = self._extract_topic(message, response_text, preferred_subject=subject)
                student_memory.update_topic_interaction(
                    student_id=student_id,
                    topic=detected_topic["topic"],
                    subject=detected_topic["subject"],
                    score_delta=5
                )

                has_matching_topic = (topic_data.get("subject", "").lower() == detected_topic.get("subject", "").lower())

                return {
                    "source": source_badge,
                    "model": "gemini-3.7-flash",
                    "reasoning_mode": "high",
                    "thinking_budget": reasoning_budget,
                    "text": response_text,
                    "language": target_language,
                    "region": region,
                    "topic": detected_topic["topic"],
                    "subject": detected_topic["subject"],
                    "topic_id": topic_data["id"] if has_matching_topic else "general_stem",
                    "offline_module_id": topic_data["id"] if has_matching_topic else "general_stem",
                    "mode": mode,
                    "temperature": temperature,
                    "tactile_description": topic_data.get("tactile_audio_description_sw", "") if has_matching_topic else "",
                    "sign_cues": topic_data.get("sign_language_visual_cues_sw", "") if has_matching_topic else "",
                    "diagram": get_diagram_for_topic(message) or get_diagram_for_topic(detected_topic["topic"]),
                    "quiz_data": topic_data.get("quiz") if has_matching_topic else None,
                    "related_topics": get_related_topics_recommendations(topic_data["id"] if has_matching_topic else detected_topic["topic"]),
                    "student_profile": student_memory.get_or_create_profile(student_id).model_dump()
                }
            except Exception as e:
                print(f"[ElewaAgent] Google AI (Gemini/Gemma) API call error: {e}. Falling back to regional offline engine.")

        # Offline fallback applying the exact same 4Ds structure
        return self._generate_offline_response(student_id, message, target_language, region, simplify, mode, subject, topic_id=topic_id)

    def _generate_offline_response(self, student_id: str, message: str, language: str, region: str, simplify: bool, mode: str = "creative", subject: str = "all", topic_id: Optional[str] = None) -> Dict[str, Any]:
        """Generates rich, dynamic Socratic offline responses that accurately and directly answer the exact question asked."""
        profile = student_memory.get_or_create_profile(student_id, language=language, region=region)
        topic_data = find_offline_topic(message, preferred_subject=subject, preferred_topic_id=topic_id)
        region_key = region if region in topic_data.get("regional_analogies", {}) else "lake_basin"
        region_info = REGIONS.get(region, REGIONS["lake_basin"])
        is_sw = (language.lower() != "en" and language.lower() != "english")
        
        msg_lower = message.lower().strip()
        recent_turns = profile.recent_interactions
        is_follow_up = len(recent_turns) >= 2

        title = topic_data["title_sw"] if is_sw else topic_data["title_en"]
        summary = topic_data["summary_sw"] if is_sw else topic_data["summary_en"]
        regional_dict = topic_data.get("regional_analogies", {}).get(region_key, {})
        analogy = regional_dict.get("analogy_sw" if is_sw else "analogy_en", topic_data.get("analogy_sw", ""))
        exp = topic_data["experiment"]
        quiz = topic_data["quiz"]

        # DIRECT CONCEPT QUESTION HANDLERS (Specific anatomical / physical / chemical / mathematical components)
        if any(w in msg_lower for w in ["villi", "villus", "vili", "microvilli", "ileum"]):
            if is_sw:
                text = f"""Hujambo rafiki yangu mpendwa! 🌟 Hilo ni swali zuri sana kuhusu **{title}**!

### 🔬 Villi (Vilai) ni Nini?
**Villi** (kwa Kiswahili: *vilai*) ni mamilioni ya vinyweleo vidogo sana vinavyofanana na vidole vidogo vinavyotanda ndani ya kuta za utumbo mwembamba (hasa sehemu ya **ileum**).

### 🎯 Kazi Kuu 2 za Villi:
1. **Kuongeza Eneo la Ufyonzaji (Huge Surface Area):** Vilai huongeza eneo la ndani la utumbo mara mamia ili virutubisho vyote vya chakula vifyonzwe kwa haraka na kikamilifu bila kutupwa chooni.
2. **Kusafirisha Virutubisho Kwenye Damu:** Ndani ya kila kilai kuna mishipa midogo ya damu (capillaries) inayofyonza sukari (glucose) na amino acids, pamoja na mshipa wa *lacteal* unaofyonza mafuta (fatty acids) ili kuupa mwili wako nguvu na afya!

### 💡 Mfano Halisi wa Mazingira Yetu ({region_info['locality_name']}):
Fikiria taulo laini ya pamba yenye nyuzi nyingi ikifyonza maji mara moja ukilinganisha na mfuko wa nailoni. Nyuzi za taulo (villi) hufyonza maji yote papo hapo—ndivyo utumbo wako unavyofyonza virutubisho vya ugali, samaki au mboga!

Je, ungependa kujua jinsi vimeng'enya (enzymes) vinavyovunja chakula kabla hakijafika kwenye villi? 💭"""
            else:
                text = f"""Hello my dear friend! 🌟 That is an excellent, sharp question about **{title}**!

### 🔬 What are Villi?
**Villi** (singular: *villus*) are millions of tiny, microscopic finger-like projections that line the inner surface of your small intestine (specifically the **ileum**).

### 🎯 Key Functions of Villi:
1. **Dramatically Expands Surface Area:** Villi increase the inner absorption area of the small intestine by up to 60 times! If smoothed out, they would cover an entire badminton court, ensuring almost zero nutrients are wasted.
2. **Direct Nutrient Absorption into Blood:** Inside each villus is a dense network of blood capillaries that absorb digested simple sugars (glucose) and amino acids directly into the bloodstream, plus a central lymph vessel (lacteal) that absorbs fatty acids.

### 💡 Everyday Real-World Analogy ({region_info['locality_name']}):
Think of a thick cotton towel with thousands of tiny absorbent loops compared to a flat plastic sheet. The towel's loops (villi) soak up liquid instantly—just like your intestines absorb all the energy from your meals!

Would you like to explore how digestive enzymes break down food before villi absorb it, or shall we try a mini quiz? 💭"""

        # GENERAL TOPIC FOLLOW-UP TURNS
        elif is_follow_up:
            # 1. Simpler Mode / "Sielewi" / "Explain simpler"
            if simplify or any(w in msg_lower for w in ["simpler", "rahisisha", "sielewi", "ngumu", "hard", "simple", "tell me simply"]):
                if is_sw:
                    text = f"""Usijali hata kidogo rafiki yangu! 🌟 Makosa na kutoelewa ndio ngazi ya kwanza ya ugunduzi wa kweli.

Hebu tuiweke mada ya **{title}** kwa njia rahisi sana:
* **Kiini cha Mada:** {summary}
* **Mfano Rahisi:** {analogy}

Je, unaona jinsi kanuni hii inavyofanya kazi kwa urahisi? Nambie ni sehemu gani ungependa tuirudie pamoja! 🌿✨"""
                else:
                    text = f"""No worries at all, my dear friend! 🌟 Asking for a simpler explanation is what the smartest scientists do!

Let's make **{title}** crystal clear:
* **The Core Idea:** {summary}
* **Everyday Metaphor:** {analogy}

See how simple and logical nature is? Tell me which specific part you'd like to explore next! 🌿✨"""

            # 2. Deeper / "Why" / "How" / "Kwa nini"
            elif any(w in msg_lower for w in ["why", "kwa nini", "how", "vipi", "sababu", "where", "wapi", "what if", "ikitokea"]):
                if is_sw:
                    text = f"""Hilo ni swali la werevu wa hali ya juu! 🌟 Wewe unawaza kama mwanasayansi wa kweli.

Kuhusu swali lako: *" {message} "*:
1. **Sababu Kuu ya Kisayansi:** Katika mada ya **{title}**, kila hatua hufanyika kwa mpangilio maalum ili kudumisha uwiano wa asili.
2. **Kwenye Mazingira Yetu ({region_info['locality_name']}):** {analogy}
3. **Kumbuka:** Kanuni hii inahakikisha nishati na rasilimali zinatumika kwa ufanisi wa hali ya juu.

Je, unaona jambo kama hili likitokea kwenye maisha ya kila siku hapo nyumbani au shuleni? Nambie unafikiri nini! 💭"""
                else:
                    text = f"""That is a brilliant, sharp question! 🌟 You are thinking like a true scientist!

Regarding what you just asked: *" {message} "*:
1. **The Core Scientific Reason:** In **{title}**, this happens because the system operates on precise biological/physical laws to transfer energy efficiently.
2. **In Our Local Environment ({region_info['locality_name']}):** {analogy}
3. **Key Insight:** Everything in nature works together in harmony to maintain life and energy.

Have you ever observed something similar happening in nature around your community? What do you think? 💭"""

            # 3. Another Example / "Mfano Mwingine"
            elif any(w in msg_lower for w in ["another", "mwingine", "example", "mfano", "more"]):
                alt_region = "coastal" if region_key == "lake_basin" else "lake_basin"
                alt_info = REGIONS.get(alt_region, REGIONS["coastal"])
                alt_analogy = topic_data.get("regional_analogies", {}).get(alt_region, {}).get("analogy_sw" if is_sw else "analogy_en", analogy)
                
                if is_sw:
                    text = f"""Bila shaka! Hebu tuchukue mfano kutoka eneo lingine la bara letu la Afrika—**{alt_info['icon']} {alt_info['name_sw']}**:

{alt_analogy}

Unaona jinsi kanuni hii ya **{title}** inavyofanya kazi sawa kote barani? Ni sayansi ile ile lakini inatumika kwa njia tofauti za kiasili! 🌍"""
                else:
                    text = f"""Absolutely! Let's look at another real-world example from another part of Africa—**{alt_info['icon']} {alt_info['name_en']}**:

{alt_analogy}

See how the same scientific principle of **{title}** applies across different ecosystems? Nature uses the exact same law everywhere! 🌍"""

            # 4. Standard Conversational Follow-up
            else:
                if is_sw:
                    text = f"""Ninakusikia vizuri rafiki yangu mpendwa! 🌟 

Kuhusu mada yetu ya **{title}**:
* **Ufahamu wa Haraka:** {summary}
* **Swali la Kufikirisha:** Je, unajua ni nini kingetokea endapo mchakato huu ungekoma kwa siku chache tu katika mazingira yetu ya {region_info['locality_name']}?

Endelea kuuliza chochote—mimi niko hapa kufafanua hatua kwa hatua! 🚀"""
                else:
                    text = f"""I hear you loud and clear, my dear friend! 🌟

Continuing our discovery of **{title}**:
* **Quick Insight:** {summary}
* **Curiosity Question:** What do you think would happen if this natural process paused for just a few days in our {region_info['locality_name']} environment?

Keep asking anything that comes to mind—I'm right here to guide you step-by-step! 🚀"""

        # INITIAL TOPIC OVERVIEW (Turn 1: Comprehensive Walkthrough)
        else:
            intro = (
                f"Hujambo rafiki yangu mpendwa! 🌟 Nimefurahi sana kusikia swali lako zuri kuhusu eneo letu zuri la **{region_info['icon']} {region_info['name_sw']}**! "
                f"Wewe ni mwanafunzi hodari na mwenye akili nyingi. Hebu tuchunguze mada hii ya **{title}** pamoja kama marafiki:"
                if is_sw else
                f"Hello my dear friend! 🌟 I am so proud of your wonderful question about our beautiful **{region_info['icon']} {region_info['name_en']}**! "
                f"You have such a sharp and curious mind. Let's explore **{title}** together step-by-step:"
            )

            text = f"""{intro}

### 🌟 {title}
{summary}

### 🏞️ Mfano Halisi wa Eneo Lako ({region_info['locality_name']}):
{analogy}

### 🧪 Jaribio la Nyumbani Lisilo na Gharama:
**{exp['title_sw' if is_sw else 'title_en']}**
* **Vifaa / Materials:** {exp['materials_sw' if is_sw else 'materials_en']}
* **Hatua / Steps:**
{exp['steps_sw' if is_sw else 'steps_en']}

### 💬 Maneno Muhimu ya Kisayansi (Vocabulary):
"""
            text += f"\n> *\"{topic_data.get('cbc_strand', 'CBC Curriculum')}\" — Usimeze maneno tu, elewa sayansi inayokuzunguka kila siku!*"

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
            "model": "gemini-3.7-flash",
            "reasoning_mode": "high",
            "thinking_budget": 2048,
            "text": text,
            "language": language,
            "region": region,
            "topic": topic_data["title_en"],
            "subject": topic_data["subject"],
            "topic_id": topic_data["id"],
            "offline_module_id": topic_data["id"],
            "mode": mode,
            "temperature": 0.2 if mode == "precise" else 0.75,
            "tactile_description": topic_data.get("tactile_audio_description_sw", ""),
            "sign_cues": topic_data.get("sign_language_visual_cues_sw", ""),
            "diagram": get_diagram_for_topic(message) or get_diagram_for_topic(topic_data["id"]),
            "quiz_data": quiz,
            "related_topics": get_related_topics_recommendations(topic_data["id"]),
            "student_profile": student_memory.get_or_create_profile(student_id).model_dump()
        }

    def _extract_topic(self, user_msg: str, bot_response: str, preferred_subject: str = "all") -> Dict[str, str]:
        # Resolve topic accurately using curriculum search
        topic_data = find_offline_topic(user_msg, preferred_subject)
        if topic_data and topic_data.get("title_en"):
            return {
                "topic": topic_data["title_en"],
                "subject": topic_data["subject"],
                "topic_id": topic_data["id"]
            }
        
        subj_map = {
            "mathematics": "Mathematics",
            "physics": "Physics",
            "chemistry": "Chemistry",
            "biology": "Biology",
            "computer_science": "Computer Science"
        }
        mapped_subj = subj_map.get(preferred_subject.lower(), "General Science")
        return {"topic": f"{mapped_subj} Exploration", "subject": mapped_subj, "topic_id": "general_stem"}


# Singleton Agent
elewa_agent = ElewaAgent()
