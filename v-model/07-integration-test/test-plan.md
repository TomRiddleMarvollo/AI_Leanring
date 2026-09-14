# Integration Test — Plan (Kế hoạch)

> Tổ chức & lịch chạy Integration Test. Chiến lược: [test-strategy.md](test-strategy.md);
> ca cụ thể: [test-cases.md](test-cases.md). Kiểm chứng `ARC-###`.

## Môi trường — Environment
- DB/queue thật (hoặc container) + service ghép. Công cụ: _(testcontainers / supertest / httpx... )_.

## Bộ ca chạy — Test suites
- Suite "Auth-integration": `IT-001` _(thêm các IT khác...)_

## Tiêu chí vào/ra — Entry / Exit
- **Vào:** unit pass; thành phần build & deploy được vào môi trường tích hợp.
- **Ra:** 100% `IT` pass; mọi `ARC` được phủ; không link truy vết đứt.

## Rủi ro — Risks
_(vd: phụ thuộc dịch vụ ngoài không ổn định → dùng double ở biên.)_

## Checklist review chất lượng — Quality review
- [ ] Môi trường tích hợp & dữ liệu xác định, dựng lại được.
- [ ] **Mọi `IT` thuộc một suite**; tiêu chí vào/ra đo được.
- [ ] Rủi ro tích hợp chính có biện pháp.
