#!/usr/bin/env bash
#
# gen-ground-truth.sh — TẦNG 1: liệt kê "tập đầy đủ" từ nguồn chân lý (code, i18n)
# để tài liệu không thể quên món nào. / Enumerate ground-truth so docs can't omit items.
#
# Sinh v-model/_traceability/GROUND-TRUTH.md: mã lỗi (locales), endpoint (code), màn hình (router),
# kèm dấu ✓/✗ cho biết đã xuất hiện trong tài liệu tương ứng chưa.
#
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"   # đường dẫn v-model dùng chung
[[ -d "$D" ]] || { echo "ℹ Không có $D — bỏ qua."; exit 0; }
# Test coverage trải trên cả 3 phase test (unit/integration/sw-qualification).
TESTS=("$UT_DOC" "$IT_DOC" "$QT_DOC")
OUT="$D/_traceability/GROUND-TRUTH.md"

mark() { grep -qF "$2" "$1" 2>/dev/null && echo "✓" || echo "✗"; }
mark_test() { grep -qF "$1" "${TESTS[@]}" 2>/dev/null && echo "✓" || echo "✗"; }

err_keys() {
  while IFS= read -r f; do
    python3 - "$f" <<'PY'
import json,sys
try:
    d=json.load(open(sys.argv[1],encoding="utf-8"))
    for k in (d.get("errors") or {}): print(k)
except Exception: pass
PY
  done < <(find frontend backend backend-python -path '*/locales/en.json' 2>/dev/null)
  : ; }
endpoints() {
  grep -rhoE "\.(get|post|put|patch|delete)\((\"[^\"]+\"|'[^']+')" backend backend-python 2>/dev/null \
    | grep -oE "(\"[^\"]+\"|'[^']+')" | tr -d "\"'" | grep -vE '^$' | sort -u || true
}
screens() {
  find frontend/src/app -type f -name 'page.*' 2>/dev/null | while IFS= read -r p; do
    d="/$(dirname "${p#frontend/src/app/}")"; [[ "$d" == "/." ]] && d="/"; echo "$d"
  done | sort -u || true
}
# Buttons/actions từ i18n (frontend) → nhãn hiển thị phải xuất hiện trong User Manual.
# In ra sẵn dòng bảng "| `key` | en / vi | ✓|✗ |" (mark = nhãn en HOẶC vi có trong UM).
buttons_rows() {
  python3 - "$UM" <<'PY'
import json,os,re,sys,glob
UM=sys.argv[1]; um=open(UM,encoding="utf-8").read() if os.path.exists(UM) else ""
ACTION=re.compile(r'^(save|cancel|submit|login|log ?in|logout|log ?out|sign ?in|sign ?up|signin|signup|register|delete|remove|add|create|edit|update|confirm|close|open|next|back|prev|previous|continue|search|filter|apply|reset|send|upload|download|export|import|refresh|retry|ok|start|stop|pause|resume|enable|disable|approve|reject|accept|decline|copy|share|print|clear|select|view|show|hide)$',re.I)
def flat(d,p=''):
    if isinstance(d,dict):
        for k,v in d.items(): yield from flat(v,(p+'.'+k) if p else k)
    else: yield p,d
def is_action(key):
    segs=key.lower().split('.')
    return any(s in ('button','buttons','btn','action','actions') for s in segs[:-1]) or bool(ACTION.match(segs[-1]))
seen=set(); rows=[]
for enp in sorted(glob.glob('frontend/**/locales/en.json',recursive=True)):
    try: en=json.load(open(enp,encoding="utf-8"))
    except Exception: continue
    vip=os.path.join(os.path.dirname(enp),'vi.json')
    vf=dict(flat(json.load(open(vip,encoding="utf-8")))) if os.path.exists(vip) else {}
    for key,val in flat(en):
        if not is_action(key) or key in seen: continue
        seen.add(key)
        ev=str(val); vv=str(vf.get(key,''))
        found=(ev and ev in um) or (vv and vv in um)
        rows.append(f"| `{key}` | {ev} / {vv} | {'✓' if found else '✗'} |")
print("\n".join(rows) if rows else "| _(chưa có)_ | — | — |")
PY
}
# Use-cases = các dòng SRS-### (SRS đặc tả use case cụ thể). Liệt kê để LLM/người soi UM có phủ đủ.
usecases_rows() {
  [[ -f "$SRS" ]] || { echo "| _(chưa có)_ | — | — |"; return; }
  awk -F'|' '/^\| *SRS-[0-9]{3} *\|/{
    id=$2; spec=$3; up=$4
    gsub(/^[ \t]+|[ \t]+$/,"",id); gsub(/^[ \t]+|[ \t]+$/,"",spec); gsub(/^[ \t]+|[ \t]+$/,"",up)
    if(length(spec)>70) spec=substr(spec,1,70) "…"
    printf "| %s | %s | %s |\n", id, spec, up
  }' "$SRS" | grep . || echo "| _(chưa có)_ | — | — |"
}

TMP="$(mktemp)"
{
  echo "# Ground-Truth Inventory — Tập đầy đủ (sinh tự động)"
  echo
  echo "> TẦNG 1 chống làm thiếu: liệt kê MỌI món suy ra từ code/i18n. Tài liệu phải phủ hết."
  echo "> Sinh bởi \`scripts/gen-ground-truth.sh\` — **đừng sửa tay**. ✓ = đã có trong tài liệu, ✗ = còn thiếu."
  echo
  echo "## Error codes (từ locales) → phải xử lý trong Design (DDD) & Test"
  echo "| Error code | Design | Test |"; echo "|---|---|---|"
  n=0; while IFS= read -r k; do [[ -z "$k" ]] && continue; n=$((n+1)); echo "| \`$k\` | $(mark "$DDD" "$k") | $(mark_test "$k") |"; done < <(err_keys | sort -u)
  [[ $n -eq 0 ]] && echo "| _(chưa có)_ | — | — |"
  echo
  echo "## Endpoints (từ code) → phải có trong Design (DDD)"
  echo "| Endpoint | Design |"; echo "|---|---|"
  n=0; while IFS= read -r e; do [[ -z "$e" ]] && continue; n=$((n+1)); echo "| \`$e\` | $(mark "$DDD" "$e") |"; done < <(endpoints)
  [[ $n -eq 0 ]] && echo "| _(chưa có)_ | — |"
  echo
  echo "## Screens (từ router) → phải có trong User Manual"
  echo "| Route | User Manual |"; echo "|---|---|"
  n=0; while IFS= read -r s; do [[ -z "$s" ]] && continue; n=$((n+1)); echo "| \`$s\` | $(mark "$UM" "$s") |"; done < <(screens)
  [[ $n -eq 0 ]] && echo "| _(chưa có)_ | — |"
  echo
  echo "## Buttons / actions (từ i18n) → nhãn phải xuất hiện trong User Manual"
  echo "> ✗ = nhãn nút (en/vi) chưa thấy trong User Manual → nghi thiếu hướng dẫn cho nút đó."
  echo "| Action (i18n key) | Label (en / vi) | User Manual |"; echo "|---|---|---|"
  buttons_rows
  echo
  echo "## Use-cases (từ SRS) → mỗi use-case phải có luồng trong User Manual"
  echo "> Máy KHÔNG chấm ✓/✗ (UM viết văn xuôi, không trích SRS-ID) — dùng cho LLM/người soi độ phủ."
  echo "| Use-case (SRS) | Đặc tả | Traces ↑ |"; echo "|---|---|---|"
  usecases_rows
} > "$TMP"

mv "$TMP" "$OUT"
echo "✓ Đã cập nhật $OUT"
