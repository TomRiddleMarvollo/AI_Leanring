#!/usr/bin/env bash
#
# new-feature.sh — Scaffold một tính năng xuyên ĐỦ chuỗi V-model với ID khớp sẵn.
# Sinh stub liên kết (REQ→SRS→ARC→DD→UT/IT/QT/AT) để check-traceability XANH ngay;
# nội dung để _(TODO)_ cho bạn/agent điền. CHỈ THÊM, không sửa nội dung sẵn có.
#
# Dùng / Usage:
#   bash scripts/new-feature.sh "Quên mật khẩu"            # chuỗi cơ bản
#   bash scripts/new-feature.sh "Xuất báo cáo" --nfr       # kèm 1 NFR (gắn vào QT)
#   bash scripts/new-feature.sh "Trang hồ sơ" --screen     # kèm 1 màn hình (User Manual)
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
[[ -d v-model ]] || { echo "ℹ Không có v-model/ — bỏ qua."; exit 0; }

exec python3 "$(dirname "${BASH_SOURCE[0]}")/new_feature.py" "$@"
