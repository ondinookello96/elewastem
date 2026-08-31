/**
 * ElewaSTEM Pan-African Frontend Logic: 16+ African Languages, Multi-Stakeholder Feedback Loop & Cross-Border DPA Compliance Matrix
 */

// Application State
const STATE = {
  studentId: 'demo_student',
  language: localStorage.getItem('elewa_user_lang') || 'en',
  jurisdiction: 'KE',
  country: 'Kenya',
  subject: 'all',
  gradeLevel: 'Grade 6 (Upper Primary)',
  region: 'lake_basin',
  autoSpeak: true,
  screenReaderMode: true,
  signLanguageMode: true,
  dyslexiaMode: false,
  highContrast: false,
  textSize: 'normal',
  gpsCoords: null,
  dpaConsent: false,
  simulatedOffline: false,
  activeTab: 'chat',
  activeStakeholderSubTab: 'parents',
  agentMode: 'creative', // 'creative' (Temp 0.75) vs 'precise' (Temp 0.2)
  activeSpeechUtterance: null,
  activeSpeechRecognition: null,
  offlineModules: [],
  languagesMeta: {},
  jurisdictionsMeta: {},
  feedbackData: { total_feedback: 4, average_rating: 5.0, recent: [] },
  regionsMeta: {
    lake_basin: { name_sw: 'Kisumu & Ziwa Victoria', name_en: 'Lake Victoria Basin (Kisumu)', icon: '🏞️', desc_sw: 'Kisumu, Mwanza, Entebbe • Samaki Ngege & Mbuta, Magugu Maji (Akech), Osuga & Mitoo' },
    coastal: { name_sw: 'Pwani na Bahari', name_en: 'Coastal & Ocean (Mombasa/Lagos)', icon: '🌊', desc_sw: 'Mombasa, Kilifi, Zanzibar, Lagos • Minazi, mikoko ya kupumulia, chumvi' },
    highlands: { name_sw: 'Nyanda za Juu & Kilimo', name_en: 'Highlands & Farms', icon: '⛰️', desc_sw: 'Nakuru, Eldoret, Mt. Kenya, Ethiopian Highlands • Mashamba ya chai, mahindi, kahawa' },
    arid: { name_sw: 'Maeneo Kavu & Sahel', name_en: 'Arid & Pastoralist (Sahel/Kalahari)', icon: '☀️', desc_sw: 'Turkana, Garissa, Kano, Sahel • Miti ya acacia yenye nta, ngamia, solar boreholes' },
    urban: { name_sw: 'Mijini', name_en: 'Urban Centers (Nairobi, Lagos, Joburg)', icon: '🏙️', desc_sw: 'Nairobi, Lagos, Johannesburg, Accra • Taa za solar, matatu/danfo electronics' }
  },
  profile: {
    name: 'Mwanafunzi Hodari',
    grade_level: 'Grade 6',
    current_region: 'lake_basin',
    jurisdiction: 'KE',
    mastery_graph: {},
    badges: ['🌟 Mwanzo Bora (Great Start)']
  },
  currentQuiz: null
};

// UI Translations (Pure Single-Language per selected locale)
const I18N = {
  sw: {
    menu_btn: 'Menyu & Mipangilio',
    active_profile_label: 'Wasifu wa Mwanafunzi',
    learner_setup_title: '🎓 Mipangilio ya Masomo',
    subject_label: '📚 Somo:',
    grade_label: '🎓 Kiwango cha Masomo:',
    country_label: '🌍 Nchi:',
    language_label: '🗣️ Lugha ya Kujifunza:',
    region_label: '🏞️ Mazingira ya Eneo:',
    inclusion_title: '♿ Ujumuishi na Ufikiaji',
    inclusion_btn_title: 'Ujumuishi',
    inclusion_btn_sub: 'Kuona, Kusikia & Kujifunza',
    voice_label_on: 'Sauti: Washa',
    voice_label_off: 'Sauti: Zima',
    voice_btn_sub: 'Usomaji wa Sauti',
    thinking_mode_title: '🧠 Hali ya Kufikiri',
    thinking_mode_btn: 'Badili Hali',
    hubs_title: '📂 Masomo, Maendeleo & Wadau',
    hub_chat_title: 'Gumzo la Masomo',
    hub_chat_sub: 'Rudi kwenye ukurasa wa gumzo',
    hub_vault_title: 'Hifadhi ya Masomo (Offline Vault)',
    hub_vault_sub: 'Masomo makuu yanapatikana bila mtandao baada ya kusakinisha',
    hub_mastery_title: 'Maendeleo & Beji za Ushindi',
    hub_mastery_sub: 'Kiwango cha uelewa wa mada na beji',
    hub_stakeholders_title: 'Kituo cha Wadau & Maoni',
    hub_stakeholders_sub: 'Mipango ya walimu, SMS za wazazi na maoni',
    hub_privacy_title: 'Ulinzi wa Data za Kibinafsi',
    hub_privacy_sub: 'Sheria 8 za nchi za Afrika (DPA)',
    hub_languages_title: 'Lugha 16+ za Kiafrika',
    hub_languages_sub: 'Tathmini za Masakhane na Gemini Multilingual',
    hub_install_title: 'Sakinisha Programu',
    hub_install_sub: 'Weka kwenye simu, masomo makuu yanapatikana bila mtandao',
    feedback_btn: '💬 Toa Maoni',
    back_to_chat: 'Rudi kwenye Gumzo',
    welcome_title: 'Hujambo rafiki yangu! 🌟',
    welcome_text: 'Mimi ni ElewaSTEM—mwalimu wako wa Sayansi na Hesabu. Bonyeza kipaza sauti 🎤 kuongea au andika swali lako hapa chini!',
    welcome_chips_title: '💡 Mada za Kuanza:',
    input_placeholder: 'Ongea kwa sauti au andika swali lako...',
    online_text: 'Mtandaoni (AI Kamili)',
    offline_text: 'Nje ya Mtandao (Masomo Makuu)',
    listen_btn: '🔊 Sikiliza',
    simplify_btn: '💡 Rahisisha',
    quiz_btn: '🎯 Fanya Jaribio',
    vault_box_title: '📦 Hifadhi ya Masomo ya Sayansi',
    vault_box_sub: 'Masomo makuu ya sayansi yanapatikana bila mtandao baada ya kusakinisha.',
    profile_memory_desc: 'Mfumo unafuatilia maendeleo yako kote barani Afrika.',
    badges_earned_title: 'Beji Ulizoshinda',
    concept_mastery_title: 'Kiwango cha Uelewa kwa Mada',
    stakeholders_banner_title: 'Kituo cha Wadau wa Elimu & Mfumo wa Maoni',
    stakeholders_banner_sub: 'Kuunganisha Wazazi, Walimu, Vilabu vya Jamii na Wataalamu wa Mahitaji Maalum ili kutoa maoni endelevu na kuboresha elimu ya STEM.',
    privacy_banner_title: 'Ulinzi wa Data & Maadili ya AI',
    privacy_banner_sub: 'Kuzingatia sheria za ulinzi wa data za watoto na mifumo ya maadili ya AI barani Afrika.',
    subjects: {
      all: '🌟 Masomo Yote ya STEM',
      mathematics: '📐 Hisabati & Aljebra',
      biology: '🔬 Biolojia',
      physics: '⚡ Fizikia',
      chemistry: '⚗️ Kemia',
      computer_science: '💻 Sayansi ya Kompyuta',
      agriculture: '🌾 Kilimo & Mazingira'
    },
    grades: {
      'Grade 1-3 (Lower Primary)': '🌱 Darasa 1–3 (Msingi)',
      'Grade 6 (Upper Primary)': '🌿 Darasa 4–6 (CBC)',
      'Grade 7-9 (Junior Secondary)': '🔬 Darasa 7–9 (JSS)',
      'Grade 10-12 (Senior High)': '⚡ Kidato 3–4 (Upili)'
    },
    regions: {
      lake_basin: '🏞️ Ziwa Victoria & Kisumu',
      coastal: '🌊 Pwani na Bahari',
      highlands: '⛰️ Nyanda za Juu & Kilimo',
      arid: '☀️ Maeneo Kavu & Sahel',
      urban: '🏙️ Mijini'
    }
  },
  en: {
    menu_btn: 'Menu & Settings',
    active_profile_label: 'Active Profile',
    learner_setup_title: '🎓 Learner Settings',
    subject_label: '📚 Subject:',
    grade_label: '🎓 Grade Level:',
    country_label: '🌍 Country:',
    language_label: '🗣️ Learning Language:',
    region_label: '🏞️ Eco-Zone / Region:',
    inclusion_title: '♿ Universal Accessibility',
    inclusion_btn_title: 'Accessibility',
    inclusion_btn_sub: 'Visual, Hearing & Learning',
    voice_label_on: 'Voice: On',
    voice_label_off: 'Voice: Off',
    voice_btn_sub: 'Voice Reading',
    thinking_mode_title: '🧠 Thinking Mode',
    thinking_mode_btn: 'Switch Mode',
    hubs_title: '📂 Learning, Mastery & Stakeholders',
    hub_chat_title: 'Learner Chat',
    hub_chat_sub: 'Return to active learning chat',
    hub_vault_title: 'Offline Knowledge Vault',
    hub_vault_sub: 'Core learning modules available offline after installation/download',
    hub_mastery_title: 'Concept Mastery & Badges',
    hub_mastery_sub: 'Track topic scores and badges',
    hub_stakeholders_title: 'Stakeholder & Feedback Hub',
    hub_stakeholders_sub: 'Lesson plans, parent SMS digests and reviews',
    hub_privacy_title: 'Data Privacy & Legal Compliance',
    hub_privacy_sub: 'African data protection acts (DPA)',
    hub_languages_title: '16+ African Languages',
    hub_languages_sub: 'Masakhane & Gemini multilingual models',
    hub_install_title: 'Install App (PWA)',
    hub_install_sub: 'Install on phone, core modules work offline',
    feedback_btn: '💬 Feedback',
    back_to_chat: 'Back to Chat',
    welcome_title: 'Hello young scientist! 🌟',
    welcome_text: 'I am ElewaSTEM—your African STEM tutor. Tap the microphone 🎤 to speak, or type your question below!',
    welcome_chips_title: '💡 Try asking about:',
    input_placeholder: 'Speak into microphone or type your question...',
    online_text: 'Online (Full AI Cloud)',
    offline_text: 'Offline (Core Modules Available)',
    listen_btn: '🔊 Listen',
    simplify_btn: '💡 Simplify',
    quiz_btn: '🎯 Practice Quiz',
    vault_box_title: '📦 Core Offline Science Vault',
    vault_box_sub: 'Core learning modules available offline after installation/download.',
    profile_memory_desc: 'System tracks your concept mastery across African curriculum strands.',
    badges_earned_title: 'Badges Earned',
    concept_mastery_title: 'Concept Mastery Level',
    stakeholders_banner_title: 'Multi-Stakeholder Educational Hub & Feedback Loop',
    stakeholders_banner_sub: 'Connecting Parents, Teachers, Community Mentors, and Accessibility Advocates for continuous STEM improvement.',
    privacy_banner_title: 'Data Privacy & Responsible AI Matrix',
    privacy_banner_sub: 'Protecting children\'s data privacy and upholding ethical AI governance across Africa.',
    subjects: {
      all: '🌟 All STEM Subjects',
      mathematics: '📐 Mathematics & Algebra',
      biology: '🔬 Biology & Life Sciences',
      physics: '⚡ Physics & Energy',
      chemistry: '⚗️ Chemistry & Matter',
      computer_science: '💻 Computer Science & Coding',
      agriculture: '🌾 Agriculture & Environment'
    },
    grades: {
      'Grade 1-3 (Lower Primary)': '🌱 Grade 1–3 (Lower Primary)',
      'Grade 6 (Upper Primary)': '🌿 Grade 4–6 (Upper Primary)',
      'Grade 7-9 (Junior Secondary)': '🔬 Grade 7–9 (Junior Secondary)',
      'Grade 10-12 (Senior High)': '⚡ Grade 10–12 (Senior High)'
    },
    regions: {
      lake_basin: '🏞️ Lake Victoria Basin & Kisumu',
      coastal: '🌊 Coastal Mangroves & Marine',
      highlands: '⛰️ Agricultural Highlands',
      arid: '☀️ Arid ASAL & Sahel',
      urban: '🏙️ Urban Metropolises'
    }
  },
  sheng: {
    menu_btn: 'Menyu & Mipangilio',
    active_profile_label: 'Level Yangu',
    learner_setup_title: '🎓 Setup ya Masomo',
    subject_label: '📚 Somo:',
    grade_label: '🎓 Kiwango:',
    country_label: '🌍 Country:',
    language_label: '🗣️ Lugha:',
    region_label: '🏞️ Eneo:',
    inclusion_title: '♿ Ujumuishi',
    inclusion_btn_title: 'Ujumuishi',
    inclusion_btn_sub: 'Visual, Hearing & Learning',
    voice_label_on: 'Sauti: Washa',
    voice_label_off: 'Sauti: Zima',
    voice_btn_sub: 'Usomaji wa Sauti',
    thinking_mode_title: '🧠 Kufikiri',
    thinking_mode_btn: 'Badili Mode',
    hubs_title: '📂 Masomo & Wadau',
    hub_chat_title: 'Msee wa STEM',
    hub_chat_sub: 'Rudi kwenye chat',
    hub_vault_title: 'Masomo ya Offline',
    hub_vault_sub: 'Masomo makuu yanapatikana offline baada ya kudownload',
    hub_mastery_title: 'Level Yangu & Badges',
    hub_mastery_sub: 'Alama za mada na beji',
    hub_stakeholders_title: 'Wadau & Maoni',
    hub_stakeholders_sub: 'Walimu, wazazi na maoni',
    hub_privacy_title: 'Privacy ya Data',
    hub_privacy_sub: 'Sheria za data Afrika',
    hub_languages_title: 'Lugha 16+ za Afrika',
    hub_languages_sub: 'Masakhane & Gemini',
    hub_install_title: 'Weka kwa Simu',
    hub_install_sub: 'Weka kwa screen, masomo yapo offline',
    feedback_btn: '💬 Toa Maoni',
    back_to_chat: 'Rudi kwa Chat',
    welcome_title: 'Niaje msee wangu! 🌟',
    welcome_text: 'Mimi ni ElewaSTEM—ticha wako wa Sayansi na Maths. Bonga na mic 🎤 au type swali hapa chini!',
    welcome_chips_title: '💡 Anzia Hapa:',
    input_placeholder: 'Bonga na mic au type swali yako...',
    online_text: 'Online',
    offline_text: 'Offline (Masomo Makuu)',
    listen_btn: '🔊 Sikiza',
    simplify_btn: '💡 Fafanua zaidi',
    quiz_btn: '🎯 Cheza Quiz'
  },
  yo: {
    menu_btn: 'Ètò & Àkójọ',
    active_profile_label: 'Ìwé Ẹ̀kọ́ Rẹ',
    learner_setup_title: '🎓 Ètò Ẹ̀kọ́',
    subject_label: '📚 Kókó Ẹ̀kọ́:',
    grade_label: '🎓 Ipele:',
    country_label: '🌍 Orílẹ̀-èdè:',
    language_label: '🗣️ Èdè:',
    region_label: '🏞️ Agbègbè:',
    inclusion_title: '♿ Àwọn Àìní Pàtàkì',
    inclusion_btn_title: 'Àìní Pàtàkì',
    inclusion_btn_sub: 'Ìríran, Ìgbọ́ran & Ẹ̀kọ́',
    voice_label_on: 'Ohùn: Tan',
    voice_label_off: 'Ohùn: Pa',
    voice_btn_sub: 'Kíkà Ohùn',
    thinking_mode_title: '🧠 Ọ̀nà Ìrònú',
    thinking_mode_btn: 'Yípadà',
    hubs_title: '📂 Ẹ̀kọ́ & Ìlọsíwájú',
    hub_chat_title: 'Olùkọ́ STEM',
    hub_chat_sub: 'Padà sí ìfọ̀rọ̀wérọ̀',
    hub_vault_title: 'Ẹ̀kọ́ Àìlórí Ayélujára',
    hub_vault_sub: 'Àwọn ẹ̀kọ́ pàtàkì wà lárọ̀ọ́wọ́tó láìsí ayélujára lẹ́yìn ìfipamọ́',
    hub_mastery_title: 'Ìlọsíwájú & Àwọn Àmì',
    hub_mastery_sub: 'Àwọn àmì ẹ̀kọ́ rẹ',
    hub_stakeholders_title: 'Àwọn Olùkópa & Èsì',
    hub_stakeholders_sub: 'Àwọn olùkọ́ & àwọn òbí',
    hub_privacy_title: 'Ààbò Data',
    hub_privacy_sub: 'Òfin ààbò data ní Áfíríkà',
    hub_languages_title: 'Àwọn Èdè Áfíríkà 16+',
    hub_languages_sub: 'Masakhane & Gemini',
    hub_install_title: 'Fi Sori Fóònù',
    hub_install_sub: 'Fi sori iboju fóònù, àwọn ẹ̀kọ́ wà láìsí ayélujára',
    feedback_btn: '💬 Fi Èsì Ránṣẹ́',
    back_to_chat: 'Padà sí Ìfọ̀rọ̀wérọ̀',
    welcome_title: 'Báwo ọ̀rẹ́ mi! 🌟',
    welcome_text: 'Èmi ni ElewaSTEM—olùkọ́ rẹ fún STEM. Tẹ maiki 🎤 tàbí kọ ìbéèrè rẹ ní ìsàlẹ̀!',
    welcome_chips_title: '💡 Àwọn Àkòrí Ìbẹ̀rẹ̀:',
    input_placeholder: 'Sọ̀rọ̀ sínú mic tàbí kọ ìbéèrè rẹ...',
    online_text: 'Lórí Ayélujára',
    offline_text: 'Àìlórí Ayélujára (Ẹ̀kọ́ Pàtàkì)',
    listen_btn: '🔊 Gbọ́',
    simplify_btn: '💡 Ṣe àlàyé',
    quiz_btn: '🎯 Ṣe Ìdánwò'
  },
  ha: {
    menu_btn: 'Menu & Saituna',
    active_profile_label: 'Bayanin Dalibi',
    learner_setup_title: '🎓 Saitin Koyo',
    subject_label: '📚 Darasi:',
    grade_label: '🎓 Mataki:',
    country_label: '🌍 Kasa:',
    language_label: '🗣️ Harshe:',
    region_label: '🏞️ Yanki:',
    inclusion_title: '♿ Bukatu Na Musamman',
    inclusion_btn_title: 'Samun Dama',
    inclusion_btn_sub: 'Saukin Gani, Ji da Koyo',
    voice_label_on: 'Murya: Kunna',
    voice_label_off: 'Murya: Kashe',
    voice_btn_sub: 'Karatun Murya',
    thinking_mode_title: '🧠 Yanayin Tunani',
    thinking_mode_btn: 'Sauya Yanayi',
    hubs_title: '📂 Karatu & Ci gaba',
    hub_chat_title: 'Malamin STEM',
    hub_chat_sub: 'Koma zuwa hira',
    hub_vault_title: 'Karatun Ba Intanet',
    hub_vault_sub: 'Babban karatun yana samuwa ba tare da intanet ba bayan saukewa',
    hub_mastery_title: 'Ci gaba & Lambobin Yabo',
    hub_mastery_sub: 'Matsayin fahimtar darussa',
    hub_stakeholders_title: 'Masu Ruwa da Tsaki',
    hub_stakeholders_sub: 'Malamai, iyaye da ra\'ayoyi',
    hub_privacy_title: 'Kariyar Bayanai',
    hub_privacy_sub: 'Dokokin kariyar bayanai a Afirka',
    hub_languages_title: 'Harsunan Afirka 16+',
    hub_languages_sub: 'Masakhane & Gemini',
    hub_install_title: 'Sanya a Waya',
    hub_install_sub: 'Sanya a fuskar waya, babban karatu yana aiki ba intanet',
    feedback_btn: '💬 Bayar da Ra\'ayi',
    back_to_chat: 'Koma zuwa Hira',
    welcome_title: 'Sannu abokina! 🌟',
    welcome_text: 'Ni ne ElewaSTEM—malamin ka na STEM. Danna makirufo 🎤 ko rubuta tambayarka a kasa!',
    welcome_chips_title: '💡 Batutuwan Farko:',
    input_placeholder: 'Yi magana ta mic ko rubuta tambaya...',
    online_text: 'A Layi',
    offline_text: 'Ba Intanet (Babban Karatu)',
    listen_btn: '🔊 Saurara',
    simplify_btn: '💡 Saukake',
    quiz_btn: '🎯 Yi Tambayoyi'
  },
  ig: {
    menu_btn: 'Menu & Ntọala',
    active_profile_label: 'Profaịlụ Nwa Akwụkwọ',
    learner_setup_title: '🎓 Ntọala Ọmụmụ',
    subject_label: '📚 Isiokwu:',
    grade_label: '🎓 Ọkwa:',
    country_label: '🌍 Obodo:',
    language_label: '🗣️ Asụsụ:',
    region_label: '🏞️ Mpaghara:',
    inclusion_title: '♿ Mkpa Pụrụ Iche',
    inclusion_btn_title: 'Nnweta',
    inclusion_btn_sub: 'Ịhụ Ụzọ, Ịnụ Ihe na Mmụta',
    voice_label_on: 'Olu: Gbanwuo',
    voice_label_off: 'Olu: Gbanyụọ',
    voice_btn_sub: 'Ọgụgụ Olu',
    thinking_mode_title: '🧠 Ụdị Echiche',
    thinking_mode_btn: 'Gbanwee Ụdị',
    hubs_title: '📂 Ọmụmụ & Ọganihu',
    hub_chat_title: 'Onye Nkuzi STEM',
    hub_chat_sub: 'Laghachi na nkata',
    hub_vault_title: 'Ihe Ọmụmụ Offline',
    hub_vault_sub: 'Isi ihe ọmụmụ dị na-enweghị ịntanetị mgbe e budatara ya',
    hub_mastery_title: 'Ọganihu & Baajị',
    hub_mastery_sub: 'Ọkwa nghọta nke isiokwu',
    hub_stakeholders_title: 'Ndị Metụtara & Nzaghachi',
    hub_stakeholders_sub: 'Ndị nkuzi, ndị nne na nna',
    hub_privacy_title: 'Nchedo Data',
    hub_privacy_sub: 'Iwu nchedo data na Afrịka',
    hub_languages_title: 'Asụsụ Afrịka 16+',
    hub_languages_sub: 'Masakhane & Gemini',
    hub_install_title: 'Wụnye na Ekwentị',
    hub_install_sub: 'Wụnye na ekwentị, isi ihe ọmụmụ dị offline',
    feedback_btn: '💬 Nye Nzaghachi',
    back_to_chat: 'Laghachi na Nkata',
    welcome_title: 'Ndewo enyi m! 🌟',
    welcome_text: 'Abụ m ElewaSTEM—onye nkuzi gị maka STEM. Pịa mic 🎤 ma ọ bụ dee ajụjụ gị n\'okpuru!',
    welcome_chips_title: '💡 Isiokwu Mmalite:',
    input_placeholder: 'Kwuo okwu na mic ma ọ bụ dee ajụjụ...',
    online_text: 'N\'ịntanetị',
    offline_text: 'Ọnọdụ Offline (Isi Ihe)',
    listen_btn: '🔊 Gee ntị',
    simplify_btn: '💡 Mee ka ọ dị mfe',
    quiz_btn: '🎯 Mee Nnwale'
  },
  pcm: {
    menu_btn: 'Menu & Settings',
    active_profile_label: 'Student Profile',
    learner_setup_title: '🎓 Learning Settings',
    subject_label: '📚 Subject:',
    grade_label: '🎓 Class Level:',
    country_label: '🌍 Country:',
    language_label: '🗣️ Language:',
    region_label: '🏞️ Area:',
    inclusion_title: '♿ Special Support',
    inclusion_btn_title: 'Accessibility',
    inclusion_btn_sub: 'Visual, Hearing & Learning',
    voice_label_on: 'Voice: On',
    voice_label_off: 'Voice: Off',
    voice_btn_sub: 'Voice Reading',
    thinking_mode_title: '🧠 Thinking Mode',
    thinking_mode_btn: 'Change Mode',
    hubs_title: '📂 Study & Progress',
    hub_chat_title: 'STEM Ticha',
    hub_chat_sub: 'Go back to chat',
    hub_vault_title: 'Offline Lessons',
    hub_vault_sub: 'Core learning modules available offline after installation/download',
    hub_mastery_title: 'My Progress & Badges',
    hub_mastery_sub: 'Topic scores and badges',
    hub_stakeholders_title: 'Stakeholders & Feedback',
    hub_stakeholders_sub: 'Teachers, parents and feedback',
    hub_privacy_title: 'Data Privacy',
    hub_privacy_sub: 'African data laws',
    hub_languages_title: '16+ African Languages',
    hub_languages_sub: 'Masakhane & Gemini',
    hub_install_title: 'Install for Phone',
    hub_install_sub: 'Put am for phone screen, core lessons work offline',
    feedback_btn: '💬 Give Feedback',
    back_to_chat: 'Go Back to Chat',
    welcome_title: 'How far my friend! 🌟',
    welcome_text: 'I be ElewaSTEM—your STEM tutor. Tap the mic 🎤 or type your question below!',
    welcome_chips_title: '💡 Topics to Start:',
    input_placeholder: 'Talk for mic or type your question...',
    online_text: 'Online',
    offline_text: 'Offline (Core Lessons)',
    listen_btn: '🔊 Listen',
    simplify_btn: '💡 Break am down',
    quiz_btn: '🎯 Take Quiz'
  }
};



