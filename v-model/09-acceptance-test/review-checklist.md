# Review Checklist — Acceptance Test

> Tick **HẾT** (base + AUTO) thì work product **ĐẠT chất lượng**. Báo cáo ở [review-report.md](review-report.md).
> Phase gồm 5 artifact: [strategy](test-strategy.md) · [plan](test-plan.md) · [spec](test-spec.md) · [cases](test-cases.md) · [report](test-report.md).

## Base (đặc thù phase)
- [ ] **Strategy:** nghiệm thu theo góc nhìn người dùng/nghiệp vụ (validation), bám `REQ`.
- [ ] **Plan:** có bên nghiệp vụ ký duyệt; môi trường nghiệm thu; tiêu chí vào/ra đo được.
- [ ] **Spec:** mỗi `REQ` có kịch bản người dùng (thành công + từ chối) map tới `AT`.
- [ ] **Cases:** mỗi `AT` **truy về `REQ`**; viết theo người dùng, lặp lại được.
- [ ] **Report:** mọi `AT` có kết quả + chữ ký; ca từ chối có defect.
- [ ] **Mọi `REQ` đều có `AT`** phủ (không sót).

<!-- AUTO-CHECKLIST:START — sinh bởi gen-review-checklist.sh (mục cụ thể từ ground-truth + auto-tick). Đừng sửa tay. -->
- [x] Mọi REQ có Acceptance Test (check-traceability)
- [x] Có Acceptance Test phủ `REQ-001`
<!-- AUTO-CHECKLIST:END -->
