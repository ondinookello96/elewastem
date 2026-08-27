/**
 * ElewaSTEM Frontend Application Logic
 * Handles Offline PWA Caching, Bilingual Switching, Speech Synthesis/Recognition, and Mastery Graphs.
 */

// Application State
const STATE = {
  studentId: 'demo_student',
  language: 'swahili', // 'swahili', 'english', 'sheng'
  simulatedOffline: false,
  activeTab: 'chat',
  offlineModules: [],
  profile: {
    name: 'Mwanafunzi Hodari',
    grade_level: 'Grade 6',
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

// Initialize Application
document.addEventListener('DOMContentLoaded', async () => {
  initNetworkListeners();
  await loadOfflinePack();
  await refreshProfile();
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
    badge.className = 'flex items-center space-x-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800 border border-emerald-300 transition-all hover:scale-105';
    dot.className = 'w-2 h-2 rounded-full bg-emerald-500 animate-pulse';
    text.innerText = I18N[STATE.language].online_text;
  } else {
    badge.className = 'flex items-center space-x-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-100 text-amber-800 border border-amber-300 transition-all hover:scale-105';
    dot.className = 'w-2 h-2 rounded-full bg-amber-500';
    text.innerText = I18N[STATE.language].offline_text;
  }
}

function toggleSimulateOffline() {
  STATE.simulatedOffline = !STATE.simulatedOffline;
  updateNetworkUI();
  const msg = STATE.simulatedOffline 
    ? (STATE.language === 'swahili' ? '🔴 Umeingia hali ya Nje ya Mtandao (Offline). Majaribio na masomo yatafanya kazi kupitia Local Vault!' : '🔴 Offline simulation enabled. Tutor is running from local offline vault!')
    : (STATE.language === 'swahili' ? '🟢 Umerudi Mtandaoni (Online). Gemini 2.5 Flash imeunganishwa tena!' : '🟢 Back Online! Connected to Gemini 2.5 Flash backend.');
  
  appendSystemNotice(msg);
}

// Language Switching
function changeLanguage(lang) {
  STATE.language = lang;
  updateUIStrings();
  updateNetworkUI();
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
    // Fetch fresh copy from backend if online
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

  // If online -> send to backend API
  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        student_id: STATE.studentId,
        message: query,
        language: STATE.language,
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

  const isSw = STATE.language !== 'english';
  const title = isSw ? matched.title_sw : matched.title_en;
  const summary = isSw ? matched.summary_sw : matched.summary_en;
  const analogy = isSw ? matched.analogy_sw : matched.analogy_en;
  const exp = matched.experiment;
  const quiz = matched.quiz;

  const termsFormatted = matched.key_terms.map(t => `• **${t.en}** ➔ ${t.sw}`).join('\n');

  const text = `### 🔬 ${title}

${isSw ? 'Ufafanuzi kutoka kwenye Offline Vault (Bila Mtandao):' : 'Explanation from Local Offline Vault:'}

${summary}

---

#### 💡 Mfano Halisi (Everyday Analogy)
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

  div.innerHTML = `
    <div class="w-8 h-8 rounded-full bg-brand-600 flex items-center justify-center text-white text-sm flex-shrink-0 shadow">
      🌱
    </div>
    <div class="bg-white border border-slate-200 rounded-2xl rounded-tl-sm p-4 shadow-sm max-w-[85%] text-sm text-slate-800 space-y-3">
      ${isOffline ? '<span class="inline-block bg-amber-100 text-amber-800 text-[10px] font-bold px-2 py-0.5 rounded-full mb-1">📦 Imetoka Offline Vault</span>' : '<span class="inline-block bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded-full mb-1">✨ Gemini 2.5 Flash</span>'}
      <div class="stem-card leading-relaxed space-y-2">${formattedHtml}</div>
      
      <!-- Action Toolbar -->
      <div class="pt-2 border-t border-slate-100 flex flex-wrap gap-2 text-xs font-semibold">
        <button onclick="speakText('${encodeURIComponent(data.text)}')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-brand-50 hover:text-brand-700 text-slate-700 flex items-center space-x-1 transition-all">
          <span>🔊</span>
          <span>Sikiliza (TTS)</span>
        </button>
        <button onclick="executeAgentQuery('Eleza hili tena kwa urahisi zaidi kama kwa mtoto wa miaka 9', true)" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-brand-50 hover:text-brand-700 text-slate-700 flex items-center space-x-1 transition-all">
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
    <span class="bg-slate-200 text-slate-700 text-xs font-semibold px-3 py-1 rounded-full shadow-inner">
      ${text}
    </span>
  `;
  container.appendChild(div);
  container.scrollTop = container.scrollHeight;
}

function appendLoadingIndicator() {
  const container = document.getElementById('chatMessages');
  const id = 'loading_' + Date.now();
  const div = document.createElement('div');
  div.id = id;
  div.className = 'flex items-start space-x-3';
  div.innerHTML = `
    <div class="w-8 h-8 rounded-full bg-brand-600 flex items-center justify-center text-white text-sm flex-shrink-0 shadow animate-pulse">
      🌱
    </div>
    <div class="bg-white border border-slate-200 rounded-2xl rounded-tl-sm px-4 py-3 shadow-sm text-xs font-bold text-slate-500 flex items-center space-x-2">
      <span class="w-2 h-2 rounded-full bg-brand-600 animate-ping"></span>
      <span>Mwalimu anafikiri na kuandaa mfano mzuri...</span>
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
    // Set language
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

  container.innerHTML = STATE.offlineModules.map(m => `
    <div class="bg-white border border-slate-200 rounded-2xl p-4 shadow-sm space-y-3 hover:border-brand-500 transition-all flex flex-col justify-between">
      <div class="space-y-1.5">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-700">${m.subject}</span>
          <span class="text-xs text-brand-600 font-bold">📦 0 KB Offline</span>
        </div>
        <h3 class="font-bold text-slate-900 text-base">${isSw ? m.title_sw : m.title_en}</h3>
        <p class="text-xs text-slate-600 line-clamp-2">${isSw ? m.summary_sw : m.summary_en}</p>
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
  `).join('');
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
