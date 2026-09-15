import React, { useState, useEffect, useMemo, useRef } from 'react';
import axios from 'axios';
import { marked } from 'marked';
import { BookOpen, ChevronDown, ChevronRight, GraduationCap, Menu, X, Search, Compass } from 'lucide-react';
import LessonWelcome from './LessonWelcome';

// UI-only labels for curriculum levels; the actual lesson content lives in the DB.
// `icon` is only used for levels in the "needs" cluster (see LEVEL_CLUSTERS below).
const LEVELS = [
  { id: 'basic', label: 'Cơ bản' },
  { id: 'prompting', label: 'Prompting' },
  { id: 'advanced', label: 'Nâng cao' },
  { id: 'study', label: 'Học tập', icon: '📘' },
  { id: 'work', label: 'Làm việc', icon: '💼' },
  { id: 'planning', label: 'Lên kế hoạch', icon: '🗓️' },
  { id: 'vibecoding', label: 'Vibe Coding', icon: '🤖' },
];

// Groups the flat LEVELS list into two sidebar clusters: a sequential
// foundations path (numbered 1→2→3) vs. a pick-what-you-need set of
// use-case playbooks (icon badges, no implied order).
const LEVEL_CLUSTERS = [
  {
    id: 'path',
    title: 'Lộ trình nền tảng',
    subtitle: 'học theo thứ tự 1→2→3',
    levelIds: ['basic', 'prompting', 'advanced'],
  },
  {
    id: 'needs',
    title: 'Ứng dụng theo nhu cầu',
    subtitle: 'xem bài nào cần, không cần theo thứ tự',
    levelIds: ['study', 'work', 'planning', 'vibecoding'],
  },
];

// "Bạn đang ở đâu?" quick-start picker: jumps straight to the relevant
// section instead of making the reader hunt through the accordion.
// `icon`/`desc` are only used by the LessonWelcome screen's richer cards;
// the compact sidebar version just shows `label`.
const QUICK_START = [
  { icon: '🌱', label: 'Chưa biết gì về AI', desc: 'Bắt đầu từ khái niệm cơ bản: AI, LLM, Token...', target: 'basic' },
  { icon: '✍️', label: 'Biết cơ bản, muốn prompt giỏi hơn', desc: 'Kỹ thuật prompt hiệu quả: cấu trúc, Chain-of-Thought...', target: 'prompting' },
  { icon: '🎯', label: 'Muốn áp dụng vào học tập/công việc', desc: 'Playbook thực tế: học tập, làm việc, lên kế hoạch', target: 'needs' },
  { icon: '💻', label: 'Code cùng AI (vibe coding)', desc: 'Làm việc hiệu quả với Claude Code và các AI agent', target: 'vibecoding' },
];

const LAST_LESSON_STORAGE_KEY = 'ai_learning_last_lesson_id';

const PROMPT_LAB_MARKER = '{{PROMPT_LAB}}';

// Strip Vietnamese diacritics so search matches regardless of accents
// (e.g. "hoc tap" still finds "Học tập").
const normalizeVN = (str) =>
  (str || '')
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/đ/g, 'd')
    .replace(/Đ/g, 'D')
    .toLowerCase();

// Splits text around the first match of query, for <mark> highlighting.
// Returns the original text untouched (as a single-element array) if no match.
const splitForHighlight = (text, query) => {
  if (!query) return [text];
  const normText = normalizeVN(text);
  const idx = normText.indexOf(normalizeVN(query));
  if (idx === -1) return [text];
  return [text.slice(0, idx), text.slice(idx, idx + query.length), text.slice(idx + query.length)];
};

