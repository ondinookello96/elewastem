"""
ElewaSTEM Specialized Agent Tools with Deep Hyper-Local African Ecosystems, Stakeholder Resources, and Universal Accessibility
Includes Screen Reader & Audio Description Mode for visually impaired learners, visual concept & flowchart cues for deaf learners, and dyslexia adaptations.
"""

from typing import Dict, List, Any
try:
    from .curriculum import ALL_CURRICULUM_TOPICS, CURRICULUM_BY_ID, CURRICULUM_BY_SUBJECT
except ImportError:
    from curriculum import ALL_CURRICULUM_TOPICS, CURRICULUM_BY_ID, CURRICULUM_BY_SUBJECT

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

# The comprehensive 52-topic STEM offline vault aggregated from modular curriculum
OFFLINE_STEM_VAULT: List[Dict[str, Any]] = ALL_CURRICULUM_TOPICS


def get_available_regions() -> Dict[str, Any]:
    return REGIONS


RELATED_TOPIC_GRAPH: Dict[str, List[Dict[str, Any]]] = {
    # Biology Topics
    "photosynthesis": [
        {"id": "plant_pollination", "title_sw": "Uchavushaji & Uzazi wa Mimea", "title_en": "Pollination & Plant Reproduction", "prompt": "Eleza jinsi uchavushaji na maua yanavyotengeneza mbegu", "icon": "🌸"},
        {"id": "plant_transpiration_transport", "title_sw": "Usafirishaji wa Maji Kwenye Mimea (Xylem & Phloem)", "title_en": "Plant Transpiration & Transport", "prompt": "Eleza jinsi mimea inavyonyonya maji kwa xylem", "icon": "🌱"}
    ],
    "human_digestive_system": [
        {"id": "circulatory_heart", "title_sw": "Moyo & Mzunguko wa Damu", "title_en": "Heart & Blood Circulation", "prompt": "Eleza jinsi damu inavyosambaza virutubisho vya chakula mwilini", "icon": "❤️"},
        {"id": "chemistry_reactions", "title_sw": "Asidi ya Tumbo & Kemia", "title_en": "Stomach Acid Chemistry", "prompt": "Eleza jinsi asidi ya tumbo inavyovunja chakula", "icon": "⚗️"}
    ],
    "circulatory_heart": [
        {"id": "human_respiration", "title_sw": "Upumuaji wa Mapafu & Oksijeni", "title_en": "Lungs & Oxygen Respiration", "prompt": "Eleza jinsi mapafu yanavyoingiza oksijeni kwenye damu", "icon": "🫁"},
        {"id": "human_excretion_kidney", "title_sw": "Figo & Usafishaji wa Damu", "title_en": "Kidneys & Blood Filtration", "prompt": "Eleza jinsi figo zinavyochuja uchafu kwenye damu", "icon": "🩺"}
    ],
    "human_respiration": [
        {"id": "circulatory_heart", "title_sw": "Moyo & Mzunguko wa Damu", "title_en": "Heart & Blood Circulation", "prompt": "Eleza jinsi damu inavyosafirisha oksijeni", "icon": "❤️"},
        {"id": "air_gases_pollution", "title_sw": "Muundo wa Hewa & Oksijeni", "title_en": "Air Composition & Oxygen", "prompt": "Eleza muundo wa hewa ya anga", "icon": "💨"}
    ],
    "cell_biology": [
        {"id": "microorganisms_health", "title_sw": "Bakteria & Viumbe Wadogo", "title_en": "Microorganisms & Health", "prompt": "Eleza seli za bakteria na virusi", "icon": "🦠"},
        {"id": "photosynthesis", "title_sw": "Kloroplasti & Usanisinuru", "title_en": "Chloroplasts & Photosynthesis", "prompt": "Eleza kazi ya kloroplasti ndani ya seli ya mmea", "icon": "🌿"}
    ],
    "plant_pollination": [
        {"id": "photosynthesis", "title_sw": "Usanisinuru & Majani", "title_en": "Photosynthesis in Leaves", "prompt": "Eleza jinsi majani ya mmea yanavyotengeneza chakula", "icon": "🌿"},
        {"id": "ecology_food_chains", "title_sw": "Wadudu & Mnyororo wa Chakula", "title_en": "Pollinators & Food Webs", "prompt": "Eleza nafasi ya nyuki katika mazingira na kilimo", "icon": "🐝"}
    ],
    "living_things_classification": [
        {"id": "aquatic_biology_kisumu", "title_sw": "Samaki & Wenye Uti wa Mgongo", "title_en": "Fish & Vertebrates", "prompt": "Eleza sifa za samaki kama wanyama wenye uti wa mgongo", "icon": "🐟"},
        {"id": "ecology_food_chains", "title_sw": "Mnyororo wa Chakula wa Wanyama", "title_en": "Vertebrate Food Chains", "prompt": "Eleza mnyororo wa chakula wa wanyama wa mbugani", "icon": "🦁"}
    ],
    "ecology_food_chains": [
        {"id": "photosynthesis", "title_sw": "Mimea kama Watengenezaji Wakuu", "title_en": "Plants as Producers", "prompt": "Eleza jinsi mimea inavyoanzisha mnyororo wa chakula", "icon": "🌿"},
        {"id": "living_things_classification", "title_sw": "Uainishaji wa Wanyama Walaji", "title_en": "Herbivores & Carnivores", "prompt": "Eleza tofauti ya wanyama walaji majani na walaji nyama", "icon": "🐾"}
    ],
    "aquatic_biology_kisumu": [
        {"id": "human_respiration", "title_sw": "Upumuaji wa Binadamu vs Samaki", "title_en": "Human vs Fish Respiration", "prompt": "Eleza tofauti ya upumuaji wa mapafu na mashavu ya samaki", "icon": "🫁"},
        {"id": "density_floating_sinking", "title_sw": "Kuelea & Kuzama kwa Mashua Ziwani", "title_en": "Buoyancy & Boat Floating", "prompt": "Eleza kwanini meli za chuma zinaelea ziwani", "icon": "⚓"}
    ],
    "human_excretion_kidney": [
        {"id": "circulatory_heart", "title_sw": "Moyo & Mzunguko wa Damu", "title_en": "Circulation & Kidneys", "prompt": "Eleza jinsi damu inavyosafirishwa kwenda kwenye figo", "icon": "❤️"},
        {"id": "water_purification_hardness", "title_sw": "Maji Safi & Usafi wa Mwili", "title_en": "Water Purification & Health", "prompt": "Eleza umuhimu wa kunywa maji safi kwa figo", "icon": "💧"}
    ],
    "nervous_sense_organs": [
        {"id": "skeletal_muscular_system", "title_sw": "Mifupa & Misuli ya Mwili", "title_en": "Skeleton & Muscular Motion", "prompt": "Eleza jinsi ubongo unavyoamuru misuli kusonga", "icon": "🦴"},
        {"id": "computer_algorithms", "title_sw": "Mishipa ya Fahamu vs Mipango ya Kompyuta", "title_en": "Neural Networks & Algorithms", "prompt": "Eleza jinsi mifumo ya kompyuta inavyoiga mishipa ya fahamu", "icon": "💻"}
    ],
    "plant_transpiration_transport": [
        {"id": "photosynthesis", "title_sw": "Usanisinuru & Maji ya Mimea", "title_en": "Photosynthesis & Water Uptake", "prompt": "Eleza jinsi maji yanavyotumika kupika chakula cha mmea", "icon": "🌿"},
        {"id": "pressure_fluids_hydraulics", "title_sw": "Shinikizo la Kimiminika (Capillary Action)", "title_en": "Fluid Pressure & Capillary Rise", "prompt": "Eleza jinsi maji yanavyopanda juu kwenye mirija ya mti", "icon": "🚰"}
    ],
    "skeletal_muscular_system": [
        {"id": "simple_machines_levers", "title_sw": "Misuli kama Wenzo (Levers)", "title_en": "Biomechanics & Levers", "prompt": "Eleza jinsi mifupa ya mkono inavyofanya kazi kama wenzo", "icon": "⚙️"},
        {"id": "circulatory_heart", "title_sw": "Moyo & Mzunguko wa Damu", "title_en": "Heart & Muscles", "prompt": "Eleza jinsi misuli inavyopata oksijeni ya damu", "icon": "❤️"}
    ],
    "microorganisms_health": [
        {"id": "water_purification_hardness", "title_sw": "Kutibu Maji Kuua Bakteria", "title_en": "Water Treatment & Disinfection", "prompt": "Eleza jinsi klorini inavyoua bakteria kwenye maji", "icon": "💧"},
        {"id": "cell_biology", "title_sw": "Seli za Bakteria vs Seli za Mnyama", "title_en": "Bacterial vs Animal Cells", "prompt": "Eleza muundo wa seli ndogo za bakteria", "icon": "🔬"}
    ],

    # Physics Topics
    "electricity_circuits": [
        {"id": "logic_gates_circuits", "title_sw": "Milango ya Mantiki & Swichi za Kompyuta", "title_en": "Logic Gates & Switches", "prompt": "Eleza jinsi swichi za umeme zinavyounda milango ya AND/OR", "icon": "💻"},
        {"id": "magnetism_electromagnets", "title_sw": "Sumaku-Umeme & Jenereta", "title_en": "Electromagnetism & Motors", "prompt": "Eleza jinsi mkondo wa umeme unavyotengeneza sumaku", "icon": "🧲"}
    ],
    "gravity_forces": [
        {"id": "work_energy_power", "title_sw": "Kazi, Nishati na Nguvu", "title_en": "Work, Energy & Power", "prompt": "Eleza jinsi grabiti inavyotengeneza Nishati ya Uwezo (Potential Energy)", "icon": "⚡"},
        {"id": "simple_machines_levers", "title_sw": "Mashine Rahisi & Mizigo", "title_en": "Simple Machines & Load Forces", "prompt": "Eleza jinsi wenzo unavyosaidia kuinua mizigo mizito", "icon": "🚜"}
    ],
    "light_reflection_refraction": [
        {"id": "sound_waves_hearing", "title_sw": "Mawimbi ya Sauti vs Mwanga", "title_en": "Sound Waves vs Light Waves", "prompt": "Eleza tofauti ya kasi ya mwanga na sauti", "icon": "🔊"},
        {"id": "geometry_shapes_angles", "title_sw": "Jiometria ya Pembe za Miale ya Mwanga", "title_en": "Geometric Angles of Reflection", "prompt": "Eleza pembe ya mguso na pembe ya muakisi wa mwanga", "icon": "📐"}
    ],
    "sound_waves_hearing": [
        {"id": "light_reflection_refraction", "title_sw": "Mwangaza & Muakisi", "title_en": "Light & Reflection", "prompt": "Eleza jinsi mwanga unavyotembea kwa miale", "icon": "🔦"},
        {"id": "nervous_sense_organs", "title_sw": "Muundo wa Sikio & Usikivu", "title_en": "Ear Anatomy & Hearing", "prompt": "Eleza jinsi ngoma ya sikio inavyopokea mitetemo ya sauti", "icon": "👂"}
    ],
    "simple_machines_levers": [
        {"id": "work_energy_power", "title_sw": "Kazi, Nishati & Nguvu", "title_en": "Work & Mechanical Advantage", "prompt": "Eleza faida ya kimitambo ya kutumia mashine rahisi", "icon": "⚡"},
        {"id": "pythagoras_trigonometry", "title_sw": "Mteremko Bapa (Inclined Plane Geometry)", "title_en": "Inclined Plane Right Triangle", "prompt": "Eleza jiometria ya mteremko bapa", "icon": "📐"}
    ],
    "heat_transfer_methods": [
        {"id": "states_of_matter", "title_sw": "Hali za Maada & Joto", "title_en": "States of Matter & Thermal Phase", "prompt": "Eleza jinsi joto linavyoyeyusha barafu kuwa maji", "icon": "🧊"},
        {"id": "carbon_fuels_combustion", "title_sw": "Kuungua kwa Kuni & Joto", "title_en": "Combustion & Thermal Energy", "prompt": "Eleza jinsi kuni zinavyotoa joto la kupika", "icon": "🔥"}
    ],
    "magnetism_electromagnets": [
        {"id": "electricity_circuits", "title_sw": "Saketi za Umeme & Waya", "title_en": "Electric Circuits & Current", "prompt": "Eleza jinsi mkondo wa umeme unavyotiririka kwenye nyaya", "icon": "⚡"},
        {"id": "computer_hardware_components", "title_sw": "Hifadhi ya Hard Disk ya Sumaku", "title_en": "Magnetic Hard Disk Drives", "prompt": "Eleza jinsi data inavyohifadhiwa kwa sumaku", "icon": "💾"}
    ],
    "pressure_fluids_hydraulics": [
        {"id": "density_floating_sinking", "title_sw": "Uzito wa Kiasi & Kuelea Ziwani", "title_en": "Density & Archimedes Buoyancy", "prompt": "Eleza Kanuni ya Archimedes ya msukumo wa maji", "icon": "🚢"},
        {"id": "water_purification_hardness", "title_sw": "Maji & Shinikizo la Mabomba", "title_en": "Water Flow & Pipe Pressure", "prompt": "Eleza jinsi mabomba ya maji yanavyosambaza maji", "icon": "💧"}
    ],
    "work_energy_power": [
        {"id": "electricity_circuits", "title_sw": "Nishati ya Umeme & Nguvu (Watts)", "title_en": "Electrical Energy & Power", "prompt": "Eleza jinsi ya kukokotoa nguvu ya umeme kwa Wati", "icon": "💡"},
        {"id": "gravity_forces", "title_sw": "Grabiti & Nishati ya Uwezo", "title_en": "Gravity & Potential Energy", "prompt": "Eleza kwanini vitu vilivyo juu vina nishati ya uwezo", "icon": "🌍"}
    ],
    "density_floating_sinking": [
        {"id": "separation_techniques", "title_sw": "Kutenganisha Michanganyiko kwa Uzito", "title_en": "Density Separation & Flotation", "prompt": "Eleza jinsi mafuta yanavyoelea juu ya maji", "icon": "🧪"},
        {"id": "perimeter_area_volume", "title_sw": "Ujazo & Vipimo vya Masi", "title_en": "Volume & Mass Measurements", "prompt": "Eleza jinsi ya kupima ujazo wa chombo", "icon": "📐"}
    ],

    # Chemistry Topics
    "chemistry_reactions": [
        {"id": "chemical_bonding_compounds", "title_sw": "Muungano wa Ioni wa Chumvi", "title_en": "Ionic Bonding of Salts", "prompt": "Eleza jinsi asidi na besi zinavyoungana kuunda chumvi", "icon": "⚛️"},
        {"id": "human_digestive_system", "title_sw": "Asidi ya Tumbo & Mmeng'enyo", "title_en": "Stomach HCl & Digestion", "prompt": "Eleza jinsi asidi ya hydrochloric inavyovunja chakula", "icon": "🍎"}
    ],
    "states_of_matter": [
        {"id": "heat_transfer_methods", "title_sw": "Uhamishaji wa Joto & Kuyeyuka", "title_en": "Heat Transfer & Phase Change", "prompt": "Eleza mabadiliko ya maada kutokana na joto", "icon": "🔥"},
        {"id": "separation_techniques", "title_sw": "Kuvukiza & Kunereka (Distillation)", "title_en": "Evaporation & Distillation", "prompt": "Eleza jinsi mvuke unavyopozwa kuwa maji safi", "icon": "💧"}
    ],
    "separation_techniques": [
        {"id": "water_purification_hardness", "title_sw": "Kuchuja & Kutibu Maji ya Mto", "title_en": "Water Filtration & Treatment", "prompt": "Eleza jinsi mitambo ya maji inavyochuja mchanga na tope", "icon": "🚰"},
        {"id": "chemical_solutions_solubility", "title_sw": "Myeyusho & Kiwango cha Kuyeyuka", "title_en": "Solutions & Solubility Limits", "prompt": "Eleza jinsi chumvi inavyoyeyuka majini", "icon": "🧂"}
    ],
    "periodic_table_atoms": [
        {"id": "chemical_bonding_compounds", "title_sw": "Muungano wa Elektroni za Atomu", "title_en": "Valence Electrons & Bonding", "prompt": "Eleza jinsi elektroni za nje zinavyoshiriki muungano", "icon": "⚛️"},
        {"id": "metals_reactivity_series", "title_sw": "Metali & Mfuatano wa Mmenyuko", "title_en": "Metals Reactivity Series", "prompt": "Eleza kwanini Potasiamu na Sodiamu zina mmenyuko mkali", "icon": "⚡"}
    ],
    "water_purification_hardness": [
        {"id": "microorganisms_health", "title_sw": "Vijidudu vya Magonjwa ya Maji", "title_en": "Waterborne Pathogens & Bacteria", "prompt": "Eleza jinsi ya kujikinga na kipindupindu na typhoid", "icon": "🦠"},
        {"id": "separation_techniques", "title_sw": "Kuchuja & Kunereka kwa Maji", "title_en": "Filtration & Distillation", "prompt": "Eleza jinsi ya kutenganisha mchanga na maji", "icon": "🧪"}
    ],
    "air_gases_pollution": [
        {"id": "human_respiration", "title_sw": "Oksijeni & Upumuaji wa Binadamu", "title_en": "Oxygen & Lung Respiration", "prompt": "Eleza jinsi mapafu yanavyofyonza oksijeni kutoka hewani", "icon": "🫁"},
        {"id": "carbon_fuels_combustion", "title_sw": "Mwako wa Mafuta & Moshi wa Carbon", "title_en": "Combustion & Carbon Emissions", "prompt": "Eleza jinsi moshi wa magari unavyoongeza kaboni hewani", "icon": "🏭"}
    ],
    "metals_reactivity_series": [
        {"id": "electricity_circuits", "title_sw": "Upitishaji wa Umeme kwenye Metali za Shaba", "title_en": "Copper Metallic Conductivity", "prompt": "Eleza kwanini waya za shaba hutumika kupitisha umeme", "icon": "⚡"},
        {"id": "periodic_table_atoms", "title_sw": "Atomu za Metali & Jedwali la Periodiki", "title_en": "Metallic Atoms & Periodic Table", "prompt": "Eleza nafasi ya metali kwenye jedwali la periodiki", "icon": "⚛️"}
    ],
    "chemical_bonding_compounds": [
        {"id": "periodic_table_atoms", "title_sw": "Atomu, Protoni & Elektroni", "title_en": "Atomic Structure & Electrons", "prompt": "Eleza muundo wa atomu na elektroni", "icon": "🔬"},
        {"id": "chemistry_reactions", "title_sw": "Mmenyuko wa Asidi na Besi", "title_en": "Acid-Base Neutralization", "prompt": "Eleza jinsi muungano wa ioni unavyounda chumvi", "icon": "🧪"}
    ],
    "carbon_fuels_combustion": [
        {"id": "air_gases_pollution", "title_sw": "Moshi wa Carbon & Mabadiliko ya Tabianchi", "title_en": "Carbon Dioxide & Climate Change", "prompt": "Eleza athari za gesi ya greenhouse", "icon": "🌍"},
        {"id": "heat_transfer_methods", "title_sw": "Joto la Moto & Uhamishaji", "title_en": "Thermal Heat Transfer", "prompt": "Eleza jinsi moto unavyotoa mionzi ya joto", "icon": "🔥"}
    ],
    "chemical_solutions_solubility": [
        {"id": "separation_techniques", "title_sw": "Kuvukiza Kupata Fuwele za Chumvi", "title_en": "Evaporation & Crystallization", "prompt": "Eleza jinsi ya kupata fuwele safi za chumvi kutoka majini", "icon": "🧂"},
        {"id": "fractions_math", "title_sw": "Uwiano wa Viwango vya Mchanganyiko", "title_en": "Concentration Ratios & Fractions", "prompt": "Eleza uwiano wa kiasi cha sukari ndani ya maji", "icon": "📐"}
    ],

    # Mathematics Topics
    "fractions_math": [
        {"id": "ratios_proportions_rates", "title_sw": "Uwiano & Viwango Linganifu", "title_en": "Ratios & Proportions", "prompt": "Eleza jinsi sehemu zinavyohusiana na uwiano wa 1:2", "icon": "⚖️"},
        {"id": "commercial_arithmetic", "title_sw": "Hesabu za Asilimia ya Faida", "title_en": "Percentage Profit & Discount", "prompt": "Eleza jinsi ya kukokotoa punguzo la asilimia 10%", "icon": "💰"}
    ],
    "algebra_math": [
        {"id": "programming_python_scratch", "title_sw": "Vigeuzi vya Kompyuta (Variables)", "title_en": "Variables in Code & Algebra", "prompt": "Eleza jinsi vigeuzi vya x na y vinavyotumika kwenye kompyuta", "icon": "💻"},
        {"id": "pythagoras_trigonometry", "title_sw": "Milinganyo ya Pythagoras (a² + b² = c²)", "title_en": "Pythagorean Equation Solving", "prompt": "Eleza jinsi ya kutatua mlinganyo wa Pythagoras", "icon": "📐"}
    ],
    "geometry_shapes_angles": [
        {"id": "pythagoras_trigonometry", "title_sw": "Pembetatu Mraba & Pythagoras", "title_en": "Right Triangles & Pythagoras", "prompt": "Eleza upande wa hypotenuse wa pembetatu mraba", "icon": "📐"},
        {"id": "perimeter_area_volume", "title_sw": "Mzingo & Eneo la Maumbo", "title_en": "Perimeter & Area Formulas", "prompt": "Eleza jinsi ya kupima eneo la mstatili na mraba", "icon": "📏"}
    ],
    "ratios_proportions_rates": [
        {"id": "fractions_math", "title_sw": "Sehemu & Desimali", "title_en": "Fractions & Decimals", "prompt": "Eleza kubadilisha uwiano kuwa sehemu", "icon": "🔢"},
        {"id": "gravity_forces", "title_sw": "Kasi ya Mwendo (Speed = Distance / Time)", "title_en": "Speed Rates & Motion", "prompt": "Eleza jinsi ya kupima kasi ya gari kwa km/h", "icon": "🚗"}
    ],
    "statistics_data_charts": [
        {"id": "probability_chance", "title_sw": "Uwezekano & Nafasi za Matukio", "title_en": "Probability & Data Sets", "prompt": "Eleza uhusiano wa takwimu na uwezekano wa matukio", "icon": "🎲"},
        {"id": "databases_information_systems", "title_sw": "Hifadhidata & Majedwali ya Takwimu", "title_en": "Databases & Data Analytics", "prompt": "Eleza jinsi kompyuta inavyochanganua data za takwimu", "icon": "📊"}
    ],
    "integers_number_line": [
        {"id": "algebra_math", "title_sw": "Aljebra & Nambari Hasi", "title_en": "Algebra with Negative Numbers", "prompt": "Eleza jinsi ya kutatua milinganyo yenye nambari hasi", "icon": "📐"},
        {"id": "commercial_arithmetic", "title_sw": "Deni & Hasara katika Fedha", "title_en": "Financial Loss & Debts", "prompt": "Eleza jinsi deni linavyowakilishwa na nambari hasi", "icon": "📉"}
    ],
    "perimeter_area_volume": [
        {"id": "geometry_shapes_angles", "title_sw": "Maumbo ya 2D na 3D", "title_en": "2D and 3D Solid Geometry", "prompt": "Eleza tofauti ya maumbo bapa na maumbo yenye ujazo", "icon": "📦"},
        {"id": "density_floating_sinking", "title_sw": "Ujazo & Uzito wa Kiasi (Density = Mass/Volume)", "title_en": "Volume & Density Calculations", "prompt": "Eleza jinsi ujazo unavyotumika kukokotoa uzito wa kiasi", "icon": "⚖️"}
    ],
    "commercial_arithmetic": [
        {"id": "fractions_math", "title_sw": "Asilimia & Sehemu za Fedha", "title_en": "Percentages & Fractions in Trade", "prompt": "Eleza jinsi ya kuhesabu asilimia ya faida", "icon": "💵"},
        {"id": "statistics_data_charts", "title_sw": "Grafu za Mauzo ya Biashara", "title_en": "Business Sales Bar Charts", "prompt": "Eleza jinsi ya kurekodi mapato kwenye grafu", "icon": "📈"}
    ],
    "pythagoras_trigonometry": [
        {"id": "geometry_shapes_angles", "title_sw": "Pembe Mraba za Nyuzi 90°", "title_en": "Right Angles & Triangles", "prompt": "Eleza sifa za pembe mraba ya nyuzi 90", "icon": "📐"},
        {"id": "algebra_math", "title_sw": "Milinganyo ya Miraba (Square Roots)", "title_en": "Quadratic Roots & Algebra", "prompt": "Eleza kipeuo cha pili (square root)", "icon": "🔢"}
    ],
    "probability_chance": [
        {"id": "statistics_data_charts", "title_sw": "Takwimu & Wastani wa Matukio", "title_en": "Statistics & Averages", "prompt": "Eleza jinsi takwimu zinavyotabiri matukio", "icon": "📊"},
        {"id": "ai_machine_learning_concepts", "title_sw": "Akili Unde & Uwezekano wa Data", "title_en": "AI Prediction Probabilities", "prompt": "Eleza jinsi Akili Unde inavyotumia uwezekano kufanya ubashiri", "icon": "🤖"}
    ],

    # Computer Science Topics
    "computer_algorithms": [
        {"id": "programming_python_scratch", "title_sw": "Kuandika Msimbo wa Python", "title_en": "Coding in Python & Scratch", "prompt": "Eleza jinsi ya kubadilisha algoriti kuwa msimbo wa Python", "icon": "🐍"},
        {"id": "logic_gates_circuits", "title_sw": "Milango ya Mantiki (AND, OR, NOT)", "title_en": "Logic Gates & Truth Tables", "prompt": "Eleza milango ya mantiki ya kielektroniki", "icon": "⚡"}
    ],
    "binary_data_representation": [
        {"id": "logic_gates_circuits", "title_sw": "Saketi za Swichi za 0 na 1", "title_en": "Logic Gate 0 and 1 Switches", "prompt": "Eleza jinsi biti 0 na 1 zinavyopita kwenye swichi", "icon": "💡"},
        {"id": "computer_hardware_components", "title_sw": "Kumbukumbu ya RAM & Baiti (Bytes)", "title_en": "RAM Memory & Bytes", "prompt": "Eleza jinsi kompyuta inavyohifadhi baiti kwenye RAM", "icon": "💾"}
    ],
    "logic_gates_circuits": [
        {"id": "computer_algorithms", "title_sw": "Masharti ya If-Else kwenye Programu", "title_en": "If-Else Conditional Logic", "prompt": "Eleza jinsi sharti la IF linavyotumia mantiki ya AND/OR", "icon": "💻"},
        {"id": "electricity_circuits", "title_sw": "Saketi za Umeme & Swichi", "title_en": "Electric Circuits & Series Switches", "prompt": "Eleza swichi za mfululizo na sambamba", "icon": "⚡"}
    ],
    "programming_python_scratch": [
        {"id": "computer_algorithms", "title_sw": "Michoro ya Mtiririko (Flowcharts)", "title_en": "Flowcharts & Algorithmic Steps", "prompt": "Eleza jinsi ya kuchora flowchart kabla ya kuandika msimbo", "icon": "📝"},
        {"id": "databases_information_systems", "title_sw": "Kuunganisha Programu na Hifadhidata", "title_en": "Connecting Code to Databases", "prompt": "Eleza jinsi programu inavyosoma taarifa kutoka kwenye database", "icon": "🗄️"}
    ],
    "computer_hardware_components": [
        {"id": "binary_data_representation", "title_sw": "Uhifadhi wa Data wa SSD & Bits", "title_en": "SSD Storage & Binary Data", "prompt": "Eleza jinsi picha zinavyohifadhiwa kama binary", "icon": "💾"},
        {"id": "networks_internet_security", "title_sw": "Vifaa vya Mtandao (Routers & Cables)", "title_en": "Network Hardware & Routers", "prompt": "Eleza jinsi router inavyosambaza intaneti", "icon": "🌐"}
    ],
    "networks_internet_security": [
        {"id": "computer_hardware_components", "title_sw": "Vifaa vya Mtandao wa Kompyuta", "title_en": "Network Interface Cards & Servers", "prompt": "Eleza kazi ya kadi ya mtandao ndani ya kompyuta", "icon": "🖥️"},
        {"id": "ai_machine_learning_concepts", "title_sw": "Usalama wa Mtandao kwa Kutumia AI", "title_en": "AI-Powered Cybersecurity", "prompt": "Eleza jinsi Akili Unde inavyozuia virusi na wadukuzi", "icon": "🛡️"}
    ],
    "ai_machine_learning_concepts": [
        {"id": "programming_python_scratch", "title_sw": "Programu za Kujifunza Mashine", "title_en": "Machine Learning Programming", "prompt": "Eleza jinsi ya kufundisha modeli ya AI kwa mifano ya picha", "icon": "🧠"},
        {"id": "statistics_data_charts", "title_sw": "Takwimu & Mifano ya Kujifunzia Data", "title_en": "Statistics for AI Models", "prompt": "Eleza umuhimu wa takwimu katika kufundisha AI", "icon": "📊"}
    ],
    "databases_information_systems": [
        {"id": "programming_python_scratch", "title_sw": "Kutafuta Taarifa kwa Programu", "title_en": "Querying Data via Code", "prompt": "Eleza jinsi ya kutumia SQL kutafuta rekodi za wanafunzi", "icon": "💻"},
        {"id": "statistics_data_charts", "title_sw": "Chati & Ripoti za Takwimu kutoka Hifadhidata", "title_en": "Database Reporting & Charts", "prompt": "Eleza jinsi ripoti za grafu zinavyotengenezwa kutoka hifadhidata", "icon": "📈"}
    ]
}


