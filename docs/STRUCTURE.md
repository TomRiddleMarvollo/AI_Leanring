# Project Structure Guide — Hướng dẫn cấu trúc dự án

> Tài liệu này mô tả cách tổ chức source code để **dễ bảo trì** và giúp người đọc
> (kể cả khi code do AI sinh ra) **hiểu nhanh** vị trí và vai trò của từng phần.
> _This document explains how the source is organized so it stays maintainable and
> easy to understand — including AI-generated code._

---

## Nguyên tắc tổ chức — Organizing principles

1. **Tách theo vai trò (separation of concerns).** Mỗi thư mục có **một trách nhiệm rõ ràng**. Không trộn UI với logic gọi API, không trộn business logic với truy vấn DB.
2. **Tên nói lên nội dung.** Đặt tên file/folder mô tả đúng thứ bên trong. Người đọc đoán được vai trò mà không cần mở file.
3. **Mỗi thư mục lớn có một `README.md`** giải thích mục đích, quy ước đặt tên, và "đặt cái gì vào đây".
4. **Phụ thuộc đi một chiều.** Frontend → gọi API qua `services/`. Backend: `routes → controllers → services → models`. Không nhảy cóc, không gọi ngược.
5. **Đa ngôn ngữ tách riêng.** Mọi chuỗi hiển thị nằm trong `locales/` (`vi`, `en`), không hardcode.

---

## Toàn cảnh cây thư mục — Directory tree

```
project-root/
├── CLAUDE.md                 # Harness RIÊNG — cài thủ công, KHÔNG commit (xem README)
├── AGENTS.md                 # Hướng dẫn cho mọi AI agent (Codex...) — commit công khai
├── CONVENTIONS.md            # Quy ước code (nguồn chuẩn cho người + agent)
├── CODEMAP.md                # Bản đồ repo: "sửa X thì vào Y" — tiết kiệm token
├── README.md                 # Giới thiệu dự án, cách chạy
├── .env.example              # Mẫu biến môi trường (KHÔNG chứa secret thật)
├── .gitignore
│
├── scripts/                  # Script tiện ích
│   ├── setup-project.sh      #   Chạy 1 lần: bật hook + auto-điền lệnh
│   ├── gen-commands.sh       #   Tự điền lệnh build/test vào AGENTS.md
│   ├── check-docs.sh         #   Nhắc cập nhật tài liệu (lint)
│   ├── check-licenses-*.sh   #   Kiểm tra license MIT/Apache-2.0
│   └── git-hooks/pre-commit  #   Hook tự nhắc trước mỗi commit
├── .github/workflows/        # CI: docs-check.yml, license-check.yml
│
├── docs/                     # Tài liệu dự án
│   ├── STRUCTURE.md          # File này
│   ├── GLOSSARY.md           # Từ điển thuật ngữ Việt/Anh (đặt tên nhất quán)
│   ├── adr/                  # Architecture Decision Records — nhật ký quyết định
│   └── (SDLC chuyển sang ../v-model/ — mỗi phase một folder + checklist/report)
│
├── shared/                   # Code dùng chung cho cả FE & BE
│   └── types/                # Kiểu dữ liệu / interface dùng chung (vd: User, ApiResponse)
│
├── frontend/                 # Ứng dụng phía client
│   ├── src/
│   │   ├── app/              # Routes / pages / entrypoint (Next.js app router)
│   │   ├── components/
│   │   │   ├── ui/           # Component tái sử dụng, "ngu" (Button, Input, Modal)
│   │   │   └── features/     # Component gắn nghiệp vụ (LoginForm, ProductCard)
│   │   ├── hooks/            # Custom React hooks (useAuth, useDebounce)
│   │   ├── lib/              # Helper thuần, không phụ thuộc UI (format, validate)
│   │   ├── services/         # Lớp gọi API tới backend (apiClient, userService)
│   │   ├── store/            # State toàn cục (Redux/Zustand/Context)
│   │   ├── types/            # Kiểu dữ liệu riêng của frontend
│   │   ├── styles/           # CSS/Tailwind/theme toàn cục
│   │   └── locales/          # i18n: vi.json, en.json
│   └── tests/                # Test cho frontend
│
│                             # (Backend Python/FastAPI: xem thư mục `backend-python/`)
└── backend/                  # API / server phía máy chủ (Node)
    ├── src/
    │   ├── routes/           # Khai báo endpoint, map URL → controller
    │   ├── controllers/      # Nhận request, validate input, gọi service, trả response
    │   ├── services/         # Business logic — TRÁI TIM của ứng dụng
    │   ├── models/           # Schema / truy cập dữ liệu (ORM, DB)
    │   ├── middlewares/      # Auth, logging, error handler, rate limit
    │   ├── config/           # Cấu hình (db, env, constants)
    │   ├── utils/            # Helper thuần dùng lại nhiều nơi
    │   ├── types/            # Kiểu dữ liệu riêng của backend
    │   └── locales/          # i18n cho thông báo server: vi.json, en.json
    └── tests/                # Test cho backend
```

---

## Luồng dữ liệu — Data flow

**Frontend:**
```
User → app/ (page) → components/ → hooks/ → services/ (gọi API) → backend
```

**Backend (mỗi request):**
```
routes/ → middlewares/ (auth, validate) → controllers/ → services/ (logic) → models/ (DB) → trả về
```

> Quy tắc vàng: **controller mỏng, service dày.** Controller chỉ điều phối; mọi logic nghiệp vụ nằm ở `services/`. Điều này giúp test dễ và tái sử dụng tốt.

---

## Quy ước đặt tên — Naming conventions

| Loại | Quy ước | Ví dụ |
|------|---------|-------|
| Component (React) | PascalCase | `ProductCard.tsx` |
| Hook | camelCase, prefix `use` | `useAuth.ts` |
| Service / util | camelCase | `userService.ts`, `formatDate.ts` |
| Type / Interface | PascalCase | `User`, `ApiResponse` |
| Folder | kebab-case hoặc camelCase (nhất quán) | `user-profile/` |
| Hằng số | UPPER_SNAKE_CASE | `MAX_RETRY` |
| File test | `*.test.ts` / `*.spec.ts` | `userService.test.ts` |

> _Quan trọng: chọn MỘT bộ quy ước và giữ nhất quán toàn dự án._

---

## Khi thêm tính năng mới — Adding a feature (checklist)

1. Có **type dùng chung** không? → thêm vào `shared/types/`.
2. **Backend:** thêm `route` → `controller` → `service` (→ `model` nếu chạm DB).
3. **Frontend:** thêm hàm gọi API trong `services/` → `hook` (nếu cần) → `component`.
4. **Chuỗi hiển thị:** thêm key vào `locales/vi.json` **và** `locales/en.json`.
5. **Test:** thêm test cho phần logic quan trọng.
6. **Tài liệu:** quyết định kiến trúc lớn → ghi một ADR trong `docs/adr/`.

---

## Vì sao cấu trúc này dễ cho người đọc (và AI) — Why this is readable

- **Đoán được vị trí:** cần sửa logic tính tiền? → `backend/src/services/`. Cần đổi nút bấm? → `frontend/src/components/ui/`.
- **README mỗi tầng:** mở folder là biết nên đặt gì vào.
- **Một chiều phụ thuộc:** đọc code theo luồng, không bị nhảy vòng vo.
- **Ranh giới rõ:** dễ review, dễ tách module, dễ viết test.
