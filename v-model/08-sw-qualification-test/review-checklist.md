# Review Checklist — Software Qualification Test

> Tick **HẾT** (base + AUTO) thì work product **ĐẠT chất lượng**. Báo cáo ở [review-report.md](review-report.md).
> Phase gồm 5 artifact: [strategy](test-strategy.md) · [plan](test-plan.md) · [spec](test-spec.md) · [cases](test-cases.md) · [report](test-report.md).

## Base (đặc thù phase)
- [ ] **Strategy:** kiểm đầu-cuối theo `SRS`; phủ chức năng + lỗi/biên + bảo mật + i18n; mức tự động hoá.
- [ ] **Plan:** tiêu chí vào/ra đo được; môi trường & dữ liệu test đầu-cuối xác định; mọi `QT` thuộc suite.
- [ ] **Spec:** mỗi `SRS` có điều kiện kiểm thử (đúng/sai/biên), map tới `QT`.
- [ ] **Cases:** mỗi `QT` **truy về `SRS`**; positive/negative/biên; kết quả mong đợi cụ thể; lặp lại được.
- [ ] **Report:** mọi `QT` có kết quả; ca fail có khiếm khuyết; kết luận Đạt/Chưa đạt theo tiêu chí ra.
- [ ] **Mọi `SRS` đều có `QT`** phủ (không sót).

<!-- AUTO-CHECKLIST:START — sinh bởi gen-review-checklist.sh (mục cụ thể từ ground-truth + auto-tick). Đừng sửa tay. -->
- [x] Mọi SRS có SW-Qualification Test (check-traceability)
- [x] Có SW-Qualification Test phủ `SRS-001`
- [x] Có SW-Qualification Test phủ `SRS-002`
<!-- AUTO-CHECKLIST:END -->
