# Review Checklist — Unit Test

> Tick **HẾT** (base + AUTO) thì work product **ĐẠT chất lượng**. Báo cáo ở [review-report.md](review-report.md).
> Phase gồm 5 artifact: [strategy](test-strategy.md) · [plan](test-plan.md) · [spec](test-spec.md) · [cases](test-cases.md) · [report](test-report.md).

## Base (đặc thù phase)
- [ ] **Strategy:** cô lập đơn vị (mock), phủ happy + lỗi/biên, coverage ngưỡng.
- [ ] **Plan:** môi trường/công cụ unit; mọi `UT` thuộc suite; tiêu chí vào/ra đo được.
- [ ] **Spec:** mỗi `DD` có điều kiện unit (đúng/sai/biên) map tới `UT`.
- [ ] **Cases:** mỗi `UT` **truy về `DD`**; kết quả mong đợi cụ thể.
- [ ] **Report:** mọi `UT` có kết quả; ca fail có khiếm khuyết.
- [ ] **Mọi `DD` đều có `UT`** phủ (không sót).

<!-- AUTO-CHECKLIST:START — sinh bởi gen-review-checklist.sh (mục cụ thể từ ground-truth + auto-tick). Đừng sửa tay. -->
- [x] Mọi DD có Unit Test (check-traceability)
- [x] Có Unit Test phủ `DD-001`
<!-- AUTO-CHECKLIST:END -->
