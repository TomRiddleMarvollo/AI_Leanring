# Acceptance Test — Strategy (Chiến lược)

> **ĐỈNH chữ V** — nghiệm thu ở góc nhìn **người dùng/nghiệp vụ**, kiểm chứng **Requirements**
> (`REQ-###`). "Đúng sản phẩm cần" (validation), khác SQT là "đúng đặc tả" (verification).
> ID ca: `AT-###` **Traces** lên `REQ`.
>
> _Một trong 4 phase test:_ [Unit](../06-unit-test/) · [Integration](../07-integration-test/) · [SW-Qual](../08-sw-qualification-test/) · **Acceptance**.

## Cách tiếp cận — Approach
- Kịch bản **theo người dùng thật** (business scenario), chạy trên môi trường giống production.
- Tiêu chí **PASS/FAIL do bên nghiệp vụ/chủ sản phẩm chốt**, bám `REQ`.
- Ưu tiên luồng giá trị chính; gồm cả kịch bản từ chối/huỷ.

## Phạm vi — Scope
- **Trong:** mỗi `REQ` được nghiệm thu end-to-end theo góc nhìn người dùng.
- **Ngoài:** đặc tả phần mềm (→ SQT), thành phần (→ IT), đơn vị (→ UT).

## Checklist review chất lượng — Quality review
- [ ] Mỗi `REQ` có kịch bản nghiệm thu theo **người dùng** (không chỉ kỹ thuật).
- [ ] Tiêu chí PASS/FAIL rõ, do nghiệp vụ chốt; môi trường giống production.
- [ ] Gồm kịch bản chính + từ chối/huỷ.
