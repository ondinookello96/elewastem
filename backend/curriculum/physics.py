"""
ElewaSTEM Curriculum — Physics Learning Modules (10 Topics)
Aligned with KICD (Kenya CBC Grades 4-9), NERDC (Nigeria), DBE CAPS (South Africa), NaCCA (Ghana).
"""

from typing import List, Dict, Any

PHYSICS_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "electricity_circuits",
        "title_en": "Electric Current, Voltage & Circuits",
        "title_sw": "Mkondo wa Umeme, Saketi na Betri",
        "subject": "Physics",
        "cbc_strand": "Energy & Transformations (Grade 5/6 Science & Grade 8 Integrated Science)",
        "summary_en": "Electricity is the flow of tiny electric charges (electrons) through a closed conductive loop with a power source (battery) and load (bulb).",
        "summary_sw": "Umeme ni mtiririko wa chembe ndogo za chaji (elektroni) kupitia waya katika saketi iliyofungwa yenye betri na balbu au kifaa cha umeme.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika betri ya tochi mkononi mwako. Ncha ya juu yenye kitufe ni Upande Chanya (+), na sehemu ya chini bapa ni Upande Hasi (-). Unapounganisha waya wa shaba kutoka juu hadi chini kupitia balbu, mtiririko wa chaji unawasha balbu mara moja!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Betri] ➔ [Waya za Shaba zilizounganishwa] ➔ [Swichi inapofungwa] ➔ [Balbu inawaka Mwangaza].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kama mtambo wa umeme wa maji wa Sondu Miriu kando ya Ziwa Victoria unavyosukuma umeme kupitia nyaya za gridi hadi kwenye taa za Kisumu, betri inasukuma chaji za umeme kwenye waya!",
                "analogy_en": "Just as the Sondu Miriu hydroelectric plant pushes electric current through power lines across Kisumu, a battery pushes electrons through circuit wires!"
            },
            "coastal": {
                "analogy_sw": "Pwani, mitambo ya upepo ya Ngong na taa za Solar za Kilifi zinabadilisha nishati ya upepo na jua kuwa umeme unaotembea kwenye waya!",
                "analogy_en": "At the coast, solar PV panels and wind turbines convert renewable energy into direct electrical current flowing through circuits!"
            },
            "highlands": {
                "analogy_sw": "Mashambani kwenye viwanda vya chai vya Kericho, mota kubwa za umeme zinafanya kazi kwa mtiririko wa umeme kupitia saketi salama zenye fyuzi!",
                "analogy_en": "In highland tea processing factories, heavy industrial electric motors run continuously via safely fused three-phase circuits!"
            },
            "arid": {
                "analogy_sw": "Kwenye vituo vya afya vya Garissa na Wajir, paneli za jua zinachaji betri za Lithium ili kuweka chanjo na dawa kwenye friji ya umeme masaa 24!",
                "analogy_en": "In arid off-grid health dispensaries, solar arrays charge battery banks to power vital vaccine refrigeration circuits continuously!"
            },
            "urban": {
                "analogy_sw": "Mtaani, swichi ya ukutani inafanya kazi kama daraja la reli—ikifungwa treni ya elektroni inapita kuwasha taa, ikifunguliwa treni inasimama!",
                "analogy_en": "In city households, light switches act as drawbridges: closing completes the circuit path, while opening breaks the electron flow instantly!"
            }
        },
        "key_terms": [
            {"en": "Electric Current (Amperes)", "sw": "Mkondo wa Umeme (Ampea)"},
            {"en": "Voltage (Volts)", "sw": "Msukumo wa Umeme (Volti)"},
            {"en": "Complete / Closed Circuit", "sw": "Saketi Iliyokamilika / Iliyofungwa"},
            {"en": "Conductors & Insulators", "sw": "Vipitishio (Shaba/Chuma) na Vihami (Plastiki/Mpira)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kutengeneza Saketi Rahisi kwa Betri ya Tochi na Waya",
            "title_en": "Experiment: Simple Battery & Torch Bulb Circuit",
            "materials_sw": "Betri moja ya tochi (1.5V), balbu ndogo, waya fupi mbili za shaba zilizomenywa ncha.",
            "materials_en": "One 1.5V AA torch battery, small torch bulb, two stripped copper wires.",
            "steps_sw": "1. Unganisha waya mmoja kwenye ncha ya juu ya betri (+).\n2. Unganisha waya wa pili chini ya betri (-).\n3. Gusa ncha zote mbili kwenye sehemu ya chuma ya balbu—balbu itawaka mara moja!",
            "steps_en": "1. Tape one wire to the positive battery terminal (+).\n2. Tape the second wire to the flat negative terminal (-).\n3. Touch both bare ends to the bulb base to complete the circuit and watch it light up!"
        },
        "quiz": {
            "question_sw": "Ni kipi kati ya vifaa vifuatavyo ni Kipitishio kizuri cha umeme (Conductor)?",
            "question_en": "Which of the following materials is an excellent Conductor of electricity?",
            "options_sw": ["A) Waya wa Shaba (Copper Wire)", "B) Plastiki", "C) Kuni kavu", "D) Mpira"],
            "options_en": ["A) Copper Wire", "B) Plastic", "C) Dry wood", "D) Rubber"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Shaba na metali zingine ni vipitishio vizuri vinavyoruhusu elektroni kupita kwa urahisi.",
            "explanation_en": "Brilliant! Copper and most metals are conductors allowing free electron movement."
        }
    },
    {
        "id": "gravity_forces",
        "title_en": "Gravity, Friction & Newton's Laws of Motion",
        "title_sw": "Grabiti, Msuguano na Nguvu za Mwendo",
        "subject": "Physics",
        "cbc_strand": "Forces & Energy (Grade 5/6 Science & Grade 7 Integrated Science)",
        "summary_en": "Gravity pulls all objects toward the center of the Earth at 9.8 m/s², while friction opposes motion between contacting surfaces.",
        "summary_sw": "Nguvu ya mvuto wa dunia (grabiti) huvuta vitu vyote chini ardhini, huku nguvu ya msuguano (friction) ikipinga mwendo kati ya nyuso mbili zinazogusana.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika kitabu au kijiti mkononi mwako. Kifungue kiganja chako na ukiachie—kitabu kitaanguka moja kwa moja sakafuni. Hiyo ni nguvu isiyoonekana ya Grabiti inayovuta vitu vyote kuelekea katikati ya dunia!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kitu kinachoanguka chini / Grabiti] + [Kusugua viganja viwili pamoja na kuhisi joto / Msuguano].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu unapoendesha baiskeli ya 'Black Mamba' au Boda boda kuteremka mlima Riat, grabiti inakuvuta chini kwa kasi huku breki za mpira zikishika tairi kutoa msuguano salama wa kusimama!",
                "analogy_en": "In Kisumu riding a bicycle down Riat Hills, gravity accelerates you downhill while rubber brake pads exert friction on the wheel rims to stop safely!"
            },
            "coastal": {
                "analogy_sw": "Pwani, nazi ikikatika mtini huanguka chini kwa kasi ya grabiti, na kutua kwenye mchanga laini unaopunguza mshtuko!",
                "analogy_en": "At coastal plantations, ripe coconuts falling from palms accelerate downward under gravity, landing safely on shock-absorbing soft sand!"
            },
            "highlands": {
                "analogy_sw": "Milimani Nyahururu kwenye Maporomoko ya Thomson (Thomson's Falls), mamilioni ya tani za maji huanguka mita 74 chini ardhini kwa sababu ya mvuto wa grabiti!",
                "analogy_en": "At Thomson's Falls in Nyahururu, immense volumes of river water plunge 74 meters downward driven entirely by gravitational potential energy!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo ya mchanga, nyayo pana za ngamia zinaongeza eneo la mguso ili kuzuia kuteleza na kutoa msuguano mzuri wa kutembea bila kuzama!",
                "analogy_en": "In desert terrains, broad camel footpads increase contact surface area, providing optimal friction across loose shifting sands!"
            },
            "urban": {
                "analogy_sw": "Mtaani, barabara za lami zenye magurudumu ya gari hutoa msuguano unaozuia gari kuteleza hata wakati wa mvua!",
                "analogy_en": "In city transport, tire tread grooves generate traction friction against asphalt to prevent vehicle hydroplaning in wet weather!"
            }
        },
        "key_terms": [
            {"en": "Gravity (Gravitational Force)", "sw": "Nguvu ya Mvuto wa Dunia (Grabiti)"},
            {"en": "Friction Force", "sw": "Nguvu ya Msuguano (Inazuia kuteleza)"},
            {"en": "Mass (kg) vs Weight (N)", "sw": "Masi (Uzito ghafi) vs Uzani (Nguvu ya mvuto)"},
            {"en": "Lubrication", "sw": "Vilainishi (Mafuta/Grisi ya kupunguza msuguano)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Jinsi Msuguano Unavyozuia Kuteleza",
            "title_en": "Experiment: Surface Friction Comparison Test",
            "materials_sw": "Kipande kidogo cha sabuni, meza kavu, tone la maji.",
            "materials_en": "Bar of soap, dry table, water droplet.",
            "steps_sw": "1. Sukuma sabuni kwenye meza kavu—utahisi ikisimama haraka kwa msuguano.\n2. Weka tone la maji na usukume tena—itateleza kwa kasi kwa sababu maji yamepunguza msuguano!\n3. Ndio maana mafuta huwekwa kwenye injini!",
            "steps_en": "1. Slide dry soap across a table—friction halts it quickly.\n2. Wet the surface and slide again—it glides effortlessly as water acts as a friction-reducing lubricant!"
        },
        "quiz": {
            "question_sw": "Ni nguvu gani inayovuta maembe, mawe na vitu vyote vilivyorushwa angani kurudi chini ardhini?",
            "question_en": "Which force pulls falling fruits and thrown stones back down to the Earth?",
            "options_sw": ["A) Nguvu ya Grabiti (Gravity)", "B) Upepo tu", "C) Sumaku", "D) Mwanga"],
            "options_en": ["A) Gravitational Force", "B) Wind only", "C) Magnetism", "D) Light"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Nguvu ya Grabiti (mvuto wa dunia) huvuta kila kitu kuelekea chini.",
            "explanation_en": "Spot on! Earth's gravitational pull accelerates all unsupported masses downward toward its center."
        }
    },
    {
        "id": "light_reflection_refraction",
        "title_en": "Light Optics: Reflection, Refraction & Lenses",
        "title_sw": "Mwangaza: Akisi (Reflection), Mvunjiko wa Nuru (Refraction) na Lenzi",
        "subject": "Physics",
        "cbc_strand": "Energy & Optics (Grade 6 Science & Grade 8 Integrated Science)",
        "summary_en": "Light travels in straight lines at 300,000 km/s. It reflects off shiny surfaces at equal angles and bends (refracts) when passing from air into water or glass.",
        "summary_sw": "Mwangaza husafiri kwa mistari iliyonyooka. Huakisiwa kwenye kioo kwa pembe sawa, na hupinda (refraction) unapoingia kutoka hewani kwenda kwenye maji au kioo.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika glasi ya maji safi na uweke kijiko ndani yake. Unapogusa kijiko, kinahisi kimenyooka kabisa, lakini machoni kinaonekana kama kimevunjika katikati ya maji—huo ni Mvunjiko wa Nuru (Refraction) kwa sababu mwanga hupunguza kasi ndani ya maji!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Mwangaza unanyooka] ➔ [Kioo kinaakisi mwanga / Reflection] ➔ [Kijiko ndani ya Maji kinaonekana kupinda / Refraction].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria wakati wa alasiri, uso wa maji tulivu ya ziwa hufanya kazi kama kioo kikubwa kinachoakisi mwangaza wa jua na picha ya anga (Reflection)!",
                "analogy_en": "Across tranquil Lake Victoria waters at sunset, the mirror-smooth surface reflects the golden sky (Reflection) like a giant optical mirror!"
            },
            "coastal": {
                "analogy_sw": "Pwani, unapoangalia samaki ndani ya maji safi ya Bahari Hindi, samaki anaonekana yuko karibu na juu kuliko alipo haswa kwa sababu ya Mvunjiko wa Nuru (Refraction)!",
                "analogy_en": "In coastal marine waters, submerged corals and fish appear shallower than their true position due to light refraction across the water-air boundary!"
            },
            "highlands": {
                "analogy_sw": "Milimani baada ya mvua ya alasiri, matone ya maji angani hupinda mwangaza wa jua na kutenganisha rangi 7 kuunda Upinde wa Mvua (Rainbow) mzuri!",
                "analogy_en": "In highland valleys after afternoon rain, suspended mist droplets disperse sunlight into the 7 spectral colors of a brilliant rainbow!"
            },
            "arid": {
                "analogy_sw": "Kwenye barabara za lami za Garissa mchana wa jua kali, hewa ya moto inavunja mwangaza wa jua na kutengeneza taswira ya maji ya uwongo barabarani (Mirage)!",
                "analogy_en": "On hot arid desert highways, layers of superheated air refract light to produce optical shimmering illusions (Mirages) resembling water pools!"
            },
            "urban": {
                "analogy_sw": "Mtaani, vioo vya pembeni vya gari (convex mirrors) vinaakisi eneo pana ili dereva aone magari yote yaliyo nyuma kwa usalama!",
                "analogy_en": "In city traffic, convex side-view mirrors diverge reflected light rays to afford drivers a panoramic wide-angle field of view!"
            }
        },
        "key_terms": [
            {"en": "Reflection", "sw": "Akisi ya Mwangaza (Kugonga na kurudi kwenye kioo)"},
            {"en": "Refraction", "sw": "Mvunjiko wa Nuru (Mwanga kupinda unapoingia majini)"},
            {"en": "Lenses (Convex & Concave)", "sw": "Lenzi Mbinuko (Kukuza) na Lenzi Mbonyeo"},
            {"en": "Spectrum & Rainbow", "sw": "Upinde wa Mvua (Rangi 7 za Mwangaza)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Kijiko 'Kilichovunjika' Ndani ya Glasi ya Maji",
            "title_en": "Experiment: The Bent Pencil Refraction Illusion",
            "materials_sw": "Glasi ya kioo iliyo wazi, maji nusu, penseli au kijiko.",
            "materials_en": "Clear glass, water, pencil or spoon.",
            "steps_sw": "1. Weka maji nusu kwenye glasi.\n2. Dumbukiza penseli iliyonyooka ndani ya maji.\n3. Angalia kwa pembeni—penseli itaonekana imekatika au kupinda kwenye mpaka wa maji na hewa!",
            "steps_en": "1. Fill a clear glass half-full with water.\n2. Place a straight pencil into the glass.\n3. View from the side—the pencil appears sharply bent at the water surface due to refraction!"
        },
        "quiz": {
            "question_sw": "Ni jambo gani la kisayansi linalosababisha kijiko kilichowekwa ndani ya glasi ya maji kuonekana kimepinda au kuvunjika?",
            "question_en": "Which optical phenomenon causes a straight spoon in a glass of water to appear bent?",
            "options_sw": ["A) Mvunjiko wa Nuru (Refraction)", "B) Giza", "C) Upepo", "D) Sumaku"],
            "options_en": ["A) Refraction of Light", "B) Darkness", "C) Wind", "D) Magnetism"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Mvunjiko wa nuru (Refraction) hutokea pale mwangaza unaposafiri polepole zaidi ndani ya maji kuliko hewani na hivyo kupinda mwelekeo.",
            "explanation_en": "Spot on! Refraction occurs because light changes speed and bends when transitioning between optical media of different densities."
        }
    },
    {
        "id": "sound_waves_hearing",
        "title_en": "Sound Waves, Frequency, Pitch & Hearing",
        "title_sw": "Mawimbi ya Sauti, Marudio (Frequency), Mlio na Usikivu",
        "subject": "Physics",
        "cbc_strand": "Energy & Wave Phenomena (Grade 6/7 Integrated Science)",
        "summary_en": "Sound is produced by vibrating objects and travels through air, liquids, and solids as longitudinal pressure waves at ~340 m/s. It cannot travel in a vacuum.",
        "summary_sw": "Sauti huzalishwa na mitetemo (vibrations) na kusafiri kupitia hewa, maji, na vitu vigumu kama mawimbi ya msukumo kwa kasi ya mita 340 kwa sekunde. Haisafiri pasipo hewa.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Weka vidole vyako kooni mbele ya koromeo lako. Imba 'laaa... laaa' au ongea kwa sauti. Utahisi mtetemo wenye kasi kwenye vidole vyako—huo mtetemo wa nyuzi za sauti ndio unaotengeneza sauti inayosafiri hewani!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kugusa Ngoma inayopigwa na Kuhisi Mtetemo] ➔ [Mawimbi ya Sauti yanasafiri Hewani] ➔ [Ngoma ya Sikio inatetemeka kutuma ujumbe kwenye Ubongo].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu unaposikia ngoma za kitamaduni za Ohangla zikipigwa, ngozi ya ngoma inatetemeka kwa nguvu na kusukuma hewa kuunda mawimbi ya sauti yanayosafiri kilomita kadhaa ziwani!",
                "analogy_en": "In lake celebrations when traditional Ohangla drums are struck, vibrating drum skins compress surrounding air to propagate resonant sound waves across the lake!"
            },
            "coastal": {
                "analogy_sw": "Pwani, mlio wa honi ya meli kubwa bandarini una sauti ya chini yenye marudio mazito (Low Pitch) inayopenya mbali hata kwenye ukungu wa bahari!",
                "analogy_en": "At the Mombasa seaport, deep low-pitch ship foghorns generate long-wavelength acoustic waves that travel miles through dense maritime fog!"
            },
            "highlands": {
                "analogy_sw": "Milimani unapopiga kelele kwenye bonde la mlima, sauti yako inagonga ukuta wa mawe na kurudi kama mwangwi (Echo / Reflection of Sound)!",
                "analogy_en": "In highland valleys when shouting near rocky cliffs, sound waves reflect off the rock face and return as distinct echoes!"
            },
            "arid": {
                "analogy_sw": "Kwenye ukimya wa usiku wa jangwani, sauti ya wanyama husafiri umbali mrefu sana kwa sababu hewa tulivu ya baridi ya ardhini inapitisha mawimbi vizuri!",
                "analogy_en": "In still desert night skies, temperature inversions trap sound waves near the ground, allowing nocturnal animal calls to carry for miles!"
            },
            "urban": {
                "analogy_sw": "Mtaani, madirisha yenye vioo vizito au spika za muziki hutetemeka kwa nguvu wakati gari lenye sauti ya 'bass' kubwa linapopita karibu!",
                "analogy_en": "In urban streets, low-frequency bass notes from music speakers physically vibrate shopfront glass windows through air pressure pulses!"
            }
        },
        "key_terms": [
            {"en": "Vibrations", "sw": "Mitetemo (Chanzo kikuu cha sauti yoyote)"},
            {"en": "Pitch (Frequency in Hertz)", "sw": "Ukali au Unene wa Sauti (Hertz)"},
            {"en": "Loudness / Volume (Decibels)", "sw": "Ukubwa wa Sauti (Decibels)"},
            {"en": "Echo", "sw": "Mwangwi (Sauti inayogonga ukuta na kurudi)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Mtetemo wa Sauti Kwenye Karatasi na Mchele",
            "title_en": "Experiment: Dancing Rice Sound Vibration Test",
            "materials_sw": "Bakuli la plastiki, nailoni iliyovutwa juu kama ngoma, punje 5 za mchele, kupiga kelele au kugonga sufuria.",
            "materials_en": "Plastic bowl, stretched cling wrap, 5 grains of uncooked rice, metal spoon/pot.",
            "steps_sw": "1. Funga nailoni juu ya bakuli iwe ngumu kama ngozi ya ngoma.\n2. Weka punje chache za mchele juu ya nailoni.\n3. Piga sufuria kwa nguvu karibu na bakuli bila kuigusa—utaona mchele 'ukicheza' na kurukaruka kwa nguvu ya mawimbi ya sauti!",
            "steps_en": "1. Stretch plastic wrap tightly over an open bowl.\n2. Place uncooked rice grains on top.\n3. Bang a metal pot near the bowl without touching it—observe the rice grains dancing from acoustic sound wave pressure!"
        },
        "quiz": {
            "question_sw": "Ni kitu gani cha lazima kinachotakiwa kutokea ili sauti yoyote iweze kuzalishwa?",
            "question_en": "What must happen for any sound to be generated?",
            "options_sw": ["A) Mtetemo wa vitu au hewa (Vibration)", "B) Mwanga mkali", "C) Kupoa kwa joto", "D) Kuwasha balbu"],
            "options_en": ["A) Mechanical vibration of matter", "B) Bright light", "C) Cooling temperature", "D) Lighting a bulb"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Sauti zote ulimwenguni huzalishwa na mitetemo (vibrations) inayotikisa hewa au vitu.",
            "explanation_en": "Brilliant! Every sound in the universe originates from mechanical vibrations disturbing a material medium."
        }
    },
    {
        "id": "simple_machines_levers",
        "title_en": "Simple Machines: Levers, Pulleys & Inclined Planes",
        "title_sw": "Mashine Rahisi: Wenzo (Levers), Roda (Pulleys) na Mtelemko",
        "subject": "Physics",
        "cbc_strand": "Work & Simple Machines (Grade 5/6 Science & Grade 7 Integrated Science)",
        "summary_en": "Simple machines make work easier by magnifying input effort force or changing its direction using mechanical advantage.",
        "summary_sw": "Mashine rahisi hufanya kazi kuwa rahisi kwa kuongeza nguvu ya msukumo au kubadilisha mwelekeo wa nguvu kwa kutumia faida ya kimitambo (Mechanical Advantage).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika mkasi mkononi mwako. Sehemu unayoshikilia kwa vidole inaitwa Nguvu (Effort), pini ya katikati inayozunguka ni Egemo (Fulcrum/Pivot), na makali yanayokata karatasi ni Mzigo (Load). Huu ni mfano wa Wenzo wa Daraja la Kwanza!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Wenzo / Lever: Nguvu ➔ Egemo Katikati ➔ Mzigo Unanyanyuka] + [Roda / Pulley: Kuvuta Kamba Chini ili Mzigo Upande Juu].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria, wavuvi wanapotumia kasia kupiga mashua majini au winchi ya kamba kuvuta mashua nchi kavu, wanatumia kanuni za mashine rahisi za Wenzo na Roda!",
                "analogy_en": "On Lake Victoria, fishermen using wooden oars as levers or rope capstans to haul canoes ashore apply fundamental simple machine mechanics!"
            },
            "coastal": {
                "analogy_sw": "Pwani, wajenzi wanapotumia mteremko wa ubao (Inclined Plane) kusukuma mapipa mazito ya mafuta kwenye gari la kubeba mizigo, wanatumia nguvu ndogo zaidi kuliko kuyanyanyua wima!",
                "analogy_en": "At coastal docks, workers using inclined wooden loading ramps push heavy drums onto trucks with far less effort force than lifting vertically!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, toroli ya kubeba magunia ya viazi (Wheelbarrow) ni mfano wa Wenzo wa Daraja la Pili ambapo mzigo uko katikati ya gurudumu na mikono ya mkulima!",
                "analogy_en": "On highland farms, farm wheelbarrows act as second-class levers with heavy crop loads positioned between the pivot wheel and the handles!"
            },
            "arid": {
                "analogy_sw": "Kwenye visima virefu vya maji kule Wajir na Turkana, ndoo ya maji huvutwa juu kwa urahisi kwa kutumia Roda (Pulley) inayobadilisha mwelekeo wa nguvu!",
                "analogy_en": "At deep pastoral boreholes, well pulleys allow herders to hoist heavy water buckets easily by pulling downward with bodyweight!"
            },
            "urban": {
                "analogy_sw": "Mtaani, kopo la soda linafunguliwa kwa urahisi kwa kizibuo cha kopo (bottle opener) kinachofanya kazi kama wenzo imara unaozidisha nguvu ya kidole chako mara tano!",
                "analogy_en": "In urban households, bottle openers act as sturdy levers, magnifying fingertip effort force to pop stubborn metal bottle caps effortlessly!"
            }
        },
        "key_terms": [
            {"en": "Lever (Effort, Pivot, Load)", "sw": "Wenzo (Nguvu, Egemo, na Mzigo)"},
            {"en": "Pulley", "sw": "Roda (Gurudumu lenye kamba ya kunyanyulia)"},
            {"en": "Inclined Plane (Ramp)", "sw": "Bapa Mwelekeo / Mteremko"},
            {"en": "Mechanical Advantage", "sw": "Faida ya Kimitambo (Uwiano wa Mzigo na Nguvu)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuinua Kitabu Kizito kwa Rula na Kifutio (Wenzo)",
            "title_en": "Experiment: Ruler & Eraser Tabletop Lever",
            "materials_sw": "Rula ya plastiki/mbao ya cm 30, kifutio kigumu au penseli ya duara (egemo), kitabu kizito.",
            "materials_en": "30 cm ruler, rubber eraser or pencil (fulcrum), heavy book.",
            "steps_sw": "1. Weka kifutio chini ya rula katikati.\n2. Weka kitabu kizito upande mmoja wa rula.\n3. Bonyeza upande wa pili kwa kidole kimoja tu—kitabu kizito kitainuka juu kwa urahisi mkubwa!",
            "steps_en": "1. Place the eraser under the center of the ruler to serve as a fulcrum.\n2. Rest a heavy book on one end.\n3. Press down on the opposite end with just one finger—the heavy load lifts effortlessly!"
        },
        "quiz": {
            "question_sw": "Kwenye Wenzo (Lever), sehemu ya katikati inayoshikilia na kugeukia ambapo mashine inasimamia inaitwaje?",
            "question_en": "In a lever, what is the fixed pivot point around which the lever rotates called?",
            "options_sw": ["A) Egemo (Fulcrum / Pivot)", "B) Mzigo tu", "C) Kamba", "D) Magurudumu"],
            "options_en": ["A) Fulcrum / Pivot", "B) Load only", "C) Rope", "D) Wheels"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Egemo (Fulcrum) ndio kitovu ambacho wenzo unazungukia ili kuwezesha kuinua mzigo mzito kwa nguvu ndogo.",
            "explanation_en": "Brilliant! The fulcrum is the fixed pivot point about which the lever pivots to gain mechanical advantage."
        }
    },
    {
        "id": "heat_transfer_methods",
        "title_en": "Heat Transfer: Conduction, Convection & Radiation",
        "title_sw": "Usafirishaji wa Joto: Mpitisho (Conduction), Msafara (Convection) na Mnururisho (Radiation)",
        "subject": "Physics",
        "cbc_strand": "Energy & Heat Dynamics (Grade 5/6 Science & Grade 8 Integrated Science)",
        "summary_en": "Thermal energy transfers in three distinct ways: Conduction through direct molecular collisions in solids, Convection through fluid bulk circulation in liquids/gases, and Radiation via infrared electromagnetic waves across empty space.",
        "summary_sw": "Nishati ya joto husafiri kwa njia tatu: Mpitisho (Conduction) kwenye vitu vigumu kama vyuma, Msafara (Convection) kwenye hewa na maji, na Mnururisho (Radiation) kupitia miale ya jua angani.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika kijiko cha chuma na ukidumbukize kwenye kikombe cha chai moto. Baada ya dakika moja, gusa ncha ya juu ya kijiko—utahisi ikiwa ya moto. Joto limesafiri chembe kwa chembe kupitia chuma kwa njia ya Mpitisho (Conduction)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kijiko cha chuma jikoni / Conduction] ➔ [Maji yanayochemka yakizunguka / Convection] ➔ [Jua linalomulika joto angani / Radiation].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu unapochemsha maji ya chai kwenye sufuria: Joto linapita kwenye chuma cha sufuria kwa Conduction, maji yanazunguka juu na chini kwenye sufuria kwa Convection, na joto la jiko unalolisikia mkononi ni Radiation!",
                "analogy_en": "In lake kitchens when boiling tea: Heat conducts through the metallic pot base, circulates warm water upward via convection currents, and radiates infrared heat to nearby hands!"
            },
            "coastal": {
                "analogy_sw": "Pwani, upepo mwanana wa nchi kavu na bahari (Land and Sea Breezes) huundwa na mikondo ya hewa ya Convection kwa sababu mchanga hupata joto haraka kuliko maji ya bahari!",
                "analogy_en": "Along coastal beaches, daily sea and land breezes are driven by atmospheric convection currents arising from differential heating of land vs sea!"
            },
            "highlands": {
                "analogy_sw": "Milimani kwenye baridi, jagi la 'Thermos' (Vacuum Flask) lina kuta mbili zenye utupu katikati kuzuia joto lisitoke kwa conduction wala convection, na kioo kinachoakisi kuzuia radiation!",
                "analogy_en": "In cold highland homes, vacuum flasks keep tea steaming hot for hours by blocking conduction/convection across the vacuum gap and reflecting infrared radiation with silvered walls!"
            },
            "arid": {
                "analogy_sw": "Kwenye jua kali la jangwani, joto lote la jua linafika ardhini moja kwa moja kupitia mamilioni ya kilomita za anga tupu kwa njia ya Mnururisho (Radiation)!",
                "analogy_en": "In arid plains, radiant thermal energy travels 150 million kilometers across the vacuum of space exclusively via electromagnetic radiation!"
            },
            "urban": {
                "analogy_sw": "Mtaani, kuta za nyumba zilizopakwa rangi nyeupe huakisi miale ya joto ya radiation ili chumba kibaki na ubaridi mzuri wakati wa mchana!",
                "analogy_en": "In urban building architecture, white rooftop coatings reflect incident solar radiation to keep indoor living spaces naturally cool!"
            }
        },
        "key_terms": [
            {"en": "Conduction (Solids)", "sw": "Mpitisho wa Joto (Kupitia vitu vigumu kama metali)"},
            {"en": "Convection (Fluids)", "sw": "Msafara wa Joto (Kupitia mzunguko wa maji na hewa)"},
            {"en": "Radiation (Waves)", "sw": "Mnururisho wa Joto (Kupitia miale isiyohitaji hewa)"},
            {"en": "Insulators", "sw": "Vihami vya Joto (Mbao, Plastiki, Nguo za pamba)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Mpitisho wa Joto Kwenye Kijiko cha Chuma",
            "title_en": "Experiment: Metal vs Wooden Spoon Thermal Conduction Test",
            "materials_sw": "Kikombe kimoja cha maji ya moto, kijiko cha chuma, kijiko cha mbao/plastiki, vitone viwili vya siagi au mafuta.",
            "materials_en": "Mug of hot water, one metal spoon, one wooden/plastic spoon, two small dabs of margarine.",
            "steps_sw": "1. Weka tone la siagi juu ya ncha ya kila kijiko.\n2. Dumbukiza ncha za chini kwenye maji ya moto kwa wakati mmoja.\n3. Siagi kwenye kijiko cha chuma itayeyuka mara moja kwa sababu chuma ni kipitishio bora cha joto (Conductor)!",
            "steps_en": "1. Place a dab of butter on the handle of both spoons.\n2. Place lower ends simultaneously into hot water.\n3. The butter on the metallic spoon melts rapidly, proving metals conduct heat far faster than wood!"
        },
        "quiz": {
            "question_sw": "Joto la jua linafikaje duniani kutoka angani ambapo hakuna hewa wala vitu vigumu?",
            "question_en": "How does thermal energy from the Sun reach Earth across the vacuum of empty space?",
            "options_sw": ["A) Kwa Mnururisho wa Miale (Radiation)", "B) Kwa Mpitisho tu", "C) Kwa kupiga kelele", "D) Kwa maji"],
            "options_en": ["A) Thermal Radiation (Infrared Waves)", "B) Conduction only", "C) Sound waves", "D) Water currents"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Mnururisho (Radiation) ndiyo njia pekee ya usafirishaji wa joto inayoweza kupita kwenye utupu (vacuum) bila kuhitaji chembe za hewa au maji.",
            "explanation_en": "Spot on! Radiation transfers heat via electromagnetic waves, which do not require a material medium and easily traverse the vacuum of space."
        }
    },
    {
        "id": "magnetism_electromagnets",
        "title_en": "Magnetism, Magnetic Poles & Electromagnets",
        "title_sw": "Sumaku, Ncha za Sumaku na Sumakuumeme (Electromagnets)",
        "subject": "Physics",
        "cbc_strand": "Forces & Magnetism (Grade 5/6 Science & Grade 8 Integrated Science)",
        "summary_en": "Magnets exert non-contact forces: like poles repel (N-N, S-S) and opposite poles attract (N-S). Electric current flowing through a coiled wire creates a controllable electromagnet.",
        "summary_sw": "Sumaku zina ncha mbili: Ncha zinazofanana husukumana (N-N, S-S) na ncha tofauti huvutana (N-S). Mkondo wa umeme unaopita kwenye koili ya waya hutengeneza Sumakuumeme inayozimika na kuwaka.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika sumaku mbili mkononi mwako. Ukileta ncha za Kaskazini na Kusini pamoja, zitanasiana kwa nguvu (Attraction). Lakini ukigeuza ncha inayofanana, utahisi msukumo usioonekana unaozikataza kugusana (Repulsion)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ncha za Sumaku N + S Zikivutana] vs [Ncha N + N Zikisukumana Mbali] ➔ [Waya iliyojizungusha kwenye msumari inawasha sumaku kwa betri].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria, dira ya nahodha wa mashua inatumia sindano ya sumaku inayoelekea Kaskazini ya dunia kila wakati ili kuongoza safari ziwani bila kupotea!",
                "analogy_en": "On Lake Victoria, navigators rely on magnetic compass needles aligning with Earth's geomagnetic field to steer safely across open waters!"
            },
            "coastal": {
                "analogy_sw": "Pwani kule bandarini, sumakuumeme kubwa sana (Electromagnet cranes) zilizounganishwa kwenye 'cranes' hutumika kunyanyua makontena na vyuma vizito kwa kuwasha swichi ya umeme tu!",
                "analogy_en": "At Mombasa container terminals, heavy industrial electromagnet cranes lift tons of scrap iron with the flip of an electrical switch!"
            },
            "highlands": {
                "analogy_sw": "Kwenye vituo vya radio na simu milimani, spika za sauti hutumia sumaku imara kusukuma koni ya spika na kutengeneza muziki mtamu!",
                "analogy_en": "In highland radio broadcast stations, acoustic loudspeakers utilize permanent neodymium magnets interacting with voice coils to produce clear sound!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo yenye madini ya chuma, sumaku hutumiwa na wachimbaji kutenganisha mchanga wa chuma na mchanga wa kawaida ardhini!",
                "analogy_en": "In mineral extraction zones, prospectors use handheld magnetic separators to isolate iron-bearing ores from non-magnetic sand!"
            },
            "urban": {
                "analogy_sw": "Mtaani, milango ya friji nyumbani ina mikanda ya sumaku laini pembezoni ili kuhakikisha mlango unafunga vizuri na hewa baridi haitoki!",
                "analogy_en": "In modern city homes, refrigerator door seals incorporate flexible magnetic strips ensuring airtight thermal insulation!"
            }
        },
        "key_terms": [
            {"en": "Magnetic Poles (North & South)", "sw": "Ncha za Sumaku (Kaskazini na Kusini)"},
            {"en": "Law of Magnetism", "sw": "Kanuni: Ncha tofauti huvutana, zinazofanana husukumana"},
            {"en": "Magnetic Field Lines", "sw": "Mistari ya Sehemu ya Nguvu ya Sumaku"},
            {"en": "Electromagnet", "sw": "Sumakuumeme (Sumaku inayoundwa na umeme)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kutengeneza Sumakuumeme kwa Msumari, Waya na Betri",
            "title_en": "Experiment: DIY Nail & Wire Electromagnet",
            "materials_sw": "Msumari mrefu wa chuma, waya mwembamba wa shaba (futi 2), betri ya 1.5V, pini ndogo za ofisi za chuma.",
            "materials_en": "Long iron nail, 2 feet insulated copper wire, 1.5V AA battery, metal paperclips.",
            "steps_sw": "1. Zungusha waya kwa kukazwa mara 30 kuzunguka msumari wa chuma.\n2. Unganisha ncha mbili za waya kwenye betri (+ na -).\n3. Sogelea pini za chuma—msumari utazivuta na kuzishika kama sumaku ya kweli! Ukikata waya, pini zitaanguka mara moja!",
            "steps_en": "1. Wrap insulated wire tightly 30 times around the iron nail.\n2. Connect both stripped wire ends to battery terminals (+ and -).\n3. Touch the nail to paperclips—it becomes an active magnet! Disconnect the wire and the paperclips immediately drop!"
        },
        "quiz": {
            "question_sw": "Ni nini kitakachotokea ukileta Ncha ya Kaskazini (N) ya sumaku moja karibu na Ncha ya Kaskazini (N) ya sumaku ya pili?",
            "question_en": "What happens when you bring the North pole (N) of one magnet near the North pole (N) of another magnet?",
            "options_sw": ["A) Zitasukumana mbali (Repel)", "B) Zitanasiana kwa nguvu", "C) Zitalipuka", "D) Zitakuwa maji"],
            "options_en": ["A) They will repel each other", "B) They will strongly attract", "C) They will explode", "D) They will turn into water"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Kanuni ya sumaku inasema ncha zinazofanana (N-N au S-S) husukumana mbali, wakati ncha tofauti (N-S) huvutana.",
            "explanation_en": "Spot on! The fundamental law of magnetism states that like poles repel, while opposite poles attract."
        }
    },
    {
        "id": "pressure_fluids_hydraulics",
        "title_en": "Pressure in Solids & Liquids: Hydraulics",
        "title_sw": "Shinikizo katika Vitu Vigumu na Vimiminika (Hydraulics)",
        "subject": "Physics",
        "cbc_strand": "Forces & Pressure (Grade 7/8 Integrated Science)",
        "summary_en": "Pressure is force per unit area (P = F/A). In liquids, pressure acts equally in all directions and increases with depth, enabling hydraulic lifts and brakes.",
        "summary_sw": "Shinikizo ni kiasi cha nguvu inayotumika kwenye eneo maalum (P = Nguvu / Eneo). Kwenye vimiminika, shinikizo husambaa sawa pande zote na huwezesha breki na jeki za haidroliki (Hydraulics).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika penseli yenye ncha kali mkononi mwako. Bonyeza ncha kali kwenye kiganja kimoja na sehemu bapa ya nyuma kwenye kiganja cha pili kwa nguvu ileile. Ncha kali inauma zaidi kwa sababu eneo lake ni dogo sana na hivyo inazalisha Shinikizo Kubwa (High Pressure)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kukanyaga Breki ya Gari] ➔ [Maji/Mafuta yanasukuma bastola kwa nguvu / Hydraulics] ➔ [Magurudumu yanasimama papo hapo].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria unapozama chini ya maji kuogelea, masikio yako yanahisi mgandamizo mkubwa kwa sababu shinikizo la maji huongezeka kadri unavyozama chini zaidi!",
                "analogy_en": "Diving deep into Lake Victoria, your eardrums feel compression because fluid hydrostatic pressure increases directly with water depth!"
            },
            "coastal": {
                "analogy_sw": "Pwani, gereji za magari hutumia jeki za mafuta (Hydraulic Car Lifts) ambapo kijana anasukuma pampu ndogo ya mafuta na kunyanyua lori zima la tani tatu angani!",
                "analogy_en": "In coastal auto garages, hydraulic lifts use Pascal's principle: applying a small force on a narrow piston lifts a multi-ton lorry on a wide piston!"
            },
            "highlands": {
                "analogy_sw": "Kwenye mabwawa ya umeme ya milimani kama Bwawa la Masinga, kuta za bwawa hujengwa zikiwa nene sana chini kuliko juu ili kustahimili shinikizo kubwa la maji ya chini!",
                "analogy_en": "At highland hydroelectric dams like Masinga, dam concrete walls are engineered dramatically thicker at the base to withstand immense deep-water pressure!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame ya mchanga, ngamia ana miguu yenye nyayo pana sana ili kupunguza shinikizo ardhini (Low Pressure) na kuzuia miguu isizame mchangani!",
                "analogy_en": "In sandy desert terrain, camels possess broad flat hooves that distribute body weight across a larger surface area, minimizing ground pressure!"
            },
            "urban": {
                "analogy_sw": "Mtaani, kisu chenye makali makali kinakata nyama na mboga kwa urahisi kwa sababu ncha nyembamba huzalisha shinikizo kubwa sana kwa nguvu ndogo ya mkono!",
                "analogy_en": "In kitchen prep, sharp knives slice effortlessly because the ultra-thin blade edge concentrates hand force into immense local pressure (P = F/A)!"
            }
        },
        "key_terms": [
            {"en": "Pressure Formula (P = F/A)", "sw": "Shinikizo = Nguvu / Eneo (N/m² au Pascals)"},
            {"en": "Fluid Pressure & Depth", "sw": "Shinikizo la Maji (Huongezeka kwa kina)"},
            {"en": "Pascal's Principle (Hydraulics)", "sw": "Kanuni ya Pascal (Shinikizo kusambaa sawa vimiminikani)"},
            {"en": "Atmospheric Pressure", "sw": "Shinikizo la Hewa ya Anga"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Ongezeko la Shinikizo la Maji Kwenye Chupa ya Plastiki",
            "title_en": "Experiment: Three-Hole Water Bottle Depth Pressure Spout Test",
            "materials_sw": "Chupa ya plastiki ya lita 1.5, pini ya kutoboa matundu 3 wima (juu, katikati, chini), maji.",
            "materials_en": "1.5L plastic bottle, pin to puncture 3 vertical holes, water.",
            "steps_sw": "1. Toboa matundu 3 kwenye chupa moja: tundu la juu, la kati, na la chini kabisa.\n2. Jaza chupa maji haraka.\n3. Angalia jinsi maji yanavyotoka: tundu la chini kabisa litarusha maji mbali zaidi kwa sababu lina shinikizo kubwa zaidi la maji ya juu!",
            "steps_en": "1. Puncture three small holes vertically along a plastic bottle (top, middle, bottom).\n2. Fill the bottle rapidly with water.\n3. Observe water jets: the bottom hole squirts water the farthest, proving fluid pressure increases with depth!"
        },
        "quiz": {
            "question_sw": "Kwa nini kisu chenye makali makali hukata vitu kwa urahisi zaidi kuliko kisu butu?",
            "question_en": "Why does a sharp knife cut materials much more easily than a blunt knife?",
            "options_sw": ["A) Makali membamba yana eneo dogo sana linalozalisha Shinikizo Kubwa (High Pressure)", "B) Kina uzito mzito zaidi", "C) Kina joto kali", "D) Kina sumaku"],
            "options_en": ["A) A sharp edge has a tiny surface area producing high pressure (P = F/A)", "B) It is heavier", "C) It is hotter", "D) It is magnetic"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Kwa kuwa Shinikizo = Nguvu / Eneo, eneo dogo sana la makali huzalisha shinikizo kubwa linalokata kwa urahisi.",
            "explanation_en": "Spot on! Because Pressure = Force / Area, reducing the contact surface area drastically multiplies cutting pressure."
        }
    },
    {
        "id": "work_energy_power",
        "title_en": "Work, Energy Forms & Power",
        "title_sw": "Kazi (Work), Aina za Nishati (Energy) na Nguvu (Power)",
        "subject": "Physics",
        "cbc_strand": "Energy & Work Principles (Grade 7/8 Integrated Science)",
        "summary_en": "Work is done when a force moves an object through a distance (Work = Force × Distance, measured in Joules). Energy is the capacity to do work, and Power is the rate of doing work (Watts = Joules/second).",
        "summary_sw": "Kazi hufanyika pale nguvu inapohamisha kitu kwa umbali fulani (Kazi = Nguvu × Umbali katika Joules). Nishati ni uwezo wa kufanya kazi, na Nguvu (Power) ni kasi ya kufanya kazi (Wati).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Nyanyua mfuko wenye vitabu kutoka sakafuni uweke mezani. Umetumia Nguvu ya misuli yako kuvuta mzigo dhidi ya grabiti kwa umbali wa mita moja—umefanya Kazi ya Kimitambo (Mechanical Work) iliyobadilisha nishati ya chakula kuwa nishati ya mahali (Potential Energy)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kusukuma Mzigo Mzito Mbele] ➔ [Kazi = Nguvu × Umbali / Joules] ➔ [Nishati ya Kikemia ➔ Nishati ya Mwendo / Kinetic Energy].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria, maji yaliyoinuka juu kwenye maporomoko yana Nishati ya Uwezo (Potential Energy), yanapoanguka yanabadilika kuwa Nishati ya Mwendo (Kinetic Energy) inayozungusha maturbini ya umeme!",
                "analogy_en": "At high waterfalls near Lake Victoria, elevated water stores gravitational Potential Energy that transforms into Kinetic Energy to spin power turbines!"
            },
            "coastal": {
                "analogy_sw": "Pwani, mawimbi makubwa ya Bahari Hindi yana nguvu kubwa ya nishati ya mwendo (Wave Kinetic Energy) inayoweza kutumiwa kuzalisha umeme safi wa baharini!",
                "analogy_en": "Along coastal ocean shores, rhythmic ocean swells carry immense mechanical kinetic energy convertible into green grid electricity!"
            },
            "highlands": {
                "analogy_sw": "Milimani, wanariadha wanaopanda vilima vya Iten kwa kasi kubwa hutoa Nguvu Kubwa ya Kazi (High Power in Watts) kwa sababu wanafanya kazi nyingi kwa sekunde chache!",
                "analogy_en": "In highland training circuits, sprinters sprinting uphill generate immense mechanical Power (Watts) by expending Joules rapidly!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame ya Turkana, mitambo ya upepo ya Lake Turkana Wind Power inabadilisha nishati ya upepo wa dhoruba kuwa megawati 310 za umeme wa kitaifa!",
                "analogy_en": "At Lake Turkana Wind Power project, fierce desert winds turn turbine blades to generate 310 Megawatts of clean electric power for the nation!"
            },
            "urban": {
                "analogy_sw": "Mtaani, balbu ya LED ya Wati 9 (Watts) inafanya kazi sawa na balbu ya zamani ya Wati 60 huku ikitumia nishati ndogo sana ya umeme kuokoa gharama!",
                "analogy_en": "In city homes, 9-Watt LED bulbs deliver bright illumination while consuming a fraction of the electrical energy (Joules per second) of older bulbs!"
            }
        },
        "key_terms": [
            {"en": "Work Done (Joules)", "sw": "Kazi = Nguvu (N) × Umbali (m)"},
            {"en": "Kinetic Energy (Motion)", "sw": "Nishati ya Mwendo (Kinetic Energy = ½mv²)"},
            {"en": "Potential Energy (Stored)", "sw": "Nishati ya Uwezo (Gravitational Potential = mgh)"},
            {"en": "Power (Watts = Joules/sec)", "sw": "Kasi ya Kazi / Nguvu (Wati)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuhesabu Kazi ya Kunyanyua Chupa ya Maji Mezani",
            "title_en": "Experiment: Calculating Mechanical Work Raising a Water Bottle",
            "materials_sw": "Chupa ya maji ya lita 1 (uzani wake ni takriban Newtons 10), rula ya kupima urefu wa meza (mfano mita 1).",
            "materials_en": "1-liter water bottle (~10 Newtons weight), ruler or tape measure.",
            "steps_sw": "1. Nyanyua chupa ya maji kutoka sakafuni hadi juu ya meza ya mita 1.\n2. Kokotoa: Kazi = Nguvu (10 N) × Umbali (1 m) = 10 Joules!\n3. Hongera! Umefanya kazi ya kiasi cha Joules 10!",
            "steps_en": "1. Lift a 1-liter bottle (~10 N) from the floor to a 1-meter tabletop.\n2. Calculate: Work = 10 N × 1 m = 10 Joules of energy transferred!\n3. You have directly quantified mechanical work!"
        },
        "quiz": {
            "question_sw": "Ikiwa nguvu ya Newtons 20 inatumika kusukuma toroli kwa umbali wa mita 5, kiasi gani cha Kazi (Work) kimefanyika?",
            "question_en": "If a force of 20 Newtons pushes a cart across a distance of 5 meters, how much Work is done?",
            "options_sw": ["A) 100 Joules (20 N × 5 m)", "B) 25 Joules", "C) 4 Joules", "D) 0 Joules"],
            "options_en": ["A) 100 Joules (20 N × 5 m)", "B) 25 Joules", "C) 4 Joules", "D) 0 Joules"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Kazi = Nguvu × Umbali = 20 N × 5 m = 100 Joules.",
            "explanation_en": "Spot on! Work Done = Force × Distance = 20 N × 5 m = 100 Joules."
        }
    },
    {
        "id": "density_floating_sinking",
        "title_en": "Density, Floating & Archimedes Principle",
        "title_sw": "Uzito wa Kadiri (Density), Kuelea na Kanuni ya Archimedes",
        "subject": "Physics",
        "cbc_strand": "Matter & Density Principles (Grade 6/7 Integrated Science)",
        "summary_en": "Density is mass per unit volume (Density = Mass / Volume). Objects float if their density is less than the liquid's density, and sink if greater. Archimedes' principle states upthrust equals weight of displaced fluid.",
        "summary_sw": "Uzito wa kadiri ni kiasi cha masi katika ujazo (Density = Masi / Ujazo). Kitu huelea kikiwa na density ndogo kuliko maji, na huzama kikiwa na density kubwa. Nguvu ya upthrust inalingana na uzito wa maji yaliyosukumwa kando.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika kipande cha mbao kavu mkononi mmoja na jiwe lenye ukubwa uleule mkononi mwingine. Jiwe linahisi zito zaidi kwa sababu chembe zake zimebanana sana (High Density). Ukitupa vyote viwili majini, mbao itaelea juu lakini jiwe litazama chini moja kwa moja!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kuweka Mbao Majini ➔ Inaeleyea Juu] vs [Kuweka Jiwe ➔ Linazama Chini] ➔ [Meli Kubwa ya Chuma inaeleyea kwa sababu ya Ujazo Mkubwa wa Hewa Ndani].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria, mashua kubwa ya mbao au feri ya chuma ya Mbita huelea majini kwa sababu umbo lake pana linasukuma maji mengi kando, na kutengeneza nguvu kubwa ya kusukuma juu (Upthrust)!",
                "analogy_en": "On Lake Victoria, large passenger ferries float despite weighing tons because their hollow hull displaces a massive volume of water, creating immense buoyant upthrust!"
            },
            "coastal": {
                "analogy_sw": "Pwani, kuogelea kwenye maji ya chumvi ya Bahari Hindi ni rahisi zaidi kuliko mtoni kwa sababu maji ya chumvi yana density kubwa zaidi inayokusukuma juu kwa nguvu!",
                "analogy_en": "In coastal marine waters, swimming is easier than in freshwater rivers because dense saline water generates greater buoyant upthrust on the human body!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, wakulima hutenganisha mbegu nzuri za mahindi na mbegu mbovu kwa kuziweka kwenye maji—mbegu zilizooza nyepesi huelea juu na mbegu nzito nzuri huzama chini!",
                "analogy_en": "On highland farms, seed sorting uses water immersion: lightweight hollow damaged seeds float, while dense healthy seeds sink to the bottom!"
            },
            "arid": {
                "analogy_sw": "Kwenye Ziwa Magadi lenye magadi na chumvi nyingi, maji yana density kubwa sana kiasi kwamba magogo na miamba ya magadi huelea juu kama barafu!",
                "analogy_en": "At hyper-saline Lake Magadi, trona brine density is so high that mineral crusts and logs float high above the mineral-rich waters!"
            },
            "urban": {
                "analogy_sw": "Mtaani, baluni za gesi ya Helium hupaa angani zenyewe kwa sababu gesi ya Helium ina density ndogo sana kuliko hewa ya kawaida ya anga!",
                "analogy_en": "In city celebrations, helium party balloons rise into the sky because helium gas is dramatically less dense than ambient atmospheric air!"
            }
        },
        "key_terms": [
            {"en": "Density = Mass / Volume (kg/m³ or g/cm³)", "sw": "Uzito wa Kadiri = Masi / Ujazo"},
            {"en": "Upthrust (Buoyancy Force)", "sw": "Nguvu ya Kusukuma Juu ya Maji (Upthrust)"},
            {"en": "Archimedes' Principle", "sw": "Kanuni ya Archimedes ya Kuelea"},
            {"en": "Hydrometer", "sw": "Kipima Uzito wa Kadiri wa Vimiminika"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kufanya Yai Lielee kwa Kuongeza Chumvi Majini",
            "title_en": "Experiment: The Floating Egg Salt Water Density Test",
            "materials_sw": "Glasi ya maji safi, yai moja bichi, vijiko 4 vya chumvi ya mezani.",
            "materials_en": "Glass of fresh water, one raw egg, 4 tablespoons of table salt.",
            "steps_sw": "1. Weka yai kwenye glasi ya maji safi—yai litazama chini kabisa.\n2. Toa yai, weka vijiko 4 vya chumvi na ukoroge vizuri ili kuongeza density ya maji.\n3. Weka yai tena—sasa yai litaelea juu kabisa ya maji ya chumvi!",
            "steps_en": "1. Place a raw egg in fresh tap water—it sinks to the bottom.\n2. Dissolve 4 spoonfuls of salt to increase fluid density.\n3. Replace the egg—it now floats buoyant at the top!"
        },
        "quiz": {
            "question_sw": "Kwa nini meli kubwa ya chuma yenye uzito wa tani elfu nyingi inaweza kuelea juu ya maji ya bahari bila kuzama?",
            "question_en": "Why does a massive steel cargo ship weighing thousands of tons float on water without sinking?",
            "options_sw": ["A) Umbo lake lina hewa nyingi ndani inayofanya wastani wa density yake kuwa ndogo kuliko maji", "B) Chuma huelea kiasili", "C) Maji hayana kina", "D) Bahari ina sumaku"],
            "options_en": ["A) Its hollow shape encloses air, making its average density lower than water", "B) Steel naturally floats", "C) Water has no depth", "D) The sea is magnetic"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Meli ina vyumba vikubwa vya hewa ndani, hivyo wastani wa density ya meli nzima pamoja na hewa ni ndogo kuliko maji, na inasukuma maji yanayotoa upthrust kubwa.",
            "explanation_en": "Spot on! The hollow hull encloses vast volumes of air, making the vessel's overall average density less than water."
        }
    }
]
