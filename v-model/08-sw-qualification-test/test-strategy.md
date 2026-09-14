# Software Qualification Test — Strategy (Chiến lược)

> **Phần Software Qualification Test** của V-model: kiểm chứng **Software Requirements / SRS**
> (`SRS-###`). Toàn phần mềm chạy đầu-cuối, đúng đặc tả yêu cầu. ID ca: `QT-###` **Traces** lên `SRS`.
>
> _Một trong 4 phase test:_ [Unit](../06-unit-test/) (↔DD) · [Integration](../07-integration-test/) (↔ARC) · **SW-Qual** (↔SRS) · [Acceptance](../09-acceptance-test/) (↔REQ).

## Cách tiếp cận — Approach
- Chạy hệ thống **đầu-cuối** (black-box) theo từng `SRS`; kiểm **tiêu chí chấp nhận**.
- Phủ **chức năng + lỗi & biên + bảo mật + i18n (vi/en)** ở góc nhìn yêu cầu.
- Tự động hoá khi luồng ổn định (e2e); thủ công cho khám phá.

## Phạm vi — Scope
- **Trong:** hành vi phần mềm vs `SRS` (đầu-cuối). **Ngoài:** đơn vị (→ Unit), tích hợp thành phần (→ Integration).
- Nghiệm thu phía người dùng (vs `REQ`) làm ở [Acceptance Test](../09-acceptance-test/) + [User Manual](../10-user-manual/06-USER-MANUAL.md).

## Tiêu chí chất lượng — Quality gates
- Mỗi `SRS-###` có ≥1 `QT-###`; mọi tiêu chí chấp nhận được phủ; truy vết không đứt.

## Checklist review chất lượng — Quality review
- [ ] Mỗi `SRS` có cách kiểm đầu-cuối; phủ **chức năng + lỗi/biên + bảo mật + i18n**.
- [ ] Kiểm theo **tiêu chí chấp nhận** của `SRS`, không "chạy được là đạt".
- [ ] **Mức tự động hoá & công cụ** xác định, khả thi với stack.
