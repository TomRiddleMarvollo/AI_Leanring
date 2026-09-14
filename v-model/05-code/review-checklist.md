# Review Checklist — Code

> Tick **HẾT** (cả mục base lẫn mục AUTO) thì work product mới **ĐẠT chất lượng**.
> Báo cáo ở [review-report.md](review-report.md). Mục AUTO sinh từ ground-truth + auto-tick.

## Base (đặc thù phase)
- [ ] Mọi file mã chức năng có **@trace DD-###**; hàm public có header **@trace/@version**.
- [ ] Theo CONVENTIONS (boring code, giới hạn size, naming); **i18n vi/en** đủ.
- [ ] **Bảo mật** (secret/injection/2FA) ổn; **responsive** nếu là web; **Tabler Icons**.
- [ ] Có **test** cho logic quan trọng; lint/format sạch.

<!-- AUTO-CHECKLIST:START — sinh bởi gen-review-checklist.sh (mục cụ thể từ ground-truth + auto-tick). Đừng sửa tay. -->
- [x] Hàm public có header @trace/@version (check-fn-doc)
- [x] Mọi file mã trace tới DD (check-code-doc-coverage)
- [x] i18n vi/en khớp key (check-i18n)
<!-- AUTO-CHECKLIST:END -->
