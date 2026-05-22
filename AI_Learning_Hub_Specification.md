# AI Learning Hub - Tài liệu Đặc tả Kiến trúc & Thiết kế Kỹ thuật (Technical Specification)

Tài liệu này cung cấp toàn bộ sơ đồ cấu trúc thư mục, lược đồ cơ sở dữ liệu quan hệ, thiết kế API RESTful, cơ chế tương tác AI (Google Gemini & Local Ollama), hệ thống Scraper thu thập tự động và giao diện UI/UX (Glassmorphism & Collapsible Workspace) của ứng dụng **AI Learning Hub**. 

---

## 1. Tổng quan Kiến trúc Hệ thống (Architecture Overview)

Ứng dụng được thiết kế theo mô hình **Client-Server đơn giản**, đóng gói hoàn toàn trong các container Docker:
*   **Frontend**: Ứng dụng Single Page App (SPA) phát triển bằng React 19 + Vite, biên dịch thành dạng static và phân phối bởi máy chủ Web **Nginx** hoạt động như một Reverse Proxy điều hướng cổng `/api/*` về phía backend.
*   **Backend**: Dịch vụ Web API hiệu năng cao bằng **FastAPI (Python 3.11)** chạy trên uvicorn server.
*   **Database**: Hệ quản trị cơ sở dữ liệu quan hệ **PostgreSQL 15** lưu trữ bền vững (persistent). Có tích hợp SQLite dự phòng cục bộ khi chạy môi trường dev độc lập.
*   **AI Engines**: Kết nối đám mây qua **Google Gemini 2.5 Flash API** và chạy cục bộ qua **Ollama API** (hỗ trợ tự động quét tất cả mô hình cục bộ trên hệ thống).

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           DOCKER COMPOSER SERVICES                      │
│                                                                         │
│  ┌───────────────────┐    HTTP /api/*    ┌───────────────────────────┐  │
│  │   aihub_frontend  ├──────────────────►│       aihub_backend       │  │
│  │  (Nginx Proxy /   │◄──────────────────┤    (FastAPI + Scraper)    │  │
│  │   React 19 SPA)   │    JSON Res       └─────┬──────────────┬──────┘  │
│  └───────────────────┘                         │              │         │
│                                           SQL  │              │ HTTP    │
│                                                ▼              ▼         │
│                                      ┌───────────┐      ┌───────────┐   │
│                                      │ aihub_db  │      │   Ollama  │   │
│                                      │(Postgres) │      │ (Host/GPU)│   │
│                                      └───────────┘      └───────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Cấu trúc Thư mục Dự án (Project Directory Structure)

```
AILearning/
├── docker-compose.yml              # Cấu hình khởi chạy các container services
├── .env                            # Tệp cấu hình biến môi trường (API Key, Host, DB)
├── config.yaml                     # Cấu hình mô hình AI cục bộ mặc định
├── README.md
├── prompts/
│   └── system_prompts/
│       └── default_system.txt      # Prompt hệ thống mặc định của trợ lý AI
├── src/
│   ├── backend/
│   │   ├── Dockerfile              # Dockerfile đa giai đoạn của backend Python
│   │   ├── requirements.txt        # Các thư viện Python phụ thuộc
│   │   ├── main.py                 # FastAPI Web Server, Schemas & API CRUD Endpoints
│   │   ├── database.py             # Cấu hình SQLAlchemy Connection & Database Models
│   │   ├── agent.py                # Xử lý tương tác LLMs (Gemini/Ollama) & Background Scraper
│   │   ├── tools.py                # Công cụ phụ trợ: DuckDuckGo Search, Web Scraper
│   │   └── sources.py              # Danh sách 50+ nguồn tin tức AI chất lượng cao
│   └── frontend/
│       ├── Dockerfile              # Dockerfile build React static & cấu hình Nginx
│       ├── nginx.conf              # Định tuyến Nginx, Proxy ngược API
│       ├── package.json            # Thư viện Frontend (React 19, Lucide, Axios, Marked)
│       ├── vite.config.js
│       ├── src/
│       │   ├── App.jsx             # Entry Point React: Quản lý Tabs, Sync Dữ liệu cũ
│       │   ├── index.css           # Căn bản thiết kế CSS, biến màu, Glassmorphism, Responsive
│       │   └── components/
│       │       ├── NewsFeed.jsx    # Giao diện hiển thị Tin tức AI tự động thu thập
│       │       ├── LearningHub.jsx # Giao diện xem Lộ trình học tập & mẹo thực hành
│       │       └── PracticeArea.jsx# Giao diện Không gian thực hành (Projects, Chats, Custom Agents)
└── tests/                          # Tệp kịch bản kiểm thử API & Hiệu năng LLMs
```

---

## 3. Lược đồ Cơ sở Dữ liệu (Database Schema)

Được định nghĩa trong `src/backend/database.py` sử dụng SQLAlchemy ORM.

### Bảng `news` (Lưu tin tức AI thu thập được)
*   `id`: `Integer` (Khóa chính, tự động tăng)
*   `title`: `String(255)` (Tiêu đề tin tức, có đánh index)
*   `summary`: `Text` (Tóm tắt chất lượng cao do AI tạo dưới 200 từ)
*   `url`: `String` (Địa chỉ liên kết gốc bài viết, duy nhất)
*   `rating`: `Integer` (Đánh giá mức độ giá trị học tập từ 1 - 10)
*   `published_at`: `DateTime` (Mặc định thời gian hiện tại)

### Bảng `learning_modules` (Lưu cẩm nang/mẹo thực hành trích xuất từ tài liệu)
*   `id`: `Integer` (Khóa chính, tự động tăng)
*   `title`: `String(255)` (Tiêu đề bài học, có đánh index)
*   `content`: `Text` (Nội dung hướng dẫn định dạng Markdown)
*   `category`: `String` (Phân loại, ví dụ: "Prompt Engineering", "RAG")
*   `created_at`: `DateTime` (Thời điểm tạo)

### Bảng `projects` (Phân chia các không gian làm việc của người dùng)
*   `id`: `String` (Khóa chính, UUID/Timestamp dạng `proj-*`)
*   `name`: `String` (Tên dự án, có đánh index)
*   `created_at`: `DateTime` (Thời điểm tạo)

### Bảng `agents` (Lưu thông tin Trợ lý AI đặc thù - Gems)
*   `id`: `String` (Khóa chính, UUID/Timestamp dạng `agent-*`)
*   `name`: `String` (Tên Agent, ví dụ: "Chuyên gia Python 🐍")
*   `system_prompt`: `Text` (Chỉ dẫn hệ thống quy định hành vi & kiến thức trợ lý)
*   `model_id`: `String` (Mô hình AI cơ sở liên kết, ví dụ: `gemini` hoặc `ollama/llama3`)
*   `color`: `String` (Từ khóa màu sắc diện mạo, ví dụ: `blue`, `purple`, `rose`)
*   `icon`: `String` (Tên biểu tượng Lucide hiển thị, ví dụ: `Brain`, `Bot`, `Code`)
*   `created_at`: `DateTime` (Thời điểm tạo)

### Bảng `conversations` (Lịch sử phiên chat)
*   `id`: `String` (Khóa chính, UUID/Timestamp dạng `chat-*`)
*   `project_id`: `String` (Khóa ngoại liên kết bảng `projects`)
*   `name`: `String` (Tên phiên chat)
*   `agent_id`: `String` (Khóa ngoại tùy chọn liên kết bảng `agents`, cho phép bật/tắt Agent)
*   `created_at`: `DateTime` (Thời điểm tạo)

### Bảng `messages` (Chi tiết tin nhắn trong hội thoại)
*   `id`: `Integer` (Khóa chính, tự động tăng)
*   `conversation_id`: `String` (Khóa ngoại liên kết bảng `conversations`)
*   `role`: `String` (Quy định vai trò: `"user"` hoặc `"ai"`)
*   `content`: `Text` (Nội dung hội thoại thô định dạng Markdown)
*   `model_name`: `String` (Lưu vết tên mô hình AI trả lời tại thời điểm đó)
*   `created_at`: `DateTime` (Thời điểm gửi)

> [!NOTE]
> **Hỗ trợ Di cư Cơ sở dữ liệu tự động (SQLAlchemy 2.0)**:
> Hệ thống tích hợp sẵn đoạn mã DDL tự động thực thi khi khởi chạy ứng dụng để cập nhật cấu trúc database nếu người dùng nâng cấp từ phiên bản cũ:
> ```python
> from sqlalchemy import text
> Base.metadata.create_all(bind=engine)
> try:
>     with engine.begin() as conn:
>         conn.execute(text("ALTER TABLE conversations ADD COLUMN agent_id VARCHAR"))
> except Exception:
>     pass # Cột đã tồn tại
> ```

---

## 4. API Endpoints Chi tiết (Backend RESTful API)

Tất cả các REST endpoints được định nghĩa trong `src/backend/main.py`.

### A. Quản lý Tin tức & Học tập
*   `GET /api/news?skip=0&limit=20`: Trả về danh sách tin tức sắp xếp theo điểm đánh giá `rating` từ cao xuống thấp và ngày xuất bản.
*   `GET /api/learn?skip=0&limit=20`: Trả về danh sách tài liệu hướng dẫn học tập AI.
*   `POST /api/agent/run`: Kích hoạt chạy Scraper ẩn tìm kiếm, tải bài viết, phân tích bằng AI và nạp vào DB trên background threads.

### B. Tương tác AI & Cấu hình Mô hình
*   `GET /api/models`:
    *   *Mô tả*: Trả về danh sách tất cả động cơ AI khả dụng.
    *   *Nội dung*: Luôn đính kèm Google Gemini 2.5 Flash làm Cloud model chính, kết hợp quét API Ollama cục bộ (`http://localhost:11434/api/tags`) để tìm kiếm các model đã tải về máy (ví dụ: `llama3`, `mistral`, `qwen2.5`) và đưa vào bộ chọn. Nếu Ollama chưa có model, trả về tùy chọn hướng dẫn tải `llama3`.
*   `POST /api/practice`:
    *   *Request Body*:
        ```json
        {
          "prompt": "nội dung tin nhắn người dùng",
          "provider": "gemini | ollama",
          "model_name": "tên model cục bộ nếu dùng ollama (tùy chọn)",
          "system_prompt": "chỉ dẫn hệ thống ghi đè nếu dùng custom agent (tùy chọn)"
        }
        ```
    *   *Response*: `{"response": "nội dung trả lời từ AI"}`

### C. Quản lý Dự án & Lịch sử Hội thoại (CRUD)
*   `GET /api/projects`: Trả về danh sách dự án. Tự động seed một dự án mặc định nếu trống.
*   `POST /api/projects`: Tạo mới hoặc đổi tên dự án hiện tại.
*   `DELETE /api/projects/{id}`: Xóa dự án, đồng thời tự động dọn sạch tất cả hội thoại và tin nhắn thuộc dự án đó.
*   `GET /api/conversations`: Trả về danh sách hội thoại kèm theo toàn bộ mảng tin nhắn con sắp xếp theo thứ tự thời gian. Tự động nạp hội thoại ban đầu nếu trống.
*   `POST /api/conversations`: Đồng bộ hóa trạng thái hội thoại và toàn bộ tin nhắn bên trong.
*   `DELETE /api/conversations/{id}`: Xóa hội thoại và các tin nhắn liên quan.

### D. Quản lý Custom AI Agents
*   `GET /api/agents`: Trả về danh sách Custom Agents. Tự động tạo mặc định "Chuyên gia Prompt 💡" (màu xanh da trời, biểu tượng Sparkles) để hướng dẫn người dùng.
*   `POST /api/agents`: Tạo mới hoặc cập nhật thông tin Custom Agent (gồm tên, chỉ dẫn hệ thống, model cơ sở, màu gradient và icon).
*   `DELETE /api/agents/{id}`: Xóa Agent và tự động ngắt liên kết (`agent_id = null`) trong các cuộc hội thoại đang liên kết với nó.

---

## 5. Logic Xử lý Trò chuyện AI & Scraper

Được triển khai trong `src/backend/agent.py` và `src/backend/tools.py`.

### A. Tích hợp Mô hình AI Linh hoạt (`practice_chat`)
Hàm xử lý phân tuyến yêu cầu dựa trên nhà cung cấp (`provider`):
1.  **Google Gemini**: Sử dụng SDK `google-generativeai`. Sử dụng model `gemini-2.5-flash`. Truyền tham số `system_instruction` để định hướng tư duy trực tiếp cho trợ lý.
2.  **Ollama**: Sử dụng thư viện `ollama`. Gửi yêu cầu qua client kết nối tới `OLLAMA_HOST`. Đóng gói tin nhắn dạng danh sách:
    ```python
    messages = [
        {'role': 'system', 'content': active_sys_prompt},
        {'role': 'user', 'content': prompt}
    ]
    ```
    Nếu dịch vụ Ollama cục bộ lỗi, tự động trả về cảnh báo kết nối kèm hướng dẫn chi tiết để người dùng xử lý.

### B. Bộ Thu thập Tin tức Tự động (Orchestrated Background Scraper)
Khi kích hoạt `/api/agent/run`, backend khởi động tiến trình bất đồng bộ:
1.  **Thu thập**: Lần lượt duyệt qua danh sách hơn 50 nguồn báo chí AI hàng đầu từ `sources.py`.
2.  **Tìm kiếm & Trích xuất**: Dùng DuckDuckGo API tìm kiếm các tiêu đề bài viết mới nhất. Sử dụng thư viện `requests` cào văn bản thô từ URL bài viết, tự động lọc mã HTML.
3.  **Tóm tắt & Đánh giá**: Gửi nội dung bài viết thô tới Gemini (hoặc Ollama dự phòng) với Prompt yêu cầu tóm tắt ngắn gọn dưới 200 từ và chấm điểm giá trị từ 1 đến 10 dựa trên tiêu chí **Ý nghĩa giáo dục**, **Tính thực hành lập trình**, và **Độ rõ ràng**.
4.  **Lưu trữ**: Phân tích kết quả JSON trả về từ AI và lưu trực tiếp vào bảng `news` hoặc `learning_modules`. Có cơ chế kiểm tra trùng lặp URL để tránh ghi đè dữ liệu cũ.

---

## 6. Thiết kế Frontend & Trải nghiệm Người dùng (UI/UX)

### A. Giao diện Tổng thể & Ngôn ngữ Màu sắc
Ứng dụng tuân thủ nghiêm ngặt phong cách **Glassmorphism hiện đại** và bố cục cân đối cao cấp:
*   **Bảng màu nền**: Sử dụng dải màu nhẹ nhàng, phối trộn giữa các token HSL. Viền phân cách mờ nhạt (`rgba(255,255,255,0.4)`), đổ bóng mềm sâu (`box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08)`).
*   **Typography**: Sử dụng font chữ tiêu đề sang trọng **Merriweather** có chân mang đậm hơi hướng tạp chí công nghệ cao cấp, kết hợp font nội dung **Inter** hoặc **system-ui** không chân dễ đọc.
*   **Màu sắc diện mạo AI Agent (Avatar Presets)**:
    *   `blue`: `linear-gradient(135deg, #3b82f6, #1d4ed8)`
    *   `purple`: `linear-gradient(135deg, #a855f7, #6d28d9)`
    *   `orange`: `linear-gradient(135deg, #f97316, #c2410c)`
    *   `emerald`: `linear-gradient(135deg, #10b981, #047857)`
    *   `rose`: `linear-gradient(135deg, #f43f5e, #be123c)`
    *   `indigo`: `linear-gradient(135deg, #6366f1, #4338ca)`

### B. Sidebar Thu gọn/Mở rộng Linh hoạt (Collapsible Navigation)
Sidebar bên trái chứa danh mục Quản lý Dự án, danh sách AI Agents, và danh sách Hội thoại.
*   **Cơ chế Toggle**: 
    *   Khi mở: Sidebar rộng `260px`. Người dùng nhấn biểu tượng `ChevronLeft` trên đầu Sidebar để thu gọn.
    *   Khi đóng: Sidebar chuyển `width: 0 !important; padding: 0 !important; border-right: none;`. Khung hiển thị chat tự động mở rộng bao phủ toàn bộ diện tích thẻ cha (`1000px`). Người dùng có thể khôi phục Sidebar bất cứ lúc nào bằng nút `Menu` nổi bên cạnh tiêu đề chat ở header khu vực trung tâm.
    *   Mã CSS chuyển động mượt mà:
        ```css
        .workspace-sidebar {
          width: 260px;
          transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
          overflow: hidden;
        }
        .workspace-sidebar.collapsed {
          width: 0 !important;
          padding: 0 !important;
          border-right: none !important;
          margin: 0 !important;
        }
        ```

### C. Cơ chế Hiển thị Bong bóng Chat & Markdown Parser
*   **Bộ phân tích Markdown**: Giao diện sử dụng thư viện `marked` tích hợp trong hàm React để biên dịch tất cả câu trả lời dạng văn bản thô chứa cú pháp Markdown (bảng so sánh biểu đồ, in đậm, khối mã nguồn `pre code`, danh sách chỉ mục) sang cấu trúc HTML sống động thông qua phương thức `dangerouslySetInnerHTML`.
*   **Huy hiệu Mô hình AI (Model Badges)**: Mỗi bong bóng thoại của AI đi kèm với một huy hiệu nhỏ có màu sắc tương ứng: màu xanh dương nhạt cho Cloud model (`gemini`), màu tím pastel cho local model (`ollama/*`), và màu xám nhẹ cho thông báo hệ thống (`system`).
*   **Giữ vết Mô hình Lịch sử**: Khi người dùng chuyển đổi mô hình AI đang chat ở thanh chọn bên dưới, các tin nhắn cũ đã lưu trong PostgreSQL vẫn hiển thị đúng huy hiệu của mô hình đã sinh ra câu trả lời đó tại thời điểm trong quá khứ nhờ thuộc tính `modelName` được lưu vĩnh viễn trên từng dòng tin nhắn.

---

## 7. Quy trình Triển khai nhanh ứng dụng (Setup & Running Guide)

Bất kỳ AI Agent nào khi có tệp đặc tả này có thể khởi tạo dự án nhanh bằng các bước sau:

### Bước 1: Chuẩn bị tệp `.env` môi trường
Tạo tệp `.env` ở thư mục gốc chứa thông tin kết nối và API Key:
```env
GEMINI_API_KEY=AIzaSy...your_gemini_key...
MODEL_PROVIDER=gemini
OLLAMA_HOST=http://host.docker.internal:11434
DATABASE_URL=postgresql://user:password@db:5432/aihub
```

### Bước 2: Chuẩn bị Docker Compose (`docker-compose.yml`)
```yaml
version: '3.8'
services:
  db:
    image: postgres:15-alpine
    container_name: aihub_db
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: aihub
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d aihub"]
      interval: 5s
      timeout: 5s
      retries: 5

  backend:
    build: ./src/backend
    container_name: aihub_backend
    env_file:
      - .env
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/aihub
      - CONFIG_PATH=/app/config.yaml
      - PROMPT_PATH=/app/prompts/system_prompts/default_system.txt
    volumes:
      - ./config.yaml:/app/config.yaml
      - ./prompts:/app/prompts
    depends_on:
      db:
        condition: service_healthy
    extra_hosts:
      - "host.docker.internal:host-gateway"
    ports:
      - "8000:8000"
    restart: unless-stopped

  frontend:
    build: ./src/frontend
    container_name: aihub_frontend
    ports:
      - "7070:80"
    depends_on:
      - backend
    restart: unless-stopped

volumes:
  postgres_data:
```

### Bước 3: Khởi tạo & Cấu hình Nginx Proxy trên Frontend
Tạo tệp `/src/frontend/nginx.conf` để phân tuyến chính xác yêu cầu frontend và proxy ngược API về backend:
```nginx
server {
    listen 80;
    server_name localhost;

    location / {
        root /usr/share/nginx/html;
        index index.html index.htm;
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://backend:8000/api;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Bước 4: Chạy lệnh Docker khởi dựng toàn diện
Khởi động toàn bộ cụm dịch vụ lên:
```bash
docker compose down && docker compose up -d --build
```
Ứng dụng sẽ tự động khởi động:
*   Mở trình duyệt truy cập: `http://localhost:7070` để bắt đầu trải nghiệm giao diện người dùng.
*   Cơ sở dữ liệu tự động cấu hình bảng, tự động di cư cột mới và tự nạp dữ liệu Seed ban đầu cho cả Projects, Conversations và Custom AI Agents.
*   Quá trình quét mô hình local trên Ollama được thực hiện tự động qua API Gateway bất cứ lúc nào người dùng kích hoạt bộ chọn động.
