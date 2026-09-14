# Ground-Truth Inventory — Tập đầy đủ (sinh tự động)

> TẦNG 1 chống làm thiếu: liệt kê MỌI món suy ra từ code/i18n. Tài liệu phải phủ hết.
> Sinh bởi `scripts/gen-ground-truth.sh` — **đừng sửa tay**. ✓ = đã có trong tài liệu, ✗ = còn thiếu.

## Error codes (từ locales) → phải xử lý trong Design (DDD) & Test
| Error code | Design | Test |
|---|---|---|
| _(chưa có)_ | — | — |

## Endpoints (từ code) → phải có trong Design (DDD)
| Endpoint | Design |
|---|---|
| _(chưa có)_ | — |

## Screens (từ router) → phải có trong User Manual
| Route | User Manual |
|---|---|
| _(chưa có)_ | — |

## Buttons / actions (từ i18n) → nhãn phải xuất hiện trong User Manual
> ✗ = nhãn nút (en/vi) chưa thấy trong User Manual → nghi thiếu hướng dẫn cho nút đó.
| Action (i18n key) | Label (en / vi) | User Manual |
|---|---|---|
| _(chưa có)_ | — | — |

## Use-cases (từ SRS) → mỗi use-case phải có luồng trong User Manual
> Máy KHÔNG chấm ✓/✗ (UM viết văn xuôi, không trích SRS-ID) — dùng cho LLM/người soi độ phủ.
| Use-case (SRS) | Đặc tả | Traces ↑ |
|---|---|---|
| SRS-001 | **Khi** người dùng gửi email hợp lệ + mật khẩu ≥ 8 ký… | REQ-001 |
| SRS-002 | **2FA bắt buộc — Khi** mật khẩu đúng, hệ thống **phả… | REQ-001 |
