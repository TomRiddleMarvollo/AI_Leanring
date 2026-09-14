# Traceability Matrix — Ma trận truy vết

> Bảng tổng hợp **độ phủ truy vết** giữa các tài liệu. Phần giữa hai mốc AUTO được
> **sinh tự động** bởi `bash scripts/gen-traceability.sh` — đừng sửa tay.
> _Coverage overview; the AUTO block is generated; don't edit it by hand._

<!-- AUTO-TRACE:START -->
_Sinh tự động — 1 commit. Đừng sửa tay._

**Requirements → Specification / Acceptance Test**
| REQ | có SRS | có AT |
|-----|--------|-------|
| REQ-001 | ✓ | ✓ |

**NFR → Test (bất kỳ UT/IT/QT/AT)**
| NFR | có test |
|-----|---------|
| NFR-001 | ✓ |
| NFR-002 | ✓ |

**Specification → Architecture / SW-Qualification Test**
| SRS | có ARC | có QT |
|-----|--------|-------|
| SRS-001 | ✓ | ✓ |
| SRS-002 | ✓ | ✓ |

**Architecture → Detailed Design / Integration Test**
| ARC | có DD | có IT |
|-----|-------|-------|
| ARC-001 | ✓ | ✓ |

**Detailed Design → Code / Unit Test**
| DD | trong code | có UT |
|----|------------|-------|
| DD-001 | ✓ | ✓ |
<!-- AUTO-TRACE:END -->

## Chú thích — Legend
- ✓ = có phủ / covered · ✗ = thiếu (lỗi) / missing (error) · — = không áp dụng.
- Quy tắc phủ: `REQ`→`SRS`→`ARC`→`DD`; `SRS`→`TC`. Xem [README.md](../README.md).
