import React from 'react';
import { Compass } from 'lucide-react';

// Default landing state for the "Bài học" tab: shown until the reader has
// picked at least one lesson (see CurriculumSection's localStorage-backed
// "last visited lesson" logic) — avoids dropping a first-time visitor
// straight into a long lesson before they've had a chance to orient.
function LessonWelcome({ quickStart, pathCount, needsCount, totalLessons, onStart }) {
  return (
    <div className="lesson-welcome">
      <span className="lesson-welcome-wave">👋</span>
      <h2>Chào bạn, bắt đầu từ đâu?</h2>
      <p className="lesson-welcome-lede">
        Khoá học có <b>{totalLessons} bài</b>, chia thành lộ trình học theo thứ tự và các playbook chọn theo nhu cầu.
        Chọn 1 trong 4 lựa chọn dưới đây — hoặc duyệt trong menu bên trái bất cứ lúc nào.
      </p>

      <div className="qs-label">
        <Compass size={15} /> Bạn đang ở đâu?
      </div>
      <div className="qs-grid welcome-qs-grid">
        {quickStart.map((qs) => (
          <button key={qs.target} className="qs-btn welcome-qs-btn" onClick={() => onStart(qs.target)}>
            <span className="qs-icon">{qs.icon}</span>
            <div className="qs-title">{qs.label}</div>
            <div className="qs-desc">{qs.desc}</div>
          </button>
        ))}
      </div>

      <div className="lesson-welcome-divider">hoặc duyệt theo cụm</div>

      <div className="browse-grid">
        <button className="browse-card path" onClick={() => onStart('basic')}>
          <div className="bc-head">
            <span className="bc-title">📚 Lộ trình nền tảng</span>
            <span className="bc-count">{pathCount} bài</span>
          </div>
          <div className="bc-desc">Cơ bản → Prompting → Nâng cao. Học theo thứ tự nếu bạn mới bắt đầu.</div>
        </button>
        <button className="browse-card needs" onClick={() => onStart('needs')}>
          <div className="bc-head">
            <span className="bc-title">🛠️ Ứng dụng theo nhu cầu</span>
            <span className="bc-count">{needsCount} bài</span>
          </div>
          <div className="bc-desc">Học tập, Làm việc, Lên kế hoạch, Vibe Coding. Xem bài nào cần, không cần theo thứ tự.</div>
        </button>
      </div>
    </div>
  );
}

export default LessonWelcome;