function HighlightedText({ text, query }) {
  const [before, match, after] = splitForHighlight(text, query);
  if (match === undefined) return <>{text}</>;
  return <>{before}<mark>{match}</mark>{after}</>;
}

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
            {reply !== 'loading' && <div className="ai-reply-body" dangerouslySetInnerHTML={renderMarkdown(reply)} />}
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
  const [searchQuery, setSearchQuery] = useState('');
  const [pickedQuickStart, setPickedQuickStart] = useState(null);
  const sectionRefs = useRef({});

  useEffect(() => {
    const fetchCurriculum = async () => {
      try {
        const response = await axios.get('/api/curriculum');
        setCurriculum(response.data);
        // Resume the last lesson the reader had open, instead of always
        // dropping first-time visitors straight into a full lesson before
        // they've had a chance to orient (see LessonWelcome).
        const lastId = localStorage.getItem(LAST_LESSON_STORAGE_KEY);
        const lastLesson = response.data.find((lesson) => lesson.id === lastId);
        if (lastLesson) {
          setSelectedLessonId(lastLesson.id);
          setExpandedLevels({ [lastLesson.level]: true });
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

  const clusterLessonCount = (clusterId) =>
    LEVEL_CLUSTERS.find((c) => c.id === clusterId).levelIds.reduce(
      (sum, levelId) => sum + lessonsByLevel[levelId].length,
      0
    );

  const trimmedQuery = searchQuery.trim();
  const searchResults = useMemo(() => {
    if (!trimmedQuery) return [];
    const q = normalizeVN(trimmedQuery);
    return curriculum.filter(
      (lesson) => normalizeVN(lesson.title).includes(q) || normalizeVN(lesson.summary).includes(q)
    );
  }, [curriculum, trimmedQuery]);

  const toggleLevel = (levelId) => {
    setExpandedLevels((prev) => ({ ...prev, [levelId]: !prev[levelId] }));
  };

  const handleSelectLesson = (levelId, lessonId) => {
    setSelectedLessonId(lessonId);
    setExpandedLevels((prev) => ({ ...prev, [levelId]: true }));
    setMobileMenuOpen(false);
    localStorage.setItem(LAST_LESSON_STORAGE_KEY, lessonId);
  };

  const handleSelectSearchResult = (lesson) => {
    handleSelectLesson(lesson.level, lesson.id);
  };

  // Jumps to the relevant section for a "Bạn đang ở đâu?" quick-start pick.
  // 'needs' expands the whole use-case cluster instead of a single level.
  const handleQuickStart = (target) => {
    setPickedQuickStart(target);
    setSearchQuery('');
    if (target === 'needs') {
      const needsCluster = LEVEL_CLUSTERS.find((c) => c.id === 'needs');
      setExpandedLevels((prev) => {
        const next = { ...prev };
        for (const levelId of needsCluster.levelIds) next[levelId] = true;
        return next;
      });
      sectionRefs.current[needsCluster.levelIds[0]]?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
      setExpandedLevels((prev) => ({ ...prev, [target]: true }));
      sectionRefs.current[target]?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  // Same targets as the quick-start picker, but triggered from the welcome
  // screen (no lesson selected yet) — so unlike handleQuickStart, this also
  // opens the first lesson of the target instead of just expanding the
  // sidebar, since there's no lesson content behind it yet to fall back on.
  const handleWelcomeStart = (target) => {
    if (target === 'needs') {
      const needsCluster = LEVEL_CLUSTERS.find((c) => c.id === 'needs');
      setExpandedLevels((prev) => {
        const next = { ...prev };
        for (const levelId of needsCluster.levelIds) next[levelId] = true;
        return next;
      });
      const firstLevelId = needsCluster.levelIds[0];
      const firstLesson = lessonsByLevel[firstLevelId]?.[0];
      if (firstLesson) handleSelectLesson(firstLevelId, firstLesson.id);
    } else {
      const firstLesson = lessonsByLevel[target]?.[0];
      if (firstLesson) handleSelectLesson(target, firstLesson.id);
    }
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
              <div className="sidebar-head-top">
                <span className="eyebrow">Mục lục · luôn hiện khi cuộn</span>
                <button className="curriculum-sidebar-close" onClick={() => setMobileMenuOpen(false)} aria-label="Đóng mục lục">
                  <X size={18} />
                </button>
              </div>
              <div className="curriculum-quickstart">
                <div className="curriculum-quickstart-label">
                  <Compass size={13} /> Bạn đang ở đâu?
                </div>
                <div className="qs-grid">
                  {QUICK_START.map((qs) => (
                    <button
                      key={qs.target}
                      className={`qs-btn ${pickedQuickStart === qs.target ? 'picked' : ''}`}
                      onClick={() => handleQuickStart(qs.target)}
                    >
                      {qs.label}
                    </button>
                  ))}
                </div>
              </div>
              <div className={`search-box ${searchQuery ? 'has-value' : ''}`}>
                <Search size={15} />
                <input
                  type="text"
                  className="search-input"
                  placeholder="Tìm bài học..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                />
                {searchQuery && (
                  <button className="search-clear" onClick={() => setSearchQuery('')} aria-label="Xoá tìm kiếm">
                    <X size={14} />
                  </button>
                )}
              </div>
            </div>
            <div className="curriculum-sidebar-scroll">
              {trimmedQuery ? (
                searchResults.length === 0 ? (
                  <div className="search-empty">
                    Không tìm thấy bài học nào phù hợp với "<strong>{trimmedQuery}</strong>".
                  </div>
                ) : (
                  <>
                    <div className="search-count">{searchResults.length} bài học phù hợp</div>
                    <div className="search-results">
                      {searchResults.map((lesson) => (
                        <button
                          key={lesson.id}
                          className="search-result-item"
                          onClick={() => handleSelectSearchResult(lesson)}
                        >
                          <span className="search-result-level">
                            {LEVELS.find((l) => l.id === lesson.level)?.label || lesson.level}
                          </span>
                          <span className="search-result-title">
                            <HighlightedText text={lesson.title} query={trimmedQuery} />
                          </span>
                          <span className="search-result-summary">
                            <HighlightedText text={lesson.summary} query={trimmedQuery} />
                          </span>
                        </button>
                      ))}
                    </div>
                  </>
                )
              ) : (
              LEVEL_CLUSTERS.map((cluster) => (
                <div className={`curriculum-cluster ${cluster.id}`} key={cluster.id}>
                  <div className={`curriculum-cluster-head ${cluster.id}`}>
                    <span className="dot"></span>
                    <h3>{cluster.title} <span className="sub">· {cluster.subtitle}</span></h3>
                  </div>
                  {cluster.levelIds.map((levelId, pathIndex) => {
                    const level = LEVELS.find((l) => l.id === levelId);
                    const lessons = lessonsByLevel[level.id];
                    const isOpen = !!expandedLevels[level.id];
                    return (
                      <div
                        className="sidebar-section"
                        key={level.id}
                        ref={(el) => { sectionRefs.current[level.id] = el; }}
                      >
                        <div className="sidebar-title" onClick={() => toggleLevel(level.id)} title="Nhấn để ẩn/hiện danh sách bài học">
                          <span>
                            <span className={`level-badge ${cluster.id === 'path' ? 'number' : 'icon'}`}>
                              {cluster.id === 'path' ? pathIndex + 1 : level.icon}
                            </span>
                            {level.label} <span className="count">({lessons.length})</span>
                          </span>
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
              ))
              )}
            </div>
          </aside>

          <div className="curriculum-main">
            <button className="curriculum-menu-toggle" onClick={() => setMobileMenuOpen(true)}>
              <Menu size={16} /> Mục lục bài học
            </button>
            {selectedLesson ? (
              <div className="list-container curriculum-lesson-card">
                <h2 className="curriculum-detail-title">{selectedLesson.title}</h2>
                <p className="curriculum-item-summary curriculum-detail-summary">{selectedLesson.summary}</p>
                <LessonContent key={selectedLesson.id} lesson={selectedLesson} />
              </div>
            ) : (
              <div className="list-container">
                <LessonWelcome
                  quickStart={QUICK_START}
                  pathCount={clusterLessonCount('path')}
                  needsCount={clusterLessonCount('needs')}
                  totalLessons={curriculum.length}
                  onStart={handleWelcomeStart}
                />
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
                <div className="community-module-content" dangerouslySetInnerHTML={renderMarkdown(mod.content)} />
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