// Regional Quick Prompt Templates
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
  loadSavedPreferences();
  applyAccessibilityClasses();
  await loadOfflinePack();
  await loadLanguagesAndJurisdictions();
  changeLanguage(STATE.language);
  await refreshProfile();
  await loadFeedbackFeed();
  renderRegionUI();
  renderVault();
  updateUIStrings();
  updateAutoSpeakUI();
  loadTeacherLessonPlan('photosynthesis');
  renderCommunityActivities();
  renderJurisdictionDetails(STATE.jurisdiction);
  updateHeaderStatusPill();
  initDynamicPlaceholder();
  selectLearnerSubject('Biology');

  const input = document.getElementById('userInput');
  if (input) {
    input.addEventListener('focus', () => {
      setTimeout(() => {
        const container = document.getElementById('chatMessages');
        if (container) container.scrollTop = container.scrollHeight;
      }, 300);
    });
  }
});


// Network Connectivity
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
  const langDict = I18N[STATE.language] || I18N.sw;

  if (badge && dot && text) {
    if (online) {
      badge.className = 'flex items-center space-x-1 px-2 sm:px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800 border border-emerald-300 transition-all hover:scale-105';
      dot.className = 'w-2 h-2 rounded-full bg-emerald-500 animate-pulse';
      text.innerText = langDict.online_text;
    } else {
      badge.className = 'flex items-center space-x-1 px-2 sm:px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-100 text-amber-800 border border-amber-300 transition-all hover:scale-105';
      dot.className = 'w-2 h-2 rounded-full bg-amber-500';
      text.innerText = langDict.offline_text;
    }
  }
}

function toggleSimulateOffline() {
  STATE.simulatedOffline = !STATE.simulatedOffline;
  updateNetworkUI();
  const reg = STATE.regionsMeta[STATE.region] || STATE.regionsMeta.lake_basin;
  const msg = STATE.simulatedOffline 
    ? `🔴 Offline mode active: Core learning modules available offline for ${reg.name_sw}!` 
    : `🟢 Back Online! Connected to Gemini 2.5 Flash Pan-African backend.`;
  
  appendSystemNotice(msg);
}

// Languages & Privacy Jurisdictions Fetcher
async function loadLanguagesAndJurisdictions() {
  try {
    if (isEffectivelyOnline()) {
      const [langRes, jurRes] = await Promise.all([
        fetch('/api/languages'),
        fetch('/api/privacy/jurisdictions')
      ]);
      if (langRes.ok) {
        const langs = await langRes.json();
        langs.forEach(l => STATE.languagesMeta[l.code] = l);
      }
      if (jurRes.ok) {
        const jurs = await jurRes.json();
        jurs.forEach(j => STATE.jurisdictionsMeta[j.country === 'Pan-African Union' ? 'AU_CONTINENTAL' : j.country.substring(0,2).toUpperCase()] = j);
      }
    }
  } catch (err) {
    console.log('Language & Privacy fetch notice:', err);
  }
}

// Multi-Stakeholder Feedback Management
function openFeedbackModal(defaultRole = 'student') {
  const modal = document.getElementById('feedbackModal');
  const roleSelect = document.getElementById('fbStakeholderType');
  const title = document.getElementById('feedbackModalTitle');
  if (roleSelect) roleSelect.value = defaultRole;

  if (title) {
    const titles = {
      student: 'Toa Maoni ya Mwanafunzi (Learner Feedback)',
      parent: 'Toa Maoni ya Mzazi (Parent Feedback)',
      teacher: 'Toa Maoni ya Mwalimu (Teacher Feedback)',
      community_mentor: 'Ripoti ya Klabu ya Sayansi (Mentor Report)',
      accessibility_advocate: 'Maoni ya Ujumuishi (Accessibility Feedback)'
    };
    title.innerText = titles[defaultRole] || 'Toa Maoni Yako (Stakeholder Feedback)';
  }

  if (modal) modal.classList.remove('hidden');
}

function closeFeedbackModal() {
  const modal = document.getElementById('feedbackModal');
  if (modal) modal.classList.add('hidden');
}

async function submitFeedbackForm(e) {
  if (e) e.preventDefault();
  const role = document.getElementById('fbStakeholderType').value;
  const category = document.getElementById('fbCategory').value;
  const ratingEls = document.getElementsByName('fbRating');
  let rating = 5;
  for (let r of ratingEls) {
    if (r.checked) { rating = parseInt(r.value); break; }
  }
  const comment = document.getElementById('fbComment').value.trim();
  if (!comment) return;

  const payload = {
    stakeholder_type: role,
    student_id: STATE.studentId,
    region: STATE.region,
    language: STATE.language,
    rating: rating,
    category: category,
    comment: comment,
    topic: 'Continuous Feedback'
  };

  try {
    if (isEffectivelyOnline()) {
      const res = await fetch('/api/feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      if (res.ok) {
        alert('🎉 Asante sana! Maoni yako yamerekodiwa kwa mafanikio.');
      }
    } else {
      alert('📦 Maoni yako yamehifadhiwa kwenye kumbukumbu ya simu na yatatumwa punde mtandao utakaporejea!');
    }
  } catch (err) {
    console.log('Feedback submit error:', err);
  }

  closeFeedbackModal();
  document.getElementById('fbComment').value = '';
  await loadFeedbackFeed();
  appendSystemNotice(`💬 <b>Asante kwa Maoni:</b> "${comment.substring(0, 50)}..."`);
}

async function loadFeedbackFeed() {
  try {
    if (isEffectivelyOnline()) {
      const [recentRes, summaryRes] = await Promise.all([
        fetch('/api/feedback/recent'),
        fetch('/api/feedback/summary')
      ]);

      if (recentRes.ok && summaryRes.ok) {
        const recent = await recentRes.json();
        const summary = await summaryRes.json();
        renderFeedbackFeed(recent, summary);
      }
    }
  } catch (e) {
    console.log('Feedback feed load notice:', e);
  }
}

function renderFeedbackFeed(recentList, summary) {
  const container = document.getElementById('recentFeedbackList');
  const countEl = document.getElementById('totalFeedbackCount');
  const ratingEl = document.getElementById('avgFeedbackRating');

  if (countEl) countEl.innerText = summary.total_feedback || recentList.length;
  if (ratingEl) ratingEl.innerText = `${summary.average_rating || 5.0} ⭐`;

  if (!container) return;

  const roleBadges = {
    student: { text: '🎓 Mwanafunzi', color: 'bg-emerald-100 text-emerald-800' },
    parent: { text: '👨‍👩‍👧 Mzazi', color: 'bg-purple-100 text-purple-800' },
    teacher: { text: '👩‍🏫 Mwalimu', color: 'bg-blue-100 text-blue-800' },
    community_mentor: { text: '🤝 Mshauri wa Klabu', color: 'bg-amber-100 text-amber-800' },
    accessibility_advocate: { text: '♿ Mtaalamu wa Mahitaji', color: 'bg-teal-100 text-teal-800' }
  };

  container.innerHTML = recentList.map(item => {
    const role = roleBadges[item.stakeholder_type] || roleBadges.student;
    return `
      <div class="bg-slate-50 border border-slate-200 rounded-xl p-3 text-xs space-y-1.5 shadow-sm">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-1.5">
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full ${role.color}">${role.text}</span>
            <span class="text-amber-500 font-bold">${'⭐'.repeat(item.rating || 5)}</span>
          </div>
          <span class="text-[9px] text-slate-400 font-mono">${new Date(item.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
        </div>
        <p class="text-slate-800 italic">"${escapeHtml(item.comment)}"</p>
        <div class="text-[10px] text-slate-500 font-semibold flex items-center space-x-2">
          <span>📍 Eneo: ${item.region || 'Kisumu'}</span>
          <span>•</span>
          <span>Mada: ${escapeHtml(item.topic || 'General')}</span>
        </div>
      </div>
    `;
  }).join('');
}

