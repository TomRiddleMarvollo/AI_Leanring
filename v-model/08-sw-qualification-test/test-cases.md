# Software Qualification Test — Cases (Ca kiểm thử)

> Ca kiểm thử đầu-cuối. ID: `QT-###`. Mỗi `QT` **Traces** lên `SRS` mà nó kiểm chứng.
> Phạm vi: [test-spec.md](test-spec.md); lịch & môi trường: [test-plan.md](test-plan.md).

## Ca kiểm thử — Test cases

| ID | Tiêu đề / Title | Traces ↑ (SRS) | Bước / Steps | Kết quả mong đợi / Expected |
|----|------------------|----------------|--------------|------------------------------|
| QT-001 | Đăng nhập + 2FA đầu-cuối | SRS-001, SRS-002 | 1) Đăng nhập đúng → nhập OTP đúng. 2) OTP sai/hết hạn. 3) Quá số lần. | 1) 200 + JWT. 2) 401. 3) 429. |
| QT-002 | Hiệu năng đăng nhập (NFR-001) | SRS-001 | Load test 100 RPS vào `/api/v1/auth/login`. | p95 < 300ms (đạt NFR-001). |
| QT-003 | Rate-limit OTP (NFR-002) | SRS-002 | Gửi/nhập OTP > 5 lần/10 phút. | Bị khoá tạm; đạt NFR-002. |
| QT-00x | _(ca tiếp theo...)_ | SRS-00x | | |

> Mỗi `SRS` phải xuất hiện ở ≥1 `QT` tại đây (nếu không → CI báo thiếu test).

## Checklist review chất lượng — Quality review
- [ ] Mỗi `QT` **truy về `SRS`** và thực sự kiểm chứng tiêu chí chấp nhận.
- [ ] Có cả ca **đúng (positive) lẫn sai (negative) & biên (edge)**.
- [ ] **Kết quả mong đợi cụ thể** (giá trị/mã trạng thái), không "chạy được là đạt".
- [ ] **Tiền điều kiện & dữ liệu test** đầy đủ, lặp lại được.
- [ ] Mọi tiêu chí chấp nhận trong `SRS` đều có `QT` phủ.
