#!/usr/bin/env bash
#
# check-i18n.sh — Ép i18n đầy đủ: mỗi `vi.json` và `en.json` phải có CÙNG bộ key.
# Enforce i18n parity: vi.json and en.json must share the exact same keys.
#
# CHẶN (ở --strict) nếu một key có ở ngôn ngữ này mà thiếu ở ngôn ngữ kia.
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1
echo "→ Kiểm tra i18n parity (vi ↔ en)"

set +e
python3 - <<'PY'
import json, glob, os, sys

def flat(d, p=""):
    ks = set()
    if isinstance(d, dict):
        for k, v in d.items():
            ks |= flat(v, f"{p}.{k}" if p else k)
    else:
        ks.add(p)
    return ks

pairs = []
for base in ("frontend", "backend", "backend-python", "shared"):
    for en in glob.glob(f"{base}/**/locales/en.json", recursive=True):
        if "node_modules" in en:
            continue
        pairs.append((os.path.join(os.path.dirname(en), "vi.json"), en))

bad = 0
for vi, en in pairs:
    try:
        ev = flat(json.load(open(en, encoding="utf-8")))
    except Exception as e:
        print(f"  ✗ {en}: {e}"); bad += 1; continue
    if not os.path.exists(vi):
        print(f"  ✗ Thiếu {vi} (đã có {en})"); bad += 1; continue
    try:
        vv = flat(json.load(open(vi, encoding="utf-8")))
    except Exception as e:
        print(f"  ✗ {vi}: {e}"); bad += 1; continue
    miss_vi = sorted(ev - vv)
    miss_en = sorted(vv - ev)
    if miss_vi or miss_en:
        bad += 1
        for k in miss_vi: print(f"  ✗ {vi}: thiếu key '{k}' (có trong en).")
        for k in miss_en: print(f"  ✗ {en}: thiếu key '{k}' (có trong vi).")

if not pairs:
    print("  ℹ Không tìm thấy cặp locales vi/en nào.")
print(f"— i18n: {bad} cặp lệch key.")
sys.exit(1 if bad else 0)
PY
rc=$?
set -e

if [[ $STRICT -eq 1 ]]; then
  [[ $rc -eq 0 ]] && echo "✓ OK" || echo "✗ FAIL (strict): i18n lệch key."
  exit $rc
fi
[[ $rc -eq 0 ]] && echo "✓ OK" || echo "(cảnh báo không chặn ở chế độ thường)"
exit 0
