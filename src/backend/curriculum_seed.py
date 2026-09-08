# Static curriculum content for the "Bài học" tab, seeded into the
# curriculum_lessons table on first request so it survives independent of
# the AI scraping pipeline (Gemini/Ollama availability).

CURRICULUM_SEED = [
    {
        "id": "basic-1",
        "level": "basic",
        "title": "Trí tuệ nhân tạo (AI) là gì?",
        "summary": "Định nghĩa AI và các nhánh chính: Machine Learning, Deep Learning, Generative AI.",
        "content": """## AI là gì?

**Trí tuệ nhân tạo (Artificial Intelligence - AI)** là lĩnh vực khoa học máy tính giúp máy tính thực hiện các tác vụ vốn cần trí thông minh của con người: nhận dạng hình ảnh, hiểu ngôn ngữ, ra quyết định, dịch thuật...

## Các nhánh chính

- **AI (Trí tuệ nhân tạo)**: khái niệm bao trùm — bất kỳ hệ thống nào mô phỏng hành vi thông minh.
- **Machine Learning (Học máy)**: một nhánh của AI, máy tính "học" từ dữ liệu thay vì được lập trình luật cứng.
- **Deep Learning (Học sâu)**: một nhánh của Machine Learning, dùng mạng nơ-ron nhiều lớp (neural network) để học các mẫu phức tạp.
- **Generative AI (AI tạo sinh)**: các mô hình học sâu có khả năng *tạo ra* nội dung mới — văn bản, hình ảnh, âm thanh — thay vì chỉ phân loại/dự đoán. ChatGPT, Gemini, Midjourney đều thuộc nhóm này.

## Vì sao AI bùng nổ gần đây?

Ba yếu tố hội tụ: (1) dữ liệu khổng lồ từ Internet, (2) sức mạnh tính toán GPU giá rẻ hơn, (3) kiến trúc **Transformer** (2017) — nền tảng cho các LLM hiện đại như GPT, Gemini, Llama.

> 💡 **Ghi nhớ**: AI ⊃ Machine Learning ⊃ Deep Learning. LLM là một ứng dụng của Deep Learning, thuộc nhóm Generative AI.""",
    },
    {
        "id": "basic-2",
        "level": "basic",
        "title": "Machine Learning vs Deep Learning: khác nhau ở đâu?",
        "summary": "So sánh cách máy tính học từ dữ liệu ở hai cấp độ truyền thống và hiện đại.",
        "content": """## Machine Learning truyền thống

Con người **chọn đặc trưng (feature)** cho dữ liệu rồi đưa vào thuật toán (Linear Regression, Decision Tree, SVM...) để mô hình học mối quan hệ giữa đặc trưng và kết quả.

Ví dụ: dự đoán giá nhà dựa trên diện tích, số phòng, vị trí — con người tự tay chọn ra các cột dữ liệu này.

## Deep Learning

Deep Learning dùng **mạng nơ-ron nhiều lớp**, tự động học đặc trưng trực tiếp từ dữ liệu thô (pixel ảnh, ký tự văn bản) mà không cần con người chọn tay.

| | Machine Learning | Deep Learning |
|---|---|---|
| Dữ liệu cần | Ít hơn | Rất nhiều |
| Đặc trưng | Con người chọn | Mô hình tự học |
| Phần cứng | CPU đủ dùng | Cần GPU/TPU |
| Ví dụ | Dự đoán churn khách hàng | Nhận diện khuôn mặt, LLM |

## Vì sao LLM cần Deep Learning?

Ngôn ngữ tự nhiên quá phức tạp và nhiều ngữ cảnh để liệt kê thủ công thành "đặc trưng". Deep Learning — cụ thể là kiến trúc Transformer — cho phép mô hình tự học cấu trúc ngữ pháp, ngữ nghĩa, và cả kiến thức thế giới từ hàng tỷ câu văn.""",
    },
    {
        "id": "basic-3",
        "level": "basic",
        "title": "LLM (Large Language Model) là gì và hoạt động ra sao?",
        "summary": 'Cách một mô hình ngôn ngữ lớn dự đoán từ tiếp theo để "viết" ra câu trả lời.',
        "content": """## Định nghĩa

**LLM (Large Language Model)** là mô hình Deep Learning được huấn luyện trên khối lượng văn bản khổng lồ (sách, web, code...) để học cách **dự đoán từ/token tiếp theo** trong một chuỗi văn bản.

## Cơ chế cốt lõi: dự đoán từ tiếp theo

Về bản chất, khi bạn hỏi "Thủ đô của Việt Nam là", LLM tính xác suất cho hàng chục nghìn từ có thể đứng tiếp theo, và chọn ra từ có xác suất cao nhất (ví dụ "Hà Nội"). Nó lặp lại quá trình này **từng token một** để tạo ra cả câu trả lời — không "suy nghĩ" theo cách con người, mà tính toán xác suất dựa trên những gì đã học.

## Kiến trúc Transformer

LLM hiện đại (GPT, Gemini, Llama, Claude) đều dựa trên kiến trúc **Transformer** (Google, 2017), với cơ chế **self-attention** cho phép mô hình "chú ý" đến các từ liên quan trong toàn bộ đoạn văn, dù chúng ở xa nhau trong câu — đây là lý do LLM hiểu ngữ cảnh tốt hơn hẳn các mô hình cũ.

## Hai giai đoạn: Training và Inference

- **Training (huấn luyện)**: quá trình tốn kém, mất hàng tuần/tháng với hàng nghìn GPU, để mô hình học từ dữ liệu.
- **Inference (suy luận)**: quá trình bạn dùng hàng ngày — nhập prompt, mô hình trả lời — dùng lại "kiến thức" đã học từ training, không học thêm gì mới trong lúc trò chuyện (trừ khi có cơ chế RAG/fine-tuning riêng).

## Giới hạn cần biết

- **Hallucination (ảo giác)**: LLM có thể "bịa" thông tin nghe rất tự tin nhưng sai, vì nó dự đoán từ có khả năng cao chứ không tra cứu sự thật.
- **Kiến thức có hạn mốc thời gian** (knowledge cutoff): mô hình không biết các sự kiện sau ngày dữ liệu huấn luyện kết thúc, trừ khi được kết nối Internet/RAG.""",
    },
    {
        "id": "basic-4",
        "level": "basic",
        "title": "Token và Context Window là gì?",
        "summary": '"Đơn vị đo lường" mà LLM dùng để đọc và viết văn bản, và giới hạn bộ nhớ ngắn hạn.',
        "content": """## Token là gì?

LLM không đọc theo "chữ cái" hay "từ" như con người, mà theo **token** — một mảnh văn bản có thể là một từ, một phần của từ, hoặc một dấu câu. Ví dụ tiếng Anh "unbelievable" có thể tách thành 3 token: `un`, `believ`, `able`. Tiếng Việt có dấu thường tốn nhiều token hơn tiếng Anh cho cùng một ý.

Quy tắc ước lượng nhanh: **1 token ≈ 4 ký tự tiếng Anh**, hoặc khoảng 0.75 từ.

## Context Window (cửa sổ ngữ cảnh)

Context Window là **số lượng token tối đa** mà mô hình có thể "nhìn thấy" cùng lúc trong một lượt hỏi-đáp — bao gồm cả prompt của bạn, lịch sử hội thoại trước đó, và câu trả lời mô hình sắp tạo ra.

- Model cũ: 4,000 token (~3,000 từ)
- Model hiện đại (Gemini 1.5/2.5, GPT-4o): 128,000 – 1,000,000+ token (~hàng trăm trang sách)

## Vì sao điều này quan trọng khi dùng AI?

1. **Hội thoại dài sẽ "quên" nội dung đầu** khi vượt quá context window — mô hình buộc phải cắt bớt phần đầu.
2. **Chi phí API thường tính theo token** (cả input lẫn output) — prompt càng dài, càng tốn kém.
3. Khi dán tài liệu dài để hỏi AI, cần kiểm tra model có context window đủ lớn để "đọc hết" tài liệu đó không.""",
    },
    {
        "id": "prompting-1",
        "level": "prompting",
        "title": "Prompt là gì? Cấu trúc một Prompt hiệu quả",
        "summary": "Bốn thành phần giúp một prompt rõ ràng, đúng ý, và cho kết quả nhất quán.",
        "content": """## Prompt là gì?

**Prompt** là đoạn văn bản bạn đưa cho AI để yêu cầu nó thực hiện một việc gì đó. Chất lượng prompt quyết định phần lớn chất lượng câu trả lời — đây là lý do "Prompt Engineering" trở thành một kỹ năng thực sự.

## 4 thành phần của một prompt tốt

1. **Vai trò / bối cảnh (Role/Context)**: AI nên đóng vai gì? Ví dụ: "Bạn là một biên tập viên kỹ thuật có 10 năm kinh nghiệm."
2. **Nhiệm vụ (Task)**: Yêu cầu cụ thể, dùng động từ rõ ràng — "tóm tắt", "liệt kê", "viết lại", "so sánh"... tránh mơ hồ như "nói gì đó về...".
3. **Ràng buộc / định dạng (Constraints/Format)**: độ dài, giọng văn, ngôn ngữ, định dạng đầu ra (bảng, bullet, JSON...).
4. **Ví dụ (nếu cần)**: cho AI 1-2 ví dụ mẫu để nó bắt đúng "tông" bạn muốn (xem bài Few-shot Prompting).

## Ví dụ so sánh

**Prompt kém:**
```
Viết về marketing.
```

**Prompt tốt:**
```
Bạn là chuyên gia marketing cho startup công nghệ.
Hãy viết 3 tiêu đề email quảng cáo (mỗi tiêu đề dưới 60 ký tự)
cho sản phẩm ứng dụng học AI dành cho người mới bắt đầu.
Giọng văn: thân thiện, tạo cảm giác cấp bách nhẹ nhàng.
```

## Nguyên tắc vàng

- **Càng cụ thể càng tốt** — AI không đọc được suy nghĩ, chỉ dựa vào chữ bạn viết.
- **Nói AI nên làm gì, thay vì không nên làm gì** ("Trả lời bằng 3 gạch đầu dòng" tốt hơn "Đừng trả lời dài dòng").
- **Lặp lại và tinh chỉnh**: prompt hiếm khi đúng ngay lần đầu — hãy đọc kết quả rồi bổ sung ràng buộc còn thiếu.""",
    },
    {
        "id": "prompting-2",
        "level": "prompting",
        "title": "Zero-shot vs Few-shot Prompting",
        "summary": "Khi nào nên hỏi thẳng, khi nào nên cho AI xem ví dụ mẫu trước.",
        "content": """## Zero-shot Prompting

Là cách hỏi **không kèm ví dụ** — bạn tin tưởng mô hình đã đủ kiến thức nền để hiểu và thực hiện yêu cầu ngay.

```
Phân loại cảm xúc của câu sau: "Tích cực", "Tiêu cực" hoặc "Trung lập".
Câu: "Sản phẩm giao chậm nhưng chất lượng khá ổn."
```

Phù hợp cho các tác vụ phổ biến, đơn giản mà mô hình đã được huấn luyện rộng rãi.

## Few-shot Prompting

Là cách **đưa vài ví dụ mẫu (input → output)** trước khi đặt câu hỏi thật, giúp AI "bắt" đúng định dạng, văn phong, hoặc logic phân loại bạn muốn — đặc biệt hữu ích với các tác vụ đặc thù, không chuẩn.

```
Phân loại mức độ ưu tiên hỗ trợ khách hàng:

Câu: "App bị crash không mở được." → Ưu tiên: Cao
Câu: "Muốn đổi màu giao diện." → Ưu tiên: Thấp
Câu: "Thanh toán bị trừ tiền 2 lần." → Ưu tiên: Cao

Câu: "Không tìm thấy nút đăng xuất." → Ưu tiên:
```

## Khi nào dùng cái nào?

| Tình huống | Nên dùng |
|---|---|
| Tác vụ phổ thông, rõ ràng | Zero-shot |
| Cần định dạng đầu ra chính xác, nhất quán | Few-shot |
| Logic phân loại đặc thù của riêng bạn/công ty | Few-shot |
| Muốn tiết kiệm token (few-shot tốn thêm token cho ví dụ) | Zero-shot |

> 💡 2-5 ví dụ chất lượng thường hiệu quả hơn nhiều ví dụ nhưng sơ sài.""",
    },
    {
        "id": "prompting-3",
        "level": "prompting",
        "title": 'Chain-of-Thought: dạy AI "suy nghĩ từng bước"',
        "summary": "Kỹ thuật giúp AI giải quyết bài toán logic/suy luận chính xác hơn.",
        "content": """## Vấn đề

LLM sinh câu trả lời theo kiểu "trả lời ngay", nên với các bài toán cần **nhiều bước suy luận** (tính toán, logic, lập kế hoạch), nó dễ nhảy cóc và ra kết quả sai — dù từng bước riêng lẻ nó có thể làm đúng.

## Giải pháp: Chain-of-Thought (CoT)

Yêu cầu AI **trình bày từng bước suy luận** trước khi đưa ra kết luận cuối cùng, thay vì trả lời tắt. Chỉ cần thêm cụm "Hãy suy luận từng bước" (*think step by step*) thường đã cải thiện đáng kể độ chính xác.

**Không có CoT:**
```
Một cửa hàng có 23 quả táo. Bán 8 quả sáng nay, nhập thêm 15 quả buổi trưa.
Chiều bán tiếp 12 quả. Hỏi cửa hàng còn bao nhiêu quả táo?
→ AI có thể trả lời ẩu, đôi khi tính sai.
```

**Có CoT:**
```
... (đề bài như trên)
Hãy giải từng bước một, ghi rõ phép tính ở mỗi bước, rồi mới kết luận.
```

Kết quả: AI liệt kê "23 - 8 = 15", "15 + 15 = 30", "30 - 12 = 18" → giảm mạnh khả năng tính nhầm vì mỗi bước đơn giản hơn cả bài toán.

## Biến thể nâng cao

- **Few-shot CoT**: kèm ví dụ mẫu có sẵn lời giải từng bước để AI bắt chước cách trình bày.
- **Self-consistency**: chạy CoT nhiều lần với cùng câu hỏi, lấy đáp án xuất hiện nhiều nhất — tăng độ tin cậy cho các quyết định quan trọng.

## Khi nào nên dùng?

Toán học, logic, debug code, lập kế hoạch nhiều bước, phân tích dữ liệu. Với câu hỏi đơn giản (tra cứu sự kiện, dịch thuật), CoT thường không cần thiết và làm câu trả lời dài dòng hơn.""",
    },
    {
        "id": "prompting-4",
        "level": "prompting",
        "title": 'Temperature, Top-p: điều khiển độ "sáng tạo" của AI',
        "summary": "Các tham số kỹ thuật quyết định câu trả lời của AI ổn định hay đa dạng.",
        "content": """## Nhắc lại: LLM chọn từ tiếp theo dựa trên xác suất

Với mỗi vị trí, mô hình tính ra một danh sách xác suất cho các token có thể đứng tiếp theo. **Temperature** và **Top-p** quyết định cách mô hình *chọn* từ danh sách xác suất đó.

## Temperature

Điều chỉnh mức độ "liều lĩnh" khi chọn từ, giá trị thường từ 0 đến 2:

- **Temperature thấp (0 – 0.3)**: gần như luôn chọn từ có xác suất cao nhất → câu trả lời **ổn định, nhất quán, ít sáng tạo**. Phù hợp: trả lời dữ kiện, code, phân loại dữ liệu, tóm tắt.
- **Temperature cao (0.7 – 1.2+)**: sẵn sàng chọn cả những từ xác suất thấp hơn → câu trả lời **đa dạng, sáng tạo hơn**, nhưng cũng dễ lạc đề/kém chính xác hơn. Phù hợp: viết sáng tạo, brainstorm, thơ văn.

## Top-p (Nucleus Sampling)

Thay vì xét toàn bộ từ vựng, Top-p chỉ giữ lại **tập từ nhỏ nhất có tổng xác suất ≥ p** rồi mới chọn ngẫu nhiên trong tập đó.

- **Top-p = 0.1**: chỉ xét nhóm từ "chắc chắn nhất" — rất an toàn, ít bất ngờ.
- **Top-p = 1.0**: xét toàn bộ từ vựng có thể — tăng sự đa dạng.

## Dùng chung thế nào?

Thông thường chỉ cần chỉnh **một trong hai** (giữ cái còn lại ở giá trị mặc định), tránh chỉnh cả hai cùng lúc vì hiệu ứng chồng chéo khó dự đoán.

| Tác vụ | Gợi ý Temperature |
|---|---|
| Viết code, trả lời tra cứu, tóm tắt | 0 – 0.3 |
| Chat trợ lý thông thường | 0.5 – 0.7 |
| Viết quảng cáo, sáng tác, brainstorm | 0.8 – 1.2 |""",
    },
    {
        "id": "advanced-1",
        "level": "advanced",
        "title": "RAG (Retrieval-Augmented Generation) là gì?",
        "summary": 'Cách "gắn" thêm kiến thức riêng/mới cho AI mà không cần huấn luyện lại mô hình.',
        "content": """## Vấn đề cần giải quyết

LLM chỉ biết những gì có trong dữ liệu huấn luyện, tính đến một mốc thời gian nhất định (*knowledge cutoff*), và **không biết** tài liệu nội bộ công ty bạn, email cá nhân, hay tin tức hôm nay.

## RAG hoạt động thế nào?

**RAG (Retrieval-Augmented Generation)** kết hợp một bước **tìm kiếm (Retrieval)** trước khi AI **sinh câu trả lời (Generation)**:

1. Người dùng đặt câu hỏi.
2. Hệ thống tìm kiếm các đoạn tài liệu liên quan nhất trong kho dữ liệu riêng (thường dùng **vector database** để tìm theo "ý nghĩa" chứ không chỉ từ khóa).
3. Các đoạn tài liệu tìm được được **chèn vào prompt** cùng câu hỏi gốc, gửi cho LLM.
4. LLM trả lời **dựa trên ngữ cảnh vừa được cung cấp**, thay vì chỉ dựa vào trí nhớ đã huấn luyện.

```
[Câu hỏi người dùng]
        ↓
[Tìm kiếm tài liệu liên quan] → [Top-k đoạn văn bản phù hợp]
        ↓
[Prompt = Tài liệu tìm được + Câu hỏi] → [LLM] → [Câu trả lời có trích dẫn nguồn]
```

## Vì sao RAG quan trọng?

- **Giảm hallucination**: AI trả lời dựa trên tài liệu thật, có thể trích dẫn nguồn.
- **Cập nhật kiến thức mới** mà không cần huấn luyện lại mô hình (chi phí huấn luyện rất cao).
- **Bảo mật dữ liệu riêng**: tài liệu nội bộ không cần đưa vào huấn luyện mô hình, chỉ dùng lúc truy vấn.

## Ứng dụng thực tế

Chatbot hỏi-đáp tài liệu nội bộ doanh nghiệp, trợ lý tra cứu pháp lý/y tế, tìm kiếm ngữ nghĩa trong kho email/wiki công ty — đây cũng chính xác là cơ chế mà tính năng "Cập nhật DL" của ứng dụng này áp dụng: thu thập tin tức mới rồi mới đưa cho AI tóm tắt.""",
    },
    {
        "id": "advanced-2",
        "level": "advanced",
        "title": 'AI Agents và Tool Use: khi AI biết "hành động"',
        "summary": "Từ chatbot chỉ biết trả lời chữ, đến AI có thể tự gọi công cụ để hoàn thành việc.",
        "content": """## Giới hạn của một LLM "thuần"

Một LLM cơ bản chỉ sinh ra **văn bản** — nó không tự tra cứu Google, không đọc được database, không gửi được email. Muốn AI thực sự "làm việc", cần kết nối nó với các **công cụ (tools)** bên ngoài.

## Tool Use / Function Calling

Cơ chế cho phép LLM **quyết định khi nào cần gọi một hàm/API cụ thể**, với tham số cụ thể, thay vì tự bịa câu trả lời. Ví dụ:

```
Người dùng: "Thời tiết Hà Nội hôm nay thế nào?"

LLM (không có tool): có thể bịa ra một câu trả lời không chính xác.

LLM (có tool "get_weather"):
  → Nhận ra cần dữ liệu thời tiết thời gian thực
  → Gọi: get_weather(city="Hà Nội")
  → Nhận kết quả JSON từ API thời tiết thật
  → Tổng hợp thành câu trả lời tự nhiên cho người dùng
```

## AI Agent là gì?

Một **Agent** là hệ thống dùng LLM làm "bộ não" trung tâm, có khả năng:

1. **Lập kế hoạch (Planning)**: chia một yêu cầu lớn thành các bước nhỏ.
2. **Dùng công cụ (Tool use)**: tìm kiếm web, chạy code, truy vấn database, gọi API...
3. **Quan sát kết quả và điều chỉnh (Reasoning loop)**: dựa trên kết quả bước trước để quyết định bước tiếp theo — lặp lại cho đến khi hoàn thành nhiệm vụ.

Đây chính là cơ chế đứng sau tính năng "Cập nhật DL" trong ứng dụng này: agent tự động quyết định tìm kiếm nguồn nào, tóm tắt ra sao, rồi lưu kết quả — thay vì chỉ trả lời một câu hỏi đơn lẻ.

## Rủi ro cần lưu ý

- Agent có thể **lặp vô hạn** hoặc chọn sai công cụ nếu prompt/thiết kế không rõ ràng.
- Cần **giới hạn quyền hạn** (ví dụ chỉ cho đọc dữ liệu, không cho xóa) để tránh hành động ngoài ý muốn.
- Luôn nên có bước **con người xác nhận** trước các hành động quan trọng, không thể hoàn tác (gửi email, thanh toán, xóa dữ liệu).""",
    },
    {
        "id": "advanced-3",
        "level": "advanced",
        "title": "Fine-tuning vs Prompting vs RAG: chọn giải pháp nào?",
        "summary": 'Ba cách "tùy biến" AI cho nhu cầu riêng — ưu, nhược điểm và khi nào nên dùng.',
        "content": """## Ba cách tùy biến một LLM có sẵn

| Phương pháp | Cách làm | Chi phí | Khi nào dùng |
|---|---|---|---|
| **Prompt Engineering** | Viết prompt tốt hơn (role, ví dụ, CoT...) | Rất thấp, tức thời | Luôn thử đầu tiên |
| **RAG** | Gắn thêm kho tài liệu để tra cứu lúc trả lời | Trung bình (cần vector DB) | Cần kiến thức mới/riêng, hay thay đổi |
| **Fine-tuning** | Huấn luyện tiếp mô hình trên dữ liệu riêng | Cao (dữ liệu, compute, thời gian) | Cần đổi *hành vi/văn phong* mô hình, khối lượng dùng rất lớn |

## Nguyên tắc chọn lựa

1. **Luôn thử Prompt Engineering trước** — rẻ nhất, nhanh nhất, nhiều vấn đề giải quyết được ngay mà không cần gì thêm.
2. Nếu vấn đề là **"AI không biết thông tin X"** (tài liệu nội bộ, tin tức mới, dữ liệu riêng công ty) → dùng **RAG**.
3. Nếu vấn đề là **"AI biết thông tin nhưng trả lời sai định dạng/văn phong/hành vi mong muốn một cách hệ thống"**, dù đã prompt rất kỹ → cân nhắc **Fine-tuning**.

## Ví dụ thực tế

- Muốn chatbot trả lời theo đúng giọng văn thương hiệu công ty → thử prompt (system prompt mô tả giọng văn) trước; nếu vẫn không nhất quán ở quy mô lớn → fine-tune.
- Muốn chatbot trả lời câu hỏi dựa trên 10,000 trang tài liệu nội bộ luôn cập nhật → RAG là lựa chọn phù hợp nhất, vì fine-tune sẽ phải làm lại mỗi khi tài liệu thay đổi.
- Muốn AI viết email chuyên nghiệp hơn → chỉ cần prompt tốt là đủ, không cần RAG hay fine-tune.

> 💡 Trong thực tế, nhiều hệ thống production kết hợp cả ba: prompt tốt + RAG để lấy kiến thức mới + đôi khi fine-tune cho các tác vụ chuyên biệt lặp lại nhiều.""",
    },
]
