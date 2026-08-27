/**
 * ElewaSTEM Frontend Application Logic with Deep Localized Context & Kenya DPA 2019 Privacy Compliance
 * Handles Offline PWA Caching, Bilingual Switching, Explicit GPS Consent, Regional Eco-Zones, and Mastery Graphs.
 */

// Application State
const STATE = {
  studentId: 'demo_student',
  language: 'swahili', // 'swahili', 'english', 'sheng'
  region: 'lake_basin', // Defaulting to Lake Victoria Basin (Kisumu)
  gpsCoords: null,
  dpaConsent: false,
  simulatedOffline: false,
  activeTab: 'chat',
  offlineModules: [],
  regionsMeta: {
    lake_basin: { name_sw: 'Kisumu & Ziwa Victoria', name_en: 'Lake Victoria Basin (Kisumu)', icon: '🏞️', desc_sw: 'Kisumu, Mwanza, Entebbe • Samaki Ngege & Mbuta, Magugu Maji (Akech), Osuga & Mitoo' },
    coastal: { name_sw: 'Pwani na Bahari', name_en: 'Coastal & Ocean (Mombasa)', icon: '🌊', desc_sw: 'Mombasa, Kilifi, Zanzibar • Minazi, mikoko ya kupumulia, chumvi' },
    highlands: { name_sw: 'Nyanda za Juu & Kilimo', name_en: 'Highlands & Farms', icon: '⛰️', desc_sw: 'Nakuru, Eldoret, Mt. Kenya • Mashamba ya chai & mahindi, mito ya milima' },
    arid: { name_sw: 'Maeneo Kavu & Ukame', name_en: 'Arid & Pastoralist', icon: '☀️', desc_sw: 'Turkana, Garissa, Kajiado • Miti ya acacia yenye nta, ngamia, solar boreholes' },
    urban: { name_sw: 'Mijini', name_en: 'Urban Centers', icon: '🏙️', desc_sw: 'Nairobi, Kampala, Dar, Lagos • Taa za solar, matatu electronics, miti ya jiji' }
  },
  profile: {
    name: 'Mwanafunzi Hodari',
    grade_level: 'Grade 6',
    current_region: 'lake_basin',
    mastery_graph: {},
    badges: ['🌟 Mwanzo Bora (Great Start)']
  },
  currentQuiz: null
};

// UI Translations
const I18N = {
  swahili: {
    tab_chat: 'Mwalimu Chat',
    tab_vault: 'Offline Vault (Masomo)',
    tab_mastery: 'Maendeleo & Beji',
    input_placeholder: 'Uliza swali la sayansi au hesabu hapa...',
    online_text: 'Mtandaoni',
    offline_text: 'Nje ya Mtandao (0 KB)',
    listen_btn: '🔊 Sikiliza',
    simplify_btn: '💡 Rahisisha',
    quiz_btn: '🎯 Fanya Jaribio'
  },
  english: {
    tab_chat: 'Tutor Chat',
    tab_vault: 'Offline Vault (Lessons)',
    tab_mastery: 'Mastery & Badges',
    input_placeholder: 'Ask any STEM question here...',
    online_text: 'Online',
    offline_text: 'Offline (0 KB)',
    listen_btn: '🔊 Listen',
    simplify_btn: '💡 Simplify',
    quiz_btn: '🎯 Take Quiz'
  },
  sheng: {
    tab_chat: 'Msee wa STEM',
    tab_vault: 'Masomo Offline',
    tab_mastery: 'Level Yangu & Badges',
    input_placeholder: 'Uliza swali ya science au math hapa...',
    online_text: 'Online',
    offline_text: 'Offline (Zero Data)',
    listen_btn: '🔊 Sikiza',
    simplify_btn: '💡 Fafanua zaidi',
    quiz_btn: '🎯 Cheza Quiz'
  }
};

