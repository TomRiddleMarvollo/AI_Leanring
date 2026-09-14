#!/usr/bin/env bash
#
# check-circular-deps.sh — Phát hiện phụ thuộc vòng (circular dependency).
# Vòng phụ thuộc làm code khó tách thành thư viện & khó bảo trì.
#   - JS/TS: madge (MIT) nếu đã cài.
#   - Python: bộ phát hiện ast tích hợp (cho backend-python/app).
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
fails=0

echo "→ Kiểm phụ thuộc vòng (circular deps)"

# --- JS/TS: madge ---
if command -v npx >/dev/null 2>&1 && npx --no-install madge --version >/dev/null 2>&1; then
  for d in frontend/src backend/src; do
    [[ -d "$d" ]] || continue
    echo "  [js] madge --circular $d"
    npx --no-install madge --circular --extensions ts,tsx,js,jsx "$d" || { echo "  ✗ có vòng ($d)"; fails=$((fails+1)); }
  done
else
  echo "  ⚠ [js] madge chưa cài (npm i -D madge) — bỏ qua JS."
fi

# --- Python: phát hiện vòng trong backend-python/app ---
if [[ -d backend-python/app ]]; then
  set +e
  python3 - <<'PY'
import os, ast, sys
base = "backend-python"
pkgroot = os.path.join(base, "app")
graph = {}

def modname(path):
    rel = os.path.relpath(path, base).replace(os.sep, ".")
    return rel[:-3] if rel.endswith(".py") else rel

for dp, dns, fns in os.walk(pkgroot):
    for fn in fns:
        if not fn.endswith(".py"):
            continue
        path = os.path.join(dp, fn)
        mod = modname(path)
        if mod.endswith(".__init__"):
            mod = mod[:-9]
        graph.setdefault(mod, set())
        try:
            tree = ast.parse(open(path, encoding="utf-8").read())
        except Exception:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module and node.module.startswith("app"):
                graph[mod].add(node.module)

# DFS tìm chu trình
WHITE, GRAY, BLACK = 0, 1, 2
color = {n: WHITE for n in graph}
cycles = []

def dfs(n, stack):
    color[n] = GRAY
    stack.append(n)
    for m in graph.get(n, ()):
        if m not in graph:
            continue
        if color.get(m) == GRAY:
            i = stack.index(m)
            cycles.append(stack[i:] + [m])
        elif color.get(m) == WHITE:
            dfs(m, stack)
    stack.pop()
    color[n] = BLACK

for n in list(graph):
    if color[n] == WHITE:
        dfs(n, [])

if cycles:
    seen = set()
    for c in cycles:
        key = tuple(sorted(set(c)))
        if key in seen:
            continue
        seen.add(key)
        print("  ✗ [py] vòng: " + " → ".join(c))
    sys.exit(1)
sys.exit(0)
PY
  [[ $? -ne 0 ]] && fails=$((fails+1))
  set -e
fi

echo "—"
echo "Kết quả: $fails nguồn có vòng."
if [[ $STRICT -eq 1 && $fails -gt 0 ]]; then echo "✗ FAIL (strict)."; exit 1; fi
echo "✓ OK (hoặc đã bỏ qua tool thiếu)."
exit 0
