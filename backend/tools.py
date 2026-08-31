"""
ElewaSTEM Specialized Agent Tools with Deep Hyper-Local African Ecosystems, Stakeholder Resources, and Universal Accessibility
Includes Screen Reader & Audio Description Mode for visually impaired learners, visual concept & flowchart cues for deaf learners, and dyslexia adaptations.
"""

from typing import Dict, List, Any

# Regional Eco-Zones & Localities definition
REGIONS = {
    "lake_basin": {
        "id": "lake_basin",
        "name_sw": "Bonde la Ziwa (Kisumu & Lake Victoria)",
        "name_en": "Lake Victoria Basin (Kisumu, Mwanza, Entebbe)",
        "locality_name": "Kisumu / Ziwa Victoria",
        "icon": "🏞️",
        "local_species": [
            "Samaki Ngege (Tilapia)",
            "Mbuta (Nile Perch)",
            "Magugu Maji / Akech (Water Hyacinth)",
            "Mboga za kienyeji: Osuga (Managu) & Mitoo",
            "Mianzi ya Papyrus ya Dunga Beach",
            "Mti wa Yago (Kigelia africana)"
        ],
        "key_ecosystems": "Ziwa Victoria, Samaki Ngege & Mbuta, Magugu Maji (Water Hyacinth), Mboga za kienyeji (Osuga & Mitoo), Upepo wa Ziwani"
    },
    "coastal": {
        "id": "coastal",
        "name_sw": "Pwani na Bahari (Mombasa, Kilifi, Zanzibar)",
        "name_en": "Coastal & Ocean Zone (Mombasa, Malindi, Dar)",
        "locality_name": "Mombasa & Pwani",
        "icon": "🌊",
        "local_species": [
            "Minazi (Coconut Palms)",
            "Mikoko (Mangrove Trees with breathing roots)",
            "Miti ya Mbuyu (Baobab)",
            "Miamba ya Matumbawe (Coral Reefs)",
            "Mkorosho (Cashew Nuts)"
        ],
        "key_ecosystems": "Minazi, Mikoko yenye mizizi ya kupumulia (Pneumatophores), Bahari ya Hindi, Mashamba ya Chumvi, Upepo wa Bahari"
    },
    "highlands": {
        "id": "highlands",
        "name_sw": "Nyanda za Juu & Kilimo (Nakuru, Mt. Kenya, Eldoret)",
        "name_en": "Highlands & Agricultural Belt (Eldoret, Kericho, Arusha)",
        "locality_name": "Nakuru / Eldoret / Mt. Kenya",
        "icon": "⛰️",
        "local_species": [
            "Majani ya Chai (Tea bushes)",
            "Mahindi & Maharagwe (Legume Nitrogen fixers)",
            "Miti ya Grevillea & Cypress",
            "Udongo mwekundu wa Volkano",
            "Mito ya Milima (Mountain streams)"
        ],
        "key_ecosystems": "Mashamba ya Chai & Mahindi, Milima, Mito inayotiririka, Mvua nyingi, Udongo wa Volkano"
    },
    "arid": {
        "id": "arid",
        "name_sw": "Maeneo Kavu & Ukame (Turkana, Garissa, Marsabit)",
        "name_en": "Arid & Pastoralist ASAL (Turkana, Garissa, Wajir)",
        "locality_name": "Turkana / Garissa / Wajir",
        "icon": "☀️",
        "local_species": [
            "Mshikio / Mgunga (Acacia tortilis with 30m taproots)",
            "Ngamia (Camels with water-retaining blood cells)",
            "Mbuyu (Water-storing Baobab)",
            "Mimea ya Mkonge (Sisal) & Ukwaju (Tamarind)",
            "Visima vya Maji ya Ardhini (Aquifer boreholes)"
        ],
        "key_ecosystems": "Jua kali, Miti ya Acacia yenye nta, Ngamia, Visima vya maji ya ardhini, Nishati ya Solar"
    },
    "urban": {
        "id": "urban",
        "name_sw": "Mijini (Nairobi, Kampala, Dar es Salaam)",
        "name_en": "Urban & Metropolitan (Nairobi, Kampala, Lagos)",
        "locality_name": "Nairobi & Mijini",
        "icon": "🏙️",
        "local_species": [
            "Miti ya Jacaranda & Nandi Flame",
            "Mimea ya bustani za mijini (Urban balcony gardens)",
            "Ndege wa Korongo (Marabou Storks)",
            "Taa za barabarani za Solar PV"
        ],
        "key_ecosystems": "Miti ya jiji inayofyonza moshi wa magari, Taa za barabarani za solar, Matatu electronics, Barabara za lami"
    }
}