// Regional Quick Prompt Templates (Deeply Localized)
const REGIONAL_PROMPT_CHIPS = {
  lake_basin: [
    { title: '🐟 Samaki Ngege & Upumuaji Ziwani', query: 'Eleza jinsi samaki Ngege (Tilapia) na Mbuta kule Kisumu wanavyotumia yavuyavu (gills) kupumua oksijeni ya Ziwa Victoria' },
    { title: '🌿 Magugu Maji (Akech) & Photosynthesis', query: 'Eleza jinsi magugu maji ya Ziwa Victoria na mboga za Osuga/Mitoo zinavyofanya usanisinuru (photosynthesis) kwa jua la ziwani' },
    { title: '⚡ Taa za Betri za Kuvulia Dagaa', query: 'Eleza saketi ya umeme kwa mfano wa betri ya 12V na taa ya kuvulia samaki usiku ziwani' },
    { title: '🐠 Kapu la Samaki 10 (Fractions)', query: 'Nifundishe fractions kwa mfano wa kupika samaki 5 kati ya 10 waliovuliwa Ziwa Victoria' }
  ],
  coastal: [
    { title: '🌴 Minazi & Usanisinuru Pwani', query: 'Eleza jinsi minazi ya Pwani inavyotumia mwangaza wa jua kutengeneza maji ya dafu (photosynthesis)' },
    { title: '⚡ Pampu za Chumvi & Umeme', query: 'Eleza volteji na mkondo wa umeme (current) kwa mfano wa pampu za maji ya chumvi baharini' },
    { title: '🌊 Grabiti & Mawimbi ya Bahari', query: 'Eleza nguvu ya grabiti ya mwezi na jinsi inavyoleta maji kujaa na kupwa baharini' },
    { title: '🥥 Kugawana Nazi & Samaki (Fractions)', query: 'Nifundishe sehemu za nambari (fractions) kwa kugawana nazi na samaki wa biriani' }
  ],
  highlands: [
    { title: '🌽 Mahindi, Chai & Photosynthesis', query: 'Eleza usanisinuru (photosynthesis) inavyofanya kazi kwa mashamba ya mahindi na majani ya chai milimani' },
    { title: '⚡ Umeme wa Maji (Hydroelectric Dams)', query: 'Eleza umeme, volteji na saketi kwa mfano wa mtambo wa maji wa Masinga au Sondu Miriu' },
    { title: '🚲 Grabiti & Breki za Baiskeli', query: 'Kwa nini baiskeli inateremka mlima kwa kasi? Eleza Grabiti na Msuguano wa breki kwenye vumbi' },
    { title: '🥔 Mavuno ya Viazi (Fractions)', query: 'Nifundishe Fractions kwa kugawa vikapu vya mavuno ya viazi shambani' }
  ],
  arid: [
    { title: '☀️ Miti ya Acacia Kwenye Jua Kali', query: 'Eleza jinsi miti ya acacia kule Turkana/Garissa inavyofanya usanisinuru bila kupoteza maji wakati wa ukame' },
    { title: '⚡ Nishati ya Solar & Visima vya Maji', query: 'Eleza volteji na saketi kwa mfano wa paneli za jua (Solar PV) zinazoendesha pampu za visima vya maji' },
    { title: '🌪️ Upepo, Mchanga & Grabiti', query: 'Kwa nini upepo hupeperusha vumbi lakini mawe mazito yanabaki chini? Eleza nguvu ya mvuto wa ardhi' },
    { title: '💧 Dumu la Maji Kisimani (Fractions)', query: 'Nifundishe fractions kwa mfano wa kuchota lita 5 kwenye dumu la lita 20 kisimani' }
  ],
  urban: [
    { title: '🌿 Miti ya Jiji & Kusafisha Moshi', query: 'Eleza jinsi miti ya kando ya barabara za jiji inavyofyonza hewa ya moshi wa magari na kutoa oksijeni' },
    { title: '⚡ Taa za Barabarani & Matatu Electronics', query: 'Eleza saketi za umeme kwa mfano wa taa za barabarani za solar na mfumo wa redio wa matatu' },
    { title: '🚗 Matairi ya Gari & Msuguano wa Lami', query: 'Eleza nguvu ya msuguano kwa mfano wa michirizi ya matairi ya gari kwenye barabara ya lami wakati wa mvua' },
    { title: '🍕 Chapati na Pizza Mtaani (Fractions)', query: 'Nifundishe fractions kwa mfano wa kukata na kugawa vipande vya chapati au pizza mtaani' }
  ]
};

// Initialize Application
document.addEventListener('DOMContentLoaded', async () => {
  initNetworkListeners();
  loadSavedConsentAndRegion();
  await loadOfflinePack();
  await refreshProfile();
  renderRegionUI();
  renderVault();
  updateUIStrings();
});

// Network Connectivity & Offline Simulation
function initNetworkListeners() {
  window.addEventListener('online', updateNetworkUI);
  window.addEventListener('offline', updateNetworkUI);
  updateNetworkUI();
}

function isEffectivelyOnline() {
  return navigator.onLine && !STATE.simulatedOffline;
}

function updateNetworkUI() {
  const badge = document.getElementById('networkBadge');
  const dot = document.getElementById('networkDot');
  const text = document.getElementById('networkText');
  const online = isEffectivelyOnline();

  if (online) {
    badge.className = 'flex items-center space-x-1 px-2 sm:px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800 border border-emerald-300 transition-all hover:scale-105';
    dot.className = 'w-2 h-2 rounded-full bg-emerald-500 animate-pulse';
    text.innerText = I18N[STATE.language].online_text;
  } else {
    badge.className = 'flex items-center space-x-1 px-2 sm:px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-100 text-amber-800 border border-amber-300 transition-all hover:scale-105';
    dot.className = 'w-2 h-2 rounded-full bg-amber-500';
    text.innerText = I18N[STATE.language].offline_text;
  }
}

