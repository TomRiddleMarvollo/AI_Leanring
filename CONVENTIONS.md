# Code Conventions — Quy ước code

> Nguồn chuẩn DUY NHẤT cho quy ước viết code của dự án. Áp dụng cho **cả người lẫn
> mọi AI agent** (xem [AGENTS.md](AGENTS.md)). Mục tiêu: code **người đọc & bảo trì
> được mà không cần AI agent**.
> _Single source of truth for code conventions. For humans and all AI agents alike._

---

## 1. Boring code — Code "nhàm chán" mới dễ bảo trì

Code do AI sinh ra hay "thông minh quá mức". Quy tắc: **ưu tiên rõ ràng hơn ngắn gọn.**

- **Tường minh hơn khôn khéo.** — Thà dài thêm vài dòng còn hơn một biểu thức cô đọng khó hiểu. Tránh one-liner lồng nhau, ternary lồng, thủ thuật ngôn ngữ ít người biết.
- **Quy tắc số 3 cho abstraction.** — Chỉ tách hàm/lớp/generic dùng chung khi có **≥ 3 chỗ** thực sự lặp lại. Đừng trừu tượng hóa "phòng xa".
- **Giới hạn kích thước** (ÉP bởi `check-code-size.sh` + eslint/ruff):
  - File: < ~300 dòng.
  - Hàm: < ~50 dòng.
  - Độ lồng (if/for): ≤ 3 cấp — sâu hơn thì tách hàm hoặc return sớm.
  - Tham số hàm: ≤ 4 — nhiều hơn thì gom thành object/struct.
- **Không "ma thuật ngầm".** — Tránh metaprogramming, magic string/number. Đặt hằng số có tên.
- **Một file một trách nhiệm.** — Một file/module làm đúng một việc, đặt tên theo việc đó.

## 2. Naming — Đặt tên

- **Tên tự giải thích.** — Đọc tên là hiểu vai trò, không cần đọc thân hàm. (Cũng giúp AI đỡ phải mở file → tiết kiệm token.)
- Dùng đúng thuật ngữ trong [docs/GLOSSARY.md](docs/GLOSSARY.md) để tên nhất quán toàn dự án.

| Loại | Quy ước | Ví dụ |
|------|---------|-------|
| Biến / hàm (JS/TS) | camelCase | `getUserById` |
| Biến / hàm (Python) | snake_case | `get_user_by_id` |
| Component (React) | PascalCase | `ProductCard` |
| Class / Type / Interface | PascalCase | `User`, `OrderStatus` |
| Hằng số | UPPER_SNAKE_CASE | `MAX_RETRY` |
| Boolean | tiền tố `is/has/can` | `isActive`, `hasAccess` |
| File test | `*.test.*` / `test_*.py` | `userService.test.ts` |

> Chọn MỘT bộ quy ước cho mỗi ngôn ngữ và giữ nhất quán toàn dự án.

## 3. Structure & dependencies — Cấu trúc & phụ thuộc

- Theo cấu trúc thư mục trong [docs/STRUCTURE.md](docs/STRUCTURE.md).
- **Phụ thuộc một chiều**, không gọi ngược (vd backend: `routes → controllers → services → models`).
- **Controller/router mỏng, service dày.** Business logic nằm ở tầng service.
- Đặt code mới đúng tầng trách nhiệm; không nhét logic vào nơi tiện tay.

## 4. Comments — Chú thích

- **Comment giải thích *vì sao*, không phải *cái gì*.** — Code đã nói "cái gì"; comment nói lý do, ràng buộc, đánh đổi.
- Không comment thừa kiểu `// tăng i lên 1`. Không để lại code chết (commented-out code).
### Header hàm chuẩn (BẮT BUỘC) — Standard function header
Mọi hàm public (trừ hàm một-câu-lệnh/getter, hàm private `_`, test) phải có **docstring/JSDoc**
ở đầu hàm gồm: dòng tóm tắt, `@trace <ID>`, `@version <x.y.z>`, và `@param`/`@returns`/`@throws`
khi áp dụng. **Code tới đâu cập nhật header tới đó**; sửa hàm → bump `@version` (SemVer:
PATCH nội bộ · MINOR thêm tương thích · MAJOR đổi signature/hành vi). Ép bởi `check-fn-doc.sh`
(@trace/@version) + **eslint-plugin-jsdoc** cho TS/JS (cấu trúc JSDoc: require-jsdoc/param/returns).

