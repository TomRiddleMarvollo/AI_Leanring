# Software Requirements Specification (SRS) — Đặc tả yêu cầu phần mềm

> Đặc tả **chi tiết, kiểm chứng được** cho từng yêu cầu mức cao: trường nào, nút nào, giao
> diện ra sao, hành vi từng trạng thái, luồng lỗi & biên. ID: `SRS-###`. Mỗi dòng **Traces**
> lên một hoặc nhiều `REQ`. _Detailed, testable software requirements (absorbs former SWS)._
>
> **Độ chi tiết:** `REQ` (HLR) nêu *tính năng* (vd login); `SRS` chia nhỏ thành các quy tắc
> cụ thể để **kiến trúc (SAD) & test (TC) bám trực tiếp** — không còn mơ hồ.
> Ví dụ: `REQ`: "cho phép phân quyền" → `SRS-1`: có 3 role (admin/manager/user);
> `SRS-2`: màn admin đổi role; `SRS-3`: khi đăng ký cho chọn role; ...

> **Viết theo EARS** (câu yêu cầu kiểm chứng được) — mỗi đặc tả là mệnh đề *hệ thống **phải/shall** \<đáp ứng\>*,
> ưu tiên có mệnh đề kích hoạt: **Khi** \<sự kiện\> / **Trong khi** \<trạng thái\> / **Nếu** \<điều kiện lỗi\> /
> **Ở nơi** \<tuỳ chọn\>, **hệ thống phải** \<đáp ứng\>. Tránh danh từ trơ ("Form đăng nhập: …") vì không test được.
> `check-completeness.sh` **cảnh báo** dòng SRS thiếu modal `phải/shall/sẽ` (opt-out `.harness-config` `REQUIRE_EARS_SRS=0`).

## Đặc tả — Specifications

| ID | Đặc tả chi tiết / Detailed spec | Traces ↑ (REQ) | Tiêu chí chấp nhận / Acceptance |
|----|----------------------------------|----------------|----------------------------------|
| SRS-001 | **Khi** người dùng gửi email hợp lệ + mật khẩu ≥ 8 ký tự, hệ thống **phải** chuyển sang bước OTP. **Nếu** email hoặc mật khẩu sai, hệ thống **phải** trả `401` + thông báo i18n. | REQ-001 | Nhập đúng → bước OTP; sai → 401 + lỗi i18n. |
| SRS-002 | **2FA bắt buộc — Khi** mật khẩu đúng, hệ thống **phải** gửi **OTP 6 số qua email** (hết hạn 5 phút, một lần, rate-limit) và **phải** chỉ trả JWT **khi** OTP đúng. | REQ-001 | OTP đúng → 200 + JWT; sai/hết hạn → 401; quá số lần → 429. |
| SRS-00x | _(đặc tả tiếp theo...)_ | REQ-00x | |

> Mỗi `SRS` phải có ≥1 `ARC` ([../03-architecture/02-SAD.md](../03-architecture/02-SAD.md)) **và**
> ≥1 `QT` (SW-Qualification Test — [../08-sw-qualification-test/test-cases.md](../08-sw-qualification-test/test-cases.md)).
> Mỗi `REQ` phải được ≥1 `SRS` đặc tả. **Yêu cầu phi chức năng** (perf/security/…): xem [01b-NFR.md](01b-NFR.md).

## Checklist review chất lượng — Quality review
- [ ] Mỗi đặc tả **truy về đúng `REQ`** và thực sự thỏa yêu cầu đó.
- [ ] **Đủ nhỏ & cụ thể** để một `ARC`/`TC` bám trực tiếp (trường/nút/trạng thái rõ ràng).
- [ ] **Viết theo EARS:** mỗi yêu cầu là câu *hệ thống **phải/shall** \<đáp ứng\>*, có mệnh đề kích hoạt (Khi/Nếu/Trong khi/Ở nơi) khi phù hợp — không phải danh từ trơ.
- [ ] **Tiêu chí chấp nhận đo được** (input → output cụ thể), test viết được ngay.
- [ ] Bao phủ **lỗi & biên** (sai dữ liệu, rỗng, giới hạn), không chỉ "happy path"; **phủ hết** nhánh/role/luồng của `REQ` cha.
- [ ] **Không lẫn chi tiết hiện thực** (tên class, thư viện) — để dành cho SAD/SDD.
- [ ] Thông báo cho người dùng đã tính tới **i18n (vi/en)**; nhất quán với HLR, không thêm yêu cầu "lậu".
