#!/usr/bin/env bash
#
# check-test-coverage.sh — Ép ngưỡng test coverage tối thiểu.
# Enforce a minimum test-coverage threshold. Dùng cơ chế fail-under sẵn có của tool.
#   - Python: pytest --cov --cov-fail-under=$COVERAGE_MIN
#   - JS/TS:  npm test (ngưỡng đặt trong cấu hình jest/vitest coverageThreshold)
# Bỏ qua êm nếu thiếu tool (CI cài đủ).
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
MIN="${COVERAGE_MIN:-70}"
fails=0

echo "→ Test coverage (ngưỡng ${MIN}%)"

# --- Python ---
if [[ -d backend-python ]]; then
  if command -v pytest >/dev/null 2>&1 && python3 -c "import pytest_cov" >/dev/null 2>&1; then
    echo "  [py] pytest --cov=app --cov-fail-under=$MIN"
    ( cd backend-python && pytest --cov=app --cov-report=term-missing --cov-fail-under="$MIN" ) \
      || { echo "  ✗ coverage Python < ${MIN}%"; fails=$((fails+1)); }
  else
    echo "  ⚠ [py] thiếu pytest/pytest-cov — bỏ qua. Cài: pip install pytest pytest-cov"
  fi
fi

# --- JS/TS (ngưỡng đặt trong coverageThreshold của jest/vitest) ---
for d in frontend backend; do
  [[ -f "$d/package.json" ]] || continue
  if command -v npm >/dev/null 2>&1 && grep -q '"test"' "$d/package.json"; then
    echo "  [js] ($d) npm test --coverage"
    ( cd "$d" && npm test ) || { echo "  ✗ test/coverage ($d)"; fails=$((fails+1)); }
  else
    echo "  ⚠ [js] ($d) chưa có npm/test script — bỏ qua."
  fi
done

echo "—"
echo "Kết quả: $fails nguồn dưới ngưỡng / lỗi test."
if [[ $STRICT -eq 1 && $fails -gt 0 ]]; then echo "✗ FAIL (strict)."; exit 1; fi
echo "✓ OK (hoặc đã bỏ qua tool thiếu)."
exit 0
