from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Import local modules
from database import get_db, NewsItem, LearningModule

load_dotenv()

app = FastAPI(title="AI Learning Web Hub API")

# Setup CORS to allow requests from the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development, allow all. In production, specify the exact frontend URL.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PracticeRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Learning Web Hub API"}

@app.get("/api/news")
def get_news(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    news = db.query(NewsItem).order_by(NewsItem.published_at.desc()).offset(skip).limit(limit).all()
    return news

@app.get("/api/learn")
def get_learning_modules(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    modules = db.query(LearningModule).order_by(LearningModule.created_at.desc()).offset(skip).limit(limit).all()
    return modules

from agent import summarize_news, fetch_best_practices, practice_chat

@app.post("/api/practice")
def practice_with_ai(req: PracticeRequest):
    response_text = practice_chat(req.prompt)
    return {"response": response_text}

@app.post("/api/agent/run")
def run_agent():
    try:
        # Note: In a real app, this should be run in a background task (e.g. celery or FastAPI BackgroundTasks)
        # to avoid blocking the API response. For this demo, we'll run it synchronously.
        summarize_news()
        fetch_best_practices()
        return {"status": "success", "message": "Agent successfully fetched new data."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
