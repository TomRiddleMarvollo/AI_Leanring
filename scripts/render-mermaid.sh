#!/usr/bin/env bash
#
# render-mermaid.sh — Đợt 3: SAD/SDD viết kiến trúc bằng YAML (có schema) → sinh Mermaid.
# ON-DEMAND (như export Đợt 2), KHÔNG chạy mỗi commit. YAML là nguồn chân lý; Mermaid sinh ra.
#
# Dùng / Usage:
#   bash scripts/render-mermaid.sh                 # vẽ lại Mermaid vào SAD + DDD
#   bash scripts/render-mermaid.sh --check         # chỉ validate YAML schema (CI), lỗi -> exit 1
#   bash scripts/render-mermaid.sh path.md ...     # chỉ định tài liệu
#
# Phụ thuộc (MIT, cài on-demand): PyYAML.
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
[[ -d v-model ]] || { echo "ℹ Không có v-model/ — bỏ qua."; exit 0; }

PY="${PYTHON:-python3}"
"$PY" -c "import yaml" 2>/dev/null || {
  echo "→ Cài PyYAML (MIT)…"; "$PY" -m pip install --quiet pyyaml;
}

exec "$PY" "$(dirname "${BASH_SOURCE[0]}")/render_mermaid.py" "$@"
