import React, { useState } from 'react';
import NewsFeed from './components/NewsFeed';
import LearningHub from './components/LearningHub';
import PracticeArea from './components/PracticeArea';
import axios from 'axios';
import { Sparkles, RefreshCw } from 'lucide-react';
import './index.css';

// Using relative path. Nginx will proxy /api to the backend container.
// In dev mode without Nginx, we would need to configure vite.config.js server.proxy

function App() {
  const [activeTab, setActiveTab] = useState('news');
  const [isRefreshing, setIsRefreshing] = useState(false);

  const handleRefresh = async () => {
    setIsRefreshing(true);
    try {
      await axios.post('/api/agent/run');
      alert("Agent has fetched new data! Refresh the tabs to see them.");
    } catch (error) {
      console.error("Error triggering agent", error);
      alert("Failed to trigger agent.");
    } finally {
      setIsRefreshing(false);
    }
  };

  return (
    <div className="app-container">
      <header>
        <div className="logo">
          <Sparkles className="inline-block mr-2" /> AI Learning Hub
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
        {activeTab === 'news' && <NewsFeed />}
        {activeTab === 'learning' && <LearningHub />}
        {activeTab === 'practice' && <PracticeArea />}
      </main>
    </div>
  );
}

export default App;
