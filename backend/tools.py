"""
ElewaSTEM Specialized Agent Tools
Provides localized STEM analogies, bilingual quiz generators, at-home experiments, and offline starter modules.
"""

from typing import Dict, List, Any


OFFLINE_STEM_VAULT = [
    {
        "id": "photosynthesis",
        "title_en": "Photosynthesis: How Plants Make Food",
        "title_sw": "Usanisinuru: Jinsi Mimea Inavyotengeneza Chakula",
        "subject": "Biology",
        "summary_en": "Plants use sunlight, water, and carbon dioxide from the air to cook their food (glucose) and release fresh oxygen.",
        "summary_sw": "Mimea hutumia mwangaza wa jua, maji kutoka ardhini, na hewa ya kaboni kutengeneza chakula chake (glukosi) huku ikitoa hewa safi ya oksijeni.",
        "analogy_sw": "Fikiria jani la mahindi kama jikoni ndogo ya kijani. Mwangaza wa jua ni moto wa jiko, maji ni maji ya kupikia, na hewa ya kaboni ni unga wa ugali!",
        "analogy_en": "Think of a maize leaf as a tiny green kitchen. Sunlight is the cooking fire, water comes from the tap (roots), and carbon dioxide is the flour to cook energy!",
        "key_terms": [
            {"en": "Chlorophyll", "sw": "Klorofili (Rangi ya kijani inayovuta mwangaza)"},
            {"en": "Carbon Dioxide", "sw": "Gesi ya Kaboni Dioksidi"},
            {"en": "Oxygen", "sw": "Hewa Safi ya Oksijeni"},
            {"en": "Glucose", "sw": "Glukosi (Sukari/Chakula cha mmea)"}
        ],
        "experiment": {
            "title_sw": "Jaribio Rahisi: Kushuhudia Oksijeni ya Mmea",
            "title_en": "Simple Experiment: Seeing Plant Oxygen",
            "materials_sw": "Jani bichi, glasi au chupa ya plastiki yenye maji safi, jua.",
            "materials_en": "A fresh green leaf, a clear glass or transparent bottle of water, sunlight.",
            "steps_sw": "1. Weka jani ndani ya chupa ya maji.\n2. Weka chupa juani kwa saa moja.\n3. Tazama viputo vidogo vya hewa vinavyojitokeza kwenye jani - hiyo ni Oksijeni safi!",
            "steps_en": "1. Submerge the leaf inside the glass of water.\n2. Leave it in direct sunlight for 1 hour.\n3. Observe tiny bubbles forming on the leaf surface - that is pure Oxygen being released!"
        },
        "quiz": {
            "question_sw": "Ni kipi mmea unachotoa hewani baada ya kutengeneza chakula (usanisinuru)?",
            "question_en": "What do plants release into the air after making their food (photosynthesis)?",
            "options_sw": ["A) Oksijeni safi", "B) Moshi", "C) Udongo", "D) Maji ya moto"],
            "options_en": ["A) Fresh Oxygen", "B) Smoke", "C) Soil", "D) Hot Water"],
            "correct_index": 0,
            "explanation_sw": "Sahihi! Mimea hutoa gesi ya oksijeni ambayo sisi wanadamu na wanyama tunaivuta ili kuishi.",
            "explanation_en": "Correct! Plants produce oxygen, which humans and animals breathe to stay alive."
        }
    },
    {
        "id": "electricity_circuits",
        "title_en": "Electric Current & Circuits",
        "title_sw": "Mkondo wa Umeme na Saketi",
        "subject": "Physics",
        "summary_en": "Electric current is the flow of tiny electric charges through a closed loop wire, just like water flowing in pipes.",
        "summary_sw": "Mkondo wa umeme ni mwendo wa chembe ndogo za chaji zinazosafiri kwenye waya uliounganishwa bila kukatika, kama maji kwenye mifereji.",
        "analogy_sw": "Battery ni kama tenki la maji lililo juu ya nyumba. Voltage ni shinikizo la maji. Waya ni mifereji, na taa ni kinu cha maji kinachozunguka maji yakipita.",
        "analogy_en": "A battery is like an elevated water tank. Voltage is the water pressure pushing through. The wire is the pipe, and the bulb is a water wheel that spins when water flows!",
        "key_terms": [
            {"en": "Voltage (Volts)", "sw": "Volteji (Shinikizo la kusukuma umeme)"},
            {"en": "Current (Amperes)", "sw": "Kasi/Kiasi cha mkondo wa umeme"},
            {"en": "Resistance (Ohms)", "sw": "Ukinzani (Kizuizi cha mtiririko wa umeme)"},
            {"en": "Closed Circuit", "sw": "Saketi iliyofungwa (Njia kamili ya umeme)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuwasha Taa Ndogo kwa Betri ya Saa",
            "title_en": "Experiment: Lighting a Small Bulb with a Cell Battery",
            "materials_sw": "Betri ndogo ya tochi (1.5V), kijiti cha waya mwembamba, taa ndogo ya LED.",
            "materials_en": "A small torch battery (1.5V), a thin copper wire, a small LED bulb.",
            "steps_sw": "1. Gusa upande wa chini wa taa kwenye sehemu ya juu ya betri (+).\n2. Unganisha waya kutoka chini ya betri (-) hadi pembeni ya taa.\n3. Taa inawaka kwa sababu saketi imekamilika!",
            "steps_en": "1. Touch the bulb base to the top (+) terminal of the battery.\n2. Connect the wire from the bottom (-) terminal to the side of the bulb.\n3. The bulb lights up because the circuit is complete!"
        },
        "quiz": {
            "question_sw": "Nini kitatokea ikiwa waya wa saketi ya umeme utakatika?",
            "question_en": "What happens if a wire in an electrical circuit is cut or broken?",
            "options_sw": ["A) Taa itazimika kwa sababu njia imekatika", "B) Taa itawaka zaidi", "C) Betri itajaa maji", "D) Hakuna kitakachobadilika"],
            "options_en": ["A) The light bulb turns off because the path is open", "B) The bulb glows brighter", "C) The battery fills with water", "D) Nothing changes"],
            "correct_index": 0,
            "explanation_sw": "Vizuri sana! Umeme unahitaji njia iliyofungwa kikamilifu (closed circuit) ili uweze kutiririka.",
            "explanation_en": "Great job! Electricity requires a continuous, closed circuit to flow."
        }
    },
    {
        "id": "gravity_forces",
        "title_en": "Gravity & Friction: The Invisible Pullers",
        "title_sw": "Mvuto wa Ardhi (Grabiti) na Msuguano",
        "subject": "Physics",
        "summary_en": "Gravity is the invisible force that pulls everything towards the center of the Earth. Friction is the force that resists motion when two surfaces rub together.",
        "summary_sw": "Mvuto wa ardhi (Grabiti) ni nguvu isiyoonekana inayovuta vitu vyote kuelekea chini ardhini. Msuguano ni nguvu inayozuia vitu kuteleza kwa urahisi.",
        "analogy_sw": "Embe likiiva linaanguka chini ardhini kwa sababu ya grabiti. Unapofunga breki ya baiskeli kwenye barabara ya vumbi, msuguano ndio unaosimamishe baiskeli!",
        "analogy_en": "When a mango ripens, it falls down to the ground because of gravity. When you hit the bicycle brakes on a dirt road, friction stops your wheels!",
        "key_terms": [
            {"en": "Gravity", "sw": "Nguvu ya Mvuto wa Ardhi (Grabiti)"},
            {"en": "Friction", "sw": "Nguvu ya Msuguano"},
            {"en": "Mass", "sw": "Uzito/Masi ya kitu"},
            {"en": "Acceleration", "sw": "Mchapuko (Kuongezeka kwa kasi)"}
        ],
        "experiment": {
            "title_sw": "Jaribio: Kuona Msuguano na Kuteleza",
            "title_en": "Experiment: Testing Friction on Different Surfaces",
            "materials_sw": "Kifuniko cha chupa au sarafu, kitabu chenye jalada laini, kitambaa kigumu cha jiko.",
            "materials_en": "A bottle cap or coin, a smooth book cover, a rough kitchen towel.",
            "steps_sw": "1. Inamisha kitabu laini na uachie sarafu iteleze chini.\n2. Weka kitambaa juu ya kitabu kisha telezesha sarafu tena.\n3. Je, ni wapi inateleza haraka zaidi? Sehemu laini ina msuguano mdogo!",
            "steps_en": "1. Tilt the smooth book and let the coin slide down.\n2. Cover the book with the rough towel and slide the coin again.\n3. Notice where it slides faster. Smooth surfaces have much less friction!"
        },
        "quiz": {
            "question_sw": "Kwa nini embe likidondoka kutoka mtini huanguka chini badala ya kupaa angani?",
            "question_en": "Why does a mango falling from a tree fall to the ground instead of floating into the sky?",
            "options_sw": ["A) Kwa sababu ya nguvu ya mvuto wa ardhi (Grabiti)", "B) Kwa sababu ya upepo mkali", "C) Kwa sababu ya mwanga wa jua", "D) Kwa sababu jani limekauka"],
            "options_en": ["A) Because of Earth's gravitational pull", "B) Because of strong wind", "C) Because of sunlight", "D) Because the leaf is dry"],
            "correct_index": 0,
            "explanation_sw": "Safi sana! Grabiti inavuta vitu vyote vyenye uzito kuelekea katikati ya dunia.",
            "explanation_en": "Spot on! Gravity pulls all objects with mass down toward the center of the Earth."
        }
    },
    {
        "id": "fractions_math",
        "title_en": "Fractions: Dividing the Chapati",
        "title_sw": "Sehemu za Nambari (Fractions): Kugawa Chapati",
        "subject": "Mathematics",
        "summary_en": "A fraction represents a part of a whole. The top number (numerator) tells how many slices you have, and the bottom number (denominator) tells the total equal slices.",
        "summary_sw": "Sehemu (Fraction) inaonyesha kipande cha kitu kizima. Nambari ya juu (numerator) inaonyesha vipande ulivyonavyo, na ya chini (denominator) jumla ya vipande vyote vilivyogawanywa sawasawa.",
        "analogy_sw": "Ukikata chapati moja katika vipande vinne (4) vilivyo sawa, halafu ukamgawia mdogo wako kipande kimoja (1), amepata robo (1/4) ya chapati nzima!",
        "analogy_en": "If you slice one chapati into 4 equal pieces and give your sibling 1 piece, they have received one quarter (1/4) of the whole chapati!",
        "key_terms": [
            {"en": "Numerator", "sw": "Kiasi cha juu (Idadi ya vipande ulivyonavyo)"},
            {"en": "Denominator", "sw": "Kiasi cha chini (Jumla ya vipande vyote)"},
            {"en": "Half (1/2)", "sw": "Nusu"},
            {"en": "Quarter (1/4)", "sw": "Robo"}
        ],
        "experiment": {
            "title_sw": "Mchezo wa Karatasi: Kugawa Nusu na Robo",
            "title_en": "Paper Folding: Discovering Halves and Quarters",
            "materials_sw": "Karatasi moja ya daftari.",
            "materials_en": "One sheet of exercise notebook paper.",
            "steps_sw": "1. Kunja karatasi katikati mara moja = umepata nusu mbili (1/2 na 1/2).\n2. Kunja tena katikati = umepata robo nne (1/4, 1/4, 1/4, 1/4).\n3. 2/4 ni sawa kabisa na 1/2!",
            "steps_en": "1. Fold the paper in half once = you have two halves (1/2 and 1/2).\n2. Fold in half again = you have four quarters (1/4 each).\n3. Notice that 2/4 is exactly the same size as 1/2!"
        },
        "quiz": {
            "question_sw": "Ikiwa una machungwa 6 na ukala 3 kati yake, umekula sehemu gani ya machungwa yote?",
            "question_en": "If you have 6 oranges and you eat 3 of them, what fraction of the oranges did you eat?",
            "options_sw": ["A) 1/2 (Nusu)", "B) 1/4 (Robo)", "C) 1/6 (Moja ya sita)", "D) 3/4 (Robo tatu)"],
            "options_en": ["A) 1/2 (Half)", "B) 1/4 (Quarter)", "C) 1/6 (One-sixth)", "D) 3/4 (Three-quarters)"],
            "correct_index": 0,
            "explanation_sw": "Hodari sana! 3 kati ya 6 inajirudia kuwa 3/6, ambayo ikirahisishwa ni nusu (1/2).",
            "explanation_en": "Brilliant! 3 out of 6 is 3/6, which simplifies down to exactly 1/2."
        }
    }
]


def get_offline_starter_pack() -> List[Dict[str, Any]]:
    """Returns pre-packaged offline STEM modules for zero-connection caching."""
    return OFFLINE_STEM_VAULT


def find_offline_topic(query: str) -> Dict[str, Any]:
    """Finds matching offline module by topic keyword."""
    query_lower = query.lower()
    for item in OFFLINE_STEM_VAULT:
        if (item["id"] in query_lower or 
            item["title_en"].lower() in query_lower or 
            item["title_sw"].lower() in query_lower or
            item["subject"].lower() in query_lower or
            any(k["en"].lower() in query_lower or k["sw"].lower() in query_lower for k in item["key_terms"])):
            return item
    return OFFLINE_STEM_VAULT[0]
