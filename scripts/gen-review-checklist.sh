#!/usr/bin/env bash
#
# gen-review-checklist.sh — Sinh phần AUTO của review-checklist mỗi phase:
#   - Mục CỤ THỂ từ ground-truth (mỗi error-code / endpoint / màn hình một dòng).
#   - AUTO-TICK [x] nếu tài liệu phase đã phủ / check máy đã pass; [ ] nếu chưa.
# → checklist sát hệ thống thật + bớt tick bừa. (Base đặc thù phase nằm phía trên mốc AUTO.)
#
set -uo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
[[ -d v-model ]] || { echo "ℹ Không có v-model — bỏ qua."; exit 0; }

HLR=v-model/01-requirement/00-HLR.md
SRS=v-model/02-specification/01-SRS.md
NFR=v-model/02-specification/01b-NFR.md
SAD=v-model/03-architecture/02-SAD.md
DDD=v-model/04-detailed-design/03-DDD.md
UT=v-model/06-unit-test/test-cases.md
IT=v-model/07-integration-test/test-cases.md
QT=v-model/08-sw-qualification-test/test-cases.md
AT=v-model/09-acceptance-test/test-cases.md
UM=v-model/10-user-manual/06-USER-MANUAL.md

tick() {  # tick "x" nếu needle xuất hiện trong MỘT DÒNG có ngữ cảnh thật (≥12 ký tự
          # ngoài chính needle) — tránh tick khống khi chỉ liệt kê ID/key trơ trọi.
  grep -F -- "$2" "$1" 2>/dev/null | awk -v n="${#2}" 'length($0) - n >= 12 {f=1} END{exit !f}' \
    && echo "x" || echo " "
}
ids()   { grep -hoE "$2-[0-9]{3}" "$1" 2>/dev/null | sort -u; }                # liệt kê ID 1 prefix trong file
mcheck(){ bash "scripts/$1.sh" --strict >/dev/null 2>&1 && echo "x" || echo " "; }  # tick nếu check pass

