"""
ElewaSTEM Specialized Agent Tools with Hyper-Local Regional Ecosystems
Provides localized STEM analogies, experiments, and offline modules adapted to regional ecologies (Coastal, Highlands, Lake Basin, Arid, Urban).
"""

from typing import Dict, List, Any

# Regional Eco-Zones definition
REGIONS = {
    "coastal": {
        "id": "coastal",
        "name_sw": "Pwani na Bahari (Coastal)",
        "name_en": "Coastal & Ocean Zone",
        "examples": "Mombasa, Dar es Salaam, Zanzibar, Kilifi, Tanga",
        "icon": "🌊",
        "key_ecosystems": "Minazi (Coconuts), Mikoko (Mangroves), Bahari, Uvukizaji wa Chumvi (Salt Pans), Upepo wa Bahari"
    },
    "highlands": {
        "id": "highlands",
        "name_sw": "Nyanda za Juu & Kilimo (Highlands)",
        "name_en": "Highlands & Agricultural Belt",
        "examples": "Nakuru, Mt. Kenya, Arusha, Eldoret, Kisii, Meru",
        "icon": "⛰️",
        "key_ecosystems": "Mashamba ya Mahindi & Chai, Milima, Mito inayotiririka, Mvua nyingi, Udongo wa Volkano"
    },
    "lake_basin": {
        "id": "lake_basin",
        "name_sw": "Bonde la Ziwa (Lake Victoria Basin)",
        "name_en": "Lake Victoria Basin",
        "examples": "Kisumu, Mwanza, Entebbe, Homa Bay, Musoma",
        "icon": "🏞️",
        "key_ecosystems": "Ziwa Victoria, Samaki (Tilapia & Sangara), Magugu Maji (Water Hyacinth), Mvua za radi, Upepo wa ziwa"
    },
    "arid": {
        "id": "arid",
        "name_sw": "Maeneo Kavu & Ukame (Arid & Pastoralist)",
        "name_en": "Arid & Semi-Arid Lands (ASAL)",
        "examples": "Turkana, Garissa, Kajiado, Marsabit, Dodoma, Wajir",
        "icon": "☀️",
        "key_ecosystems": "Jua kali, Mbigili & Miti ya Mibabakhi (Acacia), Ngamia, Visima vya maji ya ardhini, Nishati ya Jua (Solar)"
    },
    "urban": {
        "id": "urban",
        "name_sw": "Mijini (Urban Centers)",
        "name_en": "Urban & Metropolitan Centers",
        "examples": "Nairobi, Kampala, Lagos, Dar es Salaam, Kigali",
        "icon": "🏙️",
        "key_ecosystems": "Taa za barabarani za Solar, Matatu electronics, Majengo, Mifereji ya maji ya mvua, Karakana"
    }
}


