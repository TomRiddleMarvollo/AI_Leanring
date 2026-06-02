ENV ?= dev

# ── Dev ──────────────────────────────────────────────────────
dev:
	cd environments/dev && docker compose up --build

dev-down:
	cd environments/dev && docker compose down

# Dev không dùng Docker (local nhanh nhất)
dev-local:
	@echo "Starting backend (SQLite, hot-reload)..."
	@cp environments/dev/.env src/backend/.env
	cd src/backend && uvicorn main:app --reload --port 8000 &
	@echo "Starting frontend..."
	cd src/frontend && VITE_API_URL=http://localhost:8000 npm run dev

# ── Test ─────────────────────────────────────────────────────
test:
	cd environments/test && docker compose up --build --abort-on-container-exit
	cd environments/test && docker compose down -v

test-local:
	@cp environments/test/.env src/backend/.env
	cd src/backend && pytest ../../tests/ -v --tb=short

# ── Staging ──────────────────────────────────────────────────
staging:
	cd environments/staging && docker compose up --build -d

staging-down:
	cd environments/staging && docker compose down

staging-logs:
	cd environments/staging && docker compose logs -f

# ── Production ───────────────────────────────────────────────
prod:
	@echo "Deploying to PRODUCTION..."
	@test -f environments/production/.env || (echo "ERROR: environments/production/.env not found" && exit 1)
	cd environments/production && docker compose up --build -d

prod-down:
	cd environments/production && docker compose down

prod-logs:
	cd environments/production && docker compose logs -f

# ── Utilities ────────────────────────────────────────────────
lint-backend:
	cd src/backend && python3 -m py_compile *.py && echo "All backend files OK"

status:
	@echo "=== Dev ===" && (cd environments/dev && docker compose ps 2>/dev/null || echo "stopped")
	@echo "=== Test ===" && (cd environments/test && docker compose ps 2>/dev/null || echo "stopped")
	@echo "=== Staging ===" && (cd environments/staging && docker compose ps 2>/dev/null || echo "stopped")
	@echo "=== Production ===" && (cd environments/production && docker compose ps 2>/dev/null || echo "stopped")

.PHONY: dev dev-down dev-local test test-local staging staging-down staging-logs prod prod-down prod-logs lint-backend status