def get_related_topics_recommendations(topic_id_or_query: str) -> List[Dict[str, Any]]:
    """Returns structured next topic recommendations based on current learning."""
    topic = find_offline_topic(topic_id_or_query)
    tid = topic.get("id", "photosynthesis")
    return RELATED_TOPIC_GRAPH.get(tid, RELATED_TOPIC_GRAPH.get("photosynthesis", []))


def find_offline_topic(query: str, preferred_subject: str = "all") -> Dict[str, Any]:
    query_lower = query.lower().strip()
    
    # 0. Direct match against topic ID
    if query_lower in CURRICULUM_BY_ID:
        return CURRICULUM_BY_ID[query_lower]

    # 1. High-Precision Domain Keyword Detection across all 52 modules:
    
    # --- BIOLOGY ---
    if any(k in query_lower for k in ["digest", "mmeng'enyo", "stomach", "tumbo", "esophagus", "umio", "mouth", "kinywa", "saliva", "mate", "intestine", "utumbo", "enzyme", "virutubisho", "chakula mwilini"]):
        return CURRICULUM_BY_ID.get("human_digestive_system", OFFLINE_STEM_VAULT[0])
    
    if any(k in query_lower for k in ["heart", "moyo", "circulat", "mzunguko wa damu", "blood", "damu", "artery", "ateri", "vein", "vena", "pulse", "mapigo"]):
        return CURRICULUM_BY_ID.get("circulatory_heart", OFFLINE_STEM_VAULT[0])
    
    if any(k in query_lower for k in ["kidney", "figo", "excret", "mkojo", "nephron", "uchafu wa damu", "dialysis"]):
        return CURRICULUM_BY_ID.get("human_excretion_kidney", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["nervous system", "ubongo wa binadamu", "mfumo wa fahamu", "nerve cell", "mishipa ya fahamu", "sense organs", "milango ya hisia", "reflex arc"]):
        return CURRICULUM_BY_ID.get("nervous_sense_organs", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["vertebrate", "invertebrate", "uti wa mgongo", "classify", "uainishaji", "mammal", "mamalia", "reptile", "reptilia", "amphibian", "amfibea", "insect", "wadudu"]):
        return CURRICULUM_BY_ID.get("living_things_classification", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["bone", "mifupa", "skeleton", "muscl", "misuli", "joint", "kiungio", "tendon", "ligament", "fupa la mgongo", "fupa"]):
        return CURRICULUM_BY_ID.get("skeletal_muscular_system", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["bacteria", "bakteria", "virus", "virusi", "fungi", "ukungu", "microorganism", "vijidudu", "microbe", "pathogen", "hygiene", "cholera", "kipindupindu"]):
        return CURRICULUM_BY_ID.get("microorganisms_health", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["transpirat", "mvuke wa mmea", "xylem", "phloem", "transport in plant", "mizizi inanyonya maji", "usafirishaji wa maji"]):
        return CURRICULUM_BY_ID.get("plant_transpiration_transport", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["fish biology", "aquatic fish", "samaki", "gills ya samaki", "matamvua", "ngege", "mbuta", "upumuaji wa samaki"]):
        return CURRICULUM_BY_ID.get("aquatic_biology_kisumu", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["lung", "mapafu", "respirat", "upumuaji", "breathe", "pumua", "trachea", "koromeo", "inhale", "exhale", "diaphragm", "kiwambo"]):
        return CURRICULUM_BY_ID.get("human_respiration", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["cell", "seli", "nucleus", "kiini", "cytoplasm", "saikroplasimu", "membrane", "utando", "chloroplast", "kloroplasti"]):
        return CURRICULUM_BY_ID.get("cell_biology", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["food chain", "mnyororo wa chakula", "ecolog", "ikolojia", "ecosystem", "producer", "mtengenezaji", "consumer", "mlaji", "predator", "mwindaji", "herbivore", "carnivore", "decomposer"]):
        return CURRICULUM_BY_ID.get("ecology_food_chains", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["pollinat", "uchavushaji", "flower", "maua", "petali", "petal", "stamen", "chavulio", "pistil", "kambamaua", "poleni", "chavua", "nectar"]):
        return CURRICULUM_BY_ID.get("plant_pollination", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["photo", "usanisinuru", "klorofili", "chlorophyll", "plant food", "chakula cha mmea", "stomata"]):
        return CURRICULUM_BY_ID.get("photosynthesis", OFFLINE_STEM_VAULT[0])

    # --- PHYSICS ---
    # --- COMPUTER SCIENCE & EMERGING TECH (Checked first to prevent common word collisions) ---
    if any(k in query_lower for k in ["artificial intelligence", "akili unde", "machine learning", "mafunzo ya mashine", "deep learning", "neural network", "chatgpt", "gemini", "robotics"]):
        return CURRICULUM_BY_ID.get("ai_machine_learning_concepts", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["database", "hifadhidata", "sql", "relational table", "jedwali la data", "primary key", "database query"]):
        return CURRICULUM_BY_ID.get("databases_information_systems", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["algorithm", "algoriti", "flowchart", "mchoro wa mtiririko", "computational logic", "hatua za kompyuta"]):
        return CURRICULUM_BY_ID.get("computer_algorithms", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["binary", "nambari mbili za kompyuta", "biti 8", "bits za kompyuta", "byte ya kompyuta", "baiti ya kompyuta", "kilobyte", "megabyte", "gigabyte", "0 na 1", "0 and 1", "ascii"]):
        return CURRICULUM_BY_ID.get("binary_data_representation", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["logic gate", "mlango wa mantiki", "and gate", "or gate", "not gate", "truth table", "jedwali la ukweli"]):
        return CURRICULUM_BY_ID.get("logic_gates_circuits", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["python", "scratch", "programming", "coding", "code snippet", "for loop", "while loop", "mzunguko wa loop", "if-else statement"]):
        return CURRICULUM_BY_ID.get("programming_python_scratch", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["cpu", "kichakataji", "ram memory", "ssd storage", "computer hardware", "vifaa vya kompyuta", "hard disk", "motherboard"]):
        return CURRICULUM_BY_ID.get("computer_hardware_components", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["network", "mtandao wa kompyuta", "internet", "intaneti", "mtandao wa lan", "mtandao wa wan", "local area network", "cybersecurity", "usalama wa mtandao", "strong password", "nenosiri", "phishing"]):
        return CURRICULUM_BY_ID.get("networks_internet_security", OFFLINE_STEM_VAULT[0])

    # --- PHYSICS ---
    if any(k in query_lower for k in ["sound", "sauti", "echo", "mwangwi", "frequency", "hertz", "pitch", "vibration", "mtetemo"]):
        return CURRICULUM_BY_ID.get("sound_waves_hearing", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["light", "mwanga", "mwangaza", "reflect", "muakisi", "refract", "kioo", "mirror", "lens", "lenzi", "shadow", "kivuli"]):
        return CURRICULUM_BY_ID.get("light_reflection_refraction", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["lever", "wenzo", "pulley", "kapi", "wheel and axle", "inclined plane", "mteremko", "simple machine", "mashine rahisi", "fulcrum", "egemeo"]):
        return CURRICULUM_BY_ID.get("simple_machines_levers", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["conduction", "convection", "radiation", "heat transfer", "uhamishaji wa joto", "thermal energy", "insulator", "kipitishio cha joto"]):
        return CURRICULUM_BY_ID.get("heat_transfer_methods", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["magnet", "sumaku", "electromagnet", "magnetic field", "uga wa sumaku"]):
        return CURRICULUM_BY_ID.get("magnetism_electromagnets", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["pressure", "shinikizo", "pascal", "hydraulic", "haidroliki", "barometer", "fluid pressure"]):
        return CURRICULUM_BY_ID.get("pressure_fluids_hydraulics", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["work done", "kazi ya kifizikia", "energy", "joule", "watt", "kinetic energy", "potential energy", "power in physics"]):
        return CURRICULUM_BY_ID.get("work_energy_power", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["density", "uzito wa kiasi", "buoyancy", "archimedes", "msukumo wa maji", "float or sink", "kuelea na kuzama"]):
        return CURRICULUM_BY_ID.get("density_floating_sinking", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["gravity", "grabiti", "gravitational force", "nguvu ya mvuto", "friction", "msuguano", "breki", "baiskeli", "newton"]):
        return CURRICULUM_BY_ID.get("gravity_forces", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["electr", "circuit", "umeme", "saketi", "wire", "waya", "battery", "betri", "voltage", "current", "switch"]):
        return CURRICULUM_BY_ID.get("electricity_circuits", OFFLINE_STEM_VAULT[0])

    # --- CHEMISTRY ---
    if any(k in query_lower for k in ["solid, liquid", "states of matter", "mango, kimiminika", "gesi", "melting point", "freezing point", "evaporat", "vukiza", "condens", "particle theory"]):
        return CURRICULUM_BY_ID.get("states_of_matter", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["filtrat", "chuja", "distill", "nereka", "fractional distillation", "separat", "tenganisha mchanganyiko", "chujio"]):
        return CURRICULUM_BY_ID.get("separation_techniques", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["atom", "atomu", "proton", "protoni", "neutron", "nutroni", "electron", "elektroni", "periodic table", "jedwali la periodiki", "chemical element"]):
        return CURRICULUM_BY_ID.get("periodic_table_atoms", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["hard water", "maji magumu", "soft water", "maji laini", "waterguard", "chlorinat", "water purif", "takaso wa maji", "limescale", "scum"]):
        return CURRICULUM_BY_ID.get("water_purification_hardness", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["air composition", "nitrogen gas", "nitrojeni", "oxygen gas", "oksijeni", "argon", "air pollution", "uchafuzi wa hewa", "greenhouse gas"]):
        return CURRICULUM_BY_ID.get("air_gases_pollution", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["metal", "metali", "non-metal", "reactivity series", "mfuatano wa mmenyuko", "rust", "kutu", "galvaniz", "corrosion", "alloy", "aloi"]):
        return CURRICULUM_BY_ID.get("metals_reactivity_series", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["ionic", "ioni", "covalent", "kovalent", "chemical bonding", "muungano wa kikemia", "octet rule"]):
        return CURRICULUM_BY_ID.get("chemical_bonding_compounds", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["combustion", "kuungua kwa mafuta", "mkaa", "charcoal", "biogas", "methane", "hydrocarbon", "complete combustion"]):
        return CURRICULUM_BY_ID.get("carbon_fuels_combustion", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["solute", "kiyeyushwa", "solvent", "kiyeyushaji", "chemical solution", "myeyusho", "saturated solution", "solubility"]):
        return CURRICULUM_BY_ID.get("chemical_solutions_solubility", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["acid", "asidi", "base", "besi", "neutraliz", "ph scale", "litmus", "chumvi na maji", "alkali"]):
        return CURRICULUM_BY_ID.get("chemistry_reactions", OFFLINE_STEM_VAULT[0])

    # --- MATHEMATICS ---
    if any(k in query_lower for k in ["fraction", "sehemu ya nambari", "decimal", "desimali", "percentage", "asilimia", "theluthi", "robo", "nusu"]):
        return CURRICULUM_BY_ID.get("fractions_math", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["algebra", "aljebra", "linear equation", "mlinganyo", "variable", "kigeuzi", "solve for x", "x +", "2x"]):
        return CURRICULUM_BY_ID.get("algebra_math", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["pythagoras", "pitagorasi", "hypotenuse", "a2 + b2", "right-angled triangle", "pembetatu mraba", "trigonometr", "sin cos tan"]):
        return CURRICULUM_BY_ID.get("pythagoras_trigonometry", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["perimeter", "mzingo", "area of", "eneo la", "volume of", "ujazo wa", "m2", "m3", "circumference"]):
        return CURRICULUM_BY_ID.get("perimeter_area_volume", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["profit", "faida", "loss in trade", "hasara", "simple interest", "riba", "discount", "punguzo", "buying price", "selling price"]):
        return CURRICULUM_BY_ID.get("commercial_arithmetic", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["angle", "pembe", "triangle", "pembetatu", "polygon", "poligoni", "acute", "obtuse", "right angle"]):
        return CURRICULUM_BY_ID.get("geometry_shapes_angles", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["ratio", "uwiano", "proportion", "uwiano linganifu", "rate of speed", "kiwango cha kasi", "map scale"]):
        return CURRICULUM_BY_ID.get("ratios_proportions_rates", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["mean", "wastani", "median", "mode", "nambari ya kati", "statistics", "takwimu", "bar graph", "pie chart"]):
        return CURRICULUM_BY_ID.get("statistics_data_charts", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["integer", "nambari nzima", "negative number", "nambari hasi", "number line", "mstari wa nambari", "-1", "-2", "-5"]):
        return CURRICULUM_BY_ID.get("integers_number_line", OFFLINE_STEM_VAULT[0])

    if any(k in query_lower for k in ["probabilit", "uwezekano", "chance of", "nafasi ya kutokea", "rolling a dice", "kete", "coin toss", "kurusha sarafu"]):
        return CURRICULUM_BY_ID.get("probability_chance", OFFLINE_STEM_VAULT[0])

    # 2. Match by preferred subject if selected
    if preferred_subject and preferred_subject.lower() != "all":
        subj_map = {
            "biology": "Biology",
            "physics": "Physics",
            "chemistry": "Chemistry",
            "mathematics": "Mathematics",
            "math": "Mathematics",
            "computer_science": "Computer Science",
            "cs": "Computer Science"
        }
        target_subj = subj_map.get(preferred_subject.lower())
        if target_subj and target_subj in CURRICULUM_BY_SUBJECT:
            return CURRICULUM_BY_SUBJECT[target_subj][0]

    # 3. Fallback search across title / key terms
    for item in OFFLINE_STEM_VAULT:
        if (item["id"] in query_lower or 
            item["title_en"].lower() in query_lower or 
            item["title_sw"].lower() in query_lower or
            any(k["en"].lower() in query_lower or k["sw"].lower() in query_lower for k in item.get("key_terms", []))):
            return item

    return OFFLINE_STEM_VAULT[0]


