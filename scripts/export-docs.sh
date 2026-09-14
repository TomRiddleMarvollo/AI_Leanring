#!/usr/bin/env bash
#
# export-docs.sh — Đợt 2: xuất tài liệu V-model (Markdown) sang Excel/Word KHI GIAO NỘP.
# On-demand: KHÔNG chạy mỗi commit (giữ vòng lặp code nhanh). Chỉ chạy khi cần bản giao nộp.
#
# Dùng / Usage:
#   bash scripts/export-docs.sh                 # xuất cả Excel & Word vào v-model/_export/
#   bash scripts/export-docs.sh --excel-only    # chỉ Excel (REQ/SRS/Test-Spec/Test-Cases + reviews)
#   bash scripts/export-docs.sh --word-only     # chỉ Word  (Test Plan + User Manual)
#   bash scripts/export-docs.sh --out dist/docs # đổi thư mục xuất
#
# Phụ thuộc (giấy phép MIT — cài on-demand, KHÔNG nằm trong requirements.txt lõi):
#   openpyxl (Excel) · python-docx (Word).
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

[[ -d v-model ]] || { echo "ℹ Không có v-model/ — bỏ qua."; exit 0; }

PY="${PYTHON:-python3}"
need=()
"$PY" -c "import openpyxl" 2>/dev/null || need+=("openpyxl")
"$PY" -c "import docx"     2>/dev/null || need+=("python-docx")
if [[ ${#need[@]} -gt 0 ]]; then
  echo "→ Cài thư viện export (MIT): ${need[*]}"
  "$PY" -m pip install --quiet "${need[@]}"
fi

exec "$PY" "$(dirname "${BASH_SOURCE[0]}")/export_docs.py" "$@"
