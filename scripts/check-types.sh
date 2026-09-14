#!/usr/bin/env bash
#
# check-types.sh — Type-check TypeScript (tsc --noEmit). CHẶN.
#
# Vì sao tách khỏi check-lint (eslint): eslint KHÔNG bắt lỗi kiểu. Lỗi `TS2345` từng làm
# `tsc && vite build` đỏ mà cổng chỉ chạy eslint nên LỌT tới tận build (OCTA-127/139). Đây là
# lớp lỗi build-break — phải chặn ở cổng tất định, không để soft/--full.
#
# Bỏ qua ÊM nếu chưa cài deps (frontend/node_modules) — CI/máy chưa `npm ci` không false-fail;
# nhưng nơi CÓ deps (dev + CI chuẩn) thì lỗi type CHẶN commit.
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
fails=0

echo "→ Type-check (tsc --noEmit)"

if [[ -f frontend/tsconfig.json ]]; then
  if [[ -x frontend/node_modules/.bin/tsc ]]; then
    echo "  [ts] frontend"
    ( cd frontend && node_modules/.bin/tsc --noEmit ) \
      || { echo "  ✗ tsc: có lỗi type (eslint KHÔNG thấy — sửa trước khi commit)"; fails=$((fails+1)); }
  else
    echo "  ⚠ [ts] chưa cài deps (frontend/node_modules/.bin/tsc) — bỏ qua. Cài: npm --prefix frontend ci"
  fi
fi

echo "—"
echo "Kết quả: $fails project có lỗi type."
if [[ $STRICT -eq 1 && $fails -gt 0 ]]; then echo "✗ FAIL (strict): lỗi type."; exit 1; fi
echo "✓ OK (hoặc bỏ qua tsc thiếu)."
exit 0
