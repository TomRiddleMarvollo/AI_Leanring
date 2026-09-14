# Review Checklist — Integration Test

> Tick **HẾT** (base + AUTO) thì work product **ĐẠT chất lượng**. Báo cáo ở [review-report.md](review-report.md).
> Phase gồm 5 artifact: [strategy](test-strategy.md) · [plan](test-plan.md) · [spec](test-spec.md) · [cases](test-cases.md) · [report](test-report.md).

## Base (đặc thù phase)
- [ ] **Strategy:** phủ hợp đồng & luồng dữ liệu; có ca lỗi tích hợp; môi trường xác định.
- [ ] **Plan:** môi trường tích hợp dựng lại được; mọi `IT` thuộc suite; tiêu chí vào/ra đo được.
- [ ] **Spec:** mỗi `ARC` có điều kiện tích hợp map tới `IT`.
- [ ] **Cases:** mỗi `IT` **truy về `ARC`**; kết quả mong đợi cụ thể.
- [ ] **Report:** mọi `IT` có kết quả; ca fail có khiếm khuyết.
- [ ] **Mọi `ARC` đều có `IT`** phủ (không sót).

<!-- AUTO-CHECKLIST:START — sinh bởi gen-review-checklist.sh (mục cụ thể từ ground-truth + auto-tick). Đừng sửa tay. -->
- [x] Mọi ARC có Integration Test (check-traceability)
- [x] Có Integration Test phủ `ARC-001`
<!-- AUTO-CHECKLIST:END -->