function toggleSimulateOffline() {
  STATE.simulatedOffline = !STATE.simulatedOffline;
  updateNetworkUI();
  const reg = STATE.regionsMeta[STATE.region] || STATE.regionsMeta.lake_basin;
  const msg = STATE.simulatedOffline 
    ? (STATE.language === 'swahili' ? `🔴 Umeingia hali ya Nje ya Mtandao (Offline). Mifano ya ${reg.name_sw} inafanya kazi 100% bila mtandao kupitia Local Vault!` : `🔴 Offline simulation enabled. Tutor for ${reg.name_en} running from local offline vault!`)
    : (STATE.language === 'swahili' ? '🟢 Umerudi Mtandaoni (Online). Gemini 2.5 Flash imeunganishwa tena!' : '🟢 Back Online! Connected to Gemini 2.5 Flash backend.');
  
  appendSystemNotice(msg);
}

// Data Protection & Explicit Consent Handlers (Kenya DPA 2019)
function loadSavedConsentAndRegion() {
  STATE.dpaConsent = (localStorage.getItem('elewa_dpa_consent') === 'granted');
  const saved = localStorage.getItem('elewa_user_region');
  if (saved && STATE.regionsMeta[saved]) {
    STATE.region = saved;
  }
}

function handleGPSButtonClick() {
  if (STATE.dpaConsent) {
    executeGPSScan();
  } else {
    document.getElementById('consentModal').classList.remove('hidden');
  }
}

function grantLocationConsentAndDetect() {
  STATE.dpaConsent = true;
  localStorage.setItem('elewa_dpa_consent', 'granted');
  document.getElementById('consentModal').classList.add('hidden');
  executeGPSScan();
}

function declineLocationConsent() {
  document.getElementById('consentModal').classList.add('hidden');
  openRegionModal();
}

function revokeLocationConsent() {
  STATE.dpaConsent = false;
  localStorage.removeItem('elewa_dpa_consent');
  STATE.gpsCoords = null;
  closePrivacyModal();
  appendSystemNotice('🛡️ <b>Data Protection Act:</b> Idhini ya GPS imefutwa. Hakuna data ya kijiografia itakayosomwa.');
}

function openPrivacyModal() {
  document.getElementById('privacyModal').classList.remove('hidden');
}

function closePrivacyModal() {
  document.getElementById('privacyModal').classList.add('hidden');
}

// GPS Execution (Edge calculation on device)
function executeGPSScan() {
  if (!('geolocation' in navigator)) {
    alert('Kifaa chako hakina GPS (Geolocation is not supported).');
    return;
  }

  const gpsBtn = document.getElementById('gpsBtn');
  if (gpsBtn) gpsBtn.classList.add('bg-amber-400', 'animate-pulse');

  navigator.geolocation.getCurrentPosition(
    (position) => {
      if (gpsBtn) gpsBtn.classList.remove('bg-amber-400', 'animate-pulse');
      const lat = position.coords.latitude;
      const lon = position.coords.longitude;
      STATE.gpsCoords = { lat, lon };

      // Map latitude & longitude to African eco-regions (100% on-device offline calculation)
      const detectedRegion = mapCoordinatesToEcoRegion(lat, lon);
      selectRegion(detectedRegion);

      const reg = STATE.regionsMeta[detectedRegion];
      appendSystemNotice(`🎯 <b>GPS Auto-Detect (DPA 2019 Protected):</b> [${lat.toFixed(2)}, ${lon.toFixed(2)}] ➔ ${reg.icon} <b>${reg.name_sw}</b>.`);
    },
    (error) => {
      if (gpsBtn) gpsBtn.classList.remove('bg-amber-400', 'animate-pulse');
      console.log('GPS notice:', error.message);
      appendSystemNotice(`📍 Hatujaweza kusoma GPS. Unaweza kuchagua kaunti/eneo lako kwenye orodha!`);
      openRegionModal();
    },
    { enableHighAccuracy: true, timeout: 8000, maximumAge: 60000 }
  );
}

