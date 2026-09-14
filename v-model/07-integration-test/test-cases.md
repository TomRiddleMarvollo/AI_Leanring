# Integration Test — Cases (Ca kiểm thử)

> Ca tích hợp cụ thể. ID: `IT-###`. Mỗi `IT` **Traces** lên `ARC` (Architecture) mà nó kiểm chứng.
> Phạm vi: [test-spec.md](test-spec.md); lịch & môi trường: [test-plan.md](test-plan.md).

## Ca kiểm thử — Test cases

| ID | Tiêu đề / Title | Traces ↑ (ARC) | Bước / Steps | Kết quả mong đợi / Expected |
|----|------------------|----------------|--------------|------------------------------|
| IT-001 | Auth Service ↔ Email/DB gửi & lưu OTP | ARC-001 | 1) Mật khẩu đúng → gọi gửi OTP. 2) Lỗi gửi email. | 1) OTP 6 số gửi đi, lưu DB hạn 5 phút. 2) Báo lỗi, không phát JWT. |
| IT-00x | _(ca tiếp theo...)_ | ARC-00x | | |

> Mỗi `ARC` phải xuất hiện ở ≥1 `IT` tại đây (nếu không → CI báo thiếu test).

## Checklist review chất lượng — Quality review
- [ ] Mỗi `IT` **truy về `ARC`**; phủ hợp đồng + lỗi tích hợp.
- [ ] **Kết quả mong đợi cụ thể** (trạng thái, dữ liệu lưu).
- [ ] Mọi `ARC` đều có `IT` phủ.
