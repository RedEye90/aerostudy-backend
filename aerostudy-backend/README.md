# AeroStudy Backend API

FastAPI server for AeroStudy Android app.

---

## 📁 File Structure

```
aerostudy-backend/
├── main.py          ← API routes (mat chhedo)
├── data.py          ← YAHAN content add karo ✅
├── requirements.txt ← Dependencies
├── render.yaml      ← Render deployment config
└── README.md
```

---

## ▶️ Local mein chalana

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API khulegi: http://localhost:8000

Interactive docs: http://localhost:8000/docs

---

## 🌐 Render.com pe Deploy karna

1. GitHub pe ek naya repo banao: `aerostudy-backend`
2. In files ko push karo:
   ```bash
   git init
   git add .
   git commit -m "first commit"
   git remote add origin https://github.com/TERA_USERNAME/aerostudy-backend.git
   git push -u origin main
   ```
3. **render.com** pe jao → New → Web Service
4. GitHub repo select karo
5. Sab auto-detect ho jayega (`render.yaml` se)
6. Deploy karo → URL milegi jaise: `https://aerostudy-api.onrender.com`

---

## ✏️ Content Add Karna (data.py)

### CPL Subject mein Note add karna:
```python
"notes": [
    {
        "title": "Naye Note Ka Title",
        "content": "Yahan pura content likhna..."
    },
    # ... aur notes
]
```

### CPL Subject mein MCQ add karna:
```python
"mcq": [
    {
        "question": "Question text?",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": 0,   # 0 = A, 1 = B, 2 = C, 3 = D
        "explanation": "Yahan explanation likho"
    },
]
```

### AME Module mein Study Material add karna:
```python
"study_material": [
    {
        "topic": "Topic Name",
        "content": "Detailed content yahan..."
    },
]
```

---

## 🔗 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Health check |
| `GET /cpl/subjects` | Sare CPL subjects |
| `GET /cpl/subjects/{id}` | Ek subject ki detail |
| `GET /cpl/subjects/{id}/notes` | Subject ke notes |
| `GET /cpl/subjects/{id}/questions` | Subject ke questions |
| `GET /cpl/subjects/{id}/mcq` | Subject ke MCQs |
| `GET /cpl/subjects/{id}/mock-tests` | Subject ke mock tests |
| `GET /ame/modules` | Sare AME modules |
| `GET /ame/modules/{id}` | Ek module ki detail |
| `GET /ame/modules/{id}/study-material` | Module ka study material |
| `GET /ame/modules/{id}/diagrams` | Module ke diagrams |
| `GET /ame/modules/{id}/questions` | Module ke questions |
| `GET /ame/modules/{id}/practice-test` | Module ka practice test |

---

## 📱 Android App mein Connect karna

`app.js` mein yeh URL set karo:
```javascript
const API_BASE = "https://aerostudy-api.onrender.com";  // apna URL daalo
```

Phir fetch karo:
```javascript
const res = await fetch(`${API_BASE}/cpl/subjects`);
const subjects = await res.json();
```
