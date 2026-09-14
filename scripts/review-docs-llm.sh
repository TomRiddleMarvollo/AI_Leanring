#!/usr/bin/env bash
#
# review-docs-llm.sh — TẦNG 2: AI thứ hai phản biện độ ĐẦY ĐỦ & SÂU của tài liệu.
# A second AI adversarially reviews documentation depth.
#
# Dùng LLM CHẠY LOCAL qua Ollama (miễn phí). Mặc định model: qwen3:30b.
# Uses a LOCAL LLM via Ollama (free). Default model: qwen3:30b.
#
# Cài / Setup:
#   1) Cài Ollama: https://ollama.com
#   2) ollama serve            (chạy nền)
#   3) ollama pull qwen3:30b
#
# Dùng / Usage:
#   bash scripts/review-docs-llm.sh                 # review bộ SDLC, chỉ in (exit 0)
#   bash scripts/review-docs-llm.sh --strict        # fail nếu tài liệu dưới ngưỡng
#   bash scripts/review-docs-llm.sh v-model/04-detailed-design/03-DDD.md   # review file cụ thể
#
# Biến môi trường / Env:
#   OLLAMA_HOST   (mặc định http://localhost:11434)
#   OLLAMA_MODEL  (mặc định qwen3:30b)
#   DOC_REVIEW_MIN_SCORE  (mặc định 7, thang 0..10)
#   DOC_REVIEW_REQUIRE=1  (bắt buộc phải có Ollama; thiếu -> fail ở --strict)
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

export OLLAMA_HOST="${OLLAMA_HOST:-http://localhost:11434}"
export OLLAMA_MODEL="${OLLAMA_MODEL:-qwen3:30b}"
export DOC_REVIEW_MIN_SCORE="${DOC_REVIEW_MIN_SCORE:-7}"
export DOC_REVIEW_REQUIRE="${DOC_REVIEW_REQUIRE:-0}"
export DOC_REVIEW_STRICT=0
export DELTA_MODE=0

# --diff [--base=<ref>]: chỉ soi phần tài liệu v-model THAY ĐỔI trong git (cổng nội dung delta).
DELTA=0; BASE=""
args=()
for a in "$@"; do
  case "$a" in
    --strict) export DOC_REVIEW_STRICT=1 ;;
    --diff)   DELTA=1 ;;
    --base=*) BASE="${a#--base=}" ;;
    *) args+=("$a") ;;
  esac
done

if [[ "$DELTA" == "1" ]]; then
  # Phạm vi diff: có --base → so với nhánh gốc (CI); không → staged (pre-commit), rỗng thì thử working tree.
  if [[ -n "$BASE" ]]; then RANGE=("$BASE...HEAD"); else RANGE=(--cached); fi
  changed="$(git diff --name-only "${RANGE[@]}" -- v-model 2>/dev/null | grep -E '\.md$' || true)"
  if [[ -z "$changed" && -z "$BASE" ]]; then
    changed="$(git diff --name-only -- v-model 2>/dev/null | grep -E '\.md$' || true)"; RANGE=()
  fi
  if [[ -z "$changed" ]]; then echo "→ Không có tài liệu v-model nào thay đổi — bỏ qua delta review."; exit 0; fi
  DELTA_FILE="$(mktemp)"
  while IFS= read -r f; do
    [[ -f "$f" ]] || continue
    {
      echo "=== $f (phần thêm/sửa) ==="
      git diff ${RANGE[@]+"${RANGE[@]}"} -- "$f" 2>/dev/null | grep -E '^\+' | grep -vE '^\+\+\+' | sed 's/^\+//'
      echo
    } >> "$DELTA_FILE"
  done <<< "$changed"
  export DELTA_MODE=1 DELTA_FILE
  echo "→ TẦNG 2 — LLM delta-review (git diff) — Ollama $OLLAMA_MODEL @ $OLLAMA_HOST"
  echo "  Tài liệu thay đổi:"; printf '    • %s\n' $changed
