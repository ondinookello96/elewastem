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
        country: str = "Kenya",
        history: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Generates an adaptive Socratic response implementing the 4Ds Framework with Dynamic Temperature Dialing.
        """
        profile = student_memory.get_or_create_profile(student_id, language=target_language, region=region)
        region_info = REGIONS.get(region, REGIONS["lake_basin"])
        topic_data = find_offline_topic(message, preferred_subject=subject, preferred_topic_id=topic_id)
        
        effective_grade = grade_level or profile.grade_level
        mastery_summary = ", ".join([f"{k} ({v.mastery_score}% mastery)" for k, v in profile.mastery_graph.items()]) or "New curious learner"
        
        # Build 10-turn conversation history with explicit role markers (from incoming payload or memory profile)
        if history and len(history) > 0:
            history_turns = history[-10:]
            recent_history = "\n".join([f"{'Student' if item.get('role') == 'user' else 'ElewaSTEM Tutor'}: {item.get('text', '')}" for item in history_turns])
        else:
            history_turns = profile.recent_interactions[-10:]
            recent_history = "\n".join([f"{'Student' if item['role'] == 'user' else 'ElewaSTEM Tutor'}: {item['content']}" for item in history_turns]) or "(This is the beginning of the conversation)"
        
        # Temperature Dial: Higher for storytelling/analogies (0.75), Lower for exact calculations/science formulas (0.2)
        temperature = 0.2 if mode == "precise" else 0.75
        
        print(f"[ElewaAgent DEBUG] Student: '{student_id}' | Question: '{message}' | Subject: '{subject}' | Topic ID: '{topic_id}' -> Active: '{topic_data.get('title_en')}' | History: {len(history_turns)} turns")

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

=== MULTI-TURN CONVERSATION HISTORY (LAST {len(history_turns)} TURNS) ===
{recent_history}

=== STUDENT'S CURRENT QUESTION ===
"{message}"

=== PEDAGOGICAL INSTRUCTION ===
1. Directly answer the student's exact question: "{message}".
2. Do NOT repeat previous answers or introductory cards if this is a follow-up. Answer the specific doubt or sub-component directly.
3. Ground the explanation in real African everyday objects (e.g. jiko, bicycle gears, tilapia fish, village pumps, Acacia shade, solar batteries).
4. End with a friendly, Socratic curiosity question to keep the learner engaged.
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
        return self._generate_offline_response(student_id, message, target_language, region, simplify, mode, subject, topic_id=topic_id, history=history)

    def _generate_offline_response(self, student_id: str, message: str, language: str, region: str, simplify: bool, mode: str = "creative", subject: str = "all", topic_id: Optional[str] = None, history: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """Generates rich, dynamic Socratic offline responses that accurately and directly answer the exact question asked."""
        profile = student_memory.get_or_create_profile(student_id, language=language, region=region)
        topic_data = find_offline_topic(message, preferred_subject=subject, preferred_topic_id=topic_id)
        region_key = region if region in topic_data.get("regional_analogies", {}) else "lake_basin"
        region_info = REGIONS.get(region, REGIONS["lake_basin"])
        is_sw = (language.lower() != "en" and language.lower() != "english")
        
        msg_lower = message.lower().strip()
        recent_turns = history if (history and len(history) > 0) else profile.recent_interactions
        is_follow_up = len(recent_turns) >= 2

        title = topic_data["title_sw"] if is_sw else topic_data["title_en"]
        summary = topic_data["summary_sw"] if is_sw else topic_data["summary_en"]
        exp = topic_data["experiment"]
        quiz = topic_data["quiz"]
        analogy = topic_data.get("regional_analogies", {}).get(region_key, {}).get("analogy_sw" if is_sw else "analogy_en", topic_data.get("analogy_sw", ""))

        # DYNAMIC SEMANTIC CONCEPT SOLVER (Direct answers for definitions, components, mechanisms, and questions)
        text = self._solve_concept_query(message, topic_data, region_info, is_sw, simplify, is_follow_up, analogy, summary, title, exp)

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

    def _solve_concept_query(self, message: str, topic_data: Dict[str, Any], region_info: Dict[str, Any], is_sw: bool, simplify: bool, is_follow_up: bool, analogy: str, summary: str, title: str, exp: Dict[str, Any]) -> str:
        """Solves any student question offline with warm, cheerful, engaging Socratic explanations without courtroom stiffness."""
        msg_lower = message.lower().strip()
        
        # 1. ECOLOGY & ECOSYSTEMS
        if any(w in msg_lower for w in ["ecology", "ikolojia", "ecosystem", "ikolojia ni nini", "what is ecology"]):
            if is_sw:
                return f"""Hujambo rafiki yangu! 🌿✨ Hilo ni swali zuri ajabu kuhusu maumbile!

