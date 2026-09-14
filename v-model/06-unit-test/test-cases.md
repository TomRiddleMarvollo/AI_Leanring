# Unit Test — Cases (Ca kiểm thử)

> Ca unit cụ thể. ID: `UT-###`. Mỗi `UT` **Traces** lên `DD` (Detailed Design) mà nó kiểm chứng.
> Phạm vi: [test-spec.md](test-spec.md); lịch & môi trường: [test-plan.md](test-plan.md).

## Ca kiểm thử — Test cases

| ID | Tiêu đề / Title | Traces ↑ (DD) | Bước / Steps | Kết quả mong đợi / Expected |
|----|------------------|---------------|--------------|------------------------------|
| UT-001 | `validate` mật khẩu ≥ 8 ký tự _(ví dụ mẫu từ toolkit — manual, chưa áp dụng cho tính năng thật của dự án này)_ | DD-001 | 1) Mật khẩu 7 ký tự. 2) 8 ký tự. 3) rỗng. | 1) Lỗi độ dài. 2) Hợp lệ. 3) Lỗi bắt buộc. |
| UT-00x | _(ca tiếp theo...)_ | DD-00x | | |

> Mỗi `DD` phải xuất hiện ở ≥1 `UT` tại đây (nếu không → CI báo thiếu test).

## Checklist review chất lượng — Quality review
- [ ] Mỗi `UT` **truy về `DD`**; có positive/negative/biên.
- [ ] **Kết quả mong đợi cụ thể**; đơn vị được cô lập (mock).
- [ ] Mọi `DD` đều có `UT` phủ.
