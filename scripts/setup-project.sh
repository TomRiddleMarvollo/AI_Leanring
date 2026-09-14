#!/usr/bin/env bash
#
# setup-project.sh — Chạy MỘT LẦN cho mỗi dự án mới (sau khi git init / clone).
# Run ONCE per project to enable the auto-reminder git hooks.
#
# Việc cần nhớ duy nhất là chạy script này một lần; mọi nhắc nhở sau đó tự động.
# The only thing to remember is running this once; reminders are automatic after.
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

# Trỏ git tới thư mục hook trong repo (commit được, chia sẻ cho cả team).
git config core.hooksPath scripts/git-hooks
chmod +x scripts/git-hooks/* scripts/*.sh 2>/dev/null || true
echo "✓ Đã bật git hooks: core.hooksPath = scripts/git-hooks"

echo "→ Tự điền lệnh build/test vào AGENTS.md (từ package.json/requirements):"
bash scripts/gen-commands.sh || true

echo "→ Sinh ma trận truy vết + inventory ground-truth (Tầng 1):"
bash scripts/gen-traceability.sh || true
bash scripts/gen-ground-truth.sh || true
bash scripts/gen-code-trace.sh || true   # trích @trace từ code
bash scripts/gen-review-checklist.sh || true   # sinh AUTO review-checklist

echo "→ Chạy kiểm tra tài liệu lần đầu:"
bash scripts/check-docs.sh || true
bash scripts/check-i18n.sh || true
bash scripts/check-lib-boundaries.sh || true
bash scripts/check-code-size.sh || true
bash scripts/check-lint.sh || true
bash scripts/check-fn-doc.sh || true
bash scripts/check-api-surface.sh --update || true   # ghi snapshot API lần đầu
bash scripts/check-circular-deps.sh || true
bash scripts/check-traceability.sh || true
bash scripts/check-grounding.sh || true
bash scripts/check-test-trace.sh || true
bash scripts/check-suppressions.sh || true
bash scripts/check-completeness.sh || true
bash scripts/check-review-checklists.sh || true
bash scripts/check-doc-staleness.sh || true       # Tầng 3
bash scripts/check-code-doc-coverage.sh || true   # phủ 100% code↔doc
bash scripts/check-test-coverage.sh || true       # ngưỡng coverage

echo "→ Kiểm tra bảo mật (secret / CVE / SAST):"
bash scripts/check-secrets.sh || true
bash scripts/check-deps-security.sh || true
bash scripts/check-sast.sh || true

echo "ℹ TẦNG 2 (LLM review, tuỳ chọn) — cần Ollama + qwen3:30b chạy local:"
echo "    bash scripts/review-docs-llm.sh        # phản biện độ đầy đủ/sâu"

echo "✓ Xong. Từ giờ mỗi 'git commit' sẽ tự nhắc cập nhật tài liệu."
echo "  (CI cũng kiểm tra độc lập — xem .github/workflows/docs-check.yml)"
