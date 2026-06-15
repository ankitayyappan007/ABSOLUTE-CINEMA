from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.script_routes import (
    router as script_router
)

from app.api.consultation_routes import (
    router as consultation_router
)

from app.api.story_profile_routes import (
    router as story_profile_router
)

app = FastAPI(
    title="ABSOLUTE CINEMA",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://absolute-cinema-mocha.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    script_router
)

app.include_router(
    consultation_router
)

app.include_router(
    story_profile_router
)

@app.get("/")
def home():

    return {
        "message":
        "ABSOLUTE CINEMA API RUNNING"
    }