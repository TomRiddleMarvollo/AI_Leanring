# Acceptance Test — Cases (Ca nghiệm thu)

> Ca nghiệm thu cụ thể theo người dùng. ID: `AT-###`. Mỗi `AT` **Traces** lên `REQ` mà nó nghiệm thu.
> Phạm vi: [test-spec.md](test-spec.md); lịch & bên tham gia: [test-plan.md](test-plan.md).

## Ca nghiệm thu — Acceptance cases

| ID | Tiêu đề / Title | Traces ↑ (REQ) | Bước (người dùng) / Steps | Kết quả chấp nhận / Accept |
|----|------------------|----------------|----------------------------|-----------------------------|
| AT-001 | Đăng nhập được đầu-cuối | REQ-001 | 1) Mở /login, nhập email+mật khẩu đúng. 2) Nhập OTP nhận qua email. 3) Nhập sai 6 lần. | 1–2) Vào được Dashboard. 3) Bị khoá tạm, có thông báo. |
| AT-00x | _(ca tiếp theo...)_ | REQ-00x | | |

> Mỗi `REQ` phải xuất hiện ở ≥1 `AT` tại đây (nếu không → CI báo thiếu nghiệm thu).

## Checklist review chất lượng — Quality review
- [ ] Mỗi `AT` **truy về `REQ`**; viết theo góc nhìn người dùng, lặp lại được.
- [ ] Có kịch bản **thành công lẫn từ chối**; kết quả chấp nhận cụ thể.
- [ ] Mọi `REQ` đều có `AT` phủ.
