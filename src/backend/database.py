from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Use DATABASE_URL from env if available (PostgreSQL in Docker), else fallback to SQLite
fallback_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'ai_hub.db'))
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    f"sqlite:///{fallback_path}"
)

# Connect args needed for SQLite, not for Postgres
connect_args = {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args=connect_args
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class NewsItem(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    summary = Column(Text)
    url = Column(String)
    rating = Column(Integer, default=0)
    published_at = Column(DateTime, default=datetime.utcnow)

class LearningModule(Base):
    __tablename__ = "learning_modules"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    category = Column(String) # e.g., "Prompt Engineering", "RAG"
    created_at = Column(DateTime, default=datetime.utcnow)

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Agent(Base):
    __tablename__ = "agents"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    system_prompt = Column(Text)
    model_id = Column(String)
    color = Column(String, nullable=True)
    icon = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(String, primary_key=True, index=True)
    project_id = Column(String, index=True)
    name = Column(String, index=True)
    agent_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    conversation_id = Column(String, index=True)
    role = Column(String) # "user" or "ai"
    content = Column(Text)
    model_name = Column(String, nullable=True) # The name of the AI model that answered
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Try to alter conversations table if needed (for migrating to custom agent column)
try:
    with engine.begin() as conn:
        conn.execute(text("ALTER TABLE conversations ADD COLUMN agent_id VARCHAR"))
        print("Successfully added agent_id column to conversations table.")
except Exception as e:
    # Column may already exist
    print(f"Migration check: {e}")
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
