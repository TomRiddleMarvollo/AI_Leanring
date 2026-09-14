#!/usr/bin/env python3
"""render_mermaid.py — Đợt 3: SAD/SDD vẽ kiến trúc bằng YAML (có schema) → sinh Mermaid.

Nguồn chân lý là **YAML** (agent viết dữ liệu, không vẽ cú pháp Mermaid → hết lỗi vẽ tay).
Script này đọc mỗi khối ```yaml``` có `type:` hợp lệ và **sinh/ghi lại** khối ```mermaid```
ngay dưới nó (giữa mốc MERMAID:START/END). ON-DEMAND (như Đợt 2), không chạy mỗi commit.

Kiểu hỗ trợ: `c4container` · `c4context` · `block` · `sequence`.

Dùng:
  python3 render_mermaid.py [path.md ...]     # ghi Mermaid vào tài liệu
  python3 render_mermaid.py --check [path...]  # chỉ validate YAML (không ghi), lỗi -> exit 1
Không truyền path → mặc định SAD + DDD.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_DOCS = [
    "v-model/03-architecture/02-SAD.md",
    "v-model/04-detailed-design/03-DDD.md",
]
KNOWN = {"c4container", "c4context", "block", "sequence"}
BEGIN = "<!-- MERMAID:START (sinh bởi render-mermaid.sh từ YAML trên — ĐỪNG sửa tay) -->"
END = "<!-- MERMAID:END -->"


# --- Render từng loại / Render each type -----------------------------------------
def _c4(d: dict) -> list:
    kind = "C4Context" if d["type"] == "c4context" else "C4Container"
    out = [kind]
    for p in d.get("persons", []):
        out.append(f'  Person({p["id"]}, "{p["label"]}", "{p.get("desc", "")}")')
    boundary = d.get("boundary")
    inner = d.get("containers", [])
    pad = "  "
    if boundary:
        out.append(f'  System_Boundary(_b, "{boundary}") {{')
        pad = "    "
    for c in inner:
        fn = "ContainerDb" if c.get("db") else "Container"
        out.append(f'{pad}{fn}({c["id"]}, "{c["label"]}", "{c.get("tech", "")}", "{c.get("desc", "")}")')
    if boundary:
        out.append("  }")
    for r in d.get("rels", []):
        out.append(f'  Rel({r["from"]}, {r["to"]}, "{r.get("label", "")}", "{r.get("tech", "")}")')
    return out


def _block(d: dict) -> list:
    nodes = d.get("nodes", [])
    out = [f"  columns {d.get('columns', len(nodes) or 1)}"]
    for n in nodes:
        shape = n.get("shape", "square")
        label = n["label"]
        cell = f'{n["id"]}[("{label}")]' if shape == "cyl" else f'{n["id"]}["{label}"]'
        out.append(f"  {cell}")
    for e in d.get("edges", []):
        arrow = e.get("label")
        out.append(f'  {e["from"]} --> {e["to"]}' + (f'|"{arrow}"|' if arrow else ""))
    return ["block-beta"] + out


def _msg(m: dict, pad: str = "  ") -> str:
    arrow = "-->>" if m.get("dashed") else "->>"
    return f'{pad}{m["from"]}{arrow}{m["to"]}: {m["text"]}'


def _sequence(d: dict) -> list:
    out = ["sequenceDiagram"]
    for p in d.get("participants", []):
        if isinstance(p, dict):
            kw = "actor" if p.get("actor") else "participant"
            out.append(f'  {kw} {p["id"]} as {p.get("label", p["id"])}')
        else:
            out.append(f"  participant {p}")
    for s in (d.get("steps") or d.get("messages", [])):
        if "alt" in s:  # nhóm alt/else
            out.append(f'  alt {s["alt"]}')
            for m in s.get("then", []):
                out.append(_msg(m, "    "))
            if "else" in s:
                out.append(f'  else {s["else"]}')
                for m in s.get("else_steps", []):
                    out.append(_msg(m, "    "))
            out.append("  end")
        else:
            out.append(_msg(s))
    return out


RENDERERS = {"c4container": _c4, "c4context": _c4, "block": _block, "sequence": _sequence}
REQUIRED = {
    "c4container": ["containers"], "c4context": ["containers"],
    "block": ["nodes"], "sequence": ["participants"],
}


def render_one(d: dict) -> str:
    body = RENDERERS[d["type"]](d)
    title = d.get("title", d["type"])
    return "```mermaid\n---\ntitle: " + str(title) + "\n---\n" + "\n".join(body) + "\n```"


def validate(d: dict, where: str) -> list:
    errs = []
    t = d.get("type")
    if t not in KNOWN:
        return [f"{where}: `type` không hợp lệ ({t!r}); phải là {sorted(KNOWN)}."]
    if "title" not in d:
        errs.append(f"{where}: thiếu `title`.")
    for key in REQUIRED[t]:
        if not d.get(key):
            errs.append(f"{where}: type {t} thiếu `{key}`.")
    if t == "sequence" and not (d.get("steps") or d.get("messages")):
        errs.append(f"{where}: type sequence thiếu `steps` (hoặc `messages`).")
    return errs


# --- Quét tài liệu / Scan a document ---------------------------------------------
YAML_BLOCK = re.compile(r"```ya?ml\n(.*?)\n```", re.DOTALL)


def _load_yaml(text: str):
    import yaml  # cài on-demand qua wrapper
    return yaml.safe_load(text)


def process(path: Path, check_only: bool) -> tuple:
    """Trả (số diagram, danh sách lỗi). Nếu không check_only → ghi Mermaid vào file."""
    src = path.read_text(encoding="utf-8")
    diagrams, errors = [], []
    for m in YAML_BLOCK.finditer(src):
        try:
            d = _load_yaml(m.group(1))
        except Exception as e:  # YAML hỏng
            errors.append(f"{path.name}: YAML lỗi cú pháp — {e}")
            continue
        if not isinstance(d, dict) or d.get("type") not in KNOWN:
            continue  # khối yaml thường, không phải diagram
        errors += validate(d, f"{path.name}")
        diagrams.append((m.end(), d))

    if check_only or errors or not diagrams:
        return len(diagrams), errors

    # Ghi từ CUỐI file lên đầu để offset không lệch.
    out = src
    for end_pos, d in sorted(diagrams, key=lambda x: -x[0]):
        rendered = f"{BEGIN}\n{render_one(d)}\n{END}"
        after = out[end_pos:]
        mblock = re.compile(r"\n*" + re.escape(BEGIN) + r".*?" + re.escape(END), re.DOTALL)
        m2 = mblock.match(after)
        if m2:
            out = out[:end_pos] + "\n\n" + rendered + after[m2.end():]
        else:
            out = out[:end_pos] + "\n\n" + rendered + after
    path.write_text(out, encoding="utf-8")
    return len(diagrams), errors


def main() -> int:
    args = sys.argv[1:]
    check_only = "--check" in args
    paths = [a for a in args if not a.startswith("--")] or DEFAULT_DOCS
    total, all_errors = 0, []
    for p in paths:
        path = Path(p)
        if not path.exists():
            continue
        n, errs = process(path, check_only)
        total += n
        all_errors += errs
        if not check_only and n and not errs:
            print(f"✓ {p}: render {n} sơ đồ")
    if all_errors:
        for e in all_errors:
            print(f"  ✗ {e}", file=sys.stderr)
        return 1
    if check_only:
        print(f"✓ YAML sơ đồ hợp lệ ({total} sơ đồ).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
