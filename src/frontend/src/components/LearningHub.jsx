import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BookOpen } from 'lucide-react';

function LearningHub() {
  const [modules, setModules] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchModules = async () => {
      try {
        const response = await axios.get('/api/learn');
        setModules(response.data);
      } catch (error) {
        console.error("Error fetching learning modules:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchModules();
  }, []);

  if (loading) return <p>Đang tải bài học...</p>;
  if (modules.length === 0) return <p>Chưa có bài học nào. Vui lòng bấm Cập nhật DL.</p>;

  return (
    <div className="list-container">
      <h2>Bài học Thực hành & Best Practices</h2>
      <div>
        {modules.map((mod) => (
          <div key={mod.id} className="news-item">
            <div className="news-thumbnail learning">AI GUIDE</div>
            <div className="news-content">
              <div className="news-title">{mod.title}</div>
              <div className="news-summary" style={{ whiteSpace: 'pre-line' }}>{mod.content}</div>
              <div className="news-meta">
                <span className="badge learning">{mod.category}</span>
                <span>{new Date(mod.created_at).toLocaleDateString()}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default LearningHub;
