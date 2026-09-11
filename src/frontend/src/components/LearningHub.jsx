import React, { useState, useEffect, useMemo } from 'react';
import axios from 'axios';
import { marked } from 'marked';
import { BookOpen, ChevronDown, ChevronRight, GraduationCap, Menu, X } from 'lucide-react';

// UI-only labels for curriculum levels; the actual lesson content lives in the DB.
const LEVELS = [
  { id: 'basic', label: 'Cơ bản' },
  { id: 'prompting', label: 'Prompting' },
  { id: 'advanced', label: 'Nâng cao' },
  { id: 'study', label: 'Học tập' },
  { id: 'work', label: 'Làm việc' },
  { id: 'planning', label: 'Lên kế hoạch' },
  { id: 'vibecoding', label: 'Vibe Coding' },
];

const PROMPT_LAB_MARKER = '{{PROMPT_LAB}}';

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

// Interactive but fully static/simulated prompt demo: lets the reader flip
// between a weak and a strong prompt and see a canned "AI reply" — no real
// API call, clearly labeled as a simulation.
function PromptLab({ data }) {
  const [variant, setVariant] = useState('bad');
  const [reply, setReply] = useState(null); // null | 'loading' | string

  const current = data[variant];

  const handleVariant = (v) => {
    setVariant(v);
    setReply(null);
  };

  const handleRun = () => {
    setReply('loading');
    setTimeout(() => setReply(current.reply), 700);
  };

  return (
    <div className="promptlab">
      <div className="promptlab-head">
        <div className="promptlab-title">
          🧪 Prompt Lab <span className="sim-badge">mô phỏng · không gọi AI thật</span>
        </div>
        <div className="variant-tabs" role="tablist">
          <button
            className="variant-tab"
            data-variant="bad"
            aria-selected={variant === 'bad'}
            onClick={() => handleVariant('bad')}
          >
            {data.bad.label}
          </button>
          <button
            className="variant-tab"
            data-variant="good"
            aria-selected={variant === 'good'}
            onClick={() => handleVariant('good')}
          >
            {data.good.label}
          </button>
        </div>
      </div>
      <div className="promptlab-body">
        <pre className="prompt-box">{current.prompt}</pre>
        <button className="run-btn" onClick={handleRun} disabled={reply === 'loading'}>
          ▶ Chạy thử prompt này
        </button>
        {reply && (
          <div className={`ai-reply ${variant}`}>
            <div className="ai-reply-head">
              <span>AI trả lời (mô phỏng)</span>
              {reply === 'loading' && (
                <span className="typing-dots"><span></span><span></span><span></span></span>
              )}
            </div>
            {reply !== 'loading' && <div className="ai-reply-body">{reply}</div>}
          </div>
        )}
      </div>
    </div>
  );
}

// Renders lesson.content as markdown, splicing in a PromptLab component
// wherever the {{PROMPT_LAB}} marker appears (only a few lessons have one).
function LessonContent({ lesson }) {
  if (!lesson.prompt_lab || !lesson.content.includes(PROMPT_LAB_MARKER)) {
    return <div className="curriculum-item-content" dangerouslySetInnerHTML={renderMarkdown(lesson.content)} />;
  }

  const [before, after] = lesson.content.split(PROMPT_LAB_MARKER);
  let labData;
  try {
    labData = JSON.parse(lesson.prompt_lab);
  } catch (e) {
    console.error('Invalid prompt_lab JSON:', e);
    return <div className="curriculum-item-content" dangerouslySetInnerHTML={renderMarkdown(lesson.content)} />;
  }

  return (
    <div className="curriculum-item-content">
      <div dangerouslySetInnerHTML={renderMarkdown(before)} />
      <PromptLab data={labData} />
      <div dangerouslySetInnerHTML={renderMarkdown(after)} />
    </div>
  );
}

function CurriculumSection() {
  const [curriculum, setCurriculum] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedLessonId, setSelectedLessonId] = useState(null);
  const [expandedLevels, setExpandedLevels] = useState({});
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const fetchCurriculum = async () => {
      try {
        const response = await axios.get('/api/curriculum');
        setCurriculum(response.data);
        if (response.data.length > 0) {
          setSelectedLessonId(response.data[0].id);
          setExpandedLevels({ [response.data[0].level]: true });
        }
      } catch (error) {
        console.error("Error fetching curriculum:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchCurriculum();
  }, []);

  const lessonsByLevel = useMemo(() => {
    const map = {};
    for (const level of LEVELS) map[level.id] = [];
    for (const lesson of curriculum) {
      if (map[lesson.level]) map[lesson.level].push(lesson);
    }
    return map;
  }, [curriculum]);

  const selectedLesson = curriculum.find((lesson) => lesson.id === selectedLessonId);

  const toggleLevel = (levelId) => {
    setExpandedLevels((prev) => ({ ...prev, [levelId]: !prev[levelId] }));
  };

  const handleSelectLesson = (levelId, lessonId) => {
    setSelectedLessonId(lessonId);
    setExpandedLevels((prev) => ({ ...prev, [levelId]: true }));
    setMobileMenuOpen(false);
  };

  return (
    <div className="curriculum-section">
      <h2>
        <GraduationCap size={22} style={{ verticalAlign: 'middle', marginRight: '0.5rem' }} />
        Khóa học AI: Nền tảng & Ứng dụng Thực tế
      </h2>

      {loading ? (
        <p>Đang tải khóa học...</p>
      ) : (
        <div className="curriculum-layout">
          {mobileMenuOpen && <div className="curriculum-sidebar-scrim" onClick={() => setMobileMenuOpen(false)} />}

          <aside className={`curriculum-sidebar ${mobileMenuOpen ? 'open' : ''}`}>
            <div className="curriculum-sidebar-head">
              <span className="eyebrow">Mục lục · luôn hiện khi cuộn</span>
              <button className="curriculum-sidebar-close" onClick={() => setMobileMenuOpen(false)} aria-label="Đóng mục lục">
                <X size={18} />
              </button>
            </div>
            <div className="curriculum-sidebar-scroll">
              {LEVELS.map((level) => {
                const lessons = lessonsByLevel[level.id];
                const isOpen = !!expandedLevels[level.id];
                return (
                  <div className="sidebar-section" key={level.id}>
                    <div className="sidebar-title" onClick={() => toggleLevel(level.id)} title="Nhấn để ẩn/hiện danh sách bài học">
                      <span>{level.label} <span className="count">({lessons.length})</span></span>
                      {isOpen ? <ChevronDown size={13} /> : <ChevronRight size={13} />}
                    </div>
                    {isOpen && (
                      <div className="lesson-nav-list">
                        {lessons.map((lesson, index) => (
                          <button
                            key={lesson.id}
                            className="lesson-nav-item"
                            aria-current={lesson.id === selectedLessonId}
                            onClick={() => handleSelectLesson(level.id, lesson.id)}
                          >
                            <span className="num">{index + 1}</span>
                            <span className="title">{lesson.title}</span>
                          </button>
                        ))}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </aside>

          <div className="curriculum-main">
            <button className="curriculum-menu-toggle" onClick={() => setMobileMenuOpen(true)}>
              <Menu size={16} /> Mục lục bài học
            </button>
            {selectedLesson && (
              <div className="list-container curriculum-lesson-card">
                <h2 className="curriculum-detail-title">{selectedLesson.title}</h2>
                <p className="curriculum-item-summary curriculum-detail-summary">{selectedLesson.summary}</p>
                <LessonContent lesson={selectedLesson} />
              </div>
            )}
          </div>
        </div>
      )}
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
