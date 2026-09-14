# Unit Test — Strategy (Chiến lược)

> **Phần Unit Test** của V-model: kiểm chứng **Detailed Design / SDD** (`DD-###`). Đơn vị nhỏ
> nhất (hàm/lớp/module) đúng thiết kế chi tiết. ID ca: `UT-###` **Traces** lên `DD`.

## Cách tiếp cận — Approach
- **Cô lập** đơn vị: mock/stub phụ thuộc ngoài (DB, network, service khác).
- Phủ **happy path + lỗi & biên** của từng `DD` (giá trị biên, nhánh điều kiện).
- **Tự động hoá 100%**, chạy nhanh trong CI mỗi commit.

## Phạm vi — Scope
- **Trong:** logic hàm/lớp suy ra từ `DD`. **Ngoài:** tương tác đa thành phần (→ Integration).

## Tiêu chí chất lượng — Quality gates
- Mỗi `DD-###` có ≥1 `UT-###`; coverage dòng/nhánh đạt ngưỡng dự án.

## Checklist review chất lượng — Quality review
- [ ] Mỗi `DD` có cách kiểm ở mức unit; có **happy + lỗi/biên**.
- [ ] Đơn vị được **cô lập** (mock phụ thuộc), chạy nhanh & tất định.
- [ ] **Coverage** đạt ngưỡng; không phụ thuộc thứ tự chạy.
