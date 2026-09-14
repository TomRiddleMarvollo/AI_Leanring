#!/usr/bin/env bash
#
# session-journal-reminder.sh — Stop hook (Claude Code): nhắc agent GHI agent-journal cuối phiên
# nếu có thay đổi thực chất mà `JOURNAL.md` chưa được đụng tới. Remind agent to journal at stop.
#
# Cách hoạt động: Claude Code gọi khi agent kết thúc lượt trả lời; nhận JSON qua stdin. Nếu cây
# làm việc CÓ thay đổi (tracked hoặc untracked) NHƯNG không có gì dưới agent-journal/journal/ →
# in nhắc ra stderr + exit 2, Claude Code đưa nhắc lại cho agent để ghi entry tổng kết rồi mới dừng.
#
# CHỐNG LẶP: nếu đang trong vòng continuation do chính stop hook (stop_hook_active=true) → exit 0.
# Nhắc MỀM: chỉ chặn khi có việc chưa ghi; agent ghi journal xong (JOURNAL.md đổi) → lần sau thôi nhắc.
#
# Chỉ áp dụng khi dự án có agent-journal/. Opt-out: .harness-config HOOK_JOURNAL_REMINDER=0.
#
set -uo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT" || exit 0

[[ -d agent-journal ]] || exit 0   # dự án chưa có module → không nhắc

HOOK_JOURNAL_REMINDER="${HOOK_JOURNAL_REMINDER:-1}"
[[ -f .harness-config ]] && source .harness-config
[[ "$HOOK_JOURNAL_REMINDER" == "1" ]] || exit 0

# stdin JSON — nếu đang là continuation do stop hook trước đó → dừng (chống lặp vô hạn)
INPUT="$(cat 2>/dev/null || true)"
active="$(printf '%s' "$INPUT" | python3 -c 'import json,sys
try: print(json.load(sys.stdin).get("stop_hook_active", False))
except Exception: print(False)' 2>/dev/null || echo False)"
[[ "$active" == "True" ]] && exit 0

# Có thay đổi nào trong cây làm việc không? (tracked sửa + untracked mới; .gitignore đã lọc rác)
changed="$(git status --porcelain 2>/dev/null | sed 's/^...//' || true)"
[[ -n "$changed" ]] || exit 0   # tay sạch → không có gì để ghi

# Nếu đã có thay đổi dưới agent-journal/journal/ → coi như đã ghi rồi, thôi nhắc
if printf '%s\n' "$changed" | grep -q 'agent-journal/journal/'; then
  exit 0
fi

# Có việc thực chất mà journal chưa đụng → nhắc (chặn 1 lần)
{
  echo "📓 Nhắc cuối phiên — agent-journal chưa được cập nhật cho phiên này."
  echo "   Nếu phiên có checkpoint đáng nhớ (quyết định / lỗi gặp / cách khắc phục /"
  echo "   hiểu ra cách làm đúng / tool mới), hãy append MỘT entry vào"
  echo "   agent-journal/journal/JOURNAL.md (định dạng: agent-journal/README.md) rồi dừng."
  echo "   Nếu KHÔNG có gì đáng ghi, cứ dừng lại — nhắc này sẽ không lặp."
} >&2
exit 2