OFFLINE_STEM_VAULT = [
    {
        "id": "photosynthesis",
        "title_en": "Photosynthesis: How Plants Make Food",
        "title_sw": "Usanisinuru: Jinsi Mimea Inavyotengeneza Chakula",
        "subject": "Biology",
        "cbc_strand": "Living Things & Life Processes (Grade 5/6 Science)",
        "summary_en": "Plants use sunlight, water, and carbon dioxide from the air to produce glucose energy and release fresh oxygen.",
        "summary_sw": "Mimea hutumia mwangaza wa jua, maji kutoka ardhini, na hewa ya kaboni kutengeneza chakula chake (glukosi) huku ikitoa hewa safi ya oksijeni.",
        
        # Universal Accessibility Bridges
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika jani bichi mkononi mwako. Hisi upande wa juu ulivyo laini na bapa—sehemu hii inavuta mwangaza wa jua. Geuza jani upande wa chini, utahisi mishipa midogo midogo inayopitisha maji na mashimo madogo yasiyoonekana (stomata) yanayovuta hewa ya kaboni na kutoa oksijeni safi!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Mmea unaochipua] + [Ishara ya Jua linalong'aa] + [Ishara ya Kupumua na Kutoa Hewa]. Angalia mchoro wa mishale: Jua na Maji yanaingia ndani ya jani ➔ Chakula (Sukari) kinabaki ndani ➔ Viputo vya Oksijeni vinatoka nje.",
        
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu kando ya Ziwa Victoria, tazama magugu maji (Water Hyacinth / Akech) au mboga za kienyeji kama Osuga (Managu) na Mitoo! Majani yake mapana ya kijani yamejaa 'Klorofili' inayofyonza mwangaza mkali wa jua la ziwani na maji tele ya Ziwa Victoria ili kupika virutubisho na kutoa hewa safi ya oksijeni inayosaidia samaki Ngege (Tilapia) kupumua ziwani!",
                "analogy_en": "In Kisumu along Lake Victoria, look at the broad leaves of Water Hyacinth (Akech) and indigenous greens like Osuga (Managu) and Mitoo! Their rich green chlorophyll absorbs bright equatorial lake sunlight and water to synthesize nutrients while oxygenating the water for tilapia fish (Ngege)!"
            },
            "coastal": {
                "analogy_sw": "Kule Mombasa na Kilifi, tazama minazi na mikoko (mangroves)! Majani marefu ya mnazi yanafanya kazi kama paneli kubwa za jua za kijani, yakifyonza unyevu wa bahari na mwangaza wa jua la pwani ili kutengeneza maji matamu ya dafu na nyama ya nazi!",
                "analogy_en": "In Mombasa and Kilifi, observe the tall coconut palms and coastal mangroves! The palm fronds act as giant green solar panels, harnessing coastal sunshine and soil moisture to produce sweet coconut water!"
            },
            "highlands": {
                "analogy_sw": "Kule Nakuru, Eldoret au Kericho, fikiria shamba la majani ya chai au mahindi! Kila jani la kijani linatumia unyevu wa ukungu wa asubuhi milimani na mwangaza wa jua kupika glukosi inayokuza mahindi makubwa!",
                "analogy_en": "In the highlands of Nakuru, Eldoret, or Kericho, picture lush tea bushes and maize stalks. Each leaf uses morning highland mist and sunlight to brew glucose and fuel corn development!"
            },
            "arid": {
                "analogy_sw": "Kule Turkana na Garissa, miti ya Mgunga/Mshikio (Acacia) ina majani madogo sana yenye tabaka la nta ili kuzuia maji yasipotee kwa mvuke (transpiration), huku mizizi mirefu ikivuta maji chini ya ardhi ili kupika chakula chini ya jua kali!",
                "analogy_en": "In arid regions like Turkana or Garissa, acacia trees have tiny waxy leaves that prevent moisture loss from transpiration, while taproots reach deep water aquifers to power photosynthesis under intense heat!"
            },
            "urban": {
                "analogy_sw": "Kwenye jiji kama Nairobi, miti ya kando ya barabara (kama Jacaranda) inafyonza hewa ya moshi wa magari (Carbon Dioxide) na kuibadilisha kuwa hewa safi ya oksijeni kwa wakazi wa jiji!",
                "analogy_en": "In cities like Nairobi, avenue trees like Jacaranda absorb vehicle exhaust fumes (Carbon Dioxide) and convert it into fresh oxygen for urban residents!"
            }
        },
        "key_terms": [
            {"en": "Chlorophyll", "sw": "Klorofili (Rangi ya kijani inayovuta mwangaza)"},
            {"en": "Carbon Dioxide", "sw": "Gesi ya Kaboni Dioksidi"},
            {"en": "Oxygen", "sw": "Hewa Safi ya Oksijeni"},
            {"en": "Transpiration", "sw": "Mvukizo wa maji kupitia majani"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kushuhudia Oksijeni ya Mmea wa Eneo Lako",
            "title_en": "Experiment: Observing Plant Oxygen in Your Locality",
            "materials_sw": "Jani bichi la eneo lako (jani la Osuga/managu kule Kisumu, mnazi Pwani, au mahindi milimani), chupa ya maji safi, jua.",
            "materials_en": "A fresh local leaf (Osuga/Managu in Kisumu, coconut leaf at Coast, maize in Highlands), clear bottle with water, sunlight.",
            "steps_sw": "1. Weka jani ndani ya chupa ya maji.\n2. Weka chupa juani kwa saa moja.\n3. Tazama au hisi viputo vidogo vya hewa vinavyojitokeza kwenye jani - hiyo ni Oksijeni safi ya mmea wako!",
            "steps_en": "1. Submerge the leaf inside the clear bottle of water.\n2. Place it in direct sunlight for 1 hour.\n3. Watch tiny bubbles form on the leaf surface - that is pure Oxygen released by your local plant!"
        },
        "quiz": {
            "question_sw": "Kwa nini mimea kama mboga za Osuga (Kisumu) au mnazi (Pwani) inahitaji mwangaza wa jua?",
            "question_en": "Why do local plants require direct sunlight?",
            "options_sw": ["A) Kutengeneza chakula (glukosi) kupitia usanisinuru", "B) Ili ibadilishe rangi kuwa nyekundu", "C) Kukausha udongo mzima", "D) Ili kuzuia upepo"],
            "options_en": ["A) To synthesize food energy (glucose) via photosynthesis", "B) To turn red", "C) To dry up all soil", "D) To block wind"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Mwangaza wa jua ndio chanzo cha nishati inayowezesha mmea kupika chakula chake.",
            "explanation_en": "Exactly right! Sunlight provides the fundamental energy needed to power photosynthesis."
        }
    },
    {
        "id": "aquatic_biology_kisumu",
        "title_en": "Aquatic Respiration & Fish Biology (Lake Ecosystem)",
        "title_sw": "Upumuaji wa Samaki na Uhai Ziwani (Mfano wa Ziwa Victoria)",
        "subject": "Biology",
        "cbc_strand": "Animals & Environmental Adaptations (Grade 5/6 Science)",
        "summary_en": "Fish like Tilapia (Ngege) and Nile Perch (Mbuta) breathe underwater using specialized gills that extract dissolved oxygen from water.",
        "summary_sw": "Samaki kama Ngege (Tilapia) na Mbuta (Nile Perch) wanapumua ndani ya maji kwa kutumia matamvua au mashavu (gills) yanayochuja oksijeni iliyoyeyushwa kwenye maji ya ziwa.",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria kichwa cha samaki Ngege. Kando ya kichwa kuna vifuniko vya mashavu vinavyojifungua na kujifunga. Ndani yake kuna matamvua (gills) laini yenye rangi nyekundu ya damu yanayofanya kazi kama chujio la hewa. Maji yakipita, matamvua haya yanafyonza hewa ya oksijeni na kuituma kwenye damu ya samaki!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Samaki anayeogelea] + [Ishara ya Matamvua/Gills yanayopumua] + [Mchoro wa Chujio linalovuta Oksijeni].",

        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Dunga Beach au Luanda Kotieno kando ya Ziwa Victoria, unapoangalia samaki Ngege (Tilapia), vifuniko vya mashavu yake yakifunguka na kufunga, maji hupita kwenye matamvua (gills) yanayofanya kazi kama chujio maalum linalofyonza oksijeni kutoka majini na kuingiza kwenye damu yake!",
                "analogy_en": "At Dunga Beach in Kisumu, when you watch a fresh Tilapia (Ngege), its operculum gills flap to pump lake water across gill filaments that filter dissolved oxygen directly into its bloodstream!"
            },
            "coastal": {
                "analogy_sw": "Kule Pwani, samaki wa baharini kama Changwa au Taa wanatumia matamvua/mashavu (gills) yao kuchuja oksijeni kwenye maji yenye chumvi ya Bahari ya Hindi!",
                "analogy_en": "At the coast, marine fish filter dissolved oxygen through gill lamellae in Indian Ocean saltwater!"
            },
            "highlands": {
                "analogy_sw": "Kwenye mabwawa ya samaki ya milimani au mito ya Nakuru, samaki wa maji baridi (Trout na Tilapia) wanahitaji maji yanayotiririka yenye oksijeni tele!",
                "analogy_en": "In highland coldwater fish farms, Trout and Tilapia thrive in oxygen-rich cascading mountain streams!"
            },
            "arid": {
                "analogy_sw": "Kule Ziwa Turkana au mabwawa ya Garissa, samaki aina ya Mudfish (Kamongo) wana uwezo wa kipekee wa kupumua hewa ya kawaida wakati maji yanapokauka!",
                "analogy_en": "In Lake Turkana and seasonal ASAL pans, Lungfish (Kamongo) have modified swim bladders allowing them to breathe atmospheric air during droughts!"
            },
            "urban": {
                "analogy_sw": "Kwenye mabwawa ya samaki ya mjini (aquariums au urban fish farming), pampu ya hewa (aerator) hupuliza viputo ili kuongeza oksijeni kwenye maji ya samaki!",
                "analogy_en": "In urban fish farms, water aerators inject air bubbles to maintain dissolved oxygen levels for fish health!"
            }
        },
        "key_terms": [
            {"en": "Gills (Operculum)", "sw": "Matamvua / Mashavu ya samaki (Gills)"},
            {"en": "Dissolved Oxygen", "sw": "Oksijeni iliyoyeyuka majini"},
            {"en": "Ecosystem", "sw": "Mfumo wa ikolojia ya viumbe hai"},
            {"en": "Invasive Species", "sw": "Mimea vamizi (kama Magugu Maji / Akech)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Oksijeni Ndani ya Maji ya Kunywa",
            "title_en": "Experiment: Demonstrating Dissolved Air in Water",
            "materials_sw": "Glasi safi ya maji ya baridi.",
            "materials_en": "Clear glass of cold tap/well water.",
            "steps_sw": "1. Jaza glasi na maji ya baridi kisha uiache mezani kwa saa 3 bila kuitikisa.\n2. Utaona viputo vidogo vya hewa vikijitokeza pembeni ya glasi.\n3. Hiyo ndiyo hewa ya oksijeni ambayo samaki Ngege anaitumia kupumua!",
            "steps_en": "1. Fill a clear glass with cold water and leave it undisturbed for 3 hours.\n2. Observe tiny air bubbles forming on the glass sides.\n3. That is dissolved oxygen warming and separating—the exact oxygen fish breathe!"
        },
        "quiz": {
            "question_sw": "Samaki aina ya Ngege (Tilapia) kule Kisumu anatumia kiungo gani kupumua ndani ya maji?",
            "question_en": "What organ does a Tilapia fish use to breathe underwater in Lake Victoria?",
            "options_sw": ["A) Matamvua / Mashavu (Gills)", "B) Mapafu kama ya binadamu", "C) Mkia", "D) Macho"],
            "options_en": ["A) Gills (Matamvua/Mashavu)", "B) Human-like lungs", "C) Tail fin", "D) Eyes"],
            "correct_index": 0,
            "explanation_sw": "Hodari sana! Samaki hutumia matamvua au mashavu (gills) kuchuja oksijeni moja kwa moja kutoka kwenye maji ya ziwa.",
            "explanation_en": "Brilliant! Fish use their gills to extract dissolved oxygen directly from water."
        }
    },
    {
        "id": "human_digestive_system",
        "title_en": "Human Digestive System & Nutrition",
        "title_sw": "Mfumo wa Mmeng'enyo wa Chakula na Lishe Mwilini",
        "subject": "Biology",
        "cbc_strand": "Human Body Systems & Health (Grade 5/6 Science)",
        "summary_en": "Digestion breaks down food (like ugali and greens) into microscopic nutrients that enter the bloodstream to give energy and build the body.",
        "summary_sw": "Mmeng'enyo wa chakula huvunja chakula (kama ugali na mboga) katika chembechembe ndogo za virutubisho zinazofyonzwa na damu ili kuupa mwili nguvu na afya.",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Weka kidole chako mdomoni ambapo meno yanatafuna na mate yanalainisha. Fuata koo kuelekea tumboni (umio) ambapo asidi ya tumbo inavunja protini. Kisha hisi tumbo la chini ambapo utumbo mwembamba mrefu unafyonza virutubisho vyote kuingia kwenye damu!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Kutafuna Mdomoni] ➔ [Ishara ya Kumeza kuelekea Tumboni] ➔ [Ishara ya Utumbo unaofyonza Nguvu]. Angalia mchoro wa njia ya chakula.",
        
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu unapokula ugali wa mtama kwa samaki Ngege na mboga za Osuga (Managu), mate mdomoni yanaanza kuyeyusha wanga wa ugali, tumbo linavunja protini ya samaki, na utumbo mdogo unafyonza madini ya chuma na vitamini ili kukuza misuli yako!",
                "analogy_en": "In Kisumu when you eat millet ugali with Tilapia and Osuga greens, mouth amylase breaks down starches, stomach acids digest fish proteins, and the small intestine absorbs nutrients into your bloodstream!"
            },
            "coastal": {
                "analogy_sw": "Pwani unapokula biriani au wali wa nazi kwa samaki wa kukaanga, mafuta ya nazi yanavunjwa na nyongo (bile) kutoka kwenye ini, kisha virutubisho vinasambazwa mwilini kote!",
                "analogy_en": "At the coast when eating coconut rice and fish, coconut fats are emulsified by liver bile in the duodenum, absorbing energy for your daily activities!"
            },
            "highlands": {
                "analogy_sw": "Mashambani Nakuru au Kericho unapokula githeri (mahindi na maharagwe), mmeng'enyo wa polepole unakupa nguvu ya siku nzima ya kutembea na kufanya kazi!",
                "analogy_en": "In the highlands when eating githeri (maize & beans), complex fiber and proteins digest steadily in the small intestine to provide sustained energy!"
            },
            "arid": {
                "analogy_sw": "Kule Garissa au Turkana unywapo maziwa ya ngamia yenye virutubisho tele, utumbo mdogo unafyonza maji, madini ya kalsiamu na protini kwa haraka ili kuimarisha mifupa na kuzuia kiu!",
                "analogy_en": "In arid regions, drinking nutrient-dense camel milk allows the digestive tract to rapidly absorb calcium, vitamins, and water for bone strength and hydration!"
            },
            "urban": {
                "analogy_sw": "Mtaani unapokula chapati na maharagwe, kinywa, umio, tumbo, na utumbo vinafanya kazi pamoja kama kiwanda cha kuchuja na kusambaza nishati mwilini!",
                "analogy_en": "In the city, digestion works like a biological processing factory, breaking chapati carbohydrates into glucose fuel for brain and muscle cells!"
            }
        },
        "key_terms": [
            {"en": "Digestion", "sw": "Mmeng'enyo wa Chakula"},
            {"en": "Esophagus (Gullet)", "sw": "Umio (Njia ya koo kuelekea tumboni)"},
            {"en": "Enzymes", "sw": "Vimeng'enya (Kemikali asilia za kuvunja chakula)"},
            {"en": "Small Intestine (Villi)", "sw": "Utumbo Mdogo (Sehemu ya kufyonza virutubisho)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Vimeng'enya vya Mate Mdomoni",
            "title_en": "Experiment: Salivary Amylase Starch Test",
            "materials_sw": "Kipande kidogo cha mkate kavu, biskuti au ugali.",
            "materials_en": "Small piece of plain bread, cracker or ugali.",
            "steps_sw": "1. Weka kipande kidogo cha mkate mdomoni.\n2. Tafuna taratibu kwa dakika 2 bila kukimeza.\n3. Utahisi kikianza kuwa kitamu (sukari)—hiyo inathibitisha vimeng'enya vya mate vikivunja wanga kuwa sukari!",
            "steps_en": "1. Place a piece of bread in your mouth.\n2. Chew slowly for 2 minutes without swallowing.\n3. Notice it turns sweet—salivary amylase is breaking complex starch into simple glucose sugars!"
        },
        "quiz": {
            "question_sw": "Sehemu gani ya mfumo wa mmeng'enyo inahusika zaidi na kufyonza virutubisho vya chakula kuingia kwenye damu?",
            "question_en": "Which organ in the digestive system is primarily responsible for absorbing digested nutrients into the bloodstream?",
            "options_sw": ["A) Utumbo Mdogo (Small Intestine)", "B) Kinywa tu", "C) Umio (Esophagus)", "D) Nywele"],
            "options_en": ["A) Small Intestine", "B) Mouth only", "C) Esophagus", "D) Hair"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Utumbo mdogo una vinyweleo vidogo (villi) vinavyofyonza virutubisho vyote na kuviingiza moja kwa moja kwenye mishipa ya damu.",
            "explanation_en": "Spot on! The small intestine lining is covered with villi that absorb nutrients directly into blood capillaries."
        }
    },
    {
        "id": "circulatory_heart",
        "title_en": "Human Heart & Blood Circulatory System",
        "title_sw": "Moyo na Mzunguko wa Damu Mwilini",
        "subject": "Biology",
        "cbc_strand": "Human Body & Vital Organs (Grade 5/6 Science)",
        "summary_en": "The heart acts as a muscular pump that continuously circulates blood, delivering oxygen and food nutrients to every cell while removing waste carbon dioxide.",
        "summary_sw": "Moyo hufanya kazi kama pampu ya misuli inayozungusha damu mwilini bila kukoma, ikisafirisha oksijeni na virutubisho kwa kila seli na kuondoa uchafu.",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Weka kiganja chako katikati ya kifua chako kuelekea upande wa kushoto kidogo. Hisi mpigo thabiti wa 'du-du... du-du'. Huo ni moyo wako wenye vyumba vinne ukisukuma damu safi kuelekea kichwani, mikononi, na miguuni kupitia mishipa ya ateri!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Moyo unaopiga] ➔ [Mchoro wa Damu Nyekundu inayosafiri mwilini] ➔ [Mchoro wa Damu inayorudi kwenye Mapafu].",
        
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kama pampu ya maji ya manispaa ya Kisumu inayosukuma maji safi ya Ziwa Victoria kupitia mtandao wa mabomba kwenye nyumba zote za jiji, moyo wako unasukuma damu safi kupitia ateri kwenye seli zote za mwili!",
                "analogy_en": "Like Kisumu water utility pumping clean Lake Victoria water through pipe networks to every household, your heart pumps oxygen-rich blood through arteries to every body cell!"
            },
            "coastal": {
                "analogy_sw": "Pwani, kama meli bandarini zinazosafirisha mizigo na kurudi na bidhaa mpya, chembechembe nyekundu za damu (Red Blood Cells) zinasafirisha oksijeni na kurudisha hewa ya kaboni kwenye mapafu!",
                "analogy_en": "At Mombasa port, like cargo ships delivering food and picking up exports, red blood cells ferry oxygen to tissues and return carbon dioxide waste to the lungs!"
            },
            "highlands": {
                "analogy_sw": "Milimani, wanariadha maarufu wa Eldoret na Iten wana mioyo imara sana na chembechembe nyingi za damu zinazowezesha kusafirisha oksijeni nyingi wakati wa mbio ndefu!",
                "analogy_en": "In high-altitude training camps in Iten, athletes develop strong cardiac muscles and high red blood cell counts to maximize oxygen delivery during endurance running!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo ya joto kali, mishipa ya damu ya ngozi hupanuka kidogo ili kutoa joto jingi nje ya mwili na kukuweka salama!",
                "analogy_en": "In hot ASAL regions, peripheral blood vessels dilate to radiate excess body heat, maintaining vital organ temperatures!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mtandao wa mishipa ya damu (ateri na vena) ni kama barabara za mji zenye njia mbili—njia moja inapeleka bidhaa safi na nyingine inarudisha taka za viwandani!",
                "analogy_en": "In urban centers, the circulatory system mirrors a dual-carriageway highway network—arteries transport vital supplies while veins return metabolic waste!"
            }
        },
        "key_terms": [
            {"en": "Heart (Atrium & Ventricle)", "sw": "Moyo (Vyumba vya juu na chini vya pampu)"},
            {"en": "Arteries & Veins", "sw": "Mishipa ya Ateri (Damu safi) na Vena (Damu chafu)"},
            {"en": "Red Blood Cells (Hemoglobin)", "sw": "Chembechembe Nyekundu za Damu (Zinabeba Oksijeni)"},
            {"en": "Pulse Rate", "sw": "Kasi ya Mapigo ya Moyo"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kupima Mapigo ya Moyo Kabla na Baada ya Mazoezi",
            "title_en": "Experiment: Measuring Resting vs Active Pulse Rate",
            "materials_sw": "Vidole viwili (cha kati na cha shahada), saa au kuhesabu kwa sekunde 60.",
            "materials_en": "Two fingers, watch or phone timer for 60 seconds.",
            "steps_sw": "1. Weka vidole viwili kwenye kifundo cha mkono chini ya kidole gumba.\n2. Hesabu mapigo ukiwa umepumzika (kawaida 70-85 kwa dakika).\n3. Ruka kamba au kurukaruka mara 20 kisha upime tena—moyo utapiga kwa kasi zaidi kusukuma oksijeni kwenye misuli!",
            "steps_en": "1. Place two fingers on the inside of your wrist below the thumb.\n2. Count resting pulses for 60 seconds.\n3. Jump in place 20 times and re-measure—your pulse quickens as the heart pumps extra oxygen to working muscles!"
        },
        "quiz": {
            "question_sw": "Mishipa ya Ateri inafanya kazi gani kuu mwilini?",
            "question_en": "What is the primary function of Arteries in the circulatory system?",
            "options_sw": ["A) Kusafirisha damu safi yenye oksijeni kutoka kwenye moyo kwenda mwilini", "B) Kutengeneza mate", "C) Kusaga chakula", "D) Kuotesha nywele"],
            "options_en": ["A) Carrying oxygenated blood away from the heart to body tissues", "B) Producing saliva", "C) Grinding food", "D) Growing hair"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Ateri hubeba damu safi iliyojaa oksijeni kutoka kwenye moyo kuelekea kwenye viungo vyote vya mwili.",
            "explanation_en": "Brilliant! Arteries carry oxygen-rich blood under high pressure from the heart to all body tissues."
        }
    },
    {
        "id": "human_respiration",
        "title_en": "Human Respiratory System & Lungs",
        "title_sw": "Mfumo wa Upumuaji wa Binadamu na Mapafu",
        "subject": "Biology",
        "cbc_strand": "Living Things & Life Processes (Grade 5/6 Science)",
        "summary_en": "Breathing draws fresh oxygen into the lungs where it passes into the blood, while carbon dioxide waste is breathed out.",
        "summary_sw": "Upumuaji huleta hewa safi ya oksijeni kwenye mapafu ambapo huingia kwenye damu, na kutoa nje hewa chafu ya kaboni dioksidi.",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Weka mikono yako miwili mbavuni kifuani mwako. Vuta pumzi ndefu ndani kupitia puani—hisi mbavu zako zikipanuka na kifua kikiinuka juu wakati mapafu yanapojaa hewa. Toa pumzi taratibu mdomoni—hisi kifua kikishuka chini!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Kuvuta Pumzi Puani] ➔ [Ishara ya Mapafu Yanayopanuka] ➔ [Mchoro wa Oksijeni inayoingia na Kaboni inayotoka].",
        
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria wakati upepo mwanana wa ziwani unapovuma asubuhi, unavuta hewa safi iliyojaa oksijeni kupitia koromeo (trachea) hadi kwenye mifuko midogo ya hewa (alveoli) ya mapafu yako!",
                "analogy_en": "By Lake Victoria, breathing in cool morning lake breezes channels fresh oxygen down the trachea into millions of microscopic alveoli air sacs in your lungs!"
            },
            "coastal": {
                "analogy_sw": "Pwani kwenye msitu wa mikoko au ufukweni, miti inasafisha hewa ya bahari, na mapafu yako yanatumia misuli ya kiwambo (diaphragm) kuvuta hewa ndani bila wewe kufikiria!",
                "analogy_en": "Along coastal beaches, your diaphragm muscle contracts downward automatically to draw oxygen-rich coastal air into the lung bronchi!"
            },
            "highlands": {
                "analogy_sw": "Kule milimani Mt. Kenya au Aberdares ambapo hewa ni baridi na safi, mapafu hufanya kazi kwa ufanisi mkubwa kuchuja vumbi kupitia vinyweleo vidogo (cilia) vya puani!",
                "analogy_en": "In crisp highland climates, nasal cilia and mucus filter dust before pristine air reaches deep lung tissues!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo yenye vumbi na jua kali, mfumo wa pua hupasha hewa joto na kuinywesha unyevu kabla haijafika kwenye mapafu yako laini!",
                "analogy_en": "In dry arid environments, nasal passages humidify and condition warm dry air to protect delicate alveoli membranes!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mapafu yanafanya kazi kama chujio la hewa la gari, yakilinda mwili dhidi ya chembe za moshi huku yakichukua oksijeni pekee!",
                "analogy_en": "In urban neighborhoods, the respiratory mucosa traps airborne particles while permitting pure oxygen gas exchange!"
            }
        },
        "key_terms": [
            {"en": "Trachea (Windpipe)", "sw": "Koromeo (Njia kuu ya hewa)"},
            {"en": "Lungs & Bronchi", "sw": "Mapafu na Matawi ya Koromeo"},
            {"en": "Alveoli (Air Sacs)", "sw": "Mfuko midogo ya kubadilishia hewa (Alveoli)"},
            {"en": "Diaphragm", "sw": "Kiwambo cha mbavu (Misuli inayosaidia kupumua)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Mvuke na Hewa Inayotoka Mapafuni",
            "title_en": "Experiment: Exhaled Moisture and Carbon Dioxide Test",
            "materials_sw": "Kioo kidogo au miwani safi, pumzi yako.",
            "materials_en": "Small pocket mirror or clean glass, your breath.",
            "steps_sw": "1. Shikilia kioo mbele ya mdomo wako.\n2. Pumua kwa nguvu 'haaaaa' kwenye kioo.\n3. Utaona ukungu wa matone madogo ya maji—hii inathibitisha mapafu yanatoa joto na unyevu wa maji pamoja na kaboni dioksidi!",
            "steps_en": "1. Hold a small mirror near your mouth.\n2. Exhale warmly onto the surface.\n3. Observe the fog of water condensation—proving lungs expel warm moisture alongside carbon dioxide waste!"
        },
        "quiz": {
            "question_sw": "Ni gesi gani muhimu ambayo mapafu yanaivuta kutoka hewani ili kuingia kwenye damu ya binadamu?",
            "question_en": "Which essential gas do human lungs absorb from the air into the bloodstream?",
            "options_sw": ["A) Oksijeni (Oxygen)", "B) Dioksidi ya Kaboni", "C) Moshi", "D) Chuma"],
            "options_en": ["A) Oxygen (O2)", "B) Carbon Dioxide", "C) Smoke", "D) Iron"],
            "correct_index": 0,
            "explanation_sw": "Hodari sana! Oksijeni ndiyo gesi inayohitajika na seli zote za mwili kutengeneza nishati ya uhai.",
            "explanation_en": "Correct! Oxygen is the vital gas required by all cells for cellular respiration and energy production."
        }
    },
    {
        "id": "cell_biology",
        "title_en": "Cell Biology: The Basic Units of Life",
        "title_sw": "Muundo wa Seli: Matofali ya Msingi ya Viumbe Hai",
        "subject": "Biology",
        "cbc_strand": "Cell Structure & Basic Units of Life (Junior Secondary Science)",
        "summary_en": "Cells are the microscopic building blocks of all living things. Plant cells have rigid cell walls and chloroplasts, while animal cells have flexible membranes.",
        "summary_sw": "Seli ni vitengo vidogo sana vya msingi vinavyounda viumbe hai vyote. Seli za mimea zina kuta imara na kloroplasti, wakati seli za wanyama zina utando laini.",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria nyumba imejengwa kwa matofali madogo elfu nyingi. Mwili wako na mmea vimejengwa kwa 'matofali ya uhai' yanayoitwa Seli. Ndani ya kila seli kuna Kiini (Nucleus) chenye umbo la duara kinachoongoza shughuli zote, kikiwa kimezungukwa na kioevu cha jeli kinachoitwa Saikroplasimu!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Mchoro wa Seli ya Mmea (Ukuta Kijani)] + [Mchoro wa Seli ya Mnyama (Duara Laini na Kiini Katikati)].",
        
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kama ukuta wa matofali ya mawe ya ujenzi huko Kisumu unavyounda jengo zima, mamilioni ya seli za mimea ya magugu maji au mboga za Osuga zimeungana kuunda majani, mizizi na mashina!",
                "analogy_en": "Just as brick masonry forms a sturdy house in Kisumu, billions of microscopic cells unite to construct the roots, stems, and leaves of indigenous plants!"
            },
            "coastal": {
                "analogy_sw": "Pwani, seli ya mnazi ina kloroplasti zinazofanya usanisinuru kama paneli ndogo za jua, huku seli za samaki wa baharini zikiwa na utando unaobadilika ili kuruhusu mwendo!",
                "analogy_en": "At the coast, palm leaf cells contain chloroplast solar powerhouses, while flexible marine animal cells allow fluid swimming locomotion!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, seli za viazi na mahindi zina chembechembe maalum za kuhifadhi wanga (starch granules) ili mmea uwe na chakula cha kutosha kukua!",
                "analogy_en": "In highland agricultural zones, potato cells contain specialized amyloplasts packed with starch reserves to fuel rapid sprout growth!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame, seli za mimea ya mikakasi (succulents) na acacia zina vacuoles kubwa za kuhifadhi maji kwa miezi mingi bila kukauka!",
                "analogy_en": "In arid ASAL zones, succulent plant cells feature massive central vacuoles designed to store water reserves through prolonged droughts!"
            },
            "urban": {
                "analogy_sw": "Mtaani, kiini cha seli (nucleus) kinafanya kazi kama afisa mkuu wa jiji au kompyuta kuu inayoongoza shughuli zote za uzalishaji!",
                "analogy_en": "In modern cities, the cell nucleus functions like a central municipal control hub, housing genetic DNA blueprints for all cellular operations!"
            }
        },
        "key_terms": [
            {"en": "Nucleus", "sw": "Kiini cha Seli (Kituo cha udhibiti na maagizo ya DNA)"},
            {"en": "Cell Membrane", "sw": "Utando wa Seli (Geti la kuruhusu vitu kuingia na kutoka)"},
            {"en": "Cytoplasm", "sw": "Saikroplasimu (Kioevu cha jeli kinachobeba viungo vya seli)"},
            {"en": "Cell Wall & Chloroplast", "sw": "Ukuta wa Seli & Kloroplasti (Vipengele vya mimea pekee)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuchunguza Tabaka Nyembamba la Seli za Kitunguu",
            "title_en": "Experiment: Observing Onion Skin Cell Architecture",
            "materials_sw": "Kitunguu maji kimoja, glasi yenye tone la maji, kioo cha kukuza picha au kamera ya simu.",
            "materials_en": "One fresh onion, drop of water, magnifying glass or smartphone macro camera.",
            "steps_sw": "1. Menya kitunguu na uvute utando mwembamba sana ulio wazi kama nailoni.\n2. Weka juu ya tone la maji kwenye uso safi.\n3. Angalia kwa karibu chini ya mwanga—utaona mistari inayofanana na matofali ya seli zilizopangwa vizuri!",
            "steps_en": "1. Peel a fresh onion and gently separate the thin translucent membrane between layers.\n2. Float it on a clean water droplet.\n3. Examine under light with a magnifier to observe the organized brick-like grid of plant cells!"
        },
        "quiz": {
            "question_sw": "Ni kiungo gani kinachopatikana kwenye seli za mimea pekee lakini hakipatikani kwenye seli za wanyama?",
            "question_en": "Which structure is found exclusively in plant cells but absent in animal cells?",
            "options_sw": ["A) Ukuta wa Seli (Cell Wall) & Kloroplasti", "B) Kiini (Nucleus)", "C) Maji", "D) Damu"],
            "options_en": ["A) Cell Wall & Chloroplasts", "B) Nucleus", "C) Water", "D) Blood"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Mimea ina ukuta mgumu wa selulosi (Cell Wall) na Kloroplasti za kutengeneza chakula kwa jua.",
            "explanation_en": "Spot on! Plant cells possess rigid cellulose cell walls and photosynthetic chloroplasts."
        }
    },
    {
        "id": "plant_pollination",
        "title_en": "Plant Reproduction & Flower Pollination",
        "title_sw": "Uchavushaji wa Maua na Uzazi wa Mimea",
        "subject": "Biology",
        "cbc_strand": "Plants & Reproduction (Grade 5/6 Science)",
        "summary_en": "Pollination transfers yellow pollen grains from male stamens to female pistils, allowing flowers to form seeds and delicious fruits.",
        "summary_sw": "Uchavushaji husafirisha chembe za chavua (poleni) kutoka kwenye chavulio (stamen) hadi kwenye kambamaua (pistil) ili kukuza mbegu na matunda matamu.",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika ua lililochanua mkononi mwako. Hisi petali laini zenye harufu nzuri za kuvutia nyuki. Katikati ya ua utahisi vijiti vidogo vyenye vumbi laini la unga (chavua/pollen). Ndani kabisa kuna sehemu yenye unyevu ambapo mbegu na matunda huanza kutungika!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Nyuki anayeruka] ➔ [Ishara ya Kugusa Ua na Kuchukua Poleni] ➔ [Mchoro wa Mbegu na Tunda linaloota].",
        
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu kwenye mashamba ya alizeti au maembe, nyuki wanapotua kwenye maua kunyonya majimaji matamu (nectar), miguu yao inashika unga wa chavua na kuusafirisha kwenye ua jingine ili maembe manono yatokee!",
                "analogy_en": "In Kisumu sunflower and mango groves, foraging honeybees sipping nectar pick up pollen on their fuzzy legs, cross-pollinating blossoms into juicy fruits!"
            },
            "coastal": {
                "analogy_sw": "Pwani, vipepeo wenye rangi za kuvutia na upepo wa bahari husaidia kuchavusha maua ya mikorosho na mipapai ili wakulima wavune korosho nyingi!",
                "analogy_en": "Along coastal plantations, colorful butterflies and gentle sea breezes pollinate cashew and papaya blooms for abundant harvests!"
            },
            "highlands": {
                "analogy_sw": "Kule Kitale na Nakuru, upepo wa asubuhi unatikisa mashamba ya mahindi na kurusha mamilioni ya chembe za poleni kutoka kwenye mashada ya juu (tassels) hadi kwenye nyuzi laini za mahindi (silks)!",
                "analogy_en": "In highland maize fields, morning winds shake pollen from top tassels down onto emerging ear silks, fertilizing every single sweet corn kernel!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame, miti ya mshikio (acacia) hutoa maua yenye harufu kali baada ya mvua fupi ili kuvuta wadudu wengi kwa haraka kabla ya jua kali!",
                "analogy_en": "In arid savanna zones, acacia blossoms erupt into fragrant yellow puffballs immediately after rainfall to attract pollinators quickly!"
            },
            "urban": {
                "analogy_sw": "Kwenye bustani za jiji na mitaa, nyuki wa asali wanatunza mimea ya bustani na maua ya mijini kupitia uchavushaji wa asili!",
                "analogy_en": "In urban schoolyards and community gardens, native bees provide essential pollination services to vegetables and fruit trees!"
            }
        },
        "key_terms": [
            {"en": "Pollination", "sw": "Uchavushaji (Usafirishaji wa chavua)"},
            {"en": "Pollen Grains", "sw": "Chavua / Poleni (Unga wa mbegu za kiume za ua)"},
            {"en": "Stamen (Male Part)", "sw": "Chavulio (Sehemu ya kiume ya ua inayotoa poleni)"},
            {"en": "Pistil / Carpel (Female Part)", "sw": "Kambamaua (Sehemu ya kike inayotunga mbegu na matunda)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kugundua Unga wa Chavua kwenye Ua",
            "title_en": "Experiment: Flower Anatomy and Pollen Fingerprint",
            "materials_sw": "Ua bichi la shambani (kama ua la mpera, bamia au mahindi), kidole safi.",
            "materials_en": "Fresh open flower (hibiscus, bean, or tomato bloom), clean index finger.",
            "steps_sw": "1. Gusa kwa upole sehemu ya katikati ya ua (chavulio).\n2. Angalia ncha ya kidole chako—utaona unga wa njano wenye kunata.\n3. Huu ndio unga wa chavua ambao nyuki anausafirisha miguuni mwake!",
            "steps_en": "1. Lightly tap the central stamens of an open flower.\n2. Inspect your fingertip—observe fine yellow sticky dust.\n3. That is pollen, identical to what clings to honeybee legs during pollination!"
        },
        "quiz": {
            "question_sw": "Wadudu kama nyuki wanasaidiaje mimea wakati wanapotembelea maua?",
            "question_en": "How do insects like bees assist flowering plants during their visits?",
            "options_sw": ["A) Kusafirisha chavua (pollination) ili mimea itengeneze mbegu na matunda", "B) Kula mizizi yote", "C) Kukausha majani", "D) Kupaka rangi kwenye udongo"],
            "options_en": ["A) Transferring pollen to facilitate fertilization and fruit production", "B) Eating all roots", "C) Drying leaves", "D) Coloring the soil"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Nyuki ni wachavushaji wakuu wanaosaidia mimea kutunga mbegu na matunda matamu.",
            "explanation_en": "Spot on! Bees are vital natural pollinators that enable fertilization, seed formation, and food security."
        }
    },
    {
        "id": "living_things_classification",
        "title_en": "Classification of Living Things: Vertebrates & Invertebrates",
        "title_sw": "Uainishaji wa Viumbe Hai: Wanyama Wenye Uti wa Mgongo na Wasio nao",
        "subject": "Biology",
        "cbc_strand": "Classification of Living Things (Grade 5/6 Science)",
        "summary_en": "Animals are classified into Vertebrates (with a backbone: mammals, birds, reptiles, amphibians, fish) and Invertebrates (without a backbone: insects, spiders, snails).",
        "summary_sw": "Wanyama huainishwa katika Wenye Uti wa Mgongo (Vertebrates: mamalia, ndege, reptilia, amfibea, samaki) na Wasio na Uti wa Mgongo (Invertebrates: wadudu, buibui, konokono).",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Pitisha vidole vyako katikati ya mgongo wako kuanzia shingoni hadi kiunoni. Utahisi mfupa mgumu uliopinda wenye vifundo vidogo—huo ndio Uti wa Mgongo (Backbone). Wanyama kama binadamu, mbwa, na samaki wana uti wa mgongo (Vertebrates), lakini wadudu kama panzi na konokono hawana mifupa ndani (Invertebrates)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Kushika Uti wa Mgongo] ➔ [Makundi 5 ya Vertebrates: Mamalia, Ndege, Samaki, Reptilia, Amfibea] vs [Invertebrates: Wadudu].",
        
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria, samaki Ngege ana mifupa na uti wa mgongo mgumu (Vertebrate), lakini konokono wa majini na wadudu wa ziwani hawana mfupa wowote ndani (Invertebrates)!",
                "analogy_en": "In Lake Victoria, Tilapia fish possess an internal bony vertebral column (Vertebrate), whereas freshwater snails and lake flies lack backbones (Invertebrates)!"
            },
            "coastal": {
                "analogy_sw": "Pwani, kasa wa baharini na pomboo ni wenye uti wa mgongo (Vertebrates), wakati kaa na ngisi wana maganda ya nje au miili laini bila mifupa ya ndani (Invertebrates)!",
                "analogy_en": "Along coastal reefs, sea turtles and dolphins are vertebrates, while crabs and octopuses are invertebrates with exoskeletons or soft bodies!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, ng'ombe na kuku wana mifupa ya ndani yenye uti wa mgongo, wakati minyoo ya ardhini na panzi ni wanyama wasio na mifupa ya ndani!",
                "analogy_en": "On highland farms, cattle and chickens are backboned vertebrates, while soil earthworms and grasshoppers are invertebrates!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame, ngamia na mbuni ni wanyama wenye uti wa mgongo imara, wakati nge na mchwa ni wanyama wasio na uti wa mgongo!",
                "analogy_en": "In desert expanses, camels and ostriches are vertebrates, whereas desert scorpions and termites are invertebrates!"
            },
            "urban": {
                "analogy_sw": "Mtaani, ndege wa njiwa na paka ni vertebrates, wakati mbu na vipepeo ni invertebrates wenye miguu yenye viungo sita!",
                "analogy_en": "In urban centers, pigeons and domestic cats are vertebrates, while mosquitoes and houseflies are six-legged invertebrates!"
            }
        },
        "key_terms": [
            {"en": "Vertebrates", "sw": "Wanyama Wenye Uti wa Mgongo (Mammals, Birds, Reptiles, Amphibians, Fish)"},
            {"en": "Invertebrates", "sw": "Wanyama Wasio na Uti wa Mgongo (Insects, Arachnids, Molluscs)"},
            {"en": "Warm-blooded (Endothermic)", "sw": "Viumbe wenye damu vuguvugu (Hujitengenezea joto)"},
            {"en": "Cold-blooded (Ectothermic)", "sw": "Viumbe wenye damu baridi (Hutegemea joto la mazingira)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuainisha Wanyama wa Mazingira Yako",
            "title_en": "Experiment: Backyard Creature Classification Chart",
            "materials_sw": "Daftari, kalamu, uchunguzi wa mazingira ya shule au nyumbani.",
            "materials_en": "Notebook, pen, outdoor environmental observation.",
            "steps_sw": "1. Orodhesha wanyama 5 unaowaona (kama kuku, mbwa, panzi, kipepeo, samaki).\n2. Wagawe katika safu mbili: Wenye Uti wa Mgongo vs Wasio na Uti wa Mgongo.\n3. Utaona jinsi sayansi ya uainishaji inavyorahisisha kuelewa viumbe!",
            "steps_en": "1. List 5 creatures observed around your home or school (e.g. chicken, dog, grasshopper, butterfly, fish).\n2. Categorize them into two columns: Vertebrate vs Invertebrate.\n3. Observe how biological taxonomy reveals shared evolutionary traits!"
        },
        "quiz": {
            "question_sw": "Ni kundi gani kati ya yafuatayo linalojumuisha wanyama wenye uti wa mgongo (Vertebrates) pekee?",
            "question_en": "Which group contains ONLY Vertebrate animals?",
            "options_sw": ["A) Samaki, Ndege, Mamalia, Reptilia, na Amfibea", "B) Panzi, Konokono, na Minyoo", "C) Mbu, Buibui, na Nyuki", "D) Mchwa pekee"],
            "options_en": ["A) Fish, Birds, Mammals, Reptiles, and Amphibians", "B) Grasshoppers, Snails, and Earthworms", "C) Mosquitoes, Spiders, and Bees", "D) Termites only"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Samaki, ndege, mamalia (kama binadamu na ng'ombe), reptilia (kama mijusi) na amfibea (kama vyura) wote wana uti wa mgongo.",
            "explanation_en": "Excellent! Fish, birds, mammals, reptiles, and amphibians constitute the 5 major vertebrate classes."
        }
    },
    {
        "id": "ecology_food_chains",
        "title_en": "Ecology & Food Chains: Energy Flow in Nature",
        "title_sw": "Mnyororo wa Chakula na Mfumo wa Ikolojia",
        "subject": "Biology",
        "cbc_strand": "Environment & Ecosystems (Grade 5/6 Science)",
        "summary_en": "A food chain shows how energy flows from the sun to green plant producers, then to herbivore and carnivore consumers, and finally to decomposers.",
        "summary_sw": "Mnyororo wa chakula huonyesha jinsi nishati inavyosafiri kuanzia jua hadi kwa mimea (watengenezaji), kisha kwa wanyama walaji, na hatimaye kwa waozeshaji.",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria mnyororo uliounganishwa kwa pete: Pete ya kwanza ni Jua linalomulika jani la nyasi (Mzalishaji). Pete ya pili ni Panzi au Mbuzi anayekula nyasi (Mlaji wa kwanza). Pete ya tatu ni Kuku au Simba anayekula mlaji wa kwanza. Kila kiumbe kinategemea kingine kuishi!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Jua] ➔ [Mmea / Mtengenezaji] ➔ [Panzi / Mlaji wa Kwanza] ➔ [Kuku / Mlaji wa Pili] ➔ [Waozeshaji / Decomposers].",
        
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria: Mwangaza wa Jua ➔ Mwani na Magugu Maji (Watengenezaji) ➔ Samaki Dagaa/Omena (Walaji wa kwanza) ➔ Samaki Mbuta/Nile Perch (Mlaji mkuu) ➔ Binadamu!",
                "analogy_en": "In Lake Victoria: Sunlight ➔ Microscopic Algae Producers ➔ Dagaa/Omena filter feeders ➔ Nile Perch apex predator ➔ Humans!"
            },
            "coastal": {
                "analogy_sw": "Pwani: Mwani wa Bahari ➔ Samaki wadogo na uduvi ➔ Samaki mkubwa wa Nguru au Papa ➔ Ndege wa baharini!",
                "analogy_en": "Along coastal coral reefs: Seaweed producers ➔ Small herbivorous reef fish ➔ Barracuda/Shark predators!"
            },
            "highlands": {
                "analogy_sw": "Mashambani: Mmea wa Mahindi ➔ Panzi ➔ Kuku wa kienyeji ➔ Mwewe (Ndege mwindaji)!",
                "analogy_en": "In highland agricultural zones: Green Maize Plants ➔ Grasshopper ➔ Free-range Chicken ➔ Hawk raptor!"
            },
            "arid": {
                "analogy_sw": "Kwenye mbuga za savanna: Nyasi za kijani ➔ Pundamilia na Swala ➔ Simba na Chui (Wawindaji wakuu) ➔ Tumbusi na Bakteria (Waozeshaji)!",
                "analogy_en": "In African savannah grasslands: Savannah Grasses ➔ Zebras and Antelopes ➔ Lions and Cheetahs ➔ Vultures and decomposers!"
            },
            "urban": {
                "analogy_sw": "Mtaani: Mti wa bustani ➔ Mabuu ya wadudu ➔ Ndege wa njiwa na kware ➔ Paka wa mtaani!",
                "analogy_en": "In urban parks: Garden Flowers & Shrubs ➔ Caterpillars ➔ Songbirds ➔ Urban Felines!"
            }
        },
        "key_terms": [
            {"en": "Producer (Autotroph)", "sw": "Mtengenezaji (Mimea ya kijani inayotengeneza chakula kwa jua)"},
            {"en": "Consumer (Herbivore/Carnivore)", "sw": "Mlaji (Mnyama anayekula mimea au wanyama wengine)"},
            {"en": "Apex Predator", "sw": "Mwindaji Mkuu (Aliye kileleni mwa mnyororo wa chakula)"},
            {"en": "Decomposer", "sw": "Mwozeshaji (Bakteria na uyoga wanaorejesha virutubisho ardhini)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuchora Mnyororo wa Chakula wa Shuleni",
            "title_en": "Experiment: Mapping a Local Food Chain",
            "materials_sw": "Karatasi, penseli zenye rangi.",
            "materials_en": "Paper, colored markers or pencils.",
            "steps_sw": "1. Chora Jua na Mmea wa eneo lako upande wa kushoto.\n2. Weka mshale ➔ kuelekea mnyama anayekula mmea huo (mf. mbuzi au panzi).\n3. Weka mshale mwingine ➔ kuelekea kiumbe anayekula mnyama huyo.\n4. Hongera! Umetengeneza ramani ya mzunguko wa nishati!",
            "steps_en": "1. Draw the Sun and a local green plant on the left.\n2. Add an arrow ➔ pointing to a primary herbivore (e.g. goat or insect).\n3. Add another arrow ➔ to a predator.\n4. You have mapped the vital ecological flow of solar energy through living systems!"
        },
        "quiz": {
            "question_sw": "Katika mnyororo wa chakula, ni viumbe gani wanaoitwa 'Watengenezaji' (Producers) kwa sababu wanatengeneza chakula chao kwa kutumia jua?",
            "question_en": "In a food chain, which organisms are called 'Producers' because they synthesize their own food using sunlight?",
            "options_sw": ["A) Mimea ya kijani (Green Plants)", "B) Simba", "C) Samaki Mbuta", "D) Mawe"],
            "options_en": ["A) Green Plants", "B) Lions", "C) Nile Perch", "D) Stones"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Mimea ya kijani ndiyo watengenezaji pekee wanaobadilisha nishati ya jua kuwa chakula kinacholisha viumbe vingine vyote.",
            "explanation_en": "Spot on! Green plants are autotrophic producers that convert radiant solar energy into edible chemical energy."
        }
    },
    {
        "id": "electricity_circuits",
        "title_en": "Electric Current & Circuits",
        "title_sw": "Mkondo wa Umeme na Saketi",
        "subject": "Physics",
        "cbc_strand": "Energy & Force (Grade 6 Science & Technology)",
        "summary_en": "Electric current is the continuous flow of charges through a closed circuit wire.",
        "summary_sw": "Mkondo wa umeme ni mwendo wa chembe ndogo za chaji zinazosafiri kwenye waya uliounganishwa bila kukatika.",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria bomba la duara lililojaa maji. Ukifungua pampu, maji yanasukumwa kuanzia mwanzo hadi mwisho wa bomba. Betri ndio pampu inayozungusha chembe za umeme kwenye waya wa chuma. Waya ukikatika mahali popote, mzunguko unakoma!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Waya wa Duara] + [Ishara ya Mwanga unaowaka] + [Mchoro wa Njia Iliyofungwa bila pengo].",

        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu na Ziwa Victoria, fikiria taa za betri za kuvulia dagaa usiku ziwani! Betri ya 12V inasukuma mkondo wa umeme kupitia nyaya zilizofungwa vizuri ili taa iwake gizani ziwani kuvuta samaki. Saketi ikikatika taa inazima mara moja!",
                "analogy_en": "In Kisumu on Lake Victoria, think of battery-powered lanterns used by night fishermen. The 12V battery pushes current through insulated wiring to illuminate the dark waters. If the circuit breaks, the light instantly goes out!"
            },
            "coastal": {
                "analogy_sw": "Kule Pwani, kama pampu ya maji inayosukuma maji ya bahari kwenye mashamba ya chumvi kule Gongoni/Malindi, voltage ni shinikizo la pampu na current ni kiasi cha maji yanayotiririka!",
                "analogy_en": "Like water pumps pushing brine into coastal salt evaporating beds in Malindi, voltage is the pump pressure and current is the volume of flow through the pipes!"
            },
            "highlands": {
                "analogy_sw": "Kule Nakuru au Mt. Kenya, fikiria mitambo ya umeme wa maji (hydroelectric dams). Maji yanayoanguka kutoka juu milimani yana shinikizo kubwa (Voltage) linalosukuma jenereta kuzunguka!",
                "analogy_en": "In the highlands, think of hydroelectric power stations where high-altitude mountain reservoir pressure (Voltage) drives generator current through power lines!"
            },
            "arid": {
                "analogy_sw": "Kule Turkana na Garissa, paneli ya jua (Solar PV) inavuna mwangaza wa jua na kuutuma kwenye betri. Shinikizo la volteji linasukuma umeme kwenye pampu ya kisima cha maji (borehole solar pump)!",
                "analogy_en": "In arid lands like Garissa and Turkana, solar PV panels convert sunlight into voltage that drives deep borehole water pumps for communities and livestock!"
            },
            "urban": {
                "analogy_sw": "Kwenye mji kama Nairobi, fikiria jinsi taa za barabarani za solar au betri ya matatu inavyosambaza umeme kwenye taa na muziki kupitia mtandao wa nyaya!",
                "analogy_en": "In Nairobi, think of solar smart streetlights and matatu vehicle circuits channeling current to lighting systems and audio amplifiers through closed loop wiring!"
            }
        },
        "key_terms": [
            {"en": "Voltage (Volts)", "sw": "Volteji (Shinikizo la kusukuma umeme)"},
            {"en": "Current (Amperes)", "sw": "Mkondo wa umeme unaopita"},
            {"en": "Resistance (Ohms)", "sw": "Ukinzani unaozuia mtiririko"},
            {"en": "Circuit", "sw": "Saketi (Njia kamili ya umeme)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuwasha Taa Ndogo ya LED",
            "title_en": "Experiment: Simple LED Circuit",
            "materials_sw": "Betri ndogo ya tochi (1.5V), waya mwembamba, taa ndogo ya LED.",
            "materials_en": "Small torch battery (1.5V), thin wire, small LED bulb.",
            "steps_sw": "1. Unganisha ncha chanya (+) ya betri kwenye waya mrefu wa LED.\n2. Unganisha ncha hasi (-) kwenye waya mfupi.\n3. Taa itawaka ikionyesha saketi imekamilika!",
            "steps_en": "1. Connect battery (+) to the longer LED leg.\n2. Connect battery (-) to the shorter leg.\n3. The bulb illuminates when the circuit is unbroken!"
        },
        "quiz": {
            "question_sw": "Nini kitatokea ikiwa waya wa saketi ya umeme utakatika?",
            "question_en": "What happens if a wire in an electrical circuit is severed?",
            "options_sw": ["A) Taa itazimika", "B) Betri itaongeza maji", "C) Taa itawaka zaidi", "D) Hakuna kitakachobadilika"],
            "options_en": ["A) The bulb turns off", "B) The battery gains water", "C) The bulb glows brighter", "D) Nothing changes"],
            "correct_index": 0,
            "explanation_sw": "Sahihi! Umeme unahitaji njia iliyofungwa kabisa bila kukatika ili uweze kutiririka.",
            "explanation_en": "Correct! Electricity requires a continuous closed loop to maintain flow."
        }
    },
    {
        "id": "gravity_forces",
        "title_en": "Gravity & Friction: The Earth's Forces",
        "title_sw": "Mvuto wa Ardhi (Grabiti) na Msuguano",
        "subject": "Physics",
        "cbc_strand": "Forces & Motion (Grade 5/6 Science)",
        "summary_en": "Gravity pulls mass toward the center of the Earth. Friction opposes motion between contacting surfaces.",
        "summary_sw": "Mvuto wa ardhi (Grabiti) huvuta vitu chini ardhini. Msuguano huzuia au kupunguza mwendo vitu vinapogusana.",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shikilia kitu kidogo mkononi (kama jiwe au kifuniko cha chupa) kisha ufungue mkono wako. Unahisi kikidondoka moja kwa moja ardhini—hiyo ni nguvu ya grabiti ya dunia inayokivuta. Kisha paka viganja vyako viwili pamoja kwa haraka—utahisi joto likiongezeka mkononi, hilo joto linatokana na nguvu ya msuguano!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Mchoro wa Jiwe linaloanguka chini ⬇️ (Grabiti)] + [Mchoro wa Viganja viwili vinavyosuguana ↔️ (Msuguano)].",

        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu bandarini, mvuvi anaporusha nanga nzito ya chuma ya mashua, nguvu ya grabiti inalivuta chuma kuzama chini ya maji ya Ziwa Victoria!",
                "analogy_en": "At Kisumu pier, when a fisherman drops a heavy iron anchor, Earth's gravity pulls it rapidly through Lake Victoria's waters to moor the boat!"
            },
            "coastal": {
                "analogy_sw": "Kwenye fukwe za pwani, mnazi ukiangusha dafu, grabiti inalivuta chini kwenye mchanga. Kukokota mashua kwenye mchanga mkavu kuna msuguano mkubwa kuliko kwenye maji laini!",
                "analogy_en": "On coastal beaches, falling coconuts drop straight down due to gravity. Dragging a wooden dhow boat over dry sand encounters high friction, while floating on water has minimal friction!"
            },
            "highlands": {
                "analogy_sw": "Unapoendesha baiskeli ikiteremka mlima mwinuko, grabiti inakuvuta kwa kasi kuelekea chini. Unapobonyeza breki kwenye barabara ya vumbi nyekundu, msuguano ndio unaosimamishe baiskeli!",
                "analogy_en": "Coasting a bicycle down a steep highland ridge, gravity accelerates you downhill. Clamping your rubber brake pads against the wheels creates friction against the red earth road to stop you!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo yenye mchanga na upepo kama Chalbi, upepo mkali unasukuma mchanga, lakini chembe nzito za miamba hazipeperuki kwa sababu ya nguvu ya grabiti!",
                "analogy_en": "In windswept arid expanses, light dust is swept up by gusts while heavy gravel and boulders stay firmly grounded due to gravitational pull!"
            },
            "urban": {
                "analogy_sw": "Kwenye jiji lenye barabara za lami, matairi ya magari yana michirizi maalum ya kuongeza msuguano ili gari lisiteleze wakati wa mvua!",
                "analogy_en": "On city tarmac highways, vehicle tires feature deep tread grooves engineered to maximize frictional grip and prevent hydroplaning during heavy rains!"
            }
        },
        "key_terms": [
            {"en": "Gravity", "sw": "Nguvu ya Mvuto wa Ardhi"},
            {"en": "Friction", "sw": "Nguvu ya Msuguano"},
            {"en": "Acceleration", "sw": "Mchapuko wa Kasi"},
            {"en": "Mass", "sw": "Masi / Uzito wa kitu"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuteleza na Msuguano",
            "title_en": "Experiment: Surface Friction Test",
            "materials_sw": "Sarafu au kifuniko, kitabu chenye jalada laini, kitambaa kigumu au mchanga.",
            "materials_en": "Coin or bottle cap, smooth hardcover notebook, rough cloth or sand.",
            "steps_sw": "1. Inamisha kitabu laini uone sarafu ikiteleza haraka.\n2. Weka mchanga au kitambaa juu ya kitabu telezesha tena.\n3. Sehemu mbaya ina msuguano mkubwa!",
            "steps_en": "1. Tilt smooth book to see coin slide quickly.\n2. Add cloth/sand and slide again.\n3. Rough surfaces increase friction and slow it down!"
        },
        "quiz": {
            "question_sw": "Kwa nini embe au nanga ya mashua ya ziwani huanguka kuelekea chini?",
            "question_en": "Why does a boat anchor or ripe fruit accelerate downward?",
            "options_sw": ["A) Kwa sababu ya nguvu ya mvuto wa ardhi (Grabiti)", "B) Kwa sababu ya upepo", "C) Kwa sababu ya jua", "D) Kwa sababu ya rangi yake"],
            "options_en": ["A) Earth's gravitational pull", "B) Wind gusts", "C) Sunlight", "D) Color"],
            "correct_index": 0,
            "explanation_sw": "Sahihi! Grabiti inavuta vitu vyote vyenye uzito kuelekea katikati ya dunia.",
            "explanation_en": "Spot on! Gravity accelerates all massive bodies toward Earth's center."
        }
    },
    {
        "id": "fractions_math",
        "title_en": "Fractions: Fair Sharing in Real Life",
        "title_sw": "Sehemu za Nambari: Mgawanyo Sawa Kwenye Maisha",
        "subject": "Mathematics",
        "cbc_strand": "Numbers & Operations (Grade 5/6 Mathematics)",
        "summary_en": "A fraction represents equal parts of a whole quantity (Numerator / Denominator).",
        "summary_sw": "Sehemu (Fraction) huonyesha vipande vilivyogawanywa sawasawa kutoka kwa kitu kizima kimoja.",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Chukua kijiti kimoja au karatasi. Ikate katikati uwe na vipande viwili sawa. Kila kipande mkononi mwako ni Nusu (1/2). Ukikata kila kimoja tena uwe na vipande vinne, kila kipande ni Robo (1/4). Vipande 2 vya robo ukiweka pamoja ni sawa na nusu!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Mchoro wa Duara lililogawanywa nusu (1/2)] + [Mchoro wa Duara lenye vipande 4 (1/4)].",

        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu bandarini ukinunua kapu lenye samaki 10 wa Ngege (Tilapia) na ukapika samaki 5 kwa chakula cha jioni, umepika 5/10 ya samaki wote, ambayo ikirahisishwa ni nusu kamili (1/2) ya samaki!",
                "analogy_en": "At Kisumu fish landing pier, buying a basket of 10 Tilapia and cooking 5 of them means you used 5/10, which simplifies to exactly 1/2 of your total fish!"
            },
            "coastal": {
                "analogy_sw": "Kule pwani ukipasua dafu na nazi ikagawanywa kwa watoto wawili sawa, kila mmoja anapata nusu (1/2). Ukigawa samaki mmoja kwa sahani 4 sawa za biriani, kila sahani ina robo (1/4)!",
                "analogy_en": "On the coast, splitting a fresh coconut between two siblings gives each exactly one half (1/2). Dividing a large fish across 4 equal plates gives each 1/4 of the catch!"
            },
            "highlands": {
                "analogy_sw": "Shambani ukivuna gunia la viazi na kugawa katika vikapu vitatu vilivyo sawa, kila kikapu kimepata theluthi (1/3) ya mavuno yote!",
                "analogy_en": "On a highland farm, dividing a potato harvest into 3 equal crates means each crate contains exactly one-third (1/3) of the total harvest!"
            },
            "arid": {
                "analogy_sw": "Kwenye kisima cha maji, ikiwa una dumu la lita 20 na ukachota lita 5 tu, umepata 5/20 ya dumu zima, ambayo ni sawa na robo (1/4) ya maji!",
                "analogy_en": "At a community water borehole, drawing 5 liters into a 20-liter jerrycan means filling 5/20, which is equal to 1/4 of the canister!"
            },
            "urban": {
                "analogy_sw": "Mtaani mkikatiana chapati moja kubwa au pizza katika vipande vinne sawa na ukala vipande 2, umekula 2/4, ambayo ni nusu (1/2) nzima ya chakula!",
                "analogy_en": "In the city, slicing one whole chapati or pizza into 4 equal slices and eating 2 means you consumed 2/4, which simplifies directly to 1/2!"
            }
        },
        "key_terms": [
            {"en": "Numerator", "sw": "Kiasi cha juu (Vipande vilivyopo)"},
            {"en": "Denominator", "sw": "Kiasi cha chini (Jumla ya vipande vyote)"},
            {"en": "Simplification", "sw": "Kurahisisha sehemu (mf. 2/4 = 1/2)"},
            {"en": "Proportion", "sw": "Uwiano sawa"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kugawa Karatasi Nusu na Robo",
            "title_en": "Experiment: Paper Fraction Folding",
            "materials_sw": "Karatasi moja ya daftari.",
            "materials_en": "Single sheet of notebook paper.",
            "steps_sw": "1. Kunja mara moja = umepata 1/2 na 1/2.\n2. Kunja tena = umepata 1/4 nne.\n3. Ona jinsi 2/4 ilivyo sawa na 1/2!",
            "steps_en": "1. Fold once = two halves (1/2 each).\n2. Fold again = four quarters (1/4 each).\n3. Observe how 2/4 occupies the identical area as 1/2!"
        },
        "quiz": {
            "question_sw": "Ikiwa mvuvi kule Kisumu ana samaki 8 wa Ngege na akagawia marafiki 4 kwa usawa, kila rafiki anapata samaki wangapi (sehemu gani)?",
            "question_en": "If a fisherman in Kisumu distributes 8 Tilapia equally among 4 friends, how many does each receive?",
            "options_sw": ["A) Samaki 2 (kila mmoja 1/4 ya jumla)", "B) Samaki 1", "C) Samaki 4", "D) Samaki 0"],
            "options_en": ["A) 2 fish (1/4 of total each)", "B) 1 fish", "C) 4 fish", "D) 0 fish"],
            "correct_index": 0,
            "explanation_sw": "Hongera! 8 yakigawanywa kwa 4 ni 2. Kila mmoja anapata robo (1/4) ya samaki wote, yaani samaki 2.",
            "explanation_en": "Great! 8 divided by 4 is 2. Each friend receives 1/4 of the total pool, which is 2 fish."
        }
    },
    {
        "id": "chemistry_reactions",
        "title_en": "Chemistry: Acids, Bases & Neutralization Reactions",
        "title_sw": "Kemia: Asidi, Besi na Mmenyuko wa Kikemia",
        "subject": "Chemistry",
        "cbc_strand": "Matter & Chemical Reactions (Junior Secondary Science)",
        "summary_en": "Acids (like lemon juice) and bases (like wood ash or baking soda) react chemically to neutralize each other, producing salt, water, and fizzing carbon dioxide gas.",
        "summary_sw": "Asidi (kama ndimu au siki) na besi (kama baking soda au majivu) huingiliana kikemia na kutulizana, zikitengeneza chumvi, maji, na kutoa gesi yenye viputo (CO₂).",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Gusa tone la juisi ya ndimu kwenye ulimi—ladha yake kali ya uchachu inatoka kwenye Asidi. Ukigusa maji yenye baking soda au majivu laini, hisi ulaini wake unaoteleza—hiyo ni tabia ya Besi. Ukiziweka pamoja, weka sikio lako karibu na chupa usikie sauti ya viputo 'tssshhhh'—huo ni mmenyuko wa kikemia unaotoa gesi!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Kioevu chenye Asidi] + [Ishara ya Unga wa Besi] ➔ [Ishara ya Viputo vinavyotoka kwa kasi (CO₂)].",

        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu wakati mama anaposafisha samaki Ngege kwa juisi ya ndimu (Asidi ya citric), asidi inakata harufu ya shombo ya samaki (ambayo ni amini zenye tabia ya besi) kwa kutumia kanuni ya kemia ya neutralization!",
                "analogy_en": "In Kisumu, when washing fresh Tilapia fish with lemon juice (citric acid), the acid neutralizes fishy amine bases through chemical neutralization!"
            },
            "coastal": {
                "analogy_sw": "Pwani, kupika vitumbua au mandazi kwa kutumia baking soda (Besi) na maji ya tui ya nazi au siki inafanya keki kufura vizuri kwa sababu ya gesi ya kaboni dioksidi inayozalishwa!",
                "analogy_en": "At the coast, baking mandazi with sodium bicarbonate (base) and vinegar releases bubbling CO2 that makes the dough rise fluffy and soft!"
            },
            "highlands": {
                "analogy_sw": "Mashambani kule Eldoret au Nakuru, wakulima huweka chokaa (Agricultural Lime / Besi) kwenye udongo wenye asidi nyingi ili kuusawazisha (neutralize) na kusaidia mimea ya mahindi kukua vizuri!",
                "analogy_en": "In highland farms like Eldoret, farmers add agricultural lime (base) to acidic soils to neutralize pH and boost maize yields!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo ya wafugaji, kutumia maziwa ya ngamia au majivu ya kuni kusafisha vyombo kunatokana na uwezo wa besi kuvunja mafuta kupitia mmenyuko wa kikemia!",
                "analogy_en": "In pastoral communities, using wood ash (alkali base) to clean cooking pots relies on chemistry to saponify and dissolve grease!"
            },
            "urban": {
                "analogy_sw": "Mtaani, kumeza dawa ya antacid (kama Eno au Andrews) ukiwa na kiungulia cha tumbo (stomach acid) inatuliza tumbo mara moja kwa kufanya acid-base neutralization!",
                "analogy_en": "In the city, taking an antacid (base) for stomach acid relief instantly neutralizes excess hydrochloric acid into harmless salt and water!"
            }
        },
        "key_terms": [
            {"en": "Acid", "sw": "Asidi (Kemikali yenye ladha ya chachu na pH chini ya 7)"},
            {"en": "Base / Alkali", "sw": "Besi (Kemikali yenye utelezi na pH juu ya 7)"},
            {"en": "Neutralization", "sw": "Mmenyuko wa Kutuliza (Asidi + Besi ➔ Chumvi + Maji)"},
            {"en": "Effervescence", "sw": "Uzalishaji wa Viputo vya Gesi"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Volkano ya Jikoni (Ndimu + Baking Soda)",
            "title_en": "Experiment: Kitchen Acid-Base Volcano",
            "materials_sw": "Nusu ndimu (Asidi), kijiko 1 cha baking soda (Besi), kikombe kidogo.",
            "materials_en": "Half a lemon (Acid), 1 spoon of baking soda (Base), small cup.",
            "steps_sw": "1. Weka baking soda kwenye kikombe.\n2. Kamulia maji ya ndimu juu yake.\n3. Tazama au sikiliza viputo vya hewa ya CO₂ vinavyotoka kwa kasi kama volkano!",
            "steps_en": "1. Place baking soda into the cup.\n2. Squeeze fresh lemon juice directly over it.\n3. Observe the rapid bubbling eruption of carbon dioxide gas!"
        },
        "quiz": {
            "question_sw": "Ni nini kinachozalishwa wakati Asidi (kama ndimu) inapokutana na Besi (kama baking soda)?",
            "question_en": "What is produced when an Acid reacts with a Base?",
            "options_sw": ["A) Chumvi, Maji, na Gesi ya Oksijeni/Kaboni (Neutralization)", "B) Sumu kali", "C) Umeme wa radi", "D) Dhahabu"],
            "options_en": ["A) Salt, Water, and Carbon Dioxide gas (Neutralization)", "B) Poison", "C) Lightning electricity", "D) Gold"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Asidi ikikutana na Besi hutengeneza chumvi, maji, na gesi yenye viputo.",
            "explanation_en": "Exactly right! Acids and bases react to form neutral salt, water, and bubbling gas."
        }
    },
    {
        "id": "computer_algorithms",
        "title_en": "Computer Science & Technology: Algorithms & Logic",
        "title_sw": "Sayansi ya Kompyuta & Teknolojia: Algoriti na Mantiki ya Maamuzi",
        "subject": "Computer Science",
        "cbc_strand": "Computing & Computational Thinking (Grade 6 / Junior School)",
        "summary_en": "An algorithm is a step-by-step recipe or set of precise instructions that a computer, phone, or robot follows to solve a problem or make automated decisions.",
        "summary_sw": "Algoriti ni mlolongo wa hatua au maagizo maalum ambayo kompyuta, simu au roboti hufuata hatua kwa hatua ili kutatua tatizo au kufanya maamuzi (kama If-Then-Else).",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria kichocheo cha kupika chai au ugali. Hatua ya 1: chemsha maji. Hatua ya 2: Kama maji yanatokota (True), weka unga. Kama bado hayajatokota (False), subiri. Mlolongo huu wa hatua za wazi na maamuzi ndio unaoitwa 'Algoriti ya Kompyuta'!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Hatua ya 1] ➔ [Ishara ya Swali/Uamuzi wa Njia Panda (If-Else)] ➔ [Ishara ya Kitendo cha NDIYO] au [Ishara ya Kitendo cha HAPANA].",

        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu ukiwasha pampu ya umeme ya kunyunyizia mashamba kando ya ziwa, unaweza kuandika algoriti: 'KAMA unyevu wa udongo uko chini ya 30%, BASI washa pampu; LA SIVYO, iache imezimwa!' Hii ni smart irrigation algorithm!",
                "analogy_en": "In Kisumu, an automated solar pump on a lake farm uses an algorithm: 'IF soil moisture < 30% THEN turn on pump ELSE keep pump off!' That is smart automated computing!"
            },
            "coastal": {
                "analogy_sw": "Pwani, taa za bandarini za Mombasa hutumia algoriti ya sensorer ya mwangaza: 'KAMA giza limeingia (usiku), BASI washa taa za lighthouse; KAMA jua limechomoza, ZIMA taa!'",
                "analogy_en": "At Mombasa port, lighthouse buoys follow an algorithm: 'IF ambient light is dark THEN turn on lighthouse light ELSE power off!' That is automated software logic!"
            },
            "highlands": {
                "analogy_sw": "Kwenye kiwanda cha majani ya chai kule Kericho, mashine ya kupima uzito hutumia algoriti: 'KAMA uzito wa gunia umefika kilo 50, BASI funga mfuko; LA SIVYO, endelea kujaza!'",
                "analogy_en": "In a Kericho tea factory, bagging machines use an algorithm: 'IF bag weight == 50kg THEN seal bag ELSE keep filling!'",
            },
            "arid": {
                "analogy_sw": "Kwenye vituo vya maji vya solar kule Turkana, kadi ya kidijitali (smart water meter) inafuata algoriti: 'KAMA salio la mtumiaji linatosha, FUNGUA bomba la maji; LA SIVYO, toa mlio wa onyo!'",
                "analogy_en": "In Turkana solar water kiosks, digital smart meters use: 'IF user token has credit THEN open water valve ELSE sound buzzer!'",
            },
            "urban": {
                "analogy_sw": "Kwenye jiji kama Nairobi, taa za barabarani (traffic lights) na mfumo wa kulipia M-PESA hutumia algoriti: 'KAMA nenosiri (PIN) ni sahihi na salio lipo, TUMA pesa mara moja!'",
                "analogy_en": "In Nairobi, M-PESA mobile money and smart traffic lights run on algorithms: 'IF PIN is correct and balance sufficient THEN transfer funds instantly!'",
            }
        },
        "key_terms": [
            {"en": "Algorithm", "sw": "Algoriti (Mlolongo wa hatua za kimantiki)"},
            {"en": "Condition (If-Then-Else)", "sw": "Masharti ya Maamuzi (Kama-Basi-La Sivyo)"},
            {"en": "Loop", "sw": "Mzunguko wa Marudio ya Hatua"},
            {"en": "Debugging", "sw": "Kurekebisha makosa kwenye mfumo"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuwa Roboti (Human Robot Algorithm Game)",
            "title_en": "Experiment: The Human Robot Algorithm Game",
            "materials_sw": "Marafiki wawili au mwanafunzi na mzazi.",
            "materials_en": "Two friends or student and parent.",
            "steps_sw": "1. Rafiki mmoja anafumba macho na kuwa 'Roboti'.\n2. Mwanafunzi anakuwa 'Programmer' na kutoa amri maalum tu: 'Piga hatua 2 mbele', 'Pinduka kulia digrii 90', 'Nyoosha mkono chukua kikombe'.\n3. Ona jinsi kompyuta inavyohitaji maagizo sahihi bila kukosea!",
            "steps_en": "1. One friend closes eyes to act as the 'Robot'.\n2. The student acts as the 'Programmer' giving strict commands: 'Walk 2 steps forward', 'Turn right 90 degrees', 'Reach hand and grasp cup'.\n3. Discover how computers require precise, bug-free step-by-step algorithms!"
        },
        "quiz": {
            "question_sw": "Ni nini maana ya Algoriti (Algorithm) katika sayansi ya kompyuta?",
            "question_en": "What is an Algorithm in computer science?",
            "options_sw": ["A) Mlolongo wa maagizo sahihi ya hatua kwa hatua kutatua tatizo", "B) Aina ya mchezo wa video", "C) Kioo cha simu", "D) Waya wa umeme"],
            "options_en": ["A) A step-by-step sequence of precise instructions to solve a problem", "B) A video game", "C) Phone glass", "D) Electric wire"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Algoriti ni kanuni au mlolongo wa hatua unaofuatwa na kompyuta au roboti kukamilisha kazi.",
            "explanation_en": "Spot on! An algorithm is a precise, ordered set of steps executed by a computer to accomplish a task."
        }
    },
    {
        "id": "algebra_math",
        "title_en": "Algebra: Balancing Equations & Unknown Variables (x & y)",
        "title_sw": "Aljebra: Mlinganyo na Kutafuta Nambari Zilizofichika (x na y)",
        "subject": "Mathematics",
        "cbc_strand": "Algebraic Expressions & Simple Equations (Junior Secondary Mathematics)",
        "summary_en": "Algebra uses letters (like x or y) to stand for unknown quantities. Solving an equation means keeping both sides of the '=' sign balanced like a market scale.",
        "summary_sw": "Aljebra hutumia herufi (kama x au y) kuwakilisha nambari zilizofichika. Kutatua mlinganyo ni kusawazisha pande zote mbili za alama ya '=' kama mizani ya sokoni.",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria mizani ya mawe sokoni. Upande wa kushoto una kifurushi cha siri (x) pamoja na mawe 3 ya kilo moja. Upande wa kulia una mawe 10 ya kilo moja na mizani imelingana sawasawa! Ili kujua uzito wa kifurushi (x), ondoa mawe 3 pande zote mbili: x = 10 - 3, hivyo x ni kilo 7!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Mizani iliyosawazika] + [Ishara ya Herufi x + 3 = 10] ➔ [Ishara ya Kupunguza 3 pande zote] ➔ [x = 7].",

        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule soko la Kibuye Kisumu, mchuuzi anaweka kapu lenye samaki wasiojulikana idadi yao (x) pamoja na samaki 4 wa nyongeza. Jumla yote inapimwa na kuwa samaki 12 (x + 4 = 12). Kujua idadi ya samaki ndani ya kapu, unatoa 4 kutoka kwa 12: x = 8!",
                "analogy_en": "At Kibuye market in Kisumu, a fish basket with unknown tilapia (x) plus 4 extra fish totals 12 on the scale (x + 4 = 12). Subtracting 4 from both sides reveals x = 8 tilapia!"
            },
            "coastal": {
                "analogy_sw": "Pwani, kapu la nazi (y) likiongezwa nazi 5 linakuwa na nazi 20 (y + 5 = 20). Kujua nazi zilizokuwepo ndani, unatoa 5 pande zote: y = 15!",
                "analogy_en": "At the coast, a crate of coconuts (y) plus 5 loose coconuts equals 20 (y + 5 = 20). Subtracting 5 gives y = 15 coconuts inside the crate!"
            },
            "highlands": {
                "analogy_sw": "Mashambani Eldoret, gunia la viazi (x) lililopunguzwa kilo 10 lina uzito wa kilo 40 (x - 10 = 40). Ili kujua uzito wa awali, unaongeza kilo 10 pande zote mbili: x = 50kg!",
                "analogy_en": "In highland farms, a sack of potatoes (x) with 10kg removed weighs 40kg (x - 10 = 40). Adding 10 to both sides restores x = 50kg!"
            },
            "arid": {
                "analogy_sw": "Kwenye kisima cha maji, dumu lenye lita (x) likiongezwa lita 6 linajaa kuwa lita 20 (x + 6 = 20). Maji yaliyokuwepo awali ni x = 20 - 6 = lita 14!",
                "analogy_en": "At a desert well, a jerrycan with water (x) plus 6 liters fills a 20-liter container (x + 6 = 20). The initial water was x = 14 liters!"
            },
            "urban": {
                "analogy_sw": "Mtaani, nauli ya matatu ni shilingi 50 na salio lako lililobaki baada ya kulipa ni shilingi 150 (x - 50 = 150). Pesa uliyokuwa nayo mwanzoni ni x = 150 + 50 = Shilingi 200!",
                "analogy_en": "In the city, paying a 50 KES matatu fare leaves 150 KES balance (x - 50 = 150). Your starting money was x = 200 KES!"
            }
        },
        "key_terms": [
            {"en": "Variable (x, y)", "sw": "Kigeuzi / Nambari Isiyojulikana"},
            {"en": "Equation", "sw": "Mlinganyo (Pande mbili zilizo sawa kwa alama ya =)"},
            {"en": "Balancing", "sw": "Kusawazisha Mizani ya Hesabu"},
            {"en": "Constant", "sw": "Nambari Isiyobadilika"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Mizani ya Vibandiko vya Hesabu",
            "title_en": "Experiment: The Matchbox Balance Equation",
            "materials_sw": "Kikombe kimoja (x), sarafu au maharagwe 10.",
            "materials_en": "One opaque cup (x), 10 beans or coins.",
            "steps_sw": "1. Ficha maharagwe kadhaa ndani ya kikombe (x).\n2. Weka maharagwe 3 pembeni ya kikombe: x + 3.\n3. Hesabu jumla yote (kama ni 7), toa 3 pembeni uone idadi ya maharagwe 4 ndani ya kikombe!",
            "steps_en": "1. Hide secret beans inside the cup (x).\n2. Place 3 beans beside the cup: x + 3.\n3. If total count is 7, subtract the 3 outer beans to reveal the 4 hidden beans inside!"
        },
        "quiz": {
            "question_sw": "Ikiwa x + 5 = 12, thamani ya x ni ngapi?",
            "question_en": "If x + 5 = 12, what is the value of x?",
            "options_sw": ["A) x = 7", "B) x = 17", "C) x = 5", "D) x = 60"],
            "options_en": ["A) x = 7", "B) x = 17", "C) x = 5", "D) x = 60"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Ili kupata x, toa 5 pande zote mbili: x = 12 - 5 = 7.",
            "explanation_en": "Excellent! Subtract 5 from both sides: x = 12 - 5 = 7."
        }
    }
]


