#!/usr/bin/env bash
#
# post-edit-check.sh — TẦNG 0: bắt lỗi NGAY KHI agent sửa file (PostToolUse hook của Claude Code),
# không đợi tới pre-commit. Catch violations at edit-time, not commit-time.
#
# Cách hoạt động: .claude/settings.json gọi script này sau mỗi Write/Edit; nhận JSON qua stdin
# (tool_input.file_path), route theo loại file → chạy các check NHANH liên quan. Fail → exit 2
# + stderr: Claude Code đưa lỗi lại cho agent ngay trong phiên để sửa liền (rẻ hơn nhiều so với
# bị pre-commit chặn sau đó — và giảm cám dỗ bypass).
#
# CHỈ chạy check tất định & nhanh (grep-level): i18n / grounding / traceability / suppressions /
# code-size. KHÔNG lint/test/LLM ở đây (chậm — để pre-commit/CI/on-demand).
# Opt-out theo project: .harness-config HOOK_EDIT_CHECKS=0.
#
set -uo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

HOOK_EDIT_CHECKS="${HOOK_EDIT_CHECKS:-1}"
[[ -f .harness-config ]] && source .harness-config
[[ "$HOOK_EDIT_CHECKS" == "1" ]] || exit 0

FILE="$(python3 -c 'import json,sys
try: print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))
except Exception: print("")' 2>/dev/null || true)"
[[ -n "$FILE" ]] || exit 0

case "$FILE" in
  */locales/*.json)          CHECKS=(check-i18n) ;;
  */v-model/*.md)            CHECKS=(check-grounding check-traceability) ;;
  *.py|*.ts|*.tsx|*.js|*.jsx) CHECKS=(check-suppressions check-code-size) ;;
  *) exit 0 ;;
esac

out=""; failed=0
for c in "${CHECKS[@]}"; do
  s="scripts/$c.sh"; [[ -f "$s" ]] || continue
  if ! o="$(bash "$s" --strict 2>&1)"; then
    failed=1
    out+="--- $c ---"$'\n'"$o"$'\n'
  fi
done

if [[ $failed -eq 1 ]]; then
  {
    echo "⛔ Tầng 0 (edit-time) — file vừa sửa làm check fail. SỬA NGAY trước khi làm tiếp"
    echo "   (đừng để dồn tới pre-commit; KHÔNG bypass):"
    echo "$out"
  } >&2
  exit 2
fi
exit 0
