# Extraction Guide — Trích xuất code thành thư viện

> Quy trình nhấc một module từ dự án ra thành **thư viện dùng lại**. Nếu module đã tuân
> CONVENTIONS.md §9 (tự đủ, không phụ thuộc app), bước này gần như chỉ là *copy*.

## A. Trước khi trích — Checklist sẵn sàng
- [ ] Module nằm gọn trong **một thư mục** `*/lib/<pkg>/` (hoặc `packages/<pkg>/`).
- [ ] Có **một cửa công khai** (`index.ts` / `__init__.py`) — bên ngoài chỉ import qua đó.
- [ ] **Không import ngược vào app** (`routes`/`services`/`store`/`config`/`app.*`...).
      Chạy: `bash scripts/check-lib-boundaries.sh` → 0 vi phạm.
- [ ] **Tự đủ:** types/errors/test/README nằm trong thư mục module.
- [ ] Phụ thuộc ngoài tối thiểu, đã liệt kê rõ.
- [ ] Lõi thuần; mọi I/O được **inject** (không gọi env/DB/global trực tiếp).
- [ ] Tên public API ổn định (coi như hợp đồng).

## B. Trích xuất (mức A — lib-in-place)
1. Copy thư mục `*/lib/<pkg>/` sang repo/thư viện mới.
2. Thêm metadata: `package.json` (Node) hoặc `pyproject.toml` (Python), trỏ `exports`/entry tới cửa công khai.
3. Khai báo dependency ngoài (đã tối thiểu) vào metadata.
4. Chạy test đi kèm — phải xanh ngay (vì module tự đủ).
5. Chọn license & version khởi đầu (vd `0.1.0`).

## C. Nâng cấp (mức B — workspace package, khi dùng ở ≥2 nơi)
1. Chuyển module vào `packages/<pkg>/` với `package.json`/`pyproject.toml` riêng
   (xem mẫu [packages/example-lib/](../packages/example-lib/) — build bằng `tsup`).
2. Cấu hình **workspace** (npm/pnpm workspaces) để app phụ thuộc qua tên package, không copy.
3. **Versioning (SemVer):** đổi public API = **major**. Ghim API bằng `check-api-surface.sh`
   (đổi → fail; nếu cố ý: `--update` + bump version + ghi `CHANGELOG.md`).
4. **Build độc lập:** `bash scripts/build-lib.sh` phải xanh (package build ra `dist/`).
5. **Không vòng phụ thuộc:** `bash scripts/check-circular-deps.sh` (vòng = khó tách).
6. Khi cần chia sẻ ra ngoài: `publish` (registry công khai hoặc nội bộ).

## D. Sau khi trích — đừng để lệch
- App cũ chuyển sang import từ package thay vì code cũ; xoá bản trùng.
- Nếu module có liên kết SDLC (`DD-###`), cập nhật tài liệu cho khớp vị trí mới.