# --- STAKEHOLDER RESOURCES ---

def generate_teacher_lesson_plan(topic_id: str, region: str) -> Dict[str, Any]:
    topic = find_offline_topic(topic_id)
    reg_info = REGIONS.get(region, REGIONS["lake_basin"])
    regional_analogy = topic["regional_analogies"].get(region, topic["regional_analogies"]["lake_basin"])

    return {
        "curriculum_strand": topic.get("cbc_strand", "CBC Science & Technology"),
        "grade_level": "Grade 5 & 6 (Upper Primary / Junior School)",
        "lesson_title": topic["title_sw"] + f" ({topic['title_en']})",
        "eco_zone": reg_info["name_sw"],
        "locality": reg_info["locality_name"],
        "learning_outcomes": [
            f"Mwanafunzi aweze kueleza dhana ya {topic['title_sw']} kwa kutumia mifano ya eneo la {reg_info['locality_name']}.",
            "Mwanafunzi aweze kutaja msamiati wa Kiingereza unaolingana na maneno ya Kiswahili.",
            "Kufanya jaribio salama la kisayansi kwa kutumia vifaa vya nyumbani/shuleni."
        ],
        "local_teaching_aid": regional_analogy["analogy_sw"],
        "tactile_support_for_blind": topic.get("tactile_audio_description_sw", ""),
        "visual_sign_for_deaf": topic.get("sign_language_visual_cues_sw", ""),
        "in_class_activity": topic["experiment"],
        "diagnostic_quiz": topic["quiz"],
        "dpa_privacy_note": "Hakuna data ya kibinafsi ya mtoto inayohitajika kufanya somo hili darasani."
    }


