#!/usr/bin/env python3
"""check_completeness.py — Ép ĐỘ ĐẦY ĐỦ của tài liệu thiết kế & hướng dẫn.

Logic của check-completeness.sh (bash/awk) chuyển sang Python cho dễ bảo trì —
block parsing, đếm nội dung, bảng threat model bằng awk là chỗ dễ mục nhất của harness.
Gọi qua wrapper scripts/check-completeness.sh (giữ nguyên giao diện --strict).

Khác biệt CÓ CHỦ ĐÍCH so với bản bash: placeholder ("để sau", "TODO"...) giờ so
case-insensitive ĐÚNG Unicode — bản awk chỉ hạ chữ ASCII nên "Để sau" (Đ hoa) lọt lưới.
"""
from __future__ import annotations

import glob
import json
import os
import re
import subprocess
import sys

# --- về gốc repo ---
root = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                      capture_output=True, text=True).stdout.strip()
os.chdir(root or os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

D = "v-model"
SAD = f"{D}/03-architecture/02-SAD.md"
NFR = f"{D}/02-specification/01b-NFR.md"
SRS = f"{D}/02-specification/01-SRS.md"
DDD = f"{D}/04-detailed-design/03-DDD.md"
UM = f"{D}/10-user-manual/06-USER-MANUAL.md"

DD_HEADERS = ["#### Functions / APIs", "#### Happy path", "#### Error & alternate flows",
              "#### Sequence diagram", "#### Validation", "#### Security", "#### Data model"]
SCR_HEADERS = ["#### Purpose", "#### Steps", "#### Transitions", "#### Error & empty states"]

PLACEHOLDER = re.compile(
    r"_____|_\(|todo|tbd|n/a|pending|unspecified|coming soon|chi tiết sau|bổ sung sau"
    r"|cập nhật sau|chưa xử lý|chưa có nội dung|để sau|xử lý sau", re.I)
STRIDE = re.compile(r"(^|[^a-z])(s|t|r|i|d|e)\s*:|spoofing|tampering|repudiation"
                    r"|disclosure|denial|elevation", re.I)

errors = 0
warns = 0


def err(msg: str) -> None:
    global errors
    print(f"  ✗ {msg}")
    errors += 1


def warn(msg: str) -> None:
    global warns
    print(f"  ⚠ {msg}")
    warns += 1


def read(path: str) -> str | None:
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        return f.read()


def config(name: str) -> str:
    """Mặc định 1; env override; .harness-config (KEY=value) override cuối — như bash source."""
    val = os.environ.get(name, "1")
    if os.path.isfile(".harness-config"):
        for line in open(".harness-config", encoding="utf-8"):
            m = re.match(rf"\s*{name}\s*=\s*([^#\s]+)", line)
            if m:
                val = m.group(1).strip("\"'")
    return val


def block_of(text: str, id_: str) -> list[str]:
    """Khối của một mục: từ '### <id>' tới '### ' kế tiếp."""
    out, on = [], False
    for line in text.split("\n"):
        if re.match(rf"^### {id_}([: ]|$)", line):
            on = True
            out.append(line)
            continue
        if on and line.startswith("### "):
            break
        if on:
            out.append(line)
    return out


def sub_count(block: list[str], header: str) -> tuple[int, int]:
    """Đếm (số dòng, tổng ký tự) nội dung THẬT dưới một tiểu mục (bỏ blank/bảng-kẻ/placeholder)."""
    on, cnt, length = False, 0, 0
    for line in block:
        if header in line:
            on = True
            continue
        if on and (line.startswith("#### ") or line.startswith("### ") or re.match(r"^---\s*$", line)):
            on = False
        if on and line.strip() and not re.match(r"^\|[-: |]+\|$", line):
            if PLACEHOLDER.search(line):
                continue
            cnt += 1
            length += len(line)
    return cnt, length


def check_item(text: str, id_: str, headers: list[str]) -> None:
    block = block_of(text, id_)
    block_text = "\n".join(block)
    for h in headers:
        if h not in block_text:
            err(f"{id_} thiếu tiểu mục bắt buộc '{h}'.")
            continue
        cnt, length = sub_count(block, h)
        if cnt == 0:
            err(f"{id_}: tiểu mục '{h}' bỏ trống / chỉ có placeholder.")
        elif length < 20:
            warn(f"{id_}: tiểu mục '{h}' có thể quá sơ sài (dưới 20 ký tự) — heuristic, tự xem lại nội dung.")


def mermaid_missing_frontmatter(text: str) -> int:
    """Số khối ```mermaid có dòng nội dung đầu KHÔNG phải '---' frontmatter."""
    bad, inb, expect = 0, False, False
    for line in text.split("\n"):
        if line.startswith("```mermaid"):
            inb, expect = True, True
            continue
        if inb and line.startswith("```"):
            inb = False
            continue
        if inb and expect and line.strip():
            expect = False
            if not re.match(r"^---\s*$", line):
                bad += 1
    return bad


def check_sad() -> None:
    text = read(SAD)
    if text is None:
        return
    if not (re.search(r"type: *c4(container|context)", text) or re.search(r"C4Context|C4Container|C4Component", text)):
        err("SAD thiếu C4 model (YAML 'type: c4container' hoặc Mermaid C4*).")
    if not (re.search(r"type: *block", text) or "block-beta" in text):
        err("SAD thiếu Biểu đồ khối (YAML 'type: block' hoặc Mermaid block-beta).")
    if mermaid_missing_frontmatter(text):
        err("SAD: có sơ đồ Mermaid thiếu YAML frontmatter ('---').")
    if config("REQUIRE_THREAT_MODEL") != "1":
        return
    if not re.search(r"threat model|STRIDE", text, re.I):
        err("SAD thiếu mục Threat model (STRIDE) cho luồng nhạy cảm.")
    # Bảng nên có ≥1 dòng THẬT, mỗi dòng nêu loại STRIDE + biện pháp — heuristic → chỉ CẢNH BÁO.
    rows, on = [], False
    for line in text.split("\n"):
        if re.match(r"^## Threat model", line):
            on = True
            continue
        if on and line.startswith("## "):
            on = False
        if on and line.startswith("|") and not re.match(r"^\|[-: |]+\|$", line) and "Thành phần/luồng" not in line:
            rows.append(line)
    real = 0
    for row in rows:
        cols = row.split("|")
        threat = cols[2].strip() if len(cols) > 2 else ""
        mit = cols[3].strip() if len(cols) > 3 else ""
        if (not threat and not mit) or "_(" in threat:  # dòng skeleton
            continue
        real += 1
        if not STRIDE.search(threat):
            warn(f"Threat model: dòng '{threat}' không nêu rõ loại STRIDE (S/T/R/I/D/E) — heuristic, tự xem lại.")
        if len(mit) < 15 or PLACEHOLDER.search(mit):
            warn(f"Threat model: dòng '{threat}' có thể thiếu biện pháp giảm thiểu cụ thể — heuristic, tự xem lại.")
    if real < 1:
        warn("SAD: Threat model chưa có dòng đe doạ thật nào (mới chỉ có khung/skeleton).")


def check_nfr() -> None:
    text = read(NFR)
    if text is None:
        return
    quantitative = config("REQUIRE_NFR_QUANTITATIVE") == "1"
    for line in text.split("\n"):
        if not re.match(r"^\| *NFR-[0-9]{3}", line):
            continue
        id_ = re.search(r"NFR-[0-9]{3}", line).group(0)
        cols = line.split("|")
        tgt = cols[3].strip() if len(cols) > 3 else ""
        if not tgt:
            err(f"{id_} (NFR) chưa có ngưỡng đo cụ thể (cột target trống).")
        elif quantitative and not any(c.isdigit() for c in tgt):
            warn(f"{id_} (NFR) ngưỡng '{tgt}' không thấy SỐ đo cụ thể — heuristic (không có số không có nghĩa là sai), tự xem lại.")


def check_srs_ears() -> None:
    text = read(SRS)
    if text is None or config("REQUIRE_EARS_SRS") != "1":
        return
    for line in text.split("\n"):
        if not re.match(r"^\| *SRS-[0-9]{3}", line):
            continue
        id_ = re.search(r"SRS-[0-9]{3}", line).group(0)
        cols = line.split("|")
        spec = cols[2] if len(cols) > 2 else ""
        if re.search(r"đặc tả tiếp theo|_\(", spec, re.I):  # dòng skeleton
            continue
        if not re.search(r"shall|phải|sẽ", spec, re.I):
            warn(f"{id_} chưa viết theo EARS (thiếu modal 'shall/phải/sẽ' → câu yêu cầu chưa kiểm chứng được) — heuristic, tự xem lại.")


def check_ddd() -> None:
    text = read(DDD)
    if text is None:
        return
    ids = sorted(set(re.findall(r"^### (DD-[0-9]{3})", text, re.M)))
    if not ids:
        warn("DDD chưa có mục '### DD-###' nào.")
    contract = config("REQUIRE_DD_CONTRACT") == "1"
    for id_ in ids:
        check_item(text, id_, DD_HEADERS)
        block = block_of(text, id_)
        block_text = "\n".join(block)
        if not re.search(r"type: *sequence|sequenceDiagram", block_text):
            err(f"{id_}: Sequence diagram thiếu (YAML 'type: sequence' hoặc Mermaid 'sequenceDiagram').")
        if contract:
            fa_lines, on = [], False
            for line in block:
                if line.startswith("#### Functions / APIs"):
                    on = True
                    continue
                if on and (line.startswith("#### ") or line.startswith("### ")):
                    on = False
                if on:
                    fa_lines.append(line)
            fa = "\n".join(fa_lines)
            if not re.search(r"trả về|return|->|=>|response|\b2[0-9][0-9]\b", fa, re.I):
                warn(f"{id_}: hợp đồng Functions/APIs chưa nêu rõ ĐẦU RA (return/Trả về/response/2xx) — heuristic, tự xem lại.")
            if not re.search(r"raise|throw|error|lỗi|\b(4|5)[0-9][0-9]\b", fa, re.I):
                warn(f"{id_}: hợp đồng Functions/APIs chưa nêu CA LỖI (raise/throw/error/4xx/5xx) — heuristic, tự xem lại.")
    if mermaid_missing_frontmatter(text):
        err("DDD: có sơ đồ Mermaid thiếu YAML frontmatter ('---').")


def um_missing_buttons(um_text: str) -> list[str]:
    """Nhãn nút/action (i18n frontend) chưa xuất hiện trong User Manual."""
    action = re.compile(
        r"^(save|cancel|submit|login|log ?in|logout|log ?out|sign ?in|sign ?up|signin|signup"
        r"|register|delete|remove|add|create|edit|update|confirm|close|open|next|back|prev"
        r"|previous|continue|search|filter|apply|reset|send|upload|download|export|import"
        r"|refresh|retry|ok|start|stop|pause|resume|enable|disable|approve|reject|accept"
        r"|decline|copy|share|print|clear|select|view|show|hide)$", re.I)

    def flat(d, p=""):
        if isinstance(d, dict):
            for k, v in d.items():
                yield from flat(v, f"{p}.{k}" if p else k)
        else:
            yield p, d

    def is_action(key):
        segs = key.lower().split(".")
        return any(s in ("button", "buttons", "btn", "action", "actions") for s in segs[:-1]) \
            or bool(action.match(segs[-1]))

    seen, missing = set(), []
    for enp in sorted(glob.glob("frontend/**/locales/en.json", recursive=True)):
        try:
            en = json.load(open(enp, encoding="utf-8"))
        except Exception:
            continue
        vip = os.path.join(os.path.dirname(enp), "vi.json")
        vf = dict(flat(json.load(open(vip, encoding="utf-8")))) if os.path.exists(vip) else {}
        for key, val in flat(en):
            if not is_action(key) or key in seen:
                continue
            seen.add(key)
            ev, vv = str(val), str(vf.get(key, ""))
            if (ev and ev in um_text) or (vv and vv in um_text):
                continue
            missing.append(ev or vv or key)
    return missing


def check_um() -> None:
    text = read(UM)
    if text is None:
        return
    ids = sorted(set(re.findall(r"^### (SCR-[0-9]{3})", text, re.M)))
    if not ids:
        warn("User Manual chưa có mục '### SCR-###' nào.")
    for id_ in ids:
        check_item(text, id_, SCR_HEADERS)
    for id_ in sorted(set(re.findall(r"SCR-[0-9]{3}", text))):
        if id_ not in ids:
            warn(f"{id_} có trong inventory nhưng thiếu mục chi tiết '### {id_}'.")
    if config("REQUIRE_UM_BUTTONS") == "1":
        for label in um_missing_buttons(text):
            warn(f"Nút/hành động '{label}' (i18n) chưa thấy trong User Manual — nghi thiếu hướng dẫn.")


def check_code_coverage() -> None:
    """Phủ ngược từ code (WARN, best-effort): route → UM; endpoint → DDD."""
    um_text = read(UM)
    if os.path.isdir("frontend/src/app") and um_text is not None:
        for p in sorted(glob.glob("frontend/src/app/**/page.*", recursive=True)):
            rel_dir = os.path.dirname(os.path.relpath(p, "frontend/src/app"))
            route = f"/{rel_dir}" if rel_dir else "/"
            if route not in um_text:
                warn(f"Màn hình route '{route}' (từ {p}) chưa có trong User Manual.")
    ddd_text = read(DDD)
    if ddd_text is not None:
        eps = set()
        for base in ("backend", "backend-python"):
            for dirpath, _dirs, files in os.walk(base):
                for fn in files:
                    src = read(os.path.join(dirpath, fn))
                    if src is None:
                        continue
                    for m in re.finditer(r"\.(get|post|put|patch|delete)\((\"[^\"]+\"|'[^']+')", src):
                        eps.add(m.group(2).strip("\"'"))
        for ep in sorted(eps):
            if not ep or ep == "/":
                continue
            if ep not in ddd_text:
                warn(f"Endpoint '{ep}' có trong code nhưng chưa thấy trong Detailed Design.")


def main() -> int:
    if not os.path.isdir(D):
        print("ℹ Không có v-model — bỏ qua.")
        return 0
    strict = len(sys.argv) > 1 and sys.argv[1] == "--strict"
    print("→ Kiểm tra độ đầy đủ tài liệu / Checking documentation completeness")
    check_sad()
    check_nfr()
    check_srs_ears()
    check_ddd()
    check_um()
    check_code_coverage()
    print("—")
    print(f"Kết quả / Result: {errors} lỗi, {warns} cảnh báo.")
    if strict and errors > 0:
        print(f"✗ FAIL (strict): tài liệu thiếu {errors} tiểu mục bắt buộc.")
        return 1
    print("✓ OK — cảnh báo không chặn.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