// On-device coordinate to African eco-region mapper
function mapCoordinatesToEcoRegion(lat, lon) {
  // Lake Victoria Basin (Kisumu, Homa Bay, Busia, Mwanza, Entebbe)
  if (lon >= 31.0 && lon <= 35.2 && lat >= -3.5 && lat <= 2.5) {
    return 'lake_basin';
  }
  // Coastal Strip (Mombasa, Kilifi, Kwale, Lamu, Dar es Salaam, Zanzibar)
  if (lon > 38.5 && lat < 1.0 && lat > -11.0) {
    return 'coastal';
  }
  // Arid & Pastoralist Belt (Northern Kenya: Turkana, Garissa, Marsabit, Wajir, Central Tanzania)
  if ((lat > 1.2 && lon > 35.0) || (lat < -4.5 && lon < 37.0 && lon > 34.0)) {
    return 'arid';
  }
  // Major Urban Centers (Nairobi metropolitan area)
  if (lat >= -1.45 && lat <= -1.15 && lon >= 36.65 && lon <= 37.10) {
    return 'urban';
  }
  // Highlands & Agricultural Belt (Nakuru, Mt. Kenya, Eldoret, Kericho)
  return 'highlands';
}

function openRegionModal() {
  document.getElementById('regionModal').classList.remove('hidden');
}

function closeRegionModal() {
  document.getElementById('regionModal').classList.add('hidden');
}

function selectRegion(regionKey) {
  if (!STATE.regionsMeta[regionKey]) return;
  STATE.region = regionKey;
  localStorage.setItem('elewa_user_region', regionKey);
  closeRegionModal();
  renderRegionUI();
  renderVault();

  const reg = STATE.regionsMeta[regionKey];
  const isSw = STATE.language !== 'english';
  appendSystemNotice(`📍 ${isSw ? 'Mazingira ya eneo yamebadilishwa kuwa:' : 'Eco-region switched to:'} <b>${reg.icon} ${isSw ? reg.name_sw : reg.name_en}</b>.`);
}

function renderRegionUI() {
  const reg = STATE.regionsMeta[STATE.region] || STATE.regionsMeta.lake_basin;
  const isSw = STATE.language !== 'english';

  const iconEl = document.getElementById('regionIcon');
  const textEl = document.getElementById('regionNameText');
  const welcomeEcoPill = document.getElementById('welcomeEcoPill');
  const welcomeDesc = document.getElementById('welcomeLocationDesc');
  const vaultNotice = document.getElementById('vaultRegionNotice');
  const vaultIcon = document.getElementById('vaultRegionIcon');
  const profilePill = document.getElementById('profileRegionPill');

  if (iconEl) iconEl.innerText = reg.icon;
  if (textEl) textEl.innerText = isSw ? reg.name_sw : reg.name_en;
  if (welcomeEcoPill) welcomeEcoPill.innerText = `📍 Eneo: ${reg.icon} ${isSw ? reg.name_sw : reg.name_en}`;
  if (welcomeDesc) welcomeDesc.innerText = isSw ? reg.name_sw : reg.name_en;
  if (vaultNotice) vaultNotice.innerText = isSw ? reg.name_sw : reg.name_en;
  if (vaultIcon) vaultIcon.innerText = reg.icon;
  if (profilePill) profilePill.innerText = `📍 Eneo: ${reg.icon} ${isSw ? reg.name_sw : reg.name_en}`;

  // Render regional prompt chips
  const chipsContainer = document.getElementById('quickLocationChips');
  if (chipsContainer) {
    const chips = REGIONAL_PROMPT_CHIPS[STATE.region] || REGIONAL_PROMPT_CHIPS.lake_basin;
    chipsContainer.innerHTML = chips.map(c => `
      <button onclick="sendQuickPrompt('${escapeHtml(c.query)}')" class="quick-chip bg-emerald-50 text-emerald-800 border border-emerald-300 px-2.5 py-1 rounded-full text-xs hover:bg-emerald-100 font-medium transition-all">
        ${c.title}
      </button>
    `).join('');
  }
}

// Language Switching
function changeLanguage(lang) {
  STATE.language = lang;
  updateUIStrings();
  updateNetworkUI();
  renderRegionUI();
  renderVault();
  renderMastery();
}

function updateUIStrings() {
  const dict = I18N[STATE.language] || I18N.swahili;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key]) el.innerText = dict[key];
  });
  const input = document.getElementById('userInput');
  if (input) input.placeholder = dict.input_placeholder;
}

// Navigation Tabs
function switchTab(tabId) {
  STATE.activeTab = tabId;
  ['chat', 'vault', 'mastery'].forEach(t => {
    const section = document.getElementById(`${t}Section`);
    const btn = document.getElementById(`tabBtn-${t}`);
    if (t === tabId) {
      section.classList.remove('hidden');
      btn.classList.add('active-tab');
    } else {
      section.classList.add('hidden');
      btn.classList.remove('active-tab');
    }
  });

  if (tabId === 'mastery') refreshProfile();
}