def generate_parent_digest(student_profile: Dict[str, Any], region: str) -> Dict[str, Any]:
    reg_info = REGIONS.get(region, REGIONS["lake_basin"])
    mastery = student_profile.get("mastery_graph", {})
    mastered_count = sum(1 for m in mastery.values() if m.get("mastery_score", 0) >= 50)

    return {
        "student_name": student_profile.get("name", "Mwanafunzi"),
        "grade": student_profile.get("grade_level", "Grade 6"),
        "region_name": reg_info["name_sw"],
        "topics_explored_count": len(mastery),
        "concepts_mastered_count": mastered_count,
        "badges_earned": student_profile.get("badges", ["🌟 Mwanzo Bora"]),
        "sms_digest_text": f"ElewaSTEM Ripoti ya Mzazi: {student_profile.get('name', 'Mwanafunzi')} ameelewa mada {mastered_count} za sayansi kwa mifano ya {reg_info['locality_name']}. Jaribio la wiki hii: Chunguza Oksijeni ya mimea jikoni!",
        "home_activity_for_parent": {
            "title": f"Jaribio la Jioni Nyumbani: Mimea na Maji ({reg_info['locality_name']})",
            "instructions": "Chukua jani bichi (kama sukuma au managu) na chupa ya maji. Weka juani na mtoto wako muhesabu viputo vya oksijeni vinavyotoka!"
        }
    }


