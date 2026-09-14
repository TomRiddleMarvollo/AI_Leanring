#!/usr/bin/env python3
"""new_feature.py — Scaffold một feature xuyên ĐỦ chuỗi V-model, ID khớp sẵn & liên kết đúng.

Ma sát lớn khi thêm 1 tính năng: phải chạm ~11 phase, tự đặt ID và điền `Traces` cho khớp.
Script này sinh **bộ stub liên kết sẵn** (một số thứ tự `N` dùng chung, không đụng ID cũ) để
`check-traceability` XANH ngay (liên kết đủ), còn nội dung để `_(TODO)_` cho người/agent điền —
`check-completeness` sẽ chỉ đúng chỗ cần điền. CHỈ THÊM (append), không sửa nội dung sẵn có.

Chuỗi sinh: REQ → SRS → ARC → DD → UT · IT · QT · AT  (+ NFR với --nfr, + SCR với --screen).

Dùng:
  python3 new_feature.py "Tên tính năng" [--nfr] [--screen]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

V = Path("v-model")

# (khoá, đường-dẫn) các tài liệu cần quét/chèn.
DOCS = {
    "REQ": V / "01-requirement/00-HLR.md",
    "SRS": V / "02-specification/01-SRS.md",
    "NFR": V / "02-specification/01b-NFR.md",
    "ARC": V / "03-architecture/02-SAD.md",
    "DD": V / "04-detailed-design/03-DDD.md",
    "UT": V / "06-unit-test/test-cases.md",
    "IT": V / "07-integration-test/test-cases.md",
    "QT": V / "08-sw-qualification-test/test-cases.md",
    "AT": V / "09-acceptance-test/test-cases.md",
    "SCR": V / "10-user-manual/06-USER-MANUAL.md",
}


def max_id(text: str, prefix: str) -> int:
    nums = [int(m) for m in re.findall(rf"{prefix}-(\d{{3}})", text)]
    return max(nums, default=0)


def next_number() -> int:
    """Số thứ tự dùng chung cho feature = 1 + max mọi ID hiện có (không đụng ID cũ)."""
    hi = 0
    for prefix, path in DOCS.items():
        if path.exists():
            hi = max(hi, max_id(path.read_text(encoding="utf-8"), prefix))
    return hi + 1


def insert_table_row(path: Path, prefix: str, row: str, report: list) -> None:
    """Chèn 1 dòng bảng NGAY SAU dòng ID cuối cùng của prefix đó (giữ bảng liền mạch)."""
    lines = path.read_text(encoding="utf-8").split("\n")
    num = [i for i, l in enumerate(lines) if re.match(rf"^\|\s*{prefix}-\d{{3}}\b", l)]
    skel = [i for i, l in enumerate(lines) if re.match(rf"^\|\s*{prefix}-", l)]
    at = (max(num) + 1) if num else ((max(skel) + 1) if skel else len(lines))
    lines.insert(at, row)
    path.write_text("\n".join(lines), encoding="utf-8")
    report.append(f"{path} ← {row.split('|')[1].strip()}")


DD_SUBS = ["Functions / APIs", "Happy path", "Error & alternate flows",
           "Sequence diagram", "Validation", "Security", "Data model"]


def insert_dd_section(path: Path, n: int, arc: str, title: str, report: list) -> None:
    """Chèn khối '### DD-00N' (đủ 7 tiểu mục, để _(TODO)_) trước mục '## Checklist review'."""
    dd = f"DD-{n:03d}"
    block = [f"### {dd}: {title}", f"_Traces: {arc}_", ""]
    for h in DD_SUBS:
        block += [f"#### {h}", "_(TODO)_", ""]
    lines = path.read_text(encoding="utf-8").split("\n")
    idx = next((i for i, l in enumerate(lines) if l.startswith("## Checklist review")), len(lines))
    lines[idx:idx] = block
    path.write_text("\n".join(lines), encoding="utf-8")
    report.append(f"{path} ← {dd} (section, 7 tiểu mục TODO)")


def insert_scr_section(path: Path, n: int, req: str, title: str, report: list) -> None:
    scr = f"SCR-{n:03d}"
    # dòng inventory + khối chi tiết (4 tiểu mục).
    insert_table_row(path, "SCR", f"| {scr} | {title} | `/(TODO)` | {req} |", report)
    block = [f"### {scr}: {title}", f"_Route: `/(TODO)` · Traces: {req}_", "",
             "#### Purpose", "_(TODO)_", "", "#### Steps", "_(TODO)_", "",
             "#### Transitions", "_(TODO)_", "", "#### Error & empty states", "_(TODO)_", ""]
    lines = path.read_text(encoding="utf-8").split("\n")
    idx = next((i for i, l in enumerate(lines) if l.startswith("## Checklist review")), len(lines))
    lines[idx:idx] = block
    path.write_text("\n".join(lines), encoding="utf-8")
    report.append(f"{path} ← {scr} (section)")


def main() -> int:
    ap = argparse.ArgumentParser(description="Scaffold a feature across the V-model chain.")
    ap.add_argument("title", help="Tên tính năng (vd: 'Quên mật khẩu').")
    ap.add_argument("--nfr", action="store_true", help="Kèm một NFR (phi chức năng) + gắn vào QT.")
    ap.add_argument("--screen", action="store_true", help="Kèm một màn hình SCR trong User Manual.")
    a = ap.parse_args()

    if not V.is_dir():
        print("✗ Không thấy v-model/ — chạy ở gốc dự án.", file=sys.stderr)
        return 1

    n = next_number()
    t = a.title.strip()
    ids = {p: f"{p}-{n:03d}" for p in ("REQ", "SRS", "NFR", "ARC", "DD", "UT", "IT", "QT", "AT", "SCR")}
    report: list = []

    insert_table_row(DOCS["REQ"], "REQ", f"| {ids['REQ']} | {t} _(TODO mô tả)_ | Trung bình | Scaffold — điền thật. |", report)
    insert_table_row(DOCS["SRS"], "SRS", f"| {ids['SRS']} | _(TODO đặc tả chi tiết: {t})_ | {ids['REQ']} | _(TODO tiêu chí chấp nhận)_ |", report)
    arc_note = f" (thoả {ids['NFR']})" if a.nfr else ""
    insert_table_row(DOCS["ARC"], "ARC", f"| {ids['ARC']} | _(TODO thành phần: {t})_ | _(TODO trách nhiệm){arc_note}_ | {ids['SRS']} |", report)
    insert_dd_section(DOCS["DD"], n, ids["ARC"], t, report)
    insert_table_row(DOCS["UT"], "UT", f"| {ids['UT']} | _(TODO ca unit: {t})_ | {ids['DD']} | _(TODO)_ | _(TODO)_ |", report)
    insert_table_row(DOCS["IT"], "IT", f"| {ids['IT']} | _(TODO ca tích hợp: {t})_ | {ids['ARC']} | _(TODO)_ | _(TODO)_ |", report)
    qt_note = f" (kiểm {ids['NFR']})" if a.nfr else ""
    insert_table_row(DOCS["QT"], "QT", f"| {ids['QT']} | _(TODO đầu-cuối: {t}){qt_note}_ | {ids['SRS']} | _(TODO)_ | _(TODO)_ |", report)
    insert_table_row(DOCS["AT"], "AT", f"| {ids['AT']} | _(TODO nghiệm thu: {t})_ | {ids['REQ']} | _(TODO)_ | _(TODO)_ |", report)

    if a.nfr:
        insert_table_row(DOCS["NFR"], "NFR", f"| {ids['NFR']} | _(TODO loại)_ | _(TODO ngưỡng đo)_ | {ids['QT']} | {ids['REQ']} |", report)
    if a.screen:
        insert_scr_section(DOCS["SCR"], n, ids["REQ"], t, report)

    print(f"✓ Scaffold feature '{t}' — số thứ tự chung: {n:03d}")
    for r in report:
        print(f"  + {r}")
    print("\nChuỗi liên kết (check-traceability sẽ XANH; check-completeness chỉ chỗ cần điền):")
    chain = f"  {ids['REQ']} → {ids['SRS']} → {ids['ARC']} → {ids['DD']} → code; " \
            f"test: {ids['UT']}↔DD · {ids['IT']}↔ARC · {ids['QT']}↔SRS · {ids['AT']}↔REQ"
    if a.nfr:
        chain += f"; {ids['NFR']}↔{ids['QT']}"
    print(chain)
    print("→ Điền nội dung thật rồi chạy: bash scripts/check-traceability.sh && bash scripts/check-completeness.sh")
    return 0


if __name__ == "__main__":
    sys.exit(main())
