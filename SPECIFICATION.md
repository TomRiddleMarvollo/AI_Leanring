# AI Learning Hub — Technical Specification

> **Mục đích tài liệu này:** Đặc tả đầy đủ để một hệ thống AI đọc và sinh lại toàn bộ source code từ đầu mà không cần xem code gốc. Mọi hành vi, cấu trúc dữ liệu, API contract, business rule và quyết định kỹ thuật đều được ghi lại ở đây.

---

## 1. Tổng quan ứng dụng

**AI Learning Hub** là một web application full-stack giúp người học AI:

1. Đọc tin tức AI mới nhất được tóm tắt tự động từ 50+ nguồn uy tín.
2. Học các best practices qua các module được AI trích xuất từ các bài viết chuyên sâu.
3. Thực hành Prompt Engineering trực tiếp với AI (cloud hoặc local) trong một workspace có lịch sử, dự án, và custom agents.

**Ngôn ngữ chính:** Tiếng Việt (UI), Tiếng Anh (code, API, prompt nội bộ).

---

## 2. Kiến trúc tổng thể

```
┌─────────────────────────────────────────────────────┐
│  Browser                                             │
│  React 18 + Vite + Axios + marked + lucide-react    │
└──────────────────────┬──────────────────────────────┘
                       │ HTTP /api/*
┌──────────────────────▼──────────────────────────────┐
│  Backend: FastAPI (Python 3.11)                      │
│  ├── main.py       — REST API endpoints + CORS       │
│  ├── agent.py      — LLM logic (Gemini / Ollama)    │
│  ├── database.py   — SQLAlchemy ORM models           │
│  ├── tools.py      — Web search + content fetch      │
│  └── sources.py    — Danh sách 90+ AI sources        │
└──────────┬───────────────────────┬──────────────────┘
           │ SQLAlchemy            │ HTTP
┌──────────▼──────┐    ┌───────────▼────────────────┐
│ PostgreSQL 15   │    │ Google Gemini 2.5 Flash API │
│ (hoặc SQLite   │    │ hoặc Ollama (local LLM)     │
│  khi dev)      │    └────────────────────────────┘
└─────────────────┘
```

### Môi trường

| Môi trường | DB | Backend port | Frontend port | Hot-reload |
|---|---|---|---|---|
| `development` | SQLite `data/dev.db` | 8000 | 5173 | Có |
| `test` | PostgreSQL port 5433, tmpfs | 8000 | — | Không |
| `staging` | PostgreSQL `aihub_staging` | 8001 | 7071 | Không |
| `production` | PostgreSQL `aihub_prod` | 8000 (internal) | 80/443 | Không |

Cấu hình mỗi môi trường nằm trong `environments/<env>/.env` và `environments/<env>/docker-compose.yml`.

---

## 3. Cấu trúc thư mục

```
/
├── Makefile                        # Lệnh tắt: make dev, make test, make prod, ...
├── config.yaml                     # { model: "llama3", temperature: 0.7 }
├── docker-compose.yml              # (legacy, dùng environments/ thay thế)
├── environments/
│   ├── dev/
│   │   ├── .env                    # Commit được (không chứa secret)
│   │   └── docker-compose.yml
│   ├── test/
│   │   ├── .env                    # Commit được
│   │   └── docker-compose.yml
│   ├── staging/
│   │   ├── .env                    # KHÔNG commit
│   │   └── docker-compose.yml
│   └── production/
│       ├── .env                    # KHÔNG commit
│       └── docker-compose.yml
├── prompts/
│   └── system_prompts/
│       └── default_system.txt      # System prompt mặc định cho chat
├── src/
│   ├── backend/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── main.py
│   │   ├── agent.py
│   │   ├── database.py
│   │   ├── tools.py
│   │   └── sources.py
│   └── frontend/
│       ├── Dockerfile              # Multi-stage: node build → nginx serve
│       ├── nginx.conf
│       ├── vite.config.js
│       ├── package.json
│       ├── .env.development
│       ├── .env.test
│       ├── .env.staging
│       ├── .env.production
│       └── src/
│           ├── main.jsx
│           ├── App.jsx
│           ├── index.css
│           └── components/
│               ├── NewsFeed.jsx
│               ├── LearningHub.jsx
│               └── PracticeArea.jsx
├── tests/
│   ├── test_gemini_api.py
│   └── test_ollama_speed.py
└── data/                           # SQLite files (gitignore)
```

