import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import { Send, Bot } from 'lucide-react';

function PracticeArea() {
  const [messages, setMessages] = useState([
    { role: 'ai', content: 'Chào bạn! Đây là không gian thực hành. Hãy thử áp dụng các kỹ thuật Prompt Engineering bạn vừa học vào đây nhé.' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const chatHistoryRef = useRef(null);

  useEffect(() => {
    if (chatHistoryRef.current) {
      chatHistoryRef.current.scrollTop = chatHistoryRef.current.scrollHeight;
    }
  }, [messages]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await axios.post('/api/practice', { prompt: userMessage.content });
      setMessages((prev) => [...prev, { role: 'ai', content: response.data.response }]);
    } catch (error) {
      console.error("Error with practice chat:", error);
      setMessages((prev) => [...prev, { role: 'ai', content: 'Lỗi: Không thể kết nối với AI model nội bộ.' }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Không gian Thực hành</h2>
      <p style={{ marginBottom: '1.5rem' }}>Tương tác trực tiếp với Local LLM (Ollama) hoàn toàn riêng tư và không giới hạn token.</p>
      
      <div className="chat-container">
        <div className="chat-history" ref={chatHistoryRef}>
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.role}`}>
              {msg.role === 'ai' && (
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem', color: '#94a3b8' }}>
                  <Bot size={16} /> <span style={{ fontSize: '0.8rem', fontWeight: 'bold' }}>AI Assistant</span>
                </div>
              )}
              <div style={{ whiteSpace: 'pre-wrap' }}>{msg.content}</div>
            </div>
          ))}
          {loading && (
            <div className="message ai">
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: '#94a3b8' }}>
                <Bot size={16} /> <span style={{ fontSize: '0.8rem', fontWeight: 'bold' }}>AI Assistant</span>
              </div>
              <div style={{ fontStyle: 'italic', opacity: 0.7 }}>Đang suy nghĩ...</div>
            </div>
          )}
        </div>
        
        <form onSubmit={handleSend} className="chat-input-area">
          <input 
            type="text" 
            placeholder="Nhập prompt thực hành của bạn tại đây..." 
            value={input}
            onChange={(e) => setInput(e.target.value)}
            disabled={loading}
          />
          <button type="submit" className="btn-primary" disabled={loading} style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Send size={18} /> Gửi
          </button>
        </form>
      </div>
    </div>
  );
}

export default PracticeArea;
