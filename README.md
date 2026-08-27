# 🌱 ElewaSTEM (Mwalimu STEM) — Geo-Adaptive & Multilingual AI STEM Tutor

> **"Usimeze, Elewa!"** — *Demystifying STEM for Every African Child in Their Own Language & Local Ecosystem.*

**ElewaSTEM** is an adaptive, offline-first multilingual AI STEM tutor designed specifically for children and young students in Africa. It bridges educational and language barriers by explaining complex concepts in Physics, Mathematics, Biology, Chemistry, and Computing through **culturally and geographically grounded analogies**, real-time code-switching between English, Swahili (Kiswahili), and Sheng, **offline GPS auto-detection**, interactive quizzes, and persistent student memory.

---

## 🏆 All Things Agentic Hackathon Submission

* **Track**: **The Collaborative Partner**
* **Target Categories**: Best Multimodal UX, Best Architectural Design, Grand Prize
* **Core Technologies**: Google Gemini 2.5 / 3.5 Flash, `google-genai` Python SDK, FastAPI, PWA, Service Worker, Geolocation API, Web Speech API

---

## 🌟 Key Features

1. **Hyper-Local Geo-Adaptive Context & Offline GPS**:
   * Automatically detects or allows selecting the student's African eco-region (**🌊 Coastal**, **⛰️ Highlands**, **🏞️ Lake Victoria Basin**, **☀️ Arid & Pastoralist**, **🏙️ Urban**).
   * Uses device hardware GPS (**which works 100% offline without mobile data**) to map coordinates directly to regional biomes.
   * Dynamically adapts all science analogies, experiments, and examples to the learner's immediate physical surroundings.
2. **Dual-Language & Code-Switching Bridge**:
   * Fluidly switch between 🇬🇧 English, 🇰🇪 Kiswahili, and 💬 Sheng.
   * Understands questions asked in vernacular and pairs every concept with the formal English scientific terminology required for national exams.
3. **Culturally Grounded African Analogies**:
   * Explains electrical circuits via water tanks & solar borehole pumps, cellular biology via village homesteads, fractions by sharing fish/chapatis, and gravity via falling mangoes/coconuts.
4. **Socratic & Interactive Pedagogy**:
   * Step-by-step guidance rather than homework spoon-feeding.
   * Hands-on at-home mini-experiments using everyday household items (water bottles, salt, sunlight, leaves).
5. **Persistent Student Mastery Bank**:
   * Tracks student progress, concept mastery percentage (0–100%), and awards badges (*Mvumbuzi Chipukizi*, *Bingwa wa Sayansi*).
6. **Offline-First & Low-Connectivity Architecture**:
   * Progressive Web App (PWA) with a local **Offline Knowledge Vault** (0 KB data required).
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
      | + Geo-Context Engine        |   |   + Offline GPS Biome Mapper  |
      +-----------------------------+   +-------------------------------+
         |           |           |                     |
         |           |           |                     v
         v           v           v          +-----------------------+
   +----------+ +---------+ +--------+      |  Zero-Bandwidth TTS   |
   |  Google  | | Student | |  SMS/  |      |  & SVG Science Cards  |
   |  Gemini  | | Mastery | |  USSD  |      +-----------------------+
   | 2.5/3.5  | | Memory  | | Webhook|
   |  Flash   | |  Bank   | +--------+
   +----------+ +---------+
```

---

## 🚀 Quick Start & Reproducible Testing

### 1. Prerequisites
* Python 3.10+
* Google Gemini API Key (Optional for live LLM mode; the app includes a full built-in Offline Vault if no key is set).

### 2. Run the Application
```powershell
cd C:\Users\Cosmas\.gemini\antigravity\scratch\elewastem
.\venv\Scripts\python run.py
```
Open your browser at **`http://localhost:8000`**.

---

## 🧪 Testing Guide

### Test 1: Geo-Adaptive Location Switching & Offline GPS
1. In the header bar, click the **`⛰️ Nyanda za Juu (Highlands)`** button or **`📍 GPS`** button.
2. Select **`🌊 Pwani na Bahari (Coastal)`**.
3. Notice how the chat prompt chips and offline vault immediately adapt to **coconut palms (*minazi*)**, **sea breezes**, and **salt evaporation pans**!
4. Switch to **`☀️ Maeneo Kavu (Turkana / Arid)`** to see **acacia drought adaptations** and **solar borehole pumps**.

### Test 2: Low-Connectivity & Offline Simulation
1. Click the green **`🟢 Mtandaoni`** button to switch to **`🔴 Nje ya Mtandao (0 KB)`**.
2. Notice that the entire chat, localized analogies, and quizzes continue working seamlessly from the local offline knowledge vault without an internet connection!
3. Click the **`📦 Offline Vault`** tab to browse pre-cached modules.

### Test 3: Multilingual Code-Switching & Speech
1. Select **🇰🇪 Kiswahili** or **💬 Sheng** in the language dropdown.
2. Ask: *"Eleza usanisinuru inavyofanya kazi"*
3. Click **`🔊 Sikiliza`** to hear speech synthesis audio.

---

## 📄 License
MIT License. Built with ❤️ for African children and young scientists everywhere.
