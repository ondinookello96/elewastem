# ElewaSTEM — Devpost Submission Story

## Project Name
**ElewaSTEM (Mwalimu STEM)** — *Demystifying STEM for Every African Child, Parent, Teacher & Community in Native Voice & Local Context*

## Tagline
A voice-first, offline-capable AI STEM learning ecosystem connecting learners, parents (SMS digests), teachers (CBC lesson plans), and community mentors through native African languages and localized geo-context.

---

## 🌟 Inspiration
In many African communities, children and educators face systemic hurdles in STEM education:
1. **The Literacy & Typing Barrier**: Early-grade and primary school learners often struggle to type on touchscreens or read dense paragraphs of technical English text.
2. **The Parent-Teacher Disconnect**: Parents in rural and peri-urban areas (many without STEM backgrounds or smartphones) struggle to follow what their children are learning or support them at home.
3. **The Teacher Workload & Resource Gap**: Teachers lack localized teaching aids aligned with modern Competency-Based Curriculums (CBC in Kenya, NECTA in Tanzania, UNEB in Uganda) that connect textbook theory to the school's immediate environment.
4. **The Context & Connectivity Barrier**: Traditional textbooks reference foreign contexts with zero internet access in classrooms.

When an 8-year-old in Kisumu wonders why fish can breathe under Lake Victoria, they need more than a dry English definition. They need a **complete educational ecosystem**:
* **The Child** speaks into their phone in Swahili and receives an audio explanation grounded in *Ngege (Tilapia)* gills and Lake Victoria oxygen.
* **The Parent** receives a simple Swahili SMS digest celebrating their child's progress with a fun 2-minute kitchen science challenge.
* **The Teacher** gets an instant CBC-aligned lesson plan with localized teaching aids and diagnostic quizzes using free local materials.
* **The Community Mentor** gets zero-cost group STEM club projects for village youth centers.

We built **ElewaSTEM** to unite all these stakeholders into one holistic, privacy-respecting (Kenya DPA 2019 compliant) platform that works with **0 KB data connection**.

---

## 🚀 The Multi-Stakeholder Ecosystem

### 1. 🎓 **For Learners (Mwanafunzi)**:
* **Voice-First Accessibility (STT & TTS)**: Hands-free speech recognition in Swahili and English with automatic read-aloud for children with reading or typing challenges.
* **Hyper-Local African Geo-Context**: Adapts all science analogies to the learner's immediate eco-zone (**Kisumu & Lake Victoria**, **Mombasa Coastal**, **Highland Farms**, **Turkana Arid Lands**, **Urban Centers**).
* **Offline Knowledge Vault**: Browse lessons, conduct experiments, and take quizzes with **0 KB data connection**.
* **Child Data Protection (DPA 2019)**: 100% on-device edge calculation with explicit opt-in consent and zero cloud profiling.

### 2. 👨‍👩‍👧‍👦 **For Parents & Guardians (Wazazi na Walezi)**:
* **Weekly Progress Digest**: Plain-language summaries of concepts explored and badges won.
* **1-Click SMS & WhatsApp Card**: Formats a clean progress update for parents on basic 2G feature phones.
* **At-Home Kitchen / Farm Science Challenges**: Step-by-step guidance on how non-STEM parents can conduct fun weekend experiments with their children using household items (bottles, leaves, salt).

### 3. 👩‍🏫 **For Teachers & Educators (Walimu)**:
* **CBC / NECTA Lesson Plan Generator**: Automatically generates lesson plans mapped to national curriculum strands (e.g. *Grade 5/6 Science: Living Things & Life Processes*).
* **Localized Teaching Aids**: Provides relatable cultural metaphors tailored to the school's local ecology (e.g. using fishing lanterns for circuits in Kisumu, or hydro dams in the Highlands).
* **Diagnostic Misconception Quizzes**: Ready-to-use in-class formative assessment questions with full answer keys.

### 4. 🤝 **For Community STEM Mentors & Village Centers (Vilabu vya Sayansi)**:
* **Zero-Budget STEM Club Guides**: Practical group projects using local materials (e.g., Clean Water Charcoal Filter, Cardboard Solar Cooker).

---

## 🛠️ How We Built It

* **AI & Multi-Agent Core**: 
  - Google Gemini 2.5 / 3.5 Flash via the official `google-genai` Python SDK.
  - Specialized system prompts engineered with pedagogical scaffolding, regional eco-zone grounding, and bilingual scientific vocabulary pairing.
* **Voice & Multimodal UX**:
  - Web Speech API for real-time speech recognition (STT) and native multilingual speech synthesis (TTS).
  - Audio waveform visualizers and auto-speak accessibility pipeline.
* **Backend Architecture**:
  - FastAPI asynchronous server with REST endpoints for multi-turn chat, stakeholder lesson plans, parent digests, offline pack distribution, and SMS webhook.
  - Persistent JSON/Firestore-ready Memory Bank tracking student mastery levels and geo-coordinates.
* **Frontend & Edge Client**:
  - Progressive Web App (PWA) with Service Worker caching and IndexedDB local storage.
  - Offline GPS Coordinate-to-Biome mapping algorithm with Kenya DPA 2019 consent gatekeeper.

---

## 🧗 Challenges We Ran Into

1. **Uniting Diverse Stakeholders with Differing Tech Access**:
   - Students have smartphones or offline PWAs, parents may only have basic 2G SMS feature phones, and teachers need structured curriculum documentation. We engineered unified data bridges: generating interactive PWA lessons for students, printable CBC lesson plans for teachers, and plain-text SMS cards for parents.
2. **Accessible Voice and Offline GPS**:
   - Standard APIs rely on continuous internet connectivity. We engineered client-side edge mathematical bounding boxes and on-device Web Speech integration so voice and regional adaptation work 100% disconnected.

---

## 🏆 Accomplishments We're Proud Of

* A complete, multi-stakeholder platform that bridges the gap between students, parents, teachers, and communities.
* Giving non-typing and low-literacy children equal access to AI tutoring through native voice interaction.
* Zero-bandwidth voice, offline GPS detection, and offline lesson capabilities that make generative AI accessible beyond high-speed urban fibers.

---

## 🔮 What's Next for ElewaSTEM

* **Language Expansion**: Scaling beyond Swahili and Sheng to Yoruba, Hausa, Igbo, Amharic, Oromo, and Zulu.
* **Direct SMS / USSD & IVR (Interactive Voice Response) Deployment**: Partnering with Africa's Talking to launch ElewaSTEM on toll-free phone calls and SMS across Kenya, Tanzania, Uganda, and Nigeria.
* **Official Curriculum Partnership**: Collaborating with KICD (Kenya), NECTA (Tanzania), and UNEB (Uganda) to certify ElewaSTEM lesson plans across all national primary school clusters.
