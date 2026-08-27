# ElewaSTEM — Devpost Submission Story

## Project Name
**ElewaSTEM (Mwalimu STEM)** — *Demystifying STEM for Every African Child in Their Own Language, Voice & Local Ecosystem*

## Tagline
An adaptive, voice-first and offline-capable AI STEM tutor that explains science and math to African children through native speech, local geo-context (GPS-adaptive), and zero-barrier audio accessibility.

---

## 🌟 Inspiration
In many African communities, children face a quadruple hurdle in STEM education:
1. **The Literacy & Typing Barrier**: Early-grade and primary school learners often struggle to type on touchscreens or read dense paragraphs of technical text.
2. **The Language Barrier**: Forced to decode hard science through unfamiliar, foreign academic English.
3. **The Context Barrier**: Textbook examples reference foreign contexts (subways, snow, baseball) rather than familiar local realities (maize farms, coconut palms, solar boreholes, Lake Victoria fisheries).
4. **The Connectivity Barrier**: Rural and peri-urban schools frequently experience zero or intermittent internet access.

When an 8-year-old child in Kisumu wonders why fish can breathe under Lake Victoria, they shouldn't need a keyboard or read complex textbooks. They should simply **speak into their phone in Swahili** (*"Mbona samaki wa Ngege hawazami ziwani?"*), and have a friendly tutor **speak back to them aloud** with local analogies of Tilapia gills, water hyacinth (*Akech*), and clean lake oxygen.

We built **ElewaSTEM** to bridge this gap: a voice-first, empathetic, Socratic AI tutor that speaks the child's mother tongue, adapts to their local geography using offline GPS, complies with the **Kenya Data Protection Act 2019**, and works with **0 KB data connection**.

---

## 🚀 What ElewaSTEM Does

1. **Voice Recognition (STT) & Speech Synthesis (TTS) for High Accessibility**:
   - **Voice-First Interaction**: Children who cannot type or read complex text can simply press the large microphone button and speak in Swahili, English, or Sheng.
   - **Auto-Read Aloud**: Automatically reads out scientific explanations, glossaries, and quiz questions in warm, natural speech.
   - **Audio Feedback**: Spoken celebrations and encouragement on quizzes (*"Hongera sana! Uko sahihi!"*).
   - **Zero-Data Offline Audio**: Operates on native on-device Web Speech engines with 0 KB internet bandwidth.

2. **Hyper-Local Geo-Adaptive Context & Offline GPS**:
   - Automatically detects or allows selecting the student's African eco-region (**🌊 Coastal**, **⛰️ Highlands**, **🏞️ Lake Victoria Basin / Kisumu**, **☀️ Arid & Pastoralist**, **🏙️ Urban**).
   - Utilizes device hardware GPS (which functions **100% offline without cellular data**) to map coordinates directly to regional biomes.
   - Dynamically adapts all science analogies, experiments, and examples to the learner's immediate physical surroundings (e.g. *Samaki Ngege / Tilapia* and *Magugu Maji / Akech* in Kisumu; *Minazi* and *Mikoko* at the Coast).

3. **Child Data Protection & Consent (Kenya Data Protection Act 2019 Compliant)**:
   - Full compliance with **Section 29 of the Kenya DPA 2019** (Processing Personal Data of Children).
   - GPS is strictly **opt-in with clear consent**, processed **100% on-device**, with zero cloud profiling or tracking.

4. **Fluid Multilingual Code-Switching (English ⇄ Kiswahili ⇄ Sheng)**:
   - Students can ask questions in their mother tongue, formal Swahili, English, or colloquial Sheng.
   - Pairs vernacular intuition with the formal English scientific terminology required for national exams (*Yavuyavu ➔ Gills*, *Usanisinuru ➔ Photosynthesis*).

5. **Socratic "Usimeze, Elewa!" Pedagogy**:
   - Guided step-by-step discovery with safe, at-home mini-experiments using everyday household items.

6. **Persistent Student Mastery Memory & Badges**:
   - Maintains a dynamic mastery graph across Physics, Biology, Chemistry, and Math.
   - Remembers what topics the student understands, tracks misconceptions, and awards motivational badges (*"Mvumbuzi Chipukizi"*, *"Bingwa wa Sayansi"*).

---

## 🛠️ How We Built It

* **AI & Agent Core**: 
  - Google Gemini 2.5 / 3.5 Flash via the official `google-genai` Python SDK.
  - Specialized system prompts engineered with pedagogical scaffolding, regional eco-zone grounding, and bilingual scientific vocabulary pairing.
* **Voice & Multimodal UX**:
  - Web Speech API for real-time speech recognition (STT) and native multilingual speech synthesis (TTS).
  - Audio waveform visualizers and auto-speak accessibility pipeline.
* **Backend Architecture**:
  - FastAPI asynchronous server with REST endpoints for multi-turn chat, geo-region listing, student profile management, offline pack distribution, and SMS webhook.
  - Persistent JSON/Firestore-ready Memory Bank tracking student mastery levels and geo-coordinates.
* **Frontend & Edge Client**:
  - Progressive Web App (PWA) with Service Worker caching and IndexedDB local storage.
  - Offline GPS Coordinate-to-Biome mapping algorithm with Kenya DPA 2019 consent gatekeeper.

---

## 🧗 Challenges We Ran Into

1. **Accessibility for Young Learners with Low Reading/Typing Skills**:
   - Young children in primary school often get frustrated by touchscreen keyboards. We engineered a hands-free Voice Mode where the app listens to speech, displays a live waveform, and automatically speaks the resulting science explanation aloud.
2. **Making Voice and GPS Work 100% Offline**:
   - Cloud speech and reverse-geocoding APIs fail when internet drops. We leveraged on-device Web Speech APIs and local mathematical bounding-box algorithms so voice and location adaptation function with 0 KB connection.

---

## 🏆 Accomplishments We're Proud Of

* Creating an agent that African children genuinely feel comfortable talking to—free of judgment, culturally grounded in their home region, and deeply encouraging.
* Zero-bandwidth voice, offline GPS detection, and offline lesson capabilities that make generative AI accessible beyond high-speed urban fibers.
* Giving non-typing and low-literacy children equal access to AI tutoring through native voice interaction.

---

## 🔮 What's Next for ElewaSTEM

* **Language Expansion**: Scaling beyond Swahili and Sheng to Yoruba, Hausa, Igbo, Amharic, Oromo, and Zulu.
* **Direct SMS / USSD & IVR (Interactive Voice Response) Deployment**: Partnering with Africa's Talking to launch ElewaSTEM on toll-free phone calls and SMS across Kenya, Tanzania, Uganda, and Nigeria.
* **National Curriculum Alignment**: Collaborating with KICD (Kenya), NECTA (Tanzania), and UNEB (Uganda) to align every topic directly to competency-based curriculum (CBC) strands.
