# ElewaSTEM — Devpost Submission Story

## Project Name
**ElewaSTEM (Mwalimu STEM)** — *Demystifying STEM for Every African Child in Their Own Language & Local Ecosystem*

## Tagline
An adaptive, offline-first multilingual AI STEM tutor that explains complex science and math to African children through native languages (Kiswahili, English, Sheng), hyper-local geo-context (GPS-adaptive), interactive quizzes, and persistent student memory.

---

## 🌟 Inspiration
In many African communities, children face a triple hurdle in STEM education:
1. **The Language Barrier**: Forced to decode hard science through unfamiliar, foreign academic English.
2. **The Context Barrier**: Textbook examples reference foreign contexts (subways, snow, baseball) rather than familiar local realities (maize farms, coconut palms, solar boreholes, Lake Victoria fisheries).
3. **The Connectivity Barrier**: Rural and peri-urban schools frequently experience zero or intermittent internet access.

When a child asks *"Mwalimu, umeme unafanyaje kazi?"* (Teacher, how does electricity work?), they don't need a dry English definition about "potential differences and Coulombs." They need an intuitive mental model grounded in their own environment:
* In the **Highlands**: *"Fikiria jinsi mtambo wa maji wa Masinga unavyotumia nguvu ya maji yanayoanguka milimani kusukuma umeme..."*
* In **Arid pastoralist lands**: *"Fikiria jinsi paneli ya jua (Solar PV) kule Garissa inavyovuta mwangaza wa jua kusukuma pampu ya kisima cha maji..."*
* At the **Coast**: *"Kama vile pampu inavyosukuma maji ya bahari kwenye mashamba ya kukausha chumvi..."*

We built **ElewaSTEM** to bridge this gap: an empathetic, Socratic AI tutor that speaks the child's mother tongue, adapts to their local geography using offline GPS, and works with **0 KB data connection**.

---

## 🚀 What ElewaSTEM Does

1. **Hyper-Local Geo-Adaptive Context & Offline GPS**:
   - Automatically detects or allows selecting the student's African eco-region (**🌊 Coastal**, **⛰️ Highlands**, **🏞️ Lake Victoria Basin**, **☀️ Arid & Pastoralist**, **🏙️ Urban**).
   - Utilizes device hardware GPS (which functions **100% offline without cellular data**) to map coordinates directly to regional biomes.
   - Dynamically adapts all science analogies, experiments, and examples to the learner's immediate physical surroundings.

2. **Fluid Multilingual Code-Switching (English ⇄ Kiswahili ⇄ Sheng)**:
   - Students can ask questions in their mother tongue, formal Swahili, English, or colloquial Sheng.
   - ElewaSTEM provides the conceptual explanation in conversational Swahili while highlighting the formal English scientific terms required to pass national examinations (*Usanisinuru ➔ Photosynthesis*).

3. **Socratic "Usimeze, Elewa!" Pedagogy**:
   - Rather than just giving the direct answer to homework, the agent guides the child step-by-step with intuitive questions, encouraging feedback, and safe at-home mini-experiments using everyday household items (bottles, salt, water, leaves).

4. **Persistent Student Mastery Memory & Badges**:
   - Maintains a dynamic mastery graph across Physics, Biology, Chemistry, and Math.
   - Remembers what topics the student understands, tracks misconceptions, and awards motivational badges (*"Mvumbuzi Chipukizi"*, *"Bingwa wa Sayansi"*).

5. **Offline-First & Low-Connectivity PWA Architecture**:
   - Built as a lightweight Progressive Web App (<100KB) with a local **Offline Knowledge Vault**.
   - Children can browse lessons, conduct experiments, and take quizzes with **0 KB data connection**.
   - Features zero-bandwidth browser speech synthesis (TTS) and voice recognition (STT).
   - SMS/USSD gateway webhook ready for basic 2G feature phones.

---

## 🛠️ How We Built It

* **AI & Agent Core**: 
  - Google Gemini 2.5 / 3.5 Flash via the official `google-genai` Python SDK.
  - Specialized system prompts engineered with pedagogical scaffolding, regional eco-zone grounding, and bilingual scientific vocabulary pairing.
* **Backend Architecture**:
  - FastAPI asynchronous server with REST endpoints for multi-turn chat, geo-region listing, student profile management, offline pack distribution, and SMS webhook.
  - Persistent JSON/Firestore-ready Memory Bank tracking student mastery levels and geo-coordinates.
* **Frontend & Edge Client**:
  - Progressive Web App (PWA) with Service Worker caching and IndexedDB local storage.
  - Offline GPS Coordinate-to-Biome mapping algorithm.
  - Web Speech API for real-time voice input (STT) and native African accent speech synthesis (TTS).
  - Clean, kid-friendly responsive UI built with Tailwind CSS.

---

## 🧗 Challenges We Ran Into

1. **Making GPS & Geo-Context Work 100% Disconnected**:
   - Standard geolocation lookups query cloud reverse-geocoding APIs which fail without internet. We overcame this by implementing an edge bounding-box mathematical algorithm directly in the client that maps raw GPS hardware coordinates to African ecological regions with zero network calls.
2. **Balancing Vernacular Intuition with Academic Terminology**:
   - We built the **Dual-Language Vocabulary Bridge**, which always pairs the Swahili concept with its English exam counterpart (e.g. *Usanisinuru ➔ Photosynthesis*).

---

## 🏆 Accomplishments We're Proud Of

* Creating an agent that African children genuinely feel comfortable talking to—free of judgment, culturally grounded in their home region, and deeply encouraging.
* Zero-bandwidth voice, offline GPS detection, and offline lesson capabilities that make generative AI accessible beyond high-speed urban fibers.
* Seamless real-time code-switching between English, Swahili, and Sheng without losing scientific accuracy.

---

## 📚 What We Learned

True educational equity in AI isn't just about translating English words into another language—it is about **cultural and geographical translation of mental models**. Grounding science in a child's lived environment transforms STEM from an intimidating, foreign subject into a joyful, familiar journey of discovery.

---

## 🔮 What's Next for ElewaSTEM

* **Language Expansion**: Scaling beyond Swahili and Sheng to Yoruba, Hausa, Igbo, Amharic, Oromo, and Zulu.
* **Direct SMS / USSD Deployment**: Partnering with Africa's Talking to launch ElewaSTEM on toll-free SMS numbers across Kenya, Tanzania, Uganda, and Nigeria.
* **Integration with National Curriculums**: Partnering with KICD (Kenya), NECTA (Tanzania), and UNEB (Uganda) to map every lesson directly to official primary and junior secondary competency-based strands.
