#!/usr/bin/env bash
# Kiểm tra license của dependencies Node. / Check Node dependency licenses.
# Fail nếu có package dùng giấy phép NGOÀI danh sách cho phép.
# Fails if any package uses a license OUTSIDE the allowlist.
#
# Dùng: chạy trong thư mục có package.json (frontend/ hoặc backend/).
# Usage: run inside a folder with package.json (frontend/ or backend/).
set -euo pipefail

# --- Danh sách giấy phép cho phép / Allowed licenses ---
# Chính sách dự án: ưu tiên MIT và Apache-2.0.
# LƯU Ý: dependency gián tiếp (transitive) thường dùng thêm ISC / BSD —
# nếu build fail vì các giấy phép permissive này, hãy thêm chúng vào đây.
# NOTE: transitive deps often use ISC / BSD; add them here if needed.
ALLOWED="MIT;Apache-2.0"
# Gợi ý mở rộng permissive an toàn (bỏ comment nếu cần):
# ALLOWED="MIT;Apache-2.0;ISC;BSD-2-Clause;BSD-3-Clause;0BSD;Unlicense"

echo "→ Checking Node licenses (allowed: ${ALLOWED})"
npx --yes license-checker-rseidelsohn \
  --production \
  --onlyAllow "${ALLOWED}" \
  --excludePrivatePackages

echo "✓ All Node dependency licenses are allowed."
