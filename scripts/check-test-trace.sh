#!/usr/bin/env bash
#
# check-test-trace.sh — Test DOCS ↔ Test CODE: ca test đã tài liệu hoá phải có TEST CODE THẬT mang ID.
# Khép vòng V với thực tại: check-traceability lo doc↔doc; script này lo doc↔code-test
# (một UT-### chỉ nằm trong test-cases.md mà không có test code = "test trên giấy").
#
#   - UT-### → PHẢI có test code tham chiếu ID (err — chặn).
#   - IT/QT-### → NÊN có (warn — có thể là bench/e2e tay, tuỳ dự án).
#   - AT-### → bỏ qua (nghiệm thu người dùng, thường thao tác tay).
#   - Ngược lại: ID trong test code mà không định nghĩa trong tài liệu → err (link đứt).
#
# Escape hatch (giống `inferred` của grounding): dòng ca test chứa `_(TODO` (chưa claim xong)
# hoặc chữ `manual` (test tay có chủ đích, cần người duyệt) → bỏ qua ca đó.
# Opt-out cả check theo project: .harness-config REQUIRE_TEST_CODE=0.
# Việc CHẠY test & coverage là của check-test-coverage.sh — script này chỉ ép tồn tại + trace.
#
set -uo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"   # đường dẫn v-model dùng chung
[[ -d "$D" ]] || { echo "ℹ Không có v-model — bỏ qua."; exit 0; }

REQUIRE_TEST_CODE="${REQUIRE_TEST_CODE:-1}"
[[ -f .harness-config ]] && source .harness-config
[[ "$REQUIRE_TEST_CODE" == "1" ]] || { echo "ℹ REQUIRE_TEST_CODE=0 — bỏ qua check test-trace."; exit 0; }

STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
errors=0; warns=0
err()  { echo "  ✗ $1"; errors=$((errors + 1)); }
warn() { echo "  ⚠ $1"; warns=$((warns + 1)); }

# Test code = file test thật trong source tree (không tính tài liệu v-model).
TEST_FILES="$(find frontend backend backend-python shared packages -type f \
  \( -name '*.test.*' -o -name '*.spec.*' -o -name 'test_*.py' -o -name '*_test.py' -o -path '*/tests/*' \) \
  2>/dev/null | grep -E '\.(py|ts|tsx|js|jsx)$' || true)"

echo "→ Test-trace: ca test tài liệu hoá ↔ test code thật"

in_test_code() { [[ -n "$TEST_FILES" ]] && grep -qE "(^|[^0-9A-Za-z])$1([^0-9]|$)" $TEST_FILES 2>/dev/null; }

# Các ca ĐÃ claim (bỏ dòng TODO/manual) trong tài liệu phải có test code.
check_level() {  # $1=doc $2=prefix $3=err|warn
  [[ -f "$1" ]] || return 0
  local id
  for id in $(grep -E "^\| *$2-[0-9]{3}" "$1" | grep -viE '_\(TODO|manual' | grep -oE "$2-[0-9]{3}" | sort -u); do
    if ! in_test_code "$id"; then
      if [[ "$3" == "err" ]]; then
        err "$id có trong $1 nhưng KHÔNG có test code nào mang ID này (test trên giấy — viết test thật, hoặc đánh dấu 'manual' + người duyệt)."
      else
        warn "$id ($1) chưa có test code mang ID — nếu là bench/test tay thì đánh dấu 'manual'."
      fi
    fi
  done
}
check_level "$UT_DOC" UT err
check_level "$IT_DOC" IT warn
check_level "$QT_DOC" QT warn

# Link đứt ngược: ID trong test code phải được định nghĩa trong tài liệu tương ứng.
if [[ -n "$TEST_FILES" ]]; then
  for pair in "UT:$UT_DOC" "IT:$IT_DOC" "QT:$QT_DOC"; do
    p="${pair%%:*}"; doc="${pair#*:}"
    for id in $(grep -hoE "$p-[0-9]{3}" $TEST_FILES 2>/dev/null | sort -u); do
      grep -qE "(^|[^0-9A-Za-z])$id([^0-9]|$)" "$doc" 2>/dev/null \
        || err "Link đứt: $id có trong test code nhưng không định nghĩa trong $doc."
    done
  done
fi

echo "—"
echo "Kết quả: $errors lỗi, $warns cảnh báo."
if [[ $STRICT -eq 1 && $errors -gt 0 ]]; then echo "✗ FAIL (strict): tài liệu test và test code lệch nhau."; exit 1; fi
echo "✓ OK."
exit 0
