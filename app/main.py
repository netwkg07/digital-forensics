from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

APP_ROOT = Path(__file__).resolve().parent

app = FastAPI(
    title="digital-forensics",
    description="A clean Digital Forensics lab for evidence handling, chain of custody, forensic timelines, reporting, and safe synthetic investigations.",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory=APP_ROOT / "static"), name="static")
templates = Jinja2Templates(directory=APP_ROOT / "templates")


@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "project_name": "digital-forensics",
            "safe_mode": "Enabled",
            "data_mode": "Synthetic evidence only",
        },
    )


@app.get("/health")
def health():
    return {
        "status": "ok",
        "project": "digital-forensics",
        "safe_mode": True,
        "synthetic_data_only": True,
    }


@app.get("/api/summary")
def summary():
    return {
        "project": "digital-forensics",
        "purpose": "Digital Forensics readiness and investigation workflow lab",
        "features": [
            "Evidence intake",
            "Chain of custody",
            "Forensic timeline",
            "Artifact provenance",
            "Quality gates",
            "Executive reporting",
            "Technical reporting",
            "Safe synthetic evidence"
        ],
    }


@app.get("/api/cases")
def cases():
    return {
        "cases": [
            {
                "case_id": "CASE-0001",
                "name": "Cloud Identity Investigation",
                "status": "demo-ready",
                "risk": "medium"
            },
            {
                "case_id": "CASE-0002",
                "name": "Endpoint Activity Review",
                "status": "planned",
                "risk": "low"
            },
            {
                "case_id": "CASE-0003",
                "name": "Phishing Email Investigation",
                "status": "planned",
                "risk": "medium"
            }
        ]
    }


@app.get("/api/timeline")
def timeline():
    return {
        "timeline": [
            {
                "time_utc": "2026-06-04T13:15:00Z",
                "event": "Evidence source identified",
                "artifact": "identity-log-export",
                "confidence": "high"
            },
            {
                "time_utc": "2026-06-04T13:22:00Z",
                "event": "Hash manifest generated",
                "artifact": "sha256-md5-record",
                "confidence": "high"
            },
            {
                "time_utc": "2026-06-04T13:31:00Z",
                "event": "Forensic timeline created",
                "artifact": "timeline-export",
                "confidence": "medium"
            }
        ]
    }
