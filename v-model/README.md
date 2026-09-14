# SDLC Documentation Set — Bộ tài liệu vòng đời phần mềm (V-model)

> Quy trình **chặt chẽ**: các tài liệu dưới đây **luôn phải up-to-date và nhất quán với
> nhau**, liên kết bằng **ID truy vết**. Một trình kiểm tra tự động (CI) sẽ **chặn**
> khi truy vết bị đứt/thiếu, và **cảnh báo** khi nghi tài liệu cũ hơn code.

---

## Cấu trúc thư mục V-model — mỗi phase một folder

```
v-model/
  01-requirement/           00-HLR.md   REQ-###   + review-checklist.md + review-report.md
  02-specification/         01-SRS.md (SRS-###) + 01b-NFR.md (NFR-###)  + review-checklist/report
  03-architecture/          02-SAD.md   ARC-###  (+ Threat model STRIDE)  + review-checklist/report
  04-detailed-design/       03-DDD.md   DD-###    + review-checklist/report   (SDD: YAML→Mermaid — Đợt 3)
  05-code/                  (source ở frontend/ backend/...)  + review-checklist/report
  06-unit-test/             UT-### ↔ DD    } mỗi test phase: strategy · plan · spec · cases · report
  07-integration-test/      IT-### ↔ ARC   }            + review-checklist/report
  08-sw-qualification-test/ QT-### ↔ SRS   }
  09-acceptance-test/       AT-### ↔ REQ   }  (đóng đỉnh chữ V — nghiệm thu người dùng)
  10-user-manual/           06-USER-MANUAL.md  SCR-###  + review-checklist/report
  11-operations/            deploy-guide · runbook · release-notes  + review-checklist/report
  _traceability/            TRACEABILITY · GROUND-TRUTH · CODE-TRACE (sinh tự động)
```

> **Luồng (V-model):** trái phân rã `REQ → SRS(+NFR) → SAD → SDD → Code`; phải kiểm chứng
> `Unit ↔ DD` · `Integration ↔ ARC` · `SW-Qualification ↔ SRS` · `Acceptance ↔ REQ`; giao nộp `User Manual` + `Operations`.
> **4 phase test riêng**, mỗi phase đủ 5 work product (strategy/plan/spec/cases/report) + review.
> **NFR** (phi chức năng, có số đo) mỗi cái **trích REQ gốc** và có **≥1 test** phủ; **SAD** có **Threat model (STRIDE)**.

## Định dạng & export (theo yêu cầu)
| Phase | Viết bằng | Export khi cần | Trạng thái |
|-------|-----------|----------------|------------|
| REQ / SRS / **NFR** / Test Spec / Test Cases (mỗi phase test) | **Markdown** (bảng) | → **Excel** | ✅ Đợt 2 |
| Test Strategy / Plan / Report (mỗi phase test) / User Manual / **Operations** | **Markdown** | → **Word** | ✅ Đợt 2 |
| Mọi review checklist / report | **Markdown** | → **Excel** | ✅ Đợt 2 |
| SAD / SDD (sơ đồ) | **YAML** (có `type:` schema) | → **Mermaid** (render-mermaid.sh) | ✅ Đợt 3 |

> **Hiệu năng:** tài liệu sống ở **text nhẹ** (md/yaml) — viết/sửa nhanh. Convert sang
> Excel/Word/Mermaid là **on-demand** (khi giao nộp), KHÔNG chạy mỗi commit → code vẫn nhanh.

### Xuất Excel/Word khi giao nộp — `scripts/export-docs.sh` (Đợt 2)
```bash
bash scripts/export-docs.sh                # xuất tất cả vào v-model/_export/ (đã .gitignore)
bash scripts/export-docs.sh --excel-only   # chỉ Excel · --word-only chỉ Word · --out DIR đổi nơi xuất
```
Sinh ra:
- `v-model-spec.xlsx` — sheet cho REQ · SRS · và spec/cases của **mỗi phase test** (UT/IT/QT), trích bảng Markdown.
- `v-model-reviews.xlsx` — mỗi phase một sheet checklist (`Section · Item · Checked`).
- Word: `{Unit,Integration,SWQual}-Test-{Strategy,Plan,Report}.docx` + `User-Manual.docx` — render heading/đoạn/bảng/danh sách.