// Offline Pack Management
async function loadOfflinePack() {
  try {
    const cached = localStorage.getItem('elewa_offline_pack');
    if (cached) {
      STATE.offlineModules = JSON.parse(cached);
    }
    if (navigator.onLine) {
      const res = await fetch('/api/offline-pack');
      if (res.ok) {
        const data = await res.json();
        STATE.offlineModules = data.modules || [];
        localStorage.setItem('elewa_offline_pack', JSON.stringify(STATE.offlineModules));
      }
    }
  } catch (err) {
    console.log('Offline pack load notice:', err);
  }
}

// Chat Flow
async function handleChatSubmit(e) {
  if (e) e.preventDefault();
  const input = document.getElementById('userInput');
  const query = input.value.trim();
  if (!query) return;

  input.value = '';
  appendUserMessage(query);
  await executeAgentQuery(query);
}

function sendQuickPrompt(text) {
  switchTab('chat');
  appendUserMessage(text);
  executeAgentQuery(text);
}

async function executeAgentQuery(query, simplify = false) {
  const loadingId = appendLoadingIndicator();

  // If offline or simulated offline -> execute locally from cached vault
  if (!isEffectivelyOnline()) {
    setTimeout(() => {
      removeLoadingIndicator(loadingId);
      const localResponse = generateLocalOfflineAnswer(query, simplify);
      appendAssistantMessage(localResponse);
    }, 400);
    return;
  }

  // If online -> send to backend API with region & GPS context
  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        student_id: STATE.studentId,
        message: query,
        language: STATE.language,
        region: STATE.region,
        gps_coordinates: STATE.gpsCoords,
        simplify: simplify
      })
    });

    removeLoadingIndicator(loadingId);

    if (res.ok) {
      const data = await res.json();
      appendAssistantMessage(data);
      if (data.student_profile) {
        STATE.profile = data.student_profile;
      }
    } else {
      const localFallback = generateLocalOfflineAnswer(query, simplify);
      appendAssistantMessage(localFallback);
    }
  } catch (err) {
    removeLoadingIndicator(loadingId);
    const localFallback = generateLocalOfflineAnswer(query, simplify);
    appendAssistantMessage(localFallback);
  }
}

function generateLocalOfflineAnswer(query, simplify) {
  const qLower = query.toLowerCase();
  let matched = STATE.offlineModules.find(m => 
    qLower.includes(m.id) || 
    qLower.includes(m.title_en.toLowerCase()) || 
    qLower.includes(m.title_sw.toLowerCase()) ||
    m.key_terms.some(k => qLower.includes(k.en.toLowerCase()) || qLower.includes(k.sw.toLowerCase()))
  ) || STATE.offlineModules[0];

  const regKey = STATE.region;
  const regMeta = STATE.regionsMeta[regKey] || STATE.regionsMeta.lake_basin;
  const isSw = STATE.language !== 'english';
  
  const title = isSw ? matched.title_sw : matched.title_en;
  const summary = isSw ? matched.summary_sw : matched.summary_en;

  const regionalDict = matched.regional_analogies ? (matched.regional_analogies[regKey] || matched.regional_analogies.lake_basin) : {};
  const analogy = isSw ? (regionalDict.analogy_sw || matched.analogy_sw) : (regionalDict.analogy_en || matched.analogy_en);
  
  const exp = matched.experiment;
  const quiz = matched.quiz;

  const termsFormatted = matched.key_terms.map(t => `• **${t.en}** ➔ ${t.sw}`).join('\n');

  const text = `### 🔬 ${title}

${isSw ? `Habari kutoka **${regMeta.icon} ${regMeta.name_sw}** (Offline Vault):` : `Explanation for **${regMeta.icon} ${regMeta.name_en}** (Offline Vault):`}

${summary}

---

#### 💡 Mfano Halisi wa Eneo Lako (${regMeta.icon} ${isSw ? regMeta.name_sw : regMeta.name_en})
${analogy}

---

#### 📚 Kamusi ya Sayansi (Key Terms)
${termsFormatted}

---

#### 🧪 Jaribu Hili Nyumbani (${isSw ? exp.title_sw : exp.title_en})
**Vifaa:** ${isSw ? exp.materials_sw : exp.materials_en}
**Hatua:**
${isSw ? exp.steps_sw : exp.steps_en}
`;

  return {
    source: 'local_offline_vault',
    text: text,
    language: STATE.language,
    region: STATE.region,
    topic: matched.title_en,
    subject: matched.subject,
    quiz_data: quiz
  };
}

// UI Rendering Helpers
function appendUserMessage(text) {
  const container = document.getElementById('chatMessages');
  const div = document.createElement('div');
  div.className = 'flex justify-end';
  div.innerHTML = `
    <div class="bg-brand-600 text-white rounded-2xl rounded-tr-sm px-4 py-2.5 shadow-sm max-w-[80%] text-sm font-medium leading-relaxed">
      ${escapeHtml(text)}
    </div>
  `;
  container.appendChild(div);
  container.scrollTop = container.scrollHeight;
}