function quickReact(emoji, topic) {
  const commentMap = {
    'understood': 'Nimeelewa vizuri sana!',
    'simplify': 'Tafadhali ninaomba unieleze kwa mifano rahisi zaidi ya mazingira yangu.',
    'voice': 'Asante kwa maelezo ya sauti!'
  };

  const payload = {
    stakeholder_type: 'student',
    student_id: STATE.studentId,
    region: STATE.region,
    language: STATE.language,
    rating: emoji === 'understood' ? 5 : 4,
    category: 'content_clarity',
    comment: commentMap[emoji] || 'Maoni ya haraka',
    topic: topic || 'Chat Reaction'
  };

  fetch('/api/feedback', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  }).then(() => {
    appendSystemNotice(`✨ <b>Maoni Yamepokelewa:</b> ${commentMap[emoji]}`);
    loadFeedbackFeed();
  }).catch(() => {});
}

// Universal Accessibility Controls
function openA11yModal() {
  document.getElementById('a11yModal').classList.remove('hidden');
}

function closeA11yModal() {
  document.getElementById('a11yModal').classList.add('hidden');
}

function toggleScreenReaderMode() {
  STATE.screenReaderMode = !STATE.screenReaderMode;
  localStorage.setItem('elewa_screen_reader', STATE.screenReaderMode ? 'true' : 'false');
  const btn = document.getElementById('screenReaderToggleBtn');
  if (btn) {
    btn.innerText = STATE.screenReaderMode ? 'Imewashwa' : 'Washa';
    btn.className = STATE.screenReaderMode ? 'px-2.5 py-1 rounded-lg text-xs font-bold bg-blue-600 text-white' : 'px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-200 text-slate-800';
  }
  renderVault();
}

function toggleSignLanguageMode() {
  STATE.signLanguageMode = !STATE.signLanguageMode;
  localStorage.setItem('elewa_sign_lang', STATE.signLanguageMode ? 'true' : 'false');
  const btn = document.getElementById('signLangToggleBtn');
  if (btn) {
    btn.innerText = STATE.signLanguageMode ? 'Imewashwa' : 'Washa';
    btn.className = STATE.signLanguageMode ? 'px-2.5 py-1 rounded-lg text-xs font-bold bg-emerald-600 text-white' : 'px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-200 text-slate-800';
  }
  renderVault();
}

function toggleDyslexiaMode() {
  STATE.dyslexiaMode = !STATE.dyslexiaMode;
  localStorage.setItem('elewa_dyslexia', STATE.dyslexiaMode ? 'true' : 'false');
  applyAccessibilityClasses();
  const btn = document.getElementById('dyslexiaToggleBtn');
  if (btn) {
    btn.innerText = STATE.dyslexiaMode ? 'Imewashwa' : 'Washa';
    btn.className = STATE.dyslexiaMode ? 'px-2.5 py-1 rounded-lg text-xs font-bold bg-amber-600 text-white' : 'px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-200 text-slate-800';
  }
}

function toggleHighContrast() {
  STATE.highContrast = !STATE.highContrast;
  localStorage.setItem('elewa_high_contrast', STATE.highContrast ? 'true' : 'false');
  applyAccessibilityClasses();
  const btn = document.getElementById('highContrastBtn');
  if (btn) {
    btn.innerText = STATE.highContrast ? 'Imewashwa' : 'Washa';
    btn.className = STATE.highContrast ? 'px-2.5 py-1 rounded-lg text-xs font-bold bg-yellow-400 text-black' : 'px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-200 text-slate-800';
  }
}

function setTextSize(size) {
  STATE.textSize = size;
  localStorage.setItem('elewa_text_size', size);
  applyAccessibilityClasses();
}

function applyAccessibilityClasses() {
  const body = document.getElementById('appBody');
  if (!body) return;

  if (STATE.dyslexiaMode) {
    body.classList.add('dyslexia-mode');
  } else {
    body.classList.remove('dyslexia-mode');
  }

  if (STATE.highContrast) {
    body.classList.add('high-contrast');
  } else {
    body.classList.remove('high-contrast');
  }

  body.classList.remove('text-size-lg', 'text-size-xl');
  if (STATE.textSize === 'lg') body.classList.add('text-size-lg');
  if (STATE.textSize === 'xl') body.classList.add('text-size-xl');
}

// Voice Auto-Speak Toggle
function toggleAutoSpeak() {
  STATE.autoSpeak = !STATE.autoSpeak;
  localStorage.setItem('elewa_auto_speak', STATE.autoSpeak ? 'true' : 'false');
  updateAutoSpeakUI();

  if (STATE.autoSpeak) {
    speakText('Sauti imewashwa! Mwalimu atakusomea majibu kiotomatiki.');
  } else {
    if ('speechSynthesis' in window) window.speechSynthesis.cancel();
  }
}

function updateAutoSpeakUI() {
  const btn = document.getElementById('autoSpeakBtn');
  const icon = document.getElementById('autoSpeakIcon');
  const text = document.getElementById('autoSpeakText');

  if (btn && icon && text) {
    if (STATE.autoSpeak) {
      btn.className = 'flex items-center space-x-1 px-2 sm:px-2.5 py-1 rounded-lg text-xs font-bold bg-purple-100 text-purple-900 border border-purple-400 hover:bg-purple-200 transition-all';
      icon.innerText = '🔊';
      text.innerText = 'Sauti: Washa';
    } else {
      btn.className = 'flex items-center space-x-1 px-2 sm:px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-500 border border-slate-300 hover:bg-slate-200 transition-all';
      icon.innerText = '🔇';
      text.innerText = 'Sauti: Zima';
    }
  }
}

// Privacy & Preferences Handlers
function loadSavedPreferences() {
  STATE.dpaConsent = (localStorage.getItem('elewa_dpa_consent') === 'granted');
  const savedRegion = localStorage.getItem('elewa_user_region');
  if (savedRegion && STATE.regionsMeta[savedRegion]) STATE.region = savedRegion;

  const savedLang = localStorage.getItem('elewa_user_lang');
  if (savedLang) {
    STATE.language = savedLang;
    const select = document.getElementById('langSelect');
    if (select) select.value = savedLang;
    const hSelect = document.getElementById('headerLangSelect');
    if (hSelect) hSelect.value = savedLang;
    const hFlag = document.getElementById('headerLangFlag');
    if (hFlag && STATE.languagesMeta[savedLang]?.flag) {
      hFlag.innerText = STATE.languagesMeta[savedLang].flag;
    }
  }

  if (localStorage.getItem('elewa_auto_speak') !== null) {
    STATE.autoSpeak = (localStorage.getItem('elewa_auto_speak') === 'true');
  }
  if (localStorage.getItem('elewa_dyslexia') !== null) {
    STATE.dyslexiaMode = (localStorage.getItem('elewa_dyslexia') === 'true');
  }
  if (localStorage.getItem('elewa_high_contrast') !== null) {
    STATE.highContrast = (localStorage.getItem('elewa_high_contrast') === 'true');
  }
  if (localStorage.getItem('elewa_text_size')) {
    STATE.textSize = localStorage.getItem('elewa_text_size');
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
  appendSystemNotice('🛡️ <b>Pan-African DPA:</b> Idhini ya GPS imefutwa.');
}

function executeGPSScan() {
  if (!('geolocation' in navigator)) {
    alert('Kifaa chako hakina GPS.');
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

      const detectedRegion = mapCoordinatesToEcoRegion(lat, lon);
      selectRegion(detectedRegion);

      const reg = STATE.regionsMeta[detectedRegion];
      appendSystemNotice(`🎯 <b>GPS Auto-Detect (DPA Protected):</b> [${lat.toFixed(2)}, ${lon.toFixed(2)}] ➔ ${reg.icon} <b>${reg.name_sw}</b>.`);
    },
    (error) => {
      if (gpsBtn) gpsBtn.classList.remove('bg-amber-400', 'animate-pulse');
      appendSystemNotice(`📍 Hatujaweza kusoma GPS. Unaweza kuchagua eneo kwenye orodha!`);
      openRegionModal();
    },
    { enableHighAccuracy: true, timeout: 8000, maximumAge: 60000 }
  );
}

function mapCoordinatesToEcoRegion(lat, lon) {
  if (lon >= 31.0 && lon <= 35.2 && lat >= -3.5 && lat <= 2.5) return 'lake_basin';
  if (lon > 38.5 && lat < 1.0 && lat > -11.0) return 'coastal';
  if ((lat > 1.2 && lon > 35.0) || (lat < -4.5 && lon < 37.0 && lon > 34.0)) return 'arid';
  if (lat >= -1.45 && lat <= -1.15 && lon >= 36.65 && lon <= 37.10) return 'urban';
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
  loadTeacherLessonPlan(document.getElementById('teacherTopicSelect')?.value || 'photosynthesis');
  renderCommunityActivities();
  updateParentDigestPreview();

  const reg = STATE.regionsMeta[regionKey];
  appendSystemNotice(`📍 Mazingira ya eneo yamebadilishwa kuwa: <b>${reg.icon} ${reg.name_sw}</b>.`);
}

function renderRegionUI() {
  const reg = STATE.regionsMeta[STATE.region] || STATE.regionsMeta.lake_basin;
  const isSw = STATE.language !== 'en';

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

  const chipsContainer = document.getElementById('quickLocationChips');
  if (chipsContainer) {
    const chips = (STATE.subject && STATE.subject !== 'all' && SUBJECT_PROMPT_CHIPS[STATE.subject]) 
      ? SUBJECT_PROMPT_CHIPS[STATE.subject] 
      : (REGIONAL_PROMPT_CHIPS[STATE.region] || REGIONAL_PROMPT_CHIPS.lake_basin);
    chipsContainer.innerHTML = chips.map(c => `
      <button onclick="sendQuickPrompt('${escapeHtml(c.query)}')" class="quick-chip bg-emerald-50 text-emerald-800 border border-emerald-300 px-2.5 py-1 rounded-full text-xs hover:bg-emerald-100 font-medium transition-all">
        ${c.title}
      </button>
    `).join('');
  }
}

const SUBJECT_PROMPT_CHIPS = {
  all: [
    { title: '🌿 Usanisinuru (Biology)', query: 'Nieleze kuhusu Usanisinuru na jinsi mimea inavyopika chakula' },
    { title: '⚡ Saketi za Umeme (Physics)', query: 'Nieleze kuhusu saketi kamili za umeme' },
    { title: '⚗️ Asidi na Besi (Chemistry)', query: 'Nieleze kuhusu kemia ya asidi, ndimu na majivu' },
    { title: '📐 Sehemu & Uwiano (Math)', query: 'Nieleze kuhusu sehemu za hesabu na jinsi ya kugawa' },
    { title: '💻 Algoriti & Mantiki (CS)', query: 'Nieleze kuhusu algoriti za kompyuta na roboti' }
  ],
  biology: [
    { title: '🌿 Usanisinuru & Oksijeni', query: 'Nieleze jinsi mimea inavyotumia jua kupika chakula na kutoa oksijeni' },
    { title: '🐟 Yavuyavu za Samaki', query: 'Nieleze jinsi samaki wanavyotumia mashavu yao kupumua majini' },
    { title: '🌾 Mboga za Asili & Mimea', query: 'Nieleze muundo wa majani ya mboga za kienyeji na klorofili' }
  ],
  physics: [
    { title: '💡 Saketi za Taa & Betri', query: 'Nieleze jinsi ya kutengeneza saketi kamili ya umeme wa betri na taa' },
    { title: '🌍 Mvuto na Msuguano', query: 'Nieleze nguvu ya mvuto na jinsi msuguano unavyosaidia breki za baiskeli' },
    { title: '☀️ Paneli za Jua (Solar PV)', query: 'Nieleze jinsi mwangaza wa jua unavyobadilishwa kuwa umeme wa solar' }
  ],
  chemistry: [
    { title: '🧪 Asidi, Siki na Ndimu', query: 'Nieleze sifa za asidi kama maji ya ndimu au siki' },
    { title: '🥄 Besi, Majivu na Soda', query: 'Nieleze sifa za besi kama majivu ya jikoni au baking soda' },
    { title: '💥 Volkano ya Jikoni (CO₂)', query: 'Nieleze mmenyuko wa asidi na besi unaotoa gesi ya kaboni' }
  ],
  mathematics: [
    { title: '🍕 Sehemu (1/4, 1/2, 3/4)', query: 'Nieleze jinsi ya kuelewa sehemu za nambari kama robo na nusu' },
    { title: '📊 Uwiano & Mgawanyo', query: 'Nieleze jinsi ya kugawa samaki au mavuno kwa uwiano sawa' },
    { title: '📐 Eneo na Mzingo (Area)', query: 'Nieleze jinsi ya kupima eneo la shamba la mstatili' }
  ],
  computer_science: [
    { title: '🤖 Algoriti za Maamuzi (If-Else)', query: 'Nieleze jinsi kompyuta inavyofanya maamuzi kwa kutumia If-Else' },
    { title: '💧 Smart Irrigation Logic', query: 'Nieleze jinsi ya kuandika mpango wa kuwasha pampu ya maji kiotomatiki' },
    { title: '📱 Binary & Logic Gates', query: 'Nieleze jinsi swichi za umeme zinavyoendesha programu za simu' }
  ],
  agriculture: [
    { title: '🌱 Afya ya Udongo na pH', query: 'Nieleze jinsi asidi ya udongo inavyoathiri mavuno ya mahindi' },
    { title: '☀️ Uhifadhi wa Maji ya Kilimo', query: 'Nieleze mbinu za kuhifadhi maji shambani wakati wa kiangazi' },
    { title: '🦗 Udhibiti wa Wadudu Kiasili', query: 'Nieleze sayansi ya kuzuia wadudu waharibifu kwa kutumia mimea' }
  ]
};