# --- Ground truth (như gen-ground-truth) ---
err_keys() {
  while IFS= read -r f; do
    python3 - "$f" <<'PY'
import json,sys
try:
    for k in (json.load(open(sys.argv[1],encoding="utf-8")).get("errors") or {}): print(k)
except Exception: pass
PY
  done < <(find frontend backend backend-python -path '*/locales/en.json' 2>/dev/null) | sort -u
}
endpoints() {
  grep -rhoE "\.(get|post|put|patch|delete)\((\"[^\"]+\"|'[^']+')" backend backend-python 2>/dev/null \
    | grep -oE "(\"[^\"]+\"|'[^']+')" | tr -d "\"'" | grep -vE '^$' | sort -u
}
screens() {
  find frontend/src/app -type f -name 'page.*' 2>/dev/null | while IFS= read -r p; do
    d="/$(dirname "${p#frontend/src/app/}")"; [[ "$d" == "/." ]] && d="/"; echo "$d"
  done | sort -u
}

# Chạy check máy một lần
T_TRACE=$(mcheck check-traceability)
T_COMPL=$(mcheck check-completeness)
T_FNDOC=$(mcheck check-fn-doc)
T_COV=$(mcheck check-code-doc-coverage)
T_I18N=$(mcheck check-i18n)

inject() {  # $1 = review-checklist.md, $2 = block temp file
  local f="$1" b="$2"
  grep -q 'AUTO-CHECKLIST:START' "$f" 2>/dev/null || return 0
  awk -v bf="$b" '
    BEGIN { while ((getline l < bf) > 0) blk = blk l ORS }
    /AUTO-CHECKLIST:START/ { print; printf "%s", blk; ins=1; next }
    /AUTO-CHECKLIST:END/   { ins=0 }
    !ins
  ' "$f" > "$f.tmp" && mv "$f.tmp" "$f"
}

emit() {  # $1=phase-file, build block on stdin temp
  local cl="v-model/$1/review-checklist.md"; local tmp; tmp="$(mktemp)"; cat > "$tmp"
  inject "$cl" "$tmp"; rm -f "$tmp"
}

echo "→ Sinh AUTO review-checklist (ground-truth + auto-tick)"

# 01,03: chỉ mục máy truy vết
for ph in 01-requirement 03-architecture; do
  printf -- "- [%s] Truy vết liền mạch REQ→…→TC (check-traceability)\n" "$T_TRACE" | emit "$ph"
done

# 02-specification (SRS + NFR): completeness + error codes + screens + NFR có test
{ printf -- "- [%s] Đủ tiểu mục đặc tả liên quan (check-completeness)\n" "$T_COMPL"
  while IFS= read -r k; do [[ -z "$k" ]] && continue; printf -- "- [%s] SRS đặc tả xử lý error \`%s\`\n" "$(tick "$SRS" "$k")" "$k"; done < <(err_keys)
  while IFS= read -r s; do [[ -z "$s" ]] && continue; printf -- "- [%s] SRS đặc tả màn hình \`%s\`\n" "$(tick "$SRS" "$s")" "$s"; done < <(screens)
  while IFS= read -r n; do [[ -z "$n" ]] && continue
    t=" "; for f in "$UT" "$IT" "$QT" "$AT"; do grep -qF "$n" "$f" 2>/dev/null && t="x"; done
    printf -- "- [%s] NFR \`%s\` có test kiểm chứng\n" "$t" "$n"; done < <(ids "$NFR" NFR)
} | emit 02-specification

# 04-DDD: completeness + endpoints + error flows
{ printf -- "- [%s] Đủ 7 tiểu mục/sequence (check-completeness)\n" "$T_COMPL"
  while IFS= read -r e; do [[ -z "$e" ]] && continue; printf -- "- [%s] Thiết kế endpoint \`%s\`\n" "$(tick "$DDD" "$e")" "$e"; done < <(endpoints)
  while IFS= read -r k; do [[ -z "$k" ]] && continue; printf -- "- [%s] DDD có luồng lỗi \`%s\`\n" "$(tick "$DDD" "$k")" "$k"; done < <(err_keys)
} | emit 04-detailed-design

# 05-code: fn-doc + coverage + i18n
{ printf -- "- [%s] Hàm public có header @trace/@version (check-fn-doc)\n" "$T_FNDOC"
  printf -- "- [%s] Mọi file mã trace tới DD (check-code-doc-coverage)\n" "$T_COV"
  printf -- "- [%s] i18n vi/en khớp key (check-i18n)\n" "$T_I18N"
} | emit 05-code

# 06-unit-test: MỘT dòng cho MỖI DD (mỗi DD phải có Unit Test phủ)
{ printf -- "- [%s] Mọi DD có Unit Test (check-traceability)\n" "$T_TRACE"
  while IFS= read -r d; do [[ -z "$d" ]] && continue; printf -- "- [%s] Có Unit Test phủ \`%s\`\n" "$(tick "$UT" "$d")" "$d"; done < <(ids "$DDD" DD)
} | emit 06-unit-test

# 07-integration-test: MỘT dòng cho MỖI ARC (mỗi ARC phải có Integration Test phủ)
{ printf -- "- [%s] Mọi ARC có Integration Test (check-traceability)\n" "$T_TRACE"
  while IFS= read -r a; do [[ -z "$a" ]] && continue; printf -- "- [%s] Có Integration Test phủ \`%s\`\n" "$(tick "$IT" "$a")" "$a"; done < <(ids "$SAD" ARC)
} | emit 07-integration-test

# 08-sw-qualification-test: MỘT dòng cho MỖI SRS + mỗi error/endpoint phủ đầu-cuối
{ printf -- "- [%s] Mọi SRS có SW-Qualification Test (check-traceability)\n" "$T_TRACE"
  while IFS= read -r s; do [[ -z "$s" ]] && continue; printf -- "- [%s] Có SW-Qualification Test phủ \`%s\`\n" "$(tick "$QT" "$s")" "$s"; done < <(ids "$SRS" SRS)
  while IFS= read -r k; do [[ -z "$k" ]] && continue; printf -- "- [%s] Có QT cho error \`%s\`\n" "$(tick "$QT" "$k")" "$k"; done < <(err_keys)
  while IFS= read -r e; do [[ -z "$e" ]] && continue; printf -- "- [%s] Có QT cho endpoint \`%s\`\n" "$(tick "$QT" "$e")" "$e"; done < <(endpoints)
} | emit 08-sw-qualification-test

# 09-acceptance-test: MỘT dòng cho MỖI REQ (mỗi REQ phải có Acceptance Test phủ)
{ printf -- "- [%s] Mọi REQ có Acceptance Test (check-traceability)\n" "$T_TRACE"
  while IFS= read -r r; do [[ -z "$r" ]] && continue; printf -- "- [%s] Có Acceptance Test phủ \`%s\`\n" "$(tick "$AT" "$r")" "$r"; done < <(ids "$HLR" REQ)
} | emit 09-acceptance-test

# 10-user-manual: mỗi màn hình
{ printf -- "- [%s] Hướng dẫn đầy đủ (check-completeness)\n" "$T_COMPL"
  while IFS= read -r s; do [[ -z "$s" ]] && continue; printf -- "- [%s] Có mục hướng dẫn màn hình \`%s\`\n" "$(tick "$UM" "$s")" "$s"; done < <(screens)
} | emit 10-user-manual

# 11-operations: kiểm bằng base checklist (không có mục tự sinh từ code)
printf -- "- [x] Tài liệu vận hành soi bằng base checklist (deploy/runbook/release)\n" | emit 11-operations

echo "✓ Đã cập nhật AUTO review-checklist cho các phase"
