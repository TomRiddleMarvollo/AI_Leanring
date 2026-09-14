#!/usr/bin/env bash
#
# gen-traceability.sh — Sinh bảng độ phủ truy vết vào v-model/_traceability/TRACEABILITY.md
# (phần giữa hai mốc AUTO-TRACE). / Generate the coverage matrix.
#
set -euo pipefail

source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"   # đường dẫn v-model + ids_in/has_id dùng chung
OUT="$D/_traceability/TRACEABILITY.md"

[[ -f "$OUT" ]] || { echo "✗ Không thấy $OUT"; exit 1; }
grep -q 'AUTO-TRACE:START' "$OUT" || { echo "✗ $OUT thiếu mốc AUTO-TRACE"; exit 1; }

mark()   { has_id "$1" "$2" && echo "✓" || echo "✗"; }
mark_code() { grep -rqE "(^|[^0-9A-Za-z])$1([^0-9]|$)" $SRC_DIRS 2>/dev/null && echo "✓" || echo "⚠"; }

TMP="$(mktemp)"
{
  echo "_Sinh tự động — $(git rev-list --count HEAD 2>/dev/null || echo 0) commit. Đừng sửa tay._"
  echo
  echo "**Requirements → Specification / Acceptance Test**"
  echo "| REQ | có SRS | có AT |"; echo "|-----|--------|-------|"
  for id in $(ids_in "$HLR" REQ); do echo "| $id | $(mark "$SRS" "$id") | $(mark "$AT_DOC" "$id") |"; done
  echo
  echo "**NFR ↔ REQ (trace lên) / Test (trace xuống)**"
  echo "| NFR | ↑ REQ | có test |"; echo "|-----|-------|---------|"
  for id in $(ids_in "$NFR" NFR); do
    m="✗"; for f in "$UT_DOC" "$IT_DOC" "$QT_DOC" "$AT_DOC"; do mark "$f" "$id" | grep -q '✓' && m="✓"; done
    req="$(grep -E "^\| *$id" "$NFR" 2>/dev/null | grep -oE 'REQ-[0-9]{3}' | head -1)"
    echo "| $id | ${req:-✗} | $m |"
  done
  echo
  echo "**Specification → Architecture / SW-Qualification Test**"
  echo "| SRS | có ARC | có QT |"; echo "|-----|--------|-------|"
  for id in $(ids_in "$SRS" SRS); do echo "| $id | $(mark "$SAD" "$id") | $(mark "$QT_DOC" "$id") |"; done
  echo
  echo "**Architecture → Detailed Design / Integration Test**"
  echo "| ARC | có DD | có IT |"; echo "|-----|-------|-------|"
  for id in $(ids_in "$SAD" ARC); do echo "| $id | $(mark "$DDD" "$id") | $(mark "$IT_DOC" "$id") |"; done
  echo
  echo "**Detailed Design → Code / Unit Test**"
  echo "| DD | trong code | có UT |"; echo "|----|------------|-------|"
  for id in $(ids_in "$DDD" DD); do echo "| $id | $(mark_code "$id") | $(mark "$UT_DOC" "$id") |"; done
  echo
  echo "**Unit Test ↔ Software Unit (ASPICE 4.0 SWE.4 — dẫn xuất: UT↔DD ⋈ code @trace DD)**"
  echo "| UT | qua DD | Unit (file code có \`@trace DD\`) |"; echo "|----|--------|-------------------------------|"
  while IFS= read -r row; do
    ut="$(grep -oE 'UT-[0-9]{3}' <<<"$row" | head -1)"; [[ -z "$ut" ]] && continue
    for dd in $(grep -oE 'DD-[0-9]{3}' <<<"$row" | sort -u); do
      files="$(grep -rlE "@trace[^0-9A-Za-z]*.*(^|[^0-9A-Za-z])$dd([^0-9]|$)" $SRC_DIRS 2>/dev/null | sed 's/^/`/;s/$/`/' | tr '\n' ' ')"
      echo "| $ut | $dd | ${files:-⚠ chưa có code @trace $dd} |"
    done
  done < <(grep -E '^\| *UT-[0-9]{3}' "$UT_DOC" 2>/dev/null)
} > "$TMP"

awk -v f="$TMP" '
  BEGIN { while ((getline l < f) > 0) b = b l ORS }
  /AUTO-TRACE:START/ { print; printf "%s", b; insec=1; next }
  /AUTO-TRACE:END/   { insec=0 }
  !insec
' "$OUT" > "$OUT.tmp" && mv "$OUT.tmp" "$OUT"
rm -f "$TMP"
echo "✓ Đã cập nhật $OUT"
