import React, { useState, useEffect } from 'react';
import NewsFeed from './components/NewsFeed';
import LearningHub from './components/LearningHub';
import PracticeArea from './components/PracticeArea';
import axios from 'axios';
import { Sparkles, RefreshCw } from 'lucide-react';
import './index.css';

// Using relative path. Nginx will proxy /api to the backend container.
// In dev mode without Nginx, we would need to configure vite.config.js server.proxy

function App() {
  const [activeTab, setActiveTab] = useState('learning');
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [refreshKey, setRefreshKey] = useState(0);

  // ==========================================
  // LIFTED STATES FOR PRACTICE AREA (LOADED FROM POSTGRESQL BACKEND)
  // ==========================================
  const [projects, setProjects] = useState([]);
  const [activeProjectId, setActiveProjectId] = useState(null);
  const [conversations, setConversations] = useState([]);
  const [activeConversationId, setActiveConversationId] = useState(null);

  const [selectedModelId, setSelectedModelId] = useState(() => {
    return localStorage.getItem('ai_learning_selected_model') || 'gemini';
  });

  // Load projects & conversations from PostgreSQL DB and handle localStorage migration if needed
  useEffect(() => {
    const loadWorkspaceData = async () => {
      try {
        const resProjects = await axios.get('/api/projects');
        const resConversations = await axios.get('/api/conversations');
        
        let loadedProjects = resProjects.data;
        let loadedConversations = resConversations.data;

        // Smart Migration: If PostgreSQL is empty or only contains the seeded defaults,
        // and localStorage contains old projects or chats, migrate them to PostgreSQL.
        const localProjectsStr = localStorage.getItem('ai_learning_projects');
        const localConversationsStr = localStorage.getItem('ai_learning_conversations');

        if (localProjectsStr && localConversationsStr) {
          try {
            const localProjects = JSON.parse(localProjectsStr);
            const localConversations = JSON.parse(localConversationsStr);

            const hasLocalData = localProjects.length > 1 || (localProjects.length === 1 && localProjects[0].id !== 'proj-1');
            const dbIsEmpty = loadedProjects.length === 0 || (loadedProjects.length === 1 && loadedProjects[0].id === 'proj-1');

            if (hasLocalData && dbIsEmpty) {
              console.log("Migrating local workspace data to PostgreSQL...");
              
              // Post projects
              for (const proj of localProjects) {
                await axios.post('/api/projects', proj);
              }
              
              // Post conversations
              for (const conv of localConversations) {
                const formatted = {
                  id: conv.id,
                  projectId: conv.projectId,
                  name: conv.name,
                  messages: conv.messages.map(m => ({
                    role: m.role,
                    content: m.content,
                    modelName: m.modelName || (m.role === 'ai' ? 'Google Gemini 2.5 Flash' : null)
                  }))
                };
                await axios.post('/api/conversations', formatted);
              }

              // Clean up localStorage to prevent redundant migrations
              localStorage.removeItem('ai_learning_projects');
              localStorage.removeItem('ai_learning_conversations');

              // Refetch from database
              const refetchProjects = await axios.get('/api/projects');
              const refetchConversations = await axios.get('/api/conversations');
              loadedProjects = refetchProjects.data;
              loadedConversations = refetchConversations.data;
            }
          } catch (migrateErr) {
            console.error("Failed to migrate local storage data to DB:", migrateErr);
          }
        }

        setProjects(loadedProjects);
        setConversations(loadedConversations);

        // Resolve active project ID
        const savedProjId = localStorage.getItem('ai_learning_active_project_id');
        let currentProjId = loadedProjects.length > 0 ? loadedProjects[0].id : null;
        if (savedProjId && loadedProjects.some(p => p.id === savedProjId)) {
          currentProjId = savedProjId;
        }
        setActiveProjectId(currentProjId);

        // Resolve active conversation ID
        const savedChatId = localStorage.getItem('ai_learning_active_conversation_id');
        const projChats = loadedConversations.filter(c => c.projectId === currentProjId);
        let currentChatId = projChats.length > 0 ? projChats[0].id : null;
        if (savedChatId && projChats.some(c => c.id === savedChatId)) {
          currentChatId = savedChatId;
        }
        setActiveConversationId(currentChatId);

      } catch (err) {
        console.error("Failed to load practice workspace data from PostgreSQL API:", err);
      }
    };

    loadWorkspaceData();
  }, []);

  // Save current selections to localStorage for persistent focus upon page refresh
  useEffect(() => {
    if (activeProjectId) {
      localStorage.setItem('ai_learning_active_project_id', activeProjectId);
    }
  }, [activeProjectId]);

  useEffect(() => {
    if (activeConversationId) {
      localStorage.setItem('ai_learning_active_conversation_id', activeConversationId);
    } else {
      localStorage.removeItem('ai_learning_active_conversation_id');
    }
  }, [activeConversationId]);

  useEffect(() => {
    if (selectedModelId) {
      localStorage.setItem('ai_learning_selected_model', selectedModelId);
    }
  }, [selectedModelId]);

  const handleRefresh = async () => {
    setIsRefreshing(true);
    try {
      await axios.post('/api/agent/run');
      alert('Hệ thống đã bắt đầu quét ngầm toàn bộ 50 trang. Quá trình này sẽ mất 10-20 phút. Vui lòng quay lại và làm mới trang sau để xem tin mới!');
      // Refresh the key immediately just in case we have existing new items
      setRefreshKey(prev => prev + 1);
    } catch (error) {
      console.error("Error triggering agent", error);
      alert("Failed to trigger agent.");
    } finally {
      // Turn off spinning immediately because it's running in background
      setIsRefreshing(false);
    }
  };

  return (
    <div className={`app-container ${activeTab === 'practice' ? 'practice-mode' : ''}`}>
      <header>
        <div className="logo" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Sparkles color="var(--accent-color)" /> <span>AI</span> Learning Hub
        </div>
        <nav>
          <button 
            className={`nav-btn ${activeTab === 'news' ? 'active' : ''}`}
            onClick={() => setActiveTab('news')}
          >
            Tin tức AI
          </button>
          <button 
            className={`nav-btn ${activeTab === 'learning' ? 'active' : ''}`}
            onClick={() => setActiveTab('learning')}
          >
            Bài học
          </button>
          <button 
            className={`nav-btn ${activeTab === 'practice' ? 'active' : ''}`}
            onClick={() => setActiveTab('practice')}
          >
            Thực hành
          </button>
          <button 
            className="btn-primary flex items-center gap-2 ml-4"
            onClick={handleRefresh}
            disabled={isRefreshing}
          >
            <RefreshCw className={isRefreshing ? 'animate-spin' : ''} size={18} />
            {isRefreshing ? 'Đang cập nhật...' : 'Cập nhật DL'}
          </button>
        </nav>
      </header>

      <main>
        {activeTab === 'news' && <NewsFeed key={`news-${refreshKey}`} />}
        {activeTab === 'learning' && <LearningHub key={`learn-${refreshKey}`} />}
        {activeTab === 'practice' && (
          <PracticeArea 
            projects={projects}
            setProjects={setProjects}
            activeProjectId={activeProjectId}
            setActiveProjectId={setActiveProjectId}
            conversations={conversations}
            setConversations={setConversations}
            activeConversationId={activeConversationId}
            setActiveConversationId={setActiveConversationId}
            selectedModelId={selectedModelId}
            setSelectedModelId={setSelectedModelId}
          />
        )}
      </main>
    </div>
  );
}

export default App;