function appendAssistantMessage(data) {
  const container = document.getElementById('chatMessages');
  const div = document.createElement('div');
  div.className = 'flex items-start space-x-3';

  const isOffline = data.source === 'local_offline_vault' || data.source === 'offline_knowledge_vault';
  const formattedHtml = parseMarkdownToHtml(data.text);
  const quizDataJson = data.quiz_data ? JSON.stringify(data.quiz_data).replace(/"/g, '&quot;') : '';
  const regMeta = STATE.regionsMeta[data.region || STATE.region] || STATE.regionsMeta.lake_basin;

  div.innerHTML = `
    <div class="w-8 h-8 rounded-full bg-brand-600 flex items-center justify-center text-white text-sm flex-shrink-0 shadow">
      🌱
    </div>
    <div class="bg-white border border-slate-200 rounded-2xl rounded-tl-sm p-4 shadow-sm max-w-[85%] text-sm text-slate-800 space-y-3">
      <div class="flex items-center space-x-2 flex-wrap gap-1 mb-1">
        ${isOffline ? '<span class="inline-block bg-amber-100 text-amber-800 text-[10px] font-bold px-2 py-0.5 rounded-full">📦 Offline Vault</span>' : '<span class="inline-block bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded-full">✨ Gemini 2.5 Flash</span>'}
        <span class="inline-block bg-slate-100 text-slate-700 text-[10px] font-bold px-2 py-0.5 rounded-full">${regMeta.icon} ${regMeta.name_sw}</span>
      </div>
      <div class="stem-card leading-relaxed space-y-2">${formattedHtml}</div>
      
      <!-- Action Toolbar -->
      <div class="pt-2 border-t border-slate-100 flex flex-wrap gap-2 text-xs font-semibold">
        <button onclick="speakText('${encodeURIComponent(data.text)}')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-brand-50 hover:text-brand-700 text-slate-700 flex items-center space-x-1 transition-all">
          <span>🔊</span>
          <span>Sikiliza (TTS)</span>
        </button>
        <button onclick="executeAgentQuery('Eleza hili tena kwa mifano rahisi sana ya eneo langu', true)" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-brand-50 hover:text-brand-700 text-slate-700 flex items-center space-x-1 transition-all">
          <span>💡</span>
          <span>Rahisisha</span>
        </button>
        ${data.quiz_data ? `
        <button onclick="openQuizModal('${quizDataJson}', '${escapeHtml(data.topic || 'STEM')}')" class="px-2.5 py-1 rounded-lg bg-brand-600 hover:bg-brand-700 text-white flex items-center space-x-1 shadow-sm transition-all">
          <span>🎯</span>
          <span>Fanya Jaribio</span>
        </button>` : ''}
      </div>
    </div>
  `;
  container.appendChild(div);
  container.scrollTop = container.scrollHeight;
}

function appendSystemNotice(text) {
  const container = document.getElementById('chatMessages');
  const div = document.createElement('div');
  div.className = 'flex justify-center my-2';
  div.innerHTML = `
    <span class="bg-slate-200 text-slate-700 text-xs font-semibold px-3 py-1 rounded-full shadow-inner text-center">
      ${text}
    </span>
  `;
  container.appendChild(div);
  container.scrollTop = container.scrollHeight;
}

function appendLoadingIndicator() {
  const container = document.getElementById('chatMessages');
  const id = 'loading_' + Date.now();
  const regMeta = STATE.regionsMeta[STATE.region] || STATE.regionsMeta.lake_basin;
  const div = document.createElement('div');
  div.id = id;
  div.className = 'flex items-start space-x-3';
  div.innerHTML = `
    <div class="w-8 h-8 rounded-full bg-brand-600 flex items-center justify-center text-white text-sm flex-shrink-0 shadow animate-pulse">
      🌱
    </div>
    <div class="bg-white border border-slate-200 rounded-2xl rounded-tl-sm px-4 py-3 shadow-sm text-xs font-bold text-slate-500 flex items-center space-x-2">
      <span class="w-2 h-2 rounded-full bg-brand-600 animate-ping"></span>
      <span>Mwalimu anatafuta mfano wa ${regMeta.icon} ${regMeta.name_sw}...</span>
    </div>
  `;
  container.appendChild(div);
  container.scrollTop = container.scrollHeight;
  return id;
}

function removeLoadingIndicator(id) {
  const el = document.getElementById(id);
  if (el) el.remove();
}

// Markdown Parser Helper
function parseMarkdownToHtml(markdown) {
  if (!markdown) return '';
  return markdown
    .replace(/^### (.*$)/gim, '<h3>$1</h3>')
    .replace(/^#### (.*$)/gim, '<h4>$1</h4>')
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/^---$/gim, '<hr>')
    .replace(/^\• (.*$)/gim, '<li>$1</li>')
    .replace(/\n\n/g, '<p></p>')
    .replace(/\n/g, '<br>');
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Speech Synthesis (TTS)
function speakText(encodedText) {
  const text = decodeURIComponent(encodedText)
    .replace(/###/g, '')
    .replace(/####/g, '')
    .replace(/\*\*/g, '')
    .replace(/---/g, '')
    .replace(/•/g, '');

  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 0.95;
    utterance.pitch = 1.0;
    utterance.lang = STATE.language === 'english' ? 'en-US' : 'sw-KE';
    window.speechSynthesis.speak(utterance);
  } else {
    alert('Kifaa chako hakitumii sauti (Speech synthesis is not supported on this browser).');
  }
}

// Speech Recognition (Voice Input)
function toggleVoiceInput() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    alert('Voice input is not supported in this browser. Please type your question.');
    return;
  }

  const voiceBtn = document.getElementById('voiceBtn');
  const recognition = new SpeechRecognition();
  recognition.lang = STATE.language === 'english' ? 'en-US' : 'sw-KE';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  voiceBtn.classList.add('bg-red-500', 'text-white', 'animate-pulse');

  recognition.start();

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    document.getElementById('userInput').value = transcript;
    voiceBtn.classList.remove('bg-red-500', 'text-white', 'animate-pulse');
    handleChatSubmit();
  };

  recognition.onerror = () => {
    voiceBtn.classList.remove('bg-red-500', 'text-white', 'animate-pulse');
  };

  recognition.onend = () => {
    voiceBtn.classList.remove('bg-red-500', 'text-white', 'animate-pulse');
  };
}

// Offline Vault Rendering
function renderVault() {
  const container = document.getElementById('vaultModulesGrid');
  if (!container) return;
  const isSw = STATE.language !== 'english';
  const regKey = STATE.region;
  const regMeta = STATE.regionsMeta[regKey] || STATE.regionsMeta.lake_basin;

  container.innerHTML = STATE.offlineModules.map(m => {
    const regionalDict = m.regional_analogies ? (m.regional_analogies[regKey] || m.regional_analogies.lake_basin) : {};
    const localAnalogy = isSw ? (regionalDict.analogy_sw || m.analogy_sw) : (regionalDict.analogy_en || m.analogy_en);

    return `
      <div class="bg-white border border-slate-200 rounded-2xl p-4 shadow-sm space-y-3 hover:border-brand-500 transition-all flex flex-col justify-between">
        <div class="space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-700">${m.subject}</span>
            <span class="text-[10px] text-brand-700 font-bold bg-brand-50 border border-brand-200 px-2 py-0.5 rounded-full">📍 ${regMeta.icon} ${regMeta.name_sw}</span>
          </div>
          <h3 class="font-bold text-slate-900 text-base">${isSw ? m.title_sw : m.title_en}</h3>
          <p class="text-xs text-slate-600 line-clamp-2">${isSw ? m.summary_sw : m.summary_en}</p>
          <p class="text-[11px] text-brand-900 bg-emerald-50 p-2 rounded-xl border border-emerald-100 italic line-clamp-2"><b>💡 Mfano wa Eneo Lako:</b> ${localAnalogy}</p>
        </div>

        <div class="pt-2 border-t border-slate-100 flex space-x-2">
          <button onclick="openOfflineModuleInChat('${m.id}')" class="flex-1 bg-brand-50 hover:bg-brand-100 text-brand-800 text-xs font-bold py-2 rounded-xl text-center transition-all">
            Soma Somo
          </button>
          <button onclick="openQuizModal('${JSON.stringify(m.quiz).replace(/"/g, '&quot;')}', '${escapeHtml(m.title_en)}')" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold px-3 py-2 rounded-xl transition-all">
            🎯 Quiz
          </button>
        </div>
      </div>
    `;
  }).join('');
}

function openOfflineModuleInChat(moduleId) {
  const mod = STATE.offlineModules.find(m => m.id === moduleId);
  if (!mod) return;
  switchTab('chat');
  const answer = generateLocalOfflineAnswer(mod.id, false);
  appendAssistantMessage(answer);
}

// Student Profile & Mastery Graph
async function refreshProfile() {
  try {
    if (isEffectivelyOnline()) {
      const res = await fetch(`/api/profile/${STATE.studentId}`);
      if (res.ok) {
        STATE.profile = await res.json();
        if (STATE.profile.current_region) {
          STATE.region = STATE.profile.current_region;
          renderRegionUI();
        }
      }
    }
  } catch (e) {
    console.log('Profile fetch notice:', e);
  }
  renderMastery();
}

function renderMastery() {
  const badgeContainer = document.getElementById('badgesContainer');
  const graphContainer = document.getElementById('masteryGraphContainer');
  const badgeCountEl = document.getElementById('badgeCount');

  if (badgeContainer) {
    const badges = STATE.profile.badges || ['🌟 Mwanzo Bora (Great Start)'];
    if (badgeCountEl) badgeCountEl.innerText = badges.length;
    badgeContainer.innerHTML = badges.map(b => `
      <span class="bg-amber-50 border border-amber-200 text-amber-800 text-xs font-bold px-3 py-1.5 rounded-xl flex items-center space-x-1.5 shadow-sm">
        ${b}
      </span>
    `).join('');
  }

  if (graphContainer) {
    const graph = STATE.profile.mastery_graph || {};
    const topics = Object.values(graph);
    if (topics.length === 0) {
      graphContainer.innerHTML = `
        <p class="text-xs text-slate-500 italic">Bado hujaanza majaribio. Uliza maswali na ufanye quizzes ili kukuza kiwango chako cha uelewa!</p>
      `;
    } else {
      graphContainer.innerHTML = topics.map(t => `
        <div class="space-y-1">
          <div class="flex justify-between text-xs font-bold">
            <span class="text-slate-800">${t.topic} (${t.subject})</span>
            <span class="text-brand-700">${t.mastery_score}% Uelewa</span>
          </div>
          <div class="w-full bg-slate-100 rounded-full h-2.5 overflow-hidden">
            <div class="bg-brand-500 h-2.5 rounded-full transition-all duration-500" style="width: ${t.mastery_score}%"></div>
          </div>
        </div>
      `).join('');
    }
  }
}

// Interactive Quiz Modal
function openQuizModal(quizJsonStr, topicName) {
  try {
    const quiz = JSON.parse(quizJsonStr.replace(/&quot;/g, '"'));
    STATE.currentQuiz = { quiz, topicName };
    const modal = document.getElementById('quizModal');
    const title = document.getElementById('quizModalTitle');
    const question = document.getElementById('quizQuestion');
    const optionsContainer = document.getElementById('quizOptions');
    const feedback = document.getElementById('quizFeedback');

    title.innerText = `🎯 Swali: ${topicName}`;
    const isSw = STATE.language !== 'english';
    question.innerText = isSw ? quiz.question_sw : quiz.question_en;

    const opts = isSw ? quiz.options_sw : quiz.options_en;
    feedback.className = 'hidden';

    optionsContainer.innerHTML = opts.map((opt, idx) => `
      <button onclick="handleQuizAnswer(${idx})" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50 text-xs font-bold text-slate-800 transition-all flex items-center justify-between">
        <span>${opt}</span>
        <span class="text-slate-400">➜</span>
      </button>
    `).join('');

    modal.classList.remove('hidden');
  } catch (err) {
    console.error('Quiz modal error:', err);
  }
}

function handleQuizAnswer(selectedIndex) {
  if (!STATE.currentQuiz) return;
  const { quiz, topicName } = STATE.currentQuiz;
  const isSw = STATE.language !== 'english';
  const isCorrect = (selectedIndex === quiz.correct_index);

  const feedback = document.getElementById('quizFeedback');
  feedback.classList.remove('hidden');

  if (isCorrect) {
    feedback.className = 'p-3 rounded-xl text-xs font-semibold leading-relaxed bg-emerald-100 text-emerald-900 border border-emerald-300';
    feedback.innerHTML = `🎉 <b>${isSw ? 'Hongera sana! Uko sahihi!' : 'Awesome! That is correct!'}</b><br>${isSw ? quiz.explanation_sw : quiz.explanation_en}`;
  } else {
    feedback.className = 'p-3 rounded-xl text-xs font-semibold leading-relaxed bg-amber-100 text-amber-900 border border-amber-300';
    feedback.innerHTML = `💡 <b>${isSw ? 'Uko karibu! Jaribu tena:' : 'Almost! Try again:'}</b><br>${isSw ? quiz.explanation_sw : quiz.explanation_en}`;
  }

  // Record quiz result
  if (isEffectivelyOnline()) {
    fetch('/api/quiz-result', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        student_id: STATE.studentId,
        topic: topicName,
        passed: isCorrect,
        score: isCorrect ? 100 : 40
      })
    }).then(r => r.json()).then(d => {
      if (d.mastery_graph) STATE.profile.mastery_graph = d.mastery_graph;
      if (d.badges) STATE.profile.badges = d.badges;
      renderMastery();
    }).catch(err => console.log('Quiz sync notice:', err));
  }
}

function closeQuizModal() {
  document.getElementById('quizModal').classList.add('hidden');
  STATE.currentQuiz = null;
}
