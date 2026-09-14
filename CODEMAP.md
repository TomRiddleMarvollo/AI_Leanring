# CODEMAP — Bản đồ repo

> Một trang để định vị nhanh: **"muốn sửa X thì vào đâu"**. Người mới onboard nhanh;
> AI agent đọc file này thay vì dò cả repo → **tiết kiệm token**.
> _One-page map: where to change what. Keep it SHORT and current, or delete it —
> a stale map is worse than none._

> ⚠️ Giữ NGẮN và cập nhật khi thêm/di chuyển thành phần lớn. Đây là ví dụ mẫu, hãy
> sửa cho khớp dự án thật.

---

## Entry points — Điểm khởi đầu
| Chạy gì | File |
|---------|------|
| Frontend khởi động | `frontend/src/app/` |
| Backend khởi động | `backend/src/index.ts` _(hoặc `backend-python/app/main.py`)_ |
| Cấu hình / env | `backend/src/config/` · `.env` |

## Muốn sửa... thì vào — Where to change what
| Bạn muốn... | Vào... |
|-------------|--------|
| Thêm/sửa một màn hình UI | `frontend/src/app/` + `frontend/src/components/` |
| Sửa logic gọi API ở client | `frontend/src/services/` |
| Thêm một API endpoint | `backend/src/routes/` → `controllers/` → `services/` |
| Sửa business logic | `backend/src/services/` |
| Sửa cấu trúc dữ liệu / DB | `backend/src/models/` |
| Thêm/sửa chuỗi hiển thị | `*/locales/vi.json` + `en.json` |
| Kiểu dữ liệu dùng chung FE+BE | `shared/types/` |

## Luồng dữ liệu — Data flow
```
UI (app/, components/) → services/ (client) → API
API: routes → controllers → services → models → DB
```

## Module chính — Key modules
> Liệt kê 5–10 module quan trọng nhất + một câu mô tả. / Top modules, one line each.
- `services/auth` — _đăng nhập, JWT, phân quyền._
- `services/...` — _..._

## Quy ước & tài liệu liên quan — Related docs
- Quy ước code: [CONVENTIONS.md](CONVENTIONS.md)
- Cấu trúc chi tiết: [docs/STRUCTURE.md](docs/STRUCTURE.md)
- Thuật ngữ: [docs/GLOSSARY.md](docs/GLOSSARY.md)
