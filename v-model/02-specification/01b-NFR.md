# Non-Functional Requirements (NFR) — Yêu cầu phi chức năng

> Chất lượng phần mềm phải **đo được & kiểm chứng được**, không chỉ chức năng. ID: `NFR-###`.
> Mỗi `NFR` phải có **ngưỡng số cụ thể**, **trích REQ gốc** (trace 2 chiều — ASPICE 4.0: NFR cũng là
> requirement, phải truy lên được), **được kiến trúc (SAD) giải quyết** (SWE.2: architecture phải thoả
> cả functional lẫn non-functional — `check-traceability` chặn nếu `NFR-###` không xuất hiện trong SAD),
> và được **≥1 test phủ** (thường ở Integration/SW-Qualification).
> _Measurable quality attributes; each NFR traces up to a REQ, is addressed in the architecture, and has ≥1 test._

## Danh mục NFR — Catalogue

| ID | Loại / Type | Yêu cầu có số đo / Measurable target | Phương pháp kiểm / Verify | Traces ↑ (REQ) |
|----|-------------|---------------------------------------|----------------------------|----------------|
| NFR-001 | Hiệu năng / Performance | API đăng nhập **p95 < 300ms** ở 100 RPS. | Load test → `QT-002` | REQ-001 |
| NFR-002 | Bảo mật / Security | OTP **rate-limit ≤ 5 lần/10 phút/tài khoản**; khoá tạm khi vượt. | `QT-003` | REQ-001 |
| NFR-00x | _(loại tiếp theo — mỗi NFR phải có ≥1 test phủ)_ | _(ngưỡng đo cụ thể...)_ | _(QT/IT/AT-###)_ | _(REQ-00x)_ |

> **Loại nên cân nhắc** (thêm khi liên quan, **mỗi cái phải có test** kẻo CI chặn): Performance ·
> Security · Availability/Reliability · Scalability · Usability/Accessibility · i18n · Maintainability ·
> Observability. Bỏ loại không liên quan, ĐỪNG bịa. Ví dụ: Availability → smoke/uptime test; i18n → UI test đa kích thước.

## Checklist review chất lượng — Quality review
- [ ] Mỗi `NFR` có **ngưỡng SỐ** (không "nhanh", "an toàn" chung chung).
- [ ] Mỗi `NFR` **kiểm chứng được** và có **≥1 test** phủ (CI chặn nếu thiếu).
- [ ] Mỗi `NFR` **trích REQ gốc** ở cột Traces ↑ (`check-grounding` chặn nếu thiếu; suy luận có chủ đích → gắn `inferred`).
- [ ] Mỗi `NFR` được **kiến trúc (SAD) giải quyết** — ID xuất hiện trong quyết định/thành phần/threat model của SAD, không chỉ nằm ở bảng NFR (`check-traceability` chặn nếu thiếu).
- [ ] Phủ các trục quan trọng của dự án (ít nhất perf + security); không thừa loại vô nghĩa.
- [ ] Ngưỡng **thực tế & khả thi** với kiến trúc (SAD) đã chọn.
