# Integration Test — Report (Báo cáo kết quả)

> Kết quả chạy thực tế các `IT`. Cập nhật sau mỗi đợt chạy. _Actual integration-test results._

## Tóm tắt — Summary
- **Đợt / Run:** _(vd: release 1.0.0 — YYYY-MM-DD)_
- **Tổng IT:** _N_ · **Pass:** _N_ · **Fail:** _N_
- **Kết luận:** _(Đạt / Chưa đạt + lý do)_

## Kết quả từng ca — Per-case results
| IT | Traces ↑ (ARC) | Kết quả / Result | Khiếm khuyết / Defect |
|----|----------------|------------------|------------------------|
| IT-001 | ARC-001 | _Pass / Fail_ | _(link bug nếu fail)_ |
| IT-00x | ARC-00x | | |

## Checklist review chất lượng — Quality review
- [ ] **Mọi `IT`** trong [test-cases.md](test-cases.md) có kết quả.
- [ ] Ca fail có khiếm khuyết ghi nhận; số liệu khớp.
- [ ] Kết luận **Đạt/Chưa đạt** theo tiêu chí ra ở [test-plan.md](test-plan.md).