// 53 Comprehensive STEM Modules Grouped by Subject for Direct Learner Topic Selection
const CURRICULUM_SUBJECT_TOPICS = {
  'Biology': [
    { id: 'photosynthesis', title_sw: '1. Usanisinuru: Mimea Inavyotengeneza Chakula', title_en: '1. Photosynthesis: Plant Food Making', icon: '🌿' },
    { id: 'human_digestive_system', title_sw: "2. Mfumo wa Mmeng'enyo wa Chakula & Lishe", title_en: '2. Digestive System & Nutrition', icon: '🍎' },
    { id: 'circulatory_heart', title_sw: '3. Moyo na Mzunguko wa Damu Mwilini', title_en: '3. Human Heart & Blood Circulation', icon: '🫀' },
    { id: 'human_respiration', title_sw: '4. Mfumo wa Upumuaji na Mapafu', title_en: '4. Respiratory System & Lungs', icon: '🫁' },
    { id: 'cell_biology', title_sw: '5. Muundo wa Seli: Mmea na Mnyama', title_en: '5. Cell Biology: Plant vs Animal', icon: '🔬' },
    { id: 'plant_pollination', title_sw: '6. Uchavushaji wa Maua & Uzalishaji', title_en: '6. Flower Pollination & Reproduction', icon: '🌸' },
    { id: 'living_things_classification', title_sw: '7. Uainishaji wa Viumbe: Uti wa Mgongo', title_en: '7. Classification: Vertebrates & Invertebrates', icon: '🦁' },
    { id: 'ecology_food_chains', title_sw: '8. Mnyororo wa Chakula & Ikolojia', title_en: '8. Ecology & Food Chains', icon: '🌾' },
    { id: 'aquatic_biology_kisumu', title_sw: '9. Upumuaji wa Samaki & Yavuyavu (Gills)', title_en: '9. Aquatic Respiration & Fish Biology', icon: '🐟' },
    { id: 'human_excretion_kidney', title_sw: '10. Figo & Mfumo wa Kutoa Taka', title_en: '10. Excretory System: Kidneys', icon: '💧' },
    { id: 'nervous_sense_organs', title_sw: '11. Mfumo wa Fahamu & Milango ya Hisia', title_en: '11. Nervous System & Sense Organs', icon: '🧠' },
    { id: 'plant_transpiration_transport', title_sw: '12. Mvuke wa Mimea & Xylem/Phloem', title_en: '12. Plant Transpiration & Transport', icon: '🌱' },
    { id: 'skeletal_muscular_system', title_sw: '13. Mifupa na Misuli: Mwendo wa Mwili', title_en: '13. Skeletal & Muscular System', icon: '🦴' },
    { id: 'microorganisms_health', title_sw: '14. Vijidudu, Kingamwili na Usafi', title_en: '14. Microorganisms, Immunity & Hygiene', icon: '🦠' },
    { id: 'genetics_dna_heredity', title_sw: '15. Jenetiki, DNA & Urithi wa Tabia', title_en: '15. Genetics, DNA & Heredity Traits', icon: '🧬' }
  ],
  'Physics': [
    { id: 'electricity_circuits', title_sw: '1. Mkondo wa Umeme, Saketi & Betri', title_en: '1. Electric Current & Circuits', icon: '⚡' },
    { id: 'gravity_forces', title_sw: '2. Nguvu ya Grabiti, Mvuto & Msuguano', title_en: '2. Gravity & Friction Forces', icon: '🌍' },
    { id: 'light_reflection_refraction', title_sw: '3. Mwangaza, Miwani, Vioo & Lenzi', title_en: '3. Light Optics: Reflection & Lenses', icon: '🔦' },
    { id: 'sound_waves_hearing', title_sw: '4. Mawimbi ya Sauti, Marudio & Sikio', title_en: '4. Sound Waves, Frequency & Hearing', icon: '🔊' },
    { id: 'simple_machines_levers', title_sw: '5. Mashine Rahisi: Wenzo, Kapi & Mteremko', title_en: '5. Simple Machines: Levers & Pulleys', icon: '🛠️' },
    { id: 'heat_transfer_methods', title_sw: '6. Uhamishaji wa Joto: Miale & Mkondo', title_en: '6. Heat Transfer: Conduction & Radiation', icon: '🔥' },
    { id: 'magnetism_electromagnets', title_sw: '7. Sumaku, Ncha & Sumaku-Umeme', title_en: '7. Magnetism & Electromagnets', icon: '🧲' },
    { id: 'pressure_fluids_hydraulics', title_sw: '8. Shinikizo la Maji, Hewa & Haidroliki', title_en: '8. Fluid Pressure & Hydraulics', icon: '🌊' },
    { id: 'work_energy_power', title_sw: '9. Kazi, Nishati & Nguvu (Power)', title_en: '9. Work, Energy Transformations & Power', icon: '⚡' },
    { id: 'density_floating_sinking', title_sw: '10. Uzito wa Kiasi, Kuelea na Kuzama', title_en: '10. Density, Upthrust & Flotation', icon: '⛵' }
  ],
  'Chemistry': [
    { id: 'chemistry_reactions', title_sw: '1. Asidi, Besi, Viashiria & Chumvi', title_en: '1. Acids, Bases & Neutralization', icon: '🧪' },
    { id: 'states_of_matter', title_sw: '2. Hali 3 za Maada: Mango, Maji & Gesi', title_en: '2. States of Matter & Particle Theory', icon: '🧊' },
    { id: 'separation_techniques', title_sw: '3. Kutenganisha Michanganyiko: Kuchuja & Kunereka', title_en: '3. Separation: Filtration & Distillation', icon: '⚗️' },
    { id: 'periodic_table_atoms', title_sw: '4. Atomu, Protoni & Jedwali la Periodiki', title_en: '4. Atoms, Protons & Periodic Table', icon: '⚛️' },
    { id: 'water_purification_hardness', title_sw: '5. Utakaso wa Maji, Usafishaji & Maji Magumu', title_en: '5. Water Purification & Hardness', icon: '🚰' },
    { id: 'air_gases_pollution', title_sw: '6. Muundo wa Hewa, Oksijeni & Uchafuzi', title_en: '6. Atmospheric Air Gases & Pollution', icon: '💨' },
    { id: 'metals_reactivity_series', title_sw: '7. Metali, Kutu & Mfuatano wa Mmenyuko', title_en: '7. Metals, Rusting & Reactivity Series', icon: '🔩' },
    { id: 'chemical_bonding_compounds', title_sw: '8. Muungano wa Kikemia: Ionic & Covalent', title_en: '8. Chemical Bonding: Ionic & Covalent', icon: '🔗' },
    { id: 'carbon_fuels_combustion', title_sw: '9. Kaboni, Mafuta, Mkaa & Kuungua', title_en: '9. Carbon, Fuels & Combustion', icon: '🔥' },
    { id: 'chemical_solutions_solubility', title_sw: '10. Myeyusho, Kiyeyushwa & Kiwango cha Kuyeyuka', title_en: '10. Chemical Solutions & Solubility', icon: '🥣' }
  ],
  'Mathematics': [
    { id: 'fractions_math', title_sw: '1. Sehemu za Nambari, Desimali & Asilimia', title_en: '1. Fractions, Decimals & Percentages', icon: '🍕' },
    { id: 'algebra_math', title_sw: '2. Aljebra, Milinganyo & Vigeuzi (Variables)', title_en: '2. Algebra & Linear Equations', icon: '🔣' },
    { id: 'geometry_shapes_angles', title_sw: '3. Jiometria: Pembe, Pembetatu & Poligoni', title_en: '3. Geometry: Angles & 2D/3D Shapes', icon: '📐' },
    { id: 'pythagoras_trigonometry', title_sw: '4. Nadharia ya Pythagoras (a² + b² = c²)', title_en: '4. Pythagoras Theorem & Triangles', icon: '📐' },
    { id: 'perimeter_area_volume', title_sw: '5. Mzingo, Eneo la Shamba & Ujazo (Volume)', title_en: '5. Perimeter, Area & Volume', icon: '📦' },
    { id: 'ratios_proportions_rates', title_sw: '6. Uwiano, Uwiano Linganifu & Kasi (Rates)', title_en: '6. Ratios, Proportions & Speed Rates', icon: '⚖️' },
    { id: 'statistics_data_charts', title_sw: '7. Takwimu, Wastani (Mean) & Grafu za Chati', title_en: '7. Statistics, Mean & Data Charts', icon: '📊' },
    { id: 'integers_number_line', title_sw: '8. Nambari Nzima & Nambari Hasi (-1, -2)', title_en: '8. Integers & Number Line', icon: '➖' },
    { id: 'commercial_arithmetic', title_sw: '9. Hesabu za Biashara: Faida, Hasara & Riba', title_en: '9. Commercial Math: Profit, Loss & Interest', icon: '💰' },
    { id: 'probability_chance', title_sw: '10. Uwezekano & Nafasi ya Matukio (Chance)', title_en: '10. Probability & Chance Events', icon: '🎲' }
  ],
  'Computer Science': [
    { id: 'computer_algorithms', title_sw: '1. Algoriti za Kompyuta & Michoro ya Flowchart', title_en: '1. Computer Algorithms & Flowcharts', icon: '📝' },
    { id: 'binary_data_representation', title_sw: '2. Nambari Mbili za Binary (Bits & Bytes)', title_en: '2. Binary Numbers (0 & 1) & Data', icon: '💡' },
    { id: 'logic_gates_circuits', title_sw: '3. Milango ya Mantiki: AND, OR, NOT & Swichi', title_en: '3. Logic Gates: AND, OR, NOT & Truth Tables', icon: '🔌' },
    { id: 'programming_python_scratch', title_sw: '4. Utayarishaji wa Programu (Python & Scratch)', title_en: '4. Coding in Python & Scratch', icon: '🐍' },
    { id: 'computer_hardware_components', title_sw: '5. Vifaa vya Ndani: CPU, RAM, SSD & Motherboard', title_en: '5. Computer Hardware: CPU, RAM & SSD', icon: '🖥️' },
    { id: 'networks_internet_security', title_sw: '6. Mtandao wa Intaneti, LAN & Usalama wa Data', title_en: '6. Computer Networks & Cybersecurity', icon: '🌐' },
    { id: 'ai_machine_learning_concepts', title_sw: '7. Akili Unde (AI) & Mafunzo ya Mashine (ML)', title_en: '7. Artificial Intelligence & Machine Learning', icon: '🤖' },
    { id: 'databases_information_systems', title_sw: '8. Hifadhidata (Databases), Majedwali & SQL', title_en: '8. Relational Databases & SQL Queries', icon: '🗄️' }
  ]
};

// Interactive Learner Subject Selection & Dynamic Topic Dropdown Handlers (Menu Side)
function selectLearnerSubject(subjectName) {
  STATE.selectedSubject = subjectName;
  
  const subjects = ['Biology', 'Physics', 'Chemistry', 'Mathematics', 'Computer Science'];
  subjects.forEach(s => {
    const menuBtn = document.getElementById(`menuSubj-${s}`);
    
    if (menuBtn) {
      if (s === subjectName) {
        menuBtn.className = 'px-2 py-1.5 rounded-xl text-xs font-bold transition-all flex flex-col items-center justify-center bg-emerald-600 text-white shadow-2xs';
      } else {
        menuBtn.className = 'px-2 py-1.5 rounded-xl text-xs font-bold transition-all flex flex-col items-center justify-center bg-white hover:bg-slate-100 text-slate-700 border border-slate-200';
      }
    }
  });

  populateLearnerTopicDropdowns(subjectName);
}

function populateLearnerTopicDropdowns(subjectName) {
  const topics = CURRICULUM_SUBJECT_TOPICS[subjectName] || CURRICULUM_SUBJECT_TOPICS['Biology'];
  const isSw = STATE.language !== 'en';
  
  const menuSelect = document.getElementById('menuTopicSelect');
  
  const optionsHtml = topics.map(t => `
    <option value="${t.id}">${t.icon} ${isSw ? t.title_sw : t.title_en}</option>
  `).join('');

  if (menuSelect) {
    menuSelect.innerHTML = optionsHtml;
    STATE.selectedTopicId = menuSelect.value;
  }
}

function handleLearnerTopicSelect(topicId) {
  STATE.selectedTopicId = topicId;
  const menuSelect = document.getElementById('menuTopicSelect');
  if (menuSelect && menuSelect.value !== topicId) menuSelect.value = topicId;
}

function startSelectedTopicLesson() {
  const topicId = STATE.selectedTopicId || document.getElementById('menuTopicSelect')?.value || 'photosynthesis';
  
  let topicObj = null;
  for (let s in CURRICULUM_SUBJECT_TOPICS) {
    const found = CURRICULUM_SUBJECT_TOPICS[s].find(t => t.id === topicId);
    if (found) { topicObj = found; break; }
  }
  
  const isSw = STATE.language !== 'en';
  const topicTitle = topicObj ? (isSw ? topicObj.title_sw : topicObj.title_en) : topicId;
  
  let promptText = '';
  if (STATE.language === 'en') {
    promptText = `Teach me about ${topicTitle}`;
  } else if (STATE.language === 'sheng') {
    promptText = `Nielezange kuhusu ${topicTitle}`;
  } else if (STATE.language === 'yo') {
    promptText = `Kọ́ mi nípa ${topicTitle}`;
  } else if (STATE.language === 'ha') {
    promptText = `Koya mini game da ${topicTitle}`;
  } else {
    promptText = `Nifundishe kuhusu ${topicTitle}`;
  }
  
  sendQuickPrompt(promptText);
}

function handleSubjectChange(e) {
  STATE.subject = e.target.value;
  const labels = {
    all: 'Masomo Yote (All STEM)',
    biology: 'Biolojia (Biology)',
    physics: 'Fizikia (Physics)',
    chemistry: 'Kemia (Chemistry)',
    mathematics: 'Hesabu (Mathematics)',
    computer_science: 'Sayansi ya Kompyuta (CS)',
    agriculture: 'Kilimo & Mazingira (Agri)'
  };
  appendSystemNotice(`📚 <b>Somo Limebadilishwa:</b> Umelenga <b>${labels[STATE.subject] || STATE.subject}</b>.`);
  renderRegionUI();
}

function handleGradeChange(e) {
  STATE.gradeLevel = e.target.value;
  if (STATE.profile) STATE.profile.grade_level = STATE.gradeLevel;
  appendSystemNotice(`🎓 <b>Kiwango cha Mwanafunzi:</b> Kimebadilishwa kuwa <b>${STATE.gradeLevel}</b>.`);
}

function handleCountryChange(e) {
  STATE.country = e.target.value;
  const countryJurisdictions = {
    Kenya: 'KE',
    Tanzania: 'TZ',
    Uganda: 'UG',
    Rwanda: 'RW',
    Nigeria: 'NG',
    Ghana: 'GH',
    'South Africa': 'ZA',
    Ethiopia: 'ET'
  };
  if (countryJurisdictions[STATE.country]) {
    STATE.jurisdiction = countryJurisdictions[STATE.country];
    const jSelect = document.getElementById('jurisdictionSelect');
    if (jSelect) jSelect.value = STATE.jurisdiction;
  }
  appendSystemNotice(`🌍 <b>Nchi Imewekwa:</b> <b>${STATE.country}</b> (Sheria ya Data: ${STATE.jurisdiction}).`);
}

function handleRegionChange(e) {
  STATE.region = e.target.value;
  renderRegionUI();
  appendSystemNotice(`🏞️ <b>Eneo la Mazingira:</b> Limewekwa kuwa <b>${STATE.regionsMeta[STATE.region]?.name_sw || STATE.region}</b>.`);
}

function detectGPSLocation() {
  if (!navigator.geolocation) {
    alert('Kifaa hiki hakina huduma ya GPS. Tafadhali chagua nchi na eneo kwa mikono.');
    return;
  }
  const btn = document.getElementById('gpsDetectBtn');
  const text = document.getElementById('gpsDetectText');
  if (text) text.innerText = 'Inatambua... 📡';
  
  navigator.geolocation.getCurrentPosition(
    (pos) => {
      const lat = pos.coords.latitude;
      const lon = pos.coords.longitude;
      STATE.gpsCoords = { lat, lon };
      
      if (lat >= -4.7 && lat <= 5.5 && lon >= 33.9 && lon <= 41.9) {
        STATE.country = 'Kenya';
        STATE.jurisdiction = 'KE';
        if (lon < 35.0) STATE.region = 'lake_basin';
        else if (lon > 39.0) STATE.region = 'coastal';
        else if (lat > 2.0) STATE.region = 'arid';
        else STATE.region = 'highlands';
      } else if (lat < -4.7 && lat > -11.8 && lon >= 29.3 && lon <= 40.5) {
        STATE.country = 'Tanzania';
        STATE.jurisdiction = 'TZ';
        STATE.region = (lon > 38.5) ? 'coastal' : 'lake_basin';
      } else if (lat >= 4.0 && lat <= 14.0 && lon >= 2.5 && lon <= 15.0) {
        STATE.country = 'Nigeria';
        STATE.jurisdiction = 'NG';
        STATE.region = (lat < 7.0) ? 'coastal' : ((lat > 11.0) ? 'arid' : 'urban');
      } else if (lat < -22.0) {
        STATE.country = 'South Africa';
        STATE.jurisdiction = 'ZA';
        STATE.region = 'urban';
      }

      const cSelect = document.getElementById('learnerCountrySelect');
      if (cSelect) cSelect.value = STATE.country;
      const rSelect = document.getElementById('learnerRegionSelect');
      if (rSelect) rSelect.value = STATE.region;
      
      if (text) text.innerText = 'GPS: ' + STATE.country + ' 📍';
      if (btn) btn.className = 'flex items-center space-x-1 px-2.5 py-1 bg-teal-700 text-white rounded-xl font-bold shadow-xs transition-all flex-shrink-0';

      renderRegionUI();
      appendSystemNotice(`📍 <b>Eneo Lako:</b> Nchi: <b>${STATE.country}</b> • Eneo: <b>${STATE.regionsMeta[STATE.region]?.name_sw || STATE.region}</b>.`);
    },
    (err) => {
      if (text) text.innerText = 'GPS Auto-Detect';
      appendSystemNotice('📍 <i>Haikuweza kupata eneo kiotomatiki. Unaweza kuchagua nchi na eneo kwa urahisi kwenye menyu ☰.</i>');
    },
    { timeout: 8000 }
  );
}

// Pan-African Language Switching (Instant Language Switcher & Inline Badge)
function changeLanguage(langCode) {
  STATE.language = langCode;
  localStorage.setItem('elewa_user_lang', langCode);

  const mSelect = document.getElementById('langSelect');
  if (mSelect) mSelect.value = langCode;

  const langMeta = STATE.languagesMeta[langCode];
  const inFlag = document.getElementById('inputLangFlag');
  const inName = document.getElementById('inputLangName');
  if (langMeta) {
    if (inFlag) inFlag.innerText = langMeta.flag || '🌍';
    if (inName) inName.innerText = langMeta.native_name || langMeta.name_en;
  }

  updateUIStrings();
  updateNetworkUI();
  renderRegionUI();
  renderVault();
  renderMastery();
  populateLearnerTopicDropdowns(STATE.selectedSubject || 'Biology');

  if (langMeta) {
    appendSystemNotice(`🌍 Lugha: <b>${langMeta.flag} ${langMeta.native_name}</b> (${langMeta.motto}).`);
  }
}