def get_offline_starter_pack() -> List[Dict[str, Any]]:
    """Returns all 52 curriculum modules for full offline PWA caching."""
    return ALL_CURRICULUM_TOPICS


def generate_teacher_lesson_plan(topic_id_or_query: str, region: str = "lake_basin") -> Dict[str, Any]:
    """Generates a structured CBC / National Curriculum lesson plan for teachers."""
    topic = find_offline_topic(topic_id_or_query)
    reg_meta = REGIONS.get(region, REGIONS["lake_basin"])
    regional_dict = topic.get("regional_analogies", {}).get(region, topic.get("regional_analogies", {}).get("lake_basin", {}))
    
    return {
        "topic_id": topic.get("id"),
        "title_en": topic.get("title_en"),
        "title_sw": topic.get("title_sw"),
        "subject": topic.get("subject"),
        "cbc_strand": topic.get("cbc_strand"),
        "eco_zone": reg_meta["name_sw"],
        "learning_objectives": [
            f"Kuelewa misingi ya {topic.get('title_sw', '')} kwa lugha asilia na Kiswahili.",
            f"Kutumia mifano halisi ya eneo la {reg_meta['locality_name']} badala ya kukariri nadharia tu.",
            f"Kufanya jaribio la vitendo lisilo na gharama nyumbani au darasani."
        ],
        "regional_teaching_analogy": regional_dict.get("analogy_sw", ""),
        "tactile_inclusion_guide": topic.get("tactile_audio_description_sw", ""),
        "sign_language_cues": topic.get("sign_language_visual_cues_sw", ""),
        "classroom_experiment": topic.get("experiment", {}),
        "formative_assessment_quiz": topic.get("quiz", {})
    }


