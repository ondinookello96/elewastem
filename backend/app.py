"""
ElewaSTEM FastAPI Server with Multi-Stakeholder Ecosystem Support
Serves Learners (PWA, Voice, Quizzes), Teachers (CBC Lesson Plans), Parents (SMS Digests), Community Mentors, and Curriculum Bodies.
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

app = FastAPI(
    title="ElewaSTEM Multi-Stakeholder API",
    description="Multilingual Adaptive AI STEM Tutor for African Children with Parent, Teacher, and Community Stakeholder Hubs",
    version="1.2.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")


# Request & Response Models
class ChatRequest(BaseModel):
    student_id: str = "demo_student"
    message: str
    language: str = "swahili"  # "swahili", "english", "sheng"
    region: str = "lake_basin"
    gps_coordinates: Optional[Dict[str, float]] = None
    simplify: bool = False


class ProfileUpdateRequest(BaseModel):
    name: Optional[str] = None
    grade_level: Optional[str] = None
    preferred_language: Optional[str] = None
    current_region: Optional[str] = None
    gps_coordinates: Optional[Dict[str, float]] = None


class QuizResultRequest(BaseModel):
    student_id: str
    topic: str
    passed: bool
    score: int = 100


# --- Core Learner Endpoints ---

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "app": "ElewaSTEM",
        "version": "1.2.0",
        "features": [
            "multilingual",
            "offline_pwa",
            "voice_accessibility_tts_stt",
            "geo_adaptive_context",
            "dpa_2019_consent",
            "stakeholders_parents_teachers_mentors"
        ],
        "gemini_connected": elewa_agent.client is not None
    }


@app.get("/api/regions")
async def list_regions():
    """Returns available African eco-regions for localized context."""
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
    return {
        "pack_name": "ElewaSTEM Regional Offline Knowledge Vault",
        "version": "1.2",
        "module_count": len(modules),
        "regions": regions,
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


# --- Stakeholder Hub Endpoints ---

@app.get("/api/teacher/lesson-plan")
async def get_teacher_lesson_plan(topic: str = "photosynthesis", region: str = "lake_basin"):
    """Returns a CBC-aligned STEM lesson plan with local African analogies and diagnostics."""
    return generate_teacher_lesson_plan(topic, region)


@app.get("/api/parent/digest/{student_id}")
async def get_parent_progress_digest(student_id: str, region: str = "lake_basin"):
    """Returns a simplified progress digest and SMS alert for parents on feature phones."""
    profile = student_memory.get_or_create_profile(student_id).model_dump()
    return generate_parent_digest(profile, region)


@app.get("/api/community/activities")
async def get_community_activities(region: str = "lake_basin"):
    """Returns low-cost STEM club projects for village community centers and mentors."""
    return get_community_club_projects(region)


# --- SMS Gateway ---

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

    is_sw = any(w in user_msg.lower() for w in ["eleza", "nini", "kwa nini", "jinsi", "sayansi", "mmea", "umeme", "hesabu"])
    lang = "swahili" if is_sw else "english"

    region = "lake_basin"
    if any(w in user_msg.lower() for w in ["pwani", "mombasa", "coast", "bahari", "dar"]):
        region = "coastal"
    elif any(w in user_msg.lower() for w in ["ziwa", "victoria", "kisumu", "mwanza", "samaki"]):
        region = "lake_basin"
    elif any(w in user_msg.lower() for w in ["turkana", "garissa", "kavu", "arid", "jua"]):
        region = "arid"
    elif any(w in user_msg.lower() for w in ["jiji", "nairobi", "kampala", "urban", "matatu"]):
        region = "urban"

    response = elewa_agent.generate_response(
        student_id=f"sms_{user_phone}",
        message=user_msg,
        target_language=lang,
        region=region,
        simplify=True
    )
    
    clean_text = response["text"].replace("#", "").replace("**", "").replace("---", "").strip()
    sms_reply = clean_text[:450] + ("..." if len(clean_text) > 450 else "")
    return sms_reply


# --- Serve Static Frontend ---
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
