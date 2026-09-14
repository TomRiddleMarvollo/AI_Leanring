#!/usr/bin/env bash
#
# check-fn-doc.sh — Ép header chuẩn cho mỗi hàm public: phải có docstring/JSDoc
# chứa @trace và @version. Enforce a standard function header with @trace + @version.
#
# Miễn: hàm private (_), hàm một-câu-lệnh (getter/trivial), file trong .doc-coverage-ignore.
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1

echo "→ Kiểm header hàm (docstring/JSDoc có @trace + @version)"
set +e
python3 - <<'PY'
import ast, os, re, fnmatch, sys
roots = ["frontend/src", "backend/src", "backend-python/app", "shared", "packages"]
skip = {"node_modules", "dist", "build", ".git", "__pycache__", ".next", "coverage"}
ign = []
if os.path.exists(".doc-coverage-ignore"):
    for line in open(".doc-coverage-ignore", encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#"):
            ign.append(line)

def waived(p):
    b = os.path.basename(p)
    return any(fnmatch.fnmatch(p, g) or fnmatch.fnmatch(p, "*/" + g) or fnmatch.fnmatch(b, g) for g in ign)

errors = 0
def check(where, doc):
    global errors
    if doc is None:
        print(f"  ✗ {where}: thiếu header/docstring"); errors += 1; return
    if "@trace" not in doc:
        print(f"  ✗ {where}: header thiếu @trace"); errors += 1
    if "@version" not in doc:
        print(f"  ✗ {where}: header thiếu @version"); errors += 1

def real_stmts(node):
    out = []
    for s in node.body:
        if isinstance(s, ast.Expr) and isinstance(getattr(s, "value", None), ast.Constant) and isinstance(s.value.value, str):
            continue  # bỏ qua docstring
        out.append(s)
    return out

for r in roots:
    for dp, dns, fns in os.walk(r):
        dns[:] = [d for d in dns if d not in skip]
        for fn in fns:
            p = os.path.join(dp, fn)
            if waived(p):
                continue
            if fn.endswith(".py"):
                try:
                    tree = ast.parse(open(p, encoding="utf-8").read())
                except Exception:
                    continue
                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        if node.name.startswith("_"):
                            continue
                        if len(real_stmts(node)) <= 1:
                            continue  # một-câu-lệnh → miễn
                        check(f"{p}:{node.lineno} def {node.name}", ast.get_docstring(node))
            elif fn.endswith((".ts", ".tsx", ".js", ".jsx")):
                lines = open(p, encoding="utf-8").read().splitlines()
                for i, line in enumerate(lines):
                    m = re.match(r'\s*export\s+(?:async\s+)?function\s+([A-Za-z0-9_]+)', line) \
                        or re.match(r'\s*export\s+const\s+([A-Za-z0-9_]+)\s*=\s*(?:async\s*)?\([^)]*\)\s*(?::[^=]+)?=>\s*\{', line)
                    if not m:
                        continue
                    j = i - 1
                    while j >= 0 and lines[j].strip() == "":
                        j -= 1
                    if j < 0 or not lines[j].strip().endswith("*/"):
                        check(f"{p}:{i+1} {m.group(1)}", None); continue
                    k = j
                    while k >= 0 and "/**" not in lines[k]:
                        k -= 1
                    block = "\n".join(lines[k:j + 1]) if k >= 0 else ""
                    check(f"{p}:{i+1} {m.group(1)}", block if "/**" in block else None)

print(f"— fn-doc: {errors} hàm thiếu header chuẩn.")
sys.exit(1 if errors else 0)
PY
rc=$?
set -e
if [[ $STRICT -eq 1 ]]; then
  [[ $rc -eq 0 ]] && echo "✓ OK" || echo "✗ FAIL (strict): hàm thiếu header @trace/@version."
  exit $rc
fi
[[ $rc -eq 0 ]] && echo "✓ OK" || echo "(cảnh báo không chặn)"
exit 0
