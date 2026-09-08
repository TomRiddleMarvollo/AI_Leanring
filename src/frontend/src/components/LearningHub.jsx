import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { marked } from 'marked';
import { BookOpen, ChevronDown, ChevronRight, GraduationCap } from 'lucide-react';
import { CURRICULUM, LEVELS } from '../data/curriculum';

// Helper to render markdown safely (same pattern as PracticeArea)
const renderMarkdown = (text) => {
  try {
    const rawHtml = marked.parse(text || '', { gfm: true, breaks: true });
    return { __html: rawHtml };
  } catch (e) {
    console.error("Markdown parsing error:", e);
    return { __html: text || '' };
  }
};

function CurriculumSection() {
  const [activeLevel, setActiveLevel] = useState(LEVELS[0].id);
  const [expandedId, setExpandedId] = useState(null);

  const lessons = CURRICULUM.filter((lesson) => lesson.level === activeLevel);

  const handleSelectLevel = (levelId) => {
    setActiveLevel(levelId);
    setExpandedId(null);
  };

  return (
    <div className="list-container curriculum-section">
      <h2><GraduationCap size={22} style={{ verticalAlign: 'middle', marginRight: '0.5rem' }} />Khóa học AI Cơ bản đến Nâng cao</h2>

      <div className="curriculum-tabs">
        {LEVELS.map((level) => (
          <button
            key={level.id}
            className={`nav-btn curriculum-tab ${activeLevel === level.id ? 'active' : ''}`}
            onClick={() => handleSelectLevel(level.id)}
          >
            {level.label}
          </button>
        ))}
      </div>

      <div className="curriculum-list">
        {lessons.map((lesson, index) => {
          const isOpen = expandedId === lesson.id;
          return (
            <div key={lesson.id} className={`curriculum-item ${isOpen ? 'open' : ''}`}>
              <button
                className="curriculum-item-header"
                onClick={() => setExpandedId(isOpen ? null : lesson.id)}
              >
                <span className="curriculum-item-number">{index + 1}</span>
                <span className="curriculum-item-title-wrap">
                  <span className="curriculum-item-title">{lesson.title}</span>
                  <span className="curriculum-item-summary">{lesson.summary}</span>
                </span>
                {isOpen ? <ChevronDown size={20} /> : <ChevronRight size={20} />}
              </button>
              {isOpen && (
                <div
                  className="curriculum-item-content"
                  dangerouslySetInnerHTML={renderMarkdown(lesson.content)}
                />
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

function CommunityFeed() {
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

  return (
    <div className="list-container">
      <h2><BookOpen size={22} style={{ verticalAlign: 'middle', marginRight: '0.5rem' }} />Bài học Cộng đồng (AI tổng hợp)</h2>
      {loading ? (
        <p>Đang tải bài học...</p>
      ) : modules.length === 0 ? (
        <p>Chưa có bài học nào. Vui lòng bấm Cập nhật DL.</p>
      ) : (
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
      )}
    </div>
  );
}

function LearningHub() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <CurriculumSection />
      <CommunityFeed />
    </div>
  );
}

export default LearningHub;
