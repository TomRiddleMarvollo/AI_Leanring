#!/usr/bin/env bash
#
# verify-all.sh — MỘT lệnh cho Definition of Done: chạy đủ gen + check, in SCORECARD.
# One command to run every generator + check and print a scorecard.
#
# Vấn đề: AGENTS.md từng bắt agent nhớ ~7 lệnh — một lệnh thì luôn được chạy, bảy lệnh thì quên ba.
#
#   bash scripts/verify-all.sh          # gen + check tất định + heuristic (nhanh, không tool ngoài)
#   bash scripts/verify-all.sh --full   # thêm tool ngoài (lint/SAST/deps/coverage) + LLM delta (nếu có)
#
# Ký hiệu: ✓ đạt · ✗ FAIL (tầng tất định → exit 1) · ⚠ cảnh báo (không chặn) · ⊘ bỏ qua (thiếu script/tool).
# Log đầy đủ ghi ra file tạm (in đường dẫn cuối); chạy lại từng check riêng để xem chi tiết.
#
set -uo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

MODE=fast; [[ "${1:-}" == "--full" ]] && MODE=full
LOG="$(mktemp -t verify-all)"
pass=0; failn=0; warnn=0; skipn=0
FAILED=""

say()  { printf '%s\n' "$1"; }
mark() { # $1=icon $2=name $3=note
  printf '  %s %-28s%s\n' "$1" "$2" "${3:+ $3}"
}

run_gen() {  # generator: lỗi không chặn (⚠)
  local n="$1" s="scripts/$1.sh"
  [[ -f "$s" ]] || { mark "⊘" "$n" "(không có)"; skipn=$((skipn+1)); return; }
  if bash "$s" >>"$LOG" 2>&1; then mark "✓" "$n"; pass=$((pass+1))
  else mark "⚠" "$n" "(gen lỗi — xem log)"; warnn=$((warnn+1)); fi
}

run_hard() {  # check tất định: fail → chặn (✗, exit 1 cuối cùng)
  local n="$1" s="scripts/$1.sh" out rc nw first
  [[ -f "$s" ]] || { mark "⊘" "$n" "(không có)"; skipn=$((skipn+1)); return; }
  out="$(bash "$s" --strict 2>&1)"; rc=$?
  printf '===== %s =====\n%s\n' "$n" "$out" >>"$LOG"
  if [[ $rc -eq 0 ]]; then
    nw="$(grep -c '⚠' <<<"$out" || true)"
    if [[ "$nw" -gt 0 ]]; then mark "✓" "$n" "(kèm $nw cảnh báo)"; warnn=$((warnn+nw))
    else mark "✓" "$n"; fi
    pass=$((pass+1))
  else
    first="$(grep -m1 '✗' <<<"$out" | sed 's/^ *//')"
    mark "✗" "$n" "${first:+— $first}"
    failn=$((failn+1)); FAILED+=" $n"
  fi
}

run_soft() {  # tool ngoài / heuristic độc lập: fail → chỉ ⚠
  local n="$1" s="scripts/$1.sh"
  [[ -f "$s" ]] || { mark "⊘" "$n" "(không có)"; skipn=$((skipn+1)); return; }
  if bash "$s" >>"$LOG" 2>&1; then mark "✓" "$n"; pass=$((pass+1))
  else mark "⚠" "$n" "(xem log / thiếu tool)"; warnn=$((warnn+1)); fi
}

say "════ verify-all — Definition of Done scorecard (mode: $MODE) ════"

say "— Sinh tài liệu (gen) —"
for g in gen-traceability gen-ground-truth gen-code-trace gen-review-checklist; do run_gen "$g"; done

say "— Tất định (FAIL là chặn — đúng bộ pre-commit) —"
for c in check-secrets check-i18n check-types check-lib-boundaries check-code-size \
         check-fn-doc check-api-surface check-circular-deps \
         check-traceability check-grounding check-completeness check-code-doc-coverage \
         check-review-checklists check-suppressions check-test-trace; do
  run_hard "$c"
done

say "— Heuristic / tool ngoài (cảnh báo, không chặn) —"
for c in check-docs check-doc-staleness; do run_soft "$c"; done
if [[ "$MODE" == "full" ]]; then
  for c in check-lint check-sast check-deps-security check-test-coverage; do run_soft "$c"; done
  say "— LLM (Tầng 2, tuỳ chọn) —"
  if [[ -f scripts/review-docs-llm.sh ]]; then
    if bash scripts/review-docs-llm.sh --diff >>"$LOG" 2>&1; then mark "✓" "review-docs-llm --diff"; pass=$((pass+1))
    else mark "⚠" "review-docs-llm --diff" "(xem log)"; warnn=$((warnn+1)); fi
  fi
fi

say "—"
say "KẾT QUẢ: $pass ✓ · $failn ✗ · $warnn ⚠ · $skipn ⊘   (log: $LOG)"
if [[ $failn -gt 0 ]]; then
  say "✗ CHƯA ĐẠT Definition of Done — sửa:$FAILED"
  first_failed="${FAILED## }"; first_failed="${first_failed%% *}"
  say "  Chạy riêng từng check để xem chi tiết, vd: bash scripts/$first_failed.sh --strict"
  exit 1
fi
say "✓ ĐẠT tầng tất định. Rà nốt ⚠ (nếu có) trước khi giao."
exit 0
