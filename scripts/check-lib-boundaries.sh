#!/usr/bin/env bash
#
# check-lib-boundaries.sh — Ép tính tự-đủ của lõi tái dùng: `lib/`/`packages/`
# KHÔNG được import ngược vào app (routes/services/store/config/app.*...).
# Enforce that reusable code does not depend on app-specific layers.
#
# Vi phạm = code khó trích xuất thành thư viện. CHẶN ở --strict.
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
LIB_DIRS="frontend/src/lib backend/src/lib backend-python/app/lib packages"
errors=0
echo "→ Kiểm tra ranh giới lib (lib/ không phụ thuộc app)"

# JS/TS: import/require/from "<.. | @ | ~>/...app|routes|services|store|controllers|models|middlewares|pages..."
JS_RE="(import|require|from)[^\"']*[\"'](\\.\\.|@|~)[^\"']*\\b(app|routes|services|store|controllers|models|middlewares|pages)\\b"
# Python: from app.<layer> ... / import app.<layer>
PY_RE="^[[:space:]]*(from|import)[[:space:]]+app\\.(services|routes|controllers|api|core|db|models|middlewares|config)\\b"

report() { echo "  ✗ $1"; errors=$((errors + 1)); }

for d in $LIB_DIRS; do
  [[ -d "$d" ]] || continue
  while IFS= read -r hit; do
    [[ -z "$hit" ]] && continue
    report "$hit"
  done < <(grep -rnE "$JS_RE" "$d" --include='*.ts' --include='*.tsx' --include='*.js' --include='*.jsx' 2>/dev/null || true)
  while IFS= read -r hit; do
    [[ -z "$hit" ]] && continue
    report "$hit"
  done < <(grep -rnE "$PY_RE" "$d" --include='*.py' 2>/dev/null || true)
done

echo "—"
echo "Kết quả / Result: $errors vi phạm ranh giới (lib phụ thuộc app)."
if [[ $STRICT -eq 1 && $errors -gt 0 ]]; then
  echo "✗ FAIL (strict): lõi tái dùng đang phụ thuộc app → khó trích xuất."
  exit 1
fi
echo "✓ OK."
