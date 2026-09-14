# Software Qualification Test — Plan (Kế hoạch)

> Tổ chức & lịch chạy Qualification Test. Chiến lược: [test-strategy.md](test-strategy.md);
> ca cụ thể: [test-cases.md](test-cases.md). Kiểm chứng `SRS-###` (đầu-cuối).

## Môi trường — Environment
- Staging giống production + dữ liệu test. Công cụ e2e: _(playwright / cypress / httpx... )_.

## Bộ ca chạy — Test suites
- Suite "Auth-qualification": `QT-001` _(thêm các QT khác...)_

## Tiêu chí vào/ra — Entry / Exit criteria
- **Vào:** unit + integration pass; hệ thống deploy được lên staging; đủ `QT` cho mỗi `SRS`.
- **Ra:** 100% `QT` pass (hoặc khiếm khuyết được duyệt); mọi `SRS` được phủ; không link truy vết đứt.

## Rủi ro — Risks
_(vd: dữ liệu staging lệch production → đồng bộ bộ dữ liệu chuẩn.)_

## Checklist review chất lượng — Quality review
- [ ] **Tiêu chí vào/ra đo được**, không chung chung.
- [ ] **Môi trường & dữ liệu test** đầu-cuối đã xác định.
- [ ] Mọi `QT` thuộc **một bộ chạy (suite)** nào đó.
- [ ] **Rủi ro** chính được nêu kèm biện pháp giảm thiểu.