---

## 4. Backend

### 4.1 Môi trường & biến env

| Biến | Mặc định | Mô tả |
|---|---|---|
| `DATABASE_URL` | `sqlite:///./data/dev.db` | PostgreSQL hoặc SQLite URL |
| `GEMINI_API_KEY` | `""` | API key Google AI Studio |
| `MODEL_PROVIDER` | `"gemini"` | `"gemini"` hoặc `"ollama"` |
| `OLLAMA_HOST` | `http://localhost:11434` | URL Ollama server |
| `DEFAULT_MODEL` | đọc từ `config.yaml` → `"llama3"` | Tên model Ollama mặc định |
| `ALLOWED_ORIGINS` | `http://localhost:5173,http://localhost:3000` | CORS whitelist, ngăn cách bằng dấu phẩy |
| `CONFIG_PATH` | `config.yaml` (tìm từ project root) | Đường dẫn tuyệt đối tới config.yaml |
| `PROMPT_PATH` | `prompts/system_prompts/default_system.txt` | Đường dẫn tới system prompt |

**Logic chọn provider:** Nếu `GEMINI_API_KEY` không rỗng VÀ `MODEL_PROVIDER == "gemini"` → dùng Gemini. Ngược lại → dùng Ollama. Gemini luôn fallback sang Ollama khi gặp lỗi.

### 4.2 Dependencies (`requirements.txt`)

```
fastapi==0.111.0
uvicorn==0.30.1
ollama==0.2.1
googlesearch-python==1.2.4
beautifulsoup4==4.12.3
requests==2.32.3
python-dotenv==1.0.1
pydantic==2.7.4
sqlalchemy==2.0.31
psycopg2-binary==2.9.9
PyYAML==6.0.1
google-generativeai==0.5.4
slowapi==0.1.9
```

### 4.3 `database.py` — ORM Models

Database URL được đọc từ env `DATABASE_URL`. Nếu SQLite, thêm `connect_args={"check_same_thread": False}`. Tất cả bảng được tạo tự động qua `Base.metadata.create_all()`.

**Bảng `news`**

| Cột | Kiểu | Ghi chú |
|---|---|---|
| `id` | Integer PK autoincrement | |
| `title` | String indexed | Tiêu đề bài viết |
| `summary` | Text | Tóm tắt do AI tạo |
| `url` | String | URL gốc |
| `rating` | Integer default 0 | Điểm 1–10 do AI chấm |
| `published_at` | DateTime default utcnow | |

**Bảng `learning_modules`**

| Cột | Kiểu | Ghi chú |
|---|---|---|
| `id` | Integer PK autoincrement | |
| `title` | String indexed | |
| `content` | Text | Markdown list của best practices |
| `category` | String | `"Prompt Engineering"` hoặc `"General AI"` |
| `created_at` | DateTime default utcnow | |

**Bảng `projects`**

| Cột | Kiểu | Ghi chú |
|---|---|---|
| `id` | String PK | UUID do client tạo |
| `name` | String indexed | |
| `created_at` | DateTime default utcnow | |

**Bảng `agents`**

| Cột | Kiểu | Ghi chú |
|---|---|---|
| `id` | String PK | UUID do client tạo |
| `name` | String indexed | Tên hiển thị |
| `system_prompt` | Text | System prompt tùy chỉnh |
| `model_id` | String | ID model trong danh sách `/api/models` |
| `color` | String nullable | Hex color hoặc tên màu |
| `icon` | String nullable | Tên icon từ `lucide-react` |
| `created_at` | DateTime default utcnow | |

**Bảng `conversations`**

| Cột | Kiểu | Ghi chú |
|---|---|---|
| `id` | String PK | UUID do client tạo |
| `project_id` | String indexed | FK → `projects.id` (soft, không enforce) |
| `name` | String indexed | |
| `agent_id` | String nullable | FK → `agents.id` (soft) |
| `created_at` | DateTime default utcnow | |

