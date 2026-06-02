import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import { marked } from 'marked';
import { 
  Send, 
  Sparkles, 
  Plus, 
  Trash2, 
  Folder, 
  MessageSquare, 
  Edit3, 
  ChevronDown, 
  Brain, 
  Cpu, 
  Check,
  RefreshCw,
  ArrowRight,
  ChevronLeft,
  ChevronRight,
  Menu,
  X,
  Bot,
  Terminal,
  Code,
  Paperclip
} from 'lucide-react';

const iconMap = {
  Sparkles: Sparkles,
  Brain: Brain,
  Cpu: Cpu,
  MessageSquare: MessageSquare,
  Terminal: Terminal,
  Code: Code,
  Bot: Bot
};

// Helper to render markdown safely
const renderMarkdown = (text) => {
  try {
    // Configure marked for simple line breaks and safe rendering
    const rawHtml = marked.parse(text || '', { gfm: true, breaks: true });
    return { __html: rawHtml };
  } catch (e) {
    console.error("Markdown parsing error:", e);
    return { __html: text || '' };
  }
};

function PracticeArea({
  projects,
  setProjects,
  activeProjectId,
  setActiveProjectId,
  conversations,
  setConversations,
  activeConversationId,
  setActiveConversationId,
  selectedModelId,
  setSelectedModelId
}) {
  // 2. Models State (Fetched dynamically from backend)
  const [models, setModels] = useState([
    {
      id: 'gemini',
      name: 'Google Gemini 2.5 Flash',
      provider: 'gemini',
      model_name: 'gemini-2.5-flash',
      description: 'Cloud API - Siêu tốc & Siêu trí tuệ'
    }
  ]);
  const [dropdownOpen, setDropdownOpen] = useState(false);

  // 3. UI states
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [fetchingModels, setFetchingModels] = useState(false);
  const [editingId, setEditingId] = useState(null);
  const [editingValue, setEditingValue] = useState('');
  const [editType, setEditType] = useState(''); // 'project' or 'conversation'

  // 4. AI Agent Custom States
  const [agents, setAgents] = useState([]);
  const [agentModalOpen, setAgentModalOpen] = useState(false);
  const [editingAgent, setEditingAgent] = useState(null);
  const [agentName, setAgentName] = useState('');
  const [agentSystemPrompt, setAgentSystemPrompt] = useState('');
  const [agentModelId, setAgentModelId] = useState('gemini');
  const [agentColor, setAgentColor] = useState('blue');
  const [agentIcon, setAgentIcon] = useState('Bot');

  // 5. Sidebar Collapse States
  const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(() => {
    return localStorage.getItem('ai_learning_sidebar_collapsed') === 'true';
  });

  // Sync sidebar state to localStorage
  useEffect(() => {
    localStorage.setItem('ai_learning_sidebar_collapsed', isSidebarCollapsed);
  }, [isSidebarCollapsed]);

  // Collapsible sections within sidebar
  const [isProjectsExpanded, setIsProjectsExpanded] = useState(() => {
    return localStorage.getItem('ai_learning_projects_expanded') !== 'false';
  });
  const [isAgentsExpanded, setIsAgentsExpanded] = useState(() => {
    return localStorage.getItem('ai_learning_agents_expanded') !== 'false';
  });
  const [isConversationsExpanded, setIsConversationsExpanded] = useState(() => {
    return localStorage.getItem('ai_learning_conversations_expanded') !== 'false';
  });

  // Sync expanded section states to localStorage
  useEffect(() => {
    localStorage.setItem('ai_learning_projects_expanded', isProjectsExpanded);
  }, [isProjectsExpanded]);

  useEffect(() => {
    localStorage.setItem('ai_learning_agents_expanded', isAgentsExpanded);
  }, [isAgentsExpanded]);

  useEffect(() => {
    localStorage.setItem('ai_learning_conversations_expanded', isConversationsExpanded);
  }, [isConversationsExpanded]);

  // Refs
  const chatHistoryRef = useRef(null);
  const textareaRef = useRef(null);
  const fileInputRef = useRef(null);

  // File attachment state
  const [attachedFile, setAttachedFile] = useState(null);

  const handleAttachmentClick = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    if (file.size > 10 * 1024 * 1024) {
      alert("Dung lượng tệp tin quá lớn! Vui lòng chọn tệp dưới 10MB.");
      e.target.value = '';
      return;
    }

    const reader = new FileReader();
    reader.onload = (event) => {
      const base64Data = event.target.result.split(',')[1];
      setAttachedFile({
        name: file.name,
        size: file.size,
        type: file.type || 'application/octet-stream',
        data: base64Data
      });
    };
    reader.onerror = (err) => {
      console.error("FileReader error:", err);
      alert("Lỗi khi đọc tệp tin!");
    };
    reader.readAsDataURL(file);
    e.target.value = '';
  };

  const handleRemoveFile = () => {
    setAttachedFile(null);
  };


  // Fetch available models & agents on mount
  useEffect(() => {
    fetchAvailableModels();
    fetchAgents();
  }, []);

  const selectProject = (projId) => {
    setActiveProjectId(projId);
    const projChats = conversations.filter(c => c.projectId === projId);
    if (projChats.length > 0) {
      setActiveConversationId(projChats[0].id);
    } else {
      setActiveConversationId(null);
    }
  };

  const selectConversation = (chatId) => {
    setActiveConversationId(chatId);
  };

  // Fetch available models from FastAPI endpoint
  const fetchAvailableModels = async () => {
    setFetchingModels(true);
    try {
      const response = await axios.get('/api/models');
      if (response.data && response.data.length > 0) {
        setModels(response.data);
        
        // If current selected ID is no longer in the list and it's not 'gemini', reset to first available
        const currentValid = response.data.some(m => m.id === selectedModelId);
        if (!currentValid && selectedModelId !== 'gemini') {
          setSelectedModelId(response.data[0].id);
        }
      }
    } catch (error) {
      console.error("Error fetching models:", error);
    } finally {
      setFetchingModels(false);
    }
  };

  // Fetch all custom AI Agents from backend
  const fetchAgents = async () => {
    try {
      const response = await axios.get('/api/agents');
      setAgents(response.data);
    } catch (err) {
      console.error("Failed to fetch agents:", err);
    }
  };

  // Toggle selecting an Agent for the active conversation
  const selectAgentForConversation = async (agentId) => {
    if (!activeConversation) return;
    
    // Toggle agent selection
    const newAgentId = activeConversation.agentId === agentId ? null : agentId;
    const updatedConv = { ...activeConversation, agentId: newAgentId };

    try {
      await axios.post('/api/conversations', {
        id: updatedConv.id,
        projectId: updatedConv.projectId,
        name: updatedConv.name,
        agentId: updatedConv.agentId,
        messages: updatedConv.messages.map(m => ({
          role: m.role,
          content: m.content,
          modelName: m.modelName || null
        }))
      });

      const updated = conversations.map(c => c.id === activeConversationId ? updatedConv : c);
      setConversations(updated);
    } catch (err) {
      console.error("Failed to link agent to conversation:", err);
    }
  };

  // Open modal to create/edit Agent
  const handleOpenAgentModal = (agent = null) => {
    if (agent) {
      setEditingAgent(agent);
      setAgentName(agent.name);
      setAgentSystemPrompt(agent.system_prompt);
      setAgentModelId(agent.model_id);
      setAgentColor(agent.color || 'blue');
      setAgentIcon(agent.icon || 'Bot');
    } else {
      setEditingAgent(null);
      setAgentName('');
      setAgentSystemPrompt('');
      setAgentModelId(selectedModelId || 'gemini');
      setAgentColor('blue');
      setAgentIcon('Bot');
    }
    setAgentModalOpen(true);
  };

  // Save new/edited Agent to backend
  const handleSaveAgent = async (e) => {
    if (e) e.preventDefault();
    if (!agentName.trim() || !agentSystemPrompt.trim()) {
      alert("Vui lòng điền đầy đủ Tên Agent và Chỉ dẫn hệ thống!");
      return;
    }

    const agentId = editingAgent ? editingAgent.id : `agent-${Date.now()}`;
    const newAgent = {
      id: agentId,
      name: agentName.trim(),
      system_prompt: agentSystemPrompt.trim(),
      model_id: agentModelId,
      color: agentColor,
      icon: agentIcon
    };

    try {
      await axios.post('/api/agents', newAgent);
      await fetchAgents();
      setAgentModalOpen(false);
    } catch (err) {
      console.error("Failed to save agent:", err);
      alert("Lỗi khi lưu Agent. Vui lòng kiểm tra lại kết nối!");
    }
  };

  // Delete Agent from backend
  const handleDeleteAgent = async (agentId) => {
    if (!confirm("Bạn có chắc chắn muốn xóa AI Agent này?")) {
      return;
    }

    try {
      await axios.delete(`/api/agents/${agentId}`);
      await fetchAgents();
      
      // Update local state conversations using this agent
      const updatedConversations = conversations.map(c => {
        if (c.agentId === agentId) {
          return { ...c, agentId: null };
        }
        return c;
      });
      setConversations(updatedConversations);
    } catch (err) {
      console.error("Failed to delete agent:", err);
      alert("Lỗi khi xóa Agent!");
    }
  };

  // Scroll to bottom on new messages
  useEffect(() => {
    if (chatHistoryRef.current) {
      chatHistoryRef.current.scrollTop = chatHistoryRef.current.scrollHeight;
    }
  }, [conversations, activeConversationId, loading]);

  // Handle textarea autosizing
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    }
  }, [input]);

  // Save state helpers (simply update state, useEffect handles saving)
  const saveProjectsToStorage = (updatedProjects) => {
    setProjects(updatedProjects);
  };

  const saveConversationsToStorage = (updatedConversations) => {
    setConversations(updatedConversations);
  };

  const selectModel = (modelId) => {
    setSelectedModelId(modelId);
    setDropdownOpen(false);
  };

  // ==========================================
  // PROJECT ACTIONS
  // ==========================================
  // ==========================================
  // PROJECT ACTIONS
  // ==========================================
  const handleAddProject = async () => {
    const newProjId = `proj-${Date.now()}`;
    const newProjName = `Dự án Mới #${projects.length + 1}`;
    const newProj = { id: newProjId, name: newProjName };

    try {
      // 1. Persist new project to PostgreSQL
      await axios.post('/api/projects', newProj);
      setProjects([...projects, newProj]);
      setActiveProjectId(newProjId);

      // 2. Persist default conversation for this project
      const newChatId = `chat-${Date.now()}`;
      const newConv = {
        id: newChatId,
        projectId: newProjId,
        name: 'Cuộc trò chuyện mới 💬',
        messages: [
          { role: 'ai', content: 'Dự án mới đã được khởi tạo! Bạn muốn thực hành điều gì hôm nay?', modelName: 'Hệ thống AI' }
        ]
      };

      await axios.post('/api/conversations', {
        id: newConv.id,
        projectId: newConv.projectId,
        name: newConv.name,
        messages: newConv.messages.map(m => ({
          role: m.role,
          content: m.content,
          modelName: m.modelName
        }))
      });

      setConversations([...conversations, newConv]);
      setActiveConversationId(newChatId);
    } catch (err) {
      console.error("Failed to add project to PostgreSQL:", err);
    }
  };

  const handleDeleteProject = async (projId, e) => {
    e.stopPropagation();
    if (projects.length <= 1) {
      alert("Bạn phải có ít nhất một dự án hoạt động!");
      return;
    }
    if (!confirm("Bạn có chắc chắn muốn xóa dự án này cùng toàn bộ các cuộc trò chuyện bên trong?")) {
      return;
    }

    try {
      // 1. Delete from PostgreSQL
      await axios.delete(`/api/projects/${projId}`);

      const updatedProjects = projects.filter(p => p.id !== projId);
      const updatedConversations = conversations.filter(c => c.projectId !== projId);
      
      setProjects(updatedProjects);
      setConversations(updatedConversations);

      // If deleted active project, select another one
      if (activeProjectId === projId) {
        const fallbackProj = updatedProjects[0];
        setActiveProjectId(fallbackProj.id);
        
        const fallbackChats = updatedConversations.filter(c => c.projectId === fallbackProj.id);
        if (fallbackChats.length > 0) {
          setActiveConversationId(fallbackChats[0].id);
        } else {
          setActiveConversationId(null);
        }
      }
    } catch (err) {
      console.error("Failed to delete project from PostgreSQL:", err);
    }
  };

  // ==========================================
  // CONVERSATION ACTIONS
  // ==========================================
  const handleAddConversation = async () => {
    if (!activeProjectId) return;
    const newChatId = `chat-${Date.now()}`;
    const activeProjectChats = conversations.filter(c => c.projectId === activeProjectId);
    const newChatName = `Cuộc hội thoại #${activeProjectChats.length + 1}`;
    
    const newConv = {
      id: newChatId,
      projectId: activeProjectId,
      name: newChatName,
      messages: [
        { role: 'ai', content: 'Cuộc trò chuyện mới đã bắt đầu. Hãy nhập prompt của bạn!', modelName: 'Hệ thống AI' }
      ]
    };

    try {
      // 1. Persist new conversation to PostgreSQL
      await axios.post('/api/conversations', {
        id: newConv.id,
        projectId: newConv.projectId,
        name: newConv.name,
        messages: newConv.messages.map(m => ({
          role: m.role,
          content: m.content,
          modelName: m.modelName
        }))
      });

      setConversations([...conversations, newConv]);
      setActiveConversationId(newChatId);
    } catch (err) {
      console.error("Failed to add conversation to PostgreSQL:", err);
    }
  };

  const handleDeleteConversation = async (chatId, e) => {
    e.stopPropagation();
    const projectChats = conversations.filter(c => c.projectId === activeProjectId);
    if (projectChats.length <= 1) {
      alert("Bạn phải giữ lại ít nhất một cuộc hội thoại trong dự án này!");
      return;
    }
    if (!confirm("Xóa cuộc trò chuyện này?")) {
      return;
    }

    try {
      // 1. Delete from PostgreSQL
      await axios.delete(`/api/conversations/${chatId}`);

      const updatedConversations = conversations.filter(c => c.id !== chatId);
      setConversations(updatedConversations);

      if (activeConversationId === chatId) {
        const remainingProjectChats = updatedConversations.filter(c => c.projectId === activeProjectId);
        setActiveConversationId(remainingProjectChats[0].id);
      }
    } catch (err) {
      console.error("Failed to delete conversation from PostgreSQL:", err);
    }
  };

  // ==========================================
  // RENAME ITEM ACTIONS
  // ==========================================
  const startEditing = (id, currentValue, type, e) => {
    e.stopPropagation();
    setEditingId(id);
    setEditingValue(currentValue);
    setEditType(type);
  };

  const saveRename = async () => {
    if (!editingValue.trim()) return;

    try {
      if (editType === 'project') {
        const targetProj = projects.find(p => p.id === editingId);
        if (targetProj) {
          const updatedProj = { ...targetProj, name: editingValue };
          await axios.post('/api/projects', updatedProj);
          
          const updated = projects.map(p => p.id === editingId ? updatedProj : p);
          setProjects(updated);
        }
      } else if (editType === 'conversation') {
        const targetConv = conversations.find(c => c.id === editingId);
        if (targetConv) {
          const updatedConv = { ...targetConv, name: editingValue };
          await axios.post('/api/conversations', {
            id: updatedConv.id,
            projectId: updatedConv.projectId,
            name: updatedConv.name,
            messages: updatedConv.messages.map(m => ({
              role: m.role,
              content: m.content,
              modelName: m.modelName || null
            }))
          });
          
          const updated = conversations.map(c => c.id === editingId ? updatedConv : c);
          setConversations(updated);
        }
      }
    } catch (err) {
      console.error("Failed to rename item in PostgreSQL:", err);
    }

    setEditingId(null);
    setEditingValue('');
    setEditType('');
  };

  // ==========================================
  // CHAT SENDING LOGIC
  // ==========================================
  const activeConversation = conversations.find(c => c.id === activeConversationId);
  const activeMessages = activeConversation ? activeConversation.messages : [];

  const handleSend = async (e) => {
    if (e) e.preventDefault();
    const hasInput = input.trim().length > 0;
    if ((!hasInput && !attachedFile) || loading || !activeConversationId || !activeConversation) return;

    let userMessageContent = input.trim();
    if (!userMessageContent && attachedFile) {
      userMessageContent = "Hãy phân tích tài liệu đính kèm này.";
    }

    let displayMessageContent = userMessageContent;
    if (attachedFile) {
      displayMessageContent += `\n\n📎 *[Đính kèm: ${attachedFile.name}]*`;
    }

    // Keep a local copy of attachedFile to use during API requests
    const fileToSend = attachedFile;

    setInput('');
    setAttachedFile(null);
    setLoading(true);

    // Get active custom agent
    const activeAgent = activeConversation.agentId ? agents.find(a => a.id === activeConversation.agentId) : null;
    // Resolve which base model to call
    const resolvedModel = activeAgent ? (models.find(m => m.id === activeAgent.model_id) || activeModel) : activeModel;

    // 1. Create and append user message
    const userMsg = { role: 'user', content: displayMessageContent };
    const updatedMessagesWithUser = [...activeMessages, userMsg];

    // Update frontend state with User message
    const conversationsWithUser = conversations.map(c => {
      if (c.id === activeConversationId) {
        return { ...c, messages: updatedMessagesWithUser };
      }
      return c;
    });
    setConversations(conversationsWithUser);

    try {
      // Sync User message to PostgreSQL DB
      await axios.post('/api/conversations', {
        id: activeConversation.id,
        projectId: activeConversation.projectId,
        name: activeConversation.name,
        agentId: activeConversation.agentId,
        messages: updatedMessagesWithUser.map(m => ({
          role: m.role,
          content: m.content,
          modelName: m.modelName || null
        }))
      });

      // 2. Post prompt to practice endpoint
      const response = await axios.post('/api/practice', { 
        prompt: userMessageContent,
        provider: resolvedModel.provider,
        model_name: resolvedModel.provider === 'ollama' ? resolvedModel.model_name : null,
        system_prompt: activeAgent ? activeAgent.system_prompt : null,
        file_data: fileToSend ? fileToSend.data : null,
        file_name: fileToSend ? fileToSend.name : null,
        file_type: fileToSend ? fileToSend.type : null
      });

      // 3. Construct AI response with the current answering model name
      const aiMsg = { 
        role: 'ai', 
        content: response.data.response, 
        modelName: activeAgent ? `🤖 ${activeAgent.name} (${resolvedModel.name})` : resolvedModel.name 
      };
      const updatedMessagesWithAI = [...updatedMessagesWithUser, aiMsg];

      // Update frontend state with AI message
      const conversationsWithAI = conversations.map(c => {
        if (c.id === activeConversationId) {
          return { ...c, messages: updatedMessagesWithAI };
        }
        return c;
      });
      setConversations(conversationsWithAI);

      // Sync AI message to PostgreSQL DB
      await axios.post('/api/conversations', {
        id: activeConversation.id,
        projectId: activeConversation.projectId,
        name: activeConversation.name,
        agentId: activeConversation.agentId,
        messages: updatedMessagesWithAI.map(m => ({
          role: m.role,
          content: m.content,
          modelName: m.modelName || null
        }))
      });

    } catch (error) {
      console.error("Error sending message to practice AI:", error);
      
      const errorMsg = { 
        role: 'ai', 
        content: `❌ LỖI HỆ THỐNG: Không thể kết nối với mô hình '${resolvedModel.name}'. Vui lòng kiểm tra lại cấu hình key API hoặc dịch vụ Ollama nội bộ của bạn.`,
        modelName: 'Hệ thống AI'
      };
      const updatedMessagesWithErr = [...updatedMessagesWithUser, errorMsg];

      const conversationsWithErr = conversations.map(c => {
        if (c.id === activeConversationId) {
          return { ...c, messages: updatedMessagesWithErr };
        }
        return c;
      });
      setConversations(conversationsWithErr);

      // Sync error message to PostgreSQL DB
      try {
        await axios.post('/api/conversations', {
          id: activeConversation.id,
          projectId: activeConversation.projectId,
          name: activeConversation.name,
          agentId: activeConversation.agentId,
          messages: updatedMessagesWithErr.map(m => ({
            role: m.role,
            content: m.content,
            modelName: m.modelName || null
          }))
        });
      } catch (dbErr) {
        console.error("Failed to sync error message to DB:", dbErr);
      }
    } finally {
      setLoading(false);
    }
  };

  // Handle keyboard submit
  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handlePromptCardClick = (promptText) => {
    setInput(promptText);
    if (textareaRef.current) {
      textareaRef.current.focus();
    }
  };

  // Active Project & Active Chat objects
  const activeProject = projects.find(p => p.id === activeProjectId);
  const activeChat = conversations.find(c => c.id === activeConversationId);
  const activeModel = models.find(m => m.id === selectedModelId) || models[0];
  const activeAgent = activeChat && activeChat.agentId ? agents.find(a => a.id === activeChat.agentId) : null;

  return (
    <div className="practice-workspace">
      {/* ==========================================
         SIDEBAR: PROJECT & CONVERSATION PANEL
         ========================================== */}
      <aside className={`workspace-sidebar ${isSidebarCollapsed ? 'collapsed' : ''}`}>
        {!isSidebarCollapsed && (
          <>
            {/* Sidebar Header with Collapse button */}
            <div className="sidebar-header" style={{ padding: '1rem 1.2rem 0.5rem 1.2rem', borderBottom: '1px solid var(--card-border)' }}>
              <span style={{ fontSize: '0.8rem', fontWeight: 800, color: 'var(--text-color)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                Không gian làm việc
              </span>
              <button 
                type="button" 
                onClick={() => setIsSidebarCollapsed(true)} 
                className="sidebar-collapse-btn" 
                title="Thu gọn sidebar"
              >
                <ChevronLeft size={16} />
              </button>
            </div>

            {/* Project Section */}
            <div className="sidebar-section">
              <div 
                className="sidebar-title" 
                onClick={() => setIsProjectsExpanded(!isProjectsExpanded)}
                style={{ cursor: 'pointer', display: 'flex', justifyContent: 'space-between', alignItems: 'center', userSelect: 'none' }}
                title="Nhấn để ẩn/hiện danh sách dự án"
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <Folder size={14} style={{ color: 'var(--accent-color)', opacity: 0.85 }} />
                  <span>Dự án thực hành</span>
                  <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: 'normal' }}>({projects.length})</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.3rem' }} onClick={(e) => e.stopPropagation()}>
                  <button 
                    onClick={handleAddProject} 
                    className="sidebar-header-action-btn"
                    title="Thêm Dự án mới"
                  >
                    <Plus size={13} />
                  </button>
                  <button 
                    onClick={() => setIsProjectsExpanded(!isProjectsExpanded)}
                    className="sidebar-header-action-btn"
                    title="Thu gọn/Mở rộng"
                  >
                    {isProjectsExpanded ? <ChevronDown size={13} /> : <ChevronRight size={13} />}
                  </button>
                </div>
              </div>
              
              {isProjectsExpanded && (
                <>
                  
                  <div className="sidebar-list" style={{ marginTop: '0.8rem' }}>
                    {projects.map((proj) => (
                      <div 
                        key={proj.id} 
                        onClick={() => selectProject(proj.id)}
                        className={`sidebar-item ${activeProjectId === proj.id ? 'active' : ''}`}
                      >
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', flex: 1, minWidth: 0 }}>
                          <Folder size={15} style={{ flexShrink: 0 }} />
                          {editingId === proj.id && editType === 'project' ? (
                            <input 
                              type="text" 
                              value={editingValue} 
                              onChange={(e) => setEditingValue(e.target.value)}
                              onBlur={saveRename}
                              onKeyDown={(e) => e.key === 'Enter' && saveRename()}
                              onClick={(e) => e.stopPropagation()}
                              autoFocus
                              style={{ background: 'var(--bg-color)', border: '1px solid var(--accent-color)', color: 'var(--text-color)', fontSize: '0.8rem', width: '100%', padding: '0.1rem 0.3rem', borderRadius: '4px' }}
                            />
                          ) : (
                            <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{proj.name}</span>
                          )}
                        </div>
                        
                        {editingId !== proj.id && (
                          <div className="sidebar-item-actions">
                            <button 
                              onClick={(e) => startEditing(proj.id, proj.name, 'project', e)} 
                              className="sidebar-action-btn edit"
                              title="Đổi tên"
                            >
                              <Edit3 size={12} />
                            </button>
                            <button 
                              onClick={(e) => handleDeleteProject(proj.id, e)} 
                              className="sidebar-action-btn"
                              title="Xóa dự án"
                            >
                              <Trash2 size={12} />
                            </button>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </>
              )}
            </div>

            {/* AI Agents Section */}
            <div className="sidebar-section">
              <div 
                className="sidebar-title" 
                onClick={() => setIsAgentsExpanded(!isAgentsExpanded)}
                style={{ cursor: 'pointer', display: 'flex', justifyContent: 'space-between', alignItems: 'center', userSelect: 'none' }}
                title="Nhấn để ẩn/hiện danh sách AI Agents"
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <Brain size={14} style={{ color: 'var(--accent-color)', opacity: 0.85 }} />
                  <span>AI Agents thực hành</span>
                  <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: 'normal' }}>({agents.length})</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.3rem' }} onClick={(e) => e.stopPropagation()}>
                  <button 
                    onClick={() => handleOpenAgentModal()} 
                    className="sidebar-header-action-btn"
                    title="Tạo AI Agent mới"
                  >
                    <Plus size={13} />
                  </button>
                  <button 
                    onClick={() => setIsAgentsExpanded(!isAgentsExpanded)}
                    className="sidebar-header-action-btn"
                    title="Thu gọn/Mở rộng"
                  >
                    {isAgentsExpanded ? <ChevronDown size={13} /> : <ChevronRight size={13} />}
                  </button>
                </div>
              </div>
              
              {isAgentsExpanded && (
                <>
                  
                  <div className="sidebar-list" style={{ marginTop: '0.8rem' }}>
                    {agents.map((agent) => {
                      const IconComponent = iconMap[agent.icon] || Bot;
                      const isActive = activeChat && activeChat.agentId === agent.id;
                      return (
                        <div 
                          key={agent.id} 
                          onClick={() => selectAgentForConversation(agent.id)}
                          className={`sidebar-item ${isActive ? 'active' : ''}`}
                          style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '0.4rem 0.6rem' }}
                          title="Nhấn để Bật/Tắt Agent cho cuộc trò chuyện này"
                        >
                          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', flex: 1, minWidth: 0 }}>
                            <div className={`agent-avatar color-${agent.color || 'blue'}`}>
                              <IconComponent size={14} />
                            </div>
                            <div style={{ display: 'flex', flexDirection: 'column', minWidth: 0 }}>
                              <span style={{ fontWeight: 600, fontSize: '0.82rem', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                                {agent.name}
                              </span>
                              <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                                {agent.system_prompt}
                              </span>
                            </div>
                          </div>
                          
                          <div className="sidebar-item-actions">
                            <button 
                              onClick={(e) => {
                                e.stopPropagation();
                                handleOpenAgentModal(agent);
                              }} 
                              className="sidebar-action-btn edit"
                              title="Chỉnh sửa"
                            >
                              <Edit3 size={12} />
                            </button>
                            <button 
                              onClick={(e) => {
                                e.stopPropagation();
                                handleDeleteAgent(agent.id);
                              }} 
                              className="sidebar-action-btn"
                              title="Xóa Agent"
                            >
                              <Trash2 size={12} />
                            </button>
                          </div>
                        </div>
                      );
                    })}
                    {agents.length === 0 && (
                      <div style={{ textAlign: 'center', color: 'var(--text-muted)', fontSize: '0.75rem', padding: '1rem 0' }}>
                        Chưa tạo Agent nào. Hãy tạo ngay!
                      </div>
                    )}
                  </div>
                </>
              )}
            </div>

            {/* Conversation Section */}
            <div className="sidebar-section" style={{ display: 'flex', flexDirection: 'column' }}>
              <div 
                className="sidebar-title" 
                onClick={() => setIsConversationsExpanded(!isConversationsExpanded)}
                style={{ cursor: 'pointer', display: 'flex', justifyContent: 'space-between', alignItems: 'center', userSelect: 'none' }}
                title="Nhấn để ẩn/hiện danh sách cuộc trò chuyện"
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <MessageSquare size={14} style={{ color: 'var(--accent-color)', opacity: 0.85 }} />
                  <span>Danh sách cuộc trò chuyện</span>
                  <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: 'normal' }}>
                    ({conversations.filter(c => c.projectId === activeProjectId).length})
                  </span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.3rem' }} onClick={(e) => e.stopPropagation()}>
                  <button 
                    onClick={handleAddConversation} 
                    className="sidebar-header-action-btn"
                    title="Cuộc trò chuyện mới"
                    disabled={!activeProjectId}
                  >
                    <Plus size={13} />
                  </button>
                  <button 
                    onClick={() => setIsConversationsExpanded(!isConversationsExpanded)}
                    className="sidebar-header-action-btn"
                    title="Thu gọn/Mở rộng"
                  >
                    {isConversationsExpanded ? <ChevronDown size={13} /> : <ChevronRight size={13} />}
                  </button>
                </div>
              </div>
              
              {isConversationsExpanded && (
                <>
    
                  <div className="conversations-list" style={{ marginTop: '0.8rem' }}>
                    {conversations
                      .filter(c => c.projectId === activeProjectId)
                      .map((chat) => (
                        <div 
                          key={chat.id} 
                          onClick={() => selectConversation(chat.id)}
                          className={`sidebar-item ${activeConversationId === chat.id ? 'active' : ''}`}
                        >
                          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', flex: 1, minWidth: 0 }}>
                            <MessageSquare size={15} style={{ flexShrink: 0 }} />
                            {editingId === chat.id && editType === 'conversation' ? (
                              <input 
                                type="text" 
                                value={editingValue} 
                                onChange={(e) => setEditingValue(e.target.value)}
                                onBlur={saveRename}
                                onKeyDown={(e) => e.key === 'Enter' && saveRename()}
                                onClick={(e) => e.stopPropagation()}
                                autoFocus
                                style={{ background: 'var(--bg-color)', border: '1px solid var(--accent-color)', color: 'var(--text-color)', fontSize: '0.8rem', width: '100%', padding: '0.1rem 0.3rem', borderRadius: '4px' }}
                              />
                            ) : (
                              <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{chat.name}</span>
                            )}
                          </div>
                          
                          {editingId !== chat.id && (
                            <div className="sidebar-item-actions">
                              <button 
                                onClick={(e) => startEditing(chat.id, chat.name, 'conversation', e)} 
                                className="sidebar-action-btn edit"
                                title="Đổi tên"
                              >
                                <Edit3 size={12} />
                              </button>
                              <button 
                                onClick={(e) => handleDeleteConversation(chat.id, e)} 
                                className="sidebar-action-btn"
                                title="Xóa hội thoại"
                              >
                                <Trash2 size={12} />
                              </button>
                            </div>
                          )}
                        </div>
                      ))}
                    
                    {conversations.filter(c => c.projectId === activeProjectId).length === 0 && (
                      <div style={{ textAlign: 'center', color: 'var(--text-muted)', fontSize: '0.8rem', marginTop: '2rem' }}>
                        Chưa có hội thoại nào trong dự án này.
                      </div>
                    )}
                  </div>
                </>
              )}
            </div>
          </>
        )}
      </aside>

      {/* ==========================================
         MAIN AREA: GEMINI WORKSPACE PANEL
         ========================================== */}
      <section className="workspace-panel">
        
        {/* Panel Header */}
        <header className="panel-header" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center' }}>
            {isSidebarCollapsed && (
              <button 
                type="button"
                onClick={() => setIsSidebarCollapsed(false)} 
                className="panel-expand-btn" 
                title="Mở rộng sidebar"
              >
                <Menu size={16} />
              </button>
            )}
            <div className="panel-path">
              <span style={{ textTransform: 'uppercase', fontSize: '0.75rem', fontWeight: 600, color: 'var(--accent-color)' }}>Không gian thực hành</span>
              <span>/</span>
              <span>{activeProject ? activeProject.name : 'Chưa chọn dự án'}</span>
              <span>/</span>
              <span className="panel-path-active">{activeChat ? activeChat.name : 'Chưa chọn cuộc hội thoại'}</span>
            </div>
          </div>
        </header>

        {/* Chat Area Panel */}
        <div className="workspace-chat-history" ref={chatHistoryRef}>
          {activeMessages.length === 0 ? (
            /* Gemini dynamic greeting when empty */
            <div className="gemini-greeting">
              <h1 className="gemini-greeting-title">
                {activeAgent ? `Chào bạn, tôi là ${activeAgent.name}` : 'Chào bạn,'}
              </h1>
              <div className="gemini-greeting-subtitle">
                {activeAgent 
                  ? `Tôi đã sẵn sàng hỗ trợ bạn theo chỉ dẫn: "${activeAgent.system_prompt}"`
                  : 'Bạn muốn thực hành Prompt Engineering gì hôm nay?'}
              </div>
              
              <div className="gemini-suggested-prompts">
                <div 
                  onClick={() => handlePromptCardClick("Viết một prompt áp dụng kỹ thuật Few-Shot để phân loại cảm xúc bình luận của khách hàng về sản phẩm công nghệ.")} 
                  className="suggested-prompt-card"
                >
                  <p>Áp dụng kỹ thuật <b>Few-Shot Learning</b> để phân loại bình luận sản phẩm.</p>
                  <ArrowRight size={14} className="suggested-prompt-card-icon" />
                </div>
                
                <div 
                  onClick={() => handlePromptCardClick("Hãy hướng dẫn mình cấu trúc một prompt sử dụng Chain-of-Thought (Chuỗi tư duy) để giải bài toán logic phức tạp.")}
                  className="suggested-prompt-card"
                >
                  <p>Cấu trúc prompt bằng <b>Chain-of-Thought</b> giải toán logic.</p>
                  <ArrowRight size={14} className="suggested-prompt-card-icon" />
                </div>
                
                <div 
                  onClick={() => handlePromptCardClick("Hãy đóng vai một chuyên gia bảo mật và phân tích các rủi ro bảo mật tiềm ẩn của đoạn prompt này.")}
                  className="suggested-prompt-card"
                >
                  <p>Yêu cầu AI <b>đóng vai (Role-play)</b> chuyên gia phân tích bảo mật prompt.</p>
                  <ArrowRight size={14} className="suggested-prompt-card-icon" />
                </div>
              </div>
            </div>
          ) : (
            /* Chat bubble rows */
            activeMessages.map((msg, index) => {
              // Find if this message relates to a custom agent in the list
              const msgAgent = activeChat && activeChat.agentId ? agents.find(a => a.id === activeChat.agentId) : null;
              return (
                <div key={index} className={`chat-message-row ${msg.role}`}>
                  {msg.role === 'ai' && (
                    msg.modelName && msg.modelName.includes('🤖') ? (
                      <div className="chat-bubble-avatar custom-agent">
                        <div className={`agent-avatar color-${msgAgent ? (msgAgent.color || 'blue') : 'blue'}`} style={{ width: '32px', height: '32px', fontSize: '0.95rem' }}>
                          {React.createElement(msgAgent ? (iconMap[msgAgent.icon] || Bot) : Bot, { size: 16 })}
                        </div>
                      </div>
                    ) : (
                      <div className="chat-bubble-avatar gemini-ai">
                        <Sparkles size={16} />
                      </div>
                    )
                  )}
                  
                  <div className="chat-message-content">
                    <span className="chat-message-sender-name">
                      {msg.role === 'ai' ? (
                        <>
                          {msg.modelName || 'Hệ thống AI'}
                          <span className={`chat-model-badge ${
                            (msg.modelName || '').includes('🤖') ? 'agent' :
                            (msg.modelName || '').toLowerCase().includes('gemini') ? 'gemini' : 
                            (msg.modelName || '').toLowerCase().includes('ollama') || (msg.modelName || '').toLowerCase().includes('local') ? 'ollama' : 'system'
                          }`}>
                            {(msg.modelName || '').includes('🤖') ? 'Agent' :
                             (msg.modelName || '').toLowerCase().includes('gemini') ? 'Cloud' : 
                             (msg.modelName || '').toLowerCase().includes('ollama') || (msg.modelName || '').toLowerCase().includes('local') ? 'Local' : 'System'}
                          </span>
                        </>
                      ) : 'BẠN'}
                    </span>
                    {msg.role === 'ai' ? (
                      <div 
                        className="chat-bubble ai" 
                        dangerouslySetInnerHTML={renderMarkdown(msg.content)} 
                      />
                    ) : (
                      <div className="chat-bubble user">
                        {msg.content}
                      </div>
                    )}
                  </div>
                  
                  {msg.role === 'user' && (
                    <div className="chat-bubble-avatar">
                      U
                    </div>
                  )}
                </div>
              );
            })
          )}

          {/* AI generating loader */}
          {loading && (
            <div className="chat-message-row ai">
              {activeAgent ? (
                <div className="chat-bubble-avatar custom-agent">
                  <div className={`agent-avatar color-${activeAgent.color || 'blue'}`} style={{ width: '32px', height: '32px', fontSize: '0.95rem' }}>
                    {React.createElement(iconMap[activeAgent.icon] || Bot, { size: 16 })}
                  </div>
                </div>
              ) : (
                <div className="chat-bubble-avatar gemini-ai">
                  <Sparkles size={16} />
                </div>
              )}
              <div className="chat-message-content">
                <span className="chat-message-sender-name">
                  {activeAgent ? `🤖 ${activeAgent.name} (${activeModel.name})` : activeModel.name}
                  <span className={`chat-model-badge ${activeAgent ? 'agent' : activeModel.provider === 'gemini' ? 'gemini' : 'ollama'}`}>
                    {activeAgent ? 'Agent' : activeModel.provider === 'gemini' ? 'Cloud' : 'Local'}
                  </span>
                </span>
                <div className="chat-bubble ai">
                  <div className="gemini-shimmer-container">
                    <div className="gemini-shimmer-line"></div>
                    <div className="gemini-shimmer-line medium"></div>
                    <div className="gemini-shimmer-line short"></div>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Capsule Prompt Input */}
        <div className="workspace-input-container">
          {attachedFile && (
            <div className="workspace-file-preview animate-slide-up">
              <Paperclip size={14} className="workspace-file-icon" />
              <span className="file-name">{attachedFile.name}</span>
              <span className="file-size">({Math.round(attachedFile.size / 1024)} KB)</span>
              <button 
                type="button" 
                onClick={handleRemoveFile} 
                className="workspace-file-remove-btn" 
                title="Xóa tệp đính kèm"
              >
                <X size={14} />
              </button>
            </div>
          )}

          <form onSubmit={handleSend} className="workspace-input-capsule">
            <input 
              type="file" 
              ref={fileInputRef} 
              onChange={handleFileChange} 
              style={{ display: 'none' }} 
            />
            <button 
              type="button" 
              onClick={handleAttachmentClick} 
              className="workspace-attach-btn" 
              title="Đính kèm tài liệu" 
              disabled={loading || !activeConversationId}
            >
              <Plus size={18} />
            </button>
            <textarea
              ref={textareaRef}
              rows={1}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder={`Đặt câu hỏi hoặc viết prompt thực hành cho ${activeModel.name}...`}
              disabled={loading || !activeConversationId}
              className="workspace-textarea"
            />
            <button 
              type="submit" 
              disabled={loading || (!input.trim() && !attachedFile) || !activeConversationId}
              className="workspace-send-btn"
            >
              <Send size={16} />
            </button>
          </form>

          <div className="workspace-input-footer">
            {/* Model Selector Pill Dropdown */}
            <div className="model-selector-container">
              <button 
                type="button"
                onClick={() => setDropdownOpen(!dropdownOpen)} 
                className="model-selector-trigger"
              >
                {activeModel.provider === 'gemini' ? <Sparkles size={14} color="var(--accent-color)" /> : <Cpu size={14} color="#a855f7" />}
                <span>{activeModel.name}</span>
                <ChevronDown size={14} style={{ opacity: 0.7 }} />
              </button>

              {dropdownOpen && (
                <div className="model-selector-dropdown">
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '0.4rem 0.8rem', borderBottom: '1px solid var(--card-border)', marginBottom: '0.2rem' }}>
                    <span style={{ fontSize: '0.7rem', fontWeight: 'bold', textTransform: 'uppercase', color: 'var(--text-muted)' }}>Chọn động cơ AI</span>
                    <button 
                      type="button"
                      onClick={fetchAvailableModels}
                      disabled={fetchingModels}
                      style={{ background: 'transparent', border: 'none', color: 'var(--accent-color)', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '0.2rem', fontSize: '0.7rem' }}
                    >
                      <RefreshCw size={10} className={fetchingModels ? 'animate-spin' : ''} /> Quét Local Models
                    </button>
                  </div>
                  
                  {models.map((model) => (
                    <div 
                      key={model.id}
                      onClick={() => selectModel(model.id)}
                      className={`model-option ${selectedModelId === model.id ? 'active' : ''}`}
                    >
                      <div className="model-option-header">
                        {model.provider === 'gemini' ? (
                          <Sparkles size={14} color="var(--accent-color)" style={{ flexShrink: 0 }} />
                        ) : (
                          <Cpu size={14} color="#a855f7" style={{ flexShrink: 0 }} />
                        )}
                        <span>{model.name}</span>
                        {selectedModelId === model.id && <Check size={14} color="var(--accent-color)" style={{ marginLeft: 'auto' }} />}
                      </div>
                      <div className="model-option-desc">{model.description}</div>
                    </div>
                  ))}
                </div>
              )}
            </div>

            <div className="workspace-input-hint">
              Không gian thực hành bảo mật và không giới hạn token. Nhấn <b>Enter</b> để gửi, <b>Shift + Enter</b> để xuống dòng.
            </div>
          </div>
        </div>
      </section>

      {/* ==========================================
         GLASSMORPHISM MODAL: AI AGENT CREATION / EDIT
         ========================================== */}
      {agentModalOpen && (
        <div className="modal-overlay">
          <div className="modal-content">
            <div className="modal-header">
              <h2 className="modal-title">
                {editingAgent ? 'Chỉnh sửa AI Agent' : 'Tạo AI Agent Mới'}
              </h2>
              <button 
                type="button"
                onClick={() => setAgentModalOpen(false)}
                className="modal-close-btn"
                title="Đóng"
              >
                <X size={18} />
              </button>
            </div>
            
            <form onSubmit={handleSaveAgent}>
              <div className="form-group">
                <label className="form-label">Tên Agent</label>
                <input 
                  type="text" 
                  value={agentName}
                  onChange={(e) => setAgentName(e.target.value)}
                  placeholder="Ví dụ: Chuyên gia Lập trình Python 🐍"
                  className="form-input"
                  required
                />
              </div>
              
              <div className="form-group">
                <label className="form-label">Chỉ dẫn Hệ thống (System Prompt)</label>
                <textarea 
                  value={agentSystemPrompt}
                  onChange={(e) => setAgentSystemPrompt(e.target.value)}
                  placeholder="Viết hướng dẫn chi tiết cách Agent tư duy và phản hồi..."
                  className="form-textarea"
                  rows={4}
                  required
                />
              </div>

              <div className="form-group">
                <label className="form-label">Động cơ cơ bản (Base Model)</label>
                <select 
                  value={agentModelId} 
                  onChange={(e) => setAgentModelId(e.target.value)}
                  className="form-select"
                >
                  {models.map(m => (
                    <option key={m.id} value={m.id}>
                      {m.name}
                    </option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label className="form-label">Màu sắc đại diện</label>
                <div className="color-presets">
                  {['blue', 'purple', 'orange', 'emerald', 'rose', 'indigo'].map((c) => (
                    <div 
                      key={c}
                      onClick={() => setAgentColor(c)}
                      className={`color-preset color-${c} ${agentColor === c ? 'active' : ''}`}
                      title={c}
                    />
                  ))}
                </div>
              </div>

              <div className="form-group">
                <label className="form-label">Icon đại diện</label>
                <div className="icon-presets">
                  {Object.keys(iconMap).map((iconName) => {
                    const IconComp = iconMap[iconName];
                    return (
                      <button
                        key={iconName}
                        type="button"
                        onClick={() => setAgentIcon(iconName)}
                        className={`icon-preset ${agentIcon === iconName ? 'active' : ''}`}
                        title={iconName}
                      >
                        <IconComp size={16} />
                      </button>
                    );
                  })}
                </div>
              </div>

              <div className="modal-footer">
                <button 
                  type="button" 
                  onClick={() => setAgentModalOpen(false)}
                  className="btn-secondary"
                >
                  Hủy
                </button>
                <button 
                  type="submit" 
                  className="btn-primary"
                  style={{ background: 'var(--accent-color)', color: '#ffffff', border: 'none', padding: '0.6rem 1.2rem', borderRadius: '8px', fontWeight: 600, cursor: 'pointer' }}
                >
                  {editingAgent ? 'Cập nhật' : 'Tạo mới'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

export default PracticeArea;