> Phụ thuộc **MIT**: `openpyxl` (Excel) + `python-docx` (Word) — cài **on-demand** khi chạy,
> KHÔNG nằm trong `requirements.txt` lõi (giữ cài đặt nhẹ). Thư mục `v-model/_export/`
> được `.gitignore` (bản giao nộp, không commit).

### Sơ đồ SAD/SDD: YAML → Mermaid — `scripts/render-mermaid.sh` (Đợt 3)
Viết kiến trúc/sequence bằng **YAML** (`type: c4container | block | sequence`) — nguồn chân lý;
Mermaid do script sinh ra giữa mốc `MERMAID:START/END` (đừng sửa tay → hết lỗi vẽ tay).
```bash
bash scripts/render-mermaid.sh            # vẽ lại Mermaid vào SAD + DDD
bash scripts/render-mermaid.sh --check    # validate YAML schema (CI), lỗi → fail
```
> `check-completeness` (per-commit) chấp nhận **nguồn YAML** *hoặc* Mermaid tay (tương thích ngược).
> Render + validate đầy đủ là **on-demand** (cài `PyYAML` MIT khi chạy) — không chạy mỗi commit.

## Review checklist + report (mỗi phase) — BẮT BUỘC
- Mỗi phase có `review-checklist.md` + `review-report.md`. Checklist **tick HẾT** thì work
  product mới **ĐẠT chất lượng**; việc thực hiện ghi ở report.
- `check-review-checklists.sh` chặn nếu phase thiếu file review; `--quality` kiểm checklist đã tick hết (gate giao nộp).
- **Checklist "đủ tốt" (4 lớp):** (1) **base đặc thù phase** (phần trên mốc AUTO); (2) mục **sinh từ ground-truth
  — một dòng cho MỖI món thật:** mỗi error/endpoint/màn hình, và với 3 phase test là **mỗi `DD`→UT, mỗi `ARC`→IT,
  mỗi `SRS`→SQT** (không gộp chung chung); + (3) **auto-tick** mục máy kiểm được — do `gen-review-checklist.sh`
  sinh vào khối `AUTO-CHECKLIST`; (4) `review-docs-llm.sh` (Qwen3 local) soi mục tick hời hợt/còn thiếu.

## Grounding & cặp verify Code↔SAST
- **Grounding (bottom-up):** mỗi item downstream (SRS/ARC/DD/test) phải **trích ID upstream** — chống AI bịa item không gốc. Không có gốc → gắn `inferred` (cần người duyệt). `check-grounding.sh`.
- **Cặp verify của phase Code = static analysis** (không phải doc): SAST bằng bandit/eslint-security/ruff (MIT/Apache); **suppress phải có lý do** (`check-suppressions.sh`). Không dùng SonarQube (LGPL) / semgrep (LGPL).
- **Cổng nội dung LLM (delta):** `review-docs-llm.sh --diff` chỉ soi phần v-model **vừa đổi trong git** — phản biện NỘI DUNG (logic/mâu thuẫn/thiếu ca), không chỉ cấu trúc. Opt-in pre-commit: `.harness-config` `DOC_REVIEW_ON_COMMIT=1` (cảnh báo) / `LLM_DELTA_GATE=1` (chặn). Ollama vắng → bỏ qua (Tầng 2 không bắt buộc).
- **SRS viết theo EARS · SDD nêu đủ hợp đồng:** mỗi `SRS` là câu *hệ thống **phải/shall** \<đáp ứng\>* (kiểm chứng được; `check-completeness` cảnh báo nếu thiếu modal — opt-out `REQUIRE_EARS_SRS=0`); mỗi hàm/endpoint trong `DD` nêu đủ **input/output/CA LỖI** (opt-out `REQUIRE_DD_CONTRACT=0`).
- **User Manual phủ đủ 3 trục (không sót):** mọi **màn hình** (route) · mọi **button/action** (nhãn i18n) · mọi **use-case** (SRS). `gen-ground-truth.sh` liệt kê tập đầy đủ (buttons chấm ✓/✗ theo nhãn có trong UM); `check-completeness.sh` **cảnh báo** nút chưa hướng dẫn (opt-out `REQUIRE_UM_BUTTONS=0`); `review-docs-llm.sh` có prompt UM riêng.