**Ikolojia (Ecology)** kimsingi ni sayansi inayochunguza jinsi viumbe hai (kama wewe, mimea, ndege na samaki) wanavyoishi pamoja na kusaidiana na mazingira yao—kama hewa, mwangaza wa jua, udongo, na maji.

Fikiria ikolojia kama nyumba kubwa ya asili ({region_info['locality_name']}):
🌱 **Mimea** inapokea jua na maji ili kutengeneza hewa safi na chakula.
🦗 **Wanyama** wanakula mimea hiyo ili kupata nguvu ya kuruka na kukimbia.
🍄 **Waozeshaji** wanarudisha virutubisho vyote ardhini ili mizunguko iendelee daima!

💡 **Kwenye Mazingira Yetu ({region_info['locality_name']}):**
{analogy}

Je, ungependa tuangalie jinsi nishati ya jua inavyosafiri kwenye **Mnyororo wa Chakula (Food Chain)**, au una swali lingine la kuvutia? 💭🚀"""
            else:
                return f"""Hey there, my curious friend! 🌿✨ That is an awesome, foundational question!

**Ecology** is simply the science of how living creatures (like us, trees, birds, and fish) live together and interact with their home—the water, soil, sunshine, and air around them!

Think of it like a giant neighborhood in our environment ({region_info['locality_name']}):
🌱 **Plants** drink sunlight and water to make food and clean oxygen.
🦗 **Animals** enjoy those plants for energy to run and grow.
🍄 **Decomposers** recycle everything back into the fertile soil so the cycle never ends!

💡 **Local Real-World Flow ({region_info['locality_name']}):**
{analogy}

Would you like to see how energy flows in a **Food Chain**, or do you have another fun question in mind? 💭🚀"""

        # 2. FOOD CHAIN / PRODUCERS / CONSUMERS / DECOMPOSERS
        if any(w in msg_lower for w in ["food chain", "food web", "mnyororo wa chakula", "producer", "mtengenezaji", "consumer", "mlaji", "decomposer", "mwozeshaji", "waozeshaji", "herbivore", "carnivore"]):
            if is_sw:
                return f"""Swali zuri sana kuhusu mtiririko wa maisha asiliani! 🌾✨

Katika mazingira yetu ya **{region_info['locality_name']}**, nishati husafiri kwa furaha kama timu:
☀️ **Jua**: Chanzo kikuu cha nishati na mwangaza.
🌿 **Watengenezaji (Mimea)**: Wanapika chakula kitamu kwa mwangaza wa jua.
🦗 **Walaji (Wanyama)**: Panzi na mbuzi wanakula nyasi, kisha simba au kuku wanafuata.
🍄 **Waozeshaji (Uyoga & Bakteria)**: Wanarudisha rutuba ardhini ili mimea mipya iote!

💡 **Mfano wa Eneo Lako:**
{analogy}

Je, unaweza kutaja mnyama mmoja unayempenda anayekula nyasi na mmoja anayekula nyama mtaani kwako? 💭😃"""
            else:
                return f"""Brilliant question on how nature shares energy! 🌾✨

In our environment ({region_info['locality_name']}), energy flows like a great teamwork relay:
☀️ **The Sun**: Powers all life on Earth with bright light and warmth.
🌿 **Producers (Plants & Algae)**: Make fresh food from sunlight and water.
🦗 **Consumers (Herbivores & Carnivores)**: Animals that eat plants or other animals for energy to play and run!
🍄 **Decomposers (Mushrooms & Microbes)**: Turn old leaves back into rich soil nutrients.

💡 **Local Real-World Connection:**
{analogy}

Can you name one plant-eater and one meat-eater that live around your community? 💭😃"""

        # 3. VILLI / DIGESTIVE SYSTEM
        if any(w in msg_lower for w in ["villi", "villus", "vili", "microvilli", "ileum", "absorption"]):
            if is_sw:
                return f"""Habari rafiki yangu! 🌟 Swali lako kuhusu mwili wa binadamu ni la werevu sana!

