# Acceptance Test — Specification (Đặc tả)

> **Cái gì cần nghiệm thu** cho mỗi `REQ`: kịch bản người dùng, điều kiện chấp nhận.
> Ca step-by-step ở [test-cases.md](test-cases.md) (`AT-###`).

## Kịch bản nghiệm thu theo REQ — Conditions per REQ

| Traces ↑ (REQ) | Kịch bản người dùng cần phủ / User scenarios | AT liên quan |
|----------------|-----------------------------------------------|--------------|
| REQ-001 | Người dùng đăng nhập thành công (email+mật khẩu+OTP); và các lối từ chối (sai/khoá). | AT-001 |
| REQ-00x | _(kịch bản cho yêu cầu tiếp theo...)_ | AT-00x |

> Mỗi `REQ` phải có ≥1 kịch bản ở đây, dẫn tới ≥1 `AT` trong [test-cases.md](test-cases.md).

## Checklist review chất lượng — Quality review
- [ ] Mỗi `REQ` có kịch bản nghiệm thu theo **giá trị người dùng**.
- [ ] Gồm cả kịch bản **thành công lẫn từ chối/huỷ**.
- [ ] Mỗi kịch bản **map tới `AT`**.