function updateUIStrings() {
  const dict = I18N[STATE.language] || I18N.sw;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key]) el.innerText = dict[key];
  });
  const input = document.getElementById('userInput');
  if (input) input.placeholder = dict.input_placeholder;

  // Translate subject select options
  if (dict.subjects) {
    const subjSelect = document.getElementById('learnerSubjectSelect');
    if (subjSelect) {
      Array.from(subjSelect.options).forEach(opt => {
        if (dict.subjects[opt.value]) opt.text = dict.subjects[opt.value];
      });
    }
  }

  // Translate grade select options
  if (dict.grades) {
    const gradeSelect = document.getElementById('learnerGradeSelect');
    if (gradeSelect) {
      Array.from(gradeSelect.options).forEach(opt => {
        if (dict.grades[opt.value]) opt.text = dict.grades[opt.value];
      });
    }
  }

  // Translate region select options
  if (dict.regions) {
    const regionSelect = document.getElementById('learnerRegionSelect');
    if (regionSelect) {
      Array.from(regionSelect.options).forEach(opt => {
        if (dict.regions[opt.value]) opt.text = dict.regions[opt.value];
      });
    }
  }

  updateHeaderStatusPill();
}


// Navigation Tabs (Learn -> Practice -> Progress -> Parent/Teacher -> Accessibility -> Offline, with Governance & Research as separate dedicated hubs)
function switchTab(tabId) {
  STATE.activeTab = tabId;
  ['chat', 'vault', 'mastery', 'stakeholders', 'privacy_hub', 'research_hub'].forEach(t => {
    const section = document.getElementById(`${t}Section`);
    const btn = document.getElementById(`tabBtn-${t}`);
    if (t === tabId) {
      if (section) section.classList.remove('hidden');
      if (btn) btn.classList.add('active-tab');
    } else {
      if (section) section.classList.add('hidden');
      if (btn) btn.classList.remove('active-tab');
    }
  });

  // Update Journey Navigation Bar Buttons
  ['chat', 'mastery', 'stakeholders', 'vault'].forEach(t => {
    const jBtn = document.getElementById(`journeyBtn-${t}`);
    if (jBtn) {
      if (t === tabId) {
        jBtn.className = 'px-2.5 sm:px-3 py-1 rounded-xl flex items-center space-x-1 transition-all bg-brand-600 text-white shadow-xs font-bold';
      } else {
        jBtn.className = 'px-2.5 sm:px-3 py-1 rounded-xl flex items-center space-x-1 transition-all bg-white hover:bg-slate-200 text-slate-700 border border-slate-200 font-bold';
      }
    }
  });

  if (tabId === 'mastery') refreshProfile();
  if (tabId === 'stakeholders') {
    updateParentDigestPreview();
    loadFeedbackFeed();
  }
  if (tabId === 'privacy_hub') renderJurisdictionDetails(STATE.jurisdiction);
}

function openPracticeHub() {
  const isSw = STATE.language !== 'en';
  // Open the interactive quiz for current active topic or default module
  const mod = STATE.offlineModules.find(m => m.id === 'photosynthesis') || STATE.offlineModules[0];
  if (mod && mod.quiz) {
    openQuizModal(JSON.stringify(mod.quiz), isSw ? mod.title_sw : mod.title_en);
  } else {
    switchTab('vault');
  }
}

// Stakeholders Sub-Tabs
function switchStakeholderTab(subTab) {
  STATE.activeStakeholderSubTab = subTab;
  ['parents', 'teachers', 'community', 'feedback_feed'].forEach(s => {
    const view = document.getElementById(`stakeholderView-${s}`);
    const btn = document.getElementById(`subTab-${s}`);
    if (s === subTab) {
      view.classList.remove('hidden');
      btn.className = 'px-3.5 py-2 rounded-xl bg-indigo-50 text-indigo-900 border border-indigo-200';
    } else {
      view.classList.add('hidden');
      btn.className = 'px-3.5 py-2 rounded-xl bg-slate-100 text-slate-600 hover:bg-slate-200';
    }
  });
  if (subTab === 'feedback_feed') loadFeedbackFeed();
}

// Governance & Privacy Hub Sub-Tabs (National DPAs & ElewaSTEM Design Frameworks)
function switchEthicsSubTab(subTab) {
  ['dpas', 'frameworks'].forEach(e => {
    const view = document.getElementById(`ethicsView-${e}`);
    const btn = document.getElementById(`ethicsSubTab-${e}`);
    if (e === subTab) {
      if (view) view.classList.remove('hidden');
      if (btn) btn.className = 'px-3.5 py-2 rounded-xl bg-emerald-50 text-emerald-900 border border-emerald-200';
    } else {
      if (view) view.classList.add('hidden');
      if (btn) btn.className = 'px-3.5 py-2 rounded-xl bg-slate-100 text-slate-600 hover:bg-slate-200';
    }
  });
}

// Research & Pedagogy Hub Sub-Tabs (Empirical Statistics & African Learning Theories)
function switchResearchSubTab(subTab) {
  ['statistics', 'theories'].forEach(r => {
    const view = document.getElementById(`researchView-${r}`);
    const btn = document.getElementById(`researchSubTab-${r}`);
    if (r === subTab) {
      if (view) view.classList.remove('hidden');
      if (btn) btn.className = 'px-3.5 py-2 rounded-xl bg-blue-50 text-blue-900 border border-blue-200';
    } else {
      if (view) view.classList.add('hidden');
      if (btn) btn.className = 'px-3.5 py-2 rounded-xl bg-slate-100 text-slate-600 hover:bg-slate-200';
    }
  });
}

function triggerSafetyOverride() {
  stopSpeech();
  appendSystemNotice('🛑 <b>Teacher/Parent Safety Override Activated:</b> Mwalimu au mzazi amesimamisha mazungumzo ya AI mara moja kwa ajili ya usalama.');
  alert('🛑 Safety Override: Mazungumzo yamesimamishwa. Unaweza kuuliza swali jipya au kusahihisha dhana darasani.');
}

function triggerKillSwitch() {
  triggerSafetyOverride();
}

function elderDisagreement(topic) {
  openFeedbackModal('teacher');
  appendSystemNotice('👥 <b>Parent–Teacher–Community Advisory Panel:</b> Haki ya kupinga au kusahihisha jibu la AI imefunguliwa kwa Mwalimu/Mzazi.');
}

function getOrCreateStudentPairingCode() {
  let code = localStorage.getItem('elewa_student_pairing_code');
  if (!code) {
    const randomNum = Math.floor(1000 + Math.random() * 9000);
    code = `ELEWA-${randomNum}`;
    localStorage.setItem('elewa_student_pairing_code', code);
  }
  return code;
}

function generateNewPairingCode() {
  const randomNum = Math.floor(1000 + Math.random() * 9000);
  const code = `ELEWA-${randomNum}`;
  localStorage.setItem('elewa_student_pairing_code', code);
  STATE.parentPairingCode = code;
  const codeEl = document.getElementById('parentPairingCode');
  if (codeEl) codeEl.innerText = code;
  appendSystemNotice(`🔑 <b>Nambari Mpya ya Mzazi Imewekwa:</b> ${code} (Demo Mode)`);
}

function updateParentDigestPreview() {
  const smsEl = document.getElementById('parentSmsPreview');
  const codeEl = document.getElementById('parentPairingCode');
  const reg = STATE.regionsMeta[STATE.region] || STATE.regionsMeta.lake_basin;
  const mastery = STATE.profile.mastery_graph || {};
  const count = Object.keys(mastery).length || 1;

  const dynamicCode = getOrCreateStudentPairingCode();
  STATE.parentPairingCode = dynamicCode;
  if (codeEl) codeEl.innerText = dynamicCode;

  const defaultSms = `ElewaSTEM Ripoti ya Mzazi: Mwanafunzi amechunguza mada ${count} za Sayansi kwa mifano ya ${reg.name_sw}. Jaribio la wiki hii: Chunguza Oksijeni ya mimea ya jikoni na mtoto wako!`;
  if (smsEl) smsEl.innerText = defaultSms;

  if (isEffectivelyOnline()) {
    fetch(`/api/parent/digest/${STATE.studentId}?region=${STATE.region}`)
      .then(r => r.json())
      .then(data => {
        if (data.sms_digest_text && smsEl) smsEl.innerText = data.sms_digest_text;
        if (data.pairing_code && codeEl) {
          // If server provides a customized pairing code, sync it
          codeEl.innerText = data.pairing_code;
          STATE.parentPairingCode = data.pairing_code;
        }
        STATE.parentMagicLink = data.remote_magic_link;
      })
      .catch(e => console.log('Parent digest remote fetch notice:', e));
  }
}

function absHash(str) {
  let hash = 0;
  for (let i = 0; i < str.length; i++) hash = ((hash << 5) - hash) + str.charCodeAt(i);
  return Math.abs(hash);
}

function copyPairingCode() {
  const code = document.getElementById('parentPairingCode')?.innerText || getOrCreateStudentPairingCode();
  navigator.clipboard.writeText(code).then(() => {
    alert(`Nambari ya kuunganisha (${code}) imenakiliwa! Mzazi anaweza kuitumia kwenye simu yake.`);
  }).catch(() => alert('Nambari ya kuunganisha: ' + code));
}

function copyParentMagicLink() {
  const code = document.getElementById('parentPairingCode')?.innerText || getOrCreateStudentPairingCode();
  const link = `https://elewastem.org/parent?code=${code}&student=${STATE.studentId}`;
  navigator.clipboard.writeText(link).then(() => {
    alert(`Kiungo cha Mzazi kimenakiliwa! Tuma kwa WhatsApp au SMS ya mzazi:\n${link}`);
  }).catch(() => alert('Kiungo cha mzazi: ' + link));
}

async function dispatchRemoteParentSms() {
  const phone = document.getElementById('parentPhoneNumberInput')?.value.trim() || '+254712345678';
  try {
    if (isEffectivelyOnline()) {
      const res = await fetch('/api/parent/send-remote-alert', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          phone_number: phone,
          student_id: STATE.studentId,
          region: STATE.region
        })
      });
      if (res.ok) {
        const data = await res.json();
        alert(`📲 ${data.message}\n\nUjumbe uliotumwa:\n"${data.sms_content}"`);
        appendSystemNotice(`📲 <b>SMS Imetumwa kwa Mzazi:</b> Ujumbe wa maendeleo umetumwa kwa ${phone}.`);
      }
    } else {
      alert(`📲 Ujumbe wa SMS umehifadhiwa na utatumwa kwa nambari ${phone} punde mtandao wa simu utakapopatikana!`);
    }
  } catch (err) {
    alert(`Ujumbe umetumwa kwa ${phone}`);
  }
}

function copySmsDigest() {
  const text = document.getElementById('parentSmsPreview').innerText;
  navigator.clipboard.writeText(text).then(() => {
    alert('Ujumbe wa SMS umenakiliwa! Unaweza kuutuma kwa simu ya mzazi.');
  }).catch(() => {
    alert('Nakili maandishi haya: ' + text);
  });
}

function loadTeacherLessonPlan(topicId) {
  const card = document.getElementById('teacherLessonPlanCard');
  if (!card) return;

  const mod = STATE.offlineModules.find(m => m.id === topicId) || STATE.offlineModules[0];
  if (!mod) return;

  const regKey = STATE.region;
  const regMeta = STATE.regionsMeta[regKey] || STATE.regionsMeta.lake_basin;
  const regionalDict = mod.regional_analogies ? (mod.regional_analogies[regKey] || mod.regional_analogies.lake_basin) : {};

  card.innerHTML = `
    <div class="space-y-3">
      <div class="flex items-center justify-between border-b border-slate-200 pb-2">
        <div>
          <span class="text-[10px] font-bold uppercase tracking-wider text-blue-700 bg-blue-50 px-2 py-0.5 rounded">${mod.cbc_strand || 'CBC Science & Technology'}</span>
          <h4 class="font-black text-slate-900 text-sm mt-1">${mod.title_sw} (${mod.title_en})</h4>
        </div>
        <span class="text-xs font-bold text-slate-500">Grade 5 & 6</span>
      </div>

      <div>
        <p class="font-bold text-slate-800 mb-1">🎯 Matokeo ya Kujifunza (Learning Outcomes):</p>
        <ul class="list-disc pl-4 space-y-0.5 text-slate-600">
          <li>Mwanafunzi aweze kueleza dhana ya <b>${mod.title_sw}</b> kwa kutumia mazingira ya <b>${regMeta.name_sw}</b>.</li>
          <li>Kutambua msamiati wa kisayansi katika lugha ya asili na Kiingereza.</li>
          <li>Kufanya jaribio la vitendo darasani kwa kutumia vifaa vya bure vya mazingira.</li>
        </ul>
      </div>

      <div class="bg-emerald-50 border border-emerald-200 p-3 rounded-xl">
        <p class="font-bold text-emerald-900 mb-0.5">💡 Zana ya Kufundishia ya Eneo (Local Teaching Aid):</p>
        <p class="text-emerald-950 italic">${regionalDict.analogy_sw || mod.analogy_sw}</p>
      </div>

      ${mod.tactile_audio_description_sw ? `
      <div class="bg-blue-50 border border-blue-200 p-3 rounded-xl">
        <p class="font-bold text-blue-900 mb-0.5">👁️ Mwongozo wa Wanafunzi Wasioona (Tactile Description):</p>
        <p class="text-blue-950">${mod.tactile_audio_description_sw}</p>
      </div>` : ''}

      ${mod.sign_language_visual_cues_sw ? `
      <div class="bg-purple-50 border border-purple-200 p-3 rounded-xl">
        <p class="font-bold text-purple-900 mb-0.5">🧏 Vielelezo vya Picha & Michoro (Visual & Concept Cues):</p>
        <p class="text-purple-950">${mod.sign_language_visual_cues_sw}</p>
      </div>` : ''}

      <div>
        <p class="font-bold text-slate-800 mb-1">🧪 Shughuli ya Darasani / Jaribio:</p>
        <p class="text-slate-600"><b>Vifaa:</b> ${mod.experiment.materials_sw}</p>
        <p class="text-slate-600"><b>Hatua:</b> ${mod.experiment.steps_sw.replace(/\n/g, ' ')}</p>
      </div>

      <div class="bg-indigo-50 border border-indigo-200 p-3 rounded-xl">
        <p class="font-bold text-indigo-900 mb-1">📝 Swali la Mtihani wa Kujipima (Diagnostic Quiz):</p>
        <p class="text-indigo-950 font-medium">${mod.quiz.question_sw}</p>
        <p class="text-xs text-indigo-800 mt-1"><b>Jibu Sahihi:</b> ${mod.quiz.options_sw[mod.quiz.correct_index]}</p>
      </div>
    </div>
  `;
}

function renderCommunityActivities() {
  const grid = document.getElementById('communityProjectsGrid');
  if (!grid) return;
  const regMeta = STATE.regionsMeta[STATE.region] || STATE.regionsMeta.lake_basin;

  grid.innerHTML = `
    <div class="bg-slate-50 border border-slate-200 rounded-xl p-3.5 space-y-2">
      <div class="flex items-center justify-between">
        <h5 class="font-bold text-slate-900 text-xs">💧 Mradi wa Chujio la Maji (${regMeta.name_sw})</h5>
        <span class="text-[9px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.5 rounded">Mazingira</span>
      </div>
      <p class="text-[11px] text-slate-600 leading-relaxed">
        <b>Vifaa:</b> Chupa ya plastiki, mchanga wa mto, makaa ya jikoni, pamba.<br>
        <b>Lengo:</b> Watoto wanajionea jinsi uchafu unavyochujwa kutoka kwa maji ya mvua/mto.
      </p>
    </div>

    <div class="bg-slate-50 border border-slate-200 rounded-xl p-3.5 space-y-2">
      <div class="flex items-center justify-between">
        <h5 class="font-bold text-slate-900 text-xs">☀️ Mradi wa Kukausha Mboga kwa Jua (Solar Dryer)</h5>
        <span class="text-[9px] bg-amber-100 text-amber-800 font-bold px-1.5 py-0.5 rounded">Nishati</span>
      </div>
      <p class="text-[11px] text-slate-600 leading-relaxed">
        <b>Vifaa:</b> Sanduku la kadibodi, foil ya alumini, karatasi ya nailoni safi.<br>
        <b>Lengo:</b> Kutumia jua kukausha mboga za kienyeji kwa ajili ya kuhifadhi.
      </p>
    </div>
  `;
}

