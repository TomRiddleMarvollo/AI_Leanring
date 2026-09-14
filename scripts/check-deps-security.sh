#!/usr/bin/env bash
#
# check-deps-security.sh — Quét lỗ hổng (CVE) trong dependencies.
# Scan dependencies for known vulnerabilities. Tools dùng đều free, license Apache/MIT.
#   - Python: pip-audit (Apache-2.0)
#   - Node:   npm audit (built-in) hoặc osv-scanner (Apache-2.0)
# Bỏ qua êm nếu tool chưa cài (CI sẽ cài đủ).
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
fails=0

echo "→ Quét lỗ hổng dependency / Dependency vulnerability scan"

# --- Python ---
if [[ -f backend-python/requirements.txt || -f backend-python/pyproject.toml ]]; then
  if command -v pip-audit >/dev/null 2>&1; then
    echo "  [py] pip-audit (backend-python)"
    ( cd backend-python && pip-audit ) || { echo "  ✗ pip-audit: có lỗ hổng"; fails=$((fails+1)); }
  else
    echo "  ⚠ [py] chưa cài pip-audit — bỏ qua. Cài: pip install pip-audit"
  fi
fi

# --- Node ---
for d in frontend backend; do
  [[ -f "$d/package.json" ]] || continue
  if command -v osv-scanner >/dev/null 2>&1; then
    echo "  [node] osv-scanner ($d)"
    osv-scanner --lockfile="$d/package-lock.json" 2>/dev/null || { echo "  ✗ osv: có lỗ hổng ($d)"; fails=$((fails+1)); }
  elif command -v npm >/dev/null 2>&1; then
    echo "  [node] npm audit ($d)"
    ( cd "$d" && npm audit --omit=dev ) || { echo "  ✗ npm audit: có lỗ hổng ($d)"; fails=$((fails+1)); }
  else
    echo "  ⚠ [node] chưa có osv-scanner/npm — bỏ qua ($d)."
  fi
done

echo "—"
echo "Kết quả: $fails nguồn có lỗ hổng."
if [[ $STRICT -eq 1 && $fails -gt 0 ]]; then echo "✗ FAIL (strict)."; exit 1; fi
echo "✓ OK (hoặc đã bỏ qua tool thiếu)."
exit 0
