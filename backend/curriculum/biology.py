"""
ElewaSTEM Curriculum — Biology Learning Modules (12 Topics)
Aligned with KICD (Kenya CBC Grades 4-9), NERDC (Nigeria), DBE CAPS (South Africa), NaCCA (Ghana).
"""

from typing import List, Dict, Any

BIOLOGY_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "photosynthesis",
        "title_en": "Photosynthesis: How Plants Make Food",
        "title_sw": "Usanisinuru: Jinsi Mimea Inavyotengeneza Chakula",
        "subject": "Biology",
        "cbc_strand": "Living Things & Life Processes (Grade 5/6 Science & Grade 7 Integrated Science)",
        "summary_en": "Plants use sunlight, water, and carbon dioxide from the air to produce glucose energy and release fresh oxygen.",
        "summary_sw": "Mimea hutumia mwangaza wa jua, maji kutoka ardhini, na hewa ya kaboni kutengeneza chakula chake (glukosi) huku ikitoa hewa safi ya oksijeni.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika jani bichi mkononi mwako. Hisi upande wa juu ulivyo laini na bapa—sehemu hii inavuta mwangaza wa jua. Geuza jani upande wa chini, utahisi mishipa midogo midogo inayopitisha maji na mashimo madogo (stomata) yanayovuta hewa na kutoa oksijeni safi!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Mmea unaochipua] + [Ishara ya Jua linalong'aa] + [Ishara ya Kupumua na Kutoa Hewa]. Angalia mchoro wa mishale: Jua na Maji yanaingia ndani ya jani ➔ Chakula (Sukari) kinabaki ndani ➔ Oksijeni inatoka nje.",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu kando ya Ziwa Victoria, tazama magugu maji (Water Hyacinth / Akech) na mboga za Osuga (Managu)! Majani yake mapana ya kijani yamejaa Klorofili inayofyonza mwangaza wa jua la ziwani na maji ya ziwa kupika chakula na kutoa oksijeni inayosaidia samaki Ngege kupumua!",
                "analogy_en": "In Kisumu along Lake Victoria, water hyacinth and Osuga greens absorb lake sunlight and water to produce food while releasing oxygen for tilapia fish!"
            },
            "coastal": {
                "analogy_sw": "Pwani kule Mombasa, Diani na Kilifi, minazi na mikoko ufukweni inafyonza jua kali la Bahari Hindi na kutengeneza tui tamu la nazi lililojaa nishati!",
                "analogy_en": "Along coastal beaches, coconut palms and mangroves absorb intense tropical sunlight to synthesize sweet energy-rich coconut water!"
            },
            "highlands": {
                "analogy_sw": "Milimani Kericho na Nyeri, majani ya chai ya kijani kibichi yananasa mwangaza wa jua asubuhi baada ya umande kutengeneza virutubisho na kutoa harufu nzuri!",
                "analogy_en": "In the lush highlands of Kericho, rolling green tea bushes capture morning rays to synthesize nutrients and fresh clean air!"
            },
            "arid": {
                "analogy_sw": "Kule Garissa na Lodwar, mti wa mshikio (acacia) una majani madogo sana yenye klorofili ili kuzuia maji yasipotee huku ukiendelea kutengeneza chakula juani!",
                "analogy_en": "In arid regions, thorny acacia trees use tiny waxy leaves to capture sunlight while preventing dehydration!"
            },
            "urban": {
                "analogy_sw": "Mtaani Nairobi au Mombasa, miti ya bustani za Uhuru Park inafanya kazi kama mapafu ya jiji, ikifyonza moshi wa magari na kutoa oksijeni safi!",
                "analogy_en": "In urban schoolyards, city trees absorb traffic carbon emissions and produce pure oxygen for students!"
            }
        },
        "key_terms": [
            {"en": "Chlorophyll", "sw": "Klorofili (Rangi ya kijani inayonasa jua)"},
            {"en": "Stomata", "sw": "Stomata (Vinyweleo vya majani vya kupumulia)"},
            {"en": "Glucose", "sw": "Glukosi (Chakula cha sukari kinachotengenezwa na mmea)"},
            {"en": "Oxygen", "sw": "Oksijeni (Gesi safi inayotolewa na mmea)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Viputo vya Oksijeni kwenye Majani",
            "title_en": "Experiment: Observing Oxygen Bubbles in Water",
            "materials_sw": "Jani bichi (kama sukuma au managu), glasi au chupa safi ya maji, mwangaza wa jua.",
            "materials_en": "Fresh green leaf, clear glass of water, sunlight.",
            "steps_sw": "1. Weka jani bichi ndani ya glasi ya maji safi.\n2. Weka glasi juani kwa dakika 30.\n3. Angalia kwa karibu—utaona viputo vidogo vya hewa ya oksijeni vikitoka kwenye jani!",
            "steps_en": "1. Submerge a fresh leaf in a clear cup of water.\n2. Place it in bright sunlight for 30 minutes.\n3. Watch tiny oxygen gas bubbles form and float up!"
        },
        "quiz": {
            "question_sw": "Ni gesi gani muhimu inayotolewa na mimea wakati wa usanisinuru ambayo binadamu anahitaji ili kupumua?",
            "question_en": "Which gas do green plants release during photosynthesis that humans breathe?",
            "options_sw": ["A) Oksijeni (Oxygen)", "B) Kaboni Dioksidi", "C) Moshi", "D) Nitrojeni"],
            "options_en": ["A) Oxygen", "B) Carbon Dioxide", "C) Smoke", "D) Nitrogen"],
            "correct_index": 0,
            "explanation_sw": "Hodari sana! Mimea hutengeneza glukosi na kutoa hewa safi ya Oksijeni tunayoivuta kila sekunde.",
            "explanation_en": "Brilliant! Plants convert carbon dioxide and water into glucose, releasing oxygen as a byproduct."
        }
    },
    {
        "id": "human_digestive_system",
        "title_en": "Human Digestive System & Nutrition",
        "title_sw": "Mfumo wa Mmeng'enyo wa Chakula na Lishe Mwilini",
        "subject": "Biology",
        "cbc_strand": "Human Body Systems & Health (Grade 5/6 Science & Grade 7 Integrated Science)",
        "summary_en": "Digestion breaks down food into microscopic nutrients that are absorbed into the bloodstream to give energy and build the body.",
        "summary_sw": "Mmeng'enyo wa chakula huvunja chakula katika chembechembe ndogo za virutubisho zinazofyonzwa na damu ili kuupa mwili nguvu na afya.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Weka kidole chako mdomoni ambapo meno yanatafuna na mate yanalainisha. Fuata koo (umio) kuelekea tumboni ambapo asidi inavunja protini. Kisha hisi tumbo la chini ambapo utumbo mwembamba mrefu unafyonza virutubisho vyote kuingia kwenye damu!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kutafuna Mdomoni] ➔ [Kumeza kupitia Umio] ➔ [Tumbo linavunja Chakula] ➔ [Utumbo mdogo unafyonza Nguvu kuingia Damuni].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu unapokula ugali wa mtama kwa samaki Ngege na mboga za Osuga, mate mdomoni yanaanza kuyeyusha wanga wa ugali, tumbo linavunja protini ya samaki, na utumbo mdogo unafyonza madini ya chuma na vitamini ili kukuza misuli yako!",
                "analogy_en": "In Kisumu when eating millet ugali with Tilapia and Osuga greens, mouth amylase breaks down starches, stomach acids digest fish proteins, and the small intestine absorbs nutrients into your bloodstream!"
            },
            "coastal": {
                "analogy_sw": "Pwani unapokula wali wa nazi na samaki wa kukaanga, mafuta ya nazi yanavunjwa na nyongo (bile) kutoka kwenye ini, kisha virutubisho vinasambazwa mwilini kote!",
                "analogy_en": "At the coast when eating coconut rice, coconut fats are emulsified by liver bile in the duodenum for body energy!"
            },
            "highlands": {
                "analogy_sw": "Mashambani unapokula githeri (mahindi na maharagwe), nyuzi za chakula (fiber) na protini zinameng'enywa polepole ili kukupa nguvu ya siku nzima!",
                "analogy_en": "In the highlands when eating githeri (maize & beans), complex fiber and proteins digest steadily to provide sustained energy!"
            },
            "arid": {
                "analogy_sw": "Kule Garissa unywapo maziwa ya ngamia yenye virutubisho tele, utumbo mdogo unafyonza kalsiamu na protini kwa haraka ili kuimarisha mifupa na kuzuia kiu!",
                "analogy_en": "In arid regions, drinking nutrient-dense camel milk allows the digestive tract to rapidly absorb calcium and water!"
            },
            "urban": {
                "analogy_sw": "Mtaani unapokula chapati na maharagwe, kinywa, umio, tumbo, na utumbo vinafanya kazi pamoja kama kiwanda cha kuchuja na kusambaza nishati mwilini!",
                "analogy_en": "In the city, digestion works like a biological processing factory, breaking carbohydrates into glucose fuel for brain cells!"
            }
        },
        "key_terms": [
            {"en": "Digestion", "sw": "Mmeng'enyo wa Chakula"},
            {"en": "Esophagus", "sw": "Umio (Njia ya koo kuelekea tumboni)"},
            {"en": "Enzymes", "sw": "Vimeng'enya (Kemikali asilia za kuyeyusha chakula)"},
            {"en": "Small Intestine (Villi)", "sw": "Utumbo Mdogo (Sehemu ya kufyonza virutubisho)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Vimeng'enya vya Mate Mdomoni",
            "title_en": "Experiment: Salivary Amylase Starch Test",
            "materials_sw": "Kipande kidogo cha mkate kavu au biskuti au ugali.",
            "materials_en": "Small piece of plain bread or ugali.",
            "steps_sw": "1. Weka kipande kidogo cha mkate mdomoni.\n2. Tafuna taratibu kwa dakika 2 bila kukimeza.\n3. Utahisi kikianza kuwa kitamu (sukari)—vimeng'enya vya mate vinavunja wanga kuwa sukari!",
            "steps_en": "1. Place bread in your mouth.\n2. Chew slowly for 2 minutes without swallowing.\n3. Notice it turns sweet—salivary amylase is breaking starch into glucose!"
        },
        "quiz": {
            "question_sw": "Sehemu gani ya mfumo wa mmeng'enyo inahusika zaidi na kufyonza virutubisho vya chakula kuingia kwenye damu?",
            "question_en": "Which organ in the digestive system is primarily responsible for absorbing digested nutrients into the bloodstream?",
            "options_sw": ["A) Utumbo Mdogo (Small Intestine)", "B) Kinywa tu", "C) Umio (Esophagus)", "D) Nywele"],
            "options_en": ["A) Small Intestine", "B) Mouth only", "C) Esophagus", "D) Hair"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Utumbo mdogo una vinyweleo vidogo (villi) vinavyofyonza virutubisho vyote na kuviingiza moja kwa moja kwenye damu.",
            "explanation_en": "Spot on! The small intestine lining is covered with villi that absorb nutrients directly into blood capillaries."
        }
    },
    {
        "id": "circulatory_heart",
        "title_en": "Human Heart & Blood Circulatory System",
        "title_sw": "Moyo na Mzunguko wa Damu Mwilini",
        "subject": "Biology",
        "cbc_strand": "Human Body & Vital Organs (Grade 5/6 Science & Grade 7 Integrated Science)",
        "summary_en": "The heart acts as a muscular pump that continuously circulates blood, delivering oxygen and food nutrients to every cell while removing waste carbon dioxide.",
        "summary_sw": "Moyo hufanya kazi kama pampu ya misuli inayozungusha damu mwilini bila kukoma, ikisafirisha oksijeni na virutubisho kwa kila seli na kuondoa uchafu.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Weka kiganja chako katikati ya kifua chako kuelekea upande wa kushoto kidogo. Hisi mpigo thabiti wa 'du-du... du-du'. Huo ni moyo wako wenye vyumba vinne ukisukuma damu safi kuelekea kichwani, mikononi, na miguuni kupitia mishipa ya ateri!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Moyo unaopiga] ➔ [Mchoro wa Damu Nyekundu inayosafiri mwilini] ➔ [Damu inayorudi kwenye Mapafu kusafishwa].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kama pampu ya maji ya manispaa ya Kisumu inayosukuma maji safi ya Ziwa Victoria kupitia mtandao wa mabomba kwenye nyumba zote za jiji, moyo wako unasukuma damu safi kupitia ateri kwenye seli zote za mwili!",
                "analogy_en": "Like water pumps circulating clean lake water through pipe networks to every household, your heart pumps oxygen-rich blood through arteries to every cell!"
            },
            "coastal": {
                "analogy_sw": "Pwani, kama meli bandarini zinazosafirisha mizigo na kurudi na bidhaa mpya, chembechembe nyekundu za damu (Red Blood Cells) zinasafirisha oksijeni na kurudisha hewa ya kaboni kwenye mapafu!",
                "analogy_en": "At the port, like cargo ships delivering supplies, red blood cells ferry oxygen to tissues and return carbon dioxide to the lungs!"
            },
            "highlands": {
                "analogy_sw": "Milimani, wanariadha maarufu wa Eldoret na Iten wana mioyo imara sana na chembechembe nyingi za damu zinazowezesha kusafirisha oksijeni nyingi wakati wa mbio ndefu!",
                "analogy_en": "In high-altitude training camps in Iten, athletes develop strong cardiac muscles and high red blood cell counts to maximize oxygen delivery!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo ya joto kali, mishipa ya damu ya ngozi hupanuka kidogo ili kutoa joto jingi nje ya mwili na kukuweka salama!",
                "analogy_en": "In hot arid regions, peripheral blood vessels dilate to radiate excess body heat safely!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mtandao wa mishipa ya damu (ateri na vena) ni kama barabara za mji zenye njia mbili—njia moja inapeleka bidhaa safi na nyingine inarudisha taka!",
                "analogy_en": "In urban centers, the circulatory system mirrors a dual-carriageway highway network transporting vital nutrients and clearing waste!"
            }
        },
        "key_terms": [
            {"en": "Heart (Atrium & Ventricle)", "sw": "Moyo (Vyumba vya juu na chini vya pampu)"},
            {"en": "Arteries & Veins", "sw": "Mishipa ya Ateri (Damu safi) na Vena (Damu chafu)"},
            {"en": "Red Blood Cells", "sw": "Chembechembe Nyekundu za Damu (Zinabeba Oksijeni)"},
            {"en": "Pulse Rate", "sw": "Kasi ya Mapigo ya Moyo"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kupima Mapigo ya Moyo Kabla na Baada ya Mazoezi",
            "title_en": "Experiment: Measuring Resting vs Active Pulse Rate",
            "materials_sw": "Vidole viwili (cha kati na cha shahada), saa au kuhesabu kwa sekunde 60.",
            "materials_en": "Two fingers, watch or phone timer for 60 seconds.",
            "steps_sw": "1. Weka vidole viwili kwenye kifundo cha mkono chini ya kidole gumba.\n2. Hesabu mapigo ukiwa umepumzika (kawaida 70-85 kwa dakika).\n3. Ruka kamba mara 20 kisha upime tena—moyo utapiga kwa kasi zaidi kusukuma oksijeni kwenye misuli!",
            "steps_en": "1. Place two fingers on the inside of your wrist below the thumb.\n2. Count resting pulses for 60 seconds.\n3. Jump in place 20 times and re-measure—your pulse quickens as the heart pumps oxygen to muscles!"
        },
        "quiz": {
            "question_sw": "Mishipa ya Ateri inafanya kazi gani kuu mwilini?",
            "question_en": "What is the primary function of Arteries in the circulatory system?",
            "options_sw": ["A) Kusafirisha damu safi yenye oksijeni kutoka kwenye moyo kwenda mwilini", "B) Kutengeneza mate", "C) Kusaga chakula", "D) Kuotesha nywele"],
            "options_en": ["A) Carrying oxygenated blood away from the heart to body tissues", "B) Producing saliva", "C) Grinding food", "D) Growing hair"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Ateri hubeba damu safi iliyojaa oksijeni kutoka kwenye moyo kuelekea kwenye viungo vyote vya mwili.",
            "explanation_en": "Brilliant! Arteries carry oxygen-rich blood under pressure from the heart to all body tissues."
        }
    },
    {
        "id": "human_respiration",
        "title_en": "Human Respiratory System & Lungs",
        "title_sw": "Mfumo wa Upumuaji wa Binadamu na Mapafu",
        "subject": "Biology",
        "cbc_strand": "Living Things & Life Processes (Grade 5/6 Science & Grade 7 Integrated Science)",
        "summary_en": "Breathing draws fresh oxygen into the lungs where it passes into the blood, while carbon dioxide waste is breathed out.",
        "summary_sw": "Upumuaji huleta hewa safi ya oksijeni kwenye mapafu ambapo huingia kwenye damu, na kutoa nje hewa chafu ya kaboni dioksidi.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Weka mikono yako miwili mbavuni kifuani mwako. Vuta pumzi ndefu ndani kupitia puani—hisi mbavu zako zikipanuka na kifua kikiinuka juu wakati mapafu yanapojaa hewa. Toa pumzi taratibu mdomoni—hisi kifua kikishuka chini!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kuvuta Pumzi Puani] ➔ [Mapafu Yanayopanuka] ➔ [Oksijeni inayoingia kwenye Damu na Kaboni inayotoka Nje].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria wakati upepo mwanana wa ziwani unapovuma asubuhi, unavuta hewa safi iliyojaa oksijeni kupitia koromeo hadi kwenye mifuko midogo ya hewa (alveoli) ya mapafu yako!",
                "analogy_en": "By Lake Victoria, breathing in cool morning lake breezes channels oxygen down the trachea into microscopic alveoli air sacs in your lungs!"
            },
            "coastal": {
                "analogy_sw": "Pwani ufukweni, miti ya mikoko inasafisha hewa ya bahari, na mapafu yako yanatumia misuli ya kiwambo (diaphragm) kuvuta hewa ndani!",
                "analogy_en": "Along coastal beaches, your diaphragm muscle contracts downward to draw oxygen-rich coastal air into lung bronchi!"
            },
            "highlands": {
                "analogy_sw": "Kule milimani ambapo hewa ni baridi na safi, mapafu hufanya kazi kwa ufanisi mkubwa kuchuja vumbi kupitia vinyweleo vidogo (cilia) vya puani!",
                "analogy_en": "In highland climates, nasal cilia and mucus filter dust before pristine air reaches deep lung tissues!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo yenye vumbi na jua kali, mfumo wa pua hupasha hewa joto na kuinywesha unyevu kabla haijafika kwenye mapafu yako laini!",
                "analogy_en": "In dry arid environments, nasal passages humidify warm dry air to protect delicate alveoli membranes!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mapafu yanafanya kazi kama chujio la hewa la gari, yakilinda mwili dhidi ya chembe za moshi huku yakichukua oksijeni pekee!",
                "analogy_en": "In urban neighborhoods, the respiratory mucosa traps airborne particles while permitting pure oxygen gas exchange!"
            }
        },
        "key_terms": [
            {"en": "Trachea (Windpipe)", "sw": "Koromeo (Njia kuu ya hewa)"},
            {"en": "Lungs & Bronchi", "sw": "Mapafu na Matawi ya Koromeo"},
            {"en": "Alveoli (Air Sacs)", "sw": "Mifuko midogo ya kubadilishia hewa (Alveoli)"},
            {"en": "Diaphragm", "sw": "Kiwambo cha mbavu (Misuli inayosaidia kupumua)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Mvuke na Hewa Inayotoka Mapafuni",
            "title_en": "Experiment: Exhaled Moisture and Carbon Dioxide Test",
            "materials_sw": "Kioo kidogo au miwani safi, pumzi yako.",
            "materials_en": "Small pocket mirror or clean glass, your breath.",
            "steps_sw": "1. Shikilia kioo mbele ya mdomo wako.\n2. Pumua kwa nguvu 'haaaaa' kwenye kioo.\n3. Utaona ukungu wa matone madogo ya maji—mapafu yanatoa joto na unyevu wa maji pamoja na kaboni dioksidi!",
            "steps_en": "1. Hold a small mirror near your mouth.\n2. Exhale warmly onto the surface.\n3. Observe water condensation—proving lungs expel warm moisture alongside carbon dioxide!"
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
        "cbc_strand": "Cell Structure & Basic Units of Life (Grade 7/8 Integrated Science)",
        "summary_en": "Cells are the microscopic building blocks of all living things. Plant cells have rigid cell walls and chloroplasts, while animal cells have flexible membranes.",
        "summary_sw": "Seli ni vitengo vidogo sana vya msingi vinavyounda viumbe hai vyote. Seli za mimea zina kuta imara na kloroplasti, wakati seli za wanyama zina utando laini.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria nyumba imejengwa kwa matofali madogo elfu nyingi. Mwili wako na mmea vimejengwa kwa 'matofali ya uhai' yanayoitwa Seli. Ndani ya kila seli kuna Kiini (Nucleus) chenye umbo la duara kinachoongoza shughuli zote, kikiwa kimezungukwa na kioevu cha jeli (Saikroplasimu)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Seli ya Mmea (Ukuta Kijani Mgumu)] vs [Seli ya Mnyama (Duara Laini yenye Kiini Katikati)].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kama ukuta wa matofali ya ujenzi huko Kisumu unavyounda nyumba, mamilioni ya seli za magugu maji na mboga za kienyeji zimeungana kuunda majani, mizizi na mashina!",
                "analogy_en": "Just as bricks form a sturdy building, billions of microscopic cells unite to construct the stems, leaves, and roots of indigenous plants!"
            },
            "coastal": {
                "analogy_sw": "Pwani, seli ya mnazi ina kloroplasti zinazofanya usanisinuru kama paneli ndogo za jua, huku seli za samaki zikiwa na utando laini unaobadilika ili kuruhusu kuogelea!",
                "analogy_en": "At the coast, palm leaf cells contain chloroplast solar powerhouses, while flexible fish animal cells allow fluid swimming locomotion!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, seli za viazi na mahindi zina chembechembe maalum za kuhifadhi wanga (starch granules) ili mmea uwe na chakula cha kutosha kukua!",
                "analogy_en": "In highland agricultural zones, potato cells contain specialized amyloplasts packed with starch reserves to fuel rapid growth!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame, seli za mimea ya mikakasi (succulents) na acacia zina vacuoles kubwa za kuhifadhi maji kwa miezi mingi bila kukauka!",
                "analogy_en": "In arid ASAL zones, succulent plant cells feature massive central vacuoles designed to store water reserves through droughts!"
            },
            "urban": {
                "analogy_sw": "Mtaani, kiini cha seli (nucleus) kinafanya kazi kama afisa mkuu wa jiji au kompyuta kuu inayoongoza shughuli zote za uzalishaji!",
                "analogy_en": "In modern cities, the cell nucleus functions like a central control hub, housing genetic DNA blueprints for all operations!"
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
            "materials_sw": "Kitunguu maji kimoja, tone la maji, kioo cha kukuza picha au kamera ya simu.",
            "materials_en": "One fresh onion, water droplet, magnifying lens.",
            "steps_sw": "1. Menya kitunguu na uvute utando mwembamba sana ulio wazi kama nailoni.\n2. Weka juu ya tone la maji kwenye uso safi.\n3. Angalia kwa karibu chini ya mwanga—utaona mistari inayofanana na matofali ya seli zilizopangwa vizuri!",
            "steps_en": "1. Peel a fresh onion and gently separate the thin translucent membrane.\n2. Float it on a clean water droplet.\n3. Examine under light with a magnifier to observe the organized brick-like grid of plant cells!"
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
        "cbc_strand": "Plants & Reproduction (Grade 5/6 Science & Grade 7 Integrated Science)",
        "summary_en": "Pollination transfers yellow pollen grains from male stamens to female pistils, allowing flowers to form seeds and fruits.",
        "summary_sw": "Uchavushaji husafirisha chembe za chavua (poleni) kutoka kwenye chavulio (stamen) hadi kwenye kambamaua (pistil) ili kukuza mbegu na matunda matamu.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika ua lililochanua mkononi mwako. Hisi petali laini zenye harufu nzuri za kuvutia nyuki. Katikati ya ua utahisi vijiti vidogo vyenye vumbi laini la unga (chavua/pollen). Ndani kabisa kuna sehemu yenye unyevu ambapo mbegu na matunda huanza kutungika!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Nyuki anayeruka] ➔ [Kugusa Ua na Kuchukua Poleni] ➔ [Mbegu na Tunda linaloota].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu kwenye mashamba ya alizeti au maembe, nyuki wanapotua kwenye maua kunyonya majimaji matamu (nectar), miguu yao inashika unga wa chavua na kuusafirisha kwenye ua jingine ili maembe manono yatokee!",
                "analogy_en": "In Kisumu sunflower and mango groves, foraging honeybees sipping nectar pick up pollen on their legs, cross-pollinating blossoms into fruits!"
            },
            "coastal": {
                "analogy_sw": "Pwani, vipepeo wenye rangi za kuvutia na upepo wa bahari husaidia kuchavusha maua ya mikorosho na mipapai ili wakulima wavune korosho nyingi!",
                "analogy_en": "Along coastal plantations, colorful butterflies and sea breezes pollinate cashew and papaya blooms for abundant harvests!"
            },
            "highlands": {
                "analogy_sw": "Kule Kitale na Nakuru, upepo wa asubuhi unatikisa mashamba ya mahindi na kurusha mamilioni ya chembe za poleni kutoka kwenye mashada ya juu (tassels) hadi kwenye nyuzi laini za mahindi (silks)!",
                "analogy_en": "In highland maize fields, morning winds shake pollen from top tassels down onto emerging ear silks, fertilizing sweet corn kernels!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame, miti ya mshikio (acacia) hutoa maua yenye harufu kali baada ya mvua fupi ili kuvuta wadudu wengi kwa haraka!",
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
            "materials_en": "Fresh open flower, clean index finger.",
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
        "cbc_strand": "Classification of Living Things (Grade 5/6 Science & Grade 7 Integrated Science)",
        "summary_en": "Animals are classified into Vertebrates (with a backbone: mammals, birds, reptiles, amphibians, fish) and Invertebrates (without a backbone: insects, spiders, snails).",
        "summary_sw": "Wanyama huainishwa katika Wenye Uti wa Mgongo (Vertebrates: mamalia, ndege, reptilia, amfibea, samaki) na Wasio na Uti wa Mgongo (Invertebrates: wadudu, buibui, konokono).",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Pitisha vidole vyako katikati ya mgongo wako kuanzia shingoni hadi kiunoni. Utahisi mfupa mgumu uliopinda wenye vifundo vidogo—huo ndio Uti wa Mgongo (Backbone). Wanyama kama binadamu, mbwa, na samaki wana uti wa mgongo (Vertebrates), lakini wadudu kama panzi na konokono hawana mifupa ndani (Invertebrates)!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kushika Uti wa Mgongo] ➔ [Makundi 5 ya Vertebrates: Mamalia, Ndege, Samaki, Reptilia, Amfibea] vs [Invertebrates: Wadudu na Konokono].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria, samaki Ngege ana mifupa na uti wa mgongo mgumu (Vertebrate), lakini konokono wa majini na wadudu wa ziwani hawana mfupa wowote ndani (Invertebrates)!",
                "analogy_en": "In Lake Victoria, Tilapia fish possess an internal bony vertebral column (Vertebrate), whereas freshwater snails lack backbones (Invertebrates)!"
            },
            "coastal": {
                "analogy_sw": "Pwani, kasa wa baharini na pomboo ni wenye uti wa mgongo (Vertebrates), wakati kaa na ngisi wana maganda ya nje au miili laini bila mifupa ya ndani (Invertebrates)!",
                "analogy_en": "Along coastal reefs, sea turtles and dolphins are vertebrates, while crabs and octopuses are invertebrates!"
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
                "analogy_en": "In urban centers, pigeons and domestic cats are vertebrates, while mosquitoes and houseflies are invertebrates!"
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
            "materials_en": "Notebook, pen, outdoor observation.",
            "steps_sw": "1. Orodhesha wanyama 5 unaowaona (kama kuku, mbwa, panzi, kipepeo, samaki).\n2. Wagawe katika safu mbili: Wenye Uti wa Mgongo vs Wasio na Uti wa Mgongo.\n3. Utaona jinsi sayansi ya uainishaji inavyorahisisha kuelewa viumbe!",
            "steps_en": "1. List 5 creatures observed around your home or school.\n2. Categorize them into two columns: Vertebrate vs Invertebrate.\n3. Observe how biological taxonomy reveals shared traits!"
        },
        "quiz": {
            "question_sw": "Ni kundi gani kati ya yafuatayo linalojumuisha wanyama wenye uti wa mgongo (Vertebrates) pekee?",
            "question_en": "Which group contains ONLY Vertebrate animals?",
            "options_sw": ["A) Samaki, Ndege, Mamalia, Reptilia, na Amfibea", "B) Panzi, Konokono, na Minyoo", "C) Mbu, Buibui, na Nyuki", "D) Mchwa pekee"],
            "options_en": ["A) Fish, Birds, Mammals, Reptiles, and Amphibians", "B) Grasshoppers, Snails, and Earthworms", "C) Mosquitoes, Spiders, and Bees", "D) Termites only"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Samaki, ndege, mamalia, reptilia na amfibea wote wana uti wa mgongo.",
            "explanation_en": "Excellent! Fish, birds, mammals, reptiles, and amphibians constitute the 5 major vertebrate classes."
        }
    },
    {
        "id": "ecology_food_chains",
        "title_en": "Ecology & Food Chains: Energy Flow in Nature",
        "title_sw": "Mnyororo wa Chakula na Mfumo wa Ikolojia",
        "subject": "Biology",
        "cbc_strand": "Environment & Ecosystems (Grade 5/6 Science & Grade 8 Integrated Science)",
        "summary_en": "A food chain shows how energy flows from the sun to green plant producers, then to herbivore and carnivore consumers, and finally to decomposers.",
        "summary_sw": "Mnyororo wa chakula huonyesha jinsi nishati inavyosafiri kuanzia jua hadi kwa mimea (watengenezaji), kisha kwa wanyama walaji, na hatimaye kwa waozeshaji.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria mnyororo uliounganishwa kwa pete: Pete ya kwanza ni Jua linalomulika jani la nyasi (Mzalishaji). Pete ya pili ni Panzi au Mbuzi anayekula nyasi (Mlaji wa kwanza). Pete ya tatu ni Kuku au Simba anayekula mlaji wa kwanza. Kila kiumbe kinategemea kingine kuishi!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Jua] ➔ [Mmea / Mtengenezaji] ➔ [Panzi / Mlaji wa Kwanza] ➔ [Kuku / Mlaji wa Pili] ➔ [Waozeshaji / Decomposers].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Ziwa Victoria: Mwangaza wa Jua ➔ Mwani na Magugu Maji (Watengenezaji) ➔ Samaki Dagaa/Omena (Walaji wa kwanza) ➔ Samaki Mbuta/Nile Perch (Mlaji mkuu) ➔ Binadamu!",
                "analogy_en": "In Lake Victoria: Sunlight ➔ Microscopic Algae ➔ Dagaa/Omena filter feeders ➔ Nile Perch apex predator ➔ Humans!"
            },
            "coastal": {
                "analogy_sw": "Pwani: Mwani wa Bahari ➔ Samaki wadogo na uduvi ➔ Samaki mkubwa wa Nguru au Papa ➔ Ndege wa baharini!",
                "analogy_en": "Along coastal coral reefs: Seaweed producers ➔ Small reef fish ➔ Barracuda/Shark predators!"
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
            "materials_en": "Paper, colored pencils.",
            "steps_sw": "1. Chora Jua na Mmea wa eneo lako upande wa kushoto.\n2. Weka mshale ➔ kuelekea mnyama anayekula mmea huo (mf. mbuzi au panzi).\n3. Weka mshale mwingine ➔ kuelekea kiumbe anayekula mnyama huyo.\n4. Hongera! Umetengeneza ramani ya mzunguko wa nishati!",
            "steps_en": "1. Draw the Sun and a local green plant on the left.\n2. Add an arrow ➔ pointing to a primary herbivore.\n3. Add another arrow ➔ to a predator.\n4. You have mapped the ecological flow of solar energy!"
        },
        "quiz": {
            "question_sw": "Katika mnyororo wa chakula, ni viumbe gani wanaoitwa 'Watengenezaji' (Producers) kwa sababu wanatengeneza chakula chao kwa kutumia jua?",
            "question_en": "In a food chain, which organisms are called 'Producers' because they synthesize their own food using sunlight?",
            "options_sw": ["A) Mimea ya kijani (Green Plants)", "B) Simba", "C) Samaki Mbuta", "D) Mawe"],
            "options_en": ["A) Green Plants", "B) Lions", "C) Nile Perch", "D) Stones"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Mimea ya kijani ndiyo watengenezaji pekee wanaobadilisha nishati ya jua kuwa chakula kinacholisha viumbe vingine vyote.",
            "explanation_en": "Spot on! Green plants are autotrophic producers that convert radiant solar energy into chemical energy."
        }
    },
    {
        "id": "aquatic_biology_kisumu",
        "title_en": "Aquatic Respiration & Fish Biology (Lake Ecosystem)",
        "title_sw": "Upumuaji wa Samaki: Matamvua/Gills & Ikolojia ya Ziwani",
        "subject": "Biology",
        "cbc_strand": "Living Things & Life Processes (Grade 5/6 Science & Grade 7 Integrated Science)",
        "summary_en": "Fish use specialized feathery gills to extract dissolved oxygen directly from freshwater lakes and oceans while swimming.",
        "summary_sw": "Samaki hutumia matamvua (gills) kuchuja hewa ya oksijeni iliyoyeyuka majini ili kupumua chini ya ziwa au bahari bila mapafu.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria kichwa cha samaki Ngege. Kando ya kichwa kuna vifuniko viwili vya mashavu vinavyofunguka na kufungika. Ndani yake kuna vijipanga vyekundu vyenye manyoya membamba (matamvua) vinavyofanya kazi kama chujio la chai—maji yakipita, oksijeni inakamatwa na kuingizwa kwenye damu!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Samaki anayeogelea] + [Matamvua/Gills yanayopumua] + [Chujio linalovuta Oksijeni kutoka kwenye Maji].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Dunga Beach Kisumu, wavuvi wanapovua samaki Ngege (Tilapia) na Mbuta (Nile Perch), ukiangalia mashavuni utaona matamvua mekundu yaliyojaa mishipa ya damu ya kuchuja oksijeni ya Ziwa Victoria!",
                "analogy_en": "At Dunga Beach in Kisumu, fresh Tilapia and Nile Perch show bright red gills packed with blood vessels extracting dissolved oxygen from lake water!"
            },
            "coastal": {
                "analogy_sw": "Pwani kule Malindi na Mombasa, samaki wa matumbawe na papa hutumia matamvua yao kupumua maji ya chumvi ya Bahari Hindi!",
                "analogy_en": "At coastal marine reefs, reef fish and sharks use gills to extract oxygen from warm Indian Ocean waters!"
            },
            "highlands": {
                "analogy_sw": "Kule milimani Mt. Kenya kwenye mito yenye baridi, samaki wa Trout wanahitaji maji yanayotiririka kwa kasi kwa sababu yana oksijeni nyingi ya kupumua kupitia matamvua!",
                "analogy_en": "In fast-flowing highland mountain streams, trout fish rely on well-oxygenated water passing across their gills!"
            },
            "arid": {
                "analogy_sw": "Kule Ziwa Turkana (Bahari ya Shamu), samaki wa Kambale wana viungo maalum vinavyowasaidia kupumua hata wakati maji yanapopungua wakati wa kiangazi!",
                "analogy_en": "In Lake Turkana, mudfish have adapted accessory breathing organs allowing them to survive when water levels drop in dry seasons!"
            },
            "urban": {
                "analogy_sw": "Kwenye vidimbwi vya samaki vya shule za jiji, maji hupigwa pampu ili kuongeza viputo vya hewa ya oksijeni kwa ajili ya matamvua ya samaki!",
                "analogy_en": "In urban school aquaculture ponds, aerators bubble oxygen into water so fish gills can function efficiently!"
            }
        },
        "key_terms": [
            {"en": "Gills (Branchiae)", "sw": "Matamvua / Mashavu (Viungo vya kupumulia samaki)"},
            {"en": "Dissolved Oxygen", "sw": "Oksijeni Iliyoyeyuka Majini"},
            {"en": "Operculum", "sw": "Kifuniko cha Shavu la Samaki"},
            {"en": "Capillaries", "sw": "Mishipa midogo ya damu ya matamvuani"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuangalia Mwendo wa Mashavu ya Samaki",
            "title_en": "Experiment: Observing Fish Operculum Rhythm",
            "materials_sw": "Samaki hai kwenye beseni au kidimbwi cha maji safi.",
            "materials_en": "Live fish in an aquarium, transparent bowl or school pond.",
            "steps_sw": "1. Tazama samaki anavyofungua mdomo wake na kufunga mashavu.\n2. Maji yanaingia mdomoni na kutoka kupitia matamvua.\n3. Hesabu mara ngapi mashavu yanafunguka kwa dakika moja kuona kasi ya upumuaji!",
            "steps_en": "1. Watch the fish open its mouth while closing its opercular gill flaps.\n2. Water enters the mouth and flows out over the gill filaments.\n3. Count how many gill beats occur per minute!"
        },
        "quiz": {
            "question_sw": "Samaki hutumia kiungo gani kupumua na kuchukua oksijeni iliyoyeyuka ndani ya maji?",
            "question_en": "Which organ do fish use to breathe dissolved oxygen in water?",
            "options_sw": ["A) Matamvua / Mashavu (Gills)", "B) Mapezi ya mgongoni", "C) Magamba ya nje", "D) Mkia"],
            "options_en": ["A) Gills (Matamvua)", "B) Dorsal fins", "C) Scales", "D) Tail"],
            "correct_index": 0,
            "explanation_sw": "Hodari sana! Samaki hutumia matamvua (gills) kuchuja oksijeni moja kwa moja kutoka kwenye maji ya ziwa au bahari.",
            "explanation_en": "Brilliant! Fish use their feathery gills to extract dissolved oxygen directly from water."
        }
    },
    {
        "id": "human_excretion_kidney",
        "title_en": "Excretory System: Kidneys & Waste Removal",
        "title_sw": "Mfumo wa Utoaji Taka Mwilini na Figo",
        "subject": "Biology",
        "cbc_strand": "Human Body Systems & Health (Grade 7/8 Integrated Science)",
        "summary_en": "The kidneys act as biological filters that clean the blood, remove toxic urea waste and excess salts as urine, and balance body water.",
        "summary_sw": "Figo hufanya kazi kama chujio la kibiolojia linalosafisha damu, kuondoa taka zenye sumu (urea) na chumvi iliyozidi kwa njia ya mkojo, na kusawazisha maji mwilini.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Weka mikono yako miwili kiunoni upande wa nyuma wa mgongo chini kidogo ya mbavu zako. Hapo ndipo zilipo figo zako mbili zenye umbo la mbegu ya maharagwe. Zinasafisha lita 180 za damu kila siku!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kushika Kiuno Nyuma] ➔ [Figo mbili zinazochuja Damu] ➔ [Uchafu unatoka kwa Mkojo] ➔ [Damu Safi inarudi Mwilini].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kama mtambo wa maji wa Dunga Kisumu unavyochuja maji ya ziwa kuondoa tope na uchafu, figo zako zinachuja damu yako masaa 24 kuondoa sumu ya urea!",
                "analogy_en": "Just as municipal water plants filter lake water to remove impurities, your kidneys continuously filter your blood to eliminate urea toxins!"
            },
            "coastal": {
                "analogy_sw": "Pwani kwenye joto kali unapotoa jasho jingi, figo zako zinabana maji ili mwili usikauke, na mkojo unakuwa wa njano iliyokoza kuokoa unyevu!",
                "analogy_en": "At the hot coast when sweating heavily, your kidneys reabsorb water to prevent dehydration, producing concentrated urine!"
            },
            "highlands": {
                "analogy_sw": "Milimani kwenye baridi ambapo hutoi jasho, figo zako hutoa maji ya ziada kwa njia ya mkojo mwepesi ili kudumisha uwiano sahihi wa maji!",
                "analogy_en": "In cold highlands where sweat evaporation is low, kidneys excrete excess water as clear urine to maintain fluid balance!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame ya Garissa na Turkana, figo za ngamia na binadamu zina uwezo mkubwa wa kubana maji na madini ili kuwezesha kuishi kwa siku nyingi bila maji!",
                "analogy_en": "In arid desert zones, renal tubules reabsorb maximal water and salts to preserve vital hydration during droughts!"
            },
            "urban": {
                "analogy_sw": "Mtaani, figo zinafanya kazi kama mfumo wa kuchuja maji taka ya jiji, zikiruhusu maji safi kurudi kwenye mzunguko na kutupa uchafu nje!",
                "analogy_en": "In modern cities, the renal system acts like an advanced wastewater treatment facility, recycling pure plasma!"
            }
        },
        "key_terms": [
            {"en": "Kidneys (Nephrons)", "sw": "Figo na Nefroni (Vitengo vidogo vya kuchuja damu)"},
            {"en": "Urea", "sw": "Urea (Taka ya kikemia inayotokana na protini)"},
            {"en": "Ureters & Bladder", "sw": "Mirija ya Mkojo na Kibofu cha Kuhifadhia"},
            {"en": "Osmoregulation", "sw": "Udhibiti wa Maji na Chumvi Mwilini"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuelewa Uchujaji wa Figo kwa Kutumia Chujio la Chai",
            "title_en": "Experiment: Tea Strainer Filtration Analogy",
            "materials_sw": "Chujio la chai, maji yenye mchanga na majani, kikombe kisafi.",
            "materials_en": "Tea strainer/filter, water with soil and tea leaves, clean cup.",
            "steps_sw": "1. Mimina maji yenye majani kupitia chujio.\n2. Majani yanabaki juu (kama chembe za damu na protini zinavyobaki mwilini).\n3. Maji safi yanapita chini—hivyo ndivyo Nefroni za figo zinavyochuja damu!",
            "steps_en": "1. Pour murky liquid through a mesh filter.\n2. Large particles stay behind (like blood cells and proteins).\n3. Filtered fluid passes through—demonstrating nephron filtration!"
        },
        "quiz": {
            "question_sw": "Ni kiungo kipi kikuu mwilini kinachohusika na kuchuja damu na kutoa taka ya urea kwa njia ya mkojo?",
            "question_en": "Which major organ is responsible for filtering blood and removing urea waste as urine?",
            "options_sw": ["A) Figo (Kidneys)", "B) Mapafu", "C) Tumbo", "D) Meno"],
            "options_en": ["A) Kidneys", "B) Lungs", "C) Stomach", "D) Teeth"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Figo mbili huchuja damu masaa 24 na kutoa taka zenye sumu kwa njia ya mkojo kupitia kibofu.",
            "explanation_en": "Excellent! Kidneys contain millions of nephrons filtering blood and expelling urea waste through the bladder."
        }
    },
    {
        "id": "nervous_sense_organs",
        "title_en": "Nervous System, Brain & Sense Organs",
        "title_sw": "Mfumo wa Neva, Ubongo na Viungo vya Hisia",
        "subject": "Biology",
        "cbc_strand": "Human Body & Control Systems (Grade 7/8 Integrated Science)",
        "summary_en": "The nervous system uses electrical nerve impulses between the brain, spinal cord, and 5 sense organs (eyes, ears, skin, nose, tongue) to detect and respond to changes.",
        "summary_sw": "Mfumo wa neva hutumia mawimbi ya umeme wa kibiolojia kati ya ubongo, uti wa mgongo, na viungo 5 vya hisia (macho, masikio, ngozi, pua, ulimi) ili kutambua na kutenda.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Gusa ncha ya kidole chako kwenye meza au nguo yako. Hisi jinsi unavyotambua ulaini au ukali papo hapo. Hiyo ni kwa sababu neva za ngozi zilituma ujumbe wa umeme wa kasi ya ajabu hadi kwenye ubongo wako kuutafsiri!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kugusa kitu chenye Moto] ➔ [Neva zinatuma Ujumbe wa Haraka kwenye Ubongo] ➔ [Mkono unajivuta papo hapo / Reflex Action].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kama mtandao wa simu wa Safaricom huko Kisumu unaotuma ujumbe wa SMS kwa sekunde moja, neva zako zinatuma jumbe za hisia hadi kwenye ubongo wako!",
                "analogy_en": "Like cellular networks delivering SMS messages instantly, sensory nerves transmit electrical signals to your brain within milliseconds!"
            },
            "coastal": {
                "analogy_sw": "Pwani unaposikia harufu nzuri ya pilau au upepo wa bahari kwenye ngozi, viungo vyako vya hisia vinatafsiriwa papo hapo na ubongo wako!",
                "analogy_en": "At the coast when smelling spiced pilau or feeling ocean breezes, sensory receptors relay signals directly to the brain cortex!"
            },
            "highlands": {
                "analogy_sw": "Mashambani unaposikia mlio wa ngurumo ya radi au ndege wakiimba asubuhi, ngoma ya sikio lako inatuma mawimbi ya neva kwenye ubongo ili utambue sauti!",
                "analogy_en": "In highland farms when hearing thunder or birdsong, the eardrum vibrates to send auditory nerve signals to the brain!"
            },
            "arid": {
                "analogy_sw": "Kwenye jua kali la jangwani, macho yako yanapunguza ukubwa wa mboni (pupil) kiotomatiki ili kulinda retina isiumizwe na mwangaza mkali!",
                "analogy_en": "In bright desert sunshine, eye pupils automatically constrict to protect the retina from excessive light!"
            },
            "urban": {
                "analogy_sw": "Mtaani unapovuka barabara na kusikia honi ya matatu, mfumo wa neva unafanya mwili wako uruke kando mara moja (Reflex Action) ili kukuokoa!",
                "analogy_en": "In city streets, hearing a vehicle horn triggers an immediate spinal reflex action to jump to safety!"
            }
        },
        "key_terms": [
            {"en": "Brain & Spinal Cord", "sw": "Ubongo na Uti wa Mgongo (Kituo Kikuu cha Udhibiti)"},
            {"en": "Neurons & Nerves", "sw": "Neva na Nyuroni (Waya za umeme wa mwilini)"},
            {"en": "Sense Organs", "sw": "Viungo vya Hisia (Macho, Masikio, Ngozi, Pua, Ulimi)"},
            {"en": "Reflex Action", "sw": "Kitendo cha Haraka cha Kujilinda (Reflex)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kupima Kasi ya Majibu ya Neva (Ruler Drop Reflex Test)",
            "title_en": "Experiment: Ruler Drop Reaction Time Test",
            "materials_sw": "Rula ya sentimita 30, rafiki au mzazi.",
            "materials_en": "30 cm ruler, friend or parent.",
            "steps_sw": "1. Rafiki ashimshike rula wima juu ya kiganja chako.\n2. Aiachie bila kukuambia.\n3. Daka rula haraka uwezavyo kwa vidole viwili.\n4. Angalia nambari ya sentimita uliyodaka—kadri nambari ilivyo ndogo, ndivyo neva zako zilivyo na kasi zaidi!",
            "steps_en": "1. Have a friend hold a ruler vertically above your open hand.\n2. They release it without warning.\n3. Catch it between thumb and index finger as fast as possible.\n4. Check the cm mark caught—lower numbers indicate faster reaction speed!"
        },
        "quiz": {
            "question_sw": "Ni kituo gani kikuu cha mfumo wa neva kinachopokea taarifa kutoka kwa viungo vyote vya hisia na kuongoza maamuzi ya mwili?",
            "question_en": "Which central organ of the nervous system processes information from all sense organs and coordinates body decisions?",
            "options_sw": ["A) Ubongo (Brain)", "B) Ini", "C) Kucha", "D) Nywele"],
            "options_en": ["A) Brain", "B) Liver", "C) Nails", "D) Hair"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! Ubongo ndio kituo kikuu cha kompyuta ya mwili kinachoongoza fikra, kumbukumbu, na hisia zote.",
            "explanation_en": "Brilliant! The brain is the central control unit processing sensory data, memory, and voluntary actions."
        }
    },
    {
        "id": "plant_transpiration_transport",
        "title_en": "Plant Transport: Xylem, Phloem & Transpiration",
        "title_sw": "Usafirishaji wa Maji na Chakula kwenye Mimea (Transpiration)",
        "subject": "Biology",
        "cbc_strand": "Plants & Environmental Adaptation (Grade 7/8 Integrated Science)",
        "summary_en": "Plants draw water and mineral salts up from roots through Xylem tubes via transpiration pull, while Phloem distributes manufactured food from leaves to roots.",
        "summary_sw": "Mimea huvuta maji na madini kutoka ardhini kupitia mirija ya Xylem kwa nguvu ya uvukizi (transpiration), huku mirija ya Phloem ikisambaza chakula kutoka majanini.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Shika shina la mmea au bua la sukuma/seleri mkononi mwako. Ndani ya shina kuna mirija midogo mifano ya mrija wa kunywea soda: Mirija ya Xylem inavuta maji juu, na Phloem inashusha chakula chini!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Mizizi inanyonya Maji Ardhini] ➔ [Mshale unapanda juu kupitia Xylem] ➔ [Mvuke unatoka majanini / Transpiration] ➔ [Chakula kinasambazwa kupitia Phloem].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule mashambani Kisumu na Kakamega, miti mikubwa ya msitu wa Kakamega inavuta mamia ya lita za maji kutoka udongoni kupitia mirija ya Xylem na kutoa mvuke unaotengeneza mawingu ya mvua!",
                "analogy_en": "In Kakamega Forest, towering indigenous trees pull hundreds of liters of water through Xylem tubes, exhaling vapor that fuels rainfall cycles!"
            },
            "coastal": {
                "analogy_sw": "Pwani, miti ya minazi inavuta maji ya ardhini hadi juu kabisa kwenye nazi mita 20 angani kupitia nguvu thabiti ya Transpiration Pull!",
                "analogy_en": "Along coastal groves, tall coconut palms pull ground water 20 meters high into coconuts using transpiration pull!"
            },
            "highlands": {
                "analogy_sw": "Kule Nyeri na Meru kwenye mashamba ya migomba ya ndizi, mashina yenye maji mengi yamejaa mirija ya Xylem inayolisha ndizi manono!",
                "analogy_en": "In highland banana groves, fleshy pseudostems are packed with vascular bundles feeding heavy fruit bunches!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame ya Wajir, mimea ina tabaka nene la nta (cuticle) juu ya majani ili kupunguza uvukizi wa maji na kuhifadhi unyevu!",
                "analogy_en": "In arid ASAL zones, desert shrubs feature thick waxy cuticles that reduce transpiration loss during scorching heat!"
            },
            "urban": {
                "analogy_sw": "Mtaani, usafirishaji wa maji kwenye mti unafanana na mfumo wa mabomba ya ghorofa inayotumia pampu kuvuta maji kutoka tenki la chini hadi ghorofa ya juu!",
                "analogy_en": "In urban buildings, plant vascular transport mirrors multi-story plumbing systems drawing water from ground tanks to rooftops!"
            }
        },
        "key_terms": [
            {"en": "Xylem Vessels", "sw": "Mirija ya Xylem (Inasafirisha maji na madini juu)"},
            {"en": "Phloem Tissue", "sw": "Mirija ya Phloem (Inasafirisha sukari na chakula)"},
            {"en": "Transpiration", "sw": "Uvukizi wa Maji Majanini (Transpiration)"},
            {"en": "Root Hairs", "sw": "Vinyweleo vya Mizizi (Vinafyonza maji ardhini)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Mirija ya Xylem Ikipitisha Rangi Kwenye Shina",
            "title_en": "Experiment: Colored Water Vascular Transport in Celery/Kales",
            "materials_sw": "Shina la sukuma au ua jeupe, glasi ya maji yenye wino wa bluu au nyekundu.",
            "materials_en": "Stalk of kale/celery or white flower, cup of water with food coloring or ink.",
            "steps_sw": "1. Weka shina la sukuma ndani ya maji ya rangi nyekundu au bluu.\n2. Iache kwa masaa 4 juani.\n3. Kata shina kwa katikati—utaona vitone vya rangi ndani ya mirija ya Xylem vikithibitisha maji yamepanda juu!",
            "steps_en": "1. Place a fresh stem into colored water.\n2. Leave in sunlight for 4 hours.\n3. Cut the stem crosswise to observe colored Xylem vessels that transported dyed water upward!"
        },
        "quiz": {
            "question_sw": "Ni mirija gani ndani ya mmea inayohusika na kusafirisha maji na madini chumvi kutoka mizizini kuelekea majanini?",
            "question_en": "Which plant vascular tissue transports water and dissolved mineral salts upward from roots to leaves?",
            "options_sw": ["A) Mirija ya Xylem", "B) Mirija ya Phloem", "C) Magome tu", "D) Maua"],
            "options_en": ["A) Xylem Vessels", "B) Phloem Tissue", "C) Bark only", "D) Flowers"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Xylem husafirisha maji na madini kutoka mizizini kwenda juu, wakati Phloem husambaza chakula cha glukosi mmea mzima.",
            "explanation_en": "Spot on! Xylem vessels conduct water and minerals upward, while Phloem distributes synthesized sugars."
        }
    },
    {
        "id": "skeletal_muscular_system",
        "title_en": "Skeletal & Muscular System: Movement & Support",
        "title_sw": "Mfumo wa Mifupa na Misuli: Mwendo na Mhimili wa Mwili",
        "subject": "Biology",
        "cbc_strand": "Human Body Systems (Grade 5/6 Science & Grade 7 Integrated Science)",
        "summary_en": "The human skeleton (206 bones) provides body framework and protects vital organs, while antagonistic pairs of muscles (like biceps and triceps) contract to create movement.",
        "summary_sw": "Mifupa ya binadamu (mifupa 206) inasimamisha mwili na kulinda viungo vya ndani, huku jozi za misuli (kama misuli ya mkono) ikijivuta na kulegea ili kuwezesha mwendo.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Kunja mkono wako kwenye kiwiko ulete kiganja kifuani. Shika sehemu ya juu ya mkono wako—utahisi donge gumu la msuli (Biceps) likijivuta. Nyosha mkono tena—utahisi msuli wa chini (Triceps) ukifanya kazi!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kukunja Mkono] ➔ [Misuli ya Biceps inajikunja na Mifupa inainuka] ➔ [Kunyosha Mkono / Triceps inajikunja].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kama ubao imara wa mashua ya Dunga Beach unavyounda fremu ya mashua ili isizame ziwani, kiunzi chako cha mifupa kinalinda mapafu na moyo wako!",
                "analogy_en": "Just as strong timber ribs form the hull framework of Lake Victoria canoes, your skeletal ribcage protects your heart and lungs!"
            },
            "coastal": {
                "analogy_sw": "Pwani, wanariadha na waogeleaji hutumia viungo vya mabega (ball-and-socket joints) vinavyoruhusu mkono kuzunguka pande zote ndani ya maji!",
                "analogy_en": "At the coast, swimmers utilize flexible ball-and-socket shoulder joints providing full 360-degree rotational mobility!"
            },
            "highlands": {
                "analogy_sw": "Milimani unapopanda vilima vya Kericho na Nyahururu, misuli ya mapaja (quadriceps) na mifupa ya magoti (hinge joints) inastahimili uzito wote wa mwili!",
                "analogy_en": "In highland terrains, robust femur thigh bones and knee hinge joints bear dynamic body loads during steep ascents!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame, miguu mirefu na imara ya ngamia ina viungo vyenye unyumbulifu mkubwa wa kutembea kwenye mchanga bila kuchoka!",
                "analogy_en": "In sandy arid expanses, camels feature elongated limbs and broad elastic foot pads distributing mechanical weight evenly!"
            },
            "urban": {
                "analogy_sw": "Mtaani, mifupa na misuli hufanya kazi kama chuma cha 'crane' ya ujenzi wa ghorofa yenye nyaya za chuma (misuli na tendons) zinazonyanyua mizigo mizito!",
                "analogy_en": "In urban construction sites, musculoskeletal mechanics function like crane pulleys with tendons acting as steel tension cables!"
            }
        },
        "key_terms": [
            {"en": "Skeleton & Bones (206)", "sw": "Kiunzi cha Mifupa (Mifupa 206 mwilini)"},
            {"en": "Antagonistic Muscles (Biceps/Triceps)", "sw": "Jozi za Misuli Zinazopingana"},
            {"en": "Joints (Hinge & Ball-and-Socket)", "sw": "Viungo vya Mifupa (Kiwiko, Goti, Bega)"},
            {"en": "Cartilage & Ligaments", "sw": "Ugeghedi na Kamba za Viungo"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kutengeneza Mfano Rahisi wa Mkono na Misuli ya Kadibodi",
            "title_en": "Experiment: Cardboard & String Robotic Arm Model",
            "materials_sw": "Vipande viwili vya kadibodi, pini au msumari mdogo, nyuzi mbili za sufu.",
            "materials_en": "Two cardboard strips, split pin, two pieces of yarn string.",
            "steps_sw": "1. Unganisha vipande viwili vya kadibodi kwa pini (kutengeneza kiwiko cha goti/mkono).\n2. Funga uzi mmoja juu (Biceps) na uzi mmoja chini (Triceps).\n3. Vuta uzi wa juu—mkono unakunja! Vuta uzi wa chini—mkono unanyooka!",
            "steps_en": "1. Join two cardboard strips with a pin to create a hinge joint.\n2. Attach yarn across the top (biceps) and bottom (triceps).\n3. Pull the top string to flex, pull bottom string to extend!"
        },
        "quiz": {
            "question_sw": "Ni aina gani ya kiungo cha mfupa kinachopatikana kwenye kiwiko cha mkono na goti kinachoruhusu mwendo wa kuelekea upande mmoja kama bawaba ya mlango?",
            "question_en": "Which type of joint found at the elbow and knee operates like a door hinge?",
            "options_sw": ["A) Kiungo cha Bawaba (Hinge Joint)", "B) Kiungo cha Mpira (Ball & Socket)", "C) Mfupa laini", "D) Nywele"],
            "options_en": ["A) Hinge Joint", "B) Ball and Socket Joint", "C) Soft bone", "D) Hair"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Kiungo cha bawaba (Hinge joint) hupatikana kwenye magoti na viwiko, kikifunguka na kufungika kama mlango.",
            "explanation_en": "Brilliant! Hinge joints at the elbow and knee allow uniaxial bending motion just like a door hinge."
        }
    },
    {
        "id": "microorganisms_health",
        "title_en": "Microorganisms, Immunity & Disease Prevention",
        "title_sw": "Vimelea Vidogo (Microorganisms), Kinga ya Mwili na Usafi",
        "subject": "Biology",
        "cbc_strand": "Health Education & Infectious Diseases (Grade 6/7 Integrated Science)",
        "summary_en": "Microorganisms include beneficial bacteria (like yogurt fermenters) and harmful pathogens (bacteria, viruses, fungi). The immune system uses white blood cells to defend the body.",
        "summary_sw": "Vimelea vidogo ni pamoja na bakteria wazuri (kama wa kugandisha mtindi/maziwa lala) na vijidudu vya magonjwa. Chembechembe nyeupe za damu huunda jeshi la kinga mwilini.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Osha mikono yako kwa sabuni na maji tiririka. Hisi povu la sabuni likisafisha ngozi yako. Povu la sabuni linavunja utando wa vijidudu vidogo visivyoonekana kwa macho na kuvisafisha nje ya mikono yako!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Kuosha Mikono kwa Sabuni] ➔ [Vijidudu vinavyokufa] ➔ [Chembechembe Nyeupe za Damu zikipambana na Vijidudu ndani ya Mwili].",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule vijijini Kisumu na Siaya, wazazi wanapotengeneza maziwa lala au mtindi mtamu, bakteria wazuri wa 'Lactobacillus' wanachachisha maziwa na kuzuia vijidudu vibaya visikue!",
                "analogy_en": "In rural lake communities, preparing traditional fermented sour milk (Maziwa Lala) uses beneficial Lactobacillus bacteria to preserve nutrients!"
            },
            "coastal": {
                "analogy_sw": "Pwani kule Mombasa, kuweka chandarua chenye dawa (ITN) kunazuia mbu wa Anopheles anayebeba kimelea cha Plasmodium kinachosababisha Malaria!",
                "analogy_en": "At the coast, sleeping under insecticide-treated nets prevents Anopheles mosquitoes from transmitting malaria Plasmodium parasites!"
            },
            "highlands": {
                "analogy_sw": "Mashambani, wakulima hutumia mbolea ya samadi iliyooza ambapo mabilioni ya bakteria na kuvu wazuri wamelainisha majani kuwa mbolea ya rutuba!",
                "analogy_en": "In highland farms, compost heaps harness billions of beneficial decomposing microbes to enrich soil fertility!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame ya kaskazini, kuchemsha maji ya visima kunaua bakteria wote wa Kipindupindu na kuhara na kulinda jamii nzima!",
                "analogy_en": "In northern pastoral communities, boiling borehole water eliminates waterborne pathogens like cholera and amoeba!"
            },
            "urban": {
                "analogy_sw": "Mtaani, chanjo za watoto kliniki zinafundisha jeshi la chembechembe nyeupe za damu (White Blood Cells) kutambua na kushinda virusi kabla havijaleta ugonjwa!",
                "analogy_en": "In urban clinics, routine childhood immunizations train white blood cells to produce defensive antibodies against viruses!"
            }
        },
        "key_terms": [
            {"en": "Microorganisms / Microbes", "sw": "Vimelea Vidogo visivyoonekana kwa macho"},
            {"en": "Beneficial Bacteria (Probiotics)", "sw": "Bakteria Wazuri (Mfano: Fermentation ya Mtindi)"},
            {"en": "Pathogens & Viruses", "sw": "Vijidudu vya Magonjwa na Virusi"},
            {"en": "White Blood Cells & Antibodies", "sw": "Chembechembe Nyeupe za Damu & Kingamwili"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Ukuaji wa Kuvu Kwenye Mkate (Fungi Mold Test)",
            "title_en": "Experiment: Bread Mold Moisture Colony Test",
            "materials_sw": "Vipande viwili vya mkate, matone 3 ya maji, mifuko miwili ya nailoni safi.",
            "materials_en": "Two bread slices, 3 water droplets, two zip plastic bags.",
            "steps_sw": "1. Weka kipande kimoja cha mkate kavu kwenye mfuko A.\n2. Weka kipande cha pili chenye matone machache ya maji kwenye mfuko B.\n3. Funga mifuko yote miwili na uiache kwa siku 4.\n4. Mfuko B utaota unga wa kijani wa Kuvu (Mold)—kuthibitisha vijidudu vinahitaji unyevu na joto kukua!",
            "steps_en": "1. Place dry bread in sealed bag A.\n2. Place slightly dampened bread in sealed bag B.\n3. Keep both in a warm cupboard for 4 days.\n4. Observe fungal mold spores proliferating on moist bread B!"
        },
        "quiz": {
            "question_sw": "Ni chembechembe gani ndani ya damu ya binadamu zinazofanya kazi kama 'askari' wa kupambana na vijidudu na kutoa kinga mwilini?",
            "question_en": "Which blood cells function like body defense soldiers, destroying invading disease pathogens?",
            "options_sw": ["A) Chembechembe Nyeupe za Damu (White Blood Cells)", "B) Nywele", "C) Mifupa", "D) Mate"],
            "options_en": ["A) White Blood Cells (Leukocytes)", "B) Hair", "C) Bones", "D) Saliva"],
            "correct_index": 0,
            "explanation_sw": "Sahihi kabisa! Chembechembe nyeupe za damu (White Blood Cells) huzalisha kingamwili za kupigana na magonjwa na kuua vijidudu.",
            "explanation_en": "Spot on! White blood cells produce neutralizing antibodies and engulf harmful pathogens."
        }
    },
    {
        "id": "genetics_dna_heredity",
        "title_en": "Genetics, DNA & Heredity: How Traits are Inherited",
        "title_sw": "Jenetiki, DNA na Urithi wa Tabia: Jinsi Sifa Zinavyorithiwa",
        "subject": "Biology",
        "cbc_strand": "Genetics, Heredity & Evolution (Grade 8/9 Integrated Science & Senior Secondary Biology)",
        "summary_en": "Genetics explores how traits (eye color, height, blood group, crop yield) pass from parents to offspring via DNA, genes, and chromosomes following Gregor Mendel's laws.",
        "summary_sw": "Jenetiki huchunguza jinsi sifa za kimwili (urefu, rangi ya macho, kundi la damu, mavuno ya mbegu) zinavyorithiwa kutoka kwa wazazi kwenda kwa watoto kupitia DNA na jeni kulingana na sheria za Gregor Mendel.",
        "tactile_audio_description_sw": "Kwa wanafunzi wasioona: Fikiria kamba ndefu ya herufi zilizosokotwa kwa namna ya ngazi inayozunguka (Double Helix). Kila ngazi ndogo inashikilia maelekezo ya jinsi mwili wako utakavyokua, kuanzia urefu wako hadi unene wa sauti yako!",
        "sign_language_visual_cues_sw": "Kwa wanafunzi wasiosikia: [Ishara ya Wazazi (Baba + Mama)] ➔ [Kusokota Nyuzi za DNA] ➔ [Sifa za Mtoto (Kufanana Sura au Urefu)]. Angalia jedwali la Punnett Square: Jeni kuu (Dominant) na jeni hafifu (Recessive).",
        "regional_analogies": {
            "lake_basin": {
                "analogy_sw": "Kule Kisumu na Siaya, tazama ng'ombe wa kienyeji wa Zebu (wenye nundu na ustahimilivu wa joto) wakizalishwa na ng'ombe wa kisasa wa maziwa kupata ndama wa chotara (Hybrid) anayerithi sifa ya kutoa maziwa mengi huku akistahimili kupe na joto la ziwani!",
                "analogy_en": "In Lake Victoria communities, cross-breeding indigenous heat-resistant Zebu cattle with high-yielding dairy breeds produces hybrid calves inheriting both disease tolerance and high milk production!"
            },
            "coastal": {
                "analogy_sw": "Pwani kule Kilifi na Kwale, minazi mirefu ya asili inapopandikizwa na minazi mifupi ya mseto (Dwarf Hybrids), kizazi kipya kinarithi jeni za kukua haraka na kuzaa nazi tamu nyingi bila kupanda miti mirefu!",
                "analogy_en": "In coastal palm groves, hybrid cross-pollination between tall indigenous palms and dwarf varieties yields progeny with rapid maturation and heavy sweet coconut yields!"
            },
            "highlands": {
                "analogy_sw": "Mashambani kule Kitale, Nakuru na Nyeri, wakulima hupanda mbegu za mahindi ya chotara (Hybrid Maize kama H614) ambayo yamerithi jeni zenye nguvu za kutoa mahindi makubwa yenye punje nyingi!",
                "analogy_en": "In highland agricultural zones, hybrid maize varieties combine parental genetics to achieve vigorous growth (heterosis), high grain yield, and fungal resistance!"
            },
            "arid": {
                "analogy_sw": "Kwenye maeneo kame ya kaskazini, mbuzi wa asili wa Galla wanarithisha jeni za kustahimili ukame mkali na kutoa maziwa hata wakati wa kiangazi kirefu!",
                "analogy_en": "In arid pastoral regions, Galla goats pass down resilient genetic traits allowing sustained lactation and drought tolerance!"
            },
            "urban": {
                "analogy_sw": "Mtaani, unaweza kuona jinsi unavyofanana na wazazi wako kwa kuangalia jeni kama vile uwezo wa kukunjakunja ulimi (Tongue Rolling Gene) au kuwa na vishimo vya mashavu (Dimples)!",
                "analogy_en": "In daily life, observable inherited traits like tongue rolling ability, attached earlobes, and cheek dimples demonstrate dominant and recessive genetic inheritance!"
            }
        },
        "key_terms": [
            {"en": "DNA (Deoxyribonucleic Acid)", "sw": "DNA (Msimbo wa maisha ulio ndani ya kiini cha seli)"},
            {"en": "Gene (Unit of Heredity)", "sw": "Jeni (Sehemu ya DNA inayobeba sifa maalum)"},
            {"en": "Chromosomes (46 in humans)", "sw": "Kromosomu (Nyuzi 46 za DNA ndani ya kiini)"},
            {"en": "Dominant vs Recessive", "sw": "Jeni Yenye Nguvu (Dominant) na Iliyojificha (Recessive)"},
            {"en": "Gregor Mendel & Punnett Square", "sw": "Gregor Mendel na Jedwali la Urithi la Punnett"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Uchunguzi wa Sifa za Kurithi Mwilini (Family Genetic Traits Survey)",
            "title_en": "Experiment: Human Genetic Traits Survey & Punnett Model",
            "materials_sw": "Kalamu na karatasi, kioo cha kujiangalia, wanafamilia au marafiki 2-3.",
            "materials_en": "Pen and paper, small mirror, 2-3 family members or classmates.",
            "steps_sw": "1. Jaribu kukunjakunja ulimi wako uwe kama bomba la duara (Tongue rolling). Hii ni sifa ya jeni yenye nguvu (Dominant gene)!\n2. Angalia kwenye kioo kama mashina ya masikio yako yameungana na shingo au yako huru (Free vs Attached earlobes).\n3. Waulize wanafamilia yako—chora orodha kuona nani anashiriki sifa hizi za DNA na wewe!",
            "steps_en": "1. Try to roll the edges of your tongue into a U-tube shape—this is a dominant genetic allele!\n2. Check in a mirror whether your earlobes are free or attached.\n3. Survey your relatives to map how these dominant and recessive traits travel across generations!"
        },
        "quiz": {
            "question_sw": "Ni molekuli gani iliyo ndani ya kiini cha seli inayobeba maelekezo na msimbo wote wa kurithi sifa kutoka kwa wazazi kwenda kwa watoto?",
            "question_en": "Which molecule located within cell nuclei carries the hereditary genetic blueprint passed from parents to offspring?",
            "options_sw": ["A) DNA na Jeni (DNA & Genes)", "B) Maji safi ya kunywa", "C) Mifupa ya miguu", "D) Mate ya mdomo"],
            "options_en": ["A) DNA & Genes", "B) Drinking water", "C) Leg bones", "D) Saliva"],
            "correct_index": 0,
            "explanation_sw": "Hongera sana! DNA ndiyo molekuli ya urithi inayobeba jeni zenye maelekezo yote ya jinsi kiumbe kitakavyofanana na kukuza sifa zake.",
            "explanation_en": "Spot on! Deoxyribonucleic Acid (DNA) is the hereditary material containing the genetic code for all organismal traits."
        }
    }
]