OFFLINE_STEM_VAULT = [
    {
        "id": "photosynthesis",
        "title_en": "Photosynthesis: How Plants Make Food",
        "title_sw": "Usanisinuru: Jinsi Mimea Inavyotengeneza Chakula",
        "subject": "Biology",
        "summary_en": "Plants use sunlight, water, and carbon dioxide from the air to produce glucose energy and release fresh oxygen.",
        "summary_sw": "Mimea hutumia mwangaza wa jua, maji kutoka ardhini, na hewa ya kaboni kutengeneza chakula chake (glukosi) huku ikitoa hewa safi ya oksijeni.",
        
        # Region-adaptive analogies
        "regional_analogies": {
            "coastal": {
                "analogy_sw": "Fikiria mnazi kule Pwani! Majani yake makubwa yaliyotandazwa kuelekea jua la pwani yanafanya kazi kama paneli za jua, yakifyonza maji ya ardhini na jua kupika maji matamu ya dafu!",
                "analogy_en": "Think of a coconut palm on the coast! Its broad fronds act like solar panels absorbing intense tropical coastal sun to brew sweet coconut water inside the fruit!"
            },
            "highlands": {
                "analogy_sw": "Fikiria shamba la mahindi au majani ya chai kule milimani. Kila jani la kijani ni kama jiko dogo linalotumia unyevu wa ukungu wa asubuhi na mwangaza wa jua kutengeneza punje za mahindi!",
                "analogy_en": "Think of lush maize or tea farms in the cool highlands. Each green leaf is a tiny kitchen utilizing morning mountain mist and bright sunlight to synthesize nutrients!"
            },
            "lake_basin": {
                "analogy_sw": "Tazama magugu maji au mimea kando ya Ziwa Victoria. Inachukua maji mengi ya ziwani na mwanga mkali wa jua kutengeneza majani mazito na kutoa oksijeni inayosaidia samaki kupumua!",
                "analogy_en": "Look at the reeds and flora along Lake Victoria. They absorb lake moisture and intense equatorial sun to fuel rapid growth while infusing the water with dissolved oxygen for tilapia!"
            },
            "arid": {
                "analogy_sw": "Kule Turkana au Garissa, miti ya mshikio (acacia) na mikakasi ina majani madogo sana yenye nta ili isipoteze maji, huku mizizi mirefu ikitafuta maji chini kabisa ya ardhi ili kupika chakula wakati wa jua kali!",
                "analogy_en": "In arid regions like Turkana or Garissa, acacia trees have tiny waxy leaves that minimize evaporation, while deep taproots pull groundwater to power photosynthesis under blazing sunlight!"
            },
            "urban": {
                "analogy_sw": "Fikiria miti iliyopandwa kando ya barabara za jiji. Majani yake yanafyonza hewa chafu ya kaboni inayotoka kwenye moshi wa magari na kuibadilisha kuwa hewa safi ya oksijeni kwa wakazi wa jiji!",
                "analogy_en": "Think of urban trees lining city avenues. Their leaves scrub carbon emissions from vehicle exhaust and convert it into crisp, oxygenated air for city dwellers!"
            }
        },
        "key_terms": [
            {"en": "Chlorophyll", "sw": "Klorofili (Rangi ya kijani inayovuta mwangaza)"},
            {"en": "Carbon Dioxide", "sw": "Gesi ya Kaboni Dioksidi"},
            {"en": "Oxygen", "sw": "Hewa Safi ya Oksijeni"},
            {"en": "Transpiration", "sw": "Mvukizo wa maji kupitia majani"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kushuhudia Oksijeni ya Mmea",
            "title_en": "Experiment: Seeing Plant Oxygen in Action",
            "materials_sw": "Jani bichi la eneo lako (mnazi, mahindi, au mti wa kawaida), chupa ya maji, jua.",
            "materials_en": "A fresh leaf from your local area, a clear glass or transparent bottle with water, sunlight.",
            "steps_sw": "1. Weka jani ndani ya chupa ya maji.\n2. Weka chupa juani kwa saa moja.\n3. Tazama viputo vidogo vya hewa vinavyojitokeza kwenye jani - hiyo ni Oksijeni safi!",
            "steps_en": "1. Submerge the leaf inside the bottle of water.\n2. Place it in direct sunlight for 1 hour.\n3. Watch tiny gas bubbles gather on the leaf surface - that is pure Oxygen!"
        },
        "quiz": {
            "question_sw": "Ni kipi mmea unachotoa hewani baada ya usanisinuru (photosynthesis)?",
            "question_en": "What do plants release into the atmosphere after photosynthesis?",
            "options_sw": ["A) Oksijeni safi", "B) Moshi", "C) Mchanga", "D) Maji ya chumvi"],
            "options_en": ["A) Pure Oxygen", "B) Smoke", "C) Sand", "D) Salt Water"],
            "correct_index": 0,
            "explanation_sw": "Sahihi! Mimea hutoa gesi ya oksijeni ambayo wanadamu na wanyama huivuta ili kuishi.",
            "explanation_en": "Correct! Plants produce oxygen, which humans and animals breathe to survive."
        }
    },
    {
        "id": "electricity_circuits",
        "title_en": "Electric Current & Circuits",
        "title_sw": "Mkondo wa Umeme na Saketi",
        "subject": "Physics",
        "summary_en": "Electric current is the continuous flow of charges through a closed circuit wire.",
        "summary_sw": "Mkondo wa umeme ni mwendo wa chembe ndogo za chaji zinazosafiri kwenye waya uliounganishwa bila kukatika.",
        "regional_analogies": {
            "coastal": {
                "analogy_sw": "Kama pampu ya maji inayosukuma maji ya bahari kwenye mashamba ya chumvi kule Gongoni/Malindi, voltage ni shinikizo la pampu na current ni kiasi cha maji yanayotiririka!",
                "analogy_en": "Like water pumps pushing brine into coastal salt evaporating beds, voltage is the pump pressure and current is the volume of flow through the pipes!"
            },
            "highlands": {
                "analogy_sw": "Fikiria mtambo wa umeme wa maji (hydroelectric dam) kule Masinga au Sondu Miriu. Maji yanayoanguka kutoka juu milimani yana shinikizo kubwa (Voltage) linalosukuma jenereta kuzunguka!",
                "analogy_en": "Think of hydroelectric power stations in the highlands. High-altitude dam reservoirs build intense pressure (Voltage) that drives turbine current through the power grid!"
            },
            "lake_basin": {
                "analogy_sw": "Fikiria injini ya mashua ya wavuvi kule ziwani. Betri ya 12V inasukuma mkondo wa umeme kwenye taa ya kuvulia usiku (taa ya dagaa). Saketi ikikatika taa inazima mara moja!",
                "analogy_en": "Think of a night fisherman's lantern powered by a 12V battery on Lake Victoria. Current flows through waterproof insulated wires to keep the lights beaming for fish tracking!"
            },
            "arid": {
                "analogy_sw": "Kule Turkana na Garissa, paneli ya jua (Solar PV) inavuna mwangaza wa jua na kuutuma kwenye betri. Shinikizo la volteji linasukuma umeme kwenye pampu ya kisima cha maji (borehole solar pump)!",
                "analogy_en": "In sun-drenched pastoralist areas like Garissa, solar PV panels convert sunlight into voltage that drives deep borehole water pumps for communities and livestock!"
            },
            "urban": {
                "analogy_sw": "Kwenye mji kama Nairobi au Dar, fikiria jinsi taa za barabarani za solar au betri ya matatu inavyosambaza umeme kwenye taa na muziki kupitia mtandao wa nyaya!",
                "analogy_en": "In cities, think of solar smart streetlights and vehicle circuits channeling current to lighting systems and audio amplifiers through closed loop wiring!"
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
        "summary_en": "Gravity pulls mass toward the center of the Earth. Friction opposes motion between contacting surfaces.",
        "summary_sw": "Mvuto wa ardhi (Grabiti) huvuta vitu chini ardhini. Msuguano huzuia au kupunguza mwendo vitu vinapogusana.",
        "regional_analogies": {
            "coastal": {
                "analogy_sw": "Kwenye fukwe za pwani, mnazi ukiangusha dafu, grabiti inalivuta chini kwenye mchanga. Kukokota mashua kwenye mchanga mkavu kuna msuguano mkubwa kuliko kwenye maji laini!",
                "analogy_en": "On sandy beaches, falling coconuts drop straight down due to gravity. Dragging a wooden dhow boat over dry sand encounters high friction, while floating on water has minimal friction!"
            },
            "highlands": {
                "analogy_sw": "Unapoendesha baiskeli ikiteremka mlima mwinuko, grabiti inakuvuta kwa kasi kuelekea chini. Unapobonyeza breki kwenye barabara ya vumbi nyekundu, msuguano ndio unaosimamishe baiskeli!",
                "analogy_en": "Coasting a bicycle down a steep highland ridge, gravity accelerates you downhill. Clamping your rubber brake pads against the wheels creates friction against the red earth road to stop you!"
            },
            "lake_basin": {
                "analogy_sw": "Mvuvi anaporusha nanga nzito ya chuma ziwani, inazama chini ya maji kwa sababu ya mvuto wa grabiti!",
                "analogy_en": "When a fisherman casts a heavy iron anchor into Lake Victoria, Earth's gravity pulls it rapidly to the lake bed to moor the boat securely!"
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
            "question_sw": "Kwa nini embe au dafu lililoiva huanguka chini ardhini badala ya kupaa angani?",
            "question_en": "Why does a ripe fruit fall to the ground instead of floating into the clouds?",
            "options_sw": ["A) Kwa sababu ya nguvu ya mvuto wa ardhi (Grabiti)", "B) Kwa sababu ya upepo", "C) Kwa sababu ya jua", "D) Kwa sababu limebadilika rangi"],
            "options_en": ["A) Earth's gravitational pull", "B) Wind gusts", "C) Sunlight", "D) Color change"],
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
        "summary_en": "A fraction represents equal parts of a whole quantity (Numerator / Denominator).",
        "summary_sw": "Sehemu (Fraction) huonyesha vipande vilivyogawanywa sawasawa kutoka kwa kitu kizima kimoja.",
        "regional_analogies": {
            "coastal": {
                "analogy_sw": "Kule pwani ukipasua dafu na nazi ikagawanywa kwa watoto wawili sawa, kila mmoja anapata nusu (1/2). Ukigawa samaki mmoja kwa sahani 4 sawa za biriani, kila sahani ina robo (1/4)!",
                "analogy_en": "On the coast, splitting a fresh coconut between two siblings gives each exactly one half (1/2). Dividing a large fish across 4 equal plates gives each 1/4 of the catch!"
            },
            "highlands": {
                "analogy_sw": "Shambani ukivuna gunia la viazi na kugawa katika vikapu vitatu vilivyo sawa, kila kikapu kimepata theluthi (1/3) ya mavuno yote!",
                "analogy_en": "On a highland farm, dividing a potato harvest into 3 equal crates means each crate contains exactly one-third (1/3) of the total harvest!"
            },
            "lake_basin": {
                "analogy_sw": "Ukinunua kapu lenye samaki 10 ziwani na ukapika samaki 5, umepika 5/10 ya samaki wote, ambayo ikirahisishwa ni nusu kamili (1/2)!",
                "analogy_en": "Buying a basket of 10 fresh tilapia at the lake pier and cooking 5 of them means you used 5/10, which simplifies to exactly 1/2 of your total fish!"
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
            "question_sw": "Ikiwa unagawia marafiki 4 machungwa 8 kwa usawa, kila rafiki anapata machungwa mangapi (sehemu gani)?",
            "question_en": "If you distribute 8 oranges equally among 4 friends, how many does each receive?",
            "options_sw": ["A) Machungwa 2 (kila mmoja 1/4 ya jumla)", "B) Chungwa 1", "C) Machungwa 4", "D) Chungwa 0"],
            "options_en": ["A) 2 oranges (1/4 of total each)", "B) 1 orange", "C) 4 oranges", "D) 0 oranges"],
            "correct_index": 0,
            "explanation_sw": "Hongera! 8 yakigawanywa kwa 4 ni 2. Kila mmoja anapata robo (1/4) ya machungwa yote, yaani machungwa 2.",
            "explanation_en": "Great! 8 divided by 4 is 2. Each friend receives 1/4 of the total pool, which is 2 oranges."
        }
    }
]


def get_offline_starter_pack() -> List[Dict[str, Any]]:
    return OFFLINE_STEM_VAULT


def get_available_regions() -> Dict[str, Any]:
    return REGIONS


def find_offline_topic(query: str) -> Dict[str, Any]:
    query_lower = query.lower()
    for item in OFFLINE_STEM_VAULT:
        if (item["id"] in query_lower or 
            item["title_en"].lower() in query_lower or 
            item["title_sw"].lower() in query_lower or
            item["subject"].lower() in query_lower or
            any(k["en"].lower() in query_lower or k["sw"].lower() in query_lower for k in item["key_terms"])):
            return item
    return OFFLINE_STEM_VAULT[0]