```ts
/**
 * Đăng ký người dùng: kiểm tra trùng email, hash mật khẩu, lưu DB.
 * @trace DD-001
 * @version 1.0.0
 * @param payload Dữ liệu đăng ký.
 * @returns User vừa tạo.
 * @throws email_taken Khi email đã tồn tại.
 */
```
```python
def register_user(db, payload):
    """Đăng ký người dùng: ...

    @trace DD-001
    @version 1.0.0
    Args: ...
    Returns: ...
    Raises: ...
    """
```

## 5. Error handling — Xử lý lỗi

- Xử lý lỗi & edge case **có chủ đích**; không `catch` rồi nuốt im lặng.
- Thông báo lỗi trả người dùng phải qua i18n (mục 7), không hardcode chuỗi.
- Fail rõ ràng: ném lỗi có ngữ cảnh thay vì trả `null` mập mờ.
- Mọi lỗi bị bắt (`catch`) phải được **log ở mức `error`** (xem mục 5a).

## 5a. Logging — Ghi log để troubleshoot

> Mục tiêu: **tìm được nguyên nhân bug trong < 5 phút** nhờ log — không cần đính gdb hay thêm print rồi redeploy.

### Nguyên tắc cốt lõi

- **Dùng logger trừu tượng, không dùng `console.log` / `print` trực tiếp.**
  - TS/JS: `import { logger } from '@/lib/logger'` (wrapper trên `pino` hoặc `winston`).
  - Python: `import logging; logger = logging.getLogger(__name__)`.
  - Lý do: logger trừu tượng cho phép tắt/bật level, đổi format, gửi sang sink mà không sửa từng chỗ.

- **Structured log (JSON), không plain text.**
  Mỗi log entry là một JSON object, tối thiểu có các field:

  | Field | Kiểu | Ý nghĩa |
  |-------|------|---------|
  | `timestamp` | ISO-8601 | Thời điểm log |
  | `level` | string | `debug` / `info` / `warn` / `error` |
  | `message` | string | Mô tả ngắn, đủ hiểu không cần context |
  | `traceId` | string | ID xuyên suốt một request (từ header `X-Trace-Id` hoặc sinh ngẫu nhiên) |
  | `service` | string | Tên service/module ghi log |
  | `err` (tùy chọn) | object | `{ message, stack, code }` — chỉ khi level `error` |
  | `...ctx` | object | Context nghiệp vụ liên quan (userId, orderId…) |

- **`traceId` phải lan truyền qua mọi lớp** — từ HTTP handler → service → repo → external call.
  Dùng `AsyncLocalStorage` (Node) hoặc `contextvars` (Python) để không phải truyền tham số thủ công.

### Log đi đâu? — Sink/destination

> **App ghi log ra thư mục `log/` trong thư mục cài đặt phần mềm**, đồng thời vẫn ghi ra `stdout` khi chạy dev.
> Mục tiêu: người vận hành mở thẳng `log/` để xem, không phụ thuộc hạ tầng bên ngoài.

- **Đường dẫn:** thư mục `log/` nằm ở **gốc thư mục cài đặt** (cùng cấp với binary/`package.json`).
  Cho phép override bằng env var `LOG_DIR` (mặc định `<install-dir>/log`).
  - Phân giải đường dẫn từ vị trí app, **không** dùng cwd: Node `path.join(__dirname, '..', 'log')`; Python `Path(__file__).resolve().parent / "log"`.
  - Tự `mkdir -p` thư mục `log/` khi khởi động nếu chưa có.
  - **Thêm `log/` vào `.gitignore`** — không commit file log.

