#!/usr/bin/env bash
#
# check-traceability.sh — Ép tính nhất quán của bộ tài liệu SDLC (V-model).
# Enforce consistency across the SDLC documentation set.
#
# CHẶN (error, exit 1 ở --strict):
#   - Trái (phân rã): REQ thiếu SRS · SRS thiếu ARC · ARC thiếu DD
#   - Phải (kiểm chứng V-model): DD thiếu UT · ARC thiếu IT · SRS thiếu QT · REQ thiếu AT (Acceptance)
#   - NFR thiếu test (không test-cases nào phủ NFR-###).
#   - Link đứt: một ID được tham chiếu nhưng không định nghĩa ở tài liệu gốc.
# CẢNH BÁO (warn, không chặn):
#   - DD chưa được code tham chiếu (comment DD-###).
#   - Staleness: code commit sau tài liệu (nghi tài liệu cũ).
#
# Dùng / Usage:
#   bash scripts/check-traceability.sh            # cảnh báo
#   bash scripts/check-traceability.sh --strict   # CI: lỗi -> exit 1
#
set -euo pipefail

source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"   # đường dẫn v-model + ids_in/has_id/in_list dùng chung

[[ -d "$D" ]] || { echo "ℹ Không có $D — bỏ qua kiểm tra truy vết."; exit 0; }

STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
errors=0; warns=0
err()  { echo "  ✗ $1"; errors=$((errors + 1)); }
warn() { echo "  ⚠ $1"; warns=$((warns + 1)); }


echo "→ Kiểm tra truy vết SDLC / Checking SDLC traceability in: $ROOT"

REQ_DEF="$(ids_in "$HLR" REQ)"
SRS_DEF="$(ids_in "$SRS" SRS)"
NFR_DEF="$(ids_in "$NFR" NFR)"
ARC_DEF="$(ids_in "$SAD" ARC)"
DD_DEF="$(ids_in "$DDD" DD)"

# --- 1) Độ phủ (gaps -> ERROR) ---
# Trái (phân rã): REQ→SRS→ARC→DD
for id in $REQ_DEF; do
  has_id "$SRS" "$id" || err "$id (HLR) chưa có Specification (SRS) nào tham chiếu."
  has_id "$AT_DOC"  "$id" || err "$id (HLR) chưa có Acceptance Test (AT) nào nghiệm thu."
done
for id in $SRS_DEF; do
  has_id "$SAD" "$id" || err "$id (SRS) chưa có Architecture (ARC) nào hiện thực."
  has_id "$QT_DOC"  "$id" || err "$id (SRS) chưa có SW-Qualification Test (QT) nào kiểm chứng."
done
for id in $ARC_DEF; do
  has_id "$DDD" "$id" || err "$id (ARC) chưa có Detailed Design (DD) nào chi tiết hóa."
  has_id "$IT_DOC"  "$id" || err "$id (ARC) chưa có Integration Test (IT) nào kiểm chứng."
done
# Phải (kiểm chứng V-model): DD→UT
for id in $DD_DEF; do
  has_id "$UT_DOC" "$id" || err "$id (DD) chưa có Unit Test (UT) nào kiểm chứng."
done
# NFR: mỗi NFR phải được ≥1 test (UT/IT/QT/AT) phủ
for id in $NFR_DEF; do
  { has_id "$UT_DOC" "$id" || has_id "$IT_DOC" "$id" || has_id "$QT_DOC" "$id" || has_id "$AT_DOC" "$id"; } \
    || err "$id (NFR) chưa có test nào kiểm chứng (thêm vào một test-cases)."
done
# NFR: kiến trúc phải thoả cả phi chức năng (ASPICE 4.0 SWE.2 — architecture satisfies functional AND non-functional).
for id in $NFR_DEF; do
  has_id "$SAD" "$id" || err "$id (NFR) chưa được Architecture (SAD) giải quyết (thêm quyết định/thành phần nhắc $id)."
done

# --- 2) Link đứt (referenced nhưng không định nghĩa -> ERROR) ---
for id in $(ids_in "$SRS" REQ); do
  in_list "$id" "$REQ_DEF" || err "Link đứt: $id tham chiếu trong SRS nhưng không định nghĩa trong HLR."
done
for id in $( { ids_in "$SAD" SRS; ids_in "$QT_DOC" SRS; } | sort -u ); do
  in_list "$id" "$SRS_DEF" || err "Link đứt: $id tham chiếu trong SAD/QT nhưng không định nghĩa trong SRS."
done
for id in $( { ids_in "$DDD" ARC; ids_in "$IT_DOC" ARC; } | sort -u ); do
  in_list "$id" "$ARC_DEF" || err "Link đứt: $id tham chiếu trong DDD/IT nhưng không định nghĩa trong SAD."
done
for id in $(ids_in "$UT_DOC" DD); do
  in_list "$id" "$DD_DEF" || err "Link đứt: $id tham chiếu trong UT nhưng không định nghĩa trong DDD."
done
for id in $(ids_in "$AT_DOC" REQ); do
  in_list "$id" "$REQ_DEF" || err "Link đứt: $id tham chiếu trong AT nhưng không định nghĩa trong HLR."
done
for id in $(ids_in "$NFR" REQ); do
  in_list "$id" "$REQ_DEF" || err "Link đứt: $id tham chiếu trong NFR nhưng không định nghĩa trong HLR."
done
for id in $( { ids_in "$UT_DOC" NFR; ids_in "$IT_DOC" NFR; ids_in "$QT_DOC" NFR; ids_in "$AT_DOC" NFR; } | sort -u ); do
  in_list "$id" "$NFR_DEF" || err "Link đứt: $id tham chiếu trong test nhưng không định nghĩa trong NFR."
done

# --- 3) DD <-> code (WARN) ---
for id in $DD_DEF; do
  grep -rqE "\\b$id\\b" $SRC_DIRS 2>/dev/null || warn "$id (DD) chưa được code tham chiếu (thêm comment '$id')."
done

# --- 4) Staleness: code commit sau tài liệu (WARN, cần git) ---
if git rev-parse --git-dir >/dev/null 2>&1; then
  doc_t="$(git log -1 --format=%ct -- "$D" 2>/dev/null || echo 0)"
  code_t="$(git log -1 --format=%ct -- $SRC_DIRS 2>/dev/null || echo 0)"
  if [[ "${code_t:-0}" -gt "${doc_t:-0}" && "${doc_t:-0}" -gt 0 ]]; then
    warn "Code được commit SAU tài liệu SDLC — rà lại xem tài liệu còn đúng không."
  fi
fi

echo "—"
echo "Kết quả / Result: $errors lỗi, $warns cảnh báo."
if [[ $STRICT -eq 1 && $errors -gt 0 ]]; then
  echo "✗ FAIL (strict): truy vết có $errors lỗi."
  exit 1
fi
echo "✓ OK — cảnh báo không chặn."
