# Runbook — Sổ tay vận hành

> Xử lý sự cố & tác vụ vận hành lặp lại khi chạy production. _Ops procedures & incident response._

## Giám sát & cảnh báo — Monitoring & alerts
- **Chỉ số theo dõi:** _(latency p95, error rate 5xx, CPU/mem, hàng đợi...)_
- **Log:** thư mục `log/` (structured JSON, có `traceId`); nơi xem: _..._

## Sự cố thường gặp — Runbooks (mỗi sự cố một mục)
### OPS-001: Dịch vụ trả 5xx tăng đột biến
- **Triệu chứng:** _..._ · **Chẩn đoán:** _(xem log/metric nào)_ · **Xử lý:** _(bước khôi phục)_ · **Rollback:** _..._

### OPS-00x: _(sự cố tiếp theo...)_

## Tác vụ định kỳ — Routine tasks
_(backup, xoay khoá/secret, dọn log, chạy migration...)_

## Liên hệ / Escalation
_(ai phụ trách, kênh báo, mức ưu tiên.)_

## Checklist review chất lượng — Quality review
- [ ] Có **chỉ số & nơi xem log**; alert nối tới hành động.
- [ ] Mỗi sự cố hay gặp có **triệu chứng → chẩn đoán → xử lý → rollback**.
- [ ] Tác vụ định kỳ (backup/secret/log) & escalation rõ ràng.