> **Migration runtime:** Khi khởi động, backend thử chạy `ALTER TABLE conversations ADD COLUMN agent_id VARCHAR`. Nếu cột đã tồn tại → bắt exception và bỏ qua.

**Bảng `messages`**

| Cột | Kiểu | Ghi chú |
|---|---|---|
| `id` | Integer PK autoincrement | |
| `conversation_id` | String indexed | FK → `conversations.id` (soft) |
| `role` | String | `"user"` hoặc `"ai"` |
| `content` | Text | Nội dung tin nhắn (có thể markdown) |
| `model_name` | String nullable | Tên model AI đã trả lời |
| `created_at` | DateTime default utcnow | |

### 4.4 `main.py` — REST API

#### Setup

```python
# CORS — đọc từ ALLOWED_ORIGINS env, split(",")
allow_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://localhost:3000").split(",")
# allow_credentials = False
# allow_methods = ["GET", "POST", "DELETE"]
# allow_headers = ["Content-Type"]

# Rate limiting (slowapi)
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
```

#### Endpoints

---

**`GET /`**
```json
{ "message": "Welcome to the AI Learning Web Hub API" }
```

---

**`GET /api/news?skip=0&limit=20`**

Trả về danh sách `NewsItem`, order by `rating DESC, published_at DESC`.

Response: `List[NewsItem]` (tất cả cột).

---

**`GET /api/learn?skip=0&limit=20`**

Trả về danh sách `LearningModule`, order by `created_at DESC`.

---

**`GET /api/models`**

Trả về danh sách model khả dụng. Luôn có Gemini đầu tiên, sau đó là tất cả model Ollama tìm được qua `ollama_client.list()`. Nếu không tìm được model Ollama nào, thêm placeholder `"llama3 (Chưa tải)"`.

Response schema cho mỗi model:
```json
{
  "id": "gemini",
  "name": "Google Gemini 2.5 Flash",
  "provider": "gemini",
  "model_name": "gemini-2.5-flash",
  "description": "Cloud API - Siêu tốc & Siêu trí tuệ"
}
```

Ollama models có `id = "ollama/<model_name>"`, `provider = "ollama"`.

---

**`POST /api/practice`** — Rate limit: 20 requests/minute/IP

Request body (`PracticeRequest`):
```json
{
  "prompt": "string (required)",
  "provider": "string | null — 'gemini' hoặc 'ollama'",
  "model_name": "string | null — tên model Ollama cụ thể",
  "system_prompt": "string | null — override system prompt",
  "file_data": "string | null — base64 encoded file content",
  "file_name": "string | null",
  "file_type": "string | null — MIME type"
}
```

Response:
```json
{ "response": "string — nội dung AI trả lời" }
```

**Logic xử lý file (trong `agent.py::practice_chat`):**

1. Nếu có file: normalize `file_type` (strip params sau `;`), kiểm tra trong whitelist `_SAFE_FILE_TYPES`. Nếu không hợp lệ → trả về thông báo lỗi ngay (không gọi AI).
2. `is_binary = True` nếu MIME bắt đầu bằng `image/`, `audio/`, `video/`, hoặc là `application/pdf`.
3. **Gemini + binary:** gửi `[{"mime_type": ..., "data": bytes}, prompt_text]` tới `generate_content`.
4. **Gemini + text:** decode UTF-8, `_sanitize_file_text()` (strip null bytes, giới hạn 12,000 ký tự), tạo augmented prompt:
   ```
   Tài liệu đính kèm (<file_name>):
   ```
   <nội dung>
   ```
   
   Yêu cầu người dùng:
   <prompt>
   ```
5. **Ollama + binary:** trả về thông báo không hỗ trợ, gợi ý dùng Gemini.
6. **Ollama + text:** decode, sanitize, tạo augmented prompt tương tự.
7. **Fallback:** Nếu Gemini lỗi, tự động retry với Ollama.

**Whitelist MIME types cho file upload:**
```python
_SAFE_FILE_TYPES = {
    "text/plain", "text/markdown", "text/csv", "text/html",
    "application/json", "application/xml", "text/xml",
    "image/png", "image/jpeg", "image/gif", "image/webp",
    "audio/mpeg", "audio/wav", "video/mp4",
    "application/pdf",
}
```

