import sys
import io
import requests
import json

# Force UTF-8 stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_URL = 'http://localhost:8000'

def run_tests():
    print("============================================================")
    print(" ELEWASTEM 5-DISCIPLINE STEM CURRICULUM VERIFICATION SUITE")
    print("============================================================")

    # 1. Health & Meta
    r = requests.get(f'{BASE_URL}/api/health')
    assert r.status_code == 200, f"Health check failed: {r.status_code}"
    health = r.json()
    print(f"[PASSED] 1. Health Check: OK (v{health['version']})")
    print(f"   * Languages: {health['supported_african_languages_count']}")
    print(f"   * Privacy Jurisdictions: {health['data_protection_jurisdictions_count']}")
    print(f"   * Features: {', '.join(health['features'])}")

    # 2. African Languages Endpoint
    r = requests.get(f'{BASE_URL}/api/languages')
    assert r.status_code == 200
    langs = r.json()
    print(f"\n[PASSED] 2. Pan-African Languages: {len(langs)} languages verified")
    for l in langs[:4]:
        print(f"   * {l['flag']} {l['name']} ({l['tutor_title']} - '{l['motto']}')")

    # 3. Privacy Jurisdictions
    r = requests.get(f'{BASE_URL}/api/privacy/jurisdictions')
    assert r.status_code == 200
    jurs = r.json()
    print(f"\n[PASSED] 3. Pan-African DPA Legal Matrix: {len(jurs)} frameworks verified")
    for j in jurs[:4]:
        print(f"   * {j['flag']} {j['country']}: {j['law_name']} ({j['regulatory_body']})")

    # 4. Offline Starter Pack Verification (52 Topics across 5 disciplines)
    r = requests.get(f'{BASE_URL}/api/offline-pack')
    assert r.status_code == 200
    pack = r.json()
    print(f"\n[PASSED] 4. Full Offline Curriculum Vault: {pack['module_count']} modules loaded")
    assert pack['module_count'] >= 50, f"Expected at least 50 topics, found {pack['module_count']}"

    # 5. Teacher Lesson Plan Generator across 5 Disciplines
    teacher_topics = [
        ("photosynthesis", "Biology"),
        ("electricity_circuits", "Physics"),
        ("chemistry_reactions", "Chemistry"),
        ("algebra_math", "Mathematics"),
        ("ai_machine_learning_concepts", "Computer Science")
    ]
    print(f"\n[PASSED] 5. Multi-Discipline Teacher Lesson Plans:")
    for tid, subj in teacher_topics:
        r = requests.get(f'{BASE_URL}/api/teacher/lesson-plan?topic={tid}&region=lake_basin')
        assert r.status_code == 200
        plan = r.json()
        print(f"   * [{subj}] '{plan.get('title_sw')}' | Strand: {plan.get('cbc_strand')}")

    # 6. Multi-Discipline AI Chat & Local Grounding Verification (25 Key Benchmarks)
    stem_benchmarks = [
        # --- BIOLOGY ---
        ("Nieleze kuhusu mmeng'enyo wa chakula tumboni na utumbo mdogo", "human_digestive_system", "Biology: Digestion"),
        ("Moyo unafanya kazi gani kusukuma damu na ateri?", "circulatory_heart", "Biology: Heart"),
        ("Jinsi mapafu yanavyofanya kazi wakati wa kupumua hewa", "human_respiration", "Biology: Respiration"),
        ("Tofauti kati ya seli ya mmea na seli ya mnyama na kiini", "cell_biology", "Biology: Cell"),
        ("Uchavushaji wa maua na nyuki unavyotengeneza mbegu", "plant_pollination", "Biology: Pollination"),
        ("Wanyama wenye uti wa mgongo vertebrates na wasio nao invertebrates", "living_things_classification", "Biology: Taxonomy"),
        ("Mnyororo wa chakula jinsi nishati ya jua inavyosafiri kwa mimea na wanyama", "ecology_food_chains", "Biology: Food Chain"),
        ("Jinsi samaki Ngege anavyopumua kwa matamvua ziwani", "aquatic_biology_kisumu", "Biology: Fish Respiration"),
        ("Kazi ya figo na nephron katika kutoa taka na mkojo", "human_excretion_kidney", "Biology: Kidneys"),
        ("Mfumo wa fahamu, ubongo na milango ya hisia", "nervous_sense_organs", "Biology: Nervous"),
        ("I want to learn about Genetics, DNA and inherited traits from parents", "genetics_dna_heredity", "Biology: Genetics & DNA"),

        # --- PHYSICS ---
        ("Eleza saketi za umeme, waya na betri", "electricity_circuits", "Physics: Circuits"),
        ("Nguvu ya grabiti na msuguano wa breki za baiskeli", "gravity_forces", "Physics: Gravity"),
        ("Mwangaza unavyoakisiwa na vioo na lenzi", "light_reflection_refraction", "Physics: Light Optics"),
        ("Mawimbi ya sauti na mitetemo inavyosafiri sikioni", "sound_waves_hearing", "Physics: Sound Waves"),
        ("Mashine rahisi kama wenzo, kapi na mteremko bapa", "simple_machines_levers", "Physics: Levers"),

        # --- CHEMISTRY ---
        ("Kemia ya asidi na besi na mmenyuko wa neutralization", "chemistry_reactions", "Chemistry: Acids & Bases"),
        ("Hali tatu za maada: mango, kimiminika na gesi za mvuke", "states_of_matter", "Chemistry: States of Matter"),
        ("Mbinu za kutenganisha michanganyiko kwa kuchuja na kunereka", "separation_techniques", "Chemistry: Separation"),
        ("Muundo wa atomu, protoni, elektroni na jedwali la periodiki", "periodic_table_atoms", "Chemistry: Periodic Table"),
        ("Maji magumu na jinsi ya kusafisha na kutibu maji ya kunywa", "water_purification_hardness", "Chemistry: Water Treatment"),

        # --- MATHEMATICS ---
        ("Sehemu za nambari, desimali na asilimia", "fractions_math", "Math: Fractions"),
        ("Aljebra na kutatua mlinganyo wa 2x + 4 = 14", "algebra_math", "Math: Algebra"),
        ("Jiometria ya pembe za pembetatu na maumbo ya 2D na 3D", "geometry_shapes_angles", "Math: Geometry"),
        ("Nadharia ya Pythagoras a2 + b2 = c2 kwa pembetatu mraba", "pythagoras_trigonometry", "Math: Pythagoras"),
        ("Uwezekano na nafasi ya kupata namba kwenye kete au sarafu", "probability_chance", "Math: Probability"),

        # --- COMPUTER SCIENCE ---
        ("Algoriti za kompyuta na michoro ya mtiririko ya flowchart", "computer_algorithms", "CS: Algorithms"),
        ("Mfumo wa nambari mbili wa binary biti 0 na 1 na baiti", "binary_data_representation", "CS: Binary"),
        ("Milango ya mantiki ya AND gate, OR gate na NOT gate", "logic_gates_circuits", "CS: Logic Gates"),
        ("Utayarishaji wa programu kwa lugha ya Python na Scratch", "programming_python_scratch", "CS: Python Coding"),
        ("Akili Unde ya Artificial Intelligence na Machine Learning", "ai_machine_learning_concepts", "CS: AI & ML"),
        ("Mifumo ya hifadhidata ya relational database na jedwali la SQL", "databases_information_systems", "CS: Databases")
    ]

    print("\n[TEST] 6. Validating 31 Multi-Discipline STEM Topic Queries across 5 Subjects:")
    passed_count = 0
    for query, expected_id, label in stem_benchmarks:
        r = requests.post(f'{BASE_URL}/api/chat', json={
            'student_id': 'stem_tester',
            'message': query,
            'language': 'sw',
            'region': 'lake_basin'
        })
        assert r.status_code == 200, f"Chat query failed for: {query}"
        data = r.json()
        topic_name = data.get('topic')
        module_id = data.get('offline_module_id') or data.get('topic_id')
        subj = data.get('subject')
        diag = data.get('diagram')
        
        assert module_id == expected_id, f"Expected {expected_id} but got {module_id} for query: {query}"
        assert diag is not None, f"Expected vector diagram for topic {module_id}"
        print(f"   * [{label:26}] -> Topic: '{topic_name[:30]}' | Subj: {subj:16} | Module: '{module_id}' [OK]")
        passed_count += 1

    print("\n============================================================")
    print(f" 🎉 100% SUCCESS: ALL {passed_count}/{len(stem_benchmarks)} CROSS-DISCIPLINE STEM BENCHMARKS PASSED!")
    print("============================================================")

if __name__ == '__main__':
    run_tests()
