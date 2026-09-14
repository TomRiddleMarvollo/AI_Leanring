#!/usr/bin/env bash
#
# lib.sh — hằng & hàm DÙNG CHUNG cho scripts/check-* và scripts/gen-*.
# Shared constants/helpers for all check/gen scripts. SOURCE file này, đừng chạy trực tiếp:
#
#   source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
#
# Sourcing tự cd về gốc repo. Đường dẫn tài liệu V-model định nghĩa MỘT nơi duy nhất —
# đổi cấu trúc thư mục chỉ sửa ở đây, không sửa rải rác từng script.

# --- về gốc repo ---
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# --- đường dẫn tài liệu V-model (một nguồn chân lý) ---
D="v-model"
HLR="$D/01-requirement/00-HLR.md"
SRS="$D/02-specification/01-SRS.md"
NFR="$D/02-specification/01b-NFR.md"
SAD="$D/03-architecture/02-SAD.md"
DDD="$D/04-detailed-design/03-DDD.md"
UT_DOC="$D/06-unit-test/test-cases.md"
IT_DOC="$D/07-integration-test/test-cases.md"
QT_DOC="$D/08-sw-qualification-test/test-cases.md"
AT_DOC="$D/09-acceptance-test/test-cases.md"
UM="$D/10-user-manual/06-USER-MANUAL.md"
SRC_DIRS="frontend backend backend-python shared"

# --- ID helpers ---
# ids_in <file> <PREFIX> -> danh sách ID duy nhất (vd REQ-001)
ids_in() { grep -hoE "$2-[0-9]{3}" "$1" 2>/dev/null | sort -u; }
# has_id <file> <ID> -> ID có xuất hiện trong file không.
# LƯU Ý regex: KHÔNG dùng \b — đã dính bug với markdown _italic_ (underscore là ký tự word).
has_id() { grep -qE "(^|[^0-9A-Za-z])$2([^0-9]|$)" "$1" 2>/dev/null; }
# in_list <ID> <danh-sách-nhiều-dòng> -> ID có trong danh sách không
in_list() { printf '%s\n' "$2" | grep -qxF "$1"; }