def get_community_club_projects(region: str) -> List[Dict[str, Any]]:
    reg_info = REGIONS.get(region, REGIONS["lake_basin"])
    return [
        {
            "project_name": f"Klabu ya Mazingira & Maji Safi ({reg_info['locality_name']})",
            "materials": "Chupa za plastiki zilizotumika, mchanga safi, makaa ya jikoni, maji.",
            "objective": "Kutengeneza chujio rahisi la maji na kujifunza jinsi chembe ndogo zinavyochujwa.",
            "impact": "Inafundisha sayansi ya uchujaji (filtration) na uhifadhi wa vyanzo vya maji vya jamii."
        },
        {
            "project_name": f"Mradi wa Nishati ya Jua (Solar Cooker / Dryer)",
            "materials": "Karatasi ya alumini/foil, sanduku la kadibodi, kioo au nailoni safi.",
            "objective": "Kutumia nguvu ya jua kukausha mboga au kupasha maji joto.",
            "impact": "Inawafundisha watoto nishati mbadala (Renewable Solar Energy) bila gharama."
        }
    ]


def get_offline_starter_pack() -> List[Dict[str, Any]]:
    return OFFLINE_STEM_VAULT


def get_available_regions() -> Dict[str, Any]:
    return REGIONS


RELATED_TOPIC_GRAPH = {
    "photosynthesis": [
        {"id": "plant_pollination", "title_sw": "Uchavushaji & Uzazi wa Mimea (Biology)", "title_en": "Pollination & Plant Reproduction", "prompt": "Eleza jinsi uchavushaji na maua yanavyotengeneza mbegu", "icon": "🌸"},
        {"id": "aquatic_biology_kisumu", "title_sw": "Upumuaji wa Samaki & Matamvua/Gills (Biology)", "title_en": "Aquatic Fish Respiration", "prompt": "Eleza jinsi samaki wanavyotumia oksijeni ya mimea kupumua", "icon": "🐟"}
    ],
    "human_digestive_system": [
        {"id": "circulatory_heart", "title_sw": "Moyo & Mzunguko wa Damu (Biology)", "title_en": "Heart & Blood Circulation", "prompt": "Eleza jinsi damu inavyosambaza virutubisho vya chakula mwilini", "icon": "❤️"},
        {"id": "chemistry_reactions", "title_sw": "Asidi ya Tumbo & Kemia (Chemistry)", "title_en": "Stomach Acid Chemistry", "prompt": "Eleza jinsi asidi ya tumbo inavyovunja chakula", "icon": "⚗️"}
    ],
    "circulatory_heart": [
        {"id": "human_respiration", "title_sw": "Upumuaji wa Mapafu & Oksijeni (Biology)", "title_en": "Lungs & Oxygen Respiration", "prompt": "Eleza jinsi mapafu yanavyoingiza oksijeni kwenye damu", "icon": "🫁"},
        {"id": "human_digestive_system", "title_sw": "Mmeng'enyo wa Chakula & Lishe (Biology)", "title_en": "Digestive System & Nutrients", "prompt": "Eleza jinsi chakula kinavyomeng'enywa na kufyonzwa", "icon": "🍎"}
    ],
    "human_respiration": [
        {"id": "circulatory_heart", "title_sw": "Moyo & Mzunguko wa Damu (Biology)", "title_en": "Heart & Blood Circulation", "prompt": "Eleza jinsi damu inavyosafirisha oksijeni kutoka mapafuni", "icon": "❤️"},
        {"id": "photosynthesis", "title_sw": "Usanisinuru & Oksijeni ya Mimea (Biology)", "title_en": "Photosynthesis & Oxygen Source", "prompt": "Eleza jinsi mimea inavyozalisha oksijeni tunayopumua", "icon": "🌿"}
    ],
    "cell_biology": [
        {"id": "human_digestive_system", "title_sw": "Seli & Mmeng'enyo wa Chakula (Biology)", "title_en": "Cell Nutrition & Digestion", "prompt": "Eleza jinsi seli zinavyopata nishati ya chakula", "icon": "🔬"},
        {"id": "photosynthesis", "title_sw": "Kloroplasti & Usanisinuru (Biology)", "title_en": "Chloroplasts & Photosynthesis", "prompt": "Eleza kazi ya kloroplasti ndani ya seli ya mmea", "icon": "🌿"}
    ],
    "plant_pollination": [
        {"id": "photosynthesis", "title_sw": "Usanisinuru & Majani (Biology)", "title_en": "Photosynthesis in Leaves", "prompt": "Eleza jinsi majani ya mmea yanavyotengeneza chakula", "icon": "🌿"},
        {"id": "ecology_food_chains", "title_sw": "Wadudu & Mnyororo wa Chakula (Biology)", "title_en": "Pollinators & Food Webs", "prompt": "Eleza nafasi ya nyuki katika mazingira na kilimo", "icon": "🐝"}
    ],
    "living_things_classification": [
        {"id": "aquatic_biology_kisumu", "title_sw": "Samaki & Wenye Uti wa Mgongo (Biology)", "title_en": "Fish & Vertebrates", "prompt": "Eleza sifa za samaki kama wanyama wenye uti wa mgongo", "icon": "🐟"},
        {"id": "ecology_food_chains", "title_sw": "Mnyororo wa Chakula wa Wanyama (Biology)", "title_en": "Vertebrate Food Chains", "prompt": "Eleza mnyororo wa chakula wa wanyama wa mbugani", "icon": "🦁"}
    ],
    "ecology_food_chains": [
        {"id": "photosynthesis", "title_sw": "Mimea kama Watengenezaji Wakuu (Biology)", "title_en": "Plants as Producers", "prompt": "Eleza jinsi mimea inavyoanzisha mnyororo wa chakula", "icon": "🌿"},
        {"id": "living_things_classification", "title_sw": "Uainishaji wa Wanyama Walaji (Biology)", "title_en": "Herbivores & Carnivores", "prompt": "Eleza tofauti kati ya wanyama walaji majani na walaji nyama", "icon": "🐾"}
    ],
    "aquatic_biology_kisumu": [
        {"id": "human_respiration", "title_sw": "Upumuaji wa Binadamu vs Samaki (Biology)", "title_en": "Human vs Fish Respiration", "prompt": "Eleza tofauti ya upumuaji wa mapafu na mashavu ya samaki", "icon": "🫁"},
        {"id": "electricity_circuits", "title_sw": "Saketi za Umeme wa Kuvulia Ziwani (Physics)", "title_en": "Night Fishing Electric Circuits", "prompt": "Eleza jinsi saketi za taa za kuvulia samaki zinavyofanya kazi", "icon": "⚡"}
    ],
    "electricity_circuits": [
        {"id": "computer_algorithms", "title_sw": "Algoriti & Mantiki ya Kompyuta (Computer Science)", "title_en": "Computer Algorithms & Logic", "prompt": "Eleza jinsi kompyuta inavyofanya maamuzi ya If-Else", "icon": "💻"},
        {"id": "gravity_forces", "title_sw": "Nguvu za Mvuto & Msuguano (Physics)", "title_en": "Gravity & Friction Forces", "prompt": "Eleza nguvu ya mvuto na msuguano", "icon": "🌍"}
    ],
    "chemistry_reactions": [
        {"id": "human_digestive_system", "title_sw": "Kemia ya Mmeng'enyo wa Chakula (Biology)", "title_en": "Digestive Enzymes & Chemistry", "prompt": "Eleza jinsi asidi ya tumbo inavyomeng'enya chakula", "icon": "🍎"},
        {"id": "fractions_math", "title_sw": "Sehemu & Uwiano wa Vipimo (Mathematics)", "title_en": "Fractions & Proportions", "prompt": "Eleza sehemu na uwiano katika kugawa vitu", "icon": "🍕"}
    ],
    "computer_algorithms": [
        {"id": "electricity_circuits", "title_sw": "Saketi & Swichi za Kompyuta (Physics)", "title_en": "Circuits & Logic Gates", "prompt": "Eleza jinsi umeme na swichi zinavyoendesha kompyuta", "icon": "⚡"},
        {"id": "algebra_math", "title_sw": "Aljebra & Vigeuzi vya Kompyuta (Mathematics)", "title_en": "Algebra & Variables", "prompt": "Eleza aljebra na vigeuzi", "icon": "📐"}
    ],
    "fractions_math": [
        {"id": "algebra_math", "title_sw": "Aljebra & Milinganyo ya Hesabu (Mathematics)", "title_en": "Algebra & Equations", "prompt": "Eleza jinsi ya kutatua mlinganyo wa aljebra", "icon": "📐"},
        {"id": "chemistry_reactions", "title_sw": "Uwiano wa Kemia ya Asidi (Chemistry)", "title_en": "Chemical Ratios & Reactions", "prompt": "Eleza mmenyuko wa asidi na besi", "icon": "⚗️"}
    ],
    "gravity_forces": [
        {"id": "electricity_circuits", "title_sw": "Saketi za Umeme & Nguvu (Physics)", "title_en": "Electric Circuits & Energy", "prompt": "Eleza saketi kamili za umeme", "icon": "⚡"},
        {"id": "fractions_math", "title_sw": "Sehemu za Hesabu (Mathematics)", "title_en": "Fractions & Math", "prompt": "Eleza sehemu za nambari", "icon": "📐"}
    ],
    "algebra_math": [
        {"id": "fractions_math", "title_sw": "Sehemu & Nambari (Mathematics)", "title_en": "Fractions & Numbers", "prompt": "Eleza sehemu za nambari", "icon": "🍕"},
        {"id": "computer_algorithms", "title_sw": "Vigeuzi vya Kompyuta & Algoriti (Computer Science)", "title_en": "Variables & Algorithms", "prompt": "Eleza vigeuzi katika programu za kompyuta", "icon": "💻"}
    ]
}