def generate_parent_digest(student_id: str, region: str = "lake_basin", mastered_topics_count: int = 1) -> Dict[str, Any]:
    """Generates SMS digest and home challenge for parents without requiring internet/smartphones."""
    reg_meta = REGIONS.get(region, REGIONS["lake_basin"])
    return {
        "student_id": student_id,
        "region": region,
        "sms_digest_text": f"ElewaSTEM Ripoti ya Mzazi: Mwanafunzi amechunguza mada za STEM kwa mifano ya {reg_meta['name_sw']}. Jaribio la wiki hii: Chunguza sayansi ya jikoni na mtoto wako!",
        "pairing_code": f"ELEWA-{student_id[-4:] if len(student_id) >= 4 else '7921'}",
        "remote_magic_link": f"https://elewastem.org/parent?student={student_id}"
    }


def get_community_club_projects(region: str = "lake_basin") -> List[Dict[str, Any]]:
    """Returns local peer learning and STEM club science fair projects."""
    reg_meta = REGIONS.get(region, REGIONS["lake_basin"])
    return [
        {
            "id": "project_clean_water",
            "title": f"Mradi wa Kuchuja Maji Safi ({reg_meta['locality_name']})",
            "subject": "Chemistry & Hygiene",
            "description": "Kujenga chujio rahisi cha tabaka la mchanga, mawe madogo na makaa ya jikoni kusafisha maji machafu ya mto/ziwani.",
            "impact": "Kuzuia magonjwa ya tumbo na kuelewa mbinu za kutenganisha michanganyiko (Filtration)."
        },
        {
            "id": "project_solar_circuit",
            "title": f"Mradi wa Saketi ya Taa ya Solar ya Kusomea ({reg_meta['locality_name']})",
            "subject": "Physics & Engineering",
            "description": "Kuunganisha solar ndogo na betri ya simu ya zamani kuwasha balbu ya LED ya kusomea usiku bila umeme wa gridi.",
            "impact": "Kuelewa saketi za umeme na nishati endelevu ya jua."
        },
        {
            "id": "project_kitchen_ph",
            "title": f"Mradi wa Kupima pH ya Udongo wa Mashambani ({reg_meta['locality_name']})",
            "subject": "Chemistry & Agriculture",
            "description": "Kutumia maji ya majani ya chai au maua ya hibiscus kupima kama udongo wa shamba una asidi nyingi.",
            "impact": "Kusaidia wakulima wa kijiji kuboresha mavuno ya mahindi na mboga."
        }
    ]

