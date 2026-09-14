# Unit Test — Report (Báo cáo kết quả)

> Kết quả chạy thực tế các `UT`. Cập nhật sau mỗi đợt chạy. _Actual unit-test results._

## Tóm tắt — Summary
- **Đợt / Run:** _(vd: release 1.0.0 — YYYY-MM-DD)_
- **Tổng UT:** _N_ · **Pass:** _N_ · **Fail:** _N_ · **Coverage:** _(vd: 90% lines)_
- **Kết luận:** _(Đạt / Chưa đạt + lý do)_

## Kết quả từng ca — Per-case results
| UT | Traces ↑ (DD) | Kết quả / Result | Khiếm khuyết / Defect |
|----|---------------|------------------|------------------------|
| UT-001 | DD-001 | _Pass / Fail_ | _(link bug nếu fail)_ |
| UT-00x | DD-00x | | |

## Checklist review chất lượng — Quality review
- [ ] **Mọi `UT`** trong [test-cases.md](test-cases.md) có kết quả.
- [ ] Ca fail có khiếm khuyết ghi nhận; số liệu khớp.
- [ ] Kết luận **Đạt/Chưa đạt** theo tiêu chí ra ở [test-plan.md](test-plan.md).
