"""
ElewaSTEM FastAPI Server with Pan-African Language Scaling & Cross-Border Data Protection Framework
Serves 16+ African languages (Masakhane / Gemini), 8+ Data Protection Jurisdictions, and Universal Stakeholder Hubs.
"""

import os
from typing import Optional, List, Dict, Any
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, PlainTextResponse
from pydantic import BaseModel

from agent import elewa_agent
from memory import student_memory
from tools import (
    get_offline_starter_pack,
    get_available_regions,
    find_offline_topic,
    generate_teacher_lesson_plan,
    generate_parent_digest,
    get_community_club_projects
)
from african_languages import get_all_african_languages, get_language_meta
from privacy_matrix import get_all_jurisdictions, get_privacy_framework

app = FastAPI(
    title="ElewaSTEM Pan-African Multi-Language & Multi-Jurisdiction API",
    description="Multilingual Adaptive AI STEM Tutor for African Children across 16+ African Languages & Pan-African Data Protection Laws",
    version="1.3.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")


# Request Models
class ChatRequest(BaseModel):
    student_id: str = "demo_student"
    message: str
    language: str = "sw"  # Can be sw, sheng, yo, ha, ig, pcm, am, om, so, zu, xh, rw, lg, tw, sn, ln, en
    region: str = "lake_basin"
    jurisdiction: str = "KE"  # KE, NG, ZA, GH, UG, TZ, RW, AU_CONTINENTAL
    gps_coordinates: Optional[Dict[str, float]] = None
    simplify: bool = False


class ProfileUpdateRequest(BaseModel):
    name: Optional[str] = None
    grade_level: Optional[str] = None
    preferred_language: Optional[str] = None
    current_region: Optional[str] = None
    jurisdiction: Optional[str] = "KE"
    gps_coordinates: Optional[Dict[str, float]] = None


class QuizResultRequest(BaseModel):
    student_id: str
    topic: str
    passed: bool
    score: int = 100


# --- Endpoints ---

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "app": "ElewaSTEM Pan-African",
        "version": "1.3.0",
        "supported_african_languages_count": len(get_all_african_languages()),
        "data_protection_jurisdictions_count": len(get_all_jurisdictions()),
        "features": [
            "pan_african_languages_masakhane_gemini",
            "cross_border_data_protection_matrix",
            "offline_pwa",
            "universal_accessibility_tts_stt_tactile_sign",
            "stakeholders_parents_teachers_mentors"
        ],
        "gemini_connected": elewa_agent.client is not None
    }


@app.get("/api/languages")
async def list_african_languages():
    """Returns the Pan-African language registry."""
    return get_all_african_languages()


@app.get("/api/privacy/jurisdictions")
async def list_privacy_jurisdictions():
    """Returns the Pan-African Data Protection Legal Matrix."""
    return get_all_jurisdictions()


@app.get("/api/privacy/jurisdiction/{country_code}")
async def get_jurisdiction(country_code: str):
    return get_privacy_framework(country_code)


@app.get("/api/regions")
async def list_regions():
    return get_available_regions()


