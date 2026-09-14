#!/usr/bin/env bash
#
# check-suppressions.sh — Cặp verify Code ↔ static analysis (phần tất định).
# Cấm "lách" static analysis: mọi chỉ thị suppress (nosec/noqa/eslint-disable/ts-ignore/
# type:ignore/pylint disable/pragma no cover) PHẢI có LÝ DO trên cùng dòng — nếu không → chặn.
# (SonarQube = LGPL-3.0, không dùng; SAST thật do bandit/eslint-security/ruff — MIT/Apache.)
#
set -uo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1

echo "→ Kiểm suppression static-analysis (phải có lý do)"
set +e
python3 - <<'PY'
import os, re, sys
roots = ["frontend/src", "backend/src", "backend-python/app", "shared", "packages"]
exts = (".ts", ".tsx", ".js", ".jsx", ".py")
skip = {"node_modules", "dist", "build", ".git", "__pycache__", ".next", "coverage"}
# (regex chỉ thị, phần "sau" để đo lý do)
DIRECTIVES = [
    r'#\s*nosec\b', r'#\s*noqa\b', r'#\s*type:\s*ignore', r'#\s*pylint:\s*disable',
    r'#\s*pragma:\s*no\s*cover', r'eslint-disable(?:-next-line|-line)?', r'@ts-ignore', r'@ts-nocheck',
]
pat = re.compile("|".join(f"(?:{d})" for d in DIRECTIVES))
bad = 0
for r in roots:
    for dp, dns, fns in os.walk(r):
        dns[:] = [d for d in dns if d not in skip]
        for fn in fns:
            if not fn.endswith(exts):
                continue
            p = os.path.join(dp, fn)
            try:
                lines = open(p, encoding="utf-8").read().splitlines()
            except Exception:
                continue
            for i, line in enumerate(lines, 1):
                m = pat.search(line)
                if not m:
                    continue
                after = line[m.end():]
                # bỏ rule-code (B608, security/detect-x, E501, ...) khỏi "lý do"
                after = re.sub(r'[\w/.\-]+', lambda w: '' if re.fullmatch(r'[A-Z]?[\w/.\-]*\d[\w/.\-]*', w.group()) else w.group(), after)
                letters = re.sub(r'[^A-Za-zÀ-ỹ]', '', after)
                if len(letters) < 8:
                    print(f"  ✗ {p}:{i} — suppress '{m.group().strip()}' KHÔNG có lý do (thêm lý do rõ ràng + để người duyệt)")
                    bad += 1
print(f"— suppression: {bad} chỉ thị thiếu lý do.")
sys.exit(1 if bad else 0)
PY
rc=$?
set -e
if [[ $STRICT -eq 1 ]]; then
  [[ $rc -eq 0 ]] && echo "✓ OK" || echo "✗ FAIL (strict): có suppress static-analysis không lý do."
  exit $rc
fi
[[ $rc -eq 0 ]] && echo "✓ OK" || echo "(cảnh báo không chặn)"
exit 0
