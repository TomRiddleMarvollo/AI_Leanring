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
    <div>
      <h2>Học tập (Best Practices)</h2>
      <div className="grid-container">
        {modules.map((module) => (
          <div key={module.id} className="glass-card" style={{ borderLeft: '4px solid var(--accent-color)' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem' }}>
              <BookOpen size={20} color="var(--accent-color)" />
              <span style={{ fontSize: '0.8rem', color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                {module.category}
              </span>
            </div>
            <h3>{module.title}</h3>
            {/* Simple render of markdown-like text */}
            <div style={{ whiteSpace: 'pre-wrap', color: '#cbd5e1', fontSize: '0.95rem' }}>
              {module.content}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default LearningHub;
