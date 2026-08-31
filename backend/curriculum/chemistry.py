"""
ElewaSTEM Curriculum — Chemistry Learning Modules (10 Topics)
Aligned with KICD (Kenya CBC Grades 4-9), NERDC (Nigeria), DBE CAPS (South Africa), NaCCA (Ghana).
"""

from typing import List, Dict, Any

CHEMISTRY_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "chemistry_reactions",
        "title_en": "Acids, Bases & Neutralization",
        "title_sw": "Kemia ya Asidi, Besi, Viashiria (Indicators) na Chumvi",
        "subject": "Chemistry",
        "cbc_strand": "Mixtures, Elements & Compounds (Grade 7/8 Integrated Science)",
        "summary_en": "Acids (sour, pH < 7) react with bases (bitter/soapy, pH > 7) in a neutralization reaction to produce harmless water and salt (pH = 7).",
        "summary_sw": "Asidi (zenye ladha ya uchachu, pH < 7) hugusana na Besi (zenye utelezi na uchungu, pH > 7) katika mmenyuko wa kutulizana (Neutralization) na kuunda chumvi na maji safi (pH = 7).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Gusa kipande cha limau ncha ya ulimi wako—utahisi ladha kali ya uchachu (Asidi ya Citric). Sasa gusa tone la maji ya sabuni au majivu ya jikoni kwa vidole—utahisi utelezi laini kama mafuta (Besi). Unapochanganya vyote viwili, vinatulizana na kuwa chumvi na maji!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Limau / Asidi pH < 7] + [Sabuni / Besi pH > 7] ➔ [Karatasi ya Litmasi inabadilika Rangi] ➔ [Mchanganyiko unakuwa Maji na Chumvi / pH 7].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu unaposafisha sufuria ya samaki iliyo na harufu au magamba, unatumia juisi ya limau (Asidi) kutuliza harufu ya samaki (Amine Base) kuwa chumvi isiyo na harufu!",
                "analogy_en": "In lake kitchens when preparing fish dishes, lemon juice citric acid neutralizes fish amine bases, eliminating pungent fishy odors instantly!"
            },
            "coastal": {
                "analogy_sw": "Pwani, uking'atwa na nyigu (wasp sting yenye alkali/besi), wazee hupaka siki au ndimu (asidi) ili kutuliza maumivu ya sumu ya nyigu mara moja!",
                "analogy_en": "At the coast, acidic vinegar or lime juice neutralizes alkaline wasp venom stings to relieve pain rapidly!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, wakulima wa chai na mahindi hupima pH ya udongo na kuweka chokaa ya kilimo (Agricultural Lime - Base) ili kutuliza asidi ya udongo na kuongeza mavuno!",
                "analogy_en": "In highland agricultural soils, farmers apply agricultural limestone (calcium carbonate base) to neutralize soil acidity and boost maize harvests!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame ya Ziwa Magadi, magadi ya soda (Sodium Carbonate) ni besi imara inayotumiwa viwandani kutengeneza glasi na sabuni safi!",
                "analogy_en": "At Lake Magadi, trona deposits (sodium carbonate base) are mined industrially to manufacture soaps and glass products!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mtu akiwa na maumivu ya kiungulia tumboni (asidi nyingi ya tumbo), hunywa dawa ya 'Antacid' (Besi ya Magnesium) inayotuliza asidi hiyo kuwa maji salama!",
                "analogy_en": "In city pharmacies, antacid tablets contain magnesium hydroxide bases that neutralize excess stomach hydrochloric acid to relieve heartburn!"
            }
        },
        "key_terms": [
            {"en": "Acids (pH 0 - 6.9)", "sw": "Asidi (Ladha ya uchachu, mf. Ndimu, Siki)"},
            {"en": "Bases / Alkalis (pH 7.1 - 14)", "sw": "Besi / Alkali (Utelezi na uchungu, mf. Sabuni, Majivu)"},
            {"en": "Neutralization Reaction", "sw": "Mmenyuko wa Kutulizana: Asidi + Besi ➔ Chumvi + Maji"},
            {"en": "Indicators (Litmus / Hibiscus)", "sw": "Viashiria vya pH (Karatasi ya Litmasi / Juisi ya Maua)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kutengeneza Kiashiria cha pH cha Asili kwa Maua ya Zambarau au Majani ya Chai",
            "title_en": "Experiment: Red Cabbage / Hibiscus Natural pH Indicator Test",
            "materials_sw": "Juisi ya maua ya waridi/hibiscus au kabichi nyekundu, vijiko viwili, maji ya limau (asidi), maji ya sabuni (besi).",
            "materials_en": "Hibiscus flower extract or red cabbage water, lemon juice (acid), soap water (base).",
            "steps_sw": "1. Weka juisi ya hibiscus kwenye glasi mbili safi.\n2. Ongeza matone ya limau kwenye glasi A—rangi itabadilika kuwa nyekundu ing'aayo (Asidi)!\n3. Ongeza matone ya sabuni kwenye glasi B—rangi itabadilika kuwa kijani/bluu (Besi)!",
            "steps_en": "1. Pour hibiscus extract into two clear glasses.\n2. Add lemon juice to glass A—it turns vivid bright pink/red (acid)!\n3. Add soap water to glass B—it turns dark green/blue (base)!"
        },
        "quiz": {
            "question_sw": "Ni nini kinachozalishwa wakati Asidi inapochanganywa na Besi katika mmenyuko wa Neutralization?",
            "question_en": "What products are formed when an Acid reacts completely with a Base in a neutralization reaction?",
            "options_sw": ["A) Chumvi na Maji (Salt and Water)", "B) Moshi na moto tu", "C) Petroli", "D) Mawe"],
            "options_en": ["A) Salt and Water", "B) Smoke and fire only", "C) Petrol", "D) Stones"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Asidi + Besi hutoa Chumvi na Maji (mfano: HCl + NaOH ➔ NaCl + H2O).",
            "explanation_en": "Brilliant! Neutralization of an acid by a base yields water and a chemical salt."
        }
    },
    {
        "id": "states_of_matter",
        "title_en": "States of Matter & Kinetic Particle Theory",
        "title_sw": "Hali za Maada na Nadharia ya Chembechembe (Kinetic Theory)",
        "subject": "Chemistry",
        "cbc_strand": "Mixtures, Elements & Compounds (Grade 7/8 Integrated Science)",
        "summary_en": "All matter exists in three main states: Solid (fixed shape, tightly packed vibrating particles), Liquid (fixed volume, flowing particles), and Gas (freely expanding particles). Heating adds kinetic energy, causing state changes.",
        "summary_sw": "Maada zote zipo katika hali tatu kuu: Mango (Solid - umbo thabiti), Kimiminika (Liquid - hutiririka), na Gesi (Gas - chembe huru). Kupasha joto huongeza mwendo wa chembe na kubadilisha hali ya maada.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika barafu gumu mkononi (Mango / Solid). Iache iyeyuke mkononi kwa joto la mwili wako—itabadilika kuwa maji ya baridi (Kimiminika / Liquid). Kisha fikiria ukichemsha maji hayo sufuriani, yatabadilika kuwa mvuke unaopaa angani (Gesi / Gas)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Barafu Mango] ➔ [Kuyeyuka / Melting kuwa Kimiminika] ➔ [Kuchemka / Evaporation kuwa Gesi ya Mvuke].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria wakati wa alasiri, joto la jua hubadilisha maji ya ziwa (Liquid) kuwa mvuke usioonekana wa gesi unaopaa angani kutengeneza mawingu ya mvua (Evaporation & Condensation)!",
                "analogy_en": "Over Lake Victoria, equatorial solar heat evaporates lake water liquid into atmospheric water vapor gas, fueling afternoon rainfall condensation cycles!"
            },
            "coastal": {
                "analogy_sw": "Pwani, joto la jua hutumiwa kukausha maji ya bahari kwenye madimbwi ya chumvi kule Gongoni Malindi—maji yanageuka mvuke na kuacha fuwele ngumu za chumvi (Solid crystals)!",
                "analogy_en": "Along coastal salt pans in Malindi, solar evaporation of seawater liquid leaves behind glistening solid crystalline sodium chloride salts!"
            },
            "highlands": {
                "analogy_sw": "Kileleni mwa Mlima Kenya ambapo kuna baridi kali, maji huganda kuwa barafu imara (Solid Glaciers) kisha jua linapochomoza yanayeyuka na kutiririka mito mikuu kama Mto Tana!",
                "analogy_en": "On Mount Kenya's sub-zero peaks, liquid water freezes into solid ice glaciers that melt into crystal highland river streams like River Tana!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame ya joto, manukato au mafuta yanapofunguliwa, chembe zake za gesi husambaa kwa kasi ya ajabu chumbani kote kwa njia ya mtawanyiko (Diffusion)!",
                "analogy_en": "In hot desert rooms, perfume and scent molecules diffuse rapidly through the air due to high kinetic particle velocities!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mtungi wa gesi ya kupikia jikoni (LPG) huhifadhi gesi iliyoshinikizwa kwa nguvu kuwa kimiminika, inayotoka kama gesi mara tu unapoifungua!",
                "analogy_en": "In urban households, LPG cooking cylinders store propane/butane compressed under pressure as a liquid that vaporizes into gas at the burner!"
            }
        },
        "key_terms": [
            {"en": "Solid, Liquid, Gas", "sw": "Mango, Kimiminika, na Gesi"},
            {"en": "Melting & Freezing", "sw": "Kuyeyuka (Mango ➔ Kioevu) na Kuganda"},
            {"en": "Evaporation & Condensation", "sw": "Uvukizi (Kioevu ➔ Gesi) na Mgando wa Mvuke"},
            {"en": "Diffusion", "sw": "Mtawanyiko wa Chembechembe (Diffusion)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Mtawanyiko (Diffusion) wa Rangi Ndani ya Maji",
            "title_en": "Experiment: Food Coloring Diffusion Rate in Cold vs Warm Water",
            "materials_sw": "Glasi mbili za maji (moja ya baridi, moja ya vuguvugu), tone la wino au rangi ya chakula.",
            "materials_en": "Two clear glasses (cold water and warm water), food coloring / ink droplet.",
            "steps_sw": "1. Weka tone moja la rangi kwenye maji ya baridi na tone moja kwenye maji ya vuguvugu bila kukoroga.\n2. Kwenye maji ya vuguvugu, rangi itatawanyika kwa kasi zaidi chombo kizima!\n3. Joto linaongeza mwendo wa chembechembe (Kinetic Energy)!",
            "steps_en": "1. Drop ink into cold water and warm water simultaneously without stirring.\n2. Observe the ink disperse far faster in warm water.\n3. Proves thermal energy accelerates kinetic molecular motion!"
        },
        "quiz": {
            "question_sw": "Ni mabadiliko gani ya hali ya maada yanayotokea wakati barafu inapopata joto na kubadilika kuwa maji ya kimiminika?",
            "question_en": "What phase change occurs when solid ice absorbs thermal energy and turns into liquid water?",
            "options_sw": ["A) Kuyeyuka (Melting)", "B) Kuganda", "C) Kuchoma", "D) Kupotea"],
            "options_en": ["A) Melting", "B) Freezing", "C) Burning", "D) Disappearing"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Kuyeyuka (Melting) ni mabadiliko ya hali ya maada kutoka Mango (Solid) kuwa Kimiminika (Liquid) kutokana na kuongezeka kwa joto.",
            "explanation_en": "Spot on! Melting is the endothermic phase transition of a substance from solid to liquid."
        }
    },
    {
        "id": "separation_techniques",
        "title_en": "Separation of Mixtures: Filtration, Evaporation & Distillation",
        "title_sw": "Mbinu za Kutenganisha Michanganyiko: Kuchuja, Kuvukiza na Kunereka (Distillation)",
        "subject": "Chemistry",
        "cbc_strand": "Mixtures, Elements & Compounds (Grade 7/8 Integrated Science)",
        "summary_en": "Mixtures are physically combined substances separated by physical methods: Filtration (insoluble solids from liquids), Evaporation (soluble salts), Simple Distillation (pure water from saltwater), and Fractional Distillation (liquids with different boiling points like crude oil).",
        "summary_sw": "Michanganyiko hutenganishwa kwa mbinu za kifizikia: Kuchuja (Filtration - mchanga na maji), Kuvukiza (Evaporation - chumvi na maji), na Kunereka (Distillation - kutenganisha maji safi ya kunywa au mafuta kwa tofauti ya viwango vya kuchemka).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Changanya mchanga na maji kwenye chombo kimoja kisha umwage kupitia kitambaa safi au karatasi ya chujio. Maji safi yatapita chini lakini chembe za mchanga zitabaki juu ya kitambaa. Hiyo ndiyo njia ya Kuchuja (Filtration)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kuchuja Mchanga kwa Karatasi / Filtration] ➔ [Kuvukiza Maji ya Chumvi Jikoni / Evaporation] ➔ [Mvuke unapopozwa kuwa Maji Safi / Distillation].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu kando ya Ziwa Victoria, mitambo ya kutibu maji ya manispaa hutumia mchanga safi na makaa kuchuja tope la ziwani (Filtration) na kuongeza klorini kuua vijidudu!",
                "analogy_en": "In municipal water treatment works near Lake Victoria, multi-stage sand filters eliminate suspended silt particles before chlorine disinfection!"
            },
            "coastal": {
                "analogy_sw": "Pwani, mitambo ya kuondoa chumvi baharini (Desalination plants) huchemsha maji ya bahari na kupoza mvuke ili kupata maji safi ya kunywa yasiyo na chumvi (Simple Distillation)!",
                "analogy_en": "At coastal marine desalination facilities, thermal distillation vaporizes seawater and condenses steam into pure distilled drinking water!"
            },
            "highlands": {
                "analogy_sw": "Mashambani kule Mwea, wakulima hutenganisha makapi ya mpunga na punje za mchele kwa kupepeta upeponi (Winnowing) kwa kutumia tofauti ya uzito!",
                "analogy_en": "In highland Mwea rice plains, winnowing in afternoon breezes separates lightweight chaff from dense paddy rice grains effortlessly!"
            },
            "arid": {
                "analogy_sw": "Kwenye visima vya mchanga vya kaskazini, wakazi huchimba mchanga wa mto ili maji yaliyochujwa kiasili na tabaka la mchanga yakusanywe safi!",
                "analogy_en": "In arid seasonal riverbeds (lagas), natural subsurface sand aquifers filter turbid floodwaters into crystal-clear groundwater!"
            },
            "urban": {
                "analogy_sw": "Mtaani, kiwanda cha kusafisha mafuta (Oil Refinery) kule Changamwe hutumia Fractional Distillation kutenganisha petroli, diseli, na gesi ya mtungi kutoka kwenye mafuta ghafi!",
                "analogy_en": "At industrial oil refineries, fractional distillation columns separate crude petroleum into petrol, diesel, and paraffin based on boiling points!"
            }
        },
        "key_terms": [
            {"en": "Filtration", "sw": "Kuchuja (Kutenganisha vitu visivyoyeyuka kama mchanga)"},
            {"en": "Evaporation & Crystallization", "sw": "Kuvukiza na Kufanya Fuwele (Kupata chumvi)"},
            {"en": "Simple Distillation", "sw": "Kunereka Rahisi (Kupata maji safi kutoka maji ya chumvi)"},
            {"en": "Fractional Distillation", "sw": "Kunereka kwa Sehemu (Kutenganisha petroli na diseli)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kutenganisha Mchanganyiko wa Chumvi na Mchanga",
            "title_en": "Experiment: Separating a Sand and Salt Mixture",
            "materials_sw": "Kijiko cha mchanga, kijiko cha chumvi, glasi ya maji, kitambaa cha kuchujia, sufuria ndogo ya kuchemsha.",
            "materials_en": "Teaspoon of sand, teaspoon of salt, glass of water, filter cloth, heating pot.",
            "steps_sw": "1. Weka chumvi na mchanga kwenye maji na ukoroge—chumvi itayeyuka lakini mchanga hautayeyuka.\n2. Chuja mchanganyiko kwa kitambaa—mchanga utabaki kwenye kitambaa (Filtration).\n3. Chemsha maji yaliyochujwa hadi yakauke—fuwele nyeupe za chumvi zitabaki kwenye sufuria (Evaporation)!",
            "steps_en": "1. Dissolve salt and sand mixture in water—salt dissolves while sand remains insoluble.\n2. Filter through cloth to collect sand residue.\n3. Boil the filtered saltwater to dryness—pure white salt crystals remain!"
        },
        "quiz": {
            "question_sw": "Ni njia gani inayofaa zaidi kutenganisha mchanga usioyeyuka kutoka kwenye maji machafu ya mto?",
            "question_en": "Which separation method is best suited to separate insoluble sand from murky river water?",
            "options_sw": ["A) Kuchuja (Filtration)", "B) Sumaku", "C) Kupiga kelele", "D) Kuongeza sukari"],
            "options_en": ["A) Filtration", "B) Magnetism", "C) Shouting", "D) Adding sugar"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Kuchuja (Filtration) hutenganisha vitu vigumu visivyoyeyuka kama mchanga kwa kutumia karatasi ya chujio au kitambaa safi.",
            "explanation_en": "Brilliant! Filtration is the physical technique for separating insoluble solid suspensions from liquids."
        }
    },
    {
        "id": "periodic_table_atoms",
        "title_en": "Atoms, Elements & The Periodic Table",
        "title_sw": "Atomu, Elementi na Jedwali la Periodiki",
        "subject": "Chemistry",
        "cbc_strand": "Mixtures, Elements & Compounds (Grade 8/9 Integrated Science)",
        "summary_en": "An atom is the smallest particle of an element, consisting of protons (+), neutrons (0) in the central nucleus, and orbiting electrons (-). The Periodic Table organizes 118 elements by atomic number.",
        "summary_sw": "Atomu ni chembe ndogo kabisa ya elementi inayoundwa na protoni (+), nutroni (0) ndani ya kiini, na elektroni (-) zinazozunguka nje. Jedwali la Periodiki hupanga elementi 118 kulingana na nambari ya atomiki.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria mfumo wa jua: Jua la katikati ni Kiini cha Atomu (Nucleus) chenye Protoni (+) na Nutroni. Sayari zinazozunguka jua angani ni Elektroni zenye chaji hasi (-) zinazozunguka kwa kasi kubwa kwenye mizingo yake!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Atomu: Kiini Katikati chenye Protoni na Nutroni] ➔ [Elektroni zinazozunguka nje] ➔ [Jedwali la Periodiki lenye Alama: H, C, O, Fe, Cu].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria, kila tone la maji (H₂O) limeundwa na atomu 2 za Haidrojeni zilizoshikana na atomu 1 ya Oksijeni!",
                "analogy_en": "In every drop of Lake Victoria water, billions of water molecules (H₂O) unite two Hydrogen atoms bonded to one Oxygen atom!"
            },
            "coastal": {
                "analogy_sw": "Pwani, chumvi ya mezani (NaCl) imeundwa na atomu ya Metali ya Sodiamu (Na) iliyoungana na gesi ya Klorini (Cl) kutengeneza fuwele tamu za chumvi!",
                "analogy_en": "At coastal salt fields, crystalline table salt (NaCl) is formed by combining reactive Sodium metal (Na) and Chlorine gas (Cl)!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, mbolea ya NPK inayowekwa kwenye mashamba ya mahindi ina elementi 3 muhimu za jedwali la periodiki: Nitrojeni (N), Fosfasi (P), na Potasiamu (K)!",
                "analogy_en": "In highland farms, NPK fertilizers supply three essential chemical elements: Nitrogen (N), Phosphorus (P), and Potassium (K)!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo yenye madini ya shaba (Copper - Cu) na dhahabu (Gold - Au), kila kipande cha dhahabu safi kimeundwa na atomu za dhahabu pekee zisizopata kutu!",
                "analogy_en": "In mineral mining zones, pure gold nuggets (Au) consist entirely of dense gold atoms that never oxidize or corrode!"
            },
            "urban": {
                "analogy_sw": "Mtaani, waya za umeme zimeundwa na elementi ya Shaba (Copper - Cu) yenye elektroni zilizo huru kutembea na kusafirisha mkondo wa umeme!",
                "analogy_en": "In urban building wires, Copper element atoms (Cu) feature mobile outer valence electrons that conduct electric current effortlessly!"
            }
        },
        "key_terms": [
            {"en": "Atom (Protons, Neutrons, Electrons)", "sw": "Atomu (Protoni +, Nutroni 0, Elektroni -)"},
            {"en": "Atomic Number (Z)", "sw": "Nambari ya Atomiki (Idadi ya protoni kwenye kiini)"},
            {"en": "Chemical Elements (118)", "sw": "Elementi za Kikemia (Hawezi kuvunjwa zaidi)"},
            {"en": "Periodic Table Groups & Periods", "sw": "Safu na Mistari ya Jedwali la Periodiki"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kujenga Mfano wa Atomu kwa Kutumia Vifuniko vya Chupa",
            "title_en": "Experiment: Bottle Cap Subatomic Particle Model",
            "materials_sw": "Vifuniko vyekundu 6 (protoni), vifuniko vya bluu 6 (nutroni), vifuniko vidogo vya njano 6 (elektroni), karatasi kubwa.",
            "materials_en": "6 red bottle caps (protons), 6 blue caps (neutrons), 6 small yellow caps (electrons), large paper.",
            "steps_sw": "1. Weka vifuniko vyekundu 6 na vya bluu 6 katikati ya karatasi (Kiini cha Kaboni / Carbon Nucleus).\n2. Chora duara la kwanza kuzunguka kiini na uweke elektroni 2.\n3. Chora duara la pili na uweke elektroni 4.\n4. Hongera! Umejenga atomu kamili ya Kaboni (Carbon - C)!",
            "steps_en": "1. Cluster 6 red caps and 6 blue caps in the center (Carbon nucleus).\n2. Draw the first orbital ring and place 2 yellow electron caps.\n3. Draw outer valence ring and place 4 electron caps.\n4. You have modeled a complete Carbon-12 atom!"
        },
        "quiz": {
            "question_sw": "Ni chembe gani ndogo iliyo ndani ya kiini cha atomu (nucleus) yenye chaji chanya ya umeme (+)?",
            "question_en": "Which subatomic particle located in the nucleus carries a positive electric charge (+)?",
            "options_sw": ["A) Protoni (Proton)", "B) Elektroni (-)", "C) Nutroni (0)", "D) Mchanga"],
            "options_en": ["A) Proton", "B) Electron", "C) Neutron", "D) Sand"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Protoni zina chaji chanya (+), elektroni zina chaji hasi (-), na nutroni hazina chaji (0).",
            "explanation_en": "Spot on! Protons possess a positive (+1) charge, electrons carry negative (-1), and neutrons are neutral (0)."
        }
    },
    {
        "id": "water_purification_hardness",
        "title_en": "Water Treatment, Purification & Hardness",
        "title_sw": "Utakaso wa Maji, Usafishaji na Ugumu wa Maji (Water Hardness)",
        "subject": "Chemistry",
        "cbc_strand": "Water, Sanitation & Hygiene (Grade 7/8 Integrated Science)",
        "summary_en": "Natural water contains dissolved salts (calcium & magnesium causing hardness) and suspended microorganisms. Water purification combines sedimentation, filtration, chemical disinfection (chlorination), and boiling to make water potable.",
        "summary_sw": "Maji ya asili yana chumvi zilizoyeyuka (kalsiamu na magnesiamu zinazosababisha maji magumu/hard water) na vijidudu. Utakaso unajumuisha kutuliza, kuchuja, kuweka klorini/WaterGuard, na kuchemsha.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Jaribu kutengeneza povu la sabuni kwenye maji ya mvua (maji laini / Soft Water)—povu litatokea jingi mara moja. Sasa jaribu kwenye maji ya kisima cha chokaa (Maji Magumu / Hard Water)—sabuni haitatoa povu bali itatengeneza mabonge ya ukoko (scum)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Maji Machafu ya Mto] ➔ [Kuweka Dawa ya WaterGuard / Kuchemsha] ➔ [Kuchuja kwa Mchanga] ➔ [Maji Safi na Salama ya Kunywa].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu kando ya Ziwa Victoria, familia hutumia WaterGuard au chujio za kauri (Ceramic Pot Filters) kutibu maji ya ziwa ili kuua bakteria wa Kipindupindu na kuzuia magonjwa!",
                "analogy_en": "In Lake Victoria riparian communities, families treat lake water with WaterGuard chlorine drops and ceramic pot filters to eliminate cholera pathogens!"
            },
            "coastal": {
                "analogy_sw": "Pwani kule Mombasa, maji ya visima vingi ni 'Maji Magumu' (Hard Water) yenye madini ya chokaa na chumvi yanayoganda kwenye kuta za aaaa za kuchemshia maji (Kettle scale)!",
                "analogy_en": "In coastal boreholes, dissolved calcium and magnesium hydrogencarbonates make water hard, precipitating chalky limescale inside electric kettles!"
            },
            "highlands": {
                "analogy_sw": "Mashambani kule Nyeri, maji ya mito safi yanayotoka misitu ya Aberdare ni 'Maji Laini' (Soft Water) yanayotoa povu jingi la sabuni haraka sana!",
                "analogy_en": "In highland Aberdare mountain streams, pristine runoff contains minimal mineral salts, functioning as ideal soft water that lathers instantly!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame ya Turkana, visima vya maji ya chini ya ardhi hutumia chujio za jua (Solar Water Stills) kuondoa chumvi kali na kutoa maji baridi ya kunywa!",
                "analogy_en": "In arid northern settlements, simple solar water distillation stills desalinate brackish well water into potable drinking water!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mtambo wa kusafisha maji wa Sasumua na Ndakaini unasafisha mamilioni ya lita za maji kwa kuongeza 'Alum' (kugandisha tope), kuchuja mchanga na kuweka klorini!",
                "analogy_en": "In Nairobi's municipal supply system, water treatment adds alum coagulants to aggregate suspended clay before sand filtration and final chlorination!"
            }
        },
        "key_terms": [
            {"en": "Potable Water", "sw": "Maji Safi na Salama ya Kunywa"},
            {"en": "Hard Water vs Soft Water", "sw": "Maji Magumu (Hayatoi povu) vs Maji Laini"},
            {"en": "Chlorination (WaterGuard)", "sw": "Kuweka Klorini (Kuua vijidudu vya magonjwa)"},
            {"en": "Limescale (Scum)", "sw": "Ukoko wa Chokaa (Kwenye aaaa au sufuria)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kupima Maji Magumu dhidi ya Maji Laini kwa Sabuni",
            "title_en": "Experiment: Soap Lather Hard vs Soft Water Lather Test",
            "materials_sw": "Maji ya mvua (maji laini), maji yenye chumvi/chokaa (maji magumu), kipande cha sabuni ya kuogea, chupa mbili ndogo safi.",
            "materials_en": "Rainwater (soft water), well/chalk water (hard water), soap shavings, two small plastic bottles.",
            "steps_sw": "1. Weka maji ya mvua kwenye chupa A na maji ya kisima kwenye chupa B.\n2. Weka tone moja la sabuni kwenye kila chupa.\n3. Tikisa chupa zote mbili mara 10: Chupa A itajaa povu jeupe tele; Chupa B itabaki na ukungu bila povu!",
            "steps_en": "1. Add rainwater to bottle A and well water to bottle B.\n2. Add equal soap shavings to each.\n3. Shake both bottles 10 times: Bottle A forms thick fluffy lather; Bottle B leaves cloudy curd scum with minimal lather!"
        },
        "quiz": {
            "question_sw": "Ni njia gani rahisi na ya uhakika nyumbani ya kuua vijidudu na bakteria wote waliomo kwenye maji ya kunywa?",
            "question_en": "What is the simplest and most reliable household method to destroy all bacteria and pathogens in drinking water?",
            "options_sw": ["A) Kuchemsha maji vizuri hadi yabubujike", "B) Kuweka sukari", "C) Kupuliza upepo", "D) Kuweka rangi"],
            "options_en": ["A) Boiling water vigorously", "B) Adding sugar", "C) Blowing air", "D) Adding color"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Kuchemsha maji kwa joto la 100°C huua vijidudu, virusi na bakteria wote wa magonjwa kama Kipindupindu na Typhoid.",
            "explanation_en": "Spot on! Bringing water to a rolling boil at 100°C thermally destroys all pathogenic bacteria, amoeba, and viruses."
        }
    },
    {
        "id": "air_gases_pollution",
        "title_en": "Air Composition, Atmospheric Gases & Pollution",
        "title_sw": "Muundo wa Hewa ya Anga, Gesi Muhimu na Uchafuzi wa Mazingira",
        "subject": "Chemistry",
        "cbc_strand": "Mixtures, Elements & Environment (Grade 6/7 Integrated Science)",
        "summary_en": "Air is a homogeneous mixture of gases: Nitrogen (78%), Oxygen (21%), Argon (0.9%), Carbon Dioxide (0.04%), and variable water vapor. Air pollution from combustion and industrial emissions poses health and climate risks.",
        "summary_sw": "Hewa ni mchanganyiko wa gesi: Nitrojeni (78%), Oksijeni (21%), Gesi adimu kama Argon (0.9%), na Kaboni Dioksidi (0.04%). Moshi wa magari na viwanda huchafua hewa na kuleta ongezeko la joto duniani.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Punga kiganja chako haraka mbele ya uso wako. Utahisi upepo laini ukipiga ngozi yako—huo ni mchanganyiko wa gesi ya Nitrojeni (sehemu kubwa) na Oksijeni safi unayoivuta mapafuni kila sekunde!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Chati ya Mviringo ya Hewa: Nitrojeni 78%, Oksijeni 21%, Gesi zingine 1%] ➔ [Kupuliza Mshumaa na Kuona Unazima Chini ya Glasi].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria wakati wa dhoruba asubuhi, upepo safi wa ziwa unaleta hewa iliyojaa oksijeni safi inayotengenezwa na mimea ya ukanda wa ziwa!",
                "analogy_en": "Across Lake Victoria, clean equatorial breezes circulate fresh oxygen produced by lush riparian vegetation!"
            },
            "coastal": {
                "analogy_sw": "Pwani kule Diani na Malindi, mikoko na upepo wa Bahari Hindi husafisha hewa ya mijini na kuifanya kuwa hewa safi na yenye chumvi ya asili!",
                "analogy_en": "Along coastal shorelines, mangrove forests act as immense carbon sinks, absorbing emissions and oxygenating ocean breezes!"
            },
            "highlands": {
                "analogy_sw": "Milimani kwenye misitu ya Aberdare na Mau, miti mikubwa inafyonza mamilioni ya tani za kaboni dioksidi kutoka hewani na kuzuia mabadiliko ya tabianchi!",
                "analogy_en": "In highland Mau and Aberdare water towers, indigenous forests trap carbon dioxide emissions, regulating regional microclimates!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame ya kaskazini, dhoruba za vumbi (dust devils) hutokea pale hewa ya ardhini inapopashwa joto kali na kupaa juu kwa kasi!",
                "analogy_en": "In arid savanna plains, intense solar ground heating creates rapid convective updrafts forming swirling dust devils!"
            },
            "urban": {
                "analogy_sw": "Mtaani, msongamano wa magari hutoa moshi wa kaboni monoksaidi na chembe za vumbi (PM2.5) ndio maana kupanda miti shuleni ni muhimu sana!",
                "analogy_en": "In urban traffic corridors, vehicular exhaust releases carbon monoxide and particulates, highlighting the vital necessity of urban greening belts!"
            }
        },
        "key_terms": [
            {"en": "Air Composition (Nitrogen 78%, Oxygen 21%)", "sw": "Muundo wa Hewa (Nitrojeni 78%, Oksijeni 21%)"},
            {"en": "Carbon Dioxide (0.04%)", "sw": "Kaboni Dioksidi (Hutumiwa na mimea kutengeneza chakula)"},
            {"en": "Air Pollutants (CO, SO₂, Particulates)", "sw": "Vichafuzi vya Hewa (Moshi, Vumbi, Gesi za Viwanda)"},
            {"en": "Greenhouse Effect", "sw": "Athari ya Greenhouse na Mabadiliko ya Tabianchi"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuthibitisha Oksijeni Inachukua Asilimia 20% ya Hewa",
            "title_en": "Experiment: Burning Candle Water Rise Oxygen Consumption Test",
            "materials_sw": "Mshumaa mdogo uliowashwa kwenye sahani ya maji yenye rangi, glasi iliyo wazi.",
            "materials_en": "Small candle mounted in colored water plate, clear glass.",
            "steps_sw": "1. Washa mshumaa ndani ya sahani yenye maji yenye rangi.\n2. Funika mshumaa kwa glasi iliyo wazi.\n3. Mshumaa utazima baada ya sekunde chache na maji yatapanda juu ndani ya glasi kwa takriban 1/5 (20%)—oksijeni yote imetumika kuchoma!",
            "steps_en": "1. Light a candle sitting in a shallow dish of colored water.\n2. Invert a clear glass over the candle.\n3. The flame extinguishes and water rises ~20% up the glass as oxygen is consumed in combustion!"
        },
        "quiz": {
            "question_sw": "Ni gesi gani inayochukua sehemu kubwa zaidi (asilimia 78%) ya hewa tunayoivuta kwenye anga ya dunia?",
            "question_en": "Which gas comprises the largest proportion (approximately 78%) of Earth's atmosphere?",
            "options_sw": ["A) Nitrojeni (Nitrogen - 78%)", "B) Oksijeni (21%)", "C) Moshi", "D) Hydrojeni"],
            "options_en": ["A) Nitrogen (78%)", "B) Oxygen (21%)", "C) Smoke", "D) Hydrogen"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Gesi ya Nitrojeni ndiyo gesi tele zaidi hewani (78%), ikifuatiwa na Oksijeni (21%).",
            "explanation_en": "Brilliant! Nitrogen gas makes up approximately 78% of ambient air, while oxygen accounts for ~21%."
        }
    },
    {
        "id": "metals_reactivity_series",
        "title_en": "Metals, Non-Metals & Reactivity Series",
        "title_sw": "Metali, Zisizo Metali na Mfuatano wa Mmenyuko wa Kikemia",
        "subject": "Chemistry",
        "cbc_strand": "Mixtures, Elements & Compounds (Grade 8/9 Integrated Science)",
        "summary_en": "Metals are shiny, malleable, ductile electrical conductors. The Reactivity Series ranks metals from most reactive (Potassium, Sodium) to least reactive (Gold, Platinum) in reactions with air, water, and acids.",
        "summary_sw": "Metali hung'aa, hupitisha umeme na joto, na huweza kupigwa kuwa mabati. Mfuatano wa Mmenyuko (Reactivity Series) hupanga metali kuanzia zenye mmenyuko mkali zaidi (Potasiamu, Sodiamu) hadi hafifu (Dhahabu).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika msumari wa chuma (Metali). Unahisi ubaridi, uzito na ugumu. Sasa shika kipande cha kaa la moto/mkaa (Kaboni - Si Metali). Mkaa ni mwepesi na ukiponda unavunjika kuwa unga mara moja (Brittle)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Msumari wa Chuma unang'aa na kupitisha Umeme] vs [Kaa la Mkaa linavunjika vipande] ➔ [Jedwali la Mfuatano wa Metali kuanzia Potasiamu hadi Dhahabu].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu, mabati ya nyumba za bati yaliyotengenezwa kwa chuma kilichopakwa zinki (Galvanized Iron) hayashiki kutu kwa sababu zinki inalinda chuma kisigusane na hewa na maji!",
                "analogy_en": "In lake basin home construction, galvanized corrugated iron sheets resist rusting because a sacrificial zinc layer shields the underlying steel!"
            },
            "coastal": {
                "analogy_sw": "Pwani kule Mombasa ambapo kuna unyevu na chumvi ya bahari, vyuma hushika kutu (Rusting / Iron Oxidation) kwa kasi ya ajabu, ndio maana meli hupakwa rangi maalum za kuzuia kutu!",
                "analogy_en": "At coastal marine ports, salt spray accelerates electrochemical rusting of iron hulls, requiring protective sacrificial zinc anodes!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, majembe na mapanga yaliyotengenezwa kwa chuma cha pua (Steel - Iron & Carbon alloy) ni imara na yenye makali ya kukatia mashambani!",
                "analogy_en": "In highland agriculture, steel farming hoes and pangas combine iron with carbon to create high-tensile cutting strength!"
            },
            "arid": {
                "analogy_sw": "Kwenye migodi ya dhahabu kule Migori na Turkana, dhahabu hupatikana ikiwa safi kabisa ardhini bila kutu kwa sababu iko chini kabisa mwa mfuatano wa mmenyuko!",
                "analogy_en": "In artisanal gold mining pits, gold occurs in native unreacted metallic state because it lies at the bottom of the chemical reactivity series!"
            },
            "urban": {
                "analogy_sw": "Mtaani, madirisha na milango ya kisasa hutengenezwa kwa Alumini (Aluminium) kwa sababu ni nyepesi na haipati kutu hata wakati wa mvua!",
                "analogy_en": "In modern city buildings, architectural window frames use lightweight aluminum alloys protected by an impermeable natural oxide layer!"
            }
        },
        "key_terms": [
            {"en": "Reactivity Series (K, Na, Ca, Mg, Al, Zn, Fe, Cu, Ag, Au)", "sw": "Mfuatano wa Mmenyuko wa Metali"},
            {"en": "Rusting / Corrosion", "sw": "Kutu (Chuma + Oksijeni + Maji ➔ Kutu ya Chuma)"},
            {"en": "Galvanization", "sw": "Kupaka Zinki Kuzuia Kutu (Galvanization)"},
            {"en": "Alloys (Steel, Brass, Bronze)", "sw": "Aloi (Mchanganyiko wa metali mbili au zaidi)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Masharti ya Lazima ya Kutengeneza Kutu kwenye Misumari",
            "title_en": "Experiment: Iron Nail Rusting Conditions Test (Air + Water)",
            "materials_sw": "Misumari 3 ya chuma safi, chupa ndogo 3: Chupa A (maji + hewa), Chupa B (maji yaliyochemshwa + mafuta juu bila hewa), Chupa C (hewa kavu na pamba).",
            "materials_en": "3 clean iron nails, 3 small jars: Jar A (water + air), Jar B (boiled water + oil layer, no air), Jar C (dry air with cotton).",
            "steps_sw": "1. Weka msumari mmoja kwenye kila chupa kwa siku 3.\n2. Msumari wa Chupa A pekee ndio utakaoshika kutu ya machungwa.\n3. Hii inathibitisha kuwa kutu inahitaji Maji na Oksijeni ya hewa kwa pamoja!",
            "steps_en": "1. Place one nail in each jar for 3 days.\n2. Observe only nail A develops reddish rust.\n3. Concludes iron rusting strictly requires both water and oxygen simultaneously!"
        },
        "quiz": {
            "question_sw": "Ni vitu gani viwili vya lazima vinavyohitajika kwa pamoja ili chuma kishike kutu (rusting)?",
            "question_en": "Which two substances must be present together for iron metal to rust?",
            "options_sw": ["A) Maji (Unyevu) na Hewa ya Oksijeni", "B) Mchanga na mafuta", "C) Jua na mwezi", "D) Chumvi pekee"],
            "options_en": ["A) Water (Moisture) and Oxygen Gas", "B) Sand and oil", "C) Sun and moon", "D) Salt only"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Chuma hushika kutu pale kinapogusana na maji (unyevu) pamoja na hewa ya oksijeni kwa wakati mmoja.",
            "explanation_en": "Spot on! Chemical rusting is the oxidation of iron requiring both moisture and atmospheric oxygen."
        }
    },
    {
        "id": "chemical_bonding_compounds",
        "title_en": "Chemical Bonding: Ionic & Covalent Compounds",
        "title_sw": "Muungano wa Kikemia: Michanganyiko ya Ioni (Ionic) na Kovalent (Covalent)",
        "subject": "Chemistry",
        "cbc_strand": "Mixtures, Elements & Compounds (Grade 8/9 Integrated Science)",
        "summary_en": "Chemical bonds hold atoms together to achieve stable octet electron configurations: Ionic bonding transfers valence electrons between metals and non-metals, while Covalent bonding shares electron pairs between non-metals.",
        "summary_sw": "Muungano wa kikemia hushikilia atomu pamoja ili kufikia utulivu wa kielektroni: Muungano wa Ioni (Ionic) huhamisha elektroni kati ya metali na zisizo metali, wakati Muungano wa Kovalent (Covalent) hushiriki jozi za elektroni.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika chembe za chumvi ya mezani (Ionic compound). Fuwele zake ni ngumu na zimeshikana kwa nguvu kubwa ya chaji za umeme (+ na -). Kisha shika tone la maji au mafuta (Covalent compound) ambapo atomu zinashiriki elektroni kwa usawa!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Metali inatoa Elektroni (+) ➔ Isiyo Metali inapokea (-) / Ionic Bond] vs [Atomu mbili zinazoshiriki Elektroni pamoja / Covalent Bond].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria, molekuli ya maji (H₂O) imeundwa na muungano wa Kovalent (Covalent Bond) ambapo atomu ya Oksijeni inashiriki elektroni zake na atomu mbili za Haidrojeni!",
                "analogy_en": "In Lake Victoria water molecules, Oxygen shares electron pairs with two Hydrogen atoms via strong polar covalent bonds!"
            },
            "coastal": {
                "analogy_sw": "Pwani, fuwele za chumvi ya Bahari Hindi (NaCl) zimeundwa na muungano imara wa Ioni (Ionic Bond) kati ya Ioni Chanya ya Sodiamu (Na⁺) na Ioni Hasi ya Kloridi (Cl⁻)!",
                "analogy_en": "In coastal sea salt crystals, electrostatic ionic bonds link positive sodium cations (Na⁺) and negative chloride anions (Cl⁻) in a cubic lattice!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, sukari inayotokana na miwa ya Mumias na Nzoia (C₁₂H₂₂O₁₁) imeundwa na mamilioni ya miungano ya Kovalent ya kaboni, haidrojeni na oksijeni!",
                "analogy_en": "In Mumias sugar cane processing, table sucrose sugar molecules (C₁₂H₂₂O₁₁) are held by intricate covalent carbon-hydrogen-oxygen bonds!"
            },
            "arid": {
                "analogy_sw": "Kwenye mawe ya chokaa ya jangwani (Calcium Carbonate - CaCO₃), miungano ya ioni inashikilia kalsiamu na kaboneti kutengeneza miamba imara ya ujenzi!",
                "analogy_en": "In arid limestone quarries, ionic bonds between calcium ions and carbonate polyatomic ions build durable building stones!"
            },
            "urban": {
                "analogy_sw": "Mtaani, plastiki za mifuko na mabomba ya PVC yameundwa na minyororo mirefu ya polima yenye miungano thabiti ya Kovalent inayodumu kwa miaka mingi!",
                "analogy_en": "In modern city infrastructure, PVC water pipes and polymer containers rely on robust covalent carbon-backbone chains!"
            }
        },
        "key_terms": [
            {"en": "Ionic Bonding (Electron Transfer)", "sw": "Muungano wa Ioni (Kutoa na Kupokea Elektroni)"},
            {"en": "Covalent Bonding (Electron Sharing)", "sw": "Muungano wa Kovalent (Kushirikiana Elektroni)"},
            {"en": "Valence Electrons & Octet Rule", "sw": "Elektroni za Nje na Kanuni ya Utulivu (Octet)"},
            {"en": "Molecules & Giant Lattices", "sw": "Molekuli na Miundo ya Fuwele Imara"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kupima Upitishaji wa Umeme kwenye Maji ya Chumvi (Ionic) dhidi ya Maji ya Sukari (Covalent)",
            "title_en": "Experiment: Electrical Conductivity of Salt vs Sugar Water",
            "materials_sw": "Betri ya 1.5V, balbu ndogo, waya mbili, glasi ya maji yenye chumvi (Ionic), glasi ya maji yenye sukari (Covalent).",
            "materials_en": "1.5V battery, small bulb, two bare wire probes, saltwater solution, sugar water solution.",
            "steps_sw": "1. Dumbukiza ncha za waya kwenye maji ya chumvi—balbu itawaka mara moja (Ioni huru zinapitisha umeme)!\n2. Dumbukiza ncha za waya kwenye maji ya sukari—balbu haitawaka (Molekuli za kovalent hazina chaji huru)!",
            "steps_en": "1. Insert wire probes into saltwater—the bulb illuminates brightly as mobile ions conduct current!\n2. Insert into sugar water—the bulb remains dark, proving neutral covalent molecules do not conduct electricity!"
        },
        "quiz": {
            "question_sw": "Ni aina gani ya muungano wa kikemia unaotokea pale atomu ya metali inapotoa elektroni kwa atomu isiyo metali (mfano: Na + Cl ➔ NaCl)?",
            "question_en": "Which type of chemical bond forms when a metal transfers electrons to a non-metal atom?",
            "options_sw": ["A) Muungano wa Ioni (Ionic Bond)", "B) Muungano wa Kovalent", "C) Gundi", "D) Kamba"],
            "options_en": ["A) Ionic Bond", "B) Covalent Bond", "C) Glue", "D) String"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Muungano wa Ioni (Ionic Bond) huundwa pale metali inapotoa elektroni na kuwa ioni chanya (+), huku isiyo metali ikipokea na kuwa ioni hasi (-).",
            "explanation_en": "Spot on! Ionic bonds form through complete electron transfer from metal to non-metal, creating electrostatic attraction between ions."
        }
    },
    {
        "id": "carbon_fuels_combustion",
        "title_en": "Carbon, Fuels & Combustion Reactions",
        "title_sw": "Kaboni, Nishati ya Mafuta na Mmenyuko wa Kuungua (Combustion)",
        "subject": "Chemistry",
        "cbc_strand": "Energy & Chemical Reactions (Grade 8/9 Integrated Science)",
        "summary_en": "Carbon forms versatile organic compounds (hydrocarbons). Combustion is an exothermic chemical reaction where fuels (wood, charcoal, LPG, biogas) react with oxygen to release heat, light, carbon dioxide, and water.",
        "summary_sw": "Kaboni huunda misombo mingi ya asili. Kuungua (Combustion) ni mmenyuko wa kikemia ambapo nishati (kuni, mkaa, gesi ya mtungi, biogasi) hugusana na oksijeni kutoa joto kali, mwanga, kaboni dioksidi na maji.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika kipande cha mkaa wa kupikia mkononi mwako. Mkaa ni kaboni safi karibu asilimia 90. Unapowashwa jikoni kwa moto na kupewa hewa ya oksijeni, unaanza kuwaka kwa joto kali linalopika chakula—huo ndio Mmenyuko wa Kuungua (Combustion)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Nishati ya Kuni/Gesi + Oksijeni] ➔ [Mwako wa Moto & Joto Kali] ➔ [Moshi wa Kaboni Dioksidi & Maji].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule mashambani Kisumu na Siaya, wakulima hutumia mtambo wa Biogasi (Biogas Digester) unaovundisha samadi ya ng'ombe na kutoa gesi ya Methane (CH₄) safi ya kupikia bila moshi!",
                "analogy_en": "In lake rural homesteads, household biogas digesters ferment livestock manure into clean burning methane gas (CH₄) for smoke-free cooking!"
            },
            "coastal": {
                "analogy_sw": "Pwani, mabaki ya vifuu vya nazi (coconut shells) hutumiwa kutengeneza mkaa mweupe wa 'Briquettes' unaowaka kwa muda mrefu bila moshi na kulinda misitu!",
                "analogy_en": "At coastal artisanal workshops, coconut shell biomass briquettes burn with high calorific efficiency while conserving mangrove forests!"
            },
            "highlands": {
                "analogy_sw": "Mashambani kule Kericho, viwanda vya majani ya chai hutumia mabaki ya miti iliyopandwa (biomass boilers) kuzalisha mvuke wa joto kali unaokausha majani ya chai!",
                "analogy_en": "In highland tea estates, sustainable biomass boilers combust wood chips efficiently to generate steam for tea drying ovens!"
            },
            "arid": {
                "analogy_sw": "Kwenye jua kali la Garissa, kukausha kuni na majani makavu huhakikisha mwako kamili (Complete Combustion) wenye moto wa bluu na joto kali bila kutoa moshi mweusi!",
                "analogy_en": "In dry arid climates, fully seasoned dry wood enables complete combustion with minimal soot and carbon monoxide formation!"
            },
            "urban": {
                "analogy_sw": "Mtaani, jiko la gesi ya mtungi (LPG - Liquefied Petroleum Gas) linawaka na moto safi wa bluu kwa sababu gesi inachanganyika vizuri na oksijeni ya hewa!",
                "analogy_en": "In urban households, LPG gas cookers produce a clean blue flame indicating complete hydrocarbon combustion into CO₂ and water!"
            }
        },
        "key_terms": [
            {"en": "Complete Combustion (Blue Flame)", "sw": "Mwako Kamili (Moto wa bluu: Mafuta + O₂ ➔ CO₂ + H₂O + Joto)"},
            {"en": "Incomplete Combustion (Yellow Flame & Soot)", "sw": "Mwako Usiokamilika (Moto wa njano wenye masizi na CO)"},
            {"en": "Hydrocarbons (Methane, Propane, Butane)", "sw": "Haidrokaboni (Gesi za kupikia zenye C na H)"},
            {"en": "Carbon Monoxide (CO Hazard)", "sw": "Gesi ya Sumu ya Kaboni Monoksaidi (Haina harufu)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Tofauti ya Mwako Kamili na Mwako Usiokamilika kwa Mshumaa",
            "title_en": "Experiment: Candle Soot Incomplete Combustion Plate Test",
            "materials_sw": "Mshumaa uliowashwa, sahani ya bati au kioo kisafi, kishikio.",
            "materials_en": "Lit candle, metal spoon or clean glass plate, tongs.",
            "steps_sw": "1. Washa mshumaa wenye mwali wa njano.\n2. Shikilia sehemu ya chini ya sahani juu ya moto wa njano kwa sekunde 10.\n3. Sahani itapata doa jeusi la masizi ya kaboni (Soot)—kuthibitisha mwako usiokamilika hutoa chembe za kaboni safi!",
            "steps_en": "1. Light a candle burning with a yellow luminous flame.\n2. Hold a cold metal spoon directly in the yellow flame for 10 seconds.\n3. Observe black carbon soot deposit on the metal, proving incomplete combustion releases unburnt carbon particles!"
        },
        "quiz": {
            "question_sw": "Ni aina gani ya mwako wa gesi unaotoa moto safi wa bluu na joto kali bila kutoa moshi mweusi wala masizi?",
            "question_en": "Which type of combustion produces a clean blue flame with maximum heat and no black soot?",
            "options_sw": ["A) Mwako Kamili (Complete Combustion)", "B) Mwako Usiokamilika", "C) Kuzima moto", "D) Moshi tu"],
            "options_en": ["A) Complete Combustion", "B) Incomplete Combustion", "C) Smothering", "D) Smoke only"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Mwako kamili (Complete combustion) hutokea pale oksijeni inapotosha kabisa, ikitoa moto wa bluu na joto jingi bila masizi.",
            "explanation_en": "Spot on! Complete combustion occurs with excess oxygen, producing clean carbon dioxide, water vapor, and high thermal energy."
        }
    },
    {
        "id": "chemical_solutions_solubility",
        "title_en": "Solutions, Solutes & Saturated Solubility",
        "title_sw": "Myeyusho (Solutions), Kiyeyushwa (Solute), Kiyeyushaji (Solvent) na Kiwango cha Kuyeyuka (Solubility)",
        "subject": "Chemistry",
        "cbc_strand": "Mixtures, Elements & Compounds (Grade 7/8 Integrated Science)",
        "summary_en": "A solution is a homogeneous mixture formed when a solute dissolves in a solvent (Solution = Solute + Solvent). A saturated solution holds the maximum possible solute at a given temperature.",
        "summary_sw": "Myeyusho ni mchanganyiko sawa unaoundwa wakati kiyeyushwa (mf. sukari) kinapoyeyuka ndani ya kiyeyushaji (mf. maji). Myeyusho uliojaa (Saturated) hauwezi kuyeyusha sukari zaidi bila kuongeza joto.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Weka kijiko cha sukari kwenye glasi ya maji na ukoroge. Chembe ngumu za sukari zitatoweka machoni na mikononi kwa sababu zimeyeyuka sawia ndani ya maji (Myeyusho / Solution). Maji yote yatakuwa matamu sawasawa!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kijiko cha Sukari / Solute] + [Glasi ya Maji / Solvent] ➔ [Kukoroga = Myeyusho Safi / Solution] ➔ [Myeyusho Uliojaa / Saturated Solution].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu unapotengeneza chai tamu ya asubuhi, maji ya moto ya ziwa ndiyo Kiyeyushaji (Solvent), sukari na majani ya chai ni Viyeyushwa (Solutes), na kikombe chote cha chai ni Myeyusho (Solution)!",
                "analogy_en": "In morning tea preparation, hot water serves as the universal solvent, sugar crystals act as the solute, and sweet tea is the resulting homogeneous solution!"
            },
            "coastal": {
                "analogy_sw": "Pwani, maji ya Bahari Hindi ni myeyusho uliojaa chumvi (saline solution) ambapo lita moja ya maji hubeba takriban gramu 35 za chumvi iliyoyeyuka!",
                "analogy_en": "At coastal marine shores, seawater is a rich aqueous solution carrying ~35 grams of dissolved mineral solutes per liter of water!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, wakulima wanapochanganya dawa ya maji ya kuua wadudu na maji kwenye pampu ya mgongoni (Knapsack sprayer), wanatengeneza myeyusho sawia wa kunyunyuzia mimea!",
                "analogy_en": "In highland crop spraying, agricultural fungicides dissolve completely in water to form uniform spray solutions for maize crops!"
            },
            "arid": {
                "analogy_sw": "Kwenye Ziwa Magadi, joto kali la jua hufanya myeyusho wa maji ya magadi kujaa kupita kiasi (Super-saturated) na kuunda fuwele kubwa za magadi ya trona!",
                "analogy_en": "At hyper-saline Lake Magadi, intense solar heating drives trona brine beyond saturation point, precipitating massive mineral crystalline beds!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mtoto akiugua kuhara, daktari anashauri kutengeneza myeyusho wa ORS (Oral Rehydration Salts) kwa kuchanganya chumvi kidogo na sukari kwenye maji safi ya kunywa!",
                "analogy_en": "In urban healthcare clinics, Oral Rehydration Salt (ORS) solutions restore vital electrolytes by dissolving precise ratios of sodium and glucose in sterile water!"
            }
        },
        "key_terms": [
            {"en": "Solute (Dissolved substance, e.g. Salt)", "sw": "Kiyeyushwa (Kitu kinachoyeyushwa, mf. Chumvi)"},
            {"en": "Solvent (Dissolving liquid, e.g. Water)", "sw": "Kiyeyushaji (Kioevu kinachoyeyusha, mf. Maji)"},
            {"en": "Saturated Solution", "sw": "Myeyusho Uliojaa (Hauwezi kuyeyusha zaidi)"},
            {"en": "Solubility Curve & Temperature", "sw": "Kiwango cha Kuyeyuka (Huongezeka kwa joto)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kutengeneza Myeyusho Uliojaa wa Sukari (Saturated Solution)",
            "title_en": "Experiment: Saturation Point of Table Sugar in Water",
            "materials_sw": "Glasi nusu ya maji, vijiko 6 vya sukari, kijiko cha kukorogea.",
            "materials_en": "Half glass of water, 6 teaspoons of sugar, stirring spoon.",
            "steps_sw": "1. Weka kijiko 1 cha sukari kwenye maji na ukoroge—itayeyuka yote.\n2. Ongeza kijiko cha 2, 3, 4, 5 huku ukikoroga.\n3. Kwenye kijiko cha 6, sukari itabaki chini bila kuyeyuka hata ukikoroga vipi—huo ni Myeyusho Uliojaa (Saturated Solution)!\n4. Ukipasha maji joto kidogo, sukari hiyo iliyobaki itayeyuka mara moja!",
            "steps_en": "1. Dissolve 1 teaspoon of sugar—it dissolves completely.\n2. Continue adding spoons 2, 3, 4, 5 while stirring.\n3. By spoon 6, excess crystals remain undissolved at the bottom—reaching the Saturation Point!\n4. Gently warming the water dissolves the excess crystals immediately!"
        },
        "quiz": {
            "question_sw": "Kwenye glasi ya maji yenye chumvi iliyoyeyuka, Maji yanaitwaje katika istilahi za kikemia?",
            "question_en": "In a cup of saltwater solution, what is the Water scientifically called?",
            "options_sw": ["A) Kiyeyushaji (Solvent)", "B) Kiyeyushwa (Solute)", "C) Mawe", "D) Gesikemia"],
            "options_en": ["A) Solvent", "B) Solute", "C) Stone", "D) Gas"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Maji ndio Kiyeyushaji (Solvent) kinachoyeyusha chembe za chumvi (Kiyeyushwa / Solute).",
            "explanation_en": "Spot on! Water is the universal solvent that dissolves solid solutes like salt into homogeneous solutions."
        }
    }
]
