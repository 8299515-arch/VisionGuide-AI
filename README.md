# VisionGuide AI 🧠👁️

AI-powered assistive vision system for blind and visually impaired users.

## 🚀 Overview
VisionGuide AI is a multimodal assistance system that helps visually impaired users understand their environment in real time using computer vision + AI.

Core capabilities:
- Object detection 👀
- Text recognition (OCR) 📖
- Scene description 🧠
- Navigation hints 🧭 (future)

---

## 🏗️ System Architecture (Sprint 1)

```
Mobile App → FastAPI Backend → AI Pipeline → Vision Modules → Response API
```

### Core modules
- Backend: FastAPI (Python)
- AI Layer: Vision pipeline (YOLO / OCR / LLM)
- Client: Mobile (Flutter / React Native planned)
- Infra: Docker + CI/CD (GitHub Actions)

---

## ⚙️ Sprint 1 Scope

This sprint establishes the foundation:

- Backend project structure
- API skeleton
- AI pipeline skeleton (mocked)
- Docker setup (coming next step)
- Health check endpoint
- Analyze image endpoint (mock response)

---

## 📡 API Endpoints

### Health
```
GET /health
```

Response:
```json
{ "status": "ok" }
```

### Analyze Image
```
POST /analyze-image
```

Response:
```json
{
  "objects": [],
  "text": "",
  "description": "",
  "navigation_hint": ""
}
```

---

## 🧠 AI Pipeline (v1 design)

```
process_image(image)
  ├── detect_objects()
  ├── extract_text()
  ├── describe_scene()
  └── aggregate_response()
```

---

## 🐳 Local Run (future Sprint 1 step)

```bash
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
```

---

## 🛣️ Roadmap

### Sprint 1
- Backend foundation
- AI pipeline skeleton
- Docker setup

### Sprint 2
- Real object detection (YOLO/DETR)
- OCR engine integration
- Voice output (TTS)

### Sprint 3
- Mobile app MVP
- Real-time camera streaming

---

## 🔐 Notes
This project is designed as a scalable assistive AI system for real-world usage.