- **Đặt tên file:** `app-YYYY-MM-DD.log` (một file/ngày). Lỗi tách riêng `error-YYYY-MM-DD.log` để soi nhanh.

- **BẮT BUỘC có rotation** (tránh đầy đĩa):
  - Xoay theo **ngày** *và* theo **kích thước** (vd ~20 MB/file).
  - Giữ tối đa **14 ngày** (cấu hình qua `LOG_RETENTION_DAYS`); nén file cũ (`.gz`).
  - TS/JS: `pino` + [`pino-roll`](https://github.com/mcollina/pino-roll) (hoặc `rotating-file-stream`).
  - Python: `logging.handlers.TimedRotatingFileHandler(when="midnight", backupCount=14)`.

- **Vẫn song song ra `stdout` khi dev** (`NODE_ENV=development`) để xem trực tiếp terminal; production có thể tắt stdout, chỉ ghi file.

- **Cảnh báo vận hành:** nếu app chạy trong **container/K8s** (filesystem ephemeral), thư mục `log/` mất khi container restart — khi đó phải **mount volume** vào `LOG_DIR` để giữ log. Ghi rõ điều này trong README triển khai.

```ts
// lib/logger.ts — ghi file trong <install-dir>/log + stdout khi dev
import pino from 'pino';
import path from 'node:path';
import fs from 'node:fs';

const logDir = process.env.LOG_DIR ?? path.join(__dirname, '..', 'log');
fs.mkdirSync(logDir, { recursive: true });

const targets = [
  { target: 'pino-roll', options: { file: path.join(logDir, 'app'), frequency: 'daily', size: '20m', limit: { count: 14 } } },
];
if (process.env.NODE_ENV !== 'production') targets.push({ target: 'pino/file', options: { destination: 1 } }); // stdout

export const logger = pino({ level: process.env.LOG_LEVEL ?? 'info' }, pino.transport({ targets }));
```

### Mức log (level) — dùng đúng mức

| Level | Khi nào dùng | Ví dụ |
|-------|-------------|-------|
| `debug` | Chi tiết nội bộ chỉ cần khi dev/debugging | Giá trị trung gian, SQL query thô |
| `info` | Sự kiện nghiệp vụ quan trọng, trạng thái bình thường | `order.created`, `user.login` |
| `warn` | Bất thường nhưng hệ thống vẫn chạy được | Retry lần 2, cấu hình thiếu nhưng có fallback |
| `error` | Lỗi làm hỏng request/job; phải điều tra | Exception chưa xử lý, external API fail |

> **Không log `debug` ở production** — mặc định level production là `info`.
> Bật `debug` tạm qua env var (`LOG_LEVEL=debug`) để điều tra, tắt lại sau.

### Quy tắc nội dung log

- **Log đủ context để tái hiện bug không cần hỏi lại:**
  - ✅ `logger.error('payment.charge_failed', { traceId, userId, amount, currency, err })`
  - ❌ `logger.error('something went wrong')` — vô dụng khi debug.
- **Không log secret / PII:** không log password, token, số thẻ, CCCD/CMND, số điện thoại đầy đủ.
  Che trước khi log: `maskCard('4111-1111-1111-1111') → '****-****-****-1111'`.
- **Không log toàn bộ request body** nếu chứa field nhạy cảm — chỉ log field cần thiết.
- **Một sự kiện = một log entry.** Không tách một sự kiện ra nhiều dòng rời rạc.
- **Message dùng `snake_case.dot_notation`** để dễ filter: `user.login`, `order.created`, `db.query_slow`.

### Ví dụ (TypeScript)

```ts
// lib/logger.ts — wrapper duy nhất của dự án
import pino from 'pino';
export const logger = pino({ level: process.env.LOG_LEVEL ?? 'info' });

// Trong service
import { logger } from '@/lib/logger';
import { getTraceId } from '@/lib/trace-context';

async function chargePayment(userId: string, amount: number) {
  const traceId = getTraceId();
  logger.info({ traceId, userId, amount }, 'payment.charge_start');
  try {
    const result = await stripe.charges.create({ amount });
    logger.info({ traceId, userId, chargeId: result.id }, 'payment.charge_success');
    return result;
  } catch (err) {
    logger.error({ traceId, userId, amount, err }, 'payment.charge_failed');
    throw err;  // không nuốt lỗi
  }
}
```

### Ví dụ (Python)

```python
import logging
logger = logging.getLogger(__name__)

def charge_payment(trace_id: str, user_id: str, amount: int):
    logger.info("payment.charge_start", extra={"trace_id": trace_id, "user_id": user_id, "amount": amount})
    try:
        result = stripe.charge(amount)
        logger.info("payment.charge_success", extra={"trace_id": trace_id, "charge_id": result.id})
        return result
    except Exception as err:
        logger.error("payment.charge_failed", extra={"trace_id": trace_id, "amount": amount}, exc_info=True)
        raise
```

### Kiểm tra tự động (CI)

- **Cấm `console.log` / `print` trong code nghiệp vụ** (chỉ cho phép trong test/scripts):
  - ESLint: bật rule `no-console` (error) cho `src/` — ngoại lệ `/* eslint-disable-next-line no-console */` phải có lý do.
  - Ruff/flake8: dùng `S002` hoặc pre-commit hook grep `^\s*print(` trong `app/` / `src/`.
- **Không log secret:** pre-commit hook hoặc CI scan (ví dụ `gitleaks`) để bắt credential slip.

## 6. Tests — Kiểm thử

- Viết/cập nhật test cho **logic có ý nghĩa** (nghiệp vụ, biên, lỗi). Không cần test thứ tầm thường.
- **Co-locate:** đặt test cạnh code (`foo.ts` + `foo.test.ts`) để người sửa thấy ngay.
- Theo đúng framework test sẵn có của dự án.

## 7. Internationalization (i18n) — Đa ngôn ngữ (Việt + Anh)

> Ứng dụng hỗ trợ **tiếng Việt và tiếng Anh**.

- **Không hardcode chuỗi hiển thị.** — Dùng translation key (`locales/`).
- **Mỗi key mới có đủ `vi` và `en`.**
- Lưu ý định dạng ngày/số/tiền khác nhau giữa hai locale.
- Không xóa/đổi tên key đang dùng mà chưa kiểm tra nơi tham chiếu.
- Nếu dự án chưa có i18n, hỏi trước khi thêm thư viện.

## 8. Diffs — Thay đổi nhỏ, gọn

- Diff nhỏ, một mục đích, dễ review. Không format lại code ngoài phần đang sửa.
- Không trộn refactor lớn vào commit sửa lỗi.

## 9. Code tái dùng & trích xuất thư viện — Reusable & extraction-ready

> Mục tiêu: nhấc một mảnh code ra thành **thư viện** chỉ bằng *copy* (hoặc *publish*),
> không phải gỡ rối phụ thuộc. Cái khiến code khó trích là *phụ thuộc lẫn lộn* — nên kỷ
> luật là **cô lập lõi tái dùng**.

**Quy tắc (BẮT BUỘC cho code đặt trong `lib/` hoặc `packages/`):**
1. **Tách lõi khỏi keo ứng dụng.** Logic tái dùng sống ở `*/lib/<pkg>/` (hoặc `packages/<pkg>/`),
   tách khỏi code dính dự án (`routes`, `pages`, `controllers`, `config`).
2. **Không phụ thuộc ngược vào app.** `lib/` **không** import từ `app/`/`routes`/`services`/`store`/
   `controllers`/`models`/`config`; không đọc global env/DB singleton; không bám framework.
   Phụ thuộc được **truyền vào** (dependency injection), không **với ra** lấy.
3. **Một cửa API công khai.** Mỗi module có `index.ts`/`__init__.py` re-export đúng phần công khai;
   ẩn nội bộ. Bên ngoài chỉ import qua cửa này.
4. **Tự đủ.** Mang theo *types, errors, tests, README* của chính nó (không bám `shared/types` của app,
   hoặc chỉ bám một core rất ổn định).
5. **Lõi thuần; side-effect ở rìa.** Business logic là hàm thuần; I/O (network/DB/fs) inject qua interface.
6. **Tối thiểu dependency; public API là hợp đồng** (đổi public API = breaking).

**Hai mức tổ chức (A mặc định → B khi chín):**
- **A — lib-in-place:** `*/lib/<pkg>/` tự đủ; **trích xuất = copy thư mục**.
- **B — workspace package:** `packages/<pkg>/` là package thật (`package.json`/`pyproject`); **trích xuất = publish**.
  Nâng A → B khi module đã ổn định & dùng ở **≥ 2 nơi**.

> Kiểm tra ranh giới: `bash scripts/check-lib-boundaries.sh` (chặn nếu `lib/` import ngược vào app).
> Quy trình nhấc một module ra: xem [docs/EXTRACTION.md](docs/EXTRACTION.md).

## 10. Responsive UI (web) — BẮT BUỘC nếu là ứng dụng web

> Ứng dụng web **mặc định phải responsive**: giao diện tự thích ứng mọi trình duyệt,
> **mobile / tablet / desktop**, KHÔNG bể layout, KHÔNG tràn ngang (no horizontal scroll).

- **Mobile-first:** thiết kế cho màn hình nhỏ trước, rồi mở rộng lên bằng breakpoint.
- **Layout linh hoạt:** dùng **flexbox/grid** + đơn vị tương đối (`rem`/`%`/`vw`/`fr`/`clamp()`).
  **Không hardcode `px` cố định** cho width/chiều cao container; ưu tiên `max-width`, `min()/max()`.
- **Viewport:** trang phải có `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- **Breakpoints nhất quán:** theo framework (Tailwind `sm/md/lg/xl/2xl`...) hoặc ~`640/768/1024/1280px`. Không đặt breakpoint tuỳ tiện.
- **Media responsive:** ảnh/video `max-width:100%`, `height:auto`, dùng `srcset`/`sizes` khi cần.
- **Chạm & truy cập:** vùng chạm ≥ ~44px; không phụ thuộc `:hover` (mobile không có hover); test bàn phím.
- **Kiểm thử nhiều kích thước:** DevTools responsive **và** thiết bị thật (mobile/tablet); đảm bảo không vỡ ở các breakpoint ranh giới.
- **SDLC:** ghi "responsive" như một yêu cầu phi chức năng trong `SRS`; thêm `TC` kiểm tra ở ≥3 kích thước (mobile/tablet/desktop). Mọi `SCR` (User Manual) áp dụng cho cả 3.

> _Web apps must be responsive by default: layouts adapt to mobile/tablet/desktop without
> breaking. Mobile-first, fluid units, viewport meta, consistent breakpoints, tested on real devices._

## 11. Icons — mặc định Tabler Icons (MIT)

> Dùng **[Tabler Icons](https://tabler.io/icons)** (license **MIT**, ~5.000+ icon nét nhất quán)
> làm bộ icon **mặc định**. Khớp chính sách dependency MIT/Apache (xem §5 trong harness).

- **Mặc định Tabler:** cần icon → lấy từ Tabler trước. Không tự vẽ icon lẻ tẻ, không trộn nhiều bộ icon.
- **Cài:** `@tabler/icons-react` (React) / `@tabler/icons-vue` / `@tabler/icons` (SVG) / webfont — tuỳ stack.
- **KHÔNG dùng** bộ icon proprietary hoặc license khác MIT/Apache (vd Font Awesome Pro).
- **Thiếu icon trong Tabler** → chỉ thêm bộ khác khi **bắt buộc** VÀ license MIT/Apache-2.0; **hỏi trước** (theo rule dependency).
- Giữ kích thước/stroke nhất quán; icon có nhãn cho trợ năng (aria-label) khi không kèm text.