---

**`POST /api/agent/run`** → 202 Accepted

Trigger background task `run_all_background_tasks()` (FastAPI `BackgroundTasks`). Không chặn response.

---

**`GET /api/projects`**

Trả về tất cả projects. Nếu DB trống → seed 1 project mặc định: `{ id: "proj-1", name: "Dự án AI Learning Hub 🚀" }`.

**`POST /api/projects`** — Body: `ProjectSchema { id, name }`

Upsert: nếu `id` đã tồn tại → update `name`. Ngược lại → tạo mới.

**`DELETE /api/projects/{proj_id}`**

Xóa project, tất cả conversations của nó, và tất cả messages của các conversations đó (cascade thủ công).

---

**`GET /api/agents`**

Trả về tất cả agents. Nếu DB trống → seed 1 agent mặc định:
```json
{
  "id": "agent-default-1",
  "name": "Chuyên gia Prompt 💡",
  "system_prompt": "Bạn là một chuyên gia về Prompt Engineering...",
  "model_id": "gemini",
  "color": "#2563eb",
  "icon": "Sparkles"
}
```

**`POST /api/agents`** — Body: `AgentSchema { id, name, system_prompt, model_id, color?, icon? }`

Upsert tương tự projects.

**`DELETE /api/agents/{agent_id}`**

Xóa agent. Set `agent_id = null` trên tất cả conversations đang dùng agent đó.

---

**`GET /api/conversations`**

Trả về tất cả conversations kèm messages đầy đủ, order by `message.id ASC`.

Nếu DB trống → seed 1 conversation mặc định trong project `"proj-1"` kèm 1 message chào hỏi từ AI.

Response: `List[ConversationSchema]`
```json
[{
  "id": "chat-1",
  "projectId": "proj-1",
  "name": "Hội thoại Prompt Engineering 💡",
  "agentId": null,
  "messages": [
    { "role": "ai", "content": "...", "modelName": "Hệ thống AI" }
  ]
}]
```

**`POST /api/conversations`** — Body: `ConversationSchema`

Upsert conversation + **replace toàn bộ messages**: xóa messages cũ, insert lại từ body. Đây là cơ chế sync đơn giản (client là source of truth cho messages).

**`DELETE /api/conversations/{chat_id}`**

Xóa conversation và tất cả messages của nó.

---

### 4.5 `agent.py` — LLM Logic

#### Background scraping

**`run_all_background_tasks()`**

- Lấy tất cả URLs từ `AI_SOURCES` (tất cả categories).
- Dùng `ThreadPoolExecutor(max_workers=2)` để giới hạn VRAM.
- Với mỗi source: submit `process_news_source(source)` và `process_learning_source(source)`.
- `time.sleep(2)` giữa mỗi source để tránh rate limit DuckDuckGo.

**`process_news_source(source)`**

1. `search_web(f"Latest AI advancements news site:{source}", max_results=2)`.
2. Với mỗi kết quả: kiểm tra URL đã tồn tại trong DB chưa (skip nếu có).
3. `fetch_content(url)` → nếu rỗng thì dùng snippet.
4. Gửi prompt đánh giá + tóm tắt tới LLM. Prompt yêu cầu LLM trả về JSON thuần:
   ```json
   {"summary": "...", "rating": 8}
   ```
5. Parse JSON, lưu `NewsItem` vào DB.
6. Gemini dùng `response_mime_type="application/json"`. Ollama cần strip markdown code block (`removeprefix("```json")`, `removesuffix("```")`).

**Rating rubric trong prompt:**
- Technical & Educational Value (50%): dạy khái niệm mới, code, prompt technique?
- Actionability (30%): có thể thực hành ngay?
- Clarity (20%): có facts/benchmarks thay vì clickbait?

**`process_learning_source(source)`**

1. `search_web(f"AI best practices guide site:{source}", max_results=1)`.
2. Kiểm tra title đã tồn tại trong `learning_modules` chưa.
3. Prompt yêu cầu LLM trả về markdown list các actionable tips.
4. Category: `"Prompt Engineering"` nếu `"prompt"` in `title.lower()`, ngược lại `"General AI"`.
5. Lưu `LearningModule`.

#### `tools.py` — Web utilities

