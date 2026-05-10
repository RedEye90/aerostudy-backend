import os
import httpx
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from data import CPL_SUBJECTS, AME_MODULES

app = FastAPI(title="AeroStudy API — Capt.Aero Edition", version="3.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"],
)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
ADMIN_SECRET = os.environ.get("ADMIN_SECRET", "aerostudy-admin-2024")

# Groq model — llama fast & free tier friendly
GROQ_MODEL = "llama-3.3-70b-versatile"
GROQ_URL   = "https://api.groq.com/openai/v1/chat/completions"

# ─────────────────────────────────────────────────────────
#  Capt.Aero — AI System Prompt
# ─────────────────────────────────────────────────────────

AI_SYSTEM_PROMPT = """Tu AeroStudy ka AI Teacher hai. Tera naam "Capt.Aero" hai.

Tu CPL (Commercial Pilot License) aur AME (Aircraft Maintenance Engineering) DGCA students ka personal aviation instructor hai.

Rules:
- Hinglish mein baat kar (Hindi + English mix) — bilkul ek friendly senior pilot/engineer ki tarah
- Agar student Hindi mein pooche to Hindi mein jawab de, English mein pooche to English mein
- Har jawab mein pehle concept clearly explain kar, phir aviation/DGCA context mein example de
- Jawab concise lekin complete rakho — max 200 words regular questions ke liye
- Diagram ya PYQ explain karne par thoda detail mein jao — max 300 words
- Bullet points use kar jab list banana ho
- Agar koi aviation se related nahi sawaal pooche, politely redirect kar
- Hamesha encouraging rehna — "Bahut accha sawaal hai!", "Bilkul sahi socha!" jaise phrases use kar
- Important terms bold karo using **term** format
- Agar formula ho to clearly likho
- Weak topics pe extra focus karo aur practical examples do
- DGCA exam pattern ke hisaab se important points highlight karo

Tera role hai student ko DGCA exam crack karana aur aviation ka asli passion jagana."""


# ─────────────────────────────────────────────────────────
#  In-memory admin push storage
# ─────────────────────────────────────────────────────────
admin_diagrams      = {}   # {module_id: [diagram_dict, ...]}
admin_study         = {}   # {module_id: [study_material_dict, ...]}
admin_pyq           = {}   # {module_id: [question_dict, ...]}
admin_practice_test = {}   # {module_id: [mcq_dict, ...]}
admin_cpl_notes     = {}   # {subject_id: [note_dict, ...]}
admin_cpl_mcq       = {}   # {subject_id: [mcq_dict, ...]}


# ─────────────────────────────────────────────────────────
#  Pydantic models
# ─────────────────────────────────────────────────────────

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    subject: str = ""

class DiagramPush(BaseModel):
    title: str
    description: str
    image_url: Optional[str] = ""

class StudyMaterialPush(BaseModel):
    topic: str
    content: str

class QuestionPush(BaseModel):
    q: str
    a: str
    year: Optional[str] = ""

class CplNotePush(BaseModel):
    title: str
    content: str

class CplMcqPush(BaseModel):
    question: str
    options: List[str]
    answer: int
    explanation: str

class PracticeTestPush(BaseModel):
    question: str
    options: List[str]
    answer: int
    explanation: Optional[str] = ""


# ─────────────────────────────────────────────────────────
#  Helper — admin auth check
# ─────────────────────────────────────────────────────────
def check_admin(x_admin_secret: str):
    if x_admin_secret != ADMIN_SECRET:
        raise HTTPException(status_code=403, detail="Invalid admin secret. X-Admin-Secret header check karo.")


# ─────────────────────────────────────────────────────────
#  ROOT
# ─────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {"message": "AeroStudy API — Capt.Aero Edition is live ✈️", "version": "3.0.0"}


