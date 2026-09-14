# Review Checklist — Operations

> Tick **HẾT** (base + AUTO) thì work product **ĐẠT chất lượng**. Báo cáo ở [review-report.md](review-report.md).
> Phase gồm 3 artifact: [deploy-guide](deploy-guide.md) · [runbook](runbook.md) · [release-notes](release-notes.md).

## Base (đặc thù phase)
- [ ] **Deploy guide:** bước triển khai lặp lại được; biến môi trường/secret (nguồn) rõ; có health-check + rollback.
- [ ] **Runbook:** có chỉ số giám sát & nơi xem log; mỗi sự cố hay gặp có triệu chứng→xử lý→rollback; escalation rõ.
- [ ] **Release notes:** theo giá trị người dùng; có lưu ý nâng cấp/breaking; khớp tag phát hành.
- [ ] Không lộ secret/PII trong bất kỳ tài liệu nào.

<!-- AUTO-CHECKLIST:START — sinh bởi gen-review-checklist.sh (mục cụ thể từ ground-truth + auto-tick). Đừng sửa tay. -->
- [x] Tài liệu vận hành soi bằng base checklist (deploy/runbook/release)
<!-- AUTO-CHECKLIST:END -->
