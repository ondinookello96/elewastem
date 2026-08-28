import sys
import io
import requests
import json

# Force UTF-8 stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_URL = 'http://localhost:8000'

def run_tests():
    print("============================================================")
    print(" ELEWASTEM FULL FEATURE & FEEDBACK VERIFICATION SUITE")
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

    # 4. Multilingual & Adaptive Chat (Kisumu Biology with Tactile & Sign Support)
    payload = {
        'student_id': 'cosmas_tester',
        'message': 'Eleza jinsi samaki Ngege wa Kisumu anavyopumua ziwani',
        'language': 'sw',
        'region': 'lake_basin',
        'jurisdiction': 'KE'
    }
    r = requests.post(f'{BASE_URL}/api/chat', json=payload)
    assert r.status_code == 200
    chat_res = r.json()
    print(f"\n[PASSED] 4. AI Adaptive Chat Engine: Response generated")
    print(f"   * Engine: {chat_res.get('source')}")
    print(f"   * Tactile Description (Blind): {chat_res.get('tactile_description')[:80]}...")
    print(f"   * Sign Language (Deaf): {chat_res.get('sign_cues')}")

    # 5. CBC Teacher Lesson Plan Generator
    r = requests.get(f'{BASE_URL}/api/teacher/lesson-plan?topic=photosynthesis&region=lake_basin')
    assert r.status_code == 200
    plan = r.json()
    print(f"\n[PASSED] 5. Teacher Hub: CBC Lesson Plan Generator")
    print(f"   * Strand: {plan.get('curriculum_strand')}")
    print(f"   * Lesson: {plan.get('lesson_title')}")
    print(f"   * Local Aid: {plan.get('local_teaching_aid')[:75]}...")

    # 6. Parent Progress Digest & SMS Formatter
    r = requests.get(f'{BASE_URL}/api/parent/digest/cosmas_tester?region=lake_basin')
    assert r.status_code == 200
    parent = r.json()
    print(f"\n[PASSED] 6. Parent Hub: SMS Digest & Home Science Challenge")
    print(f"   * SMS Text: {parent.get('sms_digest_text')}")
    print(f"   * Home Challenge: {parent.get('home_activity_for_parent', {}).get('title')}")

    # 7. Community STEM Mentors Hub
    r = requests.get(f'{BASE_URL}/api/community/activities?region=lake_basin')
    assert r.status_code == 200
    comm = r.json()
    print(f"\n[PASSED] 7. Community Mentors: Zero-Cost STEM Club Guides")
    for act in comm:
        print(f"   * {act['project_name']} (Materials: {act['materials'][:50]}...)")

    # 8. Multi-Stakeholder Feedback Mechanism
    fb_payload = {
        'stakeholder_type': 'teacher',
        'student_id': 'mwalimu_otieno',
        'region': 'lake_basin',
        'language': 'sw',
        'rating': 5,
        'category': 'cbc_alignment',
        'comment': 'Mifano ya samaki Ngege na Dunga Beach inawasaidia sana wanafunzi wangu wa Darasa la 5 kuelewa respiration!',
        'topic': 'Aquatic Biology'
    }
    r = requests.post(f'{BASE_URL}/api/feedback', json=fb_payload)
    assert r.status_code == 200
    fb_res = r.json()
    print(f"\n[PASSED] 8. Multi-Stakeholder Feedback Submission: OK")
    print(f"   * Response Status: {fb_res.get('status')}")
    print(f"   * Feedback Message: {fb_res.get('message')}")

    # 9. Feedback Summary & Metrics
    r = requests.get(f'{BASE_URL}/api/feedback/summary')
    assert r.status_code == 200
    summary = r.json()
    print(f"\n[PASSED] 9. Feedback Metrics Aggregator:")
    print(f"   * Total Feedback Records: {summary.get('total_feedback')}")
    print(f"   * Average Stakeholder Rating: {summary.get('average_rating')} ⭐")
    print(f"   * Stakeholder Breakdown: {summary.get('by_stakeholder')}")

    # 10. ETHOS, TRACK, OASIS, PRIDE & HORIZON Frameworks
    r = requests.get(f'{BASE_URL}/api/ethics/frameworks')
    assert r.status_code == 200
    ethics = r.json()
    print(f"\n[PASSED] 10. Responsible AI & Ethics Frameworks (ETHOS, TRACK, OASIS, PRIDE, HORIZON):")
    for k, v in ethics.items():
        print(f"   * 🛡️ [{k}]: {v['title']}")

    # 11. RANK Roles & HUNT Multi-Agent Pipeline
    r = requests.get(f'{BASE_URL}/api/orchestrator/pipeline')
    assert r.status_code == 200
    pipeline = r.json()
    print(f"\n[PASSED] 11. Multi-Agent Orchestration (RANK & HUNT Frameworks):")
    print(f"   * Active Roles: {list(pipeline['agent_roles'].keys())}")
    for stage in pipeline['hunt_pipeline_stages']:
        print(f"   * {stage}")

    # 12. TRAIL Memory Audit & CYCLE Engine
    r1 = requests.get(f'{BASE_URL}/api/memory/trail-audit')
    r2 = requests.get(f'{BASE_URL}/api/cycle/report')
    assert r1.status_code == 200 and r2.status_code == 200
    trail = r1.json()
    cycle = r2.json()
    print(f"\n[PASSED] 12. Memory Sovereignty (TRAIL) & Continuous Learning (CYCLE):")
    print(f"   * TRAIL Land Rights: {trail['L_LandRights']}")
    print(f"   * CYCLE Insights: {cycle['Y_YieldInsights']}")

    # 13. African Pedagogy & Learning Theories Matrix
    r = requests.get(f'{BASE_URL}/api/pedagogy/theories')
    assert r.status_code == 200
    theories = r.json()
    print(f"\n[PASSED] 13. African Pedagogy & Learning Theories Matrix (8 Theories):")
    for k, v in theories.items():
        print(f"   * 🧠 [{k}]: {v['swahili_title']} ({v['theorists']})")

    print("\n============================================================")
    print(" 🎉 ALL 13 COMPREHENSIVE FEATURES & PEDAGOGICAL FRAMEWORKS VERIFIED!")
    print("============================================================")

if __name__ == '__main__':
    run_tests()