**`search_web(query, max_results=5)`**

- POST tới `https://html.duckduckgo.com/html/` với `data={'q': query}`.
- Parse HTML với BeautifulSoup, extract `.result` elements.
- Decode `uddg=` encoded URLs.
- Bỏ qua results có `ad_domain` hoặc không bắt đầu bằng `http`.
- Trả về `List[{"title", "href", "body"}]`.

**`fetch_content(url)`**

- **SSRF protection:** Trước khi fetch, gọi `_is_safe_url(url)`:
  - Chỉ chấp nhận scheme `http` hoặc `https`.
  - Block IP private/loopback/link-local (`ipaddress.ip_address`).
  - Block hostname: `localhost`, `metadata.google.internal`, `*.local`.
- `requests.get(url, timeout=10, allow_redirects=False)`.
- BeautifulSoup: remove `script`, `style`, `nav`, `footer`, `header`.
- Trả về text tối đa 4,000 ký tự.

#### `sources.py` — AI Sources

5 categories: `Personal Sites`, `Research Labs`, `Code and Tools`, `AI Safety`, `Media`. Tổng ~90 domains.

---

## 5. Frontend

### 5.1 Stack

- **React 18** (JSX, hooks)
- **Vite** — dev server + build tool
- **Axios** — HTTP client, gọi qua `/api/*` (proxy tới backend)
- **marked** — render markdown trong chat messages
- **lucide-react** — icon library

### 5.2 Environment variables (Vite)

| Biến | Mô tả |
|---|---|
| `VITE_API_URL` | URL backend (chỉ dùng cho proxy config trong vite.config.js) |
| `VITE_ENV` | `development` / `test` / `staging` / `production` |

File `.env.development`, `.env.test`, `.env.staging`, `.env.production` tương ứng mỗi môi trường. Docker build nhận qua `ARG VITE_API_URL` và `ARG VITE_ENV`.

### 5.3 `vite.config.js`

```js
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')
  const apiUrl = env.VITE_API_URL || 'http://localhost:8000'
  return {
    plugins: [react()],
    server: {
      host: true,
      proxy: { '/api': { target: apiUrl, changeOrigin: true } }
    }
  }
})
```

### 5.4 `App.jsx` — Root Component

**State được lift lên App:**

| State | Kiểu | Mô tả |
|---|---|---|
| `activeTab` | `'news' \| 'learning' \| 'practice'` | Tab hiện tại |
| `projects` | `Project[]` | Danh sách projects |
| `activeProjectId` | `string \| null` | Project đang chọn |
| `conversations` | `Conversation[]` | Tất cả conversations |
| `activeConversationId` | `string \| null` | Conversation đang chọn |
| `selectedModelId` | `string` | Model ID đang chọn, persist localStorage |

**`useEffect` khởi động (load workspace):**

1. Fetch `GET /api/projects` và `GET /api/conversations` song song.
2. **Migration localStorage → PostgreSQL:** Nếu localStorage có `ai_learning_projects` và `ai_learning_conversations`, và DB gần như trống (chỉ có seeded defaults), thì POST từng item lên DB rồi xóa localStorage keys.
3. Resolve `activeProjectId`: ưu tiên `localStorage('ai_learning_active_project_id')` nếu còn hợp lệ.
4. Resolve `activeConversationId`: ưu tiên `localStorage('ai_learning_active_conversation_id')` nếu thuộc project đang chọn.

**LocalStorage keys:**
- `ai_learning_selected_model` — model ID
- `ai_learning_active_project_id`
- `ai_learning_active_conversation_id`
- `ai_learning_sidebar_collapsed`
- `ai_learning_projects_expanded`
- `ai_learning_agents_expanded`
- `ai_learning_conversations_expanded`

**Header:**
- Logo: `<Sparkles /> AI Learning Hub`
- Nav buttons: Tin tức AI / Bài học / Thực hành
- Nút "Cập nhật DL": gọi `POST /api/agent/run`, hiện spinner khi loading, alert thông báo background task đã bắt đầu (10–20 phút).

### 5.5 `NewsFeed.jsx`

