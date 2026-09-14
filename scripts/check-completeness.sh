#!/usr/bin/env bash
#
# check-completeness.sh — Ép ĐỘ ĐẦY ĐỦ của tài liệu thiết kế & hướng dẫn.
# Enforce documentation DEPTH (not just structure/traceability).
#
# CHẶN (error, exit 1 ở --strict):
#   - Mỗi `### DD-###` (Detailed Design) thiếu một trong 7 tiểu mục bắt buộc, hoặc tiểu mục bỏ trống.
#   - Mỗi `### SCR-###` (User Manual) thiếu một trong 4 tiểu mục bắt buộc, hoặc tiểu mục bỏ trống.
#   - Mỗi `NFR-###` không có ngưỡng đo (cột target trống).
#   - Threat model (SAD): thiếu hẳn mục Threat model/STRIDE (không có mục nào).
# CẢNH BÁO (warn, không chặn — HEURISTIC, dễ bắt hụt/bắt nhầm, cần mắt người xác nhận):
#   - Tiểu mục có nội dung nhưng quá sơ sài (< 20 ký tự); NFR không có SỐ đo;
#   - Threat model thiếu loại STRIDE / biện pháp sơ sài; SRS thiếu modal EARS;
#   - DD Functions/APIs thiếu đầu ra / ca lỗi; nút i18n chưa có trong User Manual;
#   - route/endpoint trong code chưa nhắc trong UM/DDD.
#
# Opt-out theo project (.harness-config): REQUIRE_THREAT_MODEL=0 · REQUIRE_NFR_QUANTITATIVE=0 ·
#   REQUIRE_UM_BUTTONS=0 · REQUIRE_EARS_SRS=0 · REQUIRE_DD_CONTRACT=0
#
# Logic nằm ở scripts/check_completeness.py (chuyển từ bash/awk sang Python cho dễ bảo trì);
# file này chỉ là wrapper giữ nguyên giao diện `bash scripts/check-completeness.sh [--strict]`.
#
set -euo pipefail
exec python3 "$(dirname "${BASH_SOURCE[0]}")/check_completeness.py" "$@"