## Mapping ASPICE 4.0 — trace 2 chiều (bidirectional traceability)

> "2 chiều" = **phủ xuống** (coverage — mỗi item upstream được hiện thực/kiểm chứng, `check-traceability`)
> **+ truy lên** (citation — mỗi item downstream trích nguồn gốc, `check-grounding`). Hai check độc lập
> ép cả hai hướng; kèm nửa còn lại của BP ASPICE 4.0 là **consistency** (nội dung khớp, không chỉ có link)
> do `check-completeness` + EARS/contract + `review-docs-llm --diff` đảm nhiệm.

| ASPICE 4.0 | Cặp trace toolkit | Ép bởi |
|---|---|---|
| SWE.1 — SW req ↔ system req | `SRS ↔ REQ` | check-traceability + check-grounding |
| (SWE.1) — NFR cũng là requirement | `NFR ↔ REQ` (cột Traces ↑) + `NFR → ≥1 test` | check-grounding + check-traceability |
| SWE.2 — architecture thoả cả NFR | `NFR` phải xuất hiện trong SAD (thành phần/quyết định/threat model) | check-traceability |
| SWE.2 — architecture ↔ SW req | `ARC ↔ SRS` | như trên |
| SWE.3 — detailed design ↔ architecture | `DD ↔ ARC` | như trên |
| SWE.3 — units (code) ↔ detailed design | code `@trace DD-###` | check-fn-doc · gen-code-trace |
| SWE.4 — unit verification ↔ **units** | `UT ↔ DD` ⋈ `code @trace DD` → ma trận **UT ↔ Unit** trong TRACEABILITY.md | gen-traceability (dẫn xuất) |
| SWE.4 — verification measures là test THẬT | mỗi `UT-###` claim xong phải có test code mang ID (escape `manual`) | check-test-trace |
| SWE.4 — static verification trên units | Code ↔ SAST, suppress phải có lý do | check-sast · check-suppressions |
| SWE.5 — integration verification ↔ architecture | `IT ↔ ARC` | check-traceability + check-grounding |
| SWE.6 — verification ↔ SW req | `QT ↔ SRS` | như trên |
| SYS.5 / VAL.1 — validation ↔ stakeholder req | `AT ↔ REQ` | như trên |

> **Quyết định phạm vi:** toolkit gộp stakeholder + system requirements vào một tầng `REQ` (HLR) —
> tương đương SYS.1/SYS.2 thu về một mức, phù hợp dự án software-only; nếu cần đủ tầng SYS cho
> assessment automotive, tách HLR thành stakeholder (SYS.1) và system (SYS.2) riêng.
> ASPICE 4.0 **không** còn yêu cầu trace tới test *results* (khác 3.1) — report per-phase là đủ.

## Quy tắc cập nhật (BẮT BUỘC)
- **Cập nhật liên tục, đúng-đủ-không thừa-không thiếu.** Tài liệu phải khớp code hiện tại.
- **KHÔNG override (ghi đè/viết lại) tài liệu phase** — chỉ **chỉnh tại chỗ** cho đúng & đủ.
- **Mọi thay đổi FE/BE phải phản ánh ĐỦ vào REQ/SRS** (không thiếu), độ chi tiết tăng dần:
  - `REQ`: nêu **tính năng** (vd: login).
  - `SRS`: nêu **các use case cụ thể** (nhập đúng/sai, quên mật khẩu, gửi/nhận OTP...) **và đặc tả
    chi tiết** — trường nào, nút nào, giao diện ra sao, hành vi từng trạng thái (gộp vai trò SWS cũ).

