#!/usr/bin/env bash
#
# check-docs.sh — Tự NHẮC cập nhật tài liệu cho khớp dự án.
# Auto-reminder that project docs are filled in & in sync.
#
# Phát hiện: lệnh build/test chưa điền, placeholder/ví dụ mẫu còn sót,
# và thư mục nguồn chưa được nhắc trong CODEMAP.md.
#
# Dùng / Usage:
#   bash scripts/check-docs.sh            # chỉ cảnh báo (exit 0)
#   bash scripts/check-docs.sh --strict   # lỗi bắt buộc -> exit 1 (dùng cho CI)
#
set -euo pipefail

# --- Xác định gốc repo (chạy được cả trong/ngoài git) ---
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "$ROOT" ]]; then
  ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fi
cd "$ROOT"

STRICT=0
[[ "${1:-}" == "--strict" ]] && STRICT=1

errors=0
warns=0
err()  { echo "  ✗ $1"; errors=$((errors + 1)); }
warn() { echo "  ⚠ $1"; warns=$((warns + 1)); }

echo "→ Checking docs in: $ROOT"

# 1) AGENTS.md: lệnh Install/Run/Test/Lint chưa điền (BẮT BUỘC).
if [[ -f AGENTS.md ]] && grep -q '_______' AGENTS.md; then
  err "AGENTS.md còn lệnh chưa điền ('_______') — điền Install/Run/Test/Lint."
fi

# 2) Placeholder / ví dụ mẫu còn sót trong doc commit (CẢNH BÁO).
DOCS=(AGENTS.md CODEMAP.md CONVENTIONS.md README.md)
while IFS= read -r f; do DOCS+=("$f"); done < <(find docs -maxdepth 1 -name '*.md' 2>/dev/null || true)
for f in "${DOCS[@]}"; do
  [[ -f "$f" ]] || continue
  if grep -qE '_\(ví dụ|_\(e\.g\.|_\.\.\._|_{4,}' "$f"; then
    warn "$f còn placeholder/ví dụ mẫu — nhớ thay bằng nội dung thật."
  fi
done

# 3) Khu vực nguồn cấp cao chưa được nhắc trong CODEMAP.md (CẢNH BÁO).
#    Chỉ kiểm tra các "root" lớn để tránh nhiễu — CODEMAP nên ngắn gọn.
if [[ -f CODEMAP.md ]]; then
  for name in frontend backend backend-python shared packages apps services; do
    [[ -d "$name" ]] || continue
    grep -qw "$name" CODEMAP.md || warn "CODEMAP.md chưa nhắc tới khu vực nguồn '$name/'."
  done
fi

echo "—"
echo "Kết quả / Result: $errors lỗi (errors), $warns cảnh báo (warnings)."
if [[ $STRICT -eq 1 && $errors -gt 0 ]]; then
  echo "✗ FAIL (strict): còn $errors mục bắt buộc chưa hoàn tất."
  exit 1
fi
echo "✓ OK — cảnh báo không chặn (warnings don't block)."