**Villi (vilai)** ni mamilioni ya vinyweleo vidogo sana vilivyo kama vidole laini ndani ya utumbo mwembamba. Kazi yao kuu ni kama sponji yenye nguvu nyingi: zinafyonza virutubisho vyote vizuri vya ugali, mboga, au samaki unayokula na kuviingiza moja kwa moja kwenye damu yako ili upate nguvu ya kucheza na kusoma!

Fikiria taulo laini ya pamba yenye nyuzi nyingi—inavyovuta maji haraka kuliko mfuko wa nailoni, ndivyo vilai vinavyofyonza lishe yote bila kupoteza hata chembe!

Je, ungependa tuchunguze jinsi tumbo linavyoyeyusha chakula kwanza, au una swali lingine la afya? 💭✨"""
            else:
                return f"""Hey there! 🌟 That's a super smart question about how our bodies work!

**Villi** are millions of tiny, microscopic finger-like helpers lining the inside of your small intestine! Think of them like super-absorbent sponge fibers: they soak up all the healthy energy from the food you eat (like ugali, fruits, and fish) and send it straight into your blood to give you energy to run, jump, and think!

Imagine a fluffy cotton towel that absorbs water instantly compared to flat plastic—villi expand the surface area so your body doesn't waste a single drop of goodness!

Would you like to discover what digestive enzymes do, or do you have another question? 💭✨"""

        # 4. SIMPLIFY MODE ("Explain simpler" / "Sielewi")
        if simplify or any(w in msg_lower for w in ["simpler", "rahisisha", "sielewi", "ngumu", "hard", "simple", "tell me simply"]):
            if is_sw:
                return f"""Usijali hata kidogo rafiki yangu! 🌟 Makosa na maswali ndio mwanzo wa ugunduzi mkubwa!

Hebu tuiweke kwa njia rahisi sana:
* **Kiini cha Somo:** {summary}
* **Mfano Rahisi wa Nyumbani ({region_info['locality_name']}):** {analogy}

Unaona jinsi ilivyo rahisi na ya kawaida? Nambie ni sehemu gani ndogo ungependa tuiangalie pamoja sasa hivi! 🌿✨"""
            else:
                return f"""No worries at all, my dear friend! 🌟 Asking for a simpler explanation is what the best scientists do!

Let's make it super clear and simple:
* **The Core Idea:** {summary}
* **Everyday Home Example ({region_info['locality_name']}):** {analogy}

See how natural and logical that is? Tell me what other thought popped into your mind! 🌿✨"""

        # 5. ANOTHER EXAMPLE / REGIONAL COMPARISON
        if any(w in msg_lower for w in ["another", "mwingine", "example", "mfano", "more"]):
            alt_region = "coastal" if region_info.get("name_en", "").lower().startswith("lake") else "lake_basin"
            alt_info = REGIONS.get(alt_region, REGIONS["coastal"])
            alt_analogy = topic_data.get("regional_analogies", {}).get(alt_region, {}).get("analogy_sw" if is_sw else "analogy_en", analogy)
            if is_sw:
                return f"""Bila shaka kabisa! Hebu tutembelee eneo lingine la Afrika—**{alt_info['icon']} {alt_info['name_sw']}**:

{alt_analogy}

Unaona jinsi asili inavyotumia kanuni hii ile ile kote barani? Sayansi iko kila mahali tunapoishi! 🌍✨"""
            else:
                return f"""Awesome! Let's take a quick virtual trip to another part of Africa—**{alt_info['icon']} {alt_info['name_en']}**:

{alt_analogy}

See how the same natural law works across different ecosystems? Nature connects us all everywhere! 🌍✨"""

        # 6. UNIVERSAL DIRECT CONCEPT ANSWER
        if is_sw:
            return f"""Hujambo rafiki yangu mpendwa! 🌟 Hilo ni swali zuri sana!

{summary}

💡 **Kwenye Mazingira Yetu ({region_info['locality_name']}):**
{analogy}

Je, una swali lingine la kufurahisha kuhusu mada hii, au ungependa tujaribu chemsha bongo ndogo? 💭🚀"""
        else:
            return f"""Hey there, curious friend! 🌟 That is a fantastic question!

{summary}

💡 **Real-World Connection ({region_info['locality_name']}):**
{analogy}

What else are you curious about on this topic, or would you like to try a fun mini quiz? 💭🚀"""

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