---

## Bộ tài liệu & ID — Documents & IDs

| # | Tài liệu | File | ID | Truy vết lên (Traces ↑) |
|---|----------|------|----|--------------------------|
| 1 | High-Level Requirements | [00-HLR.md](01-requirement/00-HLR.md) | `REQ-###` | — (gốc) |
| 2 | Software Requirements Specification (chi tiết) | [01-SRS.md](02-specification/01-SRS.md) | `SRS-###` | `REQ` |
| 2b | Non-Functional Requirements | [01b-NFR.md](02-specification/01b-NFR.md) | `NFR-###` | `REQ` (+ ≥1 test) |
| 3 | Software Architecture Design (+ Threat model) | [02-SAD.md](03-architecture/02-SAD.md) | `ARC-###` | `SRS` |
| 4 | Detailed Design (SDD) | [03-DDD.md](04-detailed-design/03-DDD.md) | `DD-###` | `ARC` |
| 5 | **Coding** (source) | `frontend/ backend/ ...` | `@trace DD-###` | `DD` |
| 6 | **Unit Test** (5 artifact) | [06-unit-test/](06-unit-test/) | `UT-###` | `DD` |
| 7 | **Integration Test** (5 artifact) | [07-integration-test/](07-integration-test/) | `IT-###` | `ARC` |
| 8 | **SW Qualification Test** (5 artifact) | [08-sw-qualification-test/](08-sw-qualification-test/) | `QT-###` | `SRS` |
| 9 | **Acceptance Test** (5 artifact) | [09-acceptance-test/](09-acceptance-test/) | `AT-###` | `REQ` |
| 10 | User Manual | [06-USER-MANUAL.md](10-user-manual/06-USER-MANUAL.md) | `SCR-###` | `REQ` |
| 11 | Operations (deploy/runbook/release) | [11-operations/](11-operations/) | — | giao nộp |
| — | Traceability Matrix (auto) | [TRACEABILITY.md](_traceability/TRACEABILITY.md) | — | tổng hợp |

## Sơ đồ V-model — luồng truy vết

```
HLR (REQ) ──────────────────────► Acceptance Test (AT) ─► User Manual + Operations
   │                                     ▲
   └─ SRS (+NFR) ─────► SW-Qualification Test (QT)
        │                     ▲
        └─ SAD (ARC) ──► Integration Test (IT)
             │                ▲
             └─ SDD (DD) ─► Code ─► Unit Test (UT)
```
Bên trái đi xuống (phân rã), bên phải đi lên (kiểm chứng). **4 phase test riêng**, mỗi phase một
folder + đủ 5 work product: **Unit** `UT↔DD` · **Integration** `IT↔ARC` · **SW-Qualification** `QT↔SRS`
· **Acceptance** `AT↔REQ`. **NFR** mỗi cái có ≥1 test; **giao nộp** gồm User Manual + Operations.

---

## Luật vàng — Golden rules (BẮT BUỘC)

1. **Mỗi `REQ` phải có ≥1 `SRS`** đặc tả nó **và ≥1 `AT`** (Acceptance Test) nghiệm thu.
2. **Mỗi `SRS` phải có ≥1 `ARC`** (thiết kế) **và ≥1 `QT`** (SW-Qualification Test) phủ.
3. **Mỗi `ARC` phải có ≥1 `DD`** chi tiết hóa **và ≥1 `IT`** (Integration Test) phủ.
4. **Mỗi `DD` phải có ≥1 `UT`** (Unit Test) phủ; **nên** được code đánh dấu `@trace DD-###` (cảnh báo nếu thiếu).
5. **Mỗi `NFR` phải được ≥1 test** (UT/IT/QT/AT) kiểm chứng.
6. **Không link đứt:** mọi ID được tham chiếu phải tồn tại ở tài liệu gốc của nó.
7. **Sửa ở đâu, đồng bộ ở đó:** đổi một REQ → rà SRS/NFR/ARC/DD/UT/IT/QT/AT/User Manual/Operations liên quan.

