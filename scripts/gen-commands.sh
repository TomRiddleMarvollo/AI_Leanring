#!/usr/bin/env bash
#
# gen-commands.sh — Tự ĐIỀN lệnh build/test vào AGENTS.md (phần giữa mốc AUTO-COMMANDS)
# từ package.json / requirements.txt. / Auto-fill build & test commands in AGENTS.md.
#
# Chạy lại bất cứ lúc nào sau khi thêm script vào package.json.
# Re-run anytime after changing package.json scripts.
#
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

AGENTS="AGENTS.md"
[[ -f "$AGENTS" ]] || { echo "✗ Không thấy $AGENTS"; exit 1; }
grep -q 'AUTO-COMMANDS:START' "$AGENTS" || { echo "✗ $AGENTS thiếu mốc AUTO-COMMANDS"; exit 1; }

# Package manager theo lockfile / detect package manager by lockfile.
pm_for() {
  if   [[ -f "$1/pnpm-lock.yaml" ]]; then echo pnpm
  elif [[ -f "$1/yarn.lock"      ]]; then echo yarn
  else echo npm; fi
}
# Lấy giá trị một script trong package.json (rỗng nếu không có).
has_script() {
  python3 -c "import json
try: print(json.load(open('$1')).get('scripts',{}).get('$2',''))
except Exception: print('')" 2>/dev/null
}

emit_node() {  # $1=nhãn  $2=thư mục
  local label="$1" dir="$2" pj pm cdp
  pj="$dir/package.json"; pj="${pj#./}"
  pm="$(pm_for "$dir")"
  [[ "$dir" == "." ]] && cdp="" || cdp="cd ${dir#./} && "
  echo "**$label** — package manager: \`$pm\`"
  case "$pm" in
    pnpm) echo "- Install: \`${cdp}pnpm install\`" ;;
    yarn) echo "- Install: \`${cdp}yarn\`" ;;
    *)    echo "- Install: \`${cdp}npm install\`" ;;
  esac
  local s
  for s in dev start serve; do
    if [[ -n "$(has_script "$pj" "$s")" ]]; then
      [[ "$pm" == npm ]] && echo "- Run: \`${cdp}npm run $s\`" || echo "- Run: \`${cdp}$pm $s\`"
      break
    fi
  done
  if [[ -n "$(has_script "$pj" test)" ]]; then
    [[ "$pm" == npm ]] && echo "- Test: \`${cdp}npm test\`" || echo "- Test: \`${cdp}$pm test\`"
  fi
  if [[ -n "$(has_script "$pj" lint)" ]]; then
    [[ "$pm" == npm ]] && echo "- Lint: \`${cdp}npm run lint\`" || echo "- Lint: \`${cdp}$pm lint\`"
  fi
  echo
}

emit_python() {  # $1=nhãn  $2=thư mục
  local label="$1" dir="${2#./}" cdp="cd ${2#./} && "
  echo "**$label**"
  if   [[ -f "$2/requirements.txt" ]]; then echo "- Install: \`${cdp}pip install -r requirements.txt\`"
  elif [[ -f "$2/pyproject.toml"   ]]; then echo "- Install: \`${cdp}pip install -e .\`"; fi
  [[ -f "$2/app/main.py" ]] && echo "- Run: \`${cdp}uvicorn app.main:app --reload\`"
  echo "- Test: \`${cdp}pytest\`"
  echo
}

TMP="$(mktemp)"
found=0
[[ -f package.json          ]] && { emit_node "App" "." >>"$TMP"; found=1; }
[[ -f frontend/package.json ]] && { emit_node "Frontend (\`frontend/\`)" "frontend" >>"$TMP"; found=1; }
[[ -f backend/package.json  ]] && { emit_node "Backend (\`backend/\`)" "backend" >>"$TMP"; found=1; }
if [[ -f backend-python/requirements.txt || -f backend-python/pyproject.toml ]]; then
  emit_python "Backend — Python (\`backend-python/\`)" "backend-python" >>"$TMP"; found=1
fi

if [[ $found -eq 0 ]]; then
  { echo "- Install: \`_______\`"; echo "- Run: \`_______\`"; echo "- Test: \`_______\`"; } >>"$TMP"
  echo "ℹ Không phát hiện package.json/requirements.txt — để '_______' cho bạn điền tay."
fi

# Thay nội dung giữa hai mốc AUTO-COMMANDS.
awk -v f="$TMP" '
  BEGIN { while ((getline l < f) > 0) b = b l ORS }
  /AUTO-COMMANDS:START/ { print; printf "%s", b; insec=1; next }
  /AUTO-COMMANDS:END/   { insec=0 }
  !insec
' "$AGENTS" > "$AGENTS.tmp" && mv "$AGENTS.tmp" "$AGENTS"
rm -f "$TMP"
echo "✓ Đã cập nhật phần Commands trong $AGENTS"
