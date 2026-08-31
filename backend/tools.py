"""
ElewaSTEM Specialized Agent Tools with Deep Hyper-Local African Ecosystems, Stakeholder Resources, and Universal Accessibility
Includes tactile audio descriptions for visually impaired/blind learners, visual sign language cues for deaf learners, and dyslexia adaptations.
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
        "summary_sw": "Samaki kama Ngege (Tilapia) na Mbuta (Nile Perch) wanapumua ndani ya maji kwa kutumia yavuyavu (gills/mashavu) zinazochuja oksijeni iliyoyeyushwa kwenye maji ya ziwa.",
        
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria kichwa cha samaki Ngege. Kando ya kichwa kuna mashavu mawili yanayojifungua na kujifunga. Ndani yake kuna tabaka nyembamba laini zenye rangi nyekundu ya damu zinazofanya kazi kama chujio la hewa. Maji yakipita, chujio hili linafyonza hewa ya oksijeni na kuituma kwenye damu ya samaki!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Samaki anayeogelea] + [Ishara ya Mashavu yanayopumua] + [Mchoro wa Chujio linalovuta Oksijeni].",

        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Dunga Beach au Luanda Kotieno kando ya Ziwa Victoria, unapoangalia samaki Ngege (Tilapia), mashavu yake yakifunguka na kufunga, yanafanya kazi kama chujio maalum (filter) linalofyonza oksijeni kutoka majini na kuingiza kwenye damu yake!",
                "analogy_en": "At Dunga Beach in Kisumu, when you watch a fresh Tilapia (Ngege), its operculum gills flap to pump lake water across gill filaments that filter dissolved oxygen directly into its bloodstream!"
            },
            "coastal": {
                "analogy_sw": "Kule Pwani, samaki wa baharini kama Changwa au Taa wanatumia mashavu yao kuchuja oksijeni kwenye maji yenye chumvi ya Bahari ya Hindi!",
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
            {"en": "Gills (Operculum)", "sw": "Mashavu / Yavuyavu ya samaki"},
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
            "options_sw": ["A) Yavuyavu / Mashavu (Gills)", "B) Mapafu kama ya binadamu", "C) Mkia", "D) Macho"],
            "options_en": ["A) Gills (Yavuyavu)", "B) Human-like lungs", "C) Tail fin", "D) Eyes"],
            "correct_index": 0,
            "explanation_sw": "Hodari sana! Samaki hutumia yavuyavu (gills) kuchuja oksijeni moja kwa moja kutoka kwenye maji ya ziwa.",
            "explanation_en": "Brilliant! Fish use their gills to extract dissolved oxygen directly from water."
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
        {"id": "aquatic_biology_kisumu", "title_sw": "Upumuaji wa Samaki & Yavuyavu (Biology)", "title_en": "Aquatic Fish Respiration", "prompt": "Eleza jinsi samaki wanavyotumia oksijeni ya mimea ya ziwani kupumua", "icon": "🐟"},
        {"id": "chemistry_reactions", "title_sw": "Kemia ya Asidi & Mmenyuko (Chemistry)", "title_en": "Acids & Chemical Reactions", "prompt": "Eleza kemia ya asidi na besi", "icon": "⚗️"}
    ],
    "aquatic_biology_kisumu": [
        {"id": "photosynthesis", "title_sw": "Usanisinuru & Oksijeni ya Mimea (Biology)", "title_en": "Photosynthesis & Oxygen", "prompt": "Eleza jinsi mimea inavyotengeneza chakula na kutoa oksijeni", "icon": "🌿"},
        {"id": "electricity_circuits", "title_sw": "Saketi za Umeme wa Kuvulia Ziwani (Physics)", "title_en": "Night Fishing Electric Circuits", "prompt": "Eleza jinsi saketi za taa za kuvulia samaki zinavyofanya kazi", "icon": "⚡"}
    ],
    "electricity_circuits": [
        {"id": "computer_algorithms", "title_sw": "Algoriti & Mantiki ya Kompyuta (Computer Science)", "title_en": "Computer Algorithms & Logic", "prompt": "Eleza jinsi kompyuta inavyofanya maamuzi ya If-Else", "icon": "💻"},
        {"id": "gravity_forces", "title_sw": "Nguvu za Mvuto & Msuguano (Physics)", "title_en": "Gravity & Friction Forces", "prompt": "Eleza nguvu ya mvuto na msuguano", "icon": "🌍"}
    ],
    "chemistry_reactions": [
        {"id": "photosynthesis", "title_sw": "Klorofili & Mmenyuko wa Jua (Biology)", "title_en": "Photosynthesis Reaction", "prompt": "Eleza usanisinuru kama mmenyuko wa kikemia", "icon": "🌿"},
        {"id": "fractions_math", "title_sw": "Sehemu & Uwiano wa Vipimo (Mathematics)", "title_en": "Fractions & Proportions", "prompt": "Eleza sehemu na uwiano katika kugawa vitu", "icon": "🍕"}
    ],
    "computer_algorithms": [
        {"id": "electricity_circuits", "title_sw": "Saketi & Swichi za Kompyuta (Physics)", "title_en": "Circuits & Logic Gates", "prompt": "Eleza jinsi umeme na swichi zinavyoendesha kompyuta", "icon": "⚡"},
        {"id": "fractions_math", "title_sw": "Hisabati & Nambari (Mathematics)", "title_en": "Fractions & Math", "prompt": "Eleza sehemu za hesabu", "icon": "📐"}
    ],
    "fractions_math": [
        {"id": "computer_algorithms", "title_sw": "Algoriti & Hatua za Hesabu (Computer Science)", "title_en": "Algorithms & Logic", "prompt": "Eleza algoriti za kompyuta", "icon": "💻"},
        {"id": "chemistry_reactions", "title_sw": "Uwiano wa Kemia ya Asidi (Chemistry)", "title_en": "Chemical Ratios & Reactions", "prompt": "Eleza mmenyuko wa asidi na besi", "icon": "⚗️"}
    ],
    "gravity_forces": [
        {"id": "electricity_circuits", "title_sw": "Saketi za Umeme & Nguvu (Physics)", "title_en": "Electric Circuits & Energy", "prompt": "Eleza saketi kamili za umeme", "icon": "⚡"},
        {"id": "fractions_math", "title_sw": "Sehemu za Hesabu (Mathematics)", "title_en": "Fractions & Math", "prompt": "Eleza sehemu za nambari", "icon": "📐"}
    ]
}


def get_related_topics_recommendations(topic_id_or_query: str) -> List[Dict[str, Any]]:
    """Returns structured next topic recommendations based on current learning."""
    topic = find_offline_topic(topic_id_or_query)
    tid = topic.get("id", "photosynthesis")
    return RELATED_TOPIC_GRAPH.get(tid, RELATED_TOPIC_GRAPH["photosynthesis"])


def find_offline_topic(query: str, preferred_subject: str = "all") -> Dict[str, Any]:
    query_lower = query.lower()
    
    # 1. Direct algebra match
    if any(k in query_lower for k in ["algebra", "aljebra", "equation", "mlinganyo", "variable", "kigeuzi", "solve for x", "x +", "x -", "x ="]):
        for item in OFFLINE_STEM_VAULT:
            if item["id"] == "algebra_math":
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
    elif any(k in query_lower for k in ["plant", "mmea", "fish", "samaki", "leaf", "jani", "bio", "botany", "cell", "living"]):
        for item in OFFLINE_STEM_VAULT:
            if item["subject"] == "Biology":
                return item

    return OFFLINE_STEM_VAULT[0]