> Lớp 1–3, 5–6 và phần `DD→UT` của lớp 4 bị **CI chặn** nếu vi phạm. `DD→code` và staleness chỉ **cảnh báo**.

> **Truy vết (auto) vs chất lượng (người):** CI chỉ đảm bảo liên kết không đứt/không
> thiếu mức. *Nội dung có đúng không* do người/agent đánh giá bằng **"Checklist review
> chất lượng"** ở cuối mỗi template — tick trước khi coi tài liệu là xong.

---

## Quy trình thêm/sửa một yêu cầu — Workflow (cho người & AI agent)

> **Nhanh nhất — scaffolder:** `bash scripts/new-feature.sh "Tên tính năng" [--nfr] [--screen]`
> tự sinh **stub liên kết đủ chuỗi** với ID khớp sẵn (REQ→SRS→ARC→DD→UT/IT/QT/AT). Sau đó chỉ việc
> **điền nội dung** vào các `_(TODO)_` — `check-traceability` đã XANH, `check-completeness` chỉ đúng chỗ cần điền.

Nếu làm tay, **đi đủ chuỗi** (đừng bỏ mức nào):

1. Thêm `REQ-00X` vào [00-HLR.md](01-requirement/00-HLR.md).
2. Thêm `SRS-00Y` (Traces: `REQ-00X`) — đặc tả chi tiết — vào [01-SRS.md](02-specification/01-SRS.md);
   thêm `NFR-00N` (phi chức năng có số đo) vào [01b-NFR.md](02-specification/01b-NFR.md) nếu có yêu cầu chất lượng.
3. Thêm `ARC-00Z` (Traces: `SRS-00Y`) vào [02-SAD.md](03-architecture/02-SAD.md); cập nhật **Threat model** cho luồng nhạy cảm.
4. Thêm `DD-00W` (Traces: `ARC-00Z`) vào [03-DDD.md](04-detailed-design/03-DDD.md).
5. Code, đánh dấu `@trace DD-00W` ở file/hàm/lớp liên quan (tool trích bằng `gen-code-trace.sh`).
6. Thêm **test phủ cả 4 mức** (cập nhật spec/cases/report trong từng folder test):
   - `UT-00U` (Traces: `DD-00W`) vào [06-unit-test/](06-unit-test/test-cases.md);
     `IT-00I` (Traces: `ARC-00Z`) vào [07-integration-test/](07-integration-test/test-cases.md);
   - `QT-00Q` (Traces: `SRS-00Y`) vào [08-sw-qualification-test/](08-sw-qualification-test/test-cases.md);
     `AT-00A` (Traces: `REQ-00X`) vào [09-acceptance-test/](09-acceptance-test/test-cases.md);
   - **Mỗi `NFR` phải xuất hiện ở ≥1 test** (thường QT/IT).
7. Cập nhật [User Manual](10-user-manual/06-USER-MANUAL.md) & [Operations](11-operations/) nếu ảnh hưởng người dùng/vận hành.
8. Chạy `bash scripts/check-traceability.sh` — phải **0 lỗi**.

> Có một **ví dụ mẫu hoàn chỉnh** `REQ-001 → SRS-001 → ARC-001 → DD-001`, kiểm chứng bởi
> `UT-001`↔DD · `IT-001`↔ARC · `QT-001`↔SRS · `AT-001`↔REQ, `NFR-001/002` có QT. Dùng làm khuôn.

## Kiểm tra & ép buộc — Enforcement
Hai trục kiểm tra bổ sung cho nhau:
```bash
bash scripts/check-traceability.sh   # TRỤC NGANG: liên kết giữa các tài liệu (REQ→SRS→...)
bash scripts/check-completeness.sh   # TRỤC DỌC: độ đầy đủ TRONG mỗi tài liệu (đủ tiểu mục)
bash scripts/gen-traceability.sh     # cập nhật bảng tổng TRACEABILITY.md
# thêm --strict cho CI (lỗi -> fail build)
```

