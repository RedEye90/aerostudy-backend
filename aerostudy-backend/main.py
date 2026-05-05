from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from data import CPL_SUBJECTS, AME_MODULES

app = FastAPI(title="AeroStudy API", version="1.0.0")

# Allow Android WebView & browser to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────────────────
#  ROOT
# ─────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {"message": "AeroStudy API is live ✈️"}


# ─────────────────────────────────────────────────────────
#  CPL  –  all subjects list
# ─────────────────────────────────────────────────────────
@app.get("/cpl/subjects")
def get_cpl_subjects():
    return [
        {
            "id": s["id"],
            "name": s["name"],
            "icon": s["icon"],
            "description": s["description"],
        }
        for s in CPL_SUBJECTS
    ]


# ─────────────────────────────────────────────────────────
#  CPL  –  detail of one subject
# ─────────────────────────────────────────────────────────
@app.get("/cpl/subjects/{subject_id}")
def get_cpl_subject(subject_id: str):
    subject = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject


# ─────────────────────────────────────────────────────────
#  CPL  –  notes for a subject
# ─────────────────────────────────────────────────────────
@app.get("/cpl/subjects/{subject_id}/notes")
def get_cpl_notes(subject_id: str):
    subject = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return {"subject_id": subject_id, "notes": subject.get("notes", [])}


# ─────────────────────────────────────────────────────────
#  CPL  –  questions for a subject
# ─────────────────────────────────────────────────────────
@app.get("/cpl/subjects/{subject_id}/questions")
def get_cpl_questions(subject_id: str):
    subject = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return {"subject_id": subject_id, "questions": subject.get("questions", [])}


# ─────────────────────────────────────────────────────────
#  CPL  –  MCQs for a subject
# ─────────────────────────────────────────────────────────
@app.get("/cpl/subjects/{subject_id}/mcq")
def get_cpl_mcq(subject_id: str):
    subject = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return {"subject_id": subject_id, "mcq": subject.get("mcq", [])}


# ─────────────────────────────────────────────────────────
#  CPL  –  mock tests for a subject
# ─────────────────────────────────────────────────────────
@app.get("/cpl/subjects/{subject_id}/mock-tests")
def get_cpl_mock_tests(subject_id: str):
    subject = next((s for s in CPL_SUBJECTS if s["id"] == subject_id), None)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return {"subject_id": subject_id, "mock_tests": subject.get("mock_tests", [])}


# ─────────────────────────────────────────────────────────
#  AME  –  all modules list
# ─────────────────────────────────────────────────────────
@app.get("/ame/modules")
def get_ame_modules():
    return [
        {
            "id": m["id"],
            "number": m["number"],
            "title": m["title"],
        }
        for m in AME_MODULES
    ]


# ─────────────────────────────────────────────────────────
#  AME  –  detail of one module
# ─────────────────────────────────────────────────────────
@app.get("/ame/modules/{module_id}")
def get_ame_module(module_id: int):
    module = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    return module


# ─────────────────────────────────────────────────────────
#  AME  –  study material for a module
# ─────────────────────────────────────────────────────────
@app.get("/ame/modules/{module_id}/study-material")
def get_ame_study_material(module_id: int):
    module = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    return {"module_id": module_id, "study_material": module.get("study_material", [])}


# ─────────────────────────────────────────────────────────
#  AME  –  diagrams for a module
# ─────────────────────────────────────────────────────────
@app.get("/ame/modules/{module_id}/diagrams")
def get_ame_diagrams(module_id: int):
    module = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    return {"module_id": module_id, "diagrams": module.get("diagrams", [])}


# ─────────────────────────────────────────────────────────
#  AME  –  previous year questions for a module
# ─────────────────────────────────────────────────────────
@app.get("/ame/modules/{module_id}/questions")
def get_ame_questions(module_id: int):
    module = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    return {"module_id": module_id, "questions": module.get("questions", [])}


# ─────────────────────────────────────────────────────────
#  AME  –  practice test for a module
# ─────────────────────────────────────────────────────────
@app.get("/ame/modules/{module_id}/practice-test")
def get_ame_practice_test(module_id: int):
    module = next((m for m in AME_MODULES if m["id"] == module_id), None)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    return {"module_id": module_id, "practice_test": module.get("practice_test", [])}
