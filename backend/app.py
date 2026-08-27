"""
ElewaSTEM FastAPI Server
Serves the Bilingual AI STEM Tutor API, Offline Caching Pack, SMS/USSD Gateway, and Static PWA Frontend.
"""

import os
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, PlainTextResponse
from pydantic import BaseModel

from agent import elewa_agent
from memory import student_memory
from tools import get_offline_starter_pack, find_offline_topic

app = FastAPI(
    title="ElewaSTEM API",
    description="Multilingual Adaptive AI STEM Tutor for African Children",
    version="1.0.0"
)

# CORS middleware for open accessibility
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
    simplify: bool = False


class ProfileUpdateRequest(BaseModel):
    name: Optional[str] = None
    grade_level: Optional[str] = None
    preferred_language: Optional[str] = None


class QuizResultRequest(BaseModel):
    student_id: str
    topic: str
    passed: bool
    score: int = 100


# --- API Routes ---

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "app": "ElewaSTEM",
        "version": "1.0.0",
        "gemini_connected": elewa_agent.client is not None
    }


@app.post("/api/chat")
async def chat_with_agent(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    response = elewa_agent.generate_response(
        student_id=req.student_id,
        message=req.message,
        target_language=req.language,
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
        language=req.preferred_language
    )
    if req.grade_level:
        profile.grade_level = req.grade_level
        student_memory._save_profiles()
    return profile.model_dump()


@app.get("/api/offline-pack")
async def download_offline_pack():
    """Returns bundled starter STEM lessons, experiments, and quizzes for full offline caching."""
    modules = get_offline_starter_pack()
    return {
        "pack_name": "ElewaSTEM Offline Knowledge Vault",
        "version": "1.0",
        "module_count": len(modules),
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


@app.post("/api/sms", response_class=PlainTextResponse)
async def sms_gateway(
    from_: str = Form(None, alias="from"),
    text: str = Form(None),
    phoneNumber: str = Form(None)
):
    """
    SMS/USSD Webhook endpoint (compatible with Africa's Talking format).
    Allows children with basic 2G feature phones (non-smartphones) to text questions.
    """
    user_phone = phoneNumber or from_ or "sms_user"
    user_msg = text or ""
    
    if not user_msg:
        return "Karibu ElewaSTEM! Tuma swali lako la Sayansi au Hesabu (mfano: 'eleza umeme' au 'what is photosynthesis')."

    # Detect language
    is_sw = any(w in user_msg.lower() for w in ["eleza", "nini", "kwa nini", "jinsi", "sayansi", "mmea", "umeme", "hesabu"])
    lang = "swahili" if is_sw else "english"

    response = elewa_agent.generate_response(
        student_id=f"sms_{user_phone}",
        message=user_msg,
        target_language=lang,
        simplify=True
    )
    
    # Strip markdown headers for clean SMS display
    clean_text = response["text"].replace("#", "").replace("**", "").replace("---", "").strip()
    # Format to concise SMS length
    sms_reply = clean_text[:450] + ("..." if len(clean_text) > 450 else "")
    return sms_reply


# --- Serve Frontend Static Files ---
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
