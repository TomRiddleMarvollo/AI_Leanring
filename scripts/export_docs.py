#!/usr/bin/env python3
"""export_docs.py — Đợt 2: xuất tài liệu V-model (Markdown) sang Excel/Word khi giao nộp.

Tài liệu SỐNG ở dạng Markdown nhẹ (viết/sửa nhanh, diff gọn). Khi cần GIAO NỘP bản
Excel/Word, chạy on-demand script này — KHÔNG chạy mỗi commit nên code vẫn nhanh.

Bản đồ định dạng (theo `v-model/README.md`):
  • REQ / SRS / Test Spec / Test Case → Excel (mỗi tài liệu một sheet, trích bảng Markdown).
  • Mọi review-checklist của phase → Excel (mỗi phase một sheet: Section · Item · Checked).
  • Test Plan / User Manual        → Word  (render heading/đoạn/bảng/danh sách).

Living docs stay in light Markdown; this on-demand tool renders Excel/Word for delivery.
Phụ thuộc: openpyxl (MIT) + python-docx (MIT) — chỉ cài khi chạy export (xem export-docs.sh).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# --- Bản đồ tài liệu → định dạng đích / Document → output-format map -------------
# (đường dẫn tương đối so với thư mục v-model/)
EXCEL_SPEC_DOCS = [
    ("REQ", "01-requirement/00-HLR.md"),
    ("SRS", "02-specification/01-SRS.md"),
    ("NFR", "02-specification/01b-NFR.md"),
    ("UT-SPEC", "06-unit-test/test-spec.md"),
    ("UT-CASES", "06-unit-test/test-cases.md"),
    ("IT-SPEC", "07-integration-test/test-spec.md"),
    ("IT-CASES", "07-integration-test/test-cases.md"),
    ("QT-SPEC", "08-sw-qualification-test/test-spec.md"),
    ("QT-CASES", "08-sw-qualification-test/test-cases.md"),
    ("AT-SPEC", "09-acceptance-test/test-spec.md"),
    ("AT-CASES", "09-acceptance-test/test-cases.md"),
]
WORD_DOCS = [
    ("Unit-Test-Strategy", "06-unit-test/test-strategy.md"),
    ("Unit-Test-Plan", "06-unit-test/test-plan.md"),
    ("Unit-Test-Report", "06-unit-test/test-report.md"),
    ("Integration-Test-Strategy", "07-integration-test/test-strategy.md"),
    ("Integration-Test-Plan", "07-integration-test/test-plan.md"),
    ("Integration-Test-Report", "07-integration-test/test-report.md"),
    ("SWQual-Test-Strategy", "08-sw-qualification-test/test-strategy.md"),
    ("SWQual-Test-Plan", "08-sw-qualification-test/test-plan.md"),
    ("SWQual-Test-Report", "08-sw-qualification-test/test-report.md"),
    ("Acceptance-Test-Strategy", "09-acceptance-test/test-strategy.md"),
    ("Acceptance-Test-Plan", "09-acceptance-test/test-plan.md"),
    ("Acceptance-Test-Report", "09-acceptance-test/test-report.md"),
    ("User-Manual", "10-user-manual/06-USER-MANUAL.md"),
    ("Ops-Deploy-Guide", "11-operations/deploy-guide.md"),
    ("Ops-Runbook", "11-operations/runbook.md"),
    ("Ops-Release-Notes", "11-operations/release-notes.md"),
]


# --- Phân tích Markdown thành block / Parse Markdown into blocks -----------------
def iter_blocks(md: str):
    """Sinh các block tuần tự từ Markdown thô.

    Mỗi block là tuple đã chuẩn hoá để cả Excel & Word dùng chung:
      ('heading', level:int, text)        — tiêu đề ATX (#..######)
      ('table', headers:list, rows:list)  — bảng pipe `| a | b |`
      ('list', items:list)                — danh sách `-`/`*`; mỗi item (checked|None, text)
      ('para', text)                      — đoạn văn
      ('hr',)                             — đường kẻ ngang `---`

    Bỏ qua HTML comment và frontmatter `---` đầu file để bản giao nộp sạch.
    """
    lines = md.replace("\r\n", "\n").split("\n")
    i, n = 0, len(lines)
    in_comment = False
    while i < n:
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        if in_comment:
            if "-->" in stripped:
                in_comment = False
            i += 1
            continue
        if stripped.startswith("<!--"):
            in_comment = "-->" not in stripped
            i += 1
            continue
        if not stripped:
            i += 1
            continue
        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", stripped):
            yield ("hr",)
            i += 1
            continue

        m = re.match(r"(#{1,6})\s+(.*)$", stripped)
        if m:
            yield ("heading", len(m.group(1)), m.group(2).strip())
            i += 1
            continue

        # Bảng: dòng `|...|` ngay sau là dòng phân cách `|---|`.
        if stripped.startswith("|") and i + 1 < n and re.match(
            r"\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$", lines[i + 1].strip()
        ):
            headers = _split_row(stripped)
            rows, i = [], i + 2
            while i < n and lines[i].strip().startswith("|"):
                rows.append(_split_row(lines[i].strip()))
                i += 1
            yield ("table", headers, rows)
            continue

        if re.match(r"[-*]\s+", stripped):
            items = []
            while i < n and re.match(r"\s*[-*]\s+", lines[i]):
                items.append(_parse_list_item(lines[i].strip()))
                i += 1
            yield ("list", items)
            continue

        # Đoạn văn: gộp tới dòng trống / block kế tiếp.
        buf = [stripped.lstrip(">").strip() if stripped.startswith(">") else stripped]
        i += 1
        while i < n and lines[i].strip() and not _starts_block(lines[i].strip()):
            nxt = lines[i].strip()
            buf.append(nxt.lstrip(">").strip() if nxt.startswith(">") else nxt)
            i += 1
        yield ("para", " ".join(buf))


def _starts_block(s: str) -> bool:
    return bool(
        re.match(r"#{1,6}\s", s)
        or s.startswith("|")
        or re.match(r"[-*]\s", s)
        or re.fullmatch(r"-{3,}|\*{3,}|_{3,}", s)
        or s.startswith("<!--")
    )


def _split_row(line: str) -> list:
    cells = line.strip().strip("|").split("|")
    return [c.strip() for c in cells]


def _parse_list_item(s: str):
    """`- [ ] text` → (False, text); `- [x] text` → (True, text); `- text` → (None, text)."""
    body = re.sub(r"^[-*]\s+", "", s)
    m = re.match(r"\[([ xX])\]\s+(.*)$", body)
    if m:
        return (m.group(1).lower() == "x", m.group(2).strip())
    return (None, body.strip())


def _strip_md(text: str) -> str:
    """Bỏ ký hiệu inline (**bold**, `code`, _it_) cho ô Excel — Word giữ bold riêng."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"\1", text)
    return text


# --- Xuất Excel / Excel export --------------------------------------------------
def export_excel(vmodel: Path, out: Path) -> list:
    """Sinh 2 workbook: spec (REQ/SRS/Test-Spec/Test-Cases) và reviews (mỗi phase một sheet)."""
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill

    written = []
    header_fill = PatternFill("solid", fgColor="DDEBF7")
    header_font = Font(bold=True)

    def add_table_sheet(wb, title, headers, rows):
        ws = wb.create_sheet(title[:31])  # Excel: tên sheet ≤ 31 ký tự.
        if headers:
            ws.append([_strip_md(h) for h in headers])
            for c in ws[1]:
                c.font, c.fill = header_font, header_fill
        for r in rows:
            ws.append([_strip_md(c) for c in r])
        for col in ws.columns:
            width = max((len(str(c.value)) for c in col if c.value), default=10)
            ws.column_dimensions[col[0].column_letter].width = min(width + 2, 60)

    # 1) Spec workbook — mỗi tài liệu một sheet, gộp mọi bảng trong tài liệu đó.
    wb = Workbook()
    wb.remove(wb.active)
    for code, rel in EXCEL_SPEC_DOCS:
        path = vmodel / rel
        if not path.exists():
            continue
        tables = [b for b in iter_blocks(path.read_text(encoding="utf-8")) if b[0] == "table"]
        if not tables:
            continue
        if len(tables) == 1:
            add_table_sheet(wb, code, tables[0][1], tables[0][2])
        else:
            for idx, (_, h, rws) in enumerate(tables, 1):
                add_table_sheet(wb, f"{code}-{idx}", h, rws)
    if wb.sheetnames:
        dst = out / "v-model-spec.xlsx"
        wb.save(dst)
        written.append(dst)

    # 2) Reviews workbook — mỗi phase một sheet checklist (Section · Item · Checked).
    wb2 = Workbook()
    wb2.remove(wb2.active)
    for ck in sorted(vmodel.glob("*/review-checklist.md")):
        phase = ck.parent.name
        rows, section = [], ""
        for b in iter_blocks(ck.read_text(encoding="utf-8")):
            if b[0] == "heading":
                section = _strip_md(b[2])
            elif b[0] == "list":
                for checked, text in b[1]:
                    if checked is None:
                        continue
                    rows.append([section, _strip_md(text), "x" if checked else ""])
        if rows:
            add_table_sheet(wb2, phase, ["Section", "Item", "Checked"], rows)
    if wb2.sheetnames:
        dst = out / "v-model-reviews.xlsx"
        wb2.save(dst)
        written.append(dst)
    return written


# --- Xuất Word / Word export ----------------------------------------------------
def _add_runs(paragraph, text: str) -> None:
    """Thêm text vào paragraph, render **bold** và _italic_ thành run định dạng."""
    for part in re.split(r"(\*\*.+?\*\*|(?<!\w)_[^_]+_(?!\w))", text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            paragraph.add_run(part[2:-2]).bold = True
        elif part.startswith("_") and part.endswith("_"):
            paragraph.add_run(part[1:-1]).italic = True
        else:
            paragraph.add_run(re.sub(r"`([^`]+)`", r"\1", part))


def export_word(vmodel: Path, out: Path) -> list:
    """Mỗi tài liệu Word-target → một file .docx (heading/đoạn/bảng/danh sách)."""
    from docx import Document

    written = []
    for name, rel in WORD_DOCS:
        path = vmodel / rel
        if not path.exists():
            continue
        doc = Document()
        for b in iter_blocks(path.read_text(encoding="utf-8")):
            kind = b[0]
            if kind == "heading":
                doc.add_heading(_strip_md(b[2]), level=min(b[1], 9))
            elif kind == "para":
                _add_runs(doc.add_paragraph(), b[1])
            elif kind == "hr":
                doc.add_paragraph().add_run("―" * 20)
            elif kind == "list":
                for checked, text in b[1]:
                    prefix = ("☑ " if checked else "☐ ") if checked is not None else ""
                    p = doc.add_paragraph(style="List Bullet")
                    p.add_run(prefix)
                    _add_runs(p, text)
            elif kind == "table":
                headers, rows = b[1], b[2]
                t = doc.add_table(rows=0, cols=len(headers))
                t.style = "Light Grid Accent 1"
                hcells = t.add_row().cells
                for c, h in zip(hcells, headers):
                    run = c.paragraphs[0].add_run(_strip_md(h))
                    run.bold = True
                for r in rows:
                    cells = t.add_row().cells
                    for c, val in zip(cells, r):
                        _add_runs(c.paragraphs[0], val)
        dst = out / f"{name}.docx"
        doc.save(dst)
        written.append(dst)
    return written


def main() -> int:
    ap = argparse.ArgumentParser(description="Export V-model docs to Excel/Word (on-demand).")
    ap.add_argument("--out", default="v-model/_export", help="Thư mục xuất / output dir.")
    ap.add_argument("--excel-only", action="store_true")
    ap.add_argument("--word-only", action="store_true")
    args = ap.parse_args()

    root = Path.cwd()
    vmodel = root / "v-model"
    if not vmodel.is_dir():
        print("ℹ Không có v-model/ — bỏ qua export.")
        return 0
    out = (root / args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)

    written = []
    if not args.word_only:
        written += export_excel(vmodel, out)
    if not args.excel_only:
        written += export_word(vmodel, out)

    if not written:
        print("ℹ Không có tài liệu nào để export.")
        return 0
    for f in written:
        print(f"✓ {f.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