- Fetch `GET /api/news` khi mount.
- Render danh sách: thumbnail "AI NEWS", title là link (`target="_blank"`), summary, badge "AI Tech", star rating (`★` fill, `☆` empty cho 10 sao), ngày.
- Empty state: "Chưa có tin tức nào. Vui lòng bấm Cập nhật DL."

### 5.6 `LearningHub.jsx`

- Fetch `GET /api/learn` khi mount.
- Render danh sách: thumbnail "AI GUIDE", title, content (`white-space: pre-line`), badge category, ngày.
- Empty state: "Chưa có bài học nào. Vui lòng bấm Cập nhật DL."

### 5.7 `PracticeArea.jsx` — Workspace chính

Đây là component phức tạp nhất (~1400 lines). Nhận tất cả workspace state từ `App.jsx` qua props.

#### Props

```
projects, setProjects,
activeProjectId, setActiveProjectId,
conversations, setConversations,
activeConversationId, setActiveConversationId,
selectedModelId, setSelectedModelId
```

#### State nội bộ

| State | Mô tả |
|---|---|
| `models` | Danh sách models, default là Gemini, fetch từ `/api/models` |
| `dropdownOpen` | Dropdown chọn model |
| `input` | Nội dung textarea input |
| `loading` | Đang chờ AI response |
| `fetchingModels` | Đang fetch model list |
| `editingId`, `editingValue`, `editType` | Inline rename project/conversation |
| `agents` | Danh sách custom agents |
| `agentModalOpen` | Modal tạo/sửa agent |
| `editingAgent` | Agent đang edit (null nếu tạo mới) |
| `agentName`, `agentSystemPrompt`, `agentModelId`, `agentColor`, `agentIcon` | Form fields cho agent |
| `isSidebarCollapsed` | Sidebar thu gọn, persist localStorage |
| `isProjectsExpanded` | Accordion section, persist localStorage |
| `isAgentsExpanded` | Accordion section, persist localStorage |
| `isConversationsExpanded` | Accordion section, persist localStorage |
| `attachedFile` | `{ name, size, type, data (base64) } \| null` |

#### Derived values (useMemo / computed)

```js
activeConversation = conversations.find(c => c.id === activeConversationId)
activeMessages = activeConversation?.messages ?? []
activeModel = models.find(m => m.id === selectedModelId) ?? models[0]
activeAgent = agents.find(a => a.id === activeConversation?.agentId) ?? null
projectConversations = conversations.filter(c => c.projectId === activeProjectId)
```

#### useEffect hooks

1. **Fetch models:** Khi mount → `GET /api/models` → setModels. Preserve `selectedModelId` nếu còn trong danh sách mới.
2. **Fetch agents:** Khi mount → `GET /api/agents` → setAgents.
3. **Auto-scroll:** Khi `activeMessages` thay đổi → scroll `chatHistoryRef.current` xuống cuối.
4. **Auto-resize textarea:** Khi `input` thay đổi → reset height về `"auto"` rồi set `scrollHeight`.

#### File attachment flow

1. `<input type="file" style={{display:'none'}} ref={fileInputRef} />` ẩn trong DOM.
2. Nút paperclip click → `fileInputRef.current.click()`.
3. `handleFileChange`: validate size ≤ 10MB. Dùng `FileReader.readAsDataURL()` → split `','` lấy phần base64.
4. `attachedFile` state: `{ name, size, type (hoặc 'application/octet-stream'), data (base64) }`.
5. Hiển thị preview chip phía trên input: tên file, size (KB), nút X để remove.
6. Nút send enabled nếu `input.trim().length > 0 || attachedFile !== null`.

#### `handleSend()`

1. Guard: `(!input.trim() && !attachedFile) || loading || !activeConversationId` → return.
2. `userMessageContent`: nếu input rỗng nhưng có file → `"Hãy phân tích tài liệu đính kèm này."`.
3. `displayMessageContent`: append `"\n\n📎 *[Đính kèm: <filename>]*"` nếu có file.
4. Snapshot `fileToSend = attachedFile`. Clear `input` và `attachedFile`.
5. Tạo `userMsg = { role: 'user', content: displayMessageContent }`.
6. Update `conversations` state optimistically (thêm userMsg).
7. `POST /api/practice` với `{ prompt: userMessageContent, provider, model_name (nếu ollama), system_prompt (nếu agent), file_data, file_name, file_type }`.
8. `resolvedModel`: nếu có `activeAgent`, tìm model theo `activeAgent.model_id`; fallback `activeModel`.
9. Tạo `aiMsg = { role: 'ai', content: response.data.response, modelName: resolvedModel.name }`.
10. Update `conversations` state với aiMsg.
11. `POST /api/conversations` để sync toàn bộ conversation lên DB.

