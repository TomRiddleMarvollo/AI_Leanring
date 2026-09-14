# Acceptance Test — Report (Báo cáo nghiệm thu)

> Kết quả nghiệm thu thực tế các `AT` + **chữ ký chấp nhận** của nghiệp vụ. _Actual UAT results + sign-off._

## Tóm tắt — Summary
- **Đợt / Run:** _(vd: release 1.0.0 — YYYY-MM-DD)_
- **Tổng AT:** _N_ · **Chấp nhận:** _N_ · **Từ chối:** _N_
- **Kết luận:** _(Nghiệm thu ĐẠT / CHƯA — người ký, ngày)_

## Kết quả từng ca — Per-case results
| AT | Traces ↑ (REQ) | Kết quả / Result | Ghi chú / Note |
|----|----------------|------------------|-----------------|
| AT-001 | REQ-001 | _Chấp nhận / Từ chối_ | _(link defect nếu từ chối)_ |
| AT-00x | REQ-00x | | |

## Checklist review chất lượng — Quality review
- [ ] **Mọi `AT`** trong [test-cases.md](test-cases.md) có kết quả + người/ngày ký.
- [ ] Ca từ chối có defect ghi nhận; số liệu tổng khớp.
- [ ] Kết luận nghiệm thu bám tiêu chí ra ở [test-plan.md](test-plan.md).
