# Unit Test — Plan (Kế hoạch)

> Tổ chức & lịch chạy Unit Test. Chiến lược: [test-strategy.md](test-strategy.md);
> ca cụ thể: [test-cases.md](test-cases.md). Kiểm chứng `DD-###`.

## Môi trường — Environment
- Chạy local + CI (mỗi commit). Công cụ: _(pytest / jest / vitest... — điền theo stack)_.

## Bộ ca chạy — Test suites
- Suite "Auth-unit": `UT-001` _(thêm các UT khác...)_

## Tiêu chí vào/ra — Entry / Exit
- **Vào:** code build được; mỗi `DD` mới có UT.
- **Ra:** 100% `UT` pass; coverage đạt ngưỡng; không link truy vết đứt.

## Rủi ro — Risks
_(vd: phụ thuộc khó mock → tách interface. / Hard-to-mock deps → extract interface.)_

## Checklist review chất lượng — Quality review
- [ ] Môi trường & công cụ unit xác định; chạy được trong CI.
- [ ] **Mọi `UT` thuộc một suite**; tiêu chí vào/ra đo được.
- [ ] Rủi ro chính (mock, flaky) có biện pháp.
