#!/usr/bin/env bash
#
# check-code-doc-coverage.sh — Ép tài liệu thiết kế phủ 100% mã CHỨC NĂNG.
# Every functional source file must trace to a DD-### (or be waived in .doc-coverage-ignore).
#
# Mỗi file mã (trừ hạ tầng/test/lib/type được waive) phải chứa comment `DD-###`.
# File không phủ & không waive → vi phạm (CHẶN ở --strict).
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1

echo "→ Phủ code↔doc (mỗi file chức năng phải trace tới DD-###)"
set +e
python3 - <<'PY'
import os, re, fnmatch, sys
roots = ["frontend/src", "backend/src", "backend-python/app", "shared", "packages"]
exts = (".ts", ".tsx", ".js", ".jsx", ".py")
skip = {"node_modules", "dist", "build", ".git", "__pycache__", ".next", "coverage"}

ign = []
if os.path.exists(".doc-coverage-ignore"):
    for line in open(".doc-coverage-ignore", encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#"):
            ign.append(line)

def waived(p):
    base = os.path.basename(p)
    return any(fnmatch.fnmatch(p, g) or fnmatch.fnmatch(p, "*/" + g) or fnmatch.fnmatch(base, g) for g in ign)

dd = re.compile(r'\bDD-[0-9]{3}\b')
checked = missing = 0
for r in roots:
    for dp, dns, fns in os.walk(r):
        dns[:] = [d for d in dns if d not in skip]
        for fn in fns:
            if not fn.endswith(exts):
                continue
            p = os.path.join(dp, fn)
            if waived(p):
                continue
            checked += 1
            if not dd.search(open(p, encoding="utf-8").read()):
                print(f"  ✗ {p}: chưa trace DD-### → thêm comment `DD-xxx` hoặc waive trong .doc-coverage-ignore")
                missing += 1

cov = 100 if checked == 0 else round((checked - missing) * 100 / checked)
print(f"— doc-coverage: {checked - missing}/{checked} file phủ ({cov}%).")
sys.exit(1 if missing else 0)
PY
rc=$?
set -e
if [[ $STRICT -eq 1 ]]; then
  [[ $rc -eq 0 ]] && echo "✓ OK (phủ 100%)" || echo "✗ FAIL (strict): còn mã chưa phủ tài liệu."
  exit $rc
fi
[[ $rc -eq 0 ]] && echo "✓ OK" || echo "(cảnh báo không chặn)"
exit 0
