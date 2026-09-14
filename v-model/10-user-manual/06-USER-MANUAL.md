# User Manual — Hướng dẫn sử dụng

> Tài liệu cho **người dùng cuối**, song ngữ Việt/Anh. Mỗi **màn hình** có ID `SCR-###`.
>
> **Definition of Done (BẮT BUỘC):** phải có **một `### SCR-###` cho MỌI màn hình** trong
> phần mềm (đối chiếu Screen Inventory ↔ route trong code), và mỗi mục có **đủ 4 tiểu mục**:
> `Purpose` · `Steps` · `Transitions` · `Error & empty states`. `check-completeness.sh` **chặn**
> nếu thiếu mục hoặc bỏ trống. _One SCR per screen; each with all 4 subsections, filled._

## Screen Inventory — Danh sách màn hình (PHẢI đầy đủ)
> Liệt kê **tất cả** màn hình. Mỗi dòng phải có một `### SCR-###` chi tiết bên dưới.

| SCR | Màn hình / Screen | Route | Traces (REQ) |
|-----|-------------------|-------|--------------|
| SCR-001 | Đăng nhập / Login | `/login` | REQ-001 |

---

### SCR-001: Đăng nhập / Login
_Route: `/login` · Traces: REQ-001_

#### Purpose — Mục đích
**VI:** Cho phép người dùng đăng nhập bằng email và mật khẩu.
**EN:** Lets the user sign in with email and password.

#### Steps — Các bước (vi/en)
**VI:** 1) Nhập email. 2) Nhập mật khẩu (≥ 8 ký tự). 3) Nhấn **Đăng nhập**.
**EN:** 1) Enter email. 2) Enter password (≥ 8 chars). 3) Click **Log in**.

#### Transitions — Chuyển màn hình (liệt kê MỌI lối vào/ra)
- **Vào từ:** màn hình Trang chủ (nút "Đăng nhập"); tự chuyển tới đây khi truy cập trang cần đăng nhập.
- **Đăng nhập đúng →** chuyển tới **Dashboard** (`/`).
- **Đăng nhập sai →** ở lại `/login`, hiện thông báo lỗi.
- **Nhấn "Quên mật khẩu" →** màn hình Khôi phục mật khẩu (`/forgot-password`).
- **Nhấn "Đăng ký" →** màn hình Đăng ký (`/register`).

#### Error & empty states — Trạng thái lỗi & rỗng
- Sai email/mật khẩu → thông báo "Email hoặc mật khẩu không đúng" (i18n).
- Bỏ trống trường → highlight trường + nhắc nhập.
- Mất mạng / lỗi máy chủ → thông báo thử lại sau.

---

<!-- SKELETON (copy để thêm màn hình — ID 'SCR-NNN' KHÔNG bị kiểm tra) -->
### SCR-NNN: &lt;tên màn hình&gt;
_Route: `/...` · Traces: REQ-00x_

#### Purpose
#### Steps
#### Transitions
#### Error & empty states

## Checklist review chất lượng — Quality review
- [ ] **MỌI màn hình** trong app đều có một `### SCR-###` (không sót transition nào).
- [ ] Song ngữ vi/en đầy đủ cho mỗi mục.
- [ ] **Mọi lối chuyển màn hình** (vào/ra, gồm lỗi & huỷ) được liệt kê.
- [ ] Hướng dẫn khớp hành vi thực tế; mỗi màn hình truy về `REQ`.
