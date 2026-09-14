#!/usr/bin/env bash
#
# gen-code-trace.sh — Trích bản đồ truy vết TỪ CODE theo chú thích `@trace <ID>`.
# Extract a code→ID traceability map from `@trace <ID>` annotations in source.
# Sinh v-model/_traceability/CODE-TRACE.md (file → các ID). Đừng sửa tay file output.
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
[[ -d v-model ]] || { echo "ℹ Không có v-model — bỏ qua."; exit 0; }
OUT="v-model/_traceability/CODE-TRACE.md"

TMP="$(mktemp)"
{
  echo "# Code Trace — Truy vết từ code (sinh tự động)"
  echo
  echo "> Trích từ chú thích \`@trace <ID>\` trong source bằng \`scripts/gen-code-trace.sh\`."
  echo "> **Đừng sửa tay.** Quy ước: đánh dấu \`@trace DD-001\` (hoặc nhiều ID) tại file/hàm/lớp."
  echo
  echo "| File | Trace IDs |"
  echo "|------|-----------|"
  python3 - <<'PY'
import os, re
roots = ["frontend/src", "backend/src", "backend-python/app", "shared", "packages"]
exts = (".ts", ".tsx", ".js", ".jsx", ".py")
skip = {"node_modules", "dist", "build", ".git", "__pycache__", ".next", "coverage"}
pat = re.compile(r'@trace\s+((?:[A-Z]+-[0-9]{3}[ ,]*)+)')
rows = []
for r in roots:
    for dp, dns, fns in os.walk(r):
        dns[:] = [d for d in dns if d not in skip]
        for fn in fns:
            if not fn.endswith(exts):
                continue
            p = os.path.join(dp, fn)
            ids = set()
            for m in pat.finditer(open(p, encoding="utf-8").read()):
                ids.update(re.findall(r'[A-Z]+-[0-9]{3}', m.group(1)))
            if ids:
                rows.append((p, sorted(ids)))
for p, ids in sorted(rows):
    print(f"| `{p}` | {', '.join('`%s`' % i for i in ids)} |")
if not rows:
    print("| _(chưa có @trace trong code)_ | — |")
PY
} > "$TMP"
mv "$TMP" "$OUT"
echo "✓ Đã cập nhật $OUT"
