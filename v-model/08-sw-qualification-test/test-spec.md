# Software Qualification Test — Specification (Đặc tả)

> **Cái gì cần kiểm** đầu-cuối cho mỗi `SRS`: điều kiện, phân vùng dữ liệu, độ phủ.
> Ca step-by-step ở [test-cases.md](test-cases.md) (`QT-###`).

## Điều kiện kiểm thử theo SRS — Conditions per SRS

| Traces ↑ (SRS) | Điều kiện cần phủ / Conditions to cover | QT liên quan |
|----------------|------------------------------------------|--------------|
| SRS-001 | Đăng nhập: mật khẩu đúng / sai / rỗng; email không hợp lệ; < 8 ký tự. | QT-001 |
| SRS-002 | 2FA: OTP đúng / sai / hết hạn / dùng lại / vượt số lần (rate-limit). | QT-001 |
| SRS-00x | _(điều kiện cho đặc tả tiếp theo...)_ | QT-00x |

> Mỗi `SRS` phải có ≥1 điều kiện ở đây, dẫn tới ≥1 `QT` trong [test-cases.md](test-cases.md).

## Checklist review chất lượng — Quality review
- [ ] Mỗi `SRS` có **điều kiện kiểm thử** đầu-cuối rõ, gồm **đúng / sai / biên**.
- [ ] Phân vùng dữ liệu & giá trị biên được nêu (không chỉ một giá trị mẫu).
- [ ] Mỗi điều kiện **map tới `QT`** cụ thể; không điều kiện nào "mồ côi".
- [ ] Bao phủ khía cạnh **bảo mật & i18n** liên quan tới `SRS`.