// Pan-African Data Protection Legal Hub Renderer
function renderJurisdictionDetails(countryCode) {
  STATE.jurisdiction = countryCode;
  const card = document.getElementById('jurisdictionDetailCard');
  if (!card) return;

  const jurMap = {
    KE: {
      flag: '🇰🇪', country: 'Kenya', law: 'Data Protection Act 2019',
      authority: 'Office of the Data Protection Commissioner (ODPC)',
      child_section: 'Section 29 (Processing Personal Data of Children)',
      compliance: 'Designed to support compliance via strict parental consent gatekeeper, on-device edge calculation, and zero cloud retention of student telemetry.'
    },
    NG: {
      flag: '🇳🇬', country: 'Nigeria', law: 'Nigeria Data Protection Act 2023 (NDPA)',
      authority: 'Nigeria Data Protection Commission (NDPC)',
      child_section: 'Section 31 (Processing of Personal Data of a Child)',
      compliance: 'Designed to support compliance with parental consent verification, duty of care in educational software, and strict data minimization.'
    },
    ZA: {
      flag: '🇿🇦', country: 'South Africa', law: 'Protection of Personal Information Act 2013 (POPIA)',
      authority: 'Information Regulator (South Africa)',
      child_section: 'Section 34 & 35 (Prohibition on Processing Child Personal Information)',
      compliance: 'Designed to support compliance for authorized pedagogical use with competent person consent and zero marketing profiling.'
    },
    GH: {
      flag: '🇬🇭', country: 'Ghana', law: 'Data Protection Act 2012 (Act 843)',
      authority: 'Data Protection Commission (DPC Ghana)',
      child_section: 'Section 37 & 38 (Special Personal Data & Minors)',
      compliance: 'Designed to support compliance with explicit parental assent and educational data silo isolation.'
    },
    UG: {
      flag: '🇺🇬', country: 'Uganda', law: 'Data Protection and Privacy Act 2019',
      authority: 'Personal Data Protection Office (PDPO Uganda)',
      child_section: 'Section 8 (Data on Children)',
      compliance: 'Designed to support compliance through client PWA architecture preventing non-consensual transmission.'
    },
    TZ: {
      flag: '🇹🇿', country: 'Tanzania', law: 'Personal Data Protection Act 2022',
      authority: 'Personal Data Protection Commission (PDPC Tanzania)',
      child_section: 'Section 30 (Special Categories & Protection of Children)',
      compliance: 'Designed to support compliance through on-device local storage custody.'
    },
    RW: {
      flag: '🇷🇼', country: 'Rwanda', law: 'Law No. 058/2021 on Personal Data and Privacy',
      authority: 'National Cyber Security Authority (NCSA Rwanda)',
      child_section: 'Article 10 (Processing of Personal Data of a Child)',
      compliance: 'Designed to support compliance with parental authorization and instant data erasure controls.'
    },
    AU_CONTINENTAL: {
      flag: '🌍', country: 'Pan-African Union', law: 'AU Malabo Convention on Cyber Security & Personal Data (2014)',
      authority: 'African Union Commission (AUC)',
      child_section: 'Article 14 & 15 (Principles of Personal Data Processing)',
      compliance: 'Promotes African digital sovereignty through local on-device AI processing without foreign data extraction.'
    }
  };

  const jur = jurMap[countryCode] || jurMap.KE;

  card.innerHTML = `
    <div class="space-y-2.5">
      <div class="flex items-center justify-between border-b border-slate-200 pb-2">
        <div class="flex items-center space-x-2">
          <span class="text-2xl">${jur.flag}</span>
          <div>
            <h4 class="font-black text-slate-900 text-sm">${jur.country} — ${jur.law}</h4>
            <p class="text-[10px] text-slate-500 font-bold">Mamlaka ya Udhibiti: ${jur.authority}</p>
          </div>
        </div>
        <span class="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded-full">Designed for Compliance</span>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px]">
        <div class="bg-white p-3 rounded-xl border border-slate-200">
          <p class="font-bold text-slate-800">📜 Kifungu cha Ulinzi wa Watoto:</p>
          <p class="text-slate-600 mt-0.5">${jur.child_section}</p>
        </div>
        <div class="bg-white p-3 rounded-xl border border-slate-200">
          <p class="font-bold text-slate-800">🛡️ Kinga ya ElewaSTEM (Guarantees):</p>
          <p class="text-slate-600 mt-0.5">${jur.compliance}</p>
        </div>
      </div>

      <div class="bg-emerald-50 border border-emerald-200 p-3 rounded-xl flex items-center justify-between">
        <div class="flex items-center space-x-2 text-[11px] text-emerald-950">
          <span>🔒</span>
          <span><b>Ulinzi wa Data:</b> Taarifa za mwanafunzi zinalindwa kwa misingi ya kupunguza ukusanyaji wa data (Data Minimization), huku huduma za mtandao zikitumia mawasiliano yaliyosimbwa (Encrypted).</span>
        </div>
        <button onclick="revokeLocationConsent()" class="text-[10px] bg-white border border-emerald-300 text-red-600 font-bold px-2 py-1 rounded-lg">
          Futa Data
        </button>
      </div>
    </div>
  `;
}

// Offline Pack Management
async function loadOfflinePack() {
  try {
    const cached = localStorage.getItem('elewa_offline_pack');
    if (cached) STATE.offlineModules = JSON.parse(cached);

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

function getActiveSessionHistory() {
  if (!STATE.currentSessionId) return [];
  const sessions = getChatSessions();
  const session = sessions.find(s => s.id === STATE.currentSessionId);
  if (!session || !session.messages) return [];
  return session.messages.slice(-10).map(m => ({
    role: m.role === 'user' ? 'user' : 'model',
    text: m.text || ''
  }));
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

function toggleAgentMode() {
  STATE.agentMode = (STATE.agentMode === 'creative' ? 'precise' : 'creative');
  const btn = document.getElementById('agentModeBtn');
  const icon = document.getElementById('agentModeIcon');
  const text = document.getElementById('agentModeText');
  if (STATE.agentMode === 'creative') {
    if (btn) btn.className = 'px-2.5 py-1 bg-purple-100 text-purple-900 border border-purple-300 rounded-lg font-bold flex items-center space-x-1 flex-shrink-0 hover:bg-purple-200 transition-all';
    if (icon) icon.innerText = '🎨';
    if (text) text.innerText = 'Hadithi na Mifano';
    appendSystemNotice('🎨 <b>Mtindo wa Kufundisha:</b> Mifano na Hadithi za Kusisimua.');
  } else {
    if (btn) btn.className = 'px-2.5 py-1 bg-blue-100 text-blue-900 border border-blue-300 rounded-lg font-bold flex items-center space-x-1 flex-shrink-0 hover:bg-blue-200 transition-all';
    if (icon) icon.innerText = '📐';
    if (text) text.innerText = 'Maelezo Mafupi na Hesabu';
    appendSystemNotice('📐 <b>Mtindo wa Kufundisha:</b> Maelezo ya Moja kwa Moja na Hesabu.');
  }
}

function sendQuickPrompt(text) {
  switchTab('chat');
  appendUserMessage(text);
  executeAgentQuery(text);
}

async function executeAgentQuery(query, simplify = false) {
  const loadingId = appendLoadingIndicator();

  if (!isEffectivelyOnline()) {
    setTimeout(() => {
      removeLoadingIndicator(loadingId);
      const localResponse = generateLocalOfflineAnswer(query, simplify);
      appendAssistantMessage(localResponse);
      if (STATE.autoSpeak) speakText(localResponse.text);
    }, 400);
    return;
  }

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        student_id: STATE.studentId,
        message: query,
        history: getActiveSessionHistory(),
        language: STATE.language,
        region: STATE.region,
        jurisdiction: STATE.jurisdiction,
        country: STATE.country || 'Kenya',
        subject: STATE.selectedSubject || STATE.subject || 'all',
        topic_id: STATE.selectedTopicId || undefined,
        grade_level: STATE.gradeLevel || 'Grade 6 (Upper Primary)',
        gps_coordinates: STATE.gpsCoords,
        simplify: simplify,
        mode: STATE.agentMode
      })
    });

    removeLoadingIndicator(loadingId);

    if (res.ok) {
      const data = await res.json();
      appendAssistantMessage(data);
      if (data.student_profile) STATE.profile = data.student_profile;
      if (STATE.autoSpeak) speakText(data.text);
    } else {
      const localFallback = generateLocalOfflineAnswer(query, simplify);
      appendAssistantMessage(localFallback);
      if (STATE.autoSpeak) speakText(localFallback.text);
    }
  } catch (err) {
    removeLoadingIndicator(loadingId);
    const localFallback = generateLocalOfflineAnswer(query, simplify);
    appendAssistantMessage(localFallback);
    if (STATE.autoSpeak) speakText(localFallback.text);
  }
}

