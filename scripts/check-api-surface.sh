#!/usr/bin/env bash
#
# check-api-surface.sh — Ghim "public API" của mỗi lib/package để chống đổi ngầm (breaking).
# Pin the public API of each lib/package so accidental breaking changes are caught.
#
# Lấy danh sách export từ `index.ts` / `__init__.py` (có __all__), so với `.api-snapshot`.
# Khác snapshot = có thể là BREAKING → fail; nếu cố ý: `--update` rồi bump version.
#
# Dùng:
#   bash scripts/check-api-surface.sh            # kiểm tra (cảnh báo)
#   bash scripts/check-api-surface.sh --strict   # CI: đổi API -> fail
#   bash scripts/check-api-surface.sh --update   # ghi lại snapshot (khi cố ý đổi API)
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
MODE=check; STRICT=0
for a in "$@"; do case "$a" in --update) MODE=update ;; --strict) STRICT=1 ;; esac; done

echo "→ API surface (${MODE})"
set +e
python3 - "$MODE" <<'PY'
import sys, os, re, ast, glob
mode = sys.argv[1]
roots = ["frontend", "backend", "backend-python", "shared", "packages"]

def ts_exports(t):
    names = set()
    for m in re.finditer(r'export\s+(?:const|function|class|type|interface|enum)\s+([A-Za-z0-9_]+)', t):
        names.add(m.group(1))
    for m in re.finditer(r'export\s+(?:type\s+)?\{([^}]*)\}', t):
        for p in m.group(1).split(','):
            p = p.strip().replace("type ", "")
            if " as " in p:
                p = p.split(" as ")[-1].strip()
            if p:
                names.add(p)
    if re.search(r'export\s*\*\s*from', t):
        names.add("*")
    return names

def py_exports(t):
    names = set()
    try:
        tree = ast.parse(t)
    except Exception:
        return names
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for tg in node.targets:
                if isinstance(tg, ast.Name) and tg.id == "__all__" and isinstance(node.value, (ast.List, ast.Tuple)):
                    for e in node.value.elts:
                        if isinstance(e, ast.Constant):
                            names.add(str(e.value))
    return names

entries = []
for r in roots:
    for p in glob.glob(f"{r}/**/index.ts", recursive=True):
        if "/lib/" in p or "packages" in p:
            entries.append(p)
    for p in glob.glob(f"{r}/**/__init__.py", recursive=True):
        if ("/lib/" in p or "packages" in p) and "__all__" in open(p, encoding="utf-8").read():
            entries.append(p)

drift = 0; new = 0
for e in sorted(set(entries)):
    t = open(e, encoding="utf-8").read()
    names = ts_exports(t) if e.endswith((".ts", ".tsx")) else py_exports(t)
    snap = os.path.join(os.path.dirname(e), ".api-snapshot")
    cur = "\n".join(sorted(names)) + "\n" if names else ""
    if mode == "update":
        open(snap, "w", encoding="utf-8").write(cur)
        print(f"  ✓ updated {snap} ({len(names)} symbol)")
        continue
    if not os.path.exists(snap):
        print(f"  ⚠ {e}: chưa có .api-snapshot — chạy `--update` lần đầu.")
        new += 1
        continue
    old = open(snap, encoding="utf-8").read()
    if old != cur:
        oldset, newset = set(old.split()), set(cur.split())
        print(f"  ✗ {e}: PUBLIC API ĐỔI:")
        for n in sorted(newset - oldset):
            print(f"      + {n} (thêm)")
        for n in sorted(oldset - newset):
            print(f"      - {n} (XOÁ → BREAKING)")
        print("      → nếu cố ý: bump version + `check-api-surface.sh --update`.")
        drift += 1

print(f"— api-surface: {drift} đổi, {new} chưa snapshot.")
sys.exit(1 if drift else 0)
PY
rc=$?
set -e
if [[ $STRICT -eq 1 ]]; then
  [[ $rc -eq 0 ]] && echo "✓ OK" || echo "✗ FAIL (strict): public API đổi ngoài ý muốn."
  exit $rc
fi
[[ $rc -eq 0 ]] && echo "✓ OK" || echo "(cảnh báo không chặn)"
exit 0
