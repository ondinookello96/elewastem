# 🌱 ElewaSTEM (Mwalimu STEM)

> **"Usimeze, Elewa!"** — *Demystifying STEM for Every African Child in Their Own Language.*

**ElewaSTEM** is an adaptive, offline-first multilingual AI STEM tutor designed specifically for children and young students in Africa. It bridges educational and language barriers by explaining complex concepts in Physics, Mathematics, Biology, Chemistry, and Computing through culturally grounded analogies, real-time code-switching between English, Swahili (Kiswahili), and Sheng, interactive quizzes, and persistent student memory.

---

## 🏆 All Things Agentic Hackathon Submission

* **Track**: **The Collaborative Partner**
* **Target Categories**: Best Multimodal UX, Best Architectural Design, Grand Prize
* **Core Technologies**: Google Gemini 2.5 / 3.5 Flash, `google-genai` Python SDK, FastAPI, PWA, Service Worker, Web Speech API

---

## 🌟 Key Features

1. **Dual-Language & Code-Switching Bridge**:
   * Fluidly switch between 🇬🇧 English, 🇰🇪 Kiswahili, and 💬 Sheng.
   * Understands questions asked in vernacular and pairs every concept with the formal English scientific terminology required for national exams.
2. **Culturally Grounded African Analogies**:
   * Explains electrical circuits via water tanks and irrigation pipes, cellular biology via village homesteads, fractions by slicing chapatis, and gravity via falling mangoes.
3. **Socratic & Interactive Pedagogy**:
   * Step-by-step guidance rather than homework spoon-feeding.
   * Hands-on at-home mini-experiments using everyday household items (water bottles, salt, sunlight, leaves).
4. **Persistent Student Mastery Bank**:
   * Tracks student progress, concept mastery percentage (0–100%), and awards badges (*Mvumbuzi Chipukizi*, *Bingwa wa Sayansi*).
5. **Offline-First & Low-Connectivity Architecture**:
   * Progressive Web App (PWA) with a local **Offline Knowledge Vault** (0 KB data required).
   * Background sync queue when intermittent 2G/3G bursts connect.
   * Zero-bandwidth browser-native Speech Synthesis (TTS) & Voice Recognition.
   * SMS/USSD webhook endpoint for feature phones (Africa's Talking compatible).

---

## 🏗️ Architecture Diagram

```
+-------------------------------------------------------------------------------+
|                       Child / Student in Africa                               |
|              (Mobile Browser, Low-Cost Android, or 2G Phone)                  |
+-------------------------------------------------------------------------------+
                                      |
                     +----------------+----------------+
                     |                                 |
         [Online / 2G-3G Burst]              [Offline / Disconnected]
                     |                                 |
                     v                                 v
      +-----------------------------+   +-------------------------------+
      |    FastAPI Agent Gateway    |   |     PWA Service Worker        |
      |   (Cloud Run / Localhost)   |   |   + Local Offline Vault       |
      +-----------------------------+   |   (IndexedDB / LocalStorage)  |
         |           |           |      +-------------------------------+
         |           |           |                     |
         v           v           v                     v
   +----------+ +---------+ +--------+     +-----------------------+
   |  Google  | | Student | |  SMS/  |     |  Zero-Bandwidth TTS   |
   |  Gemini  | | Mastery | |  USSD  |     |  & SVG Science Cards  |
   | 2.5/3.5  | | Memory  | | Webhook|     +-----------------------+
   |  Flash   | |  Bank   | +--------+
   +----------+ +---------+
```

---

## 🚀 Quick Start & Reproducible Testing

### 1. Prerequisites
* Python 3.10+
* Google Gemini API Key (Optional for live LLM mode; the app includes a full built-in Offline Vault if no key is set).

### 2. Setup & Installation
```bash
# Clone or navigate to the directory
cd elewastem

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Set your Gemini API key (optional for live generation)
# Windows PowerShell:
$env:GEMINI_API_KEY="your-gemini-api-key"
# Linux/macOS:
export GEMINI_API_KEY="your-gemini-api-key"
```

### 3. Run the Application
```bash
python run.py
```
Open your browser at **`http://localhost:8000`**.

---

## 🧪 Testing Guide

### Test 1: Multilingual Code-Switching
1. Select **🇰🇪 Kiswahili** in the top-right dropdown.
2. Ask: *"Eleza usanisinuru (photosynthesis) inavyofanya kazi kwa mmea wa mahindi"*
3. Notice how ElewaSTEM explains the concept using the green kitchen analogy while highlighting the English terms (*Chlorophyll*, *Carbon Dioxide*, *Oxygen*, *Glucose*).
4. Switch to **🇬🇧 English** or **💬 Sheng** and ask: *"How does electric current and voltage work?"*

### Test 2: Low-Connectivity & Offline Simulation
1. In the top bar, click the green **`🟢 Mtandaoni`** button to switch to **`🔴 Nje ya Mtandao (0 KB)`**.
2. Notice that the entire chat, lesson lookup, and interactive quizzes continue working seamlessly from the local offline knowledge vault without an internet connection!
3. Click the **`📦 Offline Vault`** tab to browse pre-cached modules.

### Test 3: Socratic Quiz & Mastery Badges
1. Take a quiz on any topic (e.g. Electricity or Fractions).
2. Answer correctly and watch the feedback animation.
3. Switch to the **`🏆 Maendeleo & Beji`** tab to see your mastery score update and badges unlock!

### Test 4: SMS / USSD Gateway Webhook (Africa's Talking Simulation)
```bash
curl -X POST http://localhost:8000/api/sms \
  -d "phoneNumber=+254712345678&text=Eleza+umeme+kwa+Kiswahili"
```

---

## 📂 Project Structure

```
elewastem/
├── backend/
│   ├── app.py                 # FastAPI server & endpoints
│   ├── agent.py               # Gemini 2.5/3.5 Flash Agent Orchestrator
│   ├── memory.py              # Persistent Student Memory Bank & Mastery Graph
│   ├── tools.py               # STEM analogies, bilingual quiz & offline vault tools
│   └── requirements.txt       # Dependencies
├── frontend/
│   ├── index.html             # Kid-friendly responsive bilingual PWA UI
│   ├── app.js                 # Offline sync queue, Web Speech TTS/STT, UI state
│   ├── sw.js                  # Service Worker for 0 KB offline caching
│   ├── manifest.json          # PWA Mobile Installation manifest
│   └── style.css              # Custom styling & animations
├── docs/
│   └── SUBMISSION_STORY.md    # Devpost submission narrative
├── data/
│   └── student_profiles.json  # Persistent student mastery database
├── run.py                     # One-click startup runner
└── README.md                  # Documentation
```

---

## 📄 License
MIT License. Built with ❤️ for African children and young scientists everywhere.
