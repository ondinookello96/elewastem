# ElewaSTEM — Devpost Submission Story

## Project Name
**ElewaSTEM (Mwalimu STEM)** — *Universal, Inclusive AI STEM Learning for Every African Child Across Language, Geography & Ability*

## Tagline
A voice-first, universally accessible & offline AI STEM ecosystem connecting learners (including blind, deaf, and dyslexic children), parents (SMS digests), teachers (CBC plans), & mentors.

---

## 🌟 Inspiration: True Educational Equity Leaves No Child Behind
In many African communities, children face compounding, systemic hurdles in STEM education:
1. **The Special Needs & Disability Barrier**: Visually impaired (blind/low-vision), hearing impaired (deaf/hard-of-hearing), and neurodiverse (dyslexic/ADHD) children are often completely excluded from digital STEM tools.
2. **The Literacy & Typing Barrier**: Early-grade and primary school learners struggle to type on touchscreens or read dense paragraphs of technical English text.
3. **The Parent-Teacher Disconnect**: Parents in rural and peri-urban areas (many without STEM backgrounds or smartphones) struggle to follow what their children are learning or support them at home.
4. **The Context & Connectivity Barrier**: Traditional textbooks reference foreign contexts with zero internet access in classrooms.

When an 8-year-old in Kisumu—whether blind, deaf, or speaking only Kiswahili—wonders why fish can breathe under Lake Victoria, they need an accessible, compassionate learning companion:
* **The Blind Child** receives rich **Tactile Audio Descriptions** (*"Shika jani bichi mkononi... hisi mishipa midogo..."*) and full screen-reader spoken guidance.
* **The Deaf Child** receives **Visual Sign Language Cues** mapped to Kenyan Sign Language (KSL) and clear step-by-step visual diagrams.
* **The Dyslexic Child** enjoys **High-Legibility Dyslexia Typography**, cream anti-glare filters, and bite-sized learning chunks.
* **The Parent** receives a simple Swahili SMS digest celebrating their child's progress with a fun 2-minute kitchen science challenge.
* **The Teacher** gets an instant CBC-aligned lesson plan with localized teaching aids and diagnostic quizzes using free local materials.

We built **ElewaSTEM** to unite all these learners and stakeholders into one holistic, privacy-respecting (Kenya DPA 2019 compliant) platform that works with **0 KB data connection**.

---

## 🚀 Key Universal Innovations

### 1. ♿ **Universal Accessibility (Blindness, Deafness, Dyslexia, Low-Vision)**:
* 👁️ **For Blind & Visually Impaired Learners**:
  - Full screen-reader semantic markup (`aria-live="polite"`).
  - **Tactile Audio Descriptions**: Explains physical textures, spatial dimensions, and tactile analogies of leaves, circuits, fish gills, and fractions so blind children can visualize through touch and sound.
  - Zero-bandwidth speech synthesis in natural Swahili and English.
* 🧏 **For Deaf & Hearing Impaired Learners**:
  - Visual sign language cues and terminology bridges aligned with Kenyan Sign Language (KSL).
  - Real-time visual subtitles, graphical process flowcharts, and visual feedback pulses.
* 📖 **For Dyslexic & Neurodiverse Learners**:
  - Dyslexia-friendly high-legibility typography, increased letter spacing, and soft cream anti-glare background tints.
  - Chunked, step-by-step Socratic learning to eliminate cognitive fatigue.
* 🌓 **High Contrast & Giant Text Scaling**: High-visibility yellow-on-black mode and scalable text sizes.

### 2. 🌍 **Hyper-Local African Geo-Context & Offline GPS**:
* Automatically detects or allows selecting the student's African eco-region (**Kisumu & Lake Victoria**, **Mombasa Coastal**, **Highland Farms**, **Turkana Arid Lands**, **Urban Centers**).
* Uses hardware GPS (**100% offline without cellular data**) to ground science in the student's local flora, fauna, and geography.

### 3. 🔒 **Child Data Privacy (Kenya Data Protection Act 2019 Compliant)**:
* Full compliance with **Section 29 of the Kenya DPA 2019** (Processing Personal Data of Children).
* 100% on-device edge calculation with explicit opt-in consent and zero cloud profiling.

### 4. 👥 **Multi-Stakeholder Hub (Parents, Teachers, Community Mentors)**:
* **Parents**: Weekly plain-language progress summaries, 1-click SMS cards for 2G feature phones, and weekend kitchen/farm science challenges.
* **Teachers**: CBC/NECTA-aligned lesson plan generator with localized teaching aids and printable diagnostic quizzes.
* **Community Mentors**: Zero-cost STEM club projects using local materials (clean water charcoal filters, solar cookers).

---

## 🛠️ How We Built It

* **AI & Multi-Agent Core**: 
  - Google Gemini 2.5 / 3.5 Flash via the official `google-genai` Python SDK.
  - Specialized system prompts engineered with pedagogical scaffolding, regional eco-zone grounding, and universal accessibility adaptations.
* **Voice & Multimodal UX**:
  - Web Speech API for real-time speech recognition (STT) and native multilingual speech synthesis (TTS).
  - High-accessibility CSS themes for Dyslexia, High Contrast, and Screen Readers.
* **Backend Architecture**:
  - FastAPI asynchronous server with REST endpoints for multi-turn chat, stakeholder lesson plans, parent digests, offline pack distribution, and SMS webhook.
  - Persistent JSON/Firestore-ready Memory Bank tracking student mastery levels and geo-coordinates.
* **Frontend & Edge Client**:
  - Progressive Web App (PWA) with Service Worker caching and IndexedDB local storage.
  - Offline GPS Coordinate-to-Biome mapping algorithm with Kenya DPA 2019 consent gatekeeper.

---

## 🏆 Accomplishments We're Proud Of

* Creating a genuinely **universal and inclusive STEM AI** where blind, deaf, dyslexic, rural, and urban African children learn on equal footing.
* Zero-bandwidth voice, offline GPS detection, and offline lesson capabilities that make generative AI accessible beyond high-speed urban fibers.
* Seamless real-time code-switching between English, Swahili, and Sheng without losing scientific rigor.

---

## 🔮 What's Next for ElewaSTEM

* **Physical Braille & Tactile Kit Integration**: Partnering with African institutes for the blind to map ElewaSTEM audio lessons to tactile 3D embossed diagrams.
* **Direct SMS / USSD & IVR Deployment**: Launching toll-free voice calls and SMS across Kenya, Tanzania, Uganda, and Nigeria.
* **National Curriculum Alignment**: Collaborating with KICD (Kenya), NECTA (Tanzania), and UNEB (Uganda) to certify ElewaSTEM lesson plans across all national primary school clusters.