def get_related_topics_recommendations(topic_id_or_query: str) -> List[Dict[str, Any]]:
    """Returns structured next topic recommendations based on current learning."""
    topic = find_offline_topic(topic_id_or_query)
    tid = topic.get("id", "photosynthesis")
    return RELATED_TOPIC_GRAPH.get(tid, RELATED_TOPIC_GRAPH.get("photosynthesis", []))


def find_offline_topic(query: str, preferred_subject: str = "all") -> Dict[str, Any]:
    query_lower = query.lower()
    
    # 1. Direct specific domain keyword matching (High Precision)
    # Digestion / Nutrition
    if any(k in query_lower for k in ["digest", "mmeng'enyo", "stomach", "tumbo", "esophagus", "umio", "mouth", "kinywa", "saliva", "mate", "intestine", "utumbo", "enzyme", "virutubisho", "chakula mwilini"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "human_digestive_system":
                return item

    # Circulatory / Heart / Blood
    if any(k in query_lower for k in ["heart", "moyo", "circulat", "mzunguko wa damu", "blood", "damu", "artery", "ateri", "vein", "vena", "pulse", "mapigo"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "circulatory_heart":
                return item

    # Aquatic fish respiration
    if any(k in query_lower for k in ["fish", "samaki", "gills", "mashavu", "matamvua", "ngege", "mbuta"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "aquatic_biology_kisumu":
                return item

    # Human Respiration / Lungs
    if any(k in query_lower for k in ["lung", "mapafu", "respirat", "upumuaji", "breathe", "pumua", "trachea", "koromeo", "inhale", "exhale", "diaphragm", "kiwambo"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "human_respiration":
                return item

    # Cell Biology
    if any(k in query_lower for k in ["cell", "seli", "nucleus", "kiini", "cytoplasm", "saikroplasimu", "membrane", "utando", "chloroplast", "kloroplasti"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "cell_biology":
                return item

    # Ecology & Food chains
    if any(k in query_lower for k in ["food chain", "mnyororo wa chakula", "ecolog", "ikolojia", "ecosystem", "producer", "mtengenezaji", "consumer", "mlaji", "predator", "mwindaji", "herbivore", "carnivore", "decomposer", "mwozeshaji"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "ecology_food_chains":
                return item

    # Pollination & Flowers
    if any(k in query_lower for k in ["pollinat", "uchavushaji", "flower", "maua", "petali", "petal", "stamen", "chavulio", "pistil", "kambamaua", "poleni", "chavua", "nectar"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "plant_pollination":
                return item

    # Living things classification
    if any(k in query_lower for k in ["vertebrate", "invertebrate", "uti wa mgongo", "classify", "uainishaji", "mammal", "mamalia", "reptile", "reptilia", "amphibian", "amfibea", "insect", "wadudu", "konokono", "buibui"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "living_things_classification":
                return item

    # Photosynthesis & Plant food
    if any(k in query_lower for k in ["photo", "usanisinuru", "klorofili", "chlorophyll", "plant food", "chakula cha mmea", "stomata", "majani yanavyopika"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "photosynthesis":
                return item

    # Algebra & Math
    if any(k in query_lower for k in ["algebra", "aljebra", "equation", "mlinganyo", "variable", "kigeuzi", "solve for x", "x +", "x -", "x ="]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "algebra_math":
                return item

    # Fractions
    if any(k in query_lower for k in ["fraction", "sehemu", "divide", "gawanya", "theluthi", "robo", "nusu", "proportion", "ratio"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "fractions_math":
                return item

    # Chemistry reactions
    if any(k in query_lower for k in ["chem", "kemia", "acid", "asidi", "base", "besi", "reaction", "neutraliz", "siki", "soda", "lemon", "chumvi"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "chemistry_reactions":
                return item

    # Computer science & algorithms
    if any(k in query_lower for k in ["comput", "code", "coding", "algorithm", "algoriti", "program", "logic", "software", "binary"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "computer_algorithms":
                return item

    # Physics Electricity & Circuits
    if any(k in query_lower for k in ["electr", "circuit", "umeme", "saketi", "wire", "waya", "battery", "betri", "voltage", "current"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "electricity_circuits":
                return item

    # Physics Gravity & Friction
    if any(k in query_lower for k in ["gravity", "grabiti", "force", "nguvu ya mvuto", "friction", "msuguano", "motion", "anguka"]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "gravity_forces":
                return item

    # 2. Exact match on ID or key terms
    for item in OFFLINE_STEM_VAULT:
        if (item["id"] in query_lower or 
            item["title_en"].lower() in query_lower or 
            item["title_sw"].lower() in query_lower or
            any(k["en"].lower() in query_lower or k["sw"].lower() in query_lower for k in item["key_terms"])):
            return item

    # 3. Match by preferred subject if selected
    if preferred_subject and preferred_subject != "all":
        subj_map = {
            "biology": "Biology",
            "physics": "Physics",
            "chemistry": "Chemistry",
            "mathematics": "Mathematics",
            "computer_science": "Computer Science"
        }
        target_subj = subj_map.get(preferred_subject.lower())
        if target_subj:
            for item in OFFLINE_STEM_VAULT:
                if item["subject"] == target_subj:
                    return item

    # 4. Keyword heuristic matching across STEM disciplines
    if any(k in query_lower for k in ["math", "hesabu", "number", "gawanya", "sehemu", "fraction", "ratio", "algebra", "calculate", "hesabu"]):
        for item in OFFLINE_STEM_VAULT:
            if item["subject"] == "Mathematics":
                return item
    elif any(k in query_lower for k in ["chem", "kemia", "acid", "asidi", "base", "besi", "reaction", "salt", "chumvi"]):
        for item in OFFLINE_STEM_VAULT:
            if item["subject"] == "Chemistry":
                return item
    elif any(k in query_lower for k in ["comput", "code", "coding", "algorithm", "algoriti", "program", "logic", "software"]):
        for item in OFFLINE_STEM_VAULT:
            if item["subject"] == "Computer Science":
                return item
    elif any(k in query_lower for k in ["electr", "circuit", "umeme", "saketi", "gravity", "mvuto", "physics", "fizikia", "force", "speed"]):
        for item in OFFLINE_STEM_VAULT:
            if item["subject"] == "Physics":
                return item
    elif any(k in query_lower for k in ["plant", "mmea", "fish", "samaki", "leaf", "jani", "cell", "living", "digest", "heart", "lung"]):
        for item in OFFLINE_STEM_VAULT:
            if item["subject"] == "Biology":
                return item

    return OFFLINE_STEM_VAULT[0]