### Definition of Done — ĐỦ mới tính xong (chống làm nông)
Lỗi vibe coding hay gặp: tài liệu chỉ có happy path, thiếu luồng lỗi/bảo mật, thiếu
function/API, thiếu màn hình. Để chặn:
- **Detailed Design (`DD-###`):** mỗi mục BẮT BUỘC đủ 7 tiểu mục — Functions/APIs,
  Happy path, Error & alternate flows, Sequence diagram, Validation, Security, Data model — và có nội dung thật.
- **User Manual (`SCR-###`):** một mục cho MỌI màn hình, đủ Purpose/Steps/Transitions/Error states.
- **Biểu đồ (BẮT BUỘC):** mọi sơ đồ vẽ bằng **Mermaid**, **mỗi sơ đồ mở đầu bằng YAML
  frontmatter** (`---`). Kiến trúc tổng quát → **C4 model** + **Biểu đồ khối** (trong SAD);
  hoạt động một tính năng → **Sequence diagram** (trong từng `DD-###`).
- `check-completeness.sh` **chặn** (error) khi thứ kiểm được tất định — thiếu tiểu mục, tiểu mục
  rỗng hoàn toàn, thiếu C4/block/sequence/frontmatter, cột target NFR trống, hoặc SAD không có mục
  Threat model nào. Những gì chỉ kiểm được bằng **heuristic** (độ dài nội dung, có số hay không, có
  nhắc STRIDE hay không...) chỉ **cảnh báo** (warn), không chặn CI — heuristic dễ bắt hụt/bắt nhầm
  nên quyết định cuối vẫn cần người xem lại, không nên biến thành cổng cứng.
- **Opt-out theo project:** tạo file `.harness-config` ở gốc dự án (biến `KEY=value`, được các
  script `source`) để tắt các yêu cầu không phù hợp với dự án, ví dụ:
  ```bash
  REQUIRE_THREAT_MODEL=0        # dự án không có luồng nhạy cảm — khỏi bắt Threat model/STRIDE
  REQUIRE_NFR_QUANTITATIVE=0    # khỏi cảnh báo khi NFR không có ngưỡng bằng số
  ```

### Chống tài liệu thiếu — Giải pháp 3 tầng
Linter chỉ kiểm *khung*. Để thật sự đủ & sâu, dùng 3 tầng bổ sung nhau:

| Tầng | Mục tiêu | Công cụ | Tính chất |
|------|----------|---------|-----------|
| **1. Ground-truth** | Không **quên** món nào | `gen-ground-truth.sh` → [GROUND-TRUTH.md](_traceability/GROUND-TRUTH.md) liệt kê mọi error code / endpoint / màn hình từ code | Miễn phí, tất định |
| **2. LLM review** | Không **nông** nội dung | `review-docs-llm.sh` — AI thứ hai (Qwen3 30B qua **Ollama local**) phản biện, chấm điểm, fail nếu dưới ngưỡng | Miễn phí (local), cần Ollama |
| **3. Staleness** | Không **quên cập nhật** | `check-doc-staleness.sh` — code mang `DD-###` đổi mà thiết kế không đổi → chặn | Miễn phí, tất định |

```bash
bash scripts/gen-ground-truth.sh      # Tầng 1: cập nhật inventory
bash scripts/review-docs-llm.sh       # Tầng 2: cần `ollama serve` + `ollama pull qwen3:30b`
bash scripts/check-doc-staleness.sh   # Tầng 3: so với HEAD (CI: truyền base ref)
```

> **Giới hạn cuối:** ngay cả 3 tầng cũng KHÔNG cho "100% đầy đủ tự động". Tầng 1+3 tất định
> (không quên/không lệch), Tầng 2 bắt được "nông" nhưng không tất định 100%. Quyết định quan
> trọng vẫn cần mắt người (qua "Checklist review chất lượng" cuối mỗi template).