else
  if [[ ${#args[@]} -eq 0 ]]; then
    args=(v-model/02-specification/01-SRS.md v-model/02-specification/01b-NFR.md \
          v-model/03-architecture/02-SAD.md v-model/04-detailed-design/03-DDD.md \
          v-model/06-unit-test/test-cases.md v-model/07-integration-test/test-cases.md \
          v-model/08-sw-qualification-test/test-cases.md v-model/09-acceptance-test/test-cases.md \
          v-model/10-user-manual/06-USER-MANUAL.md v-model/11-operations/runbook.md)
  fi
  echo "→ TẦNG 2 — LLM review (Ollama $OLLAMA_MODEL @ $OLLAMA_HOST)"
fi

python3 - ${args[@]+"${args[@]}"} <<'PY'
import os, sys, json, urllib.request

host  = os.environ["OLLAMA_HOST"]
model = os.environ["OLLAMA_MODEL"]
minsc = float(os.environ.get("DOC_REVIEW_MIN_SCORE", "7"))
strict  = os.environ.get("DOC_REVIEW_STRICT", "0") == "1"
require = os.environ.get("DOC_REVIEW_REQUIRE", "0") == "1"
docs = [d for d in sys.argv[1:] if os.path.exists(d)]

# --- Ollama có chạy & đã pull đúng model chưa? ---
def skip(msg):
    print(f"  ⚠ {msg}")
    print(f"    Cài https://ollama.com → `ollama serve` → `ollama pull {model}`")
    sys.exit(1 if (strict and require) else 0)

try:
    tags = json.loads(urllib.request.urlopen(host + "/api/tags", timeout=5).read())
except Exception as e:
    skip(f"Không kết nối được Ollama ({host}): {e}")
names = [m.get("name", "") for m in (tags.get("models") or [])]
if not any(n == model or n.startswith(model.split(":")[0]) for n in names):
    skip(f"Model '{model}' chưa được pull trên Ollama (có: {', '.join(names) or 'không có'}).")

gt_full = ""
if os.path.exists("v-model/_traceability/GROUND-TRUTH.md"):
    gt_full = open("v-model/_traceability/GROUND-TRUTH.md", encoding="utf-8").read()
gt = gt_full[:4000]

INSTR = (
 "Bạn là reviewer phần mềm cấp cao, CỰC KỲ KHẮT KHE. GIẢ ĐỊNH tài liệu này CÒN THIẾU.\n"
 "Dựa trên tài liệu và 'GROUND-TRUTH' (mã lỗi, endpoint, màn hình thực tế của hệ thống),\n"
 "liệt kê CỤ THỂ những chỗ thiếu hoặc nông, ví dụ: thiếu ca lỗi, thiếu màn hình/transition,\n"
 "thiếu function/API, chưa nêu biện pháp bảo mật, đặc tả/điều kiện mơ hồ không kiểm chứng được.\n"
 'CHỈ trả về JSON đúng schema: {"score": <0-10>, "verdict": "pass|fail", "gaps": ["<cụ thể>", ...]}.\n'
 "score = độ đầy đủ (0..10). verdict=fail nếu còn thiếu sót quan trọng. Không thêm chữ ngoài JSON."
)

# Prompt RIÊNG cho User Manual: soi độ phủ theo 3 trục màn hình/use-case/button (rule #6).
UM_INSTR = (
 "Bạn là reviewer User Manual CỰC KỲ KHẮT KHE. GIẢ ĐỊNH tài liệu CÒN SÓT.\n"
 "GROUND-TRUTH liệt kê ĐẦY ĐỦ: mọi MÀN HÌNH (route), mọi BUTTON/action (i18n), mọi USE-CASE (SRS).\n"
 "Yêu cầu: KHÔNG bỏ sót màn hình nào, use-case nào, button nào.\n"
 "Với TỪNG mục trong GROUND-TRUTH, kiểm tra User Manual có mô tả chưa; liệt kê CỤ THỂ cái nào THIẾU:\n"
 " - Màn hình chưa có `### SCR-###`; button/action chưa được hướng dẫn (thao tác + kết quả);\n"
 " - Use-case (SRS) chưa có luồng tương ứng; transition (vào/ra/lỗi/huỷ) còn thiếu; thiếu song ngữ vi/en.\n"
 'CHỈ trả về JSON: {"score": <0-10>, "verdict": "pass|fail", "gaps": ["<màn hình/button/use-case cụ thể còn thiếu>", ...]}.\n'
 "verdict=fail nếu còn BẤT KỲ màn hình/button/use-case nào chưa được phủ. Không thêm chữ ngoài JSON."
)

# Prompt DELTA: chỉ soi phần THÊM/SỬA trong git diff — phản biện NỘI DUNG (không chỉ cấu trúc).
DELTA_INSTR = (
 "Bạn là reviewer phần mềm CỰC KỲ KHẮT KHE. Dưới đây là phần MỚI THÊM/SỬA trong tài liệu V-model.\n"
 "Phản biện NỘI DUNG của riêng phần thay đổi (không chỉ cấu trúc): logic đúng không, đặc tả có mâu thuẫn/\n"
 "mơ hồ không kiểm chứng được, thiếu ca lỗi/biên/điều kiện, có sai/lệch so với GROUND-TRUTH (mã lỗi/endpoint/\n"
 "màn hình/button/use-case) không, hợp đồng hàm thiếu input/output/lỗi, yêu cầu không theo EARS.\n"
 'CHỈ trả JSON: {"score": <0-10>, "verdict": "pass|fail", "gaps": ["<cụ thể>", ...]}.\n'
 "verdict=fail nếu phần thay đổi có vấn đề nội dung quan trọng. Không thêm chữ ngoài JSON."
)

def ask(prompt):
    body = json.dumps({
        "model": model, "prompt": prompt, "stream": False,
        "format": "json", "think": False, "options": {"temperature": 0},
    }).encode()
    req = urllib.request.Request(host + "/api/generate", data=body,
                                 headers={"Content-Type": "application/json"})
    out = json.loads(urllib.request.urlopen(req, timeout=600).read())
    try:
        return json.loads(out.get("response", "{}"))
    except Exception:
        return {"score": 0, "verdict": "fail", "gaps": ["Không parse được phản hồi LLM."]}

# --- Chế độ DELTA: một lượt review trên toàn bộ phần thay đổi (cổng nội dung) ---
if os.environ.get("DELTA_MODE") == "1":
    delta = open(os.environ["DELTA_FILE"], encoding="utf-8").read()
    prompt = (f"{DELTA_INSTR}\n\n=== GROUND-TRUTH ===\n{gt}\n\n=== PHẦN THAY ĐỔI ===\n{delta}")
    try:
        r = ask(prompt)
    except Exception as e:
        print(f"  ✗ delta-review: lỗi gọi LLM: {e}")
        sys.exit(1 if strict else 0)
    score = r.get("score", 0); verdict = r.get("verdict", "fail"); gaps = r.get("gaps", []) or []
    ok = (str(verdict).lower() == "pass") and (float(score) >= minsc)
    print(f"  {'✓' if ok else '✗'} delta — score {score}/10 ({verdict})")
    for g in gaps[:15]:
        print(f"      • {g}")
    print("—")
    if not ok:
        print(f"LLM delta-review: phần thay đổi chưa đạt ngưỡng {minsc}/10.")
    sys.exit(1 if (strict and not ok) else 0)

def review(path):
    content = open(path, encoding="utf-8").read()
    is_um = path.replace("\\", "/").endswith("USER-MANUAL.md") or "10-user-manual" in path
    instr = UM_INSTR if is_um else INSTR
    ground = gt_full if is_um else gt   # UM cần TOÀN BỘ ground-truth để không sót button/use-case
    prompt = (f"{instr}\n\n=== GROUND-TRUTH ===\n{ground}\n\n"
              f"=== TÀI LIỆU CẦN REVIEW: {path} ===\n{content}")
    return ask(prompt)

fails = 0
for d in docs:
    try:
        r = review(d)
    except Exception as e:
        print(f"  ✗ {d}: lỗi gọi LLM: {e}")
        fails += 1          # LLM hỏng -> coi là chưa đạt (strict sẽ fail)
        continue
    score = r.get("score", 0); verdict = r.get("verdict", "fail"); gaps = r.get("gaps", []) or []
    ok = (str(verdict).lower() == "pass") and (float(score) >= minsc)
    print(f"  {'✓' if ok else '✗'} {d} — score {score}/10 ({verdict})")
    for g in gaps[:12]:
        print(f"      • {g}")
    if not ok:
        fails += 1

print("—")
print(f"LLM review: {fails} tài liệu chưa đạt ngưỡng {minsc}/10.")
sys.exit(1 if (strict and fails > 0) else 0)
PY
