import os
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from data import CPL_SUBJECTS, AME_MODULES

app = FastAPI(title="AeroStudy API", version="2.0.0")

# Allow Android WebView & browser to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────────────────
#  AI TEACHER  –  Groq API (FREE! Fast! No rate limits!)
#  Render.com pe GROQ_API_KEY env variable set karo
#  Free key yahan se lo: https://console.groq.com
# ─────────────────────────────────────────────────────────

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

AI_SYSTEM_PROMPT = """Tu AeroStudy ka AI Teacher hai. Tera naam "Aero Sir" hai.

Tu CPL (Commercial Pilot License) aur AME (Aircraft Maintenance Engineering) students ko padhata hai.

Rules:
- Hinglish mein baat kar (Hindi + English mix) — bilkul ek friendly teacher ki tarah
- Agar student Hindi mein pooche to Hindi mein jawab de, English mein pooche to English mein
- Har jawab mein pehle concept clearly explain kar, phir aviation context mein example de
- Jawab concise rakho — max 150 words, lekin complete hona chahiye
- Bullet points use kar jab list banana ho
- Agar koi aviation se related nahi sawaal pooche, politely redirect kar
- Hamesha encouraging rehna — "Bahut accha sawaal hai!", "Bilkul sahi socha!" jaise phrases use kar
- Important terms bold karo using **term** format
- Agar formula ho to clearly likho

Tu ek experienced aviation instructor hai jo students ko genuinely samajhna chahta hai."""


class Message(BaseModel):
    role: str   # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]
    subject: str = ""   # optional: "navigation", "meteorology", etc.


@app.post("/ai/chat")
async def ai_chat(req: ChatRequest):
    if not GROQ_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY not set on server. Render.com pe env variable add karo. Free key: https://console.groq.com"
        )

    # Build messages for Groq (same format as OpenAI)
    messages = [{"role": "system", "content": AI_SYSTEM_PROMPT}]

    for m in req.messages:
        messages.append({"role": m.role, "content": m.content})

    # Subject context first user message mein add karo
    if req.subject:
        for i, msg in enumerate(messages):
            if msg["role"] == "user":
                messages[i] = {
                    "role": "user",
                    "content": f"[Subject context: {req.subject}]\n{msg['content']}"
                }
                break

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "llama-3.3-70b-versatile",
                    "messages": messages,
                    "max_tokens": 512,
                    "temperature": 0.7,
                },
            )
            resp.raise_for_status()
            data = resp.json()
            reply = data["choices"][0]["message"]["content"]
            return {"reply": reply}

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"Groq API error: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ─────────────────────────────────────────────────────────
#  ROOT
# ─────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {"message": "AeroStudy API is live ✈️"}


@app.get("/cpl/subjects")
def get_cpl_subjects():
    return [{"id": s["id"], "name": s["name"], "icon": s["icon"], "description": s["description"]} for s in CPL_SUBJECTS]

@app.get("/cpl/subjects/{subject_id}")
def get_cpl_subject(subject_id: str):
    subject = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not subject: raise HTTPException(status_code=404, detail="Subject not found")
    return subject

@app.get("/cpl/subjects/{subject_id}/notes")
def get_cpl_notes(subject_id: str):
    subject = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not subject: raise HTTPException(status_code=404, detail="Subject not found")
    return {"subject_id": subject_id, "notes": subject.get("notes", [])}

@app.get("/cpl/subjects/{subject_id}/questions")
def get_cpl_questions(subject_id: str):
    subject = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not subject: raise HTTPException(status_code=404, detail="Subject not found")
    return {"subject_id": subject_id, "questions": subject.get("questions", [])}

@app.get("/cpl/subjects/{subject_id}/mcq")
def get_cpl_mcq(subject_id: str):
    subject = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not subject: raise HTTPException(status_code=404, detail="Subject not found")
    return {"subject_id": subject_id, "mcq": subject.get("mcq", [])}

@app.get("/cpl/subjects/{subject_id}/mock-tests")
def get_cpl_mock_tests(subject_id: str):
    subject = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not subject: raise HTTPException(status_code=404, detail="Subject not found")
    return {"subject_id": subject_id, "mock_tests": subject.get("mock_tests", [])}

@app.get("/ame/modules")
def get_ame_modules():
    return [{"id": m["id"], "number": m["number"], "title": m["title"]} for m in AME_MODULES]

@app.get("/ame/modules/{module_id}")
def get_ame_module(module_id: int):
    module = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not module: raise HTTPException(status_code=404, detail="Module not found")
    return module

@app.get("/ame/modules/{module_id}/study-material")
def get_ame_study_material(module_id: int):
    module = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not module: raise HTTPException(status_code=404, detail="Module not found")
    return {"module_id": module_id, "study_material": module.get("study_material", [])}

@app.get("/ame/modules/{module_id}/diagrams")
def get_ame_diagrams(module_id: int):
    module = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not module: raise HTTPException(status_code=404, detail="Module not found")
    return {"module_id": module_id, "diagrams": module.get("diagrams", [])}

@app.get("/ame/modules/{module_id}/questions")
def get_ame_questions(module_id: int):
    module = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not module: raise HTTPException(status_code=404, detail="Module not found")
    return {"module_id": module_id, "questions": module.get("questions", [])}

@app.get("/ame/modules/{module_id}/practice-test")
def get_ame_practice_test(module_id: int):
    module = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not module: raise HTTPException(status_code=404, detail="Module not found")
    return {"module_id": module_id, "practice_test": module.get("practice_test", [])}
