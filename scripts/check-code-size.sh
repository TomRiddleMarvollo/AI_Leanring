#!/usr/bin/env bash
#
# check-code-size.sh — Ép "boring code": giới hạn kích thước file & hàm.
# Enforce boring-code size limits (deterministic, không cần tool ngoài).
#   - File > MAX_FILE dòng (mặc định 300)  → vi phạm
#   - Hàm Python > MAX_FUNC dòng (mặc định 50) → vi phạm (JS để eslint lo)
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
export MAX_FILE="${MAX_FILE:-300}" MAX_FUNC="${MAX_FUNC:-50}"

echo "→ Kiểm kích thước code (file ≤ $MAX_FILE dòng, hàm Python ≤ $MAX_FUNC dòng)"
set +e
python3 - <<'PY'
import os, ast, sys
maxf = int(os.environ["MAX_FILE"]); maxfn = int(os.environ["MAX_FUNC"])
roots = ["frontend", "backend", "backend-python", "shared", "packages"]
exts = (".ts", ".tsx", ".js", ".jsx", ".py")
skip = {"node_modules", "dist", "build", ".git", "__pycache__", ".next", "coverage"}
errors = 0
for r in roots:
    for dp, dns, fns in os.walk(r):
        dns[:] = [d for d in dns if d not in skip]
        for fn in fns:
            if not fn.endswith(exts):
                continue
            path = os.path.join(dp, fn)
            try:
                lines = open(path, encoding="utf-8").read().splitlines()
            except Exception:
                continue
            if len(lines) > maxf:
                print(f"  ✗ {path}: {len(lines)} dòng > {maxf} → tách nhỏ file")
                errors += 1
            if fn.endswith(".py"):
                try:
                    tree = ast.parse("\n".join(lines))
                except Exception:
                    continue
                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        n = (node.end_lineno or node.lineno) - node.lineno + 1
                        if n > maxfn:
                            print(f"  ✗ {path}:{node.lineno} hàm '{node.name}' {n} dòng > {maxfn} → tách hàm")
                            errors += 1
print(f"— size: {errors} vi phạm.")
sys.exit(1 if errors else 0)
PY
rc=$?
set -e
if [[ $STRICT -eq 1 ]]; then
  [[ $rc -eq 0 ]] && echo "✓ OK" || echo "✗ FAIL (strict): vượt giới hạn kích thước."
  exit $rc
fi
[[ $rc -eq 0 ]] && echo "✓ OK" || echo "(cảnh báo không chặn)"
exit 0