function generateLocalOfflineAnswer(query, simplify) {
  const qLower = query.toLowerCase();
  let matched = null;
  
  // 0. If user explicitly selected a topic in the menu
  if (STATE.selectedTopicId) {
    matched = STATE.offlineModules.find(m => m.id === STATE.selectedTopicId);
  }

  // 1. Biology: Digestive System (including villi, ileum, enzymes, absorption)
  if (!matched && (qLower.includes('digest') || qLower.includes('villi') || qLower.includes('vili') || qLower.includes('microvilli') || qLower.includes('ileum') || qLower.includes('duodenum') || qLower.includes('absorption') || qLower.includes('mmeng\'enyo') || qLower.includes('stomach') || qLower.includes('tumbo') || qLower.includes('esophagus') || qLower.includes('umio') || qLower.includes('kinywa') || qLower.includes('utumbo') || qLower.includes('enzyme') || qLower.includes('saliva') || qLower.includes('mate') || qLower.includes('bile') || qLower.includes('nyongo') || qLower.includes('pancreas') || qLower.includes('pepsin'))) {
    matched = STATE.offlineModules.find(m => m.id === 'human_digestive_system');
  }

  // 2. Biology: Heart & Circulatory System
  if (!matched && (qLower.includes('heart') || qLower.includes('moyo') || qLower.includes('circulat') || qLower.includes('mzunguko wa damu') || qLower.includes('blood') || qLower.includes('damu') || qLower.includes('artery') || qLower.includes('ateri') || qLower.includes('vein') || qLower.includes('vena') || qLower.includes('pulse') || qLower.includes('mapigo'))) {
    matched = STATE.offlineModules.find(m => m.id === 'circulatory_heart');
  }

  // 3. Biology: Human Respiration & Lungs
  if (!matched && (qLower.includes('lung') || qLower.includes('mapafu') || qLower.includes('respirat') || qLower.includes('upumuaji') || qLower.includes('breathe') || qLower.includes('pumua') || qLower.includes('trachea') || qLower.includes('koromeo') || qLower.includes('inhale') || qLower.includes('exhale'))) {
    matched = STATE.offlineModules.find(m => m.id === 'human_respiration');
  }

  // 4. Biology: Cell Biology
  if (!matched && (qLower.includes('cell') || qLower.includes('seli') || qLower.includes('nucleus') || qLower.includes('kiini') || qLower.includes('cytoplasm') || qLower.includes('saikroplasimu') || qLower.includes('membrane') || qLower.includes('utando') || qLower.includes('chloroplast') || qLower.includes('kloroplasti'))) {
    matched = STATE.offlineModules.find(m => m.id === 'cell_biology');
  }

  // 5. Biology: Food Chains & Ecology
  if (!matched && (qLower.includes('food chain') || qLower.includes('mnyororo wa chakula') || qLower.includes('ecolog') || qLower.includes('ikolojia') || qLower.includes('ecosystem') || qLower.includes('producer') || qLower.includes('mtengenezaji') || qLower.includes('consumer') || qLower.includes('predator') || qLower.includes('herbivore') || qLower.includes('carnivore'))) {
    matched = STATE.offlineModules.find(m => m.id === 'ecology_food_chains');
  }

  // 6. Biology: Pollination & Flowers
  if (!matched && (qLower.includes('pollinat') || qLower.includes('uchavushaji') || qLower.includes('flower') || qLower.includes('maua') || qLower.includes('petal') || qLower.includes('petali') || qLower.includes('stamen') || qLower.includes('pistil') || qLower.includes('chavulio') || qLower.includes('chavua') || qLower.includes('poleni') || qLower.includes('nyuki') || qLower.includes('bee'))) {
    matched = STATE.offlineModules.find(m => m.id === 'plant_pollination');
  }

  // 7. Biology: Classification of Living Things
  if (!matched && (qLower.includes('vertebrate') || qLower.includes('invertebrate') || qLower.includes('uti wa mgongo') || qLower.includes('classify') || qLower.includes('uainishaji') || qLower.includes('mammal') || qLower.includes('mamalia') || qLower.includes('reptile') || qLower.includes('amphibian') || qLower.includes('wadudu'))) {
    matched = STATE.offlineModules.find(m => m.id === 'living_things_classification');
  }

  // 8. Biology: Aquatic Fish Respiration
  if (!matched && (qLower.includes('fish') || qLower.includes('samaki') || qLower.includes('gills') || qLower.includes('mashavu') || qLower.includes('matamvua') || qLower.includes('ngege') || qLower.includes('mbuta'))) {
    matched = STATE.offlineModules.find(m => m.id === 'aquatic_biology_kisumu');
  }

  // 9. Biology: Photosynthesis
  if (!matched && (qLower.includes('photo') || qLower.includes('usanisinuru') || qLower.includes('klorofili') || qLower.includes('chlorophyll') || qLower.includes('plant food') || qLower.includes('chakula cha mmea') || qLower.includes('stomata'))) {
    matched = STATE.offlineModules.find(m => m.id === 'photosynthesis');
  }

  // 10. Mathematics: Algebra
  if (!matched && (qLower.includes('algebra') || qLower.includes('aljebra') || qLower.includes('equation') || qLower.includes('mlinganyo') || qLower.includes('variable') || qLower.includes('kigeuzi') || qLower.includes('solve for x'))) {
    matched = STATE.offlineModules.find(m => m.id === 'algebra_math');
  }

  // 11. Mathematics: Fractions
  if (!matched && (qLower.includes('fraction') || qLower.includes('sehemu') || qLower.includes('gawanya') || qLower.includes('hesabu') || qLower.includes('proportion'))) {
    matched = STATE.offlineModules.find(m => m.id === 'fractions_math');
  }

  // 12. Chemistry: Acids, Bases & Reactions
  if (!matched && (qLower.includes('chem') || qLower.includes('kemia') || qLower.includes('acid') || qLower.includes('asidi') || qLower.includes('base') || qLower.includes('besi') || qLower.includes('reaction'))) {
    matched = STATE.offlineModules.find(m => m.id === 'chemistry_reactions');
  }

  // 13. Computer Science: Algorithms & Logic
  if (!matched && (qLower.includes('comput') || qLower.includes('code') || qLower.includes('algorithm') || qLower.includes('algoriti') || qLower.includes('program') || qLower.includes('logic'))) {
    matched = STATE.offlineModules.find(m => m.id === 'computer_algorithms');
  }

  // 14. Physics: Circuits & Electricity
  if (!matched && (qLower.includes('circuit') || qLower.includes('umeme') || qLower.includes('saketi') || qLower.includes('battery') || qLower.includes('betri') || qLower.includes('electr'))) {
    matched = STATE.offlineModules.find(m => m.id === 'electricity_circuits');
  }

  // 15. Physics: Gravity & Friction
  if (!matched && (qLower.includes('gravity') || qLower.includes('grabiti') || qLower.includes('force') || qLower.includes('friction') || qLower.includes('msuguano') || qLower.includes('mvuto'))) {
    matched = STATE.offlineModules.find(m => m.id === 'gravity_forces');
  }

  // 16. Match by key terms / title
  if (!matched) {
    matched = STATE.offlineModules.find(m => 
      qLower.includes(m.id) || 
      (m.title_en && qLower.includes(m.title_en.toLowerCase())) || 
      (m.title_sw && qLower.includes(m.title_sw.toLowerCase())) ||
      (m.key_terms && m.key_terms.some(k => qLower.includes(k.en.toLowerCase()) || qLower.includes(k.sw.toLowerCase())))
    );
  }

  // 17. Match by selected subject
  if (!matched && STATE.subject && STATE.subject !== 'all') {
    const subjMap = {
      biology: 'Biology',
      physics: 'Physics',
      chemistry: 'Chemistry',
      mathematics: 'Mathematics',
      computer_science: 'Computer Science'
    };
    const targetSubj = subjMap[STATE.subject];
    if (targetSubj) {
      matched = STATE.offlineModules.find(m => m.subject === targetSubj);
    }
  }

  if (!matched) {
    matched = STATE.offlineModules[0] || {
      id: 'algebra_math',
      title_en: 'Algebra & Equations',
      title_sw: 'Aljebra & Mlinganyo wa Hesabu',
      subject: 'Mathematics',
      summary_sw: 'Aljebra hutumia herufi kutatua nambari zilizofichika kwa kusawazisha mizani.',
      summary_en: 'Algebra uses variables to solve unknown values by balancing equations.',
      regional_analogies: {},
      key_terms: [],
      experiment: { title_sw: 'Mizani', title_en: 'Balance', materials_sw: 'Vifaa vya nyumbani', materials_en: 'Materials', steps_sw: 'Sawazisha pande zote', steps_en: 'Balance both sides' },
      quiz: null
    };
  }

  const regKey = STATE.region;
  const regMeta = STATE.regionsMeta[regKey] || STATE.regionsMeta.lake_basin;
  const isSw = STATE.language !== 'en';
  
  const title = isSw ? matched.title_sw : matched.title_en;
  const summary = isSw ? matched.summary_sw : matched.summary_en;

  const regionalDict = matched.regional_analogies ? (matched.regional_analogies[regKey] || matched.regional_analogies.lake_basin) : {};
  const analogy = isSw ? (regionalDict.analogy_sw || matched.analogy_sw) : (regionalDict.analogy_en || matched.analogy_en);
  
  const exp = matched.experiment;
  const quiz = matched.quiz;

  const termsFormatted = matched.key_terms.map(t => `• **${t.en}** ➔ ${t.sw}`).join('\n');

  const text = `### 🔬 ${title}

${isSw ? `Hujambo rafiki yangu mpendwa! 🌟 Nimefurahi sana kusikia swali lako kuhusu eneo letu zuri la **${regMeta.icon} ${regMeta.name_sw}** (Offline Vault):` : `Hello my dear friend! 🌟 I am so proud of your question about **${regMeta.icon} ${regMeta.name_en}** (Offline Vault):`}

${summary}

---

#### 💡 Mfano Halisi wa Eneo Lako (${regMeta.icon} ${isSw ? regMeta.name_sw : regMeta.name_en})
${analogy}

---

#### 📚 Kamusi ya Sayansi (Maneno ya Kujivunia Kujua!)
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
    tactile_description: matched.tactile_audio_description_sw,
    sign_cues: matched.sign_language_visual_cues_sw,
    quiz_data: quiz
  };
}

// --- CONVERSATION / CHAT HISTORY SYSTEM (Local-First Offline Storage) ---
STATE.currentSessionId = null;

function getChatSessions() {
  try {
    return JSON.parse(localStorage.getItem('elewa_chat_sessions') || '[]');
  } catch (e) {
    return [];
  }
}

function saveChatSessions(sessions) {
  try {
    localStorage.setItem('elewa_chat_sessions', JSON.stringify(sessions));
  } catch (e) {
    console.error('Failed to save chat sessions:', e);
  }
}

function openChatHistoryModal() {
  renderChatHistoryList();
  const modal = document.getElementById('chatHistoryModal');
  if (modal) modal.classList.remove('hidden');
}

function closeChatHistoryModal() {
  const modal = document.getElementById('chatHistoryModal');
  if (modal) modal.classList.add('hidden');
}

function renderChatHistoryList() {
  const list = document.getElementById('chatHistoryList');
  if (!list) return;

  const sessions = getChatSessions();
  if (sessions.length === 0) {
    list.innerHTML = `
      <div class="text-center py-8 px-4 text-slate-400 space-y-2">
        <span class="text-3xl">💬</span>
        <p class="text-xs font-semibold text-slate-600">Hakuna historia ya mazungumzo bado.</p>
        <p class="text-[11px]">Uliza swali lolote la Sayansi au Hesabu kuanza mazungumzo mapya!</p>
      </div>
    `;
    return;
  }

  list.innerHTML = sessions.map(sess => {
    const isActive = STATE.currentSessionId === sess.id;
    const langMeta = STATE.languagesMeta[sess.language] || STATE.languagesMeta.sw || { flag: '🇰🇪', native_name: 'Kiswahili' };
    const regMeta = STATE.regionsMeta[sess.region] || STATE.regionsMeta.lake_basin;
    const msgCount = (sess.messages || []).length;
    const dateStr = new Date(sess.timestamp).toLocaleDateString(undefined, { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });

    return `
      <div class="p-3 rounded-2xl border transition-all flex items-center justify-between group ${isActive ? 'bg-emerald-50 border-emerald-300 ring-2 ring-emerald-500/20' : 'bg-slate-50 hover:bg-slate-100 border-slate-200'}">
        <button type="button" onclick="loadChatSession('${sess.id}')" class="flex-1 text-left space-y-1 pr-2">
          <div class="flex items-center space-x-1.5">
            <span class="text-sm">💬</span>
            <p class="font-bold text-xs text-slate-900 line-clamp-1">${escapeHtml(sess.title || 'Mazungumzo ya STEM')}</p>
            ${isActive ? '<span class="text-[9px] bg-emerald-600 text-white font-bold px-1.5 py-0.2 rounded-full flex-shrink-0">Active</span>' : ''}
          </div>
          <div class="flex items-center space-x-2 text-[10px] text-slate-500">
            <span>${langMeta.flag} ${langMeta.native_name}</span>
            <span>•</span>
            <span>${regMeta.icon} ${regMeta.name_sw}</span>
            <span>•</span>
            <span>${msgCount} ujumbe</span>
            <span>•</span>
            <span>${dateStr}</span>
          </div>
        </button>
        <button type="button" onclick="deleteChatSession('${sess.id}', event)" title="Futa mazungumzo haya" class="p-1.5 text-slate-400 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition-all flex-shrink-0">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
        </button>
      </div>
    `;
  }).join('');
}

function loadChatSession(sessionId) {
  const sessions = getChatSessions();
  const session = sessions.find(s => s.id === sessionId);
  if (!session) return;

  STATE.currentSessionId = session.id;
  if (session.language && STATE.languagesMeta[session.language]) {
    STATE.language = session.language;
  }
  if (session.region && STATE.regionsMeta[session.region]) {
    STATE.region = session.region;
  }

  // Clear current messages
  const container = document.getElementById('chatMessages');
  const landingBlock = document.getElementById('welcomeLandingBlock');
  if (container) {
    Array.from(container.children).forEach(child => {
      if (child !== landingBlock) child.remove();
    });
  }

  // Re-render past messages
  if (session.messages && session.messages.length > 0) {
    session.messages.forEach(msg => {
      if (msg.role === 'user') {
        const div = document.createElement('div');
        div.className = 'flex justify-end animate-scale-up';
        div.innerHTML = `
          <div class="bg-brand-600 text-white rounded-2xl rounded-tr-sm px-4 py-2.5 shadow-sm max-w-[88%] text-sm font-medium leading-relaxed">
            ${escapeHtml(msg.text)}
          </div>
        `;
        container.appendChild(div);
      } else if (msg.role === 'assistant') {
        appendAssistantMessage(msg.data || { text: msg.text, source: 'offline_knowledge_vault' }, false);
      }
    });
    updateChatInputPosition(true);
  } else {
    updateChatInputPosition(false);
  }

  closeChatHistoryModal();
  switchTab('chat');
  if (container) container.scrollTop = container.scrollHeight;
}

function deleteChatSession(sessionId, event) {
  if (event) event.stopPropagation();
  let sessions = getChatSessions();
  sessions = sessions.filter(s => s.id !== sessionId);
  saveChatSessions(sessions);

  if (STATE.currentSessionId === sessionId) {
    startNewChat();
  }
  renderChatHistoryList();
}

function clearAllChatHistory() {
  if (!confirm('Je, una uhakika unataka kufuta historia yote ya mazungumzo? Hatua hii haiwezi kurudishwa.')) {
    return;
  }
  localStorage.removeItem('elewa_chat_sessions');
  startNewChat();
  renderChatHistoryList();
}

// Start a New Conversation (Gemini / Copilot Style)
function startNewChat() {
  STATE.currentSessionId = null;
  switchTab('chat');

  // Clear chat messages container, preserving the welcomeLandingBlock
  const container = document.getElementById('chatMessages');
  const landingBlock = document.getElementById('welcomeLandingBlock');
  if (container) {
    Array.from(container.children).forEach(child => {
      if (child !== landingBlock) {
        child.remove();
      }
    });
  }

  // Clear input field and set focus
  const input = document.getElementById('userInput');
  if (input) {
    input.value = '';
    input.focus();
  }

  // Reposition form to the center landing state
  updateChatInputPosition(false);

  // Announce notice
  appendSystemNotice('✨ <b>Gumzo Jipya:</b> Unaweza kuuliza swali jipya la Sayansi au Hesabu.');
}

// Dynamic Chat Form Position (Centered on Landing vs Bottom Docked during Dialogue)
function updateChatInputPosition(hasMessages) {
  const form = document.getElementById('chatForm');
  const landingWrapper = document.getElementById('landingChatFormWrapper');
  const bottomBar = document.getElementById('bottomChatBar');
  const landingBlock = document.getElementById('welcomeLandingBlock');

  if (hasMessages) {
    if (landingBlock) landingBlock.classList.add('hidden');
    if (bottomBar) {
      bottomBar.classList.remove('hidden');
      if (form && form.parentElement !== bottomBar) {
        bottomBar.appendChild(form);
      }
    }
  } else {
    if (landingBlock) landingBlock.classList.remove('hidden');
    if (bottomBar) bottomBar.classList.add('hidden');
    if (form && landingWrapper && form.parentElement !== landingWrapper) {
      landingWrapper.appendChild(form);
    }
  }
}

// UI Rendering Helpers
function appendUserMessage(text) {
  updateChatInputPosition(true);

  // Initialize or retrieve current chat session
  let sessions = getChatSessions();
  if (!STATE.currentSessionId) {
    STATE.currentSessionId = 'session_' + Date.now();
    const newSession = {
      id: STATE.currentSessionId,
      title: text.length > 35 ? text.slice(0, 35) + '...' : text,
      timestamp: new Date().toISOString(),
      language: STATE.language,
      region: STATE.region,
      messages: []
    };
    sessions.unshift(newSession);
  }

  const currentSession = sessions.find(s => s.id === STATE.currentSessionId);
  if (currentSession) {
    currentSession.messages.push({
      role: 'user',
      text: text,
      timestamp: new Date().toISOString()
    });
    saveChatSessions(sessions);
  }

  const container = document.getElementById('chatMessages');
  const div = document.createElement('div');
  div.className = 'flex justify-end animate-scale-up';
  div.innerHTML = `
    <div class="bg-brand-600 text-white rounded-2xl rounded-tr-sm px-4 py-2.5 shadow-sm max-w-[88%] text-sm font-medium leading-relaxed">
      ${escapeHtml(text)}
    </div>
  `;
  container.appendChild(div);
  container.scrollTop = container.scrollHeight;
}

function appendAssistantMessage(data, shouldSave = true) {
  if (shouldSave && STATE.currentSessionId) {
    const sessions = getChatSessions();
    const currentSession = sessions.find(s => s.id === STATE.currentSessionId);
    if (currentSession) {
      currentSession.messages.push({
        role: 'assistant',
        text: data.text,
        data: data,
        timestamp: new Date().toISOString()
      });
      saveChatSessions(sessions);
    }
  }

  const container = document.getElementById('chatMessages');
  const div = document.createElement('div');
  div.className = 'flex items-start space-x-2.5 sm:space-x-3 animate-scale-up';

  const isOffline = data.source === 'local_offline_vault' || data.source === 'offline_knowledge_vault';
  const formattedHtml = parseMarkdownToHtml(data.text);
  const quizDataJson = data.quiz_data ? JSON.stringify(data.quiz_data).replace(/"/g, '&quot;') : '';
  const regMeta = STATE.regionsMeta[data.region || STATE.region] || STATE.regionsMeta.lake_basin;
  const langMeta = STATE.languagesMeta[data.language || STATE.language];

  div.innerHTML = `
    <div class="w-8 h-8 sm:w-9 sm:h-9 rounded-full bg-brand-600 flex items-center justify-center text-white text-sm sm:text-base flex-shrink-0 shadow">
      🌱
    </div>
    <div class="bg-white border border-slate-200 rounded-2xl rounded-tl-sm p-4 sm:p-5 shadow-sm max-w-[94%] w-full text-sm text-slate-800 space-y-3">
      <div class="flex items-center space-x-2 flex-wrap gap-1 mb-1">
        ${isOffline ? '<span class="inline-block bg-amber-100 text-amber-800 text-[10px] font-bold px-2 py-0.5 rounded-full">📦 Offline Vault</span>' : (data.source && data.source.includes('gemma') ? '<span class="inline-block bg-sky-100 text-sky-800 text-[10px] font-bold px-2 py-0.5 rounded-full">💎 Google Gemma 2 (Edge)</span>' : '<span class="inline-block bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded-full">✨ Google Gemini Flash</span>')}
        <span class="inline-block bg-slate-100 text-slate-700 text-[10px] font-bold px-2 py-0.5 rounded-full">${regMeta.icon} ${regMeta.name_sw}</span>
        ${langMeta ? `<span class="inline-block bg-purple-100 text-purple-800 text-[10px] font-bold px-2 py-0.5 rounded-full">${langMeta.flag} ${langMeta.native_name}</span>` : ''}
      </div>
      
      <div class="stem-card leading-relaxed space-y-2">${formattedHtml}</div>

      <!-- Universal Accessibility Cards -->
      ${data.tactile_description && STATE.screenReaderMode ? `
      <div class="bg-blue-50 border border-blue-200 rounded-xl p-3 text-xs space-y-1">
        <p class="font-bold text-blue-900 flex items-center space-x-1">
          <span>👁️</span>
          <span>Screen Reader & Audio Description Mode (Maelezo ya Sauti):</span>
        </p>
        <p class="text-blue-950">${data.tactile_description}</p>
      </div>` : ''}

      ${data.sign_cues && STATE.signLanguageMode ? `
      <div class="bg-purple-50 border border-purple-200 rounded-xl p-3 text-xs space-y-1">
        <p class="font-bold text-purple-900 flex items-center space-x-1">
          <span>🧏</span>
          <span>Vielelezo vya Picha & Mtiririko (Visual Concept & Flowchart Cues):</span>
        </p>
        <p class="text-purple-950">${data.sign_cues}</p>
      </div>` : ''}

      <!-- Interactive Visual Vector Science Diagram -->
      ${data.diagram ? `
      <div class="bg-gradient-to-b from-slate-50 to-emerald-50 border-2 border-emerald-300/80 rounded-2xl p-3.5 space-y-2 shadow-sm">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-2">
            <span class="text-xl">🎨</span>
            <h5 class="font-black text-slate-900 text-xs">${data.diagram.title_sw || 'Mchoro wa Sayansi'}</h5>
          </div>
          <span class="bg-emerald-600 text-white text-[9px] font-bold px-2 py-0.5 rounded-full shadow-xs">Vector Visual (Offline Cached)</span>
        </div>
        <div class="w-full overflow-x-auto rounded-xl border border-slate-200/60 bg-white p-1">
          ${data.diagram.svg}
        </div>
      </div>` : ''}
      
      <div class="pt-2 border-t border-slate-100 flex flex-wrap gap-2 text-xs font-semibold">
        <button onclick="speakText('${encodeURIComponent(data.text + (data.tactile_description ? ' ' + data.tactile_description : ''))}')" class="px-2.5 py-1.5 rounded-xl bg-purple-50 hover:bg-purple-100 text-purple-900 border border-purple-200 flex items-center space-x-1 transition-all">
          <span>🔊</span>
          <span>Sikiliza kwa Sauti</span>
        </button>
        <button onclick="stopSpeech()" class="px-2 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center space-x-1 transition-all" title="Simamisha Sauti">
          <span>⏹️</span>
        </button>
        <button onclick="executeAgentQuery('Eleza hili tena kwa mifano rahisi sana ya eneo langu', true)" class="px-2.5 py-1.5 rounded-xl bg-slate-100 hover:bg-brand-50 hover:text-brand-700 text-slate-700 flex items-center space-x-1 transition-all">
          <span>💡</span>
          <span>Rahisisha</span>
        </button>
        ${data.quiz_data ? `
        <button onclick="openQuizModal('${quizDataJson}', '${escapeHtml(data.topic || 'STEM')}')" class="px-2.5 py-1.5 rounded-xl bg-brand-600 hover:bg-brand-700 text-white flex items-center space-x-1 shadow-sm transition-all">
          <span>🎯</span>
          <span>Fanya Jaribio</span>
        </button>` : ''}
      </div>

      <!-- Recommended Next Topics / Learning Pathway -->
      ${data.related_topics && data.related_topics.length > 0 ? `
      <div class="pt-2 border-t border-slate-100 space-y-1.5">
        <p class="text-[11px] font-bold text-slate-600 flex items-center space-x-1">
          <span>🚀</span>
          <span>Mada Zinazofuata (Next Steps to Explore):</span>
        </p>
        <div class="flex flex-wrap gap-1.5">
          ${data.related_topics.map(rt => `
            <button onclick="executeAgentQuery('${escapeHtml(rt.prompt)}', false)" class="text-[11px] font-bold px-2.5 py-1 rounded-lg bg-emerald-50 hover:bg-emerald-100 text-emerald-900 border border-emerald-300 flex items-center space-x-1 transition-all shadow-xs">
              <span>${rt.icon || '👉'}</span>
              <span>${STATE.language === 'en' ? rt.title_en : rt.title_sw}</span>
            </button>
          `).join('')}
        </div>
      </div>` : ''}

      <!-- Stakeholder Quick Reaction & Feedback Bar -->
      <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-500">
        <div class="flex items-center space-x-1.5">
          <span class="font-medium">Umeelewa somo hili?</span>
          <button onclick="quickReact('understood', '${escapeHtml(data.topic || 'STEM')}')" class="hover:scale-125 transition-transform" title="Nimeelewa vizuri!">😃</button>
          <button onclick="quickReact('simplify', '${escapeHtml(data.topic || 'STEM')}')" class="hover:scale-125 transition-transform" title="Rahisisha zaidi">🤔</button>
          <button onclick="quickReact('voice', '${escapeHtml(data.topic || 'STEM')}')" class="hover:scale-125 transition-transform" title="Sauti nzuri">🔊</button>
        </div>
        <button onclick="openFeedbackModal('student')" class="text-brand-700 hover:text-brand-800 font-bold flex items-center space-x-1">
          <span>💬</span>
          <span>Toa Maoni</span>
        </button>
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
      <span>Mwalimu rafiki anakuandalia jibu tamu la ${regMeta.icon} ${regMeta.name_sw}...</span>
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

function speakText(rawText) {
  if (!('speechSynthesis' in window)) return;

  window.speechSynthesis.cancel();

  let cleanText = decodeURIComponent(rawText)
    .replace(/#{1,6}\s?/g, '')
    .replace(/\*\*/g, '')
    .replace(/\*/g, '')
    .replace(/---/g, '')
    .replace(/•/g, '')
    .replace(/\[.*?\]\(.*?\)/g, '')
    .replace(/https?:\/\/\S+/g, '')
    .replace(/➔/g, 'ambayo kwa kiingereza ni')
    .trim();

  if (cleanText.length > 500) {
    cleanText = cleanText.substring(0, 500) + '...';
  }

  const utterance = new SpeechSynthesisUtterance(cleanText);
  utterance.rate = 0.95;
  utterance.pitch = 1.05;

  const langMeta = STATE.languagesMeta[STATE.language];
  utterance.lang = langMeta ? langMeta.tts_locale : (STATE.language === 'en' ? 'en-US' : 'sw-KE');

  STATE.activeSpeechUtterance = utterance;
  window.speechSynthesis.speak(utterance);
}

function stopSpeech() {
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
}

function toggleVoiceInput() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    alert('Kifaa hiki hakina huduma ya sauti ya mtandao. Tafadhali andika swali lako.');
    return;
  }

  const overlay = document.getElementById('voiceOverlayModal');
  const transcriptEl = document.getElementById('voiceLiveTranscript');
  overlay.classList.remove('hidden');
  transcriptEl.innerText = '"Ninasubiri sauti yako... Ongea sasa!"';

  try {
    const recognition = new SpeechRecognition();
    const langMeta = STATE.languagesMeta[STATE.language];
    recognition.lang = langMeta ? langMeta.tts_locale : (STATE.language === 'en' ? 'en-US' : 'sw-KE');
    recognition.interimResults = true;
    recognition.continuous = false;

    STATE.activeSpeechRecognition = recognition;

    recognition.onresult = (event) => {
      let interim = '';
      let final = '';

      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          final += event.results[i][0].transcript;
        } else {
          interim += event.results[i][0].transcript;
        }
      }

      if (interim) transcriptEl.innerText = `"${interim}..."`;

      if (final) {
        transcriptEl.innerText = `"${final}"`;
        document.getElementById('userInput').value = final;
        setTimeout(() => {
          overlay.classList.add('hidden');
          handleChatSubmit();
        }, 500);
      }
    };

    recognition.onerror = () => {
      transcriptEl.innerText = 'Sauti haijasikika vizuri. Tafadhali bonyeza tena au andika.';
      setTimeout(() => overlay.classList.add('hidden'), 1500);
    };

    recognition.onend = () => {
      setTimeout(() => {
        if (!overlay.classList.contains('hidden')) overlay.classList.add('hidden');
      }, 2000);
    };

    recognition.start();
  } catch (err) {
    overlay.classList.add('hidden');
  }
}

