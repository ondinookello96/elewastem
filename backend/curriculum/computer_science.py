"""
ElewaSTEM Curriculum — Computer Science & Digital Technology Modules (8 Topics)
Aligned with KICD (Kenya CBC Junior Secondary Computer Science / Pre-Technical), NERDC (Nigeria), DBE CAPS (South Africa), NaCCA (Ghana).
"""

from typing import List, Dict, Any

COMPUTER_SCIENCE_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "computer_algorithms",
        "title_en": "Computer Algorithms, Logic & Flowcharts",
        "title_sw": "Algoriti za Kompyuta, Mantiki ya Hatua na Michoro ya Mtiririko (Flowcharts)",
        "subject": "Computer Science",
        "cbc_strand": "Computational Thinking & Algorithms (Grade 7-9 Computer Science)",
        "summary_en": "An algorithm is an unambiguous, step-by-step sequence of instructions designed to solve a specific problem or complete a task. Flowcharts represent algorithms visually using standard shapes.",
        "summary_sw": "Algoriti ni mfuatano wa hatua za wazi na zenye mantiki zilizopangwa ili kutatua tatizo au kukamilisha kazi. Michoro ya mtiririko (Flowcharts) huonyesha hatua hizo kwa maumbo ya kijiometria.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria kichocheo cha kupika ugali jikoni: Hatua ya 1: Chemsha maji. Hatua ya 2: Maji yakichemka, ongeza unga kidogo. Hatua ya 3: Koroga na usonge hadi uwe mgumu. Huu mfuatano sahihi wa hatua ndio unaitwa Algoriti katika sayansi ya kompyuta!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Mchoro wa Flowchart: Duaradufu ya Kuanza] ➔ [Mstatili wa Mchakato / Process] ➔ [Umbo la Almasi la Uamuzi / Decision: Ndiyo au Hapana] ➔ [Mwisho].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu, kupika chai tamu ya viungo inahitaji algoriti ya hatua: Washa jiko ➔ Weka maji na maziwa ➔ Ongeza majani na viungo ➔ Chemsha ➔ Chuja ➔ Pakua!",
                "analogy_en": "In lake kitchens, preparing spiced tea requires an exact algorithmic sequence: Ignite stove ➔ Add milk/water ➔ Add tea leaves ➔ Boil ➔ Filter ➔ Serve!"
            },
            "coastal": {
                "analogy_sw": "Pwani, kupika pilau ya sherehe kunafuata algoriti kamili ambapo mpishi hawezi kuweka mchele kabla ya kukaanga vitunguu na viungo vya pilau!",
                "analogy_en": "At the coast, cooking Swahili pilau follows a rigorous sequential algorithm where onions and spices must be caramelized before adding rice!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, kupanda mti hufuata algoriti: Chimba shimo ➔ Weka mbolea ➔ Weka mche ➔ Funika udongo ➔ Mwagilia maji!",
                "analogy_en": "In highland agroforestry, tree planting represents a linear algorithm: Dig hole ➔ Add compost ➔ Place sapling ➔ Refill soil ➔ Water thoroughly!"
            },
            "arid": {
                "analogy_sw": "Kwenye vituo vya kuchota maji kaskazini, algoriti ya uamuzi (Decision Diamond) inatumika: 'Kama ndoo imejaa ➔ Funga mfereji; Kama haijajaa ➔ Endelea kujaza'!",
                "analogy_en": "At automated pastoral water dispensers, a conditional decision branch executes: 'IF bucket full ➔ Close valve; ELSE ➔ Continue pumping'!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mashine ya kutoa pesa ya ATM inafuata algoriti salama: Ingiza Kadi ➔ Andika PIN ➔ Chagua Kiasi ➔ Pesa Zinatoka ➔ Chukua Kadi!",
                "analogy_en": "In urban banking, ATM automated tellers follow a secure deterministic algorithm: Insert Card ➔ Verify PIN ➔ Select Amount ➔ Dispense Cash ➔ Eject Card!"
            }
        },
        "key_terms": [
            {"en": "Algorithm", "sw": "Algoriti (Mfuatano wa hatua za kimantiki)"},
            {"en": "Flowchart Symbols", "sw": "Alama za Flowchart (Kuanza, Mchakato, Uamuzi)"},
            {"en": "Sequencing & Selection (IF/ELSE)", "sw": "Mfuatano na Uteuzi wa Maamuzi"},
            {"en": "Iteration (Loops)", "sw": "Kurudia Hatua (Loops)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuandika Algoriti ya Mchezo wa Kumpiga Chenga 'Roboti' Rafiki Yako",
            "title_en": "Experiment: Human Robot Algorithmic Instruction Game",
            "materials_sw": "Karatasi, kalamu, mwanafunzi mwenzako (roboti).",
            "materials_en": "Paper, pen, partner acting as a robot.",
            "steps_sw": "1. Andika amri 4: 'Piga hatua 2 mbele', 'Geuka kulia nyuzi 90', 'Piga hatua 3 mbele', 'Chukua kitabu'.\n2. Mpe rafiki asome na atekeleze kama kompyuta bila kubadilisha chochote.\n3. Utaona jinsi kompyuta inavyohitaji maagizo sahihi kabisa yasiyo na makosa (No bugs)!",
            "steps_en": "1. Write 4 discrete commands: 'Step forward 2 paces', 'Turn 90 degrees right', 'Step forward 3 paces', 'Pick up pen'.\n2. Have your partner execute the exact commands literally.\n3. Proves computers require unambiguous precision without logic errors!"
        },
        "quiz": {
            "question_sw": "Katika mchoro wa mtiririko wa kompyuta (Flowchart), umbo gani wa kijiometria unaotumika kuwakilisha Maamuzi (Decision: Ndiyo au Hapana)?",
            "question_en": "In standard computer flowcharts, which geometric shape represents a Conditional Decision branch (IF / ELSE)?",
            "options_sw": ["A) Umbo la Almasi (Diamond / Rhombus)", "B) Duaradufu ya Kuanzia", "C) Mstatili wa Kawaida", "D) Mduara"],
            "options_en": ["A) Diamond / Rhombus", "B) Start/End Oval", "C) Process Rectangle", "D) Circle"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Umbo la almasi (Diamond) hutumika kutoa uamuzi wenye majibu mawili: Ndiyo (Yes) au Hapana (No).",
            "explanation_en": "Spot on! The diamond symbol represents a conditional decision point with branching execution paths."
        }
    },
    {
        "id": "binary_data_representation",
        "title_en": "Binary Numbers & Digital Data Representation",
        "title_sw": "Mfumo wa Nambari Mbili (Binary: 0 na 1) na Uhifadhi wa Data",
        "subject": "Computer Science",
        "cbc_strand": "Data Representation & Architecture (Grade 7-9 Computer Science)",
        "summary_en": "Computers process and store all digital data (text, images, music, video) using the Binary system (Base-2), composed exclusively of bits (0 for switch OFF, 1 for switch ON). 8 bits make 1 Byte.",
        "summary_sw": "Kompyuta zote huchakata na kuhifadhi data zote (maandishi, picha, video) kwa kutumia mfumo wa nambari mbili (Binary - 0 na 1), ambapo 0 ni swichi imezimwa na 1 ni swichi imewashwa. Biti 8 huunda Baiti 1 (Byte).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria swichi ya taa ya ukutani: Inapozimwa ni Sifuri (0 / OFF), inapowashwa ni Moja (1 / ON). Mamilioni ya swichi hizi ndogo za umeme (transistors) zikiwashwa na kuzimwa haraka ndani ya kompyuta zinaunda nambari, picha, na maneno yote!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Swichi Imezimwa = 0] vs [Swichi Imewashwa = 1] ➔ [Biti 8 = Baiti 1 / Byte ya Herufi moja].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kama ishara za taa za taa za kuongozea mashua za Dunga Beach (Taa ikiwaka = 1, Taa ikizima = 0) zinazotuma ujumbe ziwani usiku, kompyuta hutumia 0 na 1 kuwasiliana!",
                "analogy_en": "Like maritime lighthouse beacon pulses (Light ON = 1, Light OFF = 0) signaling night boats across Lake Victoria, binary pulses encode all digital data!"
            },
            "coastal": {
                "analogy_sw": "Pwani, nyaya za intaneti za fiber optic zilizopita chini ya Bahari Hindi kule Mombasa husafirisha mamilioni ya miale ya mwanga (Mwanga upo = 1, Mwanga haupo = 0) kwa sekunde!",
                "analogy_en": "Undersea fiber optic cables landing at Mombasa transmit billions of photonic light pulses per second representing binary 1s and 0s!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, kupima uzito wa gunia kwa vizani vya binary: Jiwe la 1kg, 2kg, 4kg, 8kg linaweza kuunda uzito wowote kwa kuchagua mawe yaliyopo (1) au yasiyopo (0)!",
                "analogy_en": "In highland produce weighing, binary balance weights (1kg, 2kg, 4kg, 8kg...) combine uniquely to weigh any integer load via active (1) or inactive (0) weights!"
            },
            "arid": {
                "analogy_sw": "Kwenye nguzo za simu za kaskazini, ujumbe wa SMS wa simu husafirishwa kupitia mawimbi ya redio yaliyobeba msimbo wa binary wa herufi za ujumbe wako!",
                "analogy_en": "Across northern cellular towers, SMS text messages travel encoded as binary ASCII data packets over wireless radio frequencies!"
            },
            "urban": {
                "analogy_sw": "Mtaani, picha ya kamera ya simu (Megapixels) imeundwa na mamilioni ya vitone vidogo vya rangi (pixels) ambavyo kila kimoja kimehifadhiwa kama nambari za binary za rangi nyekundu, kijani na bluu (RGB)!",
                "analogy_en": "In smartphone photography, every image pixel is digitally stored as three 8-bit binary bytes encoding Red, Green, and Blue (RGB) color intensities!"
            }
        },
        "key_terms": [
            {"en": "Bit (Binary Digit: 0 or 1)", "sw": "Biti (Kipimo kidogo kabisa cha data: 0 au 1)"},
            {"en": "Byte (8 Bits = 1 Character)", "sw": "Baiti (Biti 8 zinazounda herufi moja)"},
            {"en": "Kilobyte (KB), Megabyte (MB), Gigabyte (GB)", "sw": "Vipimo vya Ukubwa wa Kumbukumbu"},
            {"en": "ASCII / Unicode Text Encoding", "sw": "Msimbo wa Kubadilisha Herufi kuwa Binary"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuhesabu Nambari 1 hadi 15 kwa Vidole 4 vya Mkono (Binary Counting)",
            "title_en": "Experiment: 4-Finger Binary Counting Power of Two System",
            "materials_sw": "Vidole 4 vya mkono wako wa kulia (Kidole kidogo = 1, cha pete = 2, cha kati = 4, cha shahada = 8).",
            "materials_en": "4 fingers of your hand assigned place values: 1, 2, 4, 8.",
            "steps_sw": "1. Inua kidole kidogo pekee: Nambari 1 (0001).\n2. Inua kidole cha pete pekee: Nambari 2 (0010).\n3. Inua vidole vyote viwili (kidole kidogo + cha pete): Nambari 3 (0011 = 1 + 2).\n4. Inua vidole vyote 4: Nambari 15 (1111 = 8 + 4 + 2 + 1)!",
            "steps_en": "1. Raise pinky finger only: represents 1 (0001).\n2. Raise ring finger only: represents 2 (0010).\n3. Raise both pinky and ring: represents 3 (0011 = 2 + 1).\n4. Raise all 4 fingers: represents 15 (1111 = 8 + 4 + 2 + 1)!"
        },
        "quiz": {
            "question_sw": "Baiti moja (1 Byte) ya kompyuta inaundwa na jumla ya Biti (Bits) ngapi za binary?",
            "question_en": "How many binary Bits are grouped together to form one Byte in computer memory?",
            "options_sw": ["A) Biti 8 (8 Bits = 1 Byte)", "B) Biti 2", "C) Biti 100", "D) Biti 1000"],
            "options_en": ["A) 8 Bits", "B) 2 Bits", "C) 100 Bits", "D) 1000 Bits"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Biti 8 zikiunganishwa pamoja zinaunda Baiti 1 (Byte) inayotosha kuhifadhi herufi moja kama 'A'.",
            "explanation_en": "Spot on! 8 binary bits make 1 byte, representing 256 unique character states (2⁸)."
        }
    },
    {
        "id": "logic_gates_circuits",
        "title_en": "Logic Gates: AND, OR, NOT & Truth Tables",
        "title_sw": "Milango ya Mantiki (Logic Gates: AND, OR, NOT) na Majedwali ya Ukweli",
        "subject": "Computer Science",
        "cbc_strand": "Digital Electronics & Logic (Grade 8/9 Computer Science)",
        "summary_en": "Logic gates are the fundamental digital building blocks of computer processors: AND gate outputs 1 only if ALL inputs are 1; OR gate outputs 1 if AT LEAST ONE input is 1; NOT gate inverts input (0➔1, 1➔0).",
        "summary_sw": "Milango ya mantiki ni vitengo vya msingi vya kielektroniki ndani ya processor ya kompyuta: Mlango wa AND hutoa 1 pale milango yote ikiwa 1; Mlango wa OR hutoa 1 kukiwa na angalau 1 moja; Mlango wa NOT hugeuza (0 kuwa 1 na 1 kuwa 0).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria mlango wa benki wenye kufuli mbili: Unahitaji ufunguo wa Mlinzi NA (AND) ufunguo wa Meneja ili mlango ufunguke (AND Gate). Lakini taa ya chumba chako inawaka kwa swichi ya mlangoni AU (OR) swichi ya kitandani (OR Gate)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Mlango wa AND: 1 na 1 = 1] ➔ [Mlango wa OR: 1 au 0 = 1] ➔ [Mlango wa NOT: 0 ➔ 1].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu, mashua ya injini ya petroli inawaka pale tu mafuta yapo (1) NA (AND) ufunguo umewashwa (1)!",
                "analogy_en": "On Lake Victoria, an outboard motor starts only when fuel is available (1) AND the ignition switch is turned (1) — an AND gate logic!"
            },
            "coastal": {
                "analogy_sw": "Pwani, taa ya ulinzi wa nyumba inawaka kama kuna mtu anayepita (1) AU (OR) swichi ya mwongozo imebonyezwa (1) — huu ni mfano wa OR Gate!",
                "analogy_en": "At coastal residences, perimeter security floodlights activate if motion sensors trigger (1) OR the manual override switch is pressed (1) — an OR gate logic!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, mfumo wa kumwagilia maji shambani (Smart Irrigation) unawasha pampu pale tu udongo unapokuwa mkavu (NOT wet)!",
                "analogy_en": "In automated highland greenhouse irrigation, watering valves open when soil moisture sensor is NOT wet (inverted NOT logic)!"
            },
            "arid": {
                "analogy_sw": "Kwenye vituo vya nishati ya jua, chaja inalinda betri kwa kuzima mtiririko pale betri inapokuwa imejaa (NOT overcharging)!",
                "analogy_en": "In solar battery charging controllers, circuit breakers disconnect charging when voltage is NOT within safe thresholds!"
            },
            "urban": {
                "analogy_sw": "Mtaani, kengele ya mlango wa duka inalia pale kengele imewashwa (1) NA (AND) mlango umefunguliwa (1)!",
                "analogy_en": "In urban retail shops, security door alarms sound if the system is armed (1) AND the door magnetic reed sensor breaks (1)!"
            }
        },
        "key_terms": [
            {"en": "AND Gate (Both inputs 1 = Output 1)", "sw": "Mlango wa AND (Zote lazima ziwe 1)"},
            {"en": "OR Gate (Either input 1 = Output 1)", "sw": "Mlango wa OR (Angalau moja iwe 1)"},
            {"en": "NOT Gate (Inverter: 0➔1, 1➔0)", "sw": "Mlango wa NOT (Hugeuza thamani)"},
            {"en": "Truth Table", "sw": "Jedwali la Ukweli (Truth Table)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuunda Saketi ya Swichi Mbili Kuiga Mlango wa AND na OR",
            "title_en": "Experiment: Two-Switch Circuit Modeling AND vs OR Logic",
            "materials_sw": "Betri ya 1.5V, balbu ndogo, swichi 2 ndogo za waya.",
            "materials_en": "1.5V battery, small bulb, two contact switches.",
            "steps_sw": "1. Unganisha swichi mbili katika mstari mmoja (Series): Balbu itawaka pale tu swichi A NA swichi B zikifungwa zote mbili (AND Gate).\n2. Unganisha swichi sambamba (Parallel): Balbu itawaka kama swichi A AU swichi B ikifungwa (OR Gate)!",
            "steps_en": "1. Connect two switches in series: bulb illuminates only when switch A AND switch B are both closed (AND gate).\n2. Connect switches in parallel: bulb illuminates if switch A OR switch B is closed (OR gate)!"
        },
        "quiz": {
            "question_sw": "Kwenye Mlango wa Mantiki wa AND (AND Gate), nini kitakachokuwa tokeo (output) ikiwa ingizo A = 1 na ingizo B = 0?",
            "question_en": "In a digital AND Logic Gate, what will the output be if input A = 1 and input B = 0?",
            "options_sw": ["A) Tokeo ni 0 (AND inahitaji zote ziwe 1)", "B) Tokeo ni 1", "C) Tokeo ni 2", "D) Balbu inalipuka"],
            "options_en": ["A) Output is 0", "B) Output is 1", "C) Output is 2", "D) Circuit burns"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Kwenye mlango wa AND, tokeo linakuwa 1 pale tu maingizo yote mawili yanapokuwa 1 (1 AND 1 = 1). Ikiwa moja ni 0, tokeo ni 0.",
            "explanation_en": "Spot on! An AND gate strictly requires all inputs to be true (1) for the output to be true (1 AND 0 = 0)."
        }
    },
    {
        "id": "programming_python_scratch",
        "title_en": "Computer Programming: Variables, Loops & Conditionals",
        "title_sw": "Utayarishaji wa Programu: Vigeuzi (Variables), Mizunguko (Loops) na Masharti (If/Else)",
        "subject": "Computer Science",
        "cbc_strand": "Computer Programming & Software Development (Grade 7-9 Computer Science)",
        "summary_en": "Programming translates algorithmic logic into executable code (using languages like Scratch or Python). Core concepts include Variables (storing data), Conditionals (if/else decisions), and Loops (repeating code automatically).",
        "summary_sw": "Utayarishaji wa programu hutafsiri mawazo kuwa msimbo unaotekelezwa na kompyuta (kama Scratch au Python). Misingi mikuu ni Vigeuzi (kuhifadhi data), Masharti (if/else), na Mizunguko (loops ya kurudia kazi bila kuchoka).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria sanduku lenye lebo 'alama_za_mwanafunzi = 85' (Hiki ni Kigeuzi / Variable). Kisha amri inasema: 'KAMA alama >= 50: Mwanafunzi amefaulu; LA SIVYO: Rudia mtihani' (Hili ni Sharti / Conditional IF/ELSE)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kizuizi cha Scratch: 'Wakati Kitufe cha Kijani Kinapobonyezwa'] ➔ [Rudia Mara 10 / Loop] ➔ [Kama / If X > 10 Fanya Hivi].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu, kupanga bei ya samaki kwenye programu ya simu hutumia kigeuzi: bei_ya_samaki = 300, kisha kompyuta inazidisha na idadi ya samaki wanaonunuliwa!",
                "analogy_en": "In lake commerce mobile apps, storing product price uses variables: fish_price = 300, multiplied dynamically by quantity purchased!"
            },
            "coastal": {
                "analogy_sw": "Pwani, mfumo wa taa za barabarani hutumia Mzunguko (Loop ya 'while True:') kurudia kuwasha taa usiku na kuzima mchana bila kukoma!",
                "analogy_en": "At coastal municipal traffic intersections, automated signal controllers run infinite while loops cycling green, amber, and red lights!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, programu ya mashine ya kupima majani ya chai hutumia sharti: 'if uzito > 50kg: Chapisha risiti ya mkulima'!",
                "analogy_en": "In highland tea collection centers, digital scales execute conditional logic: 'if weight > 0: record_farmer_delivery()'!"
            },
            "arid": {
                "analogy_sw": "Kwenye vituo vya hali ya hewa vya Garissa, sensor ya mvua inafanya kazi kwa loop: 'Kila dakika 10, rekodi kiwango cha joto na unyevu wa hewa'!",
                "analogy_en": "In automated arid weather stations, sensor logging scripts execute timed periodic loops reading temperature every 10 minutes!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mchezo wa video wa simu au kompyuta hutumia mizunguko (Loops) na masharti (If Statements) kutambua pale gari lako linaposhinda mbio!",
                "analogy_en": "In mobile gaming apps, game engine render loops check frame-by-frame collisions: 'if player_position == finish_line: display_victory()'!"
            }
        },
        "key_terms": [
            {"en": "Variables (Data Containers)", "sw": "Vigeuzi (Kuhifadhi nambari na maneno)"},
            {"en": "Conditionals (IF / ELIF / ELSE)", "sw": "Masharti ya Maamuzi (Kama... Basi)"},
            {"en": "Loops (FOR & WHILE)", "sw": "Mizunguko ya Kurudia Kazi (Loops)"},
            {"en": "Functions (Reusable Code Blocks)", "sw": "Kazi Ndogo za Msimbo (Functions)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuandika Msimbo Rahisi wa Python Kwenye Karatasi",
            "title_en": "Experiment: Paper Python Code Tracing Activity",
            "materials_sw": "Karatasi, penseli.",
            "materials_en": "Paper, pencil.",
            "steps_sw": "1. Andika msimbo huu kwenye karatasi:\n   jina = 'Amina'\n   alama = 80\n   if alama >= 50:\n       print('Hongera', jina)\n2. Fuatilia kwa mkono: Je, alama 80 ni kubwa kuliko 50? Ndiyo!\n3. Tokeo la kompyuta litakuwa: 'Hongera Amina'!",
            "steps_en": "1. Write Python snippet: name = 'Amina'; score = 80; if score >= 50: print('Pass', name).\n2. Trace manually: Is 80 >= 50? True!\n3. Output executes: 'Pass Amina'!"
        },
        "quiz": {
            "question_sw": "Katika programu ya kompyuta, ni neno gani linalotumika kurudia kazi mara 10 bila kuandika msimbo mara 10?",
            "question_en": "In computer programming, which control structure is used to repeat an action multiple times automatically?",
            "options_sw": ["A) Mzunguko (Loop / For / While)", "B) Kuzima kompyuta", "C) Kufuta faili", "D) Kuongeza sauti"],
            "options_en": ["A) Loop (FOR / WHILE)", "B) Shut down", "C) Delete file", "D) Increase volume"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Mzunguko (Loop kama 'for i in range(10):') hurudia kutekeleza maagizo mara 10 kiotomatiki kwa kasi ya ajabu.",
            "explanation_en": "Spot on! Loops (such as FOR and WHILE loops) automate repetitive execution blocks efficiently."
        }
    },
    {
        "id": "computer_hardware_components",
        "title_en": "Computer Hardware: CPU, Memory, Storage & I/O",
        "title_sw": "Vifaa vya Ndani vya Kompyuta: Kichakataji (CPU), Kumbukumbu (RAM), Hifadhi na Pembejeo/Matokeo",
        "subject": "Computer Science",
        "cbc_strand": "Computer Systems & Hardware Architecture (Grade 7-9 Computer Science)",
        "summary_en": "Computer hardware comprises physical electronic components: CPU (the brain executing billions of calculations per second), RAM (fast temporary working memory), Hard Drive/SSD (permanent storage), and I/O peripherals (Keyboard, Monitor, Mouse).",
        "summary_sw": "Vifaa vya kompyuta vinajumuisha sehemu za kielektroniki: Kichakataji kikuu (CPU - ubongo wa kompyuta), Kumbukumbu ya Muda (RAM), Hifadhi ya Kudumu (SSD/Hard Disk), na Vifaa vya Kuingiza na Kutoa Data (Kinanda, Kipanya, Skrini).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika kibodi (Kinanda) na panya (Mouse) mkononi—hivi ni Vifaa vya Kuingiza Taarifa (Input Devices). Spika za sauti na skrini ni Vifaa vya Kutoa Matokeo (Output Devices). Ndani ya sanduku kuna chipu ndogo ya CPU inayofanya kazi kama ubongo!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kinanda & Kipanya ➔ Kuingiza Data] ➔ [CPU inachakata Katikati] ➔ [Skrini & Printa ➔ Kutoa Matokeo].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kama meneja wa soko la samaki la Kisumu anayepokea taarifa za wavuvi (Input), kupiga hesabu kichwani (CPU), na kutoa risiti (Output), CPU ndio ubongo unaoongoza shughuli zote za kompyuta!",
                "analogy_en": "Like a market supervisor receiving fish delivery tallies (Input), computing accounts (CPU), and printing receipts (Output), the CPU orchestrates all computer operations!"
            },
            "coastal": {
                "analogy_sw": "Pwani, kama ghala kubwa la kuhifadhia mizigo ya bandari ya Mombasa (SSD Storage ya kudumu) dhidi ya meza ndogo ya ofisi ya kufanyia kazi ya siku hiyo (RAM ya muda mfupi)!",
                "analogy_en": "At Mombasa port, permanent cargo warehouses represent long-term SSD storage, while the officer's active desk surface represents fast temporary RAM working memory!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, trekta ya kulima inahitaji injini yenye nguvu (CPU) na tangi la mafuta (Power Supply) ili kufanya kazi ya kupanda mbegu!",
                "analogy_en": "On highland farms, a tractor requires a high-performance diesel engine (CPU) and fuel tank (power supply) to drive cultivation implements!"
            },
            "arid": {
                "analogy_sw": "Kwenye vituo vya simu vya jangwani, feni za kupoza (Cooling Fans) hupuliza hewa ili kuzuia CPU na vifaa vya kielektroniki visipate joto jingi!",
                "analogy_en": "In desert telecommunication hubs, heat sinks and cooling fans prevent CPU microprocessors from thermal throttling under high ambient heat!"
            },
            "urban": {
                "analogy_sw": "Mtaani, unaponunua simu janja (Smartphone), unaangalia ukubwa wa RAM (mfano 8GB kwa kasi ya kufungua programu nyingi) na Hifadhi ya Ndani (mfano 128GB ya picha na video)!",
                "analogy_en": "In urban electronics shopping, smartphones specify RAM capacity (e.g. 8GB for multitasking speed) and internal SSD storage (e.g. 128GB for photos and video files)!"
            }
        },
        "key_terms": [
            {"en": "Central Processing Unit (CPU)", "sw": "Kichakataji Kikuu (Ubongo wa kompyuta)"},
            {"en": "Random Access Memory (RAM)", "sw": "Kumbukumbu ya Muda ya Kufanyia Kazi"},
            {"en": "Solid State Drive (SSD) / Storage", "sw": "Hifadhi ya Kudumu ya Faili"},
            {"en": "Input & Output (I/O) Devices", "sw": "Vifaa vya Kuingiza na Kutoa Data"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuainisha Vifaa vya Kompyuta (Input, Output, Storage)",
            "title_en": "Experiment: Computer Hardware Classification Matrix",
            "materials_sw": "Daftari, kalamu, kuangalia vifaa vya simu au kompyuta ya shule.",
            "materials_en": "Notebook, listing everyday digital devices.",
            "steps_sw": "1. Orodhesha vifaa 6: Kinanda, Skrini, Kipanya, Spika, Flash Disk, Kamera.\n2. Weka kila kifaa kwenye safu sahihi: Input (Kinanda, Kipanya, Kamera), Output (Skrini, Spika), Storage (Flash Disk).\n3. Hongera! Umeelewa usanifu wa kompyuta!",
            "steps_en": "1. List 6 devices: Keyboard, Monitor, Mouse, Speaker, Flash Drive, Camera.\n2. Classify into Input (Keyboard, Mouse, Camera), Output (Monitor, Speaker), and Storage (Flash Drive).\n3. You have mapped the von Neumann computer architecture!"
        },
        "quiz": {
            "question_sw": "Ni kiungo kipi cha ndani ya kompyuta kinachoitwa 'Ubongo' kwa sababu kinachakata mahesabu na kutekeleza maagizo yote ya programu?",
            "question_en": "Which hardware component is called the 'Brain' of the computer because it processes all instructions and arithmetic calculations?",
            "options_sw": ["A) Kichakataji Kikuu (CPU)", "B) Kipanya tu", "C) Kifuniko cha plastiki", "D) Waya wa umeme"],
            "options_en": ["A) Central Processing Unit (CPU)", "B) Mouse only", "C) Plastic casing", "D) Power cord"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! CPU (Central Processing Unit) ndio ubongo wa kompyuta unaofanya mabilioni ya mahesabu kwa sekunde moja.",
            "explanation_en": "Spot on! The CPU executes program instructions, performing arithmetic, logic, and control operations."
        }
    },
    {
        "id": "networks_internet_security",
        "title_en": "Computer Networks, Internet & Cybersecurity",
        "title_sw": "Mitandao ya Kompyuta, Mtandao wa Intaneti na Usalama wa Kidijitali (Cybersecurity)",
        "subject": "Computer Science",
        "cbc_strand": "Computer Networks & Digital Citizenship (Grade 7-9 Computer Science)",
        "summary_en": "A computer network connects multiple computing devices to share resources and data. The Internet is a global network of networks communicating via TCP/IP protocols. Cybersecurity protects personal data using passwords, encryption, and safe online practices.",
        "summary_sw": "Mtandao wa kompyuta huunganisha vifaa vingi ili kubadilishana data. Intaneti ni mtandao wa kimataifa unaounganisha dunia nzima. Usalama wa kidijitali (Cybersecurity) hulinda data za siri kwa manenosiri thabiti na tahadhari dhidi ya walaghai wa mtandaoni.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria mtandao wa barabara unaounganisha miji yote ya nchi. Kila nyumba ina Anwani ya Posta (kama Anwani ya IP ya kompyuta). Unapotuma barua pepe, inasafiri kupitia mtandao wa nyaya na kufika moja kwa moja kwa mpokeaji!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kompyuta zilizounganishwa na Wi-Fi / Router] ➔ [Dunia Imeunganishwa na Intaneti] ➔ [Kufuli ya Usalama wa Nenosiri Imara / Cybersecurity].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu, mtandao wa Wi-Fi wa shuleni unaunganisha kompyuta za wanafunzi darasani (Local Area Network - LAN) na kuwawezesha kusoma masomo ya STEM pamoja!",
                "analogy_en": "In Kisumu school computer labs, a Local Area Network (LAN) connects all student workstations to shared STEM digital libraries!"
            },
            "coastal": {
                "analogy_sw": "Pwani, nyaya za chini ya bahari (Submarine Fiber Cables) zilizotua Mombasa zinaunganisha Kenya na nchi zote za Afrika na dunia nzima kwa intaneti ya kasi kubwa!",
                "analogy_en": "Undersea fiber optic trunk cables landing at Mombasa link East Africa to global internet backbones at terabit speeds!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, huduma ya M-PESA ya benki ya simu hutumia mtandao salama wa rununu uliosimbwa (Encrypted Mobile Network) ili kulinda pesa za wanakijiji dhidi ya wezi!",
                "analogy_en": "In highland agricultural trade, mobile money platforms utilize end-to-end encrypted cellular networks to secure financial transactions!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo ya kaskazini, mtandao wa satellite wa angani huleta mawasiliano ya intaneti kwenye shule zilizo mbali sana na miji mikuu!",
                "analogy_en": "In remote northern settlements, satellite broadband terminals provide off-grid schools with direct high-speed internet connectivity!"
            },
            "urban": {
                "analogy_sw": "Mtaani, kuweka nenosiri thabiti lenye herufi kubwa, ndogo, nambari na alama (mfano: STEM@2026!) kunalinda akaunti yako isidukuliwe na walaghai (hackers)!",
                "analogy_en": "In urban digital environments, implementing strong complex passwords (combining letters, numbers, and symbols) prevents unauthorized account compromise!"
            }
        },
        "key_terms": [
            {"en": "Local Area Network (LAN) vs WAN", "sw": "Mtandao wa Ndani (LAN) vs Mtandao Mpana (WAN)"},
            {"en": "IP Address & Web Protocols", "sw": "Anwani ya IP na Itifaki za Mtandao (HTTP/HTTPS)"},
            {"en": "Cybersecurity & Passwords", "sw": "Usalama wa Mtandao na Manenosiri Thabiti"},
            {"en": "Phishing & Online Scams", "sw": "Ulaghai wa Mtandaoni (Phishing)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuangalia Anwani ya Tovuti Salama (HTTPS yenye Kufuli)",
            "title_en": "Experiment: Inspecting Secure Browser HTTPS Padlocks",
            "materials_sw": "Kivinjari cha simu au kompyuta.",
            "materials_en": "Web browser.",
            "steps_sw": "1. Fungua tovuti ya shule au benki.\n2. Angalia juu kwenye anwani ya tovuti—utaona herufi 'https://' na alama ya Kufuli (🔒).\n3. Kufuli inathibitisha kuwa data zote zimesimbwa (Encrypted) kwa usalama na haziwezi kuibwa njiani!",
            "steps_en": "1. Open any secure educational or banking website.\n2. Examine the address bar: observe 'https://' and a green padlock icon.\n3. The padlock verifies that data in transit is cryptographically encrypted against interception!"
        },
        "quiz": {
            "question_sw": "Ni kipi kati ya vifuatavyo ni nenosiri thabiti na salama zaidi la kulinda akaunti yako ya kompyuta dhidi ya walaghai?",
            "question_en": "Which of the following represents the strongest and most secure password to protect an account?",
            "options_sw": ["A) El&wa#STEM2026! (Mchanganyiko wa herufi, nambari na alama)", "B) 123456", "C) jina langu", "D) password"],
            "options_en": ["A) El&wa#STEM2026! (Complex symbols, numbers, upper/lower case)", "B) 123456", "C) myname", "D) password"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Nenosiri thabiti linapaswa kuwa na herufi kubwa, ndogo, nambari na alama maalum ili kuzuia mtu asilibashiri kirahisi.",
            "explanation_en": "Spot on! Strong passwords incorporate upper/lowercase letters, numerals, and special characters with sufficient length."
        }
    },
    {
        "id": "ai_machine_learning_concepts",
        "title_en": "Artificial Intelligence & Machine Learning Basics",
        "title_sw": "Akili Unde (Artificial Intelligence / AI) na Mafunzo ya Mashine",
        "subject": "Computer Science",
        "cbc_strand": "Emerging Technologies & Artificial Intelligence (Grade 8/9 Computer Science)",
        "summary_en": "Artificial Intelligence (AI) enables computer systems to perform tasks that typically require human intelligence, such as visual perception, speech recognition, language translation, and decision-making by learning from vast datasets.",
        "summary_sw": "Akili Unde (AI) huwezesha mifumo ya kompyuta kufanya kazi zinazohitaji akili ya kibinadamu, kama vile kutambua sauti, kutafsiri lugha za Kiafrika, kutambua picha, na kufundisha masomo ya STEM kupitia mifumo ya kujifunza (Machine Learning).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Unapoongea na ElewaSTEM kwa Kiswahili au lugha yako ya kienyeji na ikakujibu mara moja kwa sauti nzuri, hiyo ni Akili Unde (AI) inayotumia mtandao wa neva wa kompyuta kutambua sauti yako na kukupa maelezo sahihi ya sayansi!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Mwanadamu anafundisha Kompyuta kwa Mifano 1,000 ya Picha za Magonjwa ya Mimea] ➔ [Kompyuta Inajifunza / Machine Learning] ➔ [AI inatambua Mmea Mgonjwa Papo Hapo].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu, wakulima hutumia programu ya AI ya simu inayopiga picha jani la muhogo na kutambua papo hapo kama mmea una ugonjwa wa Cassava Mosaic Virus kwa kutumia mifano iliyofundishwa!",
                "analogy_en": "In Kisumu agricultural trials, farmers use AI smartphone apps that photograph cassava leaves to instantly diagnose mosaic virus infections using computer vision models!"
            },
            "coastal": {
                "analogy_sw": "Pwani, watafiti wa Bahari Hindi hutumia roboti za AI zinazoogelea chini ya maji kutambua spishi za samaki na kuchunguza afya ya miamba ya matumbawe!",
                "analogy_en": "Along coastal coral reefs, marine scientists deploy autonomous AI underwater drones to classify fish species and assess reef ecosystem biodiversity!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, ndege zisizo na rubani (Drones za AI) huruka juu ya mashamba ya chai na mahindi kukadiria mavuno na kugundua sehemu zenye uhaba wa maji!",
                "analogy_en": "In highland estates, agricultural AI drones capture multispectral imagery to map crop vigor and forecast harvest yields automatically!"
            },
            "arid": {
                "analogy_sw": "Kwenye hifadhi za wanyama za kaskazini, kamera za AI za infrared hutambua na kuhesabu simba, tembo na wanyama walio hatarini kutoweka hata wakati wa giza la usiku!",
                "analogy_en": "In northern wildlife conservancies, automated AI camera traps identify and monitor endangered elephant and rhino herds in total nocturnal darkness!"
            },
            "urban": {
                "analogy_sw": "Mtaani, programu ya ElewaSTEM unayoitumia sasa inatumia Akili Unde (AI) kukufundisha sayansi kwa lugha 17 za Kiafrika na kukupa mifano halisi ya nyumbani!",
                "analogy_en": "In modern digital education, ElewaSTEM's agentic AI adapts real-time Socratic pedagogy across 17 African languages grounded in regional ecosystems!"
            }
        },
        "key_terms": [
            {"en": "Artificial Intelligence (AI)", "sw": "Akili Unde (Mifumo ya kompyuta inayofikiri na kujifunza)"},
            {"en": "Machine Learning (ML)", "sw": "Kujifunza kwa Mashine (Kupitia mifano ya data)"},
            {"en": "Natural Language Processing (NLP)", "sw": "Uchakataji wa Lugha za Asili (Kama Kiswahili, Yoruba, Hausa)"},
            {"en": "Computer Vision & Robotics", "sw": "Uwezo wa Kompyuta Kuona Picha na Roboti"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kufundisha 'Akili Unde' ya Darasani Kutambua Maembe dhidi ya Machungwa",
            "title_en": "Experiment: Manual Machine Learning Training Set Simulation",
            "materials_sw": "Karatasi, penseli.",
            "materials_en": "Paper, pencil.",
            "steps_sw": "1. Andika sifa 3 za Embe (Umbo la yai, ncha kali, rangi ya kijani/manjano) na sifa 3 za Chungwa (Duara kamili, ngozi yenye vinyweleo, rangi ya machungwa).\n2. Mpe rafiki sifa ya siri: 'Kitu chenye duara kamili na ngozi ya vinyweleo'.\n3. Rafiki anayetumia sheria zako za AI atatambua mara moja: 'Hili ni Chungwa!'",
            "steps_en": "1. Define features: Mango (oval, smooth skin) vs Orange (spherical, textured rind).\n2. Provide test input: 'Spherical object with textured rind'.\n3. Your simulated machine learning classifier correctly predicts: 'Orange'!"
        },
        "quiz": {
            "question_sw": "Ni tawi gani la Sayansi ya Kompyuta linalowezesha mashine kujifunza kutoka kwenye mifano ya data na kufanya maamuzi kama binadamu?",
            "question_en": "Which branch of Computer Science enables machines to learn patterns from datasets and make intelligent predictions?",
            "options_sw": ["A) Akili Unde na Mafunzo ya Mashine (AI & Machine Learning)", "B) Kuzima kompyuta", "C) Kufagia sakafu", "D) Kuosha vyombo"],
            "options_en": ["A) Artificial Intelligence & Machine Learning", "B) Powering off", "C) Sweeping floor", "D) Washing dishes"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Akili Unde (AI) na Machine Learning ndizo zinazowezesha kompyuta kujifunza, kutambua picha, na kuongea lugha mbalimbali.",
            "explanation_en": "Spot on! Artificial Intelligence and Machine Learning train algorithms to recognize complex patterns and make intelligent inferences."
        }
    },
    {
        "id": "databases_information_systems",
        "title_en": "Databases, Relational Tables & Data Storage",
        "title_sw": "Mifumo ya Kuhifadhi Data (Databases), Majedwali na Taarifa",
        "subject": "Computer Science",
        "cbc_strand": "Data Management & Information Systems (Grade 8/9 Computer Science)",
        "summary_en": "A database is an organized, searchable digital collection of structured data. Relational databases store data in tables (Rows/Records and Columns/Fields) linked by Primary Keys, queried using SQL.",
        "summary_sw": "Hifadhidata (Database) ni mfumo uliopangwa kidijitali wa kuhifadhi na kutafuta taarifa kwa urahisi. Hifadhidata ya majedwali (Relational Database) huhifadhi data kwenye safu mlalo (Records) na safu wima (Fields) zenye nambari ya kipekee ya kitambulisho (Primary Key).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria kabati kubwa la mafaili ya shule lenye droo zilizopangwa kwa herufi: Droo ya 'Wanafunzi' ina faili la kila mwanafunzi lenye Jina, Tarehe ya Kuzaliwa, na Nambari ya Usajili (Admission Number / Primary Key). Huu ndio muundo wa Hifadhidata (Database)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kabati la Mafaili ya Shule] ➔ [Jedwali la Kompyuta lenye Safu Mlalo na Wima] ➔ [Kutafuta Taarifa ya Mwanafunzi kwa Sekunde 1].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu hospitalini (JOOTRH), hifadhidata ya kidijitali huhifadhi rekodi za wagonjwa na matibabu yao ili daktari akitafuta jina la mgonjwa aone historia yote ya matibabu papo hapo!",
                "analogy_en": "At Kisumu teaching hospital, electronic health databases index patient records by national ID, retrieving complete diagnostic histories within seconds!"
            },
            "coastal": {
                "analogy_sw": "Pwani kule Mamlaka ya Bandari ya Mombasa (KPA), hifadhidata kubwa hufuatilia makontena elfu hamsini: Nambari ya Kontena, Meli iliyoleta, Uzito, na Mahali lilipo bandarini!",
                "analogy_en": "At the Port of Mombasa, enterprise relational databases track tens of thousands of shipping containers: Container ID, Vessel, Origin, Weight, and Yard Location!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, chama cha ushirika cha wakulima wa chai cha KTDA hutumia hifadhidata kurekodi kilo za majani ya chai alizoleta kila mkulima ili kumlipa kwa usahihi mwisho wa mwezi!",
                "analogy_en": "In highland tea cooperatives, member databases record daily farmer harvest weights to calculate accurate monthly bonus payments automatically!"
            },
            "arid": {
                "analogy_sw": "Kwenye vituo vya usajili wa mifugo kaskazini, hifadhidata ya nambari za hereni za ng'ombe (Ear-tag numbers) husaidia kufuatilia chanjo na kuzuia wizi wa mifugo!",
                "analogy_en": "In pastoral livestock registration, digital database registries tag individual cattle with RFID identifiers to track veterinary vaccination records!"
            },
            "urban": {
                "analogy_sw": "Mtaani, duka kuu la 'Supermarket' linapotumia mashine ya kusoma barcode (Barcode Scanner), hifadhidata inatafuta bei ya bidhaa na kupunguza idadi ya bidhaa zilizobaki rafunzi mara moja!",
                "analogy_en": "In urban retail supermarkets, point-of-sale barcode scanners query product inventory databases, instantly retrieving prices and updating stock quantities!"
            }
        },
        "key_terms": [
            {"en": "Database (Structured Data)", "sw": "Hifadhidata (Mfumo wa kidijitali wa kuhifadhi data)"},
            {"en": "Table (Rows/Records & Columns/Fields)", "sw": "Jedwali (Safu Mlalo za Taarifa & Safu Wima)"},
            {"en": "Primary Key (Unique ID)", "sw": "Nambari ya Kipekee ya Utambulisho (Primary Key)"},
            {"en": "Query (Searching Data via SQL)", "sw": "Kutafuta Taarifa (Query)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuchora Jedwali la Hifadhidata ya Wanafunzi wa Darasa Lako",
            "title_en": "Experiment: Classroom Student Database Table Schema Design",
            "materials_sw": "Karatasi, rula, kalamu.",
            "materials_en": "Paper, ruler, pen.",
            "steps_sw": "1. Chora jedwali lenye safu wima 4: Nambari_ya_Usajili (Primary Key), Jina_la_Mwanafunzi, Somo_Analopenda, Klabu_ya_Shule.\n2. Jaza taarifa za wanafunzi 3 kwenye safu mlalo (Records).\n3. Hongera! Umetengeneza muundo kamili wa Hifadhidata (Database Schema)!",
            "steps_en": "1. Draw a table with 4 column fields: Student_ID (Primary Key), Name, Favorite_STEM_Subject, Club.\n2. Populate 3 student rows (records).\n3. You have architected a relational database table schema!"
        },
        "quiz": {
            "question_sw": "Katika jedwali la hifadhidata (database table), ni safu ipi ya kipekee inayotumiwa kuhakikisha kila taarifa (record) inatambulika bila kuchanganywa na nyingine?",
            "question_en": "In a relational database table, what unique identifier field ensures every record is distinguished without duplication?",
            "options_sw": ["A) Nambari ya Kipekee ya Utambulisho (Primary Key)", "B) Rangi ya jedwali", "C) Saizi ya herufi", "D) Jina la kompyuta"],
            "options_en": ["A) Primary Key", "B) Table color", "C) Font size", "D) Computer name"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Nambari ya Utambulisho ya Kipekee (Primary Key kama Nambari ya Kitambulisho au Nambari ya Usajili) huhakikisha kila taarifa ni ya kipekee.",
            "explanation_en": "Spot on! A Primary Key is a unique database attribute that uniquely identifies each individual record in a relational table."
        }
    }
]
