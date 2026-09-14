# Unit Test — Specification (Đặc tả)

> **Cái gì cần kiểm** ở mức unit cho mỗi `DD`: điều kiện, phân vùng dữ liệu, giá trị biên.
> Ca step-by-step ở [test-cases.md](test-cases.md) (`UT-###`).

## Điều kiện kiểm thử theo DD — Conditions per DD

| Traces ↑ (DD) | Điều kiện cần phủ / Conditions | UT liên quan |
|---------------|--------------------------------|--------------|
| DD-001 | `validate` mật khẩu: < 8, = 8, > 8 ký tự; rỗng; ký tự đặc biệt. | UT-001 |
| DD-00x | _(điều kiện cho thiết kế tiếp theo...)_ | UT-00x |

> Mỗi `DD` phải có ≥1 điều kiện ở đây, dẫn tới ≥1 `UT` trong [test-cases.md](test-cases.md).

## Checklist review chất lượng — Quality review
- [ ] Mỗi `DD` có điều kiện unit rõ (đúng/sai/biên).
- [ ] Phân vùng dữ liệu & giá trị biên nêu cụ thể.
- [ ] Mỗi điều kiện **map tới `UT`**.
