#!/usr/bin/env bash
#
# check-grounding.sh — Chống HALLUCINATION: mỗi item DOWNSTREAM phải TRÍCH NGUỒN upstream.
# check-traceability lo top-down (mỗi REQ có SRS...); script này lo BOTTOM-UP: một item
# SRS/ARC/DD/TC mà KHÔNG trích ID upstream = bịa ra, không có gốc → chặn.
# Escape: gắn chữ `inferred` vào item để đánh dấu "suy luận có chủ đích, cần người duyệt".
#
set -uo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"   # đường dẫn v-model dùng chung
[[ -d "$D" ]] || { echo "ℹ Không có v-model — bỏ qua."; exit 0; }

STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
errors=0
err() { echo "  ✗ $1"; errors=$((errors + 1)); }

echo "→ Grounding: mỗi item downstream phải trích nguồn upstream"

# Table rows: | DN-### | ... | ... UP-### ... |
ground_row() {  # $1=file $2=downstream_prefix $3=upstream_prefix
  [[ -f "$1" ]] || return 0
  while IFS=: read -r ln content; do
    [[ -z "${content:-}" ]] && continue
    grep -qiE "inferred" <<<"$content" && continue
    grep -qE "$3-[0-9]{3}" <<<"$content" && continue
    err "$1:$ln — $2 item không trích nguồn $3-### (ungrounded; nếu cố ý → gắn 'inferred')"
  done < <(grep -nE "^\| *$2-[0-9]{3}" "$1")
}

# Per-item blocks: '### DD-###' ... đến '### ' kế tiếp
ground_block() {  # $1=file $2=downstream_prefix $3=upstream_prefix
  [[ -f "$1" ]] || return 0
  local id blk
  for id in $(grep -oE "^### $2-[0-9]{3}" "$1" | grep -oE "$2-[0-9]{3}" | sort -u); do
    blk="$(awk -v id="$id" 'BEGIN{re="^### " id "([: ]|$)"} $0~re{f=1;print;next} f&&/^### /{f=0} f' "$1")"
    grep -qiE "inferred" <<<"$blk" && continue
    grep -qE "$3-[0-9]{3}" <<<"$blk" || err "$1: $id ($2) không trích nguồn $3-### (ungrounded)"
  done
}

ground_row  "$SRS" SRS REQ    # SRS phải trích REQ
ground_row  "$NFR" NFR REQ    # NFR phải trích REQ (ASPICE 4.0: NFR cũng là requirement, trace 2 chiều)
ground_row  "$SAD" ARC SRS    # ARC phải trích SRS
ground_block "$DDD" DD  ARC    # DD phải trích ARC
ground_row  "$UT_DOC"  UT  DD     # Unit Test phải trích DD
ground_row  "$IT_DOC"  IT  ARC    # Integration Test phải trích ARC
ground_row  "$QT_DOC"  QT  SRS    # SW-Qualification Test phải trích SRS
ground_row  "$AT_DOC"  AT  REQ    # Acceptance Test phải trích REQ

echo "—"
echo "Kết quả: $errors item ungrounded."
if [[ $STRICT -eq 1 && $errors -gt 0 ]]; then echo "✗ FAIL (strict): có item không trích nguồn upstream."; exit 1; fi
echo "✓ OK."
exit 0