@app.post("/api/chat")
async def chat_with_agent(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    if req.gps_coordinates:
        student_memory.update_geo_location(
            req.student_id,
            region=req.region,
            lat=req.gps_coordinates.get("lat"),
            lon=req.gps_coordinates.get("lon")
        )

    response = elewa_agent.generate_response(
        student_id=req.student_id,
        message=req.message,
        target_language=req.language,
        region=req.region,
        simplify=req.simplify
    )
    # Attach language and privacy metadata
    response["language_meta"] = get_language_meta(req.language)
    response["jurisdiction_meta"] = get_privacy_framework(req.jurisdiction)
    return response


@app.get("/api/profile/{student_id}")
async def get_profile(student_id: str):
    profile = student_memory.get_or_create_profile(student_id)
    return profile.model_dump()


@app.post("/api/profile/{student_id}")
async def update_profile(student_id: str, req: ProfileUpdateRequest):
    profile = student_memory.get_or_create_profile(
        student_id=student_id,
        name=req.name,
        language=req.preferred_language,
        region=req.current_region
    )
    if req.grade_level:
        profile.grade_level = req.grade_level
    if req.gps_coordinates:
        profile.gps_coordinates = req.gps_coordinates
    student_memory._save_profiles()
    return profile.model_dump()


@app.get("/api/offline-pack")
async def download_offline_pack():
    modules = get_offline_starter_pack()
    regions = get_available_regions()
    languages = get_all_african_languages()
    privacy_frameworks = get_all_jurisdictions()
    return {
        "pack_name": "ElewaSTEM Pan-African Offline Vault",
        "version": "1.3",
        "module_count": len(modules),
        "regions": regions,
        "languages": languages,
        "privacy_jurisdictions": privacy_frameworks,
        "modules": modules
    }


@app.post("/api/quiz-result")
async def submit_quiz_result(req: QuizResultRequest):
    student_memory.record_quiz_result(
        student_id=req.student_id,
        topic=req.topic,
        passed=req.passed,
        score=req.score
    )
    profile = student_memory.get_or_create_profile(req.student_id)
    return {
        "message": "Quiz recorded successfully",
        "mastery_graph": profile.mastery_graph,
        "badges": profile.badges
    }


@app.get("/api/teacher/lesson-plan")
async def get_teacher_lesson_plan(topic: str = "photosynthesis", region: str = "lake_basin"):
    return generate_teacher_lesson_plan(topic, region)


@app.get("/api/parent/digest/{student_id}")
async def get_parent_progress_digest(student_id: str, region: str = "lake_basin"):
    profile = student_memory.get_or_create_profile(student_id).model_dump()
    return generate_parent_digest(profile, region)


@app.get("/api/community/activities")
async def get_community_activities(region: str = "lake_basin"):
    return get_community_club_projects(region)


@app.post("/api/sms", response_class=PlainTextResponse)
async def sms_gateway(
    from_: str = Form(None, alias="from"),
    text: str = Form(None),
    phoneNumber: str = Form(None)
):
    user_phone = phoneNumber or from_ or "sms_user"
    user_msg = text or ""
    
    if not user_msg:
        return "Karibu ElewaSTEM! Tuma swali lako la Sayansi (mfano: 'eleza umeme kisumu' au 'what is photosynthesis')."

    # Multilingual detector (Swahili, Yoruba, Hausa, Igbo, English)
    is_sw = any(w in user_msg.lower() for w in ["eleza", "nini", "kwa nini", "jinsi", "sayansi", "mmea", "umeme", "hesabu"])
    is_yo = any(w in user_msg.lower() for w in ["bawo", "kini", "sayensi", "oluko"])
    is_ha = any(w in user_msg.lower() for w in ["sannu", "menene", "kimiyya", "malami"])
    is_ig = any(w in user_msg.lower() for w in ["kedu", "sayensi", "onye nkuzi"])

    lang = "sw"
    if is_yo: lang = "yo"
    elif is_ha: lang = "ha"
    elif is_ig: lang = "ig"
    elif not is_sw: lang = "en"

    response = elewa_agent.generate_response(
        student_id=f"sms_{user_phone}",
        message=user_msg,
        target_language=lang,
        region="lake_basin",
        simplify=True
    )
    
    clean_text = response["text"].replace("#", "").replace("**", "").replace("---", "").strip()
    sms_reply = clean_text[:450] + ("..." if len(clean_text) > 450 else "")
    return sms_reply


if os.path.exists(FRONTEND_DIR):
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

    @app.get("/")
    async def serve_index():
        return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

    @app.get("/{full_path:path}")
    async def serve_frontend_assets(full_path: str):
        file_path = os.path.join(FRONTEND_DIR, full_path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))
