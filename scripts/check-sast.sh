#!/usr/bin/env bash
#
# check-sast.sh — Phân tích tĩnh bảo mật code (SAST). / Static security analysis.
#   - Python: bandit (Apache-2.0)
#   - JS/TS:  eslint + eslint-plugin-security (MIT) — chạy qua check-lint nếu đã cấu hình.
# Bỏ qua êm nếu tool chưa cài.
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
fails=0

echo "→ SAST (phân tích tĩnh bảo mật)"

# --- Python: bandit ---
if [[ -d backend-python/app ]]; then
  if command -v bandit >/dev/null 2>&1; then
    echo "  [py] bandit -r backend-python/app"
    bandit -q -r backend-python/app || { echo "  ✗ bandit: có cảnh báo bảo mật"; fails=$((fails+1)); }
  else
    echo "  ⚠ [py] chưa cài bandit — bỏ qua. Cài: pip install bandit"
  fi
fi

# --- JS/TS: eslint security (cần cấu hình eslint, xem P2) ---
if [[ -f frontend/package.json || -f backend/package.json ]]; then
  if command -v npx >/dev/null 2>&1 && { [[ -f .eslintrc.json || -f eslint.config.js || -f frontend/.eslintrc.json ]]; }; then
    echo "  [js] eslint (gồm rule security nếu đã bật plugin)"
    npx --no-install eslint . 2>/dev/null || { echo "  ✗ eslint: có vấn đề"; fails=$((fails+1)); }
  else
    echo "  ⚠ [js] chưa cấu hình eslint (sẽ có ở P2) — bỏ qua."
  fi
fi

echo "—"
echo "Kết quả: $fails nguồn có cảnh báo."
if [[ $STRICT -eq 1 && $fails -gt 0 ]]; then echo "✗ FAIL (strict)."; exit 1; fi
echo "✓ OK (hoặc đã bỏ qua tool thiếu)."
exit 0
