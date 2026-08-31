"""
ElewaSTEM Curriculum — Mathematics Learning Modules (10 Topics)
Aligned with KICD (Kenya CBC Grades 4-9), NERDC (Nigeria), DBE CAPS (South Africa), NaCCA (Ghana).
"""

from typing import List, Dict, Any

MATHEMATICS_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "fractions_math",
        "title_en": "Fractions, Decimals & Percentages",
        "title_sw": "Sehemu za Nambari (Fractions), Desimali na Asilimia (%)",
        "subject": "Mathematics",
        "cbc_strand": "Numbers & Operations (Grade 4-7 Mathematics)",
        "summary_en": "A fraction represents equal parts of a whole (Numerator/Denominator). Fractions easily convert into decimals (1/2 = 0.5) and percentages (1/2 = 50%).",
        "summary_sw": "Sehemu huwakilisha vipande sawa vya kitu kizima (Kiasi / Jumla). Sehemu hubadilishwa kuwa desimali (1/2 = 0.5) na asilimia (1/2 = 50%).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika chapati nzima (1). Ikate katikati sawa—sasa una nusu mbili (1/2 na 1/2). Kata kila nusu tena mara mbili—sasa una robo nne sawa (1/4 kila moja). Ukila vipande 2 kati ya 4, umekula nusu ya chapati nzima (2/4 = 1/2 au 50%)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Chapati 1 Nzima] ➔ [Kukata Katikati = 1/2 + 1/2] ➔ [Kukata Vipande 4 = 1/4 kila kimoja] ➔ [1/2 = 0.5 = 50%].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu sokoni Kibuye unapouza kikapu chenye ndoo 4 za samaki Ngege: ukiuza ndoo 3, umeuza sehemu ya tatu ya nne (3/4 au 75%) ya samaki wako!",
                "analogy_en": "In Kibuye market in Kisumu, selling 3 baskets out of 4 total fish baskets means you sold three-quarters (3/4 = 75%) of your stock!"
            },
            "coastal": {
                "analogy_sw": "Pwani, mnunuzi anaponunua nazi 10 na 5 kati ya hizo ni nazi kavu, asilimia 50% (5/10 = 1/2) ya nazi zote ni kavu!",
                "analogy_en": "At coastal markets, having 5 mature coconuts out of a batch of 10 represents exactly 50% (5/10 = 1/2) of the harvest!"
            },
            "highlands": {
                "analogy_sw": "Mashambani kule Nyandarua, mkulima anapovuna magunia 100 ya viazi na kugawa magunia 25 kwa majirani, ametoa robo moja (1/4 = 25%) ya mavuno yake yote!",
                "analogy_en": "In Nyandarua potato farms, sharing 25 bags out of a 100-bag harvest represents donating exactly one-quarter (1/4 = 25%) of total yields!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo ya wafugaji, kama ndoo 10 za maziwa zikikamuliwa na ndoo 8 zikauzwa sokoni, ndoo 8/10 (asilimia 80%) zimeleta mapato ya familia!",
                "analogy_en": "In pastoral communities, selling 8 buckets out of 10 buckets of camel milk represents commercializing 80% (8/10 = 0.8) of the morning dairy!"
            },
            "urban": {
                "analogy_sw": "Mtaani, unaponunua vocha ya simu ya shilingi 100 na kutumia shilingi 50 kupiga simu, umetumia asilimia 50% (0.50) ya salio lako!",
                "analogy_en": "In mobile banking, spending 50 shillings out of 100 airtime balance consumes exactly 50% (0.50) of total phone credit!"
            }
        },
        "key_terms": [
            {"en": "Numerator & Denominator", "sw": "Kiasi cha Juu (Numerator) & Jumla ya Chini (Denominator)"},
            {"en": "Equivalent Fractions", "sw": "Sehemu Zenye Thamani Sawa (1/2 = 2/4 = 50/100)"},
            {"en": "Decimals to Percentages", "sw": "Desimali kuwa Asilimia (0.75 = 75%)"},
            {"en": "Simplification", "sw": "Kurahisisha Sehemu kwa Nambari ya Pamoja"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kukunja Karatasi Kuthibitisha Sehemu Sawa",
            "title_en": "Experiment: Paper Folding Equivalent Fraction Proof",
            "materials_sw": "Karatasi moja ya mraba ya A4, kalamu.",
            "materials_en": "One square sheet of paper, pen.",
            "steps_sw": "1. Kunja karatasi katikati mara moja—paka rangi upande mmoja (1/2).\n2. Kunja tena katikati bila kufungua—sasa una mistari 4 na sehemu 2 zimepakwa rangi (2/4).\n3. Ona jinsi 1/2 inavyolingana sawa kabisa na 2/4!",
            "steps_en": "1. Fold a square paper in half once and shade one side (1/2).\n2. Fold in half again before opening—you now have 4 squares with 2 shaded (2/4).\n3. Visually proves 1/2 = 2/4 = 50%!"
        },
        "quiz": {
            "question_sw": "Ikiwa mwanafunzi alipata alama 15 kati ya 20 kwenye mtihani wa hesabu, alipata asilimia (%) ngapi?",
            "question_en": "If a student scores 15 marks out of 20 in a mathematics test, what percentage score did they achieve?",
            "options_sw": ["A) 75% (15/20 × 100%)", "B) 50%", "C) 15%", "D) 35%"],
            "options_en": ["A) 75% (15/20 × 100%)", "B) 50%", "C) 15%", "D) 35%"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! 15 / 20 = 3/4 = 0.75 = 75%.",
            "explanation_en": "Spot on! 15 ÷ 20 = 0.75 = 75%."
        }
    },
    {
        "id": "algebra_math",
        "title_en": "Algebra: Linear Equations & Variables",
        "title_sw": "Aljebra: Milinganyo na Vigeuzi (Variables)",
        "subject": "Mathematics",
        "cbc_strand": "Algebraic Expressions & Equations (Grade 6-9 Mathematics)",
        "summary_en": "Algebra uses letters (variables like x, y) to represent unknown values. Solving linear equations (e.g., 2x + 6 = 14) balances operations on both sides to find the unknown.",
        "summary_sw": "Aljebra hutumia herufi (vigeuzi kama x, y) kuwakilisha nambari zisizojulikana. Kutatua mlinganyo kunafanana na kusawazisha mizani pande zote mbili ili kupata thamani ya x.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria mizani ya kupimia sukari dukani yenye sahani mbili. Sahani ya kushoto ina mfuko usiojulikana (x) pamoja na mawe ya gramu 5. Sahani ya kulia ina mawe ya gramu 15. Mizani iko sawa (x + 5 = 15). Ukiondoa mawe 5 pande zote mbili, mfuko wako x = gramu 10!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Mizani Iliyosawazishwa: x + 5 = 15] ➔ [Kutoa 5 pande zote mbili] ➔ [x = 10].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu sokoni, ukimpa muuzaji wa samaki shilingi 500 na akakurudishia chenji ya shilingi 200 baada ya kununua samaki x: Mlinganyo ni x + 200 = 500, kwa hivyo samaki aligharimu x = shilingi 300!",
                "analogy_en": "In Kisumu fish stalls, paying 500 shillings and receiving 200 change for a fish x creates the linear equation: x + 200 = 500, solving to x = 300 shillings!"
            },
            "coastal": {
                "analogy_sw": "Pwani, kama bei ya nazi 3 ni shilingi 150 (3y = 150), unagawanya 150 kwa 3 pande zote mbili kupata bei ya nazi moja: y = shilingi 50!",
                "analogy_en": "At the coast, if 3 coconuts cost 150 shillings (3y = 150), dividing both sides by 3 reveals the unit price y = 50 shillings!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, mkulima anajua kuwa mizinga miwili ya nyuki ilitoa jumla ya kilo 20 za asali. Kama mzinga wa kwanza ulitoa kilo 8, basi mzinga wa pili ulitoa x ambapo: 8 + x = 20, yaani x = 12 kg!",
                "analogy_en": "In highland beekeeping, if two hives yield 20 kg honey and the first produced 8 kg, the second produced x kg: 8 + x = 20, hence x = 12 kg!"
            },
            "arid": {
                "analogy_sw": "Kwenye mifugo ya kaskazini, jumla ya mbuzi na ngamia ni 50. Kama ngamia ni 15, basi idadi ya mbuzi n inapatikana kwa: n + 15 = 50, n = 35 mbuzi!",
                "analogy_en": "In pastoral herds totaling 50 animals with 15 camels, the number of goats n is solved by: n + 15 = 50, yielding n = 35 goats!"
            },
            "urban": {
                "analogy_sw": "Mtaani, nauli ya matatu kuelekea mjini ikiongezeka mara mbili na kuwa shilingi 160 (2b = 160), nauli ya kawaida ya zamani ilikuwa b = 160 ÷ 2 = shilingi 80!",
                "analogy_en": "In city transit, if peak matatu fare doubles regular fare to 160 shillings (2b = 160), normal fare was b = 160 ÷ 2 = 80 shillings!"
            }
        },
        "key_terms": [
            {"en": "Variable (x, y, a, b)", "sw": "Kigeuzi (Herufi inayowakilisha nambari isiyojulikana)"},
            {"en": "Linear Equation", "sw": "Mlinganyo wa Mstari Mnyoofu (mf. 2x + 4 = 10)"},
            {"en": "Like Terms", "sw": "Nambari Zinazofanana (3x + 2x = 5x)"},
            {"en": "Balancing Equations", "sw": "Kusawazisha Pande Zote za Mlinganyo"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kutatua Mlinganyo kwa Njia ya Sanduku Lililofichwa",
            "title_en": "Experiment: Mystery Matchbox Algebraic Balance Game",
            "materials_sw": "Kikombe kidogo kilichofunikwa (sanduku la x), vibanzi au maharagwe 10.",
            "materials_en": "Opaque cup (box of x), 10 beans.",
            "steps_sw": "1. Weka maharagwe machache ndani ya kikombe bila kumwonyesha rafiki yako (x).\n2. Weka maharagwe 3 wazi kando ya kikombe.\n3. Mwambie rafiki: 'Jumla ya maharagwe yote ni 8' (x + 3 = 8).\n4. Rafiki akitoa 3 kutoka kwenye 8, anajua kikombe kina maharagwe x = 5!",
            "steps_en": "1. Place hidden beans inside an opaque cup (x).\n2. Place 3 beans beside the cup.\n3. State the rule: 'Total beans equal 8' (x + 3 = 8).\n4. Subtracting 3 from 8 proves the cup contains x = 5 beans!"
        },
        "quiz": {
            "question_sw": "Tatua mlinganyo huu kupata thamani ya x: 2x + 4 = 14",
            "question_en": "Solve for the unknown variable x in the equation: 2x + 4 = 14",
            "options_sw": ["A) x = 5 (2x = 10 ➔ x = 5)", "B) x = 10", "C) x = 7", "D) x = 18"],
            "options_en": ["A) x = 5 (2x = 10 ➔ x = 5)", "B) x = 10", "C) x = 7", "D) x = 18"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Toa 4 pande zote mbili: 2x = 10. Gawanya kwa 2: x = 5.",
            "explanation_en": "Spot on! Subtract 4 from both sides: 2x = 10. Divide by 2: x = 5."
        }
    },
    {
        "id": "geometry_shapes_angles",
        "title_en": "Geometry: 2D/3D Shapes, Angles & Polygons",
        "title_sw": "Jiometria: Maumbo ya 2D na 3D, Pembe (Angles) na Poligoni",
        "subject": "Mathematics",
        "cbc_strand": "Geometry & Spatial Sense (Grade 4-8 Mathematics)",
        "summary_en": "Geometry studies shapes, lines, and spatial properties. Angles are classified as Acute (<90°), Right (90°), Obtuse (90°-180°), and Reflex (>180°). The angles in any triangle always add up to 180°.",
        "summary_sw": "Jiometria huchunguza maumbo na pembe. Pembe huainishwa kama Kali (<90°), Mraba (90°), Butu (90°-180°), na Pindu (>180°). Jumla ya pembe zote ndani ya Pembetatu daima ni nyuzi 180°.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika kitabu cha mraba mkononi mwako. Pembe nne za pembeni zimekaa wima kabisa kama herufi L—hizo ni Pembe Mraba za nyuzi 90° (Right Angles). Pembetatu ina pande tatu na pembe tatu zinazojumuika kuwa nyuzi 180°!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Pembe Kali < 90°] ➔ [Pembe Mraba = 90° / Umbo la L] ➔ [Pembe Butu > 90°] ➔ [Pembetatu: Pembe zote = 180°].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu, paa za nyumba za kitamaduni za duara (Round huts) hutumia umbo la Pia (Cone 3D) na kuta za mcheduara (Cylinder 3D) kuzuia upepo wa dhoruba za ziwani!",
                "analogy_en": "In traditional lake homesteads, circular huts combine 3D conical thatched roofs with cylindrical mud walls for structural aerodynamic wind resistance!"
            },
            "coastal": {
                "analogy_sw": "Pwani kule Fort Jesus Mombasa, kuta za ngome ya kale zimejengwa kwa maumbo ya Pembenne na Pembetatu imara zinazosambaza uzito wa mawe ya matumbawe!",
                "analogy_en": "At Fort Jesus in Mombasa, historical fortress battlements incorporate rigid triangular and quadrilateral geometry to support heavy coral stone loads!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, maghala ya kuhifadhi mahindi (Cribs) hujengwa kwa umbo la Mchemraba Bapa (Cuboid 3D) wenye pembe mraba za nyuzi 90° ili kutoshea magunia mengi!",
                "analogy_en": "In highland maize cribs, rectangular cuboid frames with 90-degree right angles maximize internal storage capacity for maize sacks!"
            },
            "arid": {
                "analogy_sw": "Kwenye manyatta za wafugaji wa Maasai na Turkana, miundo ya maumbo ya nusu-tufe (Hemisphere 3D) na duaradufu (Ovals) husambaza joto vizuri!",
                "analogy_en": "In pastoralist manyatta construction, hemispherical curved dome geometries provide maximum volume with minimal perimeter materials!"
            },
            "urban": {
                "analogy_sw": "Mtaani, madaraja ya reli ya SGR na madaraja ya juu ya ghorofa hutumia pembetatu nyingi za chuma (Trusses) kwa sababu pembetatu ndilo umbo gumu zaidi lisiloweza kupinda kirahisi!",
                "analogy_en": "In modern railway bridges, structural engineers use steel triangular trusses because triangles are the most rigid and non-deformable geometric shapes!"
            }
        },
        "key_terms": [
            {"en": "Acute, Right & Obtuse Angles", "sw": "Pembe Kali (<90°), Pembe Mraba (90°), na Pembe Butu (>90°)"},
            {"en": "Triangle Angle Sum = 180°", "sw": "Jumla ya Pembe za Pembetatu = 180°"},
            {"en": "Quadrilateral Angle Sum = 360°", "sw": "Jumla ya Pembe za Pembenne = 360°"},
            {"en": "3D Solids (Cube, Cuboid, Cylinder, Sphere)", "sw": "Maumbo ya 3D (Mchemraba, Mcheduara, Tufe)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kukata Pembe 3 za Pembetatu Kuthibitisha Jumla ni Mstari Mnyoofu (180°)",
            "title_en": "Experiment: Triangle Corner Tearing 180-Degree Proof",
            "materials_sw": "Karatasi moja, mkasi au kuchana kwa mkono, rula.",
            "materials_en": "Sheet of paper, scissors or hand tearing, ruler.",
            "steps_sw": "1. Chora pembetatu yoyote kwenye karatasi na ukate pembe zake 3.\n2. Weka pembe zote 3 zikigusana ncha zake kwenye meza.\n3. Zitaungana na kuunda mstari mnyoofu kabisa wa nyuzi 180°!",
            "steps_en": "1. Draw any triangle and tear off its three corners (angles A, B, C).\n2. Arrange the three vertices adjacent to each other on a flat baseline.\n3. The three angles form a perfect 180-degree straight line!"
        },
        "quiz": {
            "question_sw": "Ikiwa pembe mbili za kwanza za pembetatu ni nyuzi 60° na nyuzi 70°, pembe ya tatu iliyobaki ina ukubwa gani?",
            "question_en": "If two angles of a triangle measure 60° and 70°, what is the measure of the third angle?",
            "options_sw": ["A) 50° (180° - 130° = 50°)", "B) 90°", "C) 130°", "D) 180°"],
            "options_en": ["A) 50° (180° - 130° = 50°)", "B) 90°", "C) 130°", "D) 180°"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Jumla ya pembe za pembetatu ni 180°. 60° + 70° = 130°. Pembe ya tatu = 180° - 130° = 50°.",
            "explanation_en": "Spot on! Sum of triangle angles = 180°. Third angle = 180° - (60° + 70°) = 50°."
        }
    },
    {
        "id": "ratios_proportions_rates",
        "title_en": "Ratios, Proportions & Scale Rates",
        "title_sw": "Uwiano (Ratios), Uwiano Linganifu (Proportions) na Viwango vya Kasi (Rates)",
        "subject": "Mathematics",
        "cbc_strand": "Numbers & Proportional Reasoning (Grade 6-8 Mathematics)",
        "summary_en": "A ratio compares quantities of the same kind (e.g., 2:3). A proportion states that two ratios are equal (a/b = c/d). Rates compare quantities of different units (e.g., Speed = km/h).",
        "summary_sw": "Uwiano hulinganisha idadi ya vitu vya aina moja (mfano 2:3). Uwiano linganifu unathibitisha usawa wa uwiano mbili. Viwango (Rates) hulinganisha vitu vyenye vipimo tofauti (mfano Kasi = km/saa).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika glasi ya juisi mkononi mwako. Kutengeneza juisi tamu ya kupoa, mama anaweka glasi 1 ya sharubati kwa glasi 3 za maji (Uwiano wa 1:3). Ukiongeza glasi 2 za sharubati, lazima uweke glasi 6 za maji (Uwiano Linganifu wa 2:6 = 1:3)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Sharubati 1 : Maji 3] ➔ [Gari linasafiri km 60 kwa Saa 1 / Kasi = km/h].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu unapotengeneza mchanganyiko wa saruji ya ujenzi: uwiano wa mfuko 1 wa saruji kwa toroli 3 za mchanga (1:3) hutoa zege imara isiyovunjika!",
                "analogy_en": "In Kisumu masonry, standard construction mortar mixes 1 bag of cement to 3 wheelbarrows of sand (1:3 ratio) for optimal structural strength!"
            },
            "coastal": {
                "analogy_sw": "Pwani, kupika wali wa nazi mtamu kunahitaji uwiano wa vikombe 2 vya mchele kwa vikombe 3 vya tui la nazi (2:3)!",
                "analogy_en": "In coastal Swahili culinary tradition, perfect coconut rice uses a fixed volumetric ratio of 2 cups rice to 3 cups coconut milk (2:3)!"
            },
            "highlands": {
                "analogy_sw": "Mashambani kule Nakuru, gari linalosafiri kutoka Nakuru hadi Naivasha (umbali wa km 80) kwa muda wa saa 1 lina Kasi ya Wastani (Rate of Speed) ya km 80 kwa saa (80 km/h)!",
                "analogy_en": "In highland highway transport, driving 80 km between Nakuru and Naivasha in 1 hour corresponds to an average rate of speed of 80 km/h!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame ya kaskazini, uwiano wa mbuzi wa dume kwa majike katika kundi la ufugaji ni dume 1 kwa majike 20 (1:20) ili kuhakikisha uzazi bora!",
                "analogy_en": "In pastoral herd management, maintaining a breeding ratio of 1 breeding buck to 20 doe goats (1:20) guarantees sustainable herd reproduction!"
            },
            "urban": {
                "analogy_sw": "Mtaani, ramani ya ramani ya jiji (Map Scale) inatumia kipimo cha sentimita 1 kwenye karatasi kuwakilisha mita 100 ardhini (1 : 10,000)!",
                "analogy_en": "In urban city planning maps, a scale ratio of 1 cm on paper represents 100 meters on the ground (1:10,000 ratio scale)!"
            }
        },
        "key_terms": [
            {"en": "Ratio (a:b)", "sw": "Uwiano (Ulinganisho wa nambari mbili)"},
            {"en": "Direct Proportion", "sw": "Uwiano wa Moja kwa Moja (Kimoja kikiongezeka, kingine kinaongezeka)"},
            {"en": "Inverse Proportion", "sw": "Uwiano Kinyume (Wafanyakazi wengi ➔ Siku chache za kazi)"},
            {"en": "Rate of Speed (Distance / Time)", "sw": "Kasi = Umbali / Muda (km/h au m/s)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuhesabu Uwiano wa Wanafunzi Wavulana kwa Wasichana Darasani",
            "title_en": "Experiment: Classroom Gender & Object Ratio Survey",
            "materials_sw": "Daftari, kuhesabu idadi ya kalamu za bluu na nyekundu kwenye dawati.",
            "materials_en": "Notebook, counting blue vs red pens.",
            "steps_sw": "1. Hesabu kalamu za bluu (mf. 6) na kalamu za nyekundu (mf. 2).\n2. Andika uwiano: 6:2.\n3. Gawanya kwa 2 pande zote: Uwiano rahisi ni 3:1 (Kila kalamu 3 za bluu kuna kalamu 1 ya nyekundu)!",
            "steps_en": "1. Count 6 blue pens and 2 red pens.\n2. Express as a ratio: 6:2.\n3. Divide by greatest common divisor (2) to simplify: 3:1 ratio!"
        },
        "quiz": {
            "question_sw": "Gari lilisafiri umbali wa kilomita 180 kwa muda wa saa 3. Kasi ya wastani ya gari hilo ilikuwa ngapi?",
            "question_en": "A bus travels a distance of 180 kilometers in 3 hours. What is the average speed rate of the bus?",
            "options_sw": ["A) 60 km/h (180 ÷ 3)", "B) 180 km/h", "C) 540 km/h", "D) 30 km/h"],
            "options_en": ["A) 60 km/h (180 ÷ 3)", "B) 180 km/h", "C) 540 km/h", "D) 30 km/h"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Kasi (Speed) = Umbali / Muda = 180 km ÷ 3 saa = 60 km/h.",
            "explanation_en": "Spot on! Speed = Distance ÷ Time = 180 km ÷ 3 hrs = 60 km/h."
        }
    },
    {
        "id": "statistics_data_charts",
        "title_en": "Statistics: Mean, Median, Mode & Data Graphs",
        "title_sw": "Takwimu: Wastani (Mean), Nambari ya Kati (Median), Nambari ya Mara Nyingi (Mode) na Grafu",
        "subject": "Mathematics",
        "cbc_strand": "Data Handling & Probability (Grade 5-8 Mathematics)",
        "summary_en": "Statistics summarizes data sets: Mean is the arithmetic average (Sum ÷ Count), Median is the middle value in ordered data, Mode is the most frequent value, and Range is Highest minus Lowest.",
        "summary_sw": "Takwimu huchanganua data: Wastani (Mean = Jumla ÷ Idadi), Nambari ya Kati (Median = nambari iliyo katikati baada ya kupanga kwa mpangilio), na Nambari ya Mara Nyingi (Mode = nambari inayojirudia zaidi).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Panga mawe 5 ya ukubwa tofauti kwenye mstari kutoka dogo hadi kubwa: Jiwe lililo katikati kabisa (la tatu) ndilo Nambari ya Kati (Median). Ukijumlisha uzito wa mawe yote 5 na kugawa kwa 5, unapata Wastani (Mean)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Grafu ya Nguzo / Bar Graph] ➔ [Grafu ya Mviringo / Pie Chart] ➔ [Wastani = Jumla / Idadi].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu sokoni Kibuye, kama bei za samaki watano zilikuwa 200, 200, 300, 400, na 500: Nambari inayojirudia zaidi (Mode) ni 200, na nambari ya kati (Median) ni 300!",
                "analogy_en": "In Kisumu fish stalls, with fish prices of 200, 200, 300, 400, 500: the Mode is 200 (most frequent), and the Median is 300 (middle value)!"
            },
            "coastal": {
                "analogy_sw": "Pwani, wavuvi hupima wastani wa uzito wa samaki wa kila siku kwa kujumlisha kilo zote na kugawa kwa idadi ya samaki waliovuliwa!",
                "analogy_en": "Along coastal fishing cooperatives, daily catch weight mean is computed by summing total kilograms and dividing by the number of fish!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, kurekodi kiwango cha mvua cha kila mwezi (Rainfall Bar Chart) huwasaidia wakulima wa chai kujua miezi yenye mvua nyingi zaidi!",
                "analogy_en": "In highland tea regions, monthly rainfall bar graphs visually communicate seasonal precipitation trends for optimal planting schedules!"
            },
            "arid": {
                "analogy_sw": "Kwenye vituo vya afya vya Garissa, chati ya pai (Pie Chart) hutumiwa kuonyesha asilimia ya watoto waliopata chanjo ya surua na polio!",
                "analogy_en": "In arid rural health centers, pie charts represent proportional vaccination coverage across child demographic cohorts!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mtihani wa shule wenye alama za wanafunzi 10 huwekwa kwenye grafu ya nguzo ili mwalimu aone alama za wastani wa darasa zima!",
                "analogy_en": "In urban school academic tracking, classroom examination distributions are analyzed using bar charts and standard deviation curves!"
            }
        },
        "key_terms": [
            {"en": "Mean (Average = Sum / N)", "sw": "Wastani wa Nambari (Jumla ÷ Idadi)"},
            {"en": "Median (Middle Value)", "sw": "Nambari ya Kati (Katikati ya mpangilio)"},
            {"en": "Mode (Most Frequent)", "sw": "Nambari ya Mara Nyingi"},
            {"en": "Bar Graphs & Pie Charts", "sw": "Grafu za Nguzo na Chati za Mviringo (Pie)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuhesabu Wastani na Nambari ya Kati ya Umri wa Watu Nyumbani",
            "title_en": "Experiment: Family Age Survey Mean & Median Calculation",
            "materials_sw": "Daftari, kuandika umri wa watu 5 wa familia au marafiki (mfano: 10, 12, 12, 14, 42).",
            "materials_en": "Notebook, listing 5 family member ages.",
            "steps_sw": "1. Panga nambari kwa mpangilio: 10, 12, 12, 14, 42.\n2. Nambari ya katikati ni 12 (Median).\n3. Nambari inayojirudia zaidi ni 12 (Mode).\n4. Jumlisha (90) na ugawanye kwa 5: Wastani (Mean) = 18!",
            "steps_en": "1. Order ages: 10, 12, 12, 14, 42.\n2. Middle number = 12 (Median).\n3. Most repeated = 12 (Mode).\n4. Sum (90) ÷ 5 = 18 (Mean)!"
        },
        "quiz": {
            "question_sw": "Tafuta Wastani (Mean) wa nambari hizi nne: 10, 20, 30, 40",
            "question_en": "What is the Mean (arithmetic average) of these four numbers: 10, 20, 30, 40?",
            "options_sw": ["A) 25 (Jumla 100 ÷ 4 = 25)", "B) 30", "C) 20", "D) 100"],
            "options_en": ["A) 25 (Sum 100 ÷ 4 = 25)", "B) 30", "C) 20", "D) 100"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Jumla = 10 + 20 + 30 + 40 = 100. Wastani = 100 ÷ 4 = 25.",
            "explanation_en": "Spot on! Sum = 100. Mean = 100 ÷ 4 = 25."
        }
    },
    {
        "id": "integers_number_line",
        "title_en": "Integers, Negative Numbers & The Number Line",
        "title_sw": "Nambari Nzima (Integers), Nambari Hasi (-) na Mstari wa Nambari",
        "subject": "Mathematics",
        "cbc_strand": "Numbers & Number Theory (Grade 5-7 Mathematics)",
        "summary_en": "Integers include positive whole numbers (+1, +2...), zero (0), and negative numbers (-1, -2...). On a number line, values increase to the right and decrease to the left.",
        "summary_sw": "Nambari nzima (Integers) zinajumuisha nambari chanya (+), sifuri (0), na nambari hasi (-). Kwenye mstari wa nambari, thamani huongezeka kuelekea kulia na kupungua kuelekea kushoto.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Simama wima: Hatua unazopiga mbele ni Nambari Chanya (+1, +2, +3). Hatua unazopiga nyuma ni Nambari Hasi (-1, -2, -3). Mahali uliposimama kabla ya kuanza ni Sifuri (0)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Mstari wa Nambari: Hasi kushoto ➔ Sifuri katikati ➔ Chanya kulia] ➔ [Deni la Pesa = Nambari Hasi (-)].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria, usawa wa kawaida wa maji ya ziwa ni Sifuri (0 m). Samaki anayeogelea mita 5 chini ya maji yuko kina cha -5 m, wakati ndege anayeruka mita 10 angani yuko +10 m!",
                "analogy_en": "On Lake Victoria, water surface level is 0 meters. A fish swimming 5 meters deep is at altitude -5 m, while a bird flying 10 meters high is at +10 m!"
            },
            "coastal": {
                "analogy_sw": "Pwani, unapoingia dukani na kuwa na deni la shilingi 50 (Deni = -50), kisha ukapewa shilingi 100 na kulipa deni: -50 + 100 = unabaki na shilingi +50 mfukoni!",
                "analogy_en": "At coastal kiosks, having a debt of 50 shillings (-50) and receiving 100 shillings leaves a net balance of: -50 + 100 = +50 shillings!"
            },
            "highlands": {
                "analogy_sw": "Kileleni mwa Mlima Kenya usiku, joto hushuka chini ya sifuri hadi nyuzi -4°C (Nambari Hasi) ambapo maji huganda kuwa barafu!",
                "analogy_en": "On Mount Kenya summit peaks at night, temperatures plummet below zero to -4°C (negative integer), freezing liquid water solid!"
            },
            "arid": {
                "analogy_sw": "Kwenye visima vya jangwani, kuchimba kisima kwenda chini ardhini ni kupunguza nambari (-1 m, -2 m, -3 m) kuelekea maji ya chini ya ardhi!",
                "analogy_en": "Excavating desert boreholes represents moving negative distance below ground datum (-1m, -2m, -3m) toward the water table!"
            },
            "urban": {
                "analogy_sw": "Mtaani kwenye jengo la ghorofa lenye lifti, ghorofa ya chini ya ardhi (basement parking) ni Ghorofa ya -1 au -2, mapokezi ni Ghorofa 0, na juu ni Ghorofa +1, +2, +3!",
                "analogy_en": "In city commercial buildings, basement parking is designated Level -1 and -2, ground lobby is 0, and upper floors are +1, +2, +3!"
            }
        },
        "key_terms": [
            {"en": "Positive Integers (+)", "sw": "Nambari Chanya (Kulia kwa sifuri)"},
            {"en": "Negative Integers (-)", "sw": "Nambari Hasi (Kushoto kwa sifuri)"},
            {"en": "Rules of Signs (- × - = +)", "sw": "Kanuni za Alama (Hasi × Hasi = Chanya)"},
            {"en": "Absolute Value (|x|)", "sw": "Umbali kutoka Sifuri"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kutembea Kwenye Mstari wa Nambari Sakafuni",
            "title_en": "Experiment: Floor Number Line Walking Activity",
            "materials_sw": "Chaki ya kuchorea sakafuni, mstari wenye -3, -2, -1, 0, +1, +2, +3.",
            "materials_en": "Chalk line on the floor marked from -3 to +3.",
            "steps_sw": "1. Simama kwenye nambari 0.\n2. Piga hatua 2 mbele (+2).\n3. Piga hatua 4 nyuma (-4).\n4. Uko wapi sasa? Umefika kwenye nambari -2! (+2 - 4 = -2).",
            "steps_en": "1. Stand at 0.\n2. Step forward 2 paces (+2).\n3. Step backward 4 paces (-4).\n4. You land on -2! Physically proves 2 - 4 = -2."
        },
        "quiz": {
            "question_sw": "Kokotoa jibu sahihi la hesabu hii: -5 + 8 = ?",
            "question_en": "Calculate the correct integer result: -5 + 8 = ?",
            "options_sw": ["A) +3 (-5 + 8 = 3)", "B) -13", "C) +13", "D) -3"],
            "options_en": ["A) +3 (-5 + 8 = 3)", "B) -13", "C) +13", "D) -3"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Una deni la 5 lakini unalipa 8, unabaki na faida ya chanya 3 (+3).",
            "explanation_en": "Spot on! Starting at -5 and adding 8 advances rightward on the number line to +3."
        }
    },
    {
        "id": "perimeter_area_volume",
        "title_en": "Measurements: Perimeter, Area & Volume",
        "title_sw": "Vipimo: Mzingo (Perimeter), Eneo (Area) na Ujazo (Volume)",
        "subject": "Mathematics",
        "cbc_strand": "Measurements (Grade 5-8 Mathematics)",
        "summary_en": "Perimeter is the total boundary distance around a 2D shape (P = 2(L + W)). Area is the 2D surface space enclosed (Area = L × W). Volume is the 3D space occupied (Volume = L × W × H).",
        "summary_sw": "Mzingo ni urefu wa kuzunguka umbo lote (P = 2(L + W)). Eneo ni ukubwa wa uwanja wa ndani (Eneo = Urefu × Upana). Ujazo ni nafasi ya ndani ya chombo cha 3D (Ujazo = Urefu × Upana × Kimo).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Pitisha kidole chako pembezoni mwa kingo nne za kitabu chako—huo urefu wa kuzunguka ndio Mzingo (Perimeter). Paka kiganja chako juu ya jalada lote—hiyo nafasi bapa ya juu ndiyo Eneo (Area). Sasa hisi unene na uzito wa kitabu chote—hiyo ndiyo Ujazo (Volume)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Mzingo: Kuzunguka kingo za Shamba] ➔ [Eneo: Kupima Uwanja wote wa ndani m²] ➔ [Ujazo: Kujaza Maji ndani ya Tangi m³].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu, mkulima anapotaka kuweka ua wa waya kuzunguka shamba lake la mahindi anapima Mzingo (Perimeter). Anapotaka kupanda mbegu anapima Eneo (Area) la mita za mraba!",
                "analogy_en": "In Kisumu agriculture, fencing a farm requires measuring the Perimeter, while calculating seed planting capacity requires computing total farm Area (m²)!"
            },
            "coastal": {
                "analogy_sw": "Pwani, kupima kiasi cha maji ya kunywa yanayotoshea ndani ya tangi la duara la plastiki la lita 5000 ni kupima Ujazo (Volume in cubic meters)!",
                "analogy_en": "At coastal homes, determining how many liters a 5,000L cylindrical water tank holds requires calculating its 3D Volume (V = πr²h)!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, uwanja wa soka wa shule wenye urefu wa mita 100 na upana wa mita 50 una Eneo la mita za mraba 5,000 (100 m × 50 m = 5,000 m²)!",
                "analogy_en": "In highland school sports fields, a standard pitch measuring 100m by 50m encloses an Area of 5,000 square meters (100 × 50 = 5,000 m²)!"
            },
            "arid": {
                "analogy_sw": "Kwenye mabwawa ya kuchimba ya kukinga maji ya mvua (Water Pans), wakazi hukokotoa Ujazo (Volume = Eneo × Kina) ili kujua maji yatadumu miezi mingapi ya kiangazi!",
                "analogy_en": "In arid earth pan construction, engineers calculate excavation Volume (Area × Depth) to ensure sufficient water storage capacity through drought seasons!"
            },
            "urban": {
                "analogy_sw": "Mtaani, kuweka vigae (tiles) sakafuni mwa chumba kunahitaji kuhesabu Eneo la chumba (m²), na kununua fremu ya picha kunahitaji kupima Mzingo!",
                "analogy_en": "In urban house tiling, flooring tile quantities depend on floor Area (m²), while baseboard skirtings require measuring the room's Perimeter!"
            }
        },
        "key_terms": [
            {"en": "Perimeter (Units: m, cm)", "sw": "Mzingo (Urefu wa kuzunguka pande zote)"},
            {"en": "Area (Units: m², cm²)", "sw": "Eneo (Urefu × Upana)"},
            {"en": "Volume (Units: m³, Liters)", "sw": "Ujazo (Urefu × Upana × Kimo)"},
            {"en": "Circle Circumference (2πr) & Area (πr²)", "sw": "Mzingo na Eneo la Duara"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kupima Mzingo na Eneo la Kitabu cha Daftari kwa Rula",
            "title_en": "Experiment: Measuring Notebook Perimeter and Area with a Ruler",
            "materials_sw": "Daftari la shule, rula ya cm 30.",
            "materials_en": "School notebook, 30 cm ruler.",
            "steps_sw": "1. Pima urefu wa daftari (mfano cm 20) na upana (mfano cm 15).\n2. Kokotoa Mzingo: 2 × (20 + 15) = cm 70.\n3. Kokotoa Eneo: 20 × 15 = 300 cm²!",
            "steps_en": "1. Measure notebook length (e.g. 20 cm) and width (e.g. 15 cm).\n2. Calculate Perimeter: 2 × (20 + 15) = 70 cm.\n3. Calculate Area: 20 × 15 = 300 cm²!"
        },
        "quiz": {
            "question_sw": "Chumba chenye urefu wa mita 6 na upana wa mita 4 kina Eneo (Area) la mita za mraba ngapi?",
            "question_en": "A rectangular room has a length of 6 meters and a width of 4 meters. What is its Area in square meters?",
            "options_sw": ["A) 24 m² (6 m × 4 m)", "B) 20 m²", "C) 10 m²", "D) 48 m²"],
            "options_en": ["A) 24 m² (6 m × 4 m)", "B) 20 m²", "C) 10 m²", "D) 48 m²"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Eneo la mstatili = Urefu × Upana = 6 m × 4 m = 24 m².",
            "explanation_en": "Spot on! Area of a rectangle = Length × Width = 6 m × 4 m = 24 m²."
        }
    },
    {
        "id": "commercial_arithmetic",
        "title_en": "Commercial Arithmetic: Profit, Loss & Simple Interest",
        "title_sw": "Hesabu za Biashara: Faida (Profit), Hasara (Loss) na Riba Rahisi (Interest)",
        "subject": "Mathematics",
        "cbc_strand": "Commercial Arithmetic & Financial Literacy (Grade 6-9 Mathematics)",
        "summary_en": "Commercial arithmetic applies mathematics to financial transactions: Profit = Selling Price - Buying Price; Loss = Buying Price - Selling Price; Simple Interest = (Principal × Rate × Time) / 100.",
        "summary_sw": "Hesabu za biashara hutumika katika fedha: Faida = Bei ya Kuuzia - Bei ya Kununulia; Hasara = Bei ya Kununulia - Bei ya Kuuzia; Riba Rahisi = (Mtaji × Asilimia ya Riba × Miaka) / 100.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria ulinunua kuku kwa shilingi 400 sokoni (Buying Price). Ukamlisha na kumuuza kwa shilingi 600 (Selling Price). Umetengeneza Faida safi ya shilingi 200 (600 - 400 = 200)! Hiyo ni faida ya asilimia 50% ya mtaji wako!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kununua Bidhaa kwa Sh 400] ➔ [Kuiza kwa Sh 600] ➔ [Faida = Sh 200] ➔ [Mifumo ya Kibenki / Riba Rahisi].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu, mama muuzaji samaki anaponunua tenga la samaki kwa Sh 2,000 na kuuza samaki wote kwa Sh 2,800, ametengeneza faida ya Sh 800 (asilimia 40% ya faida)!",
                "analogy_en": "In Kisumu fish markets, buying a basket of Tilapia for 2,000 KES and selling for 2,800 KES yields an 800 KES profit (40% profit margin)!"
            },
            "coastal": {
                "analogy_sw": "Pwani, mfanyabiashara anapochukua mkopo wa benki wa Sh 10,000 kwa riba rahisi ya asilimia 10% kwa mwaka 1: analipa riba ya Sh 1,000 (Jumla Sh 11,000)!",
                "analogy_en": "In coastal trade, a micro-business loan of 10,000 KES at 10% annual simple interest incurs 1,000 KES interest, repaying 11,000 KES total!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, mkulima anaponunua magunia ya mbolea kwa punguzo la bei (Discount) la asilimia 10%, anaokoa pesa za kutosha kununulia mbegu!",
                "analogy_en": "In highland agricultural cooperatives, a 10% bulk discount on fertilizer saves vital capital for certified crop seeds!"
            },
            "arid": {
                "analogy_sw": "Kwenye masoko ya mifugo kule Isiolo, kuuza ngamia kwa bei ndogo kuliko aliyonunuliwa wakati wa ukame huhesabiwa kama Hasara (Loss = Buying Price - Selling Price)!",
                "analogy_en": "In northern livestock auctions during droughts, selling livestock below purchase cost incurs an accounted Loss (Loss = Cost - Selling Price)!"
            },
            "urban": {
                "analogy_sw": "Mtaani, kutumia akaunti ya akiba ya simu (M-Shwari au KCB M-PESA) yenye faida ya riba husaidia kuongeza akiba ya mwanafunzi kila mwezi!",
                "analogy_en": "In urban mobile wallets (M-Shwari / Airtel Money), earned savings interest compounds monthly returns on student emergency savings!"
            }
        },
        "key_terms": [
            {"en": "Profit = Selling Price - Cost Price", "sw": "Faida = Bei ya Kuuza - Bei ya Kununua"},
            {"en": "Loss = Cost Price - Selling Price", "sw": "Hasara = Bei ya Kununua - Bei ya Kuuza"},
            {"en": "Simple Interest (I = PRT / 100)", "sw": "Riba Rahisi (Mtaji × Riba × Miaka / 100)"},
            {"en": "Percentage Profit (% Profit)", "sw": "Asilimia ya Faida (Faida / Mtaji × 100%)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuendesha 'Duka la Darasani' na Kupiga Hesabu ya Faida",
            "title_en": "Experiment: Classroom Mock Kiosk Profit & Loss Ledger",
            "materials_sw": "Daftari la fedha, kalamu 3 zilizonunuliwa kwa shilingi 10 kila moja na kuuzwa kwa shilingi 15.",
            "materials_en": "Notebook ledger, mock transaction records.",
            "steps_sw": "1. Andika gharama ya kununua kalamu 3: 3 × 10 = Sh 30 (Buying Price).\n2. Andika mapato ya kuuza kalamu 3: 3 × 15 = Sh 45 (Selling Price).\n3. Kokotoa Faida: 45 - 30 = Sh 15 faida safi!",
            "steps_en": "1. Record wholesale cost for 3 pens: 3 × 10 = 30 KES.\n2. Record retail sales: 3 × 15 = 45 KES.\n3. Calculate Net Profit: 45 - 30 = 15 KES profit!"
        },
        "quiz": {
            "question_sw": "Mkulima alinunua mbuzi kwa shilingi 3,000 na akamuuza kwa shilingi 4,500. Alipata faida ya shilingi ngapi?",
            "question_en": "A trader bought a goat for 3,000 KES and sold it for 4,500 KES. How much profit did they make?",
            "options_sw": ["A) Sh 1,500 (4,500 - 3,000)", "B) Sh 4,500", "C) Sh 7,500", "D) Sh 500"],
            "options_en": ["A) 1,500 KES (4,500 - 3,000)", "B) 4,500 KES", "C) 7,500 KES", "D) 500 KES"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Faida = Bei ya Kuuzia (4,500) - Bei ya Kununulia (3,000) = Sh 1,500.",
            "explanation_en": "Spot on! Profit = Selling Price (4,500) - Cost Price (3,000) = 1,500 KES."
        }
    },
    {
        "id": "pythagoras_trigonometry",
        "title_en": "Pythagoras Theorem & Right-Angled Triangles",
        "title_sw": "Nadharia ya Pythagoras (a² + b² = c²) na Pembetatu Mraba",
        "subject": "Mathematics",
        "cbc_strand": "Geometry & Trigonometry (Grade 7-9 Mathematics)",
        "summary_en": "Pythagoras' theorem states that in any right-angled triangle (90°), the square of the hypotenuse (longest side c) equals the sum of the squares of the other two sides: a² + b² = c².",
        "summary_sw": "Nadharia ya Pythagoras inathibitisha kuwa kwenye pembetatu yoyote yenye pembe mraba (90°), mraba wa upande mrefu zaidi (hypotenuse c) unalingana na jumla ya miraba ya pande mbili fupi: a² + b² = c².",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria ngazi iliyoegemezwa ukutani: Ukuta wima wenye urefu wa mita 4 (a) na sakafu mlalo ya mita 3 (b) zinatengeneza pembe mraba ya 90°. Urefu wa ngazi yenyewe (Hypotenuse c) ni mita 5 haswa, kwa sababu 3² (9) + 4² (16) = 25 = 5²!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Pembetatu Mraba 90°] ➔ [Upande a² + Upande b² = Upande Mrefu c² / Hypotenuse].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu, wajenzi wa nyumba hutumia kanuni ya '3, 4, 5 Pythagoras' kwa kamba ili kuhakikisha pembe zote za msingi wa nyumba ni pembe mraba kamilifu za nyuzi 90°!",
                "analogy_en": "In Kisumu building construction, masons use the classic 3-4-5 Pythagorean rope ratio to lay perfectly square 90-degree foundation corners!"
            },
            "coastal": {
                "analogy_sw": "Pwani, nguzo ya mnazi ikikatwa na kuanguka kiulalo mchangani hutengeneza pembetatu mraba inayopimika kwa urahisi kwa kanuni ya Pythagoras!",
                "analogy_en": "At coastal marine docks, mooring guide ropes anchored at angles form right triangles whose tension load length is solved by Pythagoras!"
            },
            "highlands": {
                "analogy_sw": "Milimani, kupima urefu halisi wa mteremko wa mlima kutoka chini hadi kileleni hutumia Pythagoras kwa kutumia urefu wa wima na umbali wa mlalo!",
                "analogy_en": "In highland civil surveying, the true slope distance up steep hill gradients is calculated using vertical elevation and horizontal run (a² + b² = c²)!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo ya uwanda wa wazi, njia ya mkato (diagonal shortcut) ya kuvuka uwanja wa mraba huhesabiwa kwa kanuni ya Pythagoras kuokoa muda wa kutembea!",
                "analogy_en": "In wide savanna terrain, walking along the hypotenuse diagonal shortcut saves distance compared to walking along both perimeter legs!"
            },
            "urban": {
                "analogy_sw": "Mtaani, urefu wa kioo cha runinga (TV Screen size ya inchi 55 au 65) hupimwa kwa mstari wa mlalo wa upande mrefu (Hypotenuse diagonal) kwa kutumia Pythagoras!",
                "analogy_en": "In consumer electronics, TV display dimensions (e.g. 55-inch diagonal) measure the hypotenuse screen diagonal derived via Pythagoras' theorem!"
            }
        },
        "key_terms": [
            {"en": "Hypotenuse (Longest Side c)", "sw": "Upande Mrefu Zaidi (Hypotenuse unaoelekeana na 90°)"},
            {"en": "Pythagorean Equation (a² + b² = c²)", "sw": "Mlinganyo wa Pythagoras: a² + b² = c²"},
            {"en": "Pythagorean Triples (3-4-5, 5-12-13)", "sw": "Seti Maalum za Pythagoras (3, 4, 5)"},
            {"en": "Square Root (√)", "sw": "Kipeuo cha Pili (Square Root)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuthibitisha Nadharia ya Pythagoras kwa Karatasi za Mraba (3² + 4² = 5²)",
            "title_en": "Experiment: Cutout Square Proof of Pythagoras Theorem (9 + 16 = 25)",
            "materials_sw": "Karatasi yenye miraba (grid paper), penseli, rula.",
            "materials_en": "Grid square paper, scissors, ruler.",
            "steps_sw": "1. Chora pembetatu mraba yenye pande fupi za cm 3 na cm 4.\n2. Chora mraba juu ya upande wa 3 (ina miraba 9).\n3. Chora mraba juu ya upande wa 4 (ina miraba 16).\n4. Chora mraba juu ya upande mrefu: Ina miraba 25 kamili (9 + 16 = 25 = 5²)! Imethibitishwa!",
            "steps_en": "1. Draw a right triangle with legs of 3 cm and 4 cm.\n2. Construct a 3×3 square on leg a (area = 9).\n3. Construct a 4×4 square on leg b (area = 16).\n4. Construct square on hypotenuse c: its area equals exactly 25 (9 + 16 = 25 = 5²)! Q.E.D.!"
        },
        "quiz": {
            "question_sw": "Kwenye pembetatu mraba yenye upande a = 6 cm na b = 8 cm, urefu wa upande mrefu zaidi (hypotenuse c) ni kiasi gani?",
            "question_en": "In a right triangle with legs a = 6 cm and b = 8 cm, what is the length of the hypotenuse c?",
            "options_sw": ["A) 10 cm (√(36 + 64) = √100 = 10)", "B) 14 cm", "C) 48 cm", "D) 100 cm"],
            "options_en": ["A) 10 cm (√(36 + 64) = √100 = 10)", "B) 14 cm", "C) 48 cm", "D) 100 cm"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! a² + b² = 6² + 8² = 36 + 64 = 100. c = √100 = 10 cm.",
            "explanation_en": "Spot on! c² = 6² + 8² = 36 + 64 = 100. Hypotenuse c = √100 = 10 cm."
        }
    },
    {
        "id": "probability_chance",
        "title_en": "Probability & Likelihood of Chance Events",
        "title_sw": "Uwezekano wa Matukio (Probability) na Nafasi ya Kutokea",
        "subject": "Mathematics",
        "cbc_strand": "Data Handling & Probability (Grade 6-9 Mathematics)",
        "summary_en": "Probability measures the mathematical likelihood of an event occurring on a scale from 0 (Impossible) to 1 (Certain): Probability P(E) = Number of favorable outcomes ÷ Total possible outcomes.",
        "summary_sw": "Uwezekano hupima nafasi ya tukio kutokea kwa kipimo cha 0 (Haiwezekani kabisa) hadi 1 (Tukio la uhakika): Uwezekano P(E) = Matokeo unayoyataka ÷ Jumla ya matokeo yote yanayoweza kutokea.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika sarafu ya shilingi moja mkononi mwako. Upande mmoja una picha ya kichwa (Head) na upande mwingine una nambari ya thamani (Tail). Unaporusha sarafu angani, kuna uwezekano sawa wa asilimia 50% (1/2 au 0.5) wa kupata upande wa kichwa au thamani!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasioona/wasiosikia: [Kurusha Sarafu: Kichwa 1/2 au Mkia 1/2] ➔ [Kete ya Nambari 6: Nafasi ya kupata Nambari 1 ni 1/6] ➔ [Kipimo cha Uwezekano: 0 ➔ 0.5 ➔ 1].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu, kurusha sarafu kabla ya mechi ya soka ya Gor Mahia uwanjani kuamua nani anaanza na mpira kunatumia uwezekano sawa wa 50-50 (1/2)!",
                "analogy_en": "At Kisumu stadium football matches, the pre-game referee coin toss provides an exact 50-50 (1/2) equiprobable chance for team side selection!"
            },
            "coastal": {
                "analogy_sw": "Pwani, wavuvi wanapoangalia mawingu meusi asubuhi na kutabiri uwezekano mkubwa (High probability ya 80%) wa kunyesha mvua baharini!",
                "analogy_en": "Along coastal ports, meteorological probability models predict 80% precipitation chance during monsoon seasonal cycles!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, kupanda mbegu za mahindi zilizoidhinishwa (Certified seeds) zenye uwezekano wa kuota wa 95% (0.95 probability) huhakikisha karibu mbegu zote zinaota vizuri!",
                "analogy_en": "In highland agriculture, certified hybrid maize seed germination probability exceeds 95% (0.95), ensuring reliable crop stand emergence!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame ya kaskazini, uwezekano wa mvua kunyesha mwezi wa kiangazi ni mdogo sana (Low probability ya 0.05), ndio maana kuhifadhi maji ni muhimu!",
                "analogy_en": "In arid desert zones, dry-season precipitation probability is near zero (0.05), underscoring the absolute necessity of water preservation!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mchezo wa kete (Dice) wenye nambari 1 hadi 6 una uwezekano wa moja ya sita (1/6) wa kupata nambari 6 kwa kila mruruko!",
                "analogy_en": "In board games, rolling a standard 6-sided die offers an exact probability of one in six (1/6 ≈ 16.7%) for rolling any specific number!"
            }
        },
        "key_terms": [
            {"en": "Probability Scale (0 to 1)", "sw": "Kipimo cha Uwezekano: 0 (Haiwezekani) hadi 1 (Uhakika)"},
            {"en": "Favorable vs Total Outcomes", "sw": "Matokeo Yanayotakiwa ÷ Jumla ya Matokeo"},
            {"en": "Equally Likely Events", "sw": "Matukio Yenye Nafasi Sawa (mf. Sarafu 1/2)"},
            {"en": "Sample Space (S)", "sw": "Orodha ya Matokeo Yote Yanayowezekana"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kurusha Sarafu Mara 20 Kurekodi Uwezekano Halisi",
            "title_en": "Experiment: 20-Toss Coin Probability Law of Large Numbers Test",
            "materials_sw": "Sarafu moja ya shilingi, daftari na kalamu.",
            "materials_en": "One coin, notebook.",
            "steps_sw": "1. Rusha sarafu mara 20 na uandike kama umepata Kichwa (Head) au Mkia (Tail).\n2. Hesabu jumla: Utapata takriban mara 10 kichwa na mara 10 mkia.\n3. Hii inathibitisha uwezekano wa kinadharia wa 1/2 (50%)!",
            "steps_en": "1. Flip a coin 20 times and tally Heads vs Tails.\n2. Count final tallies: results cluster near ~10 Heads and ~10 Tails.\n3. Empirically validates theoretical probability P = 1/2!"
        },
        "quiz": {
            "question_sw": "Ukiviringisha kete ya kawaida yenye nambari 1 hadi 6, kuna uwezekano gani wa kupata nambari 4?",
            "question_en": "When rolling a fair 6-sided die, what is the probability of rolling the number 4?",
            "options_sw": ["A) 1/6 (Nambari moja kati ya 6)", "B) 4/6", "C) 1/2", "D) 1/4"],
            "options_en": ["A) 1/6 (One outcome out of 6)", "B) 4/6", "C) 1/2", "D) 1/4"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Kete ina nyuso 6 zenye nafasi sawa, na nambari 4 ni uso mmoja tu, kwa hivyo uwezekano ni 1/6.",
            "explanation_en": "Spot on! There is 1 favorable outcome (the face with 4) out of 6 equiprobable faces, giving P = 1/6."
        }
    }
]