function cancelVoiceRecognition() {
  if (STATE.activeSpeechRecognition) {
    try { STATE.activeSpeechRecognition.stop(); } catch (e) {}
  }
  document.getElementById('voiceOverlayModal').classList.add('hidden');
}

// Offline Vault Rendering
function renderVault() {
  const container = document.getElementById('vaultModulesGrid');
  if (!container) return;
  const isSw = STATE.language !== 'en';
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

          ${m.tactile_audio_description_sw && STATE.screenReaderMode ? `
          <p class="text-[11px] text-blue-900 bg-blue-50 p-2 rounded-xl border border-blue-100 line-clamp-2"><b>👁️ Screen Reader / Audio Description:</b> ${m.tactile_audio_description_sw}</p>` : ''}

          ${m.sign_language_visual_cues_sw && STATE.signLanguageMode ? `
          <p class="text-[11px] text-purple-900 bg-purple-50 p-2 rounded-xl border border-purple-100 line-clamp-2"><b>🧏 Visual Concept Cues:</b> ${m.sign_language_visual_cues_sw}</p>` : ''}
        </div>

        <div class="pt-2 border-t border-slate-100 flex space-x-2">
          <button onclick="openOfflineModuleInChat('${m.id}')" class="flex-1 bg-brand-50 hover:bg-brand-100 text-brand-800 text-xs font-bold py-2 rounded-xl text-center transition-all">
            Soma Somo
          </button>
          <button onclick="speakText('${encodeURIComponent((isSw ? m.summary_sw : m.summary_en) + ' Mfano: ' + localAnalogy + (m.tactile_audio_description_sw ? ' ' + m.tactile_audio_description_sw : ''))}')" class="bg-purple-50 hover:bg-purple-100 text-purple-900 border border-purple-200 text-xs font-bold px-3 py-2 rounded-xl transition-all" title="Sikiliza kwa Sauti">
            🔊
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
  if (STATE.autoSpeak) speakText(answer.text);
}

// Student Profile
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
        <p class="text-xs text-slate-500 italic">Bado hujaanza majaribio. Uliza maswali kwa sauti na ufanye quizzes ili kukuza kiwango chako cha uelewa!</p>
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
    const isSw = STATE.language !== 'en';
    question.innerText = isSw ? quiz.question_sw : quiz.question_en;

    if (STATE.autoSpeak) {
      speakText((isSw ? 'Swali la kujipima: ' : 'Quiz Question: ') + (isSw ? quiz.question_sw : quiz.question_en));
    }

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
  const isSw = STATE.language !== 'en';
  const isCorrect = (selectedIndex === quiz.correct_index);

  const feedback = document.getElementById('quizFeedback');
  feedback.classList.remove('hidden');

  const feedbackSpokenText = isCorrect 
    ? (isSw ? `Hongera sana rafiki yangu! Uko sahihi kabisa! ${quiz.explanation_sw}` : `Awesome my dear friend! That is correct! ${quiz.explanation_en}`)
    : (isSw ? `Uko karibu sana rafiki yangu! Usijali, jaribu tena: ${quiz.explanation_sw}` : `Almost there my friend! Keep going: ${quiz.explanation_en}`);

  if (isCorrect) {
    feedback.className = 'p-3 rounded-xl text-xs font-semibold leading-relaxed bg-emerald-100 text-emerald-900 border border-emerald-300';
    feedback.innerHTML = `🎉 <b>${isSw ? 'Hongera sana rafiki yangu! Uko sahihi!' : 'Awesome my friend! That is correct!'}</b><br>${isSw ? quiz.explanation_sw : quiz.explanation_en}`;
  } else {
    feedback.className = 'p-3 rounded-xl text-xs font-semibold leading-relaxed bg-amber-100 text-amber-900 border border-amber-300';
    feedback.innerHTML = `💡 <b>${isSw ? 'Uko karibu sana! Jaribu tena:' : 'Almost there! Try again:'}</b><br>${isSw ? quiz.explanation_sw : quiz.explanation_en}`;
  }

  if (STATE.autoSpeak) speakText(feedbackSpokenText);

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
      updateParentDigestPreview();
    }).catch(err => console.log('Quiz sync notice:', err));
  }
}

function closeQuizModal() {
  document.getElementById('quizModal').classList.add('hidden');
  STATE.currentQuiz = null;
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
}

// Header Status Pill & Live Synchronization
function updateHeaderStatusPill() {
  const countryFlags = {
    Kenya: '🇰🇪 Kenya',
    Tanzania: '🇹🇿 Tanzania',
    Uganda: '🇺🇬 Uganda',
    Rwanda: '🇷🇼 Rwanda',
    Nigeria: '🇳🇬 Nigeria',
    Ghana: '🇬🇭 Ghana',
    'South Africa': '🇿🇦 South Africa',
    Ethiopia: '🇪🇹 Ethiopia'
  };

  const dict = I18N[STATE.language] || I18N.sw;
  const isEn = STATE.language === 'en';

  const reg = STATE.regionsMeta[STATE.region] || STATE.regionsMeta.lake_basin;
  const langMeta = STATE.languagesMeta[STATE.language] || { flag: '🇰🇪', native_name: 'Kiswahili' };

  // Update menu profile summary card
  const summaryEl = document.getElementById('menuProfileSummaryText');
  if (summaryEl) {
    const cName = countryFlags[STATE.country] || `🌍 ${STATE.country}`;
    const sName = dict.subjects?.[STATE.subject] || (isEn ? '🌟 All STEM' : '🌟 Masomo Yote');
    const gName = dict.grades?.[STATE.gradeLevel] || (isEn ? '🌿 Grade 4–6' : '🌿 Darasa 4–6');
    const rName = `${reg.icon} ${(isEn ? reg.name_en : reg.name_sw).split(' ')[0]}`;
    const lName = `${langMeta.flag} ${langMeta.native_name.split(' ')[0]}`;
    summaryEl.innerText = `${cName} • ${sName} • ${gName} • ${rName} • ${lName}`;
  }
  
  // Also sync auto-speak menu button text/icon
  const autoMenuText = document.getElementById('autoSpeakMenuText');
  const autoMenuIcon = document.getElementById('autoSpeakMenuIcon');
  if (autoMenuText && autoMenuIcon) {
    autoMenuText.innerText = STATE.autoSpeak ? (dict.voice_label_on || 'Sauti: Washa') : (dict.voice_label_off || 'Sauti: Zima');
    autoMenuIcon.innerText = STATE.autoSpeak ? '🔊' : '🔇';
  }


  // Sync agent mode menu text
  const modeTextEl = document.getElementById('agentModeMenuText');
  if (modeTextEl) {
    const mode = STATE.agentMode || 'creative';
    if (mode === 'creative') modeTextEl.innerText = '🎨 Hadithi (Temp 0.75)';
    else if (mode === 'balanced') modeTextEl.innerText = '⚖️ Mizani (Temp 0.40)';
    else modeTextEl.innerText = '🎯 Sahihi (Temp 0.10)';
  }
}

// Teaching Style Handler (Stories vs Direct)
function toggleAgentMode() {
  const modes = ['creative', 'balanced', 'precise'];
  const current = STATE.agentMode || 'creative';
  const next = modes[(modes.indexOf(current) + 1) % modes.length];
  STATE.agentMode = next;
  updateHeaderStatusPill();
  const modeLabelsSw = {
    creative: '🎨 Hadithi na Mifano ya Kusisimua',
    balanced: '⚖️ Uwiano wa Hadithi na Ufafanuzi',
    precise: '📐 Maelezo Mafupi na Hesabu Halisi'
  };
  appendSystemNotice(`💡 <b>Mtindo wa Kufundisha:</b> Umewekwa kuwa <b>${modeLabelsSw[next] || next}</b>.`);
}

// Unified App Menu Dropdown Handlers
function toggleAppMenuDropdown(e) {
  if (e) e.stopPropagation();
  const menu = document.getElementById('appMenuDropdown');
  const chevron = document.getElementById('appMenuChevron');
  if (menu) {
    const isHidden = menu.classList.contains('hidden');
    if (isHidden) {
      menu.classList.remove('hidden');
      if (chevron) chevron.classList.add('rotate-180');
      updateHeaderStatusPill();
    } else {
      menu.classList.add('hidden');
      if (chevron) chevron.classList.remove('rotate-180');
    }
  }
}

function closeAppMenuDropdown() {
  const menu = document.getElementById('appMenuDropdown');
  const chevron = document.getElementById('appMenuChevron');
  if (menu) menu.classList.add('hidden');
  if (chevron) chevron.classList.remove('rotate-180');
}

// Close App Menu dropdown when clicking anywhere outside
document.addEventListener('click', (e) => {
  const container = document.getElementById('appMenuContainer');
  if (container && !container.contains(e.target)) {
    closeAppMenuDropdown();
  }
});

// Languages Info Modal Handlers
function openLanguagesInfoModal() {
  const modal = document.getElementById('languagesInfoModal');
  if (modal) modal.classList.remove('hidden');
}

function closeLanguagesInfoModal() {
  const modal = document.getElementById('languagesInfoModal');
  if (modal) modal.classList.add('hidden');
}

// PWA Install Handlers
let deferredPWAInstallPrompt = null;
window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPWAInstallPrompt = e;
});

function promptPWAInstall() {
  if (deferredPWAInstallPrompt) {
    deferredPWAInstallPrompt.prompt();
    deferredPWAInstallPrompt.userChoice.then((choiceResult) => {
      if (choiceResult.outcome === 'accepted') {
        appendSystemNotice('📲 <b>Hongera!</b> ElewaSTEM imewekwa kwenye skrini ya simu yako.');
      }
      deferredPWAInstallPrompt = null;
    });
  } else {
    const modal = document.getElementById('installAppModal');
    if (modal) modal.classList.remove('hidden');
  }
}

function closeInstallAppModal() {
  const modal = document.getElementById('installAppModal');
  if (modal) modal.classList.add('hidden');
}

// Interactive Languages Modal Handlers
function openLanguagesModal() {
  const modal = document.getElementById('languagesModal');
  if (modal) modal.classList.remove('hidden');
}

function closeLanguagesModal() {
  const modal = document.getElementById('languagesModal');
  if (modal) modal.classList.add('hidden');
}

function selectLanguageFromModal(langCode) {
  changeLanguage(langCode);
  closeLanguagesModal();
}

// Dynamic Multilingual & STEM Prompt Placeholder Cycling
const PLACEHOLDER_PROMPTS = [
  "Ongea au andika kwa Kiswahili, Sheng, English, Yoruba, Hausa...",
  "Uliza swali: Mimea inavyopika chakula kwa jua? 🌿",
  "Uliza swali: Kwanini samaki wanatumia matamvua ziwani? 🐟",
  "Uliza swali: Saketi za umeme na taa hufanya kazi vipi? ⚡",
  "Uliza swali: Jinsi ya kugawa sehemu katika hesabu? 📐",
  "Ask any Science or Math question in your African language... 🎤"
];
let currentPlaceholderIndex = 0;
function initDynamicPlaceholder() {
  const input = document.getElementById('userInput');
  if (!input) return;
  setInterval(() => {
    if (document.activeElement !== input && input.value.trim() === '') {
      currentPlaceholderIndex = (currentPlaceholderIndex + 1) % PLACEHOLDER_PROMPTS.length;
      input.placeholder = PLACEHOLDER_PROMPTS[currentPlaceholderIndex];
    }
  }, 4200);
}


