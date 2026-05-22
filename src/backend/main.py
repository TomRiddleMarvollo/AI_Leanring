from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Import local modules
from database import get_db, NewsItem, LearningModule, Project, Conversation, Message, Agent

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

from typing import Optional

class PracticeRequest(BaseModel):
    prompt: str
    provider: Optional[str] = None
    model_name: Optional[str] = None
    system_prompt: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Learning Web Hub API"}

@app.get("/api/news")
def get_news(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    news = db.query(NewsItem).order_by(NewsItem.rating.desc(), NewsItem.published_at.desc()).offset(skip).limit(limit).all()
    return news

@app.get("/api/learn")
def get_learning_modules(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    modules = db.query(LearningModule).order_by(LearningModule.created_at.desc()).offset(skip).limit(limit).all()
    return modules

from fastapi import BackgroundTasks
from agent import run_all_background_tasks, practice_chat, get_ollama_models

@app.get("/api/models")
def get_models():
    try:
        ollama_models = get_ollama_models()
    except Exception as e:
        print(f"Error fetching Ollama models: {e}")
        ollama_models = []
    
    models = []
    # Always include Gemini 2.5 Flash as the primary Cloud model
    models.append({
        "id": "gemini",
        "name": "Google Gemini 2.5 Flash",
        "provider": "gemini",
        "model_name": "gemini-2.5-flash",
        "description": "Cloud API - Siêu tốc & Siêu trí tuệ"
    })
    
    # Add all local Ollama models found dynamically on the system
    for model in ollama_models:
        models.append({
            "id": f"ollama/{model}",
            "name": f"Local: {model}",
            "provider": "ollama",
            "model_name": model,
            "description": "Local GPU - Riêng tư & Không giới hạn"
        })
        
    # Fallback placeholder if no local models are detected
    if not ollama_models:
        models.append({
            "id": "ollama/llama3",
            "name": "Local: llama3 (Chưa tải)",
            "provider": "ollama",
            "model_name": "llama3",
            "description": "Chạy 'ollama pull llama3' để tải về máy"
        })
        
    return models

@app.post("/api/practice")
def practice_with_ai(req: PracticeRequest):
    response_text = practice_chat(req.prompt, req.provider, req.model_name, req.system_prompt)
    return {"response": response_text}

@app.post("/api/agent/run", status_code=202)
def run_agent(background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(run_all_background_tasks)
        return {"status": "success", "message": "Background scanning of 50 sources has started."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ==========================================
# POSTGRESQL CRUD ENDPOINTS FOR PRACTICE WORKSPACE
# ==========================================
from typing import List

class ProjectSchema(BaseModel):
    id: str
    name: str

class MessageSchema(BaseModel):
    role: str
    content: str
    modelName: Optional[str] = None

class ConversationSchema(BaseModel):
    id: str
    projectId: str
    name: str
    agentId: Optional[str] = None
    messages: List[MessageSchema] = []

class AgentSchema(BaseModel):
    id: str
    name: str
    system_prompt: str
    model_id: str
    color: Optional[str] = None
    icon: Optional[str] = None

@app.get("/api/projects", response_model=List[ProjectSchema])
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    # Seed default project if empty
    if not projects:
        default_proj = Project(id="proj-1", name="Dự án AI Learning Hub 🚀")
        db.add(default_proj)
        db.commit()
        db.refresh(default_proj)
        return [default_proj]
    return projects

@app.post("/api/projects", response_model=ProjectSchema)
def create_project(proj: ProjectSchema, db: Session = Depends(get_db)):
    db_project = db.query(Project).filter(Project.id == proj.id).first()
    if db_project:
        db_project.name = proj.name
    else:
        db_project = Project(id=proj.id, name=proj.name)
        db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.delete("/api/projects/{proj_id}")
def delete_project(proj_id: str, db: Session = Depends(get_db)):
    db.query(Project).filter(Project.id == proj_id).delete()
    conversations = db.query(Conversation).filter(Conversation.project_id == proj_id).all()
    for conv in conversations:
        db.query(Message).filter(Message.conversation_id == conv.id).delete()
    db.query(Conversation).filter(Conversation.project_id == proj_id).delete()
    db.commit()
    return {"status": "success"}

@app.get("/api/agents", response_model=List[AgentSchema])
def get_agents(db: Session = Depends(get_db)):
    agents = db.query(Agent).all()
    if not agents:
        default_agent = Agent(
            id="agent-default-1",
            name="Chuyên gia Prompt 💡",
            system_prompt="Bạn là một chuyên gia về Prompt Engineering. Hãy giúp người dùng thiết kế, tối ưu và thử nghiệm các kỹ thuật prompt như Few-Shot, Chain-of-Thought, và Role-play.",
            model_id="gemini",
            color="#2563eb",
            icon="Sparkles"
        )
        db.add(default_agent)
        db.commit()
        db.refresh(default_agent)
        return [default_agent]
    return agents

@app.post("/api/agents", response_model=AgentSchema)
def create_agent(agent: AgentSchema, db: Session = Depends(get_db)):
    db_agent = db.query(Agent).filter(Agent.id == agent.id).first()
    if db_agent:
        db_agent.name = agent.name
        db_agent.system_prompt = agent.system_prompt
        db_agent.model_id = agent.model_id
        db_agent.color = agent.color
        db_agent.icon = agent.icon
    else:
        db_agent = Agent(
            id=agent.id,
            name=agent.name,
            system_prompt=agent.system_prompt,
            model_id=agent.model_id,
            color=agent.color,
            icon=agent.icon
        )
        db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

@app.delete("/api/agents/{agent_id}")
def delete_agent(agent_id: str, db: Session = Depends(get_db)):
    db.query(Agent).filter(Agent.id == agent_id).delete()
    db.query(Conversation).filter(Conversation.agent_id == agent_id).update({Conversation.agent_id: None})
    db.commit()
    return {"status": "success"}

@app.get("/api/conversations", response_model=List[ConversationSchema])
def get_conversations(db: Session = Depends(get_db)):
    conversations = db.query(Conversation).all()
    
    # Seed default conversation if empty
    if not conversations:
        proj_exists = db.query(Project).filter(Project.id == "proj-1").first()
        if not proj_exists:
            default_proj = Project(id="proj-1", name="Dự án AI Learning Hub 🚀")
            db.add(default_proj)
            db.commit()
            
        default_conv = Conversation(id="chat-1", project_id="proj-1", name="Hội thoại Prompt Engineering 💡", agent_id=None)
        db.add(default_conv)
        db.commit()
        
        default_msg = Message(
            conversation_id="chat-1",
            role="ai",
            content='Chào bạn! Mình là AI Assistant trong Không gian Thực hành.\n\nHãy thử chọn mô hình bạn thích ở góc dưới (Gemini 2.5 Flash Cloud hoặc bất kỳ mô hình Local LLM nào đang chạy Ollama trên máy tính của bạn).\n\nSau đó, bạn có thể kiểm thử các kỹ thuật Prompt Engineering như Zero-Shot, Few-Shot, Chain-of-Thought trực tiếp tại đây! Lịch sử trò chuyện và các dự án của bạn sẽ tự động được lưu lại.',
            model_name="Hệ thống AI"
        )
        db.add(default_msg)
        db.commit()
        conversations = [default_conv]

    result = []
    for conv in conversations:
        messages = db.query(Message).filter(Message.conversation_id == conv.id).order_by(Message.id.asc()).all()
        msg_list = []
        for m in messages:
            msg_list.append(MessageSchema(
                role=m.role,
                content=m.content,
                modelName=m.model_name
            ))
        result.append(ConversationSchema(
            id=conv.id,
            projectId=conv.project_id,
            name=conv.name,
            agentId=conv.agent_id,
            messages=msg_list
        ))
    return result

@app.post("/api/conversations", response_model=ConversationSchema)
def create_conversation(conv: ConversationSchema, db: Session = Depends(get_db)):
    db_conv = db.query(Conversation).filter(Conversation.id == conv.id).first()
    if db_conv:
        db_conv.name = conv.name
        db_conv.project_id = conv.projectId
        db_conv.agent_id = conv.agentId
    else:
        db_conv = Conversation(id=conv.id, project_id=conv.projectId, name=conv.name, agent_id=conv.agentId)
        db.add(db_conv)
    db.commit()

    db.query(Message).filter(Message.conversation_id == conv.id).delete()
    for msg in conv.messages:
        db_msg = Message(
            conversation_id=conv.id,
            role=msg.role,
            content=msg.content,
            model_name=msg.modelName
        )
        db.add(db_msg)
    db.commit()
    return conv

@app.delete("/api/conversations/{chat_id}")
def delete_conversation(chat_id: str, db: Session = Depends(get_db)):
    db.query(Conversation).filter(Conversation.id == chat_id).delete()
    db.query(Message).filter(Message.conversation_id == chat_id).delete()
    db.commit()
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

