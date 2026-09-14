#!/usr/bin/env bash
#
# check-doc-staleness.sh — TẦNG 3: chống "đổi code mà quên cập nhật tài liệu".
# Per-item staleness: nếu code mang comment `DD-###` thay đổi mà mục thiết kế tương ứng
# (03-DDD.md) KHÔNG đổi trong cùng thay đổi → cảnh báo/chặn.
#
# Phạm vi diff / Diff range:
#   - Mặc định: thay đổi đang có (staged + working) so với HEAD.
#   - CI: truyền base ref, vd:  check-doc-staleness.sh --strict origin/main...HEAD
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

git rev-parse --git-dir >/dev/null 2>&1 || { echo "ℹ Không phải git repo — bỏ qua."; exit 0; }

DDD="v-model/04-detailed-design/03-DDD.md"
SRC_DIRS="frontend backend backend-python shared"
[[ -f "$DDD" ]] || { echo "ℹ Không có $DDD — bỏ qua."; exit 0; }

STRICT=0; RANGE=""
for a in "$@"; do case "$a" in --strict) STRICT=1 ;; *) RANGE="$a" ;; esac; done

# Tập file đã thay đổi.
if [[ -n "$RANGE" ]]; then
  changed="$(git diff --name-only "$RANGE" 2>/dev/null || true)"
else
  changed="$( { git diff --name-only; git diff --name-only --cached; } 2>/dev/null | sort -u )"
fi
ddd_changed=no
printf '%s\n' "$changed" | grep -qxF "$DDD" && ddd_changed=yes

errors=0; warns=0
err()  { echo "  ✗ $1"; errors=$((errors + 1)); }
warn() { echo "  ⚠ $1"; warns=$((warns + 1)); }

echo "→ TẦNG 3 — staleness theo ID (code ↔ Detailed Design)"

for id in $(grep -oE 'DD-[0-9]{3}' "$DDD" | sort -u); do
  # File code tham chiếu tới id này
  codefiles="$(grep -rlE "\\b$id\\b" $SRC_DIRS 2>/dev/null || true)"
  [[ -z "$codefiles" ]] && continue
  code_changed=no
  while IFS= read -r f; do
    [[ -z "$f" ]] && continue
    printf '%s\n' "$changed" | grep -qxF "$f" && code_changed=yes
  done <<< "$codefiles"
  if [[ "$code_changed" == "yes" && "$ddd_changed" == "no" ]]; then
    if [[ $STRICT -eq 1 ]]; then
      err "Code mang '$id' đã đổi nhưng $DDD (mục $id) KHÔNG đổi → cập nhật thiết kế."
    else
      warn "Code mang '$id' đã đổi nhưng $DDD (mục $id) chưa đổi → rà lại thiết kế."
    fi
  fi
done

echo "—"
echo "Kết quả / Result: $errors lỗi, $warns cảnh báo."
if [[ $STRICT -eq 1 && $errors -gt 0 ]]; then
  echo "✗ FAIL (strict): tài liệu thiết kế có thể đã cũ so với code."
  exit 1
fi
echo "✓ OK."
