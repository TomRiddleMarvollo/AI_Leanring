#!/usr/bin/env bash
#
# build-lib.sh — Build & verify từng package trong packages/ (Approach B) build độc lập.
# Verify each packages/* builds standalone (= sẵn sàng publish thành thư viện).
# Bỏ qua êm nếu chưa có package hoặc thiếu tool.
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
fails=0; found=0

echo "→ Build thư viện (packages/*)"
[[ -d packages ]] || { echo "  ℹ Chưa có packages/ — bỏ qua."; exit 0; }

for pkg in packages/*/; do
  [[ -d "$pkg" ]] || continue
  if [[ -f "$pkg/package.json" ]]; then
    found=1
    if command -v npm >/dev/null 2>&1; then
      echo "  [node] build $pkg"
      ( cd "$pkg" && npm ci >/dev/null 2>&1 || npm install >/dev/null 2>&1; npm run build ) \
        || { echo "  ✗ build lỗi: $pkg"; fails=$((fails+1)); }
    else
      echo "  ⚠ [node] chưa có npm — bỏ qua $pkg"
    fi
  elif [[ -f "$pkg/pyproject.toml" ]]; then
    found=1
    if python3 -c "import build" >/dev/null 2>&1; then
      echo "  [py] python -m build $pkg"
      ( cd "$pkg" && python3 -m build ) || { echo "  ✗ build lỗi: $pkg"; fails=$((fails+1)); }
    else
      echo "  ⚠ [py] chưa cài 'build' (pip install build) — bỏ qua $pkg"
    fi
  fi
done

echo "—"
[[ $found -eq 0 ]] && echo "  ℹ Không có package nào để build."
echo "Kết quả: $fails package build lỗi."
if [[ $STRICT -eq 1 && $fails -gt 0 ]]; then echo "✗ FAIL (strict)."; exit 1; fi
echo "✓ OK."
exit 0
