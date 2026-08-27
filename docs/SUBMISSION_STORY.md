# ElewaSTEM — Devpost Submission Story

## Project Name
**ElewaSTEM (Mwalimu STEM)** — *Demystifying STEM for Every African Child in Their Own Language*

## Tagline
An adaptive, offline-first multilingual AI STEM tutor that explains complex science and math to African children through native languages (Kiswahili, English, Sheng), culturally grounded analogies, interactive quizzes, and persistent student memory.

---

## 🌟 Inspiration
In many African schools, children face a silent but immense hurdle in STEM education: **The Double Cognitive Barrier**. A 10-year-old student is forced to decode two unfamiliar things simultaneously: a difficult scientific concept (e.g., electricity, photosynthesis, fractions) AND a foreign academic language (formal textbook English). 

When a child asks *"Mwalimu, umeme unafanyaje kazi?"* (Teacher, how does electricity work?), they don't need a dry English definition about "potential differences and Coulombs." They need an intuitive mental model: *"Fikiria battery kama tenki la maji lililo juu ya nyumba, na waya kama mfereji wa maji..."* (Think of a battery like a water tank on top of the house, and wires like water pipes).

We built **ElewaSTEM** to bridge this gap: an empathetic, Socratic AI tutor that meets African children where they are, speaks their language, uses relatable local analogies, and works seamlessly even in areas with zero or unstable internet connectivity.

---

## 🚀 What ElewaSTEM Does

1. **Fluid Multilingual Code-Switching (English ⇄ Kiswahili ⇄ Sheng)**:
   - Students can ask questions in their mother tongue, formal Swahili, English, or colloquial Sheng.
   - ElewaSTEM provides the conceptual explanation in conversational Swahili while highlighting the formal English scientific terms required to pass national examinations.

2. **Hyper-Localized First-Principles Analogies**:
   - Grounds abstract concepts in everyday African realities: solar crop drying for heat transfer, bicycle dynamos for electromagnetism, village homesteads for cellular biology, and sharing chapatis for fractions.

3. **Socratic "Usimeze, Elewa!" Pedagogy**:
   - Rather than just giving the direct answer to homework, the agent guides the child step-by-step with intuitive questions, encouraging feedback, and safe at-home mini-experiments using everyday household items (bottles, salt, water, sunlight).

4. **Persistent Student Mastery Memory & Badges**:
   - Maintains a dynamic mastery graph across Physics, Biology, Chemistry, and Math.
   - Remembers what topics the student understands, tracks misconceptions, and awards motivational badges (*"Mvumbuzi Chipukizi"*, *"Bingwa wa Sayansi"*).

5. **Offline-First & Low-Connectivity PWA Architecture**:
   - Built as a lightweight Progressive Web App (<100KB) with a local **Offline Knowledge Vault**.
   - Children can browse lessons, conduct experiments, and take quizzes with **0 KB data connection**.
   - Features an opportunistic background sync queue that uploads questions when intermittent 2G bursts are detected.
   - Includes zero-bandwidth browser speech synthesis (TTS) and voice recognition (STT).
   - SMS/USSD gateway webhook ready for basic 2G feature phones.

---

## 🛠️ How We Built It

* **AI & Agent Core**: 
  - Google Gemini 2.5 / 3.5 Flash via the official `google-genai` Python SDK.
  - Specialized system prompts engineered with pedagogical scaffolding and bilingual scientific grounding.
* **Backend Architecture**:
  - FastAPI asynchronous server with REST endpoints for multi-turn chat, student profile management, offline pack distribution, and SMS webhook.
  - Persistent JSON/Firestore-ready Memory Bank tracking student mastery levels and learning styles.
* **Frontend & Edge Client**:
  - Progressive Web App (PWA) with Service Worker caching and IndexedDB local storage.
  - Web Speech API for real-time voice input (STT) and native African accent speech synthesis (TTS).
  - Clean, kid-friendly responsive UI built with Tailwind CSS and custom animations.

---

## 🧗 Challenges We Ran Into

1. **Balancing Vernacular Intuition with Academic Terminology**:
   - If an agent only uses colloquial terms, the child won't learn the vocabulary needed for standardized English exams. We solved this by building the **Dual-Language Vocabulary Bridge**, which always pairs the Swahili concept with its English exam counterpart (e.g. *Usanisinuru ➔ Photosynthesis*).
2. **True Offline Resilience**:
   - Ensuring that an AI-powered agent doesn't completely fail when the student is disconnected in a rural village. We architected a dual-engine model: Gemini in the cloud when connected, and a local indexed knowledge vault at the edge when offline.

---

## 🏆 Accomplishments We're Proud Of

* Creating an agent that African children genuinely feel comfortable talking to—free of judgment, full of cultural warmth, and deeply encouraging.
* Zero-bandwidth voice and offline lesson capabilities that make generative AI accessible beyond high-speed urban fibers.
* Seamless real-time code-switching between English, Swahili, and Sheng without losing scientific accuracy.

---

## 📚 What We Learned

True educational equity in AI isn't just about translating English words into another language—it is about **cultural translation of mental models**. Grounding science in a child's lived environment transforms STEM from an intimidating, foreign subject into a joyful, familiar journey of discovery.

---

## 🔮 What's Next for ElewaSTEM

* **Language Expansion**: Scaling beyond Swahili and Sheng to Yoruba, Hausa, Igbo, Amharic, Oromo, and Zulu.
* **Direct SMS / USSD Deployment**: Partnering with Africa's Talking to launch ElewaSTEM on toll-free SMS numbers across Kenya, Tanzania, Uganda, and Nigeria.
* **Integration with National Curriculums**: Partnering with KICD (Kenya), NECTA (Tanzania), and UNEB (Uganda) to map every lesson directly to official primary and junior secondary competency-based strands.