#### Sidebar layout

```
┌──────────────────────────────┐
│ [←] Thu gọn                  │
├──────────────────────────────┤
│ ▼ DỰ ÁN (accordion)          │
│   [proj-1] + nút thêm/xóa    │
│   ...                        │
├──────────────────────────────┤
│ ▼ AI AGENTS (accordion)      │
│   [agent chip] + nút thêm    │
│   ...                        │
├──────────────────────────────┤
│ ▼ HỘI THOẠI (accordion)      │
│   [chat-1] + nút thêm/xóa    │
│   ...                        │
└──────────────────────────────┘
```

Khi `isSidebarCollapsed = true`: sidebar hiển thị chỉ icon, nút [→] để mở lại.

#### Agent modal

Form fields: Name, System Prompt (textarea), Model (dropdown từ `models`), Color (preset chips), Icon (preset từ `iconMap`).

- Create: `POST /api/agents` với UUID mới (`crypto.randomUUID()`).
- Edit: `POST /api/agents` với `id` cũ (upsert).
- Delete: `DELETE /api/agents/{id}`.

#### Chat area

- Header: tên conversation + tên agent đang dùng (nếu có).
- Messages: render markdown với `dangerouslySetInnerHTML={{ __html: marked.parse(content) }}`.
- User messages: căn phải, background accent.
- AI messages: căn trái, avatar icon.
- AI message footer: hiển thị `modelName` (tên model đã trả lời).
- Loading indicator: animated dots khi `loading = true`.

#### Input area

```
┌─────────────────────────────────────────────┐
│ [📎 file preview chip]                       │
│ ┌─────────────────────────────────────────┐ │
│ │ [+] [textarea.....................] [→] │ │
│ └─────────────────────────────────────────┘ │
│ [Model selector dropdown]                   │
└─────────────────────────────────────────────┘
```

- Nút `+` (Paperclip): trigger file input.
- Textarea: auto-resize, Enter gửi (Shift+Enter xuống dòng).
- Nút send disabled khi `loading || (!input.trim() && !attachedFile) || !activeConversationId`.
- Model selector: hiển thị tên model hiện tại, click mở dropdown chọn model khác.

---

## 6. API Contract Summary

| Method | Path | Auth | Rate limit | Mô tả |
|---|---|---|---|---|
| GET | `/` | — | — | Health check |
| GET | `/api/news` | — | — | Danh sách tin tức |
| GET | `/api/learn` | — | — | Danh sách learning modules |
| GET | `/api/models` | — | — | Danh sách AI models |
| POST | `/api/practice` | — | 20/min/IP | Chat với AI |
| POST | `/api/agent/run` | — | — | Trigger background scrape |
| GET | `/api/projects` | — | — | Danh sách projects |
| POST | `/api/projects` | — | — | Upsert project |
| DELETE | `/api/projects/{id}` | — | — | Xóa project + cascade |
| GET | `/api/agents` | — | — | Danh sách custom agents |
| POST | `/api/agents` | — | — | Upsert agent |
| DELETE | `/api/agents/{id}` | — | — | Xóa agent |
| GET | `/api/conversations` | — | — | Danh sách conversations + messages |
| POST | `/api/conversations` | — | — | Upsert conversation + replace messages |
| DELETE | `/api/conversations/{id}` | — | — | Xóa conversation + messages |

---

## 7. Nginx config (production/staging frontend)

```nginx
server {
    listen 80;
    server_name localhost;

    # SPA routing: tất cả path → index.html
    location / {
        root /usr/share/nginx/html;
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    # Proxy /api/ → backend:8000
    location /api/ {
        proxy_pass http://backend:8000/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 300s;
        proxy_connect_timeout 300s;
    }
}
```

---

## 8. Dockerfile specs