# ─────────────────────────────────────────────────────────
#  AI CHAT — Capt.Aero (Groq)
# ─────────────────────────────────────────────────────────
@app.post("/ai/chat")
async def ai_chat(req: ChatRequest):
    if not GROQ_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY not set. Render.com pe env variable add karo."
        )

    # Build messages list — system prompt pehle
    messages = [{"role": "system", "content": AI_SYSTEM_PROMPT}]

    # Subject context pehle user message mein inject karo
    user_messages = [{"role": m.role, "content": m.content} for m in req.messages]
    if req.subject and user_messages:
        first = user_messages[0]
        if first["role"] == "user":
            user_messages[0] = {
                "role": "user",
                "content": f"[Subject/Module context: {req.subject}]\n{first['content']}"
            }

    messages.extend(user_messages)

    # Max tokens by context
    subj_lower = req.subject.lower()
    if any(kw in subj_lower for kw in ["review", "auto-review", "adaptive"]):
        max_tok = 800
    elif any(kw in subj_lower for kw in ["diagram", "pyq", "video"]):
        max_tok = 600
    else:
        max_tok = 400

    payload = {
        "model"      : GROQ_MODEL,
        "messages"   : messages,
        "max_tokens" : max_tok,
        "temperature": 0.7,
        "top_p"      : 0.9,
    }

    try:
        async with httpx.AsyncClient(timeout=40.0) as client:
            resp = await client.post(
                GROQ_URL,
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type" : "application/json",
                },
                json=payload,
            )
            resp.raise_for_status()
            data  = resp.json()
            reply = data["choices"][0]["message"]["content"]
            return {"reply": reply}

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"Groq API error: {e.response.text}")
    except (KeyError, IndexError) as e:
        raise HTTPException(status_code=502, detail=f"Groq response parse error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ─────────────────────────────────────────────────────────
#  CPL SUBJECTS — Read endpoints
# ─────────────────────────────────────────────────────────
@app.get("/cpl/subjects")
def get_cpl_subjects():
    return [{"id": s["id"], "name": s["name"], "icon": s["icon"], "description": s["description"]} for s in CPL_SUBJECTS]

@app.get("/cpl/subjects/{subject_id}")
def get_cpl_subject(subject_id: str):
    s = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not s: raise HTTPException(404, "Subject not found")
    return s

@app.get("/cpl/subjects/{subject_id}/notes")
def get_cpl_notes(subject_id: str):
    s = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not s: raise HTTPException(404, "Subject not found")
    base  = s.get("notes", [])
    extra = admin_cpl_notes.get(subject_id, [])
    return {"subject_id": subject_id, "notes": base + extra}

@app.get("/cpl/subjects/{subject_id}/questions")
def get_cpl_questions(subject_id: str):
    s = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not s: raise HTTPException(404, "Subject not found")
    return {"subject_id": subject_id, "questions": s.get("questions", [])}

@app.get("/cpl/subjects/{subject_id}/mcq")
def get_cpl_mcq(subject_id: str):
    s = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not s: raise HTTPException(404, "Subject not found")
    base  = s.get("mcq", [])
    extra = admin_cpl_mcq.get(subject_id, [])
    return {"subject_id": subject_id, "mcq": base + extra}

@app.get("/cpl/subjects/{subject_id}/mock-tests")
def get_cpl_mock_tests(subject_id: str):
    s = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not s: raise HTTPException(404, "Subject not found")
    return {"subject_id": subject_id, "mock_tests": s.get("mock_tests", [])}


# ─────────────────────────────────────────────────────────
#  CPL ADMIN PUSH endpoints
# ─────────────────────────────────────────────────────────
@app.post("/admin/cpl/{subject_id}/notes")
def admin_push_cpl_note(subject_id: str, note: CplNotePush, x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    if subject_id not in admin_cpl_notes:
        admin_cpl_notes[subject_id] = []
    admin_cpl_notes[subject_id].append({"title": note.title, "content": note.content})
    return {"status": "ok", "message": f"Note added to {subject_id}", "total": len(admin_cpl_notes[subject_id])}

@app.post("/admin/cpl/{subject_id}/mcq")
def admin_push_cpl_mcq(subject_id: str, mcq: CplMcqPush, x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    if subject_id not in admin_cpl_mcq:
        admin_cpl_mcq[subject_id] = []
    admin_cpl_mcq[subject_id].append({
        "question": mcq.question,
        "options": mcq.options,
        "answer": mcq.answer,
        "explanation": mcq.explanation
    })
    return {"status": "ok", "message": f"MCQ added to {subject_id}", "total": len(admin_cpl_mcq[subject_id])}

@app.delete("/admin/cpl/{subject_id}/notes")
def admin_clear_cpl_notes(subject_id: str, x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    admin_cpl_notes[subject_id] = []
    return {"status": "ok", "message": f"Notes cleared for {subject_id}"}

@app.delete("/admin/cpl/{subject_id}/mcq")
def admin_clear_cpl_mcq(subject_id: str, x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    admin_cpl_mcq[subject_id] = []
    return {"status": "ok", "message": f"MCQs cleared for {subject_id}"}


# ─────────────────────────────────────────────────────────
#  AME MODULES — Read endpoints
# ─────────────────────────────────────────────────────────
@app.get("/ame/modules")
def get_ame_modules():
    return [{"id": m["id"], "number": m["number"], "title": m["title"]} for m in AME_MODULES]

@app.get("/ame/modules/{module_id}")
def get_ame_module(module_id: int):
    m = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not m: raise HTTPException(404, "Module not found")
    return m

@app.get("/ame/modules/{module_id}/study-material")
def get_ame_study_material(module_id: int):
    m = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not m: raise HTTPException(404, "Module not found")
    base  = m.get("study_material", [])
    extra = admin_study.get(module_id, [])
    return {"module_id": module_id, "study_material": base + extra}

@app.get("/ame/modules/{module_id}/diagrams")
def get_ame_diagrams(module_id: int):
    m = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not m: raise HTTPException(404, "Module not found")
    base  = m.get("diagrams", [])
    extra = admin_diagrams.get(module_id, [])
    return {"module_id": module_id, "diagrams": base + extra}

@app.get("/ame/modules/{module_id}/questions")
def get_ame_questions(module_id: int):
    m = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not m: raise HTTPException(404, "Module not found")
    base  = m.get("questions", [])
    extra = admin_pyq.get(module_id, [])
    return {"module_id": module_id, "questions": base + extra}

@app.get("/ame/modules/{module_id}/practice-test")
def get_ame_practice_test(module_id: int):
    m = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not m: raise HTTPException(404, "Module not found")
    base  = m.get("practice_test", [])
    extra = admin_practice_test.get(module_id, [])
    return {"module_id": module_id, "practice_test": base + extra}


# ─────────────────────────────────────────────────────────
#  AME ADMIN PUSH endpoints
# ─────────────────────────────────────────────────────────

# ── Diagrams ──
@app.post("/admin/ame/{module_id}/diagrams")
def admin_push_diagram(module_id: int, diagram: DiagramPush, x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    if module_id not in admin_diagrams:
        admin_diagrams[module_id] = []
    admin_diagrams[module_id].append({
        "title"      : diagram.title,
        "description": diagram.description,
        "image_url"  : diagram.image_url or ""
    })
    return {"status": "ok", "message": f"Diagram added to Module {module_id}", "total": len(admin_diagrams[module_id])}

@app.delete("/admin/ame/{module_id}/diagrams")
def admin_clear_diagrams(module_id: int, x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    admin_diagrams[module_id] = []
    return {"status": "ok", "message": f"Diagrams cleared for Module {module_id}"}

# ── Study Material ──
@app.post("/admin/ame/{module_id}/study-material")
def admin_push_study(module_id: int, item: StudyMaterialPush, x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    if module_id not in admin_study:
        admin_study[module_id] = []
    admin_study[module_id].append({"topic": item.topic, "content": item.content})
    return {"status": "ok", "message": f"Study material added to Module {module_id}", "total": len(admin_study[module_id])}

@app.delete("/admin/ame/{module_id}/study-material")
def admin_clear_study(module_id: int, x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    admin_study[module_id] = []
    return {"status": "ok", "message": f"Study material cleared for Module {module_id}"}

# ── Previous Year Questions ──
@app.post("/admin/ame/{module_id}/questions")
def admin_push_pyq(module_id: int, question: QuestionPush, x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    if module_id not in admin_pyq:
        admin_pyq[module_id] = []
    admin_pyq[module_id].append({"q": question.q, "a": question.a, "year": question.year or ""})
    return {"status": "ok", "message": f"PYQ added to Module {module_id}", "total": len(admin_pyq[module_id])}

@app.delete("/admin/ame/{module_id}/questions")
def admin_clear_pyq(module_id: int, x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    admin_pyq[module_id] = []
    return {"status": "ok", "message": f"PYQs cleared for Module {module_id}"}

# ── Practice Test ──
@app.post("/admin/ame/{module_id}/practice-test")
def admin_push_practice_test(module_id: int, item: PracticeTestPush, x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    if module_id not in admin_practice_test:
        admin_practice_test[module_id] = []
    admin_practice_test[module_id].append({
        "question"   : item.question,
        "options"    : item.options,
        "answer"     : item.answer,
        "explanation": item.explanation or ""
    })
    return {"status": "ok", "message": f"Practice test question added to Module {module_id}", "total": len(admin_practice_test[module_id])}

@app.delete("/admin/ame/{module_id}/practice-test")
def admin_clear_practice_test(module_id: int, x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    admin_practice_test[module_id] = []
    return {"status": "ok", "message": f"Practice test cleared for Module {module_id}"}

# ── Admin status ──
@app.get("/admin/status")
def admin_status(x_admin_secret: str = Header(...)):
    check_admin(x_admin_secret)
    return {
        "ame_diagrams_pushed"      : {k: len(v) for k, v in admin_diagrams.items()},
        "ame_study_pushed"         : {k: len(v) for k, v in admin_study.items()},
        "ame_pyq_pushed"           : {k: len(v) for k, v in admin_pyq.items()},
        "ame_practice_test_pushed" : {k: len(v) for k, v in admin_practice_test.items()},
        "cpl_notes_pushed"         : {k: len(v) for k, v in admin_cpl_notes.items()},
        "cpl_mcq_pushed"           : {k: len(v) for k, v in admin_cpl_mcq.items()},
    }
