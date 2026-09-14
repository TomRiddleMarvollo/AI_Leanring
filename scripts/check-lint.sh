#!/usr/bin/env bash
#
# check-lint.sh — Lint & format check. Tool free MIT/Apache; bỏ qua êm nếu chưa cài.
#   - Python: ruff (MIT) — lint + format check (thay black; gồm cả rule bảo mật "S").
#   - JS/TS:  eslint + prettier (MIT).
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
fails=0

echo "→ Lint & format"

# --- Python: ruff ---
if [[ -d backend-python ]]; then
  if command -v ruff >/dev/null 2>&1; then
    echo "  [py] ruff check + format --check"
    ruff check backend-python || { echo "  ✗ ruff: có vấn đề"; fails=$((fails+1)); }
    ruff format --check backend-python || { echo "  ✗ ruff format: chưa format"; fails=$((fails+1)); }
  else
    echo "  ⚠ [py] chưa cài ruff — bỏ qua. Cài: pip install ruff"
  fi
fi

# --- JS/TS: eslint + prettier ---
if [[ -f eslint.config.js || -f .eslintrc.json ]] && command -v npx >/dev/null 2>&1; then
  echo "  [js] eslint"
  npx --no-install eslint . || { echo "  ✗ eslint: có vấn đề"; fails=$((fails+1)); }
fi
if [[ -f .prettierrc.json ]] && command -v npx >/dev/null 2>&1; then
  echo "  [js] prettier --check"
  npx --no-install prettier --check . || { echo "  ✗ prettier: chưa format"; fails=$((fails+1)); }
fi

echo "—"
echo "Kết quả: $fails nguồn có vấn đề."
if [[ $STRICT -eq 1 && $fails -gt 0 ]]; then echo "✗ FAIL (strict)."; exit 1; fi
echo "✓ OK (hoặc đã bỏ qua tool thiếu)."
exit 0
