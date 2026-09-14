#!/usr/bin/env bash
#
# check-review-checklists.sh — Mỗi phase trong v-model/ phải có review-checklist.md +
# review-report.md (presence). Với --quality: checklist phải tick HẾT (= phase ĐẠT chất lượng).
#
# Dùng:
#   bash scripts/check-review-checklists.sh            # cảnh báo
#   bash scripts/check-review-checklists.sh --strict   # CHẶN nếu phase thiếu file review
#   bash scripts/check-review-checklists.sh --quality  # thêm: checklist phải tick hết (gate giao nộp)
#
set -uo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
[[ -d v-model ]] || { echo "ℹ Không có v-model — bỏ qua."; exit 0; }

STRICT=0; QUALITY=0
for a in "$@"; do case "$a" in --strict) STRICT=1 ;; --quality) QUALITY=1 ;; esac; done
errors=0
err() { echo "  ✗ $1"; errors=$((errors + 1)); }

echo "→ Kiểm review checklist/report mỗi phase"
for d in v-model/[0-9][0-9]-*/; do
  d="${d%/}"; ph="$(basename "$d")"
  [[ -f "$d/review-checklist.md" ]] || err "$ph thiếu review-checklist.md"
  [[ -f "$d/review-report.md" ]]    || err "$ph thiếu review-report.md"
  if [[ $QUALITY -eq 1 && -f "$d/review-checklist.md" ]]; then
    n="$(grep -c '^- \[ \]' "$d/review-checklist.md" 2>/dev/null || echo 0)"
    [[ "$n" -eq 0 ]] || err "$ph: checklist còn $n mục CHƯA tick (chưa ĐẠT chất lượng)."
  fi
done

echo "—"
echo "Kết quả: $errors lỗi."
if [[ $STRICT -eq 1 && $errors -gt 0 ]]; then echo "✗ FAIL (strict)."; exit 1; fi
echo "✓ OK."
exit 0
