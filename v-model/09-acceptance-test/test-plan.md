# Acceptance Test — Plan (Kế hoạch)

> Tổ chức & lịch nghiệm thu. Chiến lược: [test-strategy.md](test-strategy.md); ca: [test-cases.md](test-cases.md).
> Kiểm chứng `REQ-###` (góc nhìn người dùng).

## Môi trường & bên tham gia — Environment & actors
- Môi trường giống production (staging nghiệm thu); có bên **nghiệp vụ/chủ sản phẩm** ký duyệt.

## Bộ ca chạy — Test suites
- Suite "Auth-acceptance": `AT-001` _(thêm các AT khác...)_

## Tiêu chí vào/ra — Entry / Exit
- **Vào:** UT+IT+SQT pass; build deploy được lên môi trường nghiệm thu.
- **Ra:** 100% `AT` được nghiệp vụ **chấp nhận**; mọi `REQ` được phủ; không link truy vết đứt.

## Rủi ro — Risks
_(vd: bên nghiệp vụ không sẵn sàng đúng lịch → chốt slot sớm.)_

## Checklist review chất lượng — Quality review
- [ ] Tiêu chí vào/ra đo được; có bên nghiệp vụ ký duyệt.
- [ ] Mọi `AT` thuộc một suite; môi trường nghiệm thu xác định.
- [ ] Rủi ro chính có biện pháp.
