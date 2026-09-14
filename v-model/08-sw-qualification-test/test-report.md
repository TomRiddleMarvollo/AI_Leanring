# Software Qualification Test — Report (Báo cáo kết quả)

> Kết quả **chạy thực tế** các `QT`: pass/fail, khiếm khuyết, độ phủ. Cập nhật sau mỗi đợt
> chạy (release/sprint). _Actual qualification-test results per QT._

## Tóm tắt — Summary
- **Đợt / Run:** _(vd: release 1.0.0 — YYYY-MM-DD)_
- **Tổng QT:** _N_ · **Pass:** _N_ · **Fail:** _N_ · **Blocked/Skipped:** _N_
- **Coverage:** _(vd: 85% yêu cầu)_ · **Kết luận:** _(Đạt / Chưa đạt + lý do)_

## Kết quả từng ca — Per-case results
| QT | Traces ↑ (SRS) | Kết quả / Result | Khiếm khuyết / Defect | Ghi chú |
|----|----------------|------------------|------------------------|---------|
| QT-001 | SRS-001, SRS-002 | _Pass / Fail_ | _(link bug nếu fail)_ | |
| QT-00x | SRS-00x | | | |

## Khiếm khuyết mở — Open defects
_(Liệt kê bug chưa đóng + mức độ + trạng thái. / Open bugs, severity, status.)_

## Checklist review chất lượng — Quality review
- [ ] **Mọi `QT`** trong [test-cases.md](test-cases.md) đều có kết quả (không bỏ sót).
- [ ] Ca **fail** đều có khiếm khuyết ghi nhận (link bug) — không "fail im lặng".
- [ ] **Số liệu tổng** (pass/fail/coverage) khớp bảng chi tiết.
- [ ] Kết luận **Đạt/Chưa đạt** dựa trên tiêu chí ra ở [test-plan.md](test-plan.md).