### Backend

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Dev override CMD: `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`

### Frontend (multi-stage)

```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
ARG VITE_API_URL=http://localhost:8000
ARG VITE_ENV=production
ENV VITE_API_URL=$VITE_API_URL
ENV VITE_ENV=$VITE_ENV
COPY package.json package-lock.json* ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## 9. Security constraints

| Constraint | Áp dụng ở đâu |
|---|---|
| File type whitelist (MIME) | `agent.py::_SAFE_FILE_TYPES` |
| File content sanitize (null bytes + 12KB limit) | `agent.py::_sanitize_file_text()` |
| SSRF protection (block private IP, localhost) | `tools.py::_is_safe_url()` |
| Rate limiting 20/min/IP | `main.py` `/api/practice` via slowapi |
| CORS chỉ allow origins từ env | `main.py` ALLOWED_ORIGINS |
| `allow_credentials = False` | `main.py` |
| Không expose DB port ra ngoài (production) | `docker-compose` network `internal: true` |
| Backend dùng `expose:` thay `ports:` (production) | `docker-compose` |
| `allow_redirects=False` khi fetch URL | `tools.py` |

---

## 10. Business rules & edge cases

1. **Model fallback:** Gemini lỗi bất kỳ → tự động retry với Ollama. Không throw exception ra client.
2. **Ollama model selection:** Tìm `DEFAULT_MODEL` exact → `DEFAULT_MODEL:latest` → fuzzy match → first available → fallback về `DEFAULT_MODEL` (có thể fail gracefully).
3. **Seeding:** Tất cả GET endpoints kiểm tra DB trống và seed dữ liệu mặc định nếu cần.
4. **ID ownership:** Client tự tạo UUID cho projects, conversations, agents. Backend không validate format, chỉ dùng làm string key.
5. **Conversation sync:** Mỗi lần gửi tin nhắn, client POST toàn bộ conversation (replace messages). Backend không merge — client là source of truth.
6. **localStorage migration:** Chỉ chạy một lần khi phát hiện có data trong localStorage mà DB gần trống. Sau migration xóa localStorage keys.
7. **File upload chỉ base64:** Client encode `FileReader.readAsDataURL()` và strip `data:...;base64,` prefix trước khi gửi.
8. **Empty input + file:** Nếu user chỉ gửi file không có text, content gửi AI là `"Hãy phân tích tài liệu đính kèm này."`. Display message vẫn kèm tên file.
9. **Sidebar state persist:** Mọi trạng thái UI của sidebar (collapsed, accordion mở/đóng) được lưu localStorage và restore khi F5.
10. **Background scraping:** `ThreadPoolExecutor(max_workers=2)` để không OOM trên máy yếu. `sleep(2)` giữa mỗi source để không bị DuckDuckGo ban IP.

---

## 11. `config.yaml` format

```yaml
model: "llama3"
temperature: 0.7
```

Chỉ `model` được dùng trong code (`DEFAULT_MODEL`). `temperature` hiện không được đọc nhưng cần giữ lại cho tương thích.

---

## 12. System prompt mặc định

File: `prompts/system_prompts/default_system.txt`

```
You are a helpful AI assistant. Answer the user strictly but concisely. If they want to practice prompt engineering, act as the requested persona.
```

Custom agents override system prompt này hoàn toàn.

---

## 13. Makefile commands

| Lệnh | Mô tả |
|---|---|
| `make dev` | Docker Compose môi trường dev (hot-reload) |
| `make dev-down` | Dừng dev containers |
| `make dev-local` | Chạy local không Docker (SQLite + Vite dev server) |
| `make test` | Chạy pytest trong Docker với PostgreSQL tmpfs |
| `make test-local` | Chạy pytest trực tiếp (cần PostgreSQL test đang chạy) |
| `make staging` | Deploy staging detached |
| `make staging-down` | Dừng staging |
| `make staging-logs` | Xem logs staging |
| `make prod` | Deploy production (yêu cầu `.env` đầy đủ) |
| `make prod-down` | Dừng production |
| `make prod-logs` | Xem logs production |
| `make lint-backend` | Syntax check tất cả `.py` files |
| `make status` | Xem trạng thái tất cả môi trường |
