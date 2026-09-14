#!/usr/bin/env bash
# Kiểm tra license của dependencies Python. / Check Python dependency licenses.
# Fail nếu có package dùng giấy phép NGOÀI danh sách cho phép.
# Fails if any installed package uses a license OUTSIDE the allowlist.
#
# Dùng: chạy trong môi trường đã `pip install -r requirements.txt`.
# Usage: run in an environment where requirements are installed.
set -euo pipefail

# --- Danh sách giấy phép cho phép / Allowed licenses ---
# pip-licenses dùng tên dài (vd "Apache Software License"), nên liệt kê cả biến thể.
# pip-licenses uses long names (e.g. "Apache Software License"); list variants.
# LƯU Ý: nhiều thư viện Python phổ biến dùng BSD — bỏ comment dòng dưới nếu cần.
ALLOWED="MIT License;MIT;Apache Software License;Apache License 2.0;Apache 2.0"
# ALLOWED="${ALLOWED};BSD License;ISC License (ISCL);Python Software Foundation License"

echo "→ Checking Python licenses (allowed: ${ALLOWED})"
pip install --quiet pip-licenses
pip-licenses --allow-only="${ALLOWED}" --format=plain

echo "✓ All Python dependency licenses are allowed."
