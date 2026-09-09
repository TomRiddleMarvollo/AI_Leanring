import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { marked } from 'marked';
import { BookOpen, ChevronRight, GraduationCap, ArrowLeft } from 'lucide-react';

// UI-only labels for curriculum levels; the actual lesson content lives in the DB.
const LEVELS = [
  { id: 'basic', label: 'Cơ bản' },
  { id: 'prompting', label: 'Prompting' },
  { id: 'advanced', label: 'Nâng cao' },
  { id: 'study', label: 'Học tập' },
  { id: 'work', label: 'Làm việc' },
  { id: 'planning', label: 'Lên kế hoạch' },
];

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

function LessonDetail({ lesson, onBack }) {
  return (
    <div className="list-container curriculum-section">
      <button className="curriculum-back-btn" onClick={onBack}>
        <ArrowLeft size={18} />
        Quay lại danh sách bài học
      </button>
      <h2 className="curriculum-detail-title">{lesson.title}</h2>
      <p className="curriculum-item-summary curriculum-detail-summary">{lesson.summary}</p>
      <div
        className="curriculum-item-content curriculum-detail-content"
        dangerouslySetInnerHTML={renderMarkdown(lesson.content)}
      />
      <button className="curriculum-back-btn curriculum-back-btn-bottom" onClick={onBack}>
        <ArrowLeft size={18} />
        Quay lại danh sách bài học
      </button>
    </div>
  );
}

function CurriculumSection() {
  const [activeLevel, setActiveLevel] = useState(LEVELS[0].id);
  const [selectedLessonId, setSelectedLessonId] = useState(null);
  const [curriculum, setCurriculum] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchCurriculum = async () => {
      try {
        const response = await axios.get('/api/curriculum');
        setCurriculum(response.data);
      } catch (error) {
        console.error("Error fetching curriculum:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchCurriculum();
  }, []);

  const lessons = curriculum.filter((lesson) => lesson.level === activeLevel);
  const selectedLesson = curriculum.find((lesson) => lesson.id === selectedLessonId);

  const handleSelectLevel = (levelId) => {
    setActiveLevel(levelId);
    setSelectedLessonId(null);
  };

  if (selectedLesson) {
    return <LessonDetail lesson={selectedLesson} onBack={() => setSelectedLessonId(null)} />;
  }

  return (
    <div className="list-container curriculum-section">
      <h2><GraduationCap size={22} style={{ verticalAlign: 'middle', marginRight: '0.5rem' }} />Khóa học AI: Nền tảng & Ứng dụng Thực tế</h2>

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

      {loading && <p>Đang tải khóa học...</p>}

      <div className="curriculum-list">
        {lessons.map((lesson, index) => (
          <button
            key={lesson.id}
            className="curriculum-item-header"
            onClick={() => setSelectedLessonId(lesson.id)}
          >
            <span className="curriculum-item-number">{index + 1}</span>
            <span className="curriculum-item-title-wrap">
              <span className="curriculum-item-title">{lesson.title}</span>
              <span className="curriculum-item-summary">{lesson.summary}</span>
            </span>
            <ChevronRight size={20} />
          </button>
        ))}
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
