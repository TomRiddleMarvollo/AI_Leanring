# Integration Test — Strategy (Chiến lược)

> **Phần Integration Test** của V-model: kiểm chứng **Architecture / SAD** (`ARC-###`). Các
> thành phần ghép với nhau đúng kiến trúc & hợp đồng. ID ca: `IT-###` **Traces** lên `ARC`.

## Cách tiếp cận — Approach
- Ghép **thành phần thật ↔ thành phần thật** (hoặc test double ở biên hệ thống ngoài).
- Phủ **luồng dữ liệu & hợp đồng API** giữa các thành phần trong một `ARC`.
- Kiểm **lỗi tích hợp**: timeout, sai schema, mất kết nối, retry.

## Phạm vi — Scope
- **Trong:** tương tác đa thành phần (service↔DB, service↔service). **Ngoài:** logic đơn vị (→ Unit),
  luồng đầu-cuối theo yêu cầu (→ SW Qualification).

## Tiêu chí chất lượng — Quality gates
- Mỗi `ARC-###` có ≥1 `IT-###`; mọi ranh giới/hợp đồng quan trọng được phủ.

## Checklist review chất lượng — Quality review
- [ ] Mỗi `ARC` có cách kiểm tích hợp; phủ **hợp đồng & luồng dữ liệu**.
- [ ] Có ca **lỗi tích hợp** (timeout/schema/kết nối), không chỉ happy path.
- [ ] Môi trường tích hợp (DB/queue thật hay double) xác định.
