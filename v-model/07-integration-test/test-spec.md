# Integration Test — Specification (Đặc tả)

> **Cái gì cần kiểm** ở mức tích hợp cho mỗi `ARC`: ranh giới, hợp đồng, luồng dữ liệu, lỗi tích hợp.
> Ca step-by-step ở [test-cases.md](test-cases.md) (`IT-###`).

## Điều kiện kiểm thử theo ARC — Conditions per ARC

| Traces ↑ (ARC) | Điều kiện cần phủ / Conditions | IT liên quan |
|----------------|--------------------------------|--------------|
| ARC-001 | Auth Service ↔ Email: gửi OTP thành công; lỗi gửi; ↔ DB: lưu/đọc OTP, hết hạn. | IT-001 |
| ARC-00x | _(điều kiện cho thành phần tiếp theo...)_ | IT-00x |

> Mỗi `ARC` phải có ≥1 điều kiện ở đây, dẫn tới ≥1 `IT` trong [test-cases.md](test-cases.md).

## Checklist review chất lượng — Quality review
- [ ] Mỗi `ARC` có điều kiện tích hợp rõ (hợp đồng + lỗi).
- [ ] Phủ **luồng dữ liệu** giữa thành phần, không chỉ một chiều.
- [ ] Mỗi điều kiện **map tới `IT`**.
