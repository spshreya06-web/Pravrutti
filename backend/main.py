import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/api/health")
def health():
    return {
        "message": "Backend is running",
        "gemini_key_loaded": bool(os.getenv("GEMINI_API_KEY")),
        "groq_key_loaded": bool(os.getenv("GROQ_API_KEY")),
    }