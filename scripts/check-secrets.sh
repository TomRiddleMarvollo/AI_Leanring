#!/usr/bin/env bash
#
# check-secrets.sh — Quét secret lỡ lọt vào code. / Scan for leaked secrets.
# Ưu tiên gitleaks (MIT); nếu chưa cài → quét regex dự phòng (yếu hơn, chỉ cảnh báo).
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[[ -n "$ROOT" ]] || ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
STRICT=0; [[ "${1:-}" == "--strict" ]] && STRICT=1

echo "→ Quét secret / Secret scan"

if command -v gitleaks >/dev/null 2>&1; then
  echo "  Dùng gitleaks (MIT)."
  if gitleaks detect --no-banner --redact 2>/dev/null; then
    echo "✓ gitleaks: không thấy secret."
    exit 0
  fi
  echo "✗ gitleaks phát hiện secret (xem trên)."
  [[ $STRICT -eq 1 ]] && exit 1 || exit 0
fi

echo "  ⚠ Chưa cài gitleaks → quét regex dự phòng (chỉ cảnh báo)."
echo "    Cài để ép thật: https://github.com/gitleaks/gitleaks"
hits=0
PATTERNS='-----BEGIN ([A-Z ]+ )?PRIVATE KEY-----|AKIA[0-9A-Z]{16}|(password|passwd|pwd|secret|api[_-]?key|access[_-]?key|token)["'"'"']?[[:space:]]*[:=][[:space:]]*["'"'"'][^"'"'"']{12,}'
while IFS= read -r line; do
  # bỏ qua placeholder / tham chiếu env (không phải secret thật)
  echo "$line" | grep -qiE 'change_me|_______|your_|xxxx|process\.env|os\.environ|getenv|<[a-z_]+>' && continue
  echo "  ⚠ $line"; hits=$((hits + 1))
done < <(grep -rniE -e "$PATTERNS" . \
          --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=dist --exclude-dir=build \
          --exclude='*.lock' --exclude='*.json' --exclude='.env.example' --exclude='*.md' 2>/dev/null || true)

echo "—"
echo "Regex dự phòng: $hits nghi vấn (có thể false positive)."
echo "✓ (cảnh báo không chặn — cài gitleaks để quét chuẩn & chặn ở CI)."
exit 0
