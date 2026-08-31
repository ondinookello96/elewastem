"""
ElewaSTEM Pan-African Languages & Open NLP Integration Engine
Connects frontier multilingual LLMs (Google Gemini Flash) with African NLP innovations (Masakhane, Lelapa AI, Suno/AfriSpeech, NLLB).
"""

from typing import Dict, List, Any

# Pan-African Language Registry covering major linguistic families across Africa
AFRICAN_LANGUAGES: Dict[str, Dict[str, Any]] = {
    "sw": {
        "code": "sw",
        "name": "Kiswahili",
        "native_name": "Kiswahili",
        "flag": "🇰🇪 🇹🇿",
        "region": "East & Central Africa",
        "countries": ["Kenya", "Tanzania", "Uganda", "DR Congo", "Rwanda", "Burundi"],
        "tutor_title": "Mwalimu wa STEM",
        "motto": "Usimeze, Elewa!",
        "greeting": "Habari! Mimi ni mwalimu wako wa Sayansi na Hesabu.",
        "tts_locale": "sw-KE",
        "nlp_origin": "Bantu / Swahili Coast"
    },
    "sheng": {
        "code": "sheng",
        "name": "Sheng",
        "native_name": "Sheng / Mtaani Mix",
        "flag": "🇰🇪",
        "region": "Urban East Africa",
        "countries": ["Kenya"],
        "tutor_title": "Msee wa STEM",
        "motto": "Usicram, Elewa!",
        "greeting": "Niaje! Niko hapa kukuchanganulia science na maths bila stress.",
        "tts_locale": "sw-KE",
        "nlp_origin": "Urban Hybrid (Swahili-English-Indigenous)"
    },
    "yo": {
        "code": "yo",
        "name": "Yoruba",
        "native_name": "Èdè Yorùbá",
        "flag": "🇳🇬 🇧🇯",
        "region": "West Africa",
        "countries": ["Nigeria", "Benin", "Togo"],
        "tutor_title": "Olùkọ́ STEM",
        "motto": "Má kọ́ sórí, Ṣe àgbéyẹ̀wò!",
        "greeting": "Báwo ni! Èmi ni olùkọ́ ìmọ̀ sáyẹ́nsì àti ìṣirò rẹ.",
        "tts_locale": "yo-NG",
        "nlp_origin": "Niger-Congo (Volta-Niger)"
    },
    "ha": {
        "code": "ha",
        "name": "Hausa",
        "native_name": "Harshen Hausa",
        "flag": "🇳🇬 🇳🇪",
        "region": "West & Sahelian Africa",
        "countries": ["Nigeria", "Niger", "Ghana", "Chad", "Cameroon"],
        "tutor_title": "Malamin STEM",
        "motto": "Kada ka haddace kawai, Fahimta!",
        "greeting": "Sannu! Ni ne malamin ku na Kimiyya da Lissafi.",
        "tts_locale": "ha-NG",
        "nlp_origin": "Afroasiatic (Chadic)"
    },
    "ig": {
        "code": "ig",
        "name": "Igbo",
        "native_name": "Asụsụ Igbo",
        "flag": "🇳🇬",
        "region": "West Africa",
        "countries": ["Nigeria"],
        "tutor_title": "Onye Nkuzi STEM",
        "motto": "Akwala ya n'isi, Ghọta ya!",
        "greeting": "Nnọọ! Abụ m onye nkuzi Sayensị na Mgbakọ na Mwepụ gị.",
        "tts_locale": "ig-NG",
        "nlp_origin": "Niger-Congo (Igboid)"
    },
    "pcm": {
        "code": "pcm",
        "name": "Nigerian Pidgin",
        "native_name": "Naija Pidgin",
        "flag": "🇳🇬 🇬🇭",
        "region": "West Africa (Anglophone)",
        "countries": ["Nigeria", "Ghana", "Cameroon", "Sierra Leone"],
        "tutor_title": "STEM Ticha",
        "motto": "No cram am, Make you understand am!",
        "greeting": "How far! I be your Science and Maths teacher wey go break down everything easy-easy.",
        "tts_locale": "en-NG",
        "nlp_origin": "Creole / Lingua Franca"
    },
    "am": {
        "code": "am",
        "name": "Amharic",
        "native_name": "አማርኛ (Amarəñña)",
        "flag": "🇪🇹",
        "region": "Horn of Africa",
        "countries": ["Ethiopia"],
        "tutor_title": "የSTEM መምህር",
        "motto": "አትሸምድድ፣ ተረዳው!",
        "greeting": "ሰላም! የሳይንስ እና ሂሳብ አስተማሪህ ነኝ።",
        "tts_locale": "am-ET",
        "nlp_origin": "Afroasiatic (Semitic)"
    },
    "om": {
        "code": "om",
        "name": "Oromo",
        "native_name": "Afaan Oromoo",
        "flag": "🇪🇹 🇰🇪",
        "region": "Horn & East Africa",
        "countries": ["Ethiopia", "Kenya"],
        "tutor_title": "Barsiisaa STEM",
        "motto": "Qomatti hin qabatin, Hubadhu!",
        "greeting": "Akkam! Ani barsiisaa Saayinsii fi Herregaa keeti.",
        "tts_locale": "om-ET",
        "nlp_origin": "Afroasiatic (Cushitic)"
    },
    "so": {
        "code": "so",
        "name": "Somali",
        "native_name": "Af-Soomaali",
        "flag": "🇸🇴 🇩🇯 🇰🇪",
        "region": "Horn of Africa",
        "countries": ["Somalia", "Djibouti", "Kenya", "Ethiopia"],
        "tutor_title": "Macallinka STEM",
        "motto": "Ha xafidin, Faham!",
        "greeting": "Ku soo dhawoow! Waxaan ahay macallinkaaga Sayniska iyo Xisaabta.",
        "tts_locale": "so-SO",
        "nlp_origin": "Afroasiatic (Cushitic)"
    },
    "zu": {
        "code": "zu",
        "name": "isiZulu",
        "native_name": "isiZulu",
        "flag": "🇿🇦 🇸🇿",
        "region": "Southern Africa",
        "countries": ["South Africa", "Eswatini", "Lesotho"],
        "tutor_title": "Uthisha we-STEM",
        "motto": "Ungabambi ngekhanda kuphela, Qonda!",
        "greeting": "Sawubona! Nginguthisha wakho weSayensi neziBalo.",
        "tts_locale": "zu-ZA",
        "nlp_origin": "Niger-Congo (Nguni)"
    },
    "xh": {
        "code": "xh",
        "name": "isiXhosa",
        "native_name": "isiXhosa",
        "flag": "🇿🇦",
        "region": "Southern Africa",
        "countries": ["South Africa"],
        "tutor_title": "Utitshala we-STEM",
        "motto": "Musa ukunkqaya nje, Qonda!",
        "greeting": "Molo! Ndingutitshala wakho wezeNzululwazi neziBalo.",
        "tts_locale": "xh-ZA",
        "nlp_origin": "Niger-Congo (Nguni)"
    },
    "rw": {
        "code": "rw",
        "name": "Kinyarwanda",
        "native_name": "Ikinyarwanda",
        "flag": "🇷🇼",
        "region": "Central & East Africa",
        "countries": ["Rwanda", "DR Congo", "Uganda"],
        "tutor_title": "Mwalimu wa STEM",
        "motto": "Ntugafate mu mutwe gusa, Sobanukirwa!",
        "greeting": "Muraho! Ndi mwarimu wawe wa Siyansi n'Imibare.",
        "tts_locale": "rw-RW",
        "nlp_origin": "Niger-Congo (Bantu)"
    },
    "lg": {
        "code": "lg",
        "name": "Luganda",
        "native_name": "Oluganda",
        "flag": "🇺🇬",
        "region": "East Africa",
        "countries": ["Uganda"],
        "tutor_title": "Omusomesa wa STEM",
        "motto": "Tokwata bukwasi mu mutwe, Tegeera!",
        "greeting": "Ki kati! Nze musomesa wo owa Sayansi ne Kubala.",
        "tts_locale": "lg-UG",
        "nlp_origin": "Niger-Congo (Bantu)"
    },
    "tw": {
        "code": "tw",
        "name": "Twi / Akan",
        "native_name": "Twi (Asante / Akuapem)",
        "flag": "🇬🇭",
        "region": "West Africa",
        "countries": ["Ghana", "Ivory Coast"],
        "tutor_title": "STEM Kyerɛkyerɛfoɔ",
        "motto": "Nkyere wo tirim kɛkɛ, Te aseɛ!",
        "greeting": "Akwaaba! Meyɛ wo Sayense ne Nkontabuo kyerɛkyerɛfoɔ.",
        "tts_locale": "ak-GH",
        "nlp_origin": "Niger-Congo (Kwa)"
    },
    "sn": {
        "code": "sn",
        "name": "Shona",
        "native_name": "chiShona",
        "flag": "🇿🇼 🇲🇿",
        "region": "Southern Africa",
        "countries": ["Zimbabwe", "Mozambique", "Botswana"],
        "tutor_title": "Mudzidzisi we-STEM",
        "motto": "Usangobata nemusoro, Nzwisisa!",
        "greeting": "Mhoroi! Ndini mudzidzisi wenyu weSainzi neMasvomhu.",
        "tts_locale": "sn-ZW",
        "nlp_origin": "Niger-Congo (Bantu)"
    },
    "ln": {
        "code": "ln",
        "name": "Lingala",
        "native_name": "Lingála",
        "flag": "🇨🇩 🇨🇬",
        "region": "Central Africa",
        "countries": ["DR Congo", "Republic of the Congo", "Angola", "Central African Republic"],
        "tutor_title": "Molakisi ya STEM",
        "motto": "Kanga na motó te, Yebá!",
        "greeting": "Mbote! Nazali molakisi na yo ya Siyansi mpe Mituya.",
        "tts_locale": "ln-CD",
        "nlp_origin": "Niger-Congo (Bantu)"
    },
    "en": {
        "code": "en",
        "name": "English",
        "native_name": "English (African Context)",
        "flag": "🌍",
        "region": "Pan-African Lingua Franca",
        "countries": ["All African Countries"],
        "tutor_title": "STEM Tutor",
        "motto": "Don't Cram, Understand!",
        "greeting": "Hello! I am your STEM tutor ready to explore science and math through your local environment.",
        "tts_locale": "en-US",
        "nlp_origin": "Indo-European / Global"
    }
}


def get_all_african_languages() -> List[Dict[str, Any]]:
    return list(AFRICAN_LANGUAGES.values())


def get_language_meta(lang_code: str) -> Dict[str, Any]:
    return AFRICAN_LANGUAGES.get(lang_code.lower(), AFRICAN_LANGUAGES["sw"])
