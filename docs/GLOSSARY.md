# Glossary — Từ điển thuật ngữ (Việt / English)

> Giúp đặt tên **nhất quán** trong code và UI cho ứng dụng song ngữ. Khi một khái niệm
> nghiệp vụ xuất hiện, dùng đúng **tên code** ở cột "Code term" — đừng dùng từ đồng nghĩa
> lẫn lộn (vd vừa `order` vừa `bill` cho cùng một thứ).
> _Keeps naming consistent across code and bilingual UI. Use the canonical Code term._

## Quy ước — How to use
- **Code term** là tên dùng trong code (biến, hàm, bảng, API). Luôn dùng tiếng Anh, nhất quán.
- **Tiếng Việt / English** là nhãn hiển thị cho người dùng (vào `locales/`).
- Thêm dòng mới mỗi khi có khái niệm nghiệp vụ mới.

## Bảng thuật ngữ — Terms

| Code term | Tiếng Việt | English | Ghi chú / Notes |
|-----------|-----------|---------|------------------|
| `user` | người dùng | user | Tài khoản đăng nhập. |
| `order` | đơn hàng | order | KHÔNG dùng `bill`/`invoice` cho khái niệm này. |
| `invoice` | hóa đơn | invoice | Chứng từ thanh toán, khác `order`. |
| `product` | sản phẩm | product | |
| `cart` | giỏ hàng | cart | |
| `customer` | khách hàng | customer | Phân biệt với `user` nội bộ nếu cần. |
| `role` | vai trò | role | Phân quyền. |
| _..._ | _..._ | _..._ | |

> Xóa các dòng ví dụ không liên quan và thêm thuật ngữ thật của dự án.
