# Static curriculum content for the "Bài học" tab, seeded into the
# curriculum_lessons table on first request so it survives independent of
# the AI scraping pipeline (Gemini/Ollama availability).
#
# Each lesson's content is Markdown with occasional raw inline <svg> diagram
# blocks (marked passes raw HTML blocks through untouched, rendered via
# LearningHub's dangerouslySetInnerHTML) to make concepts easier to grasp
# for someone brand new to AI.

CURRICULUM_SEED = [
    {
        "id": "basic-1",
        "level": "basic",
        "title": "Trí tuệ nhân tạo (AI) là gì?",
        "summary": "Định nghĩa AI và các nhánh chính: Machine Learning, Deep Learning, Generative AI.",
        "content": """## AI là gì?

**Trí tuệ nhân tạo (Artificial Intelligence - AI)** là lĩnh vực khoa học máy tính giúp máy tính thực hiện các tác vụ vốn cần trí thông minh của con người: nhận dạng hình ảnh, hiểu ngôn ngữ, ra quyết định, dịch thuật...

> 🌱 **Ví dụ đời thường**: Hãy tưởng tượng AI như một "học trò" cực kỳ chăm đọc sách. Nó đọc hàng tỷ trang sách, bài báo, đoạn hội thoại... rồi dựa vào những gì đã đọc để trả lời câu hỏi, viết văn, hay nhận ra một bức ảnh có con mèo hay không.

## Các nhánh chính (từ rộng đến hẹp)

AI giống như một tập hợp lớn, bên trong có các tập hợp con nhỏ hơn, chuyên biệt hơn:

<div class="curriculum-diagram">
<svg viewBox="0 0 480 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sơ đồ AI bao gồm Machine Learning, Deep Learning và Generative AI/LLM">
  <circle cx="240" cy="180" r="135" fill="#eff6ff" stroke="#93c5fd" stroke-width="2"/>
  <circle cx="240" cy="195" r="98" fill="#e0e7ff" stroke="#818cf8" stroke-width="2"/>
  <circle cx="240" cy="210" r="60" fill="#ede9fe" stroke="#a78bfa" stroke-width="2"/>
  <circle cx="240" cy="222" r="28" fill="#2563eb"/>
  <text x="240" y="58" text-anchor="middle" font-size="15" font-weight="700" fill="#1e3a8a">AI (Trí tuệ nhân tạo)</text>
  <text x="240" y="110" text-anchor="middle" font-size="14" font-weight="700" fill="#3730a3">Machine Learning</text>
  <text x="240" y="160" text-anchor="middle" font-size="13" font-weight="700" fill="#5b21b6">Deep Learning</text>
  <text x="240" y="226" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">LLM /</text>
  <text x="240" y="238" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">Gen AI</text>
</svg>
<span class="curriculum-diagram-caption">AI là vòng ngoài cùng, mỗi vòng bên trong là một nhánh chuyên biệt hơn của vòng bên ngoài nó.</span>
</div>

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

> 🌱 **Ví dụ đời thường**: Giống như dạy một đứa trẻ nhận biết trái cây bằng cách liệt kê sẵn đặc điểm — "tròn, đỏ, có cuống → có thể là táo". Bạn (con người) phải tự nghĩ ra những đặc điểm cần chú ý.

Ví dụ: dự đoán giá nhà dựa trên diện tích, số phòng, vị trí — con người tự tay chọn ra các cột dữ liệu này.

## Deep Learning

Deep Learning dùng **mạng nơ-ron nhiều lớp**, tự động học đặc trưng trực tiếp từ dữ liệu thô (pixel ảnh, ký tự văn bản) mà không cần con người chọn tay — giống như đứa trẻ tự nhìn hàng nghìn bức ảnh trái cây và tự rút ra quy luật, không ai dạy nó "tròn, đỏ" là gì cả.

<div class="curriculum-diagram">
<svg viewBox="0 0 620 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="So sánh quy trình Machine Learning truyền thống và Deep Learning">
  <defs>
    <marker id="arrow1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#6b7280"/>
    </marker>
  </defs>
  <text x="10" y="24" font-size="13" font-weight="700" fill="#111827">Machine Learning truyền thống</text>
  <rect x="10" y="38" width="110" height="46" rx="8" fill="#f3f4f6" stroke="#d1d5db"/>
  <text x="65" y="65" text-anchor="middle" font-size="11" fill="#374151">Dữ liệu thô</text>
  <line x1="120" y1="61" x2="150" y2="61" stroke="#6b7280" stroke-width="2" marker-end="url(#arrow1)"/>
  <rect x="152" y="38" width="140" height="46" rx="8" fill="#fef3c7" stroke="#f59e0b"/>
  <text x="222" y="58" text-anchor="middle" font-size="11" fill="#92400e">Người chọn</text>
  <text x="222" y="72" text-anchor="middle" font-size="11" fill="#92400e">đặc trưng (feature)</text>
  <line x1="292" y1="61" x2="322" y2="61" stroke="#6b7280" stroke-width="2" marker-end="url(#arrow1)"/>
  <rect x="324" y="38" width="130" height="46" rx="8" fill="#e0e7ff" stroke="#818cf8"/>
  <text x="389" y="65" text-anchor="middle" font-size="11" fill="#3730a3">Thuật toán ML</text>
  <line x1="454" y1="61" x2="484" y2="61" stroke="#6b7280" stroke-width="2" marker-end="url(#arrow1)"/>
  <rect x="486" y="38" width="120" height="46" rx="8" fill="#dcfce7" stroke="#22c55e"/>
  <text x="546" y="65" text-anchor="middle" font-size="11" fill="#166534">Kết quả</text>
  <text x="10" y="130" font-size="13" font-weight="700" fill="#111827">Deep Learning</text>
  <rect x="10" y="144" width="110" height="46" rx="8" fill="#f3f4f6" stroke="#d1d5db"/>
  <text x="65" y="171" text-anchor="middle" font-size="11" fill="#374151">Dữ liệu thô</text>
  <line x1="120" y1="167" x2="150" y2="167" stroke="#6b7280" stroke-width="2" marker-end="url(#arrow1)"/>
  <rect x="152" y="144" width="302" height="46" rx="8" fill="#ede9fe" stroke="#a78bfa"/>
  <text x="303" y="164" text-anchor="middle" font-size="11" fill="#5b21b6">Mạng nơ-ron nhiều lớp</text>
  <text x="303" y="178" text-anchor="middle" font-size="11" fill="#5b21b6">tự học đặc trưng</text>
  <line x1="454" y1="167" x2="484" y2="167" stroke="#6b7280" stroke-width="2" marker-end="url(#arrow1)"/>
  <rect x="486" y="144" width="120" height="46" rx="8" fill="#dcfce7" stroke="#22c55e"/>
  <text x="546" y="171" text-anchor="middle" font-size="11" fill="#166534">Kết quả</text>
</svg>
<span class="curriculum-diagram-caption">Khác biệt cốt lõi: ai là người "chọn đặc trưng" — con người, hay chính mô hình?</span>
</div>

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

> 🌱 **Ví dụ đời thường**: Giống trò chơi "đoán chữ tiếp theo" khi nhắn tin — điện thoại gợi ý từ kế tiếp dựa trên thói quen gõ của bạn. LLM làm y hệt vậy, nhưng ở quy mô khổng lồ và thông minh hơn rất nhiều, nhờ đọc gần như toàn bộ Internet.

## Cơ chế cốt lõi: dự đoán từ tiếp theo

Khi bạn hỏi "Thủ đô của Việt Nam là", LLM không "biết" theo cách tra từ điển — nó tính **xác suất** cho hàng chục nghìn từ có thể đứng tiếp theo, rồi chọn từ có xác suất cao nhất.

<div class="curriculum-diagram">
<svg viewBox="0 0 560 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sơ đồ LLM dự đoán từ tiếp theo dựa trên xác suất">
  <defs>
    <marker id="arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#2563eb"/>
    </marker>
  </defs>
  <rect x="10" y="90" width="150" height="50" rx="8" fill="#f3f4f6" stroke="#d1d5db"/>
  <text x="85" y="112" text-anchor="middle" font-size="11" fill="#374151">"Thủ đô của</text>
  <text x="85" y="127" text-anchor="middle" font-size="11" fill="#374151">Việt Nam là..."</text>
  <line x1="160" y1="115" x2="195" y2="115" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow2)"/>
  <rect x="197" y="90" width="90" height="50" rx="8" fill="#dbeafe" stroke="#2563eb"/>
  <text x="242" y="119" text-anchor="middle" font-size="12" font-weight="700" fill="#1e3a8a">LLM</text>
  <line x1="287" y1="115" x2="317" y2="115" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow2)"/>
  <text x="400" y="35" text-anchor="middle" font-size="11" fill="#6b7280">Xác suất từ tiếp theo</text>
  <rect x="325" y="150" width="26" height="60" fill="#2563eb"/>
  <text x="338" y="225" text-anchor="middle" font-size="10" fill="#374151">Hà Nội</text>
  <text x="338" y="145" text-anchor="middle" font-size="10" fill="#1e3a8a" font-weight="700">82%</text>
  <rect x="365" y="190" width="26" height="20" fill="#93c5fd"/>
  <text x="378" y="225" text-anchor="middle" font-size="10" fill="#374151">Sài Gòn</text>
  <text x="378" y="185" text-anchor="middle" font-size="10" fill="#374151">6%</text>
  <rect x="405" y="196" width="26" height="14" fill="#bfdbfe"/>
  <text x="418" y="225" text-anchor="middle" font-size="10" fill="#374151">Huế</text>
  <text x="418" y="191" text-anchor="middle" font-size="10" fill="#374151">3%</text>
  <rect x="445" y="204" width="26" height="6" fill="#dbeafe"/>
  <text x="458" y="225" text-anchor="middle" font-size="10" fill="#374151">...</text>
  <line x1="480" y1="180" x2="480" y2="115" stroke="#9ca3af" stroke-width="1.5" stroke-dasharray="3,3"/>
  <line x1="480" y1="115" x2="510" y2="115" stroke="#22c55e" stroke-width="2" marker-end="url(#arrow2)"/>
  <rect x="490" y="90" width="60" height="50" rx="8" fill="#dcfce7" stroke="#22c55e"/>
  <text x="520" y="112" text-anchor="middle" font-size="10" fill="#166534">Chọn</text>
  <text x="520" y="126" text-anchor="middle" font-size="10" fill="#166534">"Hà Nội"</text>
</svg>
<span class="curriculum-diagram-caption">LLM tính xác suất cho mọi từ có thể đứng tiếp theo, rồi chọn từ khả năng cao nhất — lặp lại từng token một cho đến hết câu trả lời.</span>
</div>

Nó lặp lại quá trình này **từng token một** để tạo ra cả câu trả lời — không "suy nghĩ" theo cách con người, mà tính toán xác suất dựa trên những gì đã học.

## Kiến trúc Transformer

LLM hiện đại (GPT, Gemini, Llama, Claude) đều dựa trên kiến trúc **Transformer** (Google, 2017), với cơ chế **self-attention** cho phép mô hình "chú ý" đến các từ liên quan trong toàn bộ đoạn văn, dù chúng ở xa nhau trong câu — đây là lý do LLM hiểu ngữ cảnh tốt hơn hẳn các mô hình cũ.

## Hai giai đoạn: Training và Inference

- **Training (huấn luyện)**: quá trình tốn kém, mất hàng tuần/tháng với hàng nghìn GPU, để mô hình học từ dữ liệu.
- **Inference (suy luận)**: quá trình bạn dùng hàng ngày — nhập prompt, mô hình trả lời — dùng lại "kiến thức" đã học từ training, không học thêm gì mới trong lúc trò chuyện (trừ khi có cơ chế RAG/fine-tuning riêng).

## Giới hạn cần biết

- **Hallucination (ảo giác)**: LLM có thể "bịa" thông tin nghe rất tự tin nhưng sai, vì nó dự đoán từ có khả năng cao chứ không tra cứu sự thật. Ví dụ: hỏi về một cuốn sách không tồn tại, LLM vẫn có thể "tóm tắt" nó một cách rất thuyết phục.
- **Kiến thức có hạn mốc thời gian** (knowledge cutoff): mô hình không biết các sự kiện sau ngày dữ liệu huấn luyện kết thúc, trừ khi được kết nối Internet/RAG.""",
    },
    {
        "id": "basic-4",
        "level": "basic",
        "title": "Token và Context Window là gì?",
        "summary": '"Đơn vị đo lường" mà LLM dùng để đọc và viết văn bản, và giới hạn bộ nhớ ngắn hạn.',
        "content": """## Token là gì?

LLM không đọc theo "chữ cái" hay "từ" như con người, mà theo **token** — một mảnh văn bản có thể là một từ, một phần của từ, hoặc một dấu câu. Ví dụ tiếng Anh "unbelievable" có thể tách thành 3 token: `un`, `believ`, `able`. Tiếng Việt có dấu thường tốn nhiều token hơn tiếng Anh cho cùng một ý.

> 🌱 **Ví dụ đời thường**: Token giống như từng viên gạch Lego để xây một câu — có viên là cả một từ, có viên chỉ là một mảnh nhỏ của từ. LLM "xây" câu trả lời bằng cách ghép từng viên gạch một, không phải xây nguyên khối cùng lúc.

Quy tắc ước lượng nhanh: **1 token ≈ 4 ký tự tiếng Anh**, hoặc khoảng 0.75 từ.

## Context Window (cửa sổ ngữ cảnh)

Context Window là **số lượng token tối đa** mà mô hình có thể "nhìn thấy" cùng lúc trong một lượt hỏi-đáp — bao gồm cả prompt của bạn, lịch sử hội thoại trước đó, và câu trả lời mô hình sắp tạo ra.

<div class="curriculum-diagram">
<svg viewBox="0 0 560 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Minh họa Context Window bị lấp đầy bởi hội thoại và bị cắt bớt phần đầu">
  <text x="10" y="20" font-size="12" font-weight="700" fill="#111827">Context Window (giới hạn ví dụ: 8 "ô" token)</text>
  <rect x="10" y="35" width="540" height="40" rx="6" fill="none" stroke="#111827" stroke-width="2"/>
  <rect x="14" y="39" width="60" height="32" fill="#fecaca"/>
  <text x="44" y="60" text-anchor="middle" font-size="9" fill="#7f1d1d">bị cắt</text>
  <rect x="76" y="39" width="60" height="32" fill="#fde68a"/>
  <rect x="138" y="39" width="60" height="32" fill="#fde68a"/>
  <rect x="200" y="39" width="60" height="32" fill="#bbf7d0"/>
  <rect x="262" y="39" width="60" height="32" fill="#bbf7d0"/>
  <rect x="324" y="39" width="60" height="32" fill="#bfdbfe"/>
  <rect x="386" y="39" width="60" height="32" fill="#bfdbfe"/>
  <rect x="448" y="39" width="100" height="32" fill="#93c5fd"/>
  <text x="44" y="88" text-anchor="middle" font-size="9" fill="#6b7280">Tin nhắn cũ</text>
  <text x="168" y="88" text-anchor="middle" font-size="9" fill="#92400e">Hội thoại giữa</text>
  <text x="292" y="88" text-anchor="middle" font-size="9" fill="#166534">Tài liệu đính kèm</text>
  <text x="416" y="88" text-anchor="middle" font-size="9" fill="#1e3a8a">Câu hỏi mới</text>
  <text x="498" y="88" text-anchor="middle" font-size="9" fill="#1e3a8a">Câu trả lời AI</text>
  <text x="280" y="115" text-anchor="middle" font-size="10" fill="#7f1d1d">↑ Khi hội thoại quá dài, phần đầu (màu đỏ) bị đẩy ra ngoài "cửa sổ" — mô hình không còn "nhớ" nó nữa</text>
</svg>
</div>

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

> 🌱 **Ví dụ đời thường**: Prompt giống như việc bạn nhờ một nhân viên mới làm việc. Nói mơ hồ "làm giúp anh cái báo cáo" sẽ ra kết quả khó đoán; nói rõ vai trò, việc cần làm, giới hạn thời gian/định dạng thì kết quả sẽ đúng ý hơn nhiều.

## 4 thành phần của một prompt tốt

<div class="curriculum-diagram">
<svg viewBox="0 0 420 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="4 thành phần xếp chồng tạo nên một prompt hoàn chỉnh">
  <defs>
    <marker id="arrow3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#6b7280"/>
    </marker>
  </defs>
  <rect x="10" y="10" width="400" height="42" rx="8" fill="#dbeafe" stroke="#2563eb"/>
  <text x="30" y="36" font-size="12" fill="#1e3a8a">1. Vai trò / Bối cảnh (Role)</text>
  <line x1="210" y1="52" x2="210" y2="66" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow3)"/>
  <rect x="10" y="70" width="400" height="42" rx="8" fill="#dcfce7" stroke="#22c55e"/>
  <text x="30" y="96" font-size="12" fill="#166534">2. Nhiệm vụ cụ thể (Task)</text>
  <line x1="210" y1="112" x2="210" y2="126" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow3)"/>
  <rect x="10" y="130" width="400" height="42" rx="8" fill="#fef3c7" stroke="#f59e0b"/>
  <text x="30" y="156" font-size="12" fill="#92400e">3. Ràng buộc / Định dạng</text>
  <line x1="210" y1="172" x2="210" y2="186" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow3)"/>
  <rect x="10" y="190" width="400" height="42" rx="8" fill="#ede9fe" stroke="#a78bfa"/>
  <text x="30" y="216" font-size="12" fill="#5b21b6">4. Ví dụ mẫu (nếu cần)</text>
  <line x1="210" y1="232" x2="210" y2="246" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow3)"/>
  <rect x="60" y="250" width="300" height="42" rx="8" fill="#2563eb"/>
  <text x="210" y="276" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">Prompt hoàn chỉnh</text>
</svg>
</div>

1. **Vai trò / bối cảnh (Role/Context)**: AI nên đóng vai gì? Ví dụ: "Bạn là một biên tập viên kỹ thuật có 10 năm kinh nghiệm."
2. **Nhiệm vụ (Task)**: Yêu cầu cụ thể, dùng động từ rõ ràng — "tóm tắt", "liệt kê", "viết lại", "so sánh"... tránh mơ hồ như "nói gì đó về...".
3. **Ràng buộc / định dạng (Constraints/Format)**: độ dài, giọng văn, ngôn ngữ, định dạng đầu ra (bảng, bullet, JSON...).
4. **Ví dụ (nếu cần)**: cho AI 1-2 ví dụ mẫu để nó bắt đúng "tông" bạn muốn (xem bài Few-shot Prompting).

## Ví dụ so sánh — thử trực tiếp bên dưới

{{PROMPT_LAB}}

Prompt kém khiến AI phải "đoán" bạn muốn gì — nó có thể trả lời chung chung, sai giọng văn, sai độ dài. Prompt tốt loại bỏ hầu hết sự đoán mò đó.

## Nguyên tắc vàng

- **Càng cụ thể càng tốt** — AI không đọc được suy nghĩ, chỉ dựa vào chữ bạn viết.
- **Nói AI nên làm gì, thay vì không nên làm gì** ("Trả lời bằng 3 gạch đầu dòng" tốt hơn "Đừng trả lời dài dòng").
- **Lặp lại và tinh chỉnh**: prompt hiếm khi đúng ngay lần đầu — hãy đọc kết quả rồi bổ sung ràng buộc còn thiếu.""",
        "prompt_lab": {
            "bad": {
                "label": "Prompt kém",
                "prompt": "Viết về marketing.",
                "reply": "Marketing là quá trình quảng bá và bán sản phẩm hoặc dịch vụ, bao gồm nghiên cứu thị trường, quảng cáo, quan hệ công chúng và bán hàng. Marketing hiệu quả giúp doanh nghiệp:\n\n- Xây dựng nhận diện thương hiệu\n- Thu hút khách hàng mới\n- Duy trì khách hàng hiện tại\n- Tăng doanh số bán hàng\n\nCác kênh phổ biến hiện nay gồm mạng xã hội, email marketing, SEO và quảng cáo trả phí. Bạn muốn tôi đi sâu vào khía cạnh nào cụ thể — chiến lược, kênh, hay công cụ đo lường hiệu quả?",
            },
            "good": {
                "label": "Prompt tốt",
                "prompt": "Bạn là chuyên gia marketing cho startup công nghệ.\nHãy viết 3 tiêu đề email quảng cáo (mỗi tiêu đề dưới 60 ký tự)\ncho sản phẩm ứng dụng học AI dành cho người mới bắt đầu.\nGiọng văn: thân thiện, tạo cảm giác cấp bách nhẹ nhàng.",
                "reply": "1. \"AI không còn xa vời — bắt đầu từ hôm nay\"\n2. \"7 ngày để hiểu AI, cả đời để làm chủ nó\"\n3. \"Học AI dễ như lướt điện thoại, hiệu quả hơn nhiều\"",
            },
        },
    },
    {
        "id": "prompting-2",
        "level": "prompting",
        "title": "Zero-shot vs Few-shot Prompting",
        "summary": "Khi nào nên hỏi thẳng, khi nào nên cho AI xem ví dụ mẫu trước.",
        "content": """## Zero-shot Prompting

Là cách hỏi **không kèm ví dụ** — bạn tin tưởng mô hình đã đủ kiến thức nền để hiểu và thực hiện yêu cầu ngay.

> 🌱 **Ví dụ đời thường**: Zero-shot giống như hỏi thẳng một chuyên gia có kinh nghiệm — họ đã biết cách làm nên không cần bạn hướng dẫn thêm. Few-shot giống như đưa họ 2-3 mẫu báo cáo cũ trước khi nhờ viết báo cáo mới, để đảm bảo đúng format công ty bạn.

```
Phân loại cảm xúc của câu sau: "Tích cực", "Tiêu cực" hoặc "Trung lập".
Câu: "Sản phẩm giao chậm nhưng chất lượng khá ổn."
```

Phù hợp cho các tác vụ phổ biến, đơn giản mà mô hình đã được huấn luyện rộng rãi.

## Few-shot Prompting

Là cách **đưa vài ví dụ mẫu (input → output)** trước khi đặt câu hỏi thật, giúp AI "bắt" đúng định dạng, văn phong, hoặc logic phân loại bạn muốn — đặc biệt hữu ích với các tác vụ đặc thù, không chuẩn.

<div class="curriculum-diagram">
<svg viewBox="0 0 560 190" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="So sánh luồng Zero-shot và Few-shot prompting">
  <defs>
    <marker id="arrow4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#6b7280"/>
    </marker>
  </defs>
  <text x="10" y="20" font-size="12" font-weight="700" fill="#111827">Zero-shot</text>
  <rect x="10" y="30" width="140" height="40" rx="8" fill="#f3f4f6" stroke="#d1d5db"/>
  <text x="80" y="54" text-anchor="middle" font-size="11" fill="#374151">Câu hỏi</text>
  <line x1="150" y1="50" x2="180" y2="50" stroke="#6b7280" stroke-width="2" marker-end="url(#arrow4)"/>
  <rect x="182" y="30" width="90" height="40" rx="8" fill="#dbeafe" stroke="#2563eb"/>
  <text x="227" y="54" text-anchor="middle" font-size="11" fill="#1e3a8a">AI</text>
  <line x1="272" y1="50" x2="302" y2="50" stroke="#6b7280" stroke-width="2" marker-end="url(#arrow4)"/>
  <rect x="304" y="30" width="140" height="40" rx="8" fill="#dcfce7" stroke="#22c55e"/>
  <text x="374" y="54" text-anchor="middle" font-size="11" fill="#166534">Trả lời (chung chung)</text>
  <text x="10" y="110" font-size="12" font-weight="700" fill="#111827">Few-shot</text>
  <rect x="10" y="120" width="140" height="50" rx="8" fill="#fef3c7" stroke="#f59e0b"/>
  <text x="80" y="140" text-anchor="middle" font-size="10" fill="#92400e">2-3 ví dụ mẫu</text>
  <text x="80" y="154" text-anchor="middle" font-size="10" fill="#92400e">+ câu hỏi mới</text>
  <line x1="150" y1="145" x2="180" y2="145" stroke="#6b7280" stroke-width="2" marker-end="url(#arrow4)"/>
  <rect x="182" y="125" width="90" height="40" rx="8" fill="#dbeafe" stroke="#2563eb"/>
  <text x="227" y="149" text-anchor="middle" font-size="11" fill="#1e3a8a">AI</text>
  <line x1="272" y1="145" x2="302" y2="145" stroke="#6b7280" stroke-width="2" marker-end="url(#arrow4)"/>
  <rect x="304" y="125" width="140" height="40" rx="8" fill="#dcfce7" stroke="#22c55e"/>
  <text x="374" y="143" text-anchor="middle" font-size="11" fill="#166534">Trả lời đúng</text>
  <text x="374" y="157" text-anchor="middle" font-size="11" fill="#166534">định dạng mong muốn</text>
</svg>
</div>

## Thử trực tiếp: cùng một câu hỏi, có và không có ví dụ mẫu

{{PROMPT_LAB}}

## Khi nào dùng cái nào?

| Tình huống | Nên dùng |
|---|---|
| Tác vụ phổ thông, rõ ràng | Zero-shot |
| Cần định dạng đầu ra chính xác, nhất quán | Few-shot |
| Logic phân loại đặc thù của riêng bạn/công ty | Few-shot |
| Muốn tiết kiệm token (few-shot tốn thêm token cho ví dụ) | Zero-shot |

> 💡 2-5 ví dụ chất lượng thường hiệu quả hơn nhiều ví dụ nhưng sơ sài.""",
        "prompt_lab": {
            "bad": {
                "label": "Không có ví dụ (Zero-shot)",
                "prompt": "Phân loại mức độ ưu tiên: \"Không tìm thấy nút đăng xuất.\"",
                "reply": "Ưu tiên: Trung bình.\n\nĐây là lỗi về khả năng sử dụng (usability) — người dùng bị ảnh hưởng nhưng vẫn có cách khác để đăng xuất (ví dụ xoá cache trình duyệt hoặc đóng ứng dụng). Vì không gây mất dữ liệu hay ngừng hoạt động hoàn toàn nên tôi xếp ở mức trung bình, không phải mức cao nhất.",
            },
            "good": {
                "label": "Có 3 ví dụ mẫu (Few-shot)",
                "prompt": "Câu: \"App bị crash không mở được.\" → Ưu tiên: Cao\nCâu: \"Muốn đổi màu giao diện.\" → Ưu tiên: Thấp\nCâu: \"Thanh toán bị trừ tiền 2 lần.\" → Ưu tiên: Cao\n\nCâu: \"Không tìm thấy nút đăng xuất.\" → Ưu tiên:",
                "reply": "Ưu tiên: Thấp",
            },
        },
    },
    {
        "id": "prompting-3",
        "level": "prompting",
        "title": 'Chain-of-Thought: dạy AI "suy nghĩ từng bước"',
        "summary": "Kỹ thuật giúp AI giải quyết bài toán logic/suy luận chính xác hơn.",
        "content": """## Vấn đề

LLM sinh câu trả lời theo kiểu "trả lời ngay", nên với các bài toán cần **nhiều bước suy luận** (tính toán, logic, lập kế hoạch), nó dễ nhảy cóc và ra kết quả sai — dù từng bước riêng lẻ nó có thể làm đúng.

> 🌱 **Ví dụ đời thường**: Giống việc giải toán — nếu bị bắt trả lời ngay không được nháp, bạn dễ tính nhầm. Nhưng nếu được viết ra từng bước trên giấy nháp, khả năng đúng cao hơn hẳn. Chain-of-Thought chính là "cho AI viết nháp" trước khi chốt đáp án.

## Giải pháp: Chain-of-Thought (CoT)

Yêu cầu AI **trình bày từng bước suy luận** trước khi đưa ra kết luận cuối cùng, thay vì trả lời tắt. Chỉ cần thêm cụm "Hãy suy luận từng bước" (*think step by step*) thường đã cải thiện đáng kể độ chính xác.

<div class="curriculum-diagram">
<svg viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="So sánh trả lời trực tiếp dễ sai và Chain-of-Thought từng bước chính xác hơn">
  <defs>
    <marker id="arrow5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#6b7280"/>
    </marker>
  </defs>
  <text x="10" y="20" font-size="12" font-weight="700" fill="#111827">Không có CoT — dễ nhảy cóc</text>
  <rect x="10" y="30" width="130" height="40" rx="8" fill="#f3f4f6" stroke="#d1d5db"/>
  <text x="75" y="54" text-anchor="middle" font-size="10" fill="#374151">Đề bài</text>
  <line x1="140" y1="50" x2="330" y2="50" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,3" marker-end="url(#arrow5)"/>
  <rect x="332" y="30" width="130" height="40" rx="8" fill="#fee2e2" stroke="#ef4444"/>
  <text x="397" y="48" text-anchor="middle" font-size="10" fill="#991b1b">Đáp án</text>
  <text x="397" y="62" text-anchor="middle" font-size="10" fill="#991b1b">(dễ sai)</text>
  <text x="10" y="110" font-size="12" font-weight="700" fill="#111827">Có CoT — đi từng bước</text>
  <rect x="10" y="120" width="90" height="40" rx="8" fill="#f3f4f6" stroke="#d1d5db"/>
  <text x="55" y="144" text-anchor="middle" font-size="10" fill="#374151">Đề bài</text>
  <line x1="100" y1="140" x2="122" y2="140" stroke="#22c55e" stroke-width="2" marker-end="url(#arrow5)"/>
  <rect x="124" y="120" width="80" height="40" rx="8" fill="#dcfce7" stroke="#22c55e"/>
  <text x="164" y="144" text-anchor="middle" font-size="10" fill="#166534">Bước 1</text>
  <line x1="204" y1="140" x2="226" y2="140" stroke="#22c55e" stroke-width="2" marker-end="url(#arrow5)"/>
  <rect x="228" y="120" width="80" height="40" rx="8" fill="#dcfce7" stroke="#22c55e"/>
  <text x="268" y="144" text-anchor="middle" font-size="10" fill="#166534">Bước 2</text>
  <line x1="308" y1="140" x2="330" y2="140" stroke="#22c55e" stroke-width="2" marker-end="url(#arrow5)"/>
  <rect x="332" y="120" width="80" height="40" rx="8" fill="#dcfce7" stroke="#22c55e"/>
  <text x="372" y="144" text-anchor="middle" font-size="10" fill="#166534">Bước 3</text>
  <line x1="412" y1="140" x2="434" y2="140" stroke="#22c55e" stroke-width="2" marker-end="url(#arrow5)"/>
  <rect x="436" y="120" width="110" height="40" rx="8" fill="#bbf7d0" stroke="#16a34a"/>
  <text x="491" y="138" text-anchor="middle" font-size="10" fill="#14532d">Đáp án</text>
  <text x="491" y="152" text-anchor="middle" font-size="10" fill="#14532d">(chính xác hơn)</text>
</svg>
</div>

## Thử trực tiếp: cùng một bài toán, có và không có yêu cầu suy luận từng bước

{{PROMPT_LAB}}

## Biến thể nâng cao

- **Few-shot CoT**: kèm ví dụ mẫu có sẵn lời giải từng bước để AI bắt chước cách trình bày.
- **Self-consistency**: chạy CoT nhiều lần với cùng câu hỏi, lấy đáp án xuất hiện nhiều nhất — tăng độ tin cậy cho các quyết định quan trọng.

## Khi nào nên dùng?

Toán học, logic, debug code, lập kế hoạch nhiều bước, phân tích dữ liệu. Với câu hỏi đơn giản (tra cứu sự kiện, dịch thuật), CoT thường không cần thiết và làm câu trả lời dài dòng hơn.""",
        "prompt_lab": {
            "bad": {
                "label": "Không có CoT",
                "prompt": "Một cửa hàng có 23 quả táo. Bán 8 quả sáng nay, nhập thêm 15 quả buổi trưa.\nChiều bán tiếp 12 quả. Hỏi cửa hàng còn bao nhiêu quả táo?",
                "reply": "Cửa hàng còn 22 quả táo.",
            },
            "good": {
                "label": "Có CoT",
                "prompt": "Một cửa hàng có 23 quả táo. Bán 8 quả sáng nay, nhập thêm 15 quả buổi trưa.\nChiều bán tiếp 12 quả. Hỏi cửa hàng còn bao nhiêu quả táo?\n\nHãy giải từng bước một, ghi rõ phép tính ở mỗi bước, rồi mới kết luận.",
                "reply": "Bước 1: 23 - 8 = 15 quả (sau khi bán buổi sáng)\nBước 2: 15 + 15 = 30 quả (sau khi nhập thêm buổi trưa)\nBước 3: 30 - 12 = 18 quả (sau khi bán buổi chiều)\n\nVậy cửa hàng còn lại 18 quả táo.",
            },
        },
    },
    {
        "id": "prompting-4",
        "level": "prompting",
        "title": 'Temperature, Top-p: điều khiển độ "sáng tạo" của AI',
        "summary": "Các tham số kỹ thuật quyết định câu trả lời của AI ổn định hay đa dạng.",
        "content": """## Nhắc lại: LLM chọn từ tiếp theo dựa trên xác suất

Với mỗi vị trí, mô hình tính ra một danh sách xác suất cho các token có thể đứng tiếp theo. **Temperature** và **Top-p** quyết định cách mô hình *chọn* từ danh sách xác suất đó.

> 🌱 **Ví dụ đời thường**: Temperature giống như mức độ "liều" khi chọn món ăn ở quán quen. Temperature thấp = luôn gọi món tủ quen thuộc (an toàn, ổn định). Temperature cao = sẵn sàng thử món lạ trên menu (thú vị hơn, nhưng đôi khi không hợp khẩu vị).

## Temperature

Điều chỉnh mức độ "liều lĩnh" khi chọn từ, giá trị thường từ 0 đến 2:

<div class="curriculum-diagram">
<svg viewBox="0 0 560 190" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="So sánh phân phối xác suất khi Temperature thấp và cao">
  <text x="140" y="18" text-anchor="middle" font-size="12" font-weight="700" fill="#111827">Temperature thấp (0 - 0.3)</text>
  <rect x="40" y="30" width="30" height="100" fill="#2563eb"/>
  <rect x="80" y="118" width="30" height="12" fill="#93c5fd"/>
  <rect x="120" y="123" width="30" height="7" fill="#bfdbfe"/>
  <rect x="160" y="126" width="30" height="4" fill="#dbeafe"/>
  <text x="140" y="145" text-anchor="middle" font-size="10" fill="#6b7280">→ luôn chọn từ "chắc ăn" nhất</text>
  <text x="420" y="18" text-anchor="middle" font-size="12" font-weight="700" fill="#111827">Temperature cao (0.8 - 1.2+)</text>
  <rect x="320" y="70" width="30" height="60" fill="#2563eb"/>
  <rect x="360" y="80" width="30" height="50" fill="#3b82f6"/>
  <rect x="400" y="90" width="30" height="40" fill="#60a5fa"/>
  <rect x="440" y="95" width="30" height="35" fill="#93c5fd"/>
  <text x="420" y="145" text-anchor="middle" font-size="10" fill="#6b7280">→ các lựa chọn có cơ hội gần ngang nhau</text>
</svg>
<span class="curriculum-diagram-caption">Mỗi cột là xác suất của một từ ứng viên. Temperature thấp làm cột cao nhất "áp đảo"; Temperature cao san bằng các cột lại gần nhau hơn.</span>
</div>

- **Temperature thấp (0 – 0.3)**: gần như luôn chọn từ có xác suất cao nhất → câu trả lời **ổn định, nhất quán, ít sáng tạo**. Phù hợp: trả lời dữ kiện, code, phân loại dữ liệu, tóm tắt.
- **Temperature cao (0.7 – 1.2+)**: sẵn sàng chọn cả những từ xác suất thấp hơn → câu trả lời **đa dạng, sáng tạo hơn**, nhưng cũng dễ lạc đề/kém chính xác hơn. Phù hợp: viết sáng tạo, brainstorm, thơ văn.

## Thử trực tiếp: cùng yêu cầu, khác cách "ra lệnh" độ sáng tạo

Nhiều ứng dụng (kể cả không gian Thực hành của app này) không cho bạn chỉnh trực tiếp Temperature — nhưng bạn có thể **yêu cầu bằng lời** để đạt hiệu ứng tương tự:

{{PROMPT_LAB}}

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
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu trung tính (giống Temperature thấp)",
                "prompt": "Viết một khẩu hiệu quảng cáo cho quán cà phê.",
                "reply": "\"Cà phê ngon, giá tốt, phục vụ tận tâm.\"",
            },
            "good": {
                "label": "Yêu cầu đa dạng, táo bạo (giống Temperature cao)",
                "prompt": "Viết 5 khẩu hiệu quảng cáo cho quán cà phê, mỗi câu theo một phong cách hoàn toàn khác nhau (hài hước, thơ mộng, táo bạo, tối giản, gây tò mò). Đừng ngại thử ý tưởng khác lạ.",
                "reply": "1. (Hài hước) \"Cà phê ở đây đậm hơn cả deadline của bạn.\"\n2. (Thơ mộng) \"Một ngụm cà phê, một khoảng lặng giữa phố xá vội vã.\"\n3. (Táo bạo) \"Không ngon, không lấy tiền. Chấm hết.\"\n4. (Tối giản) \"Cà phê. Đúng nghĩa.\"\n5. (Gây tò mò) \"Bí quyết trong tách cà phê này, có lẽ bạn sẽ muốn hỏi lại lần hai.\"",
            },
        },
    },
    {
        "id": "advanced-1",
        "level": "advanced",
        "title": "RAG (Retrieval-Augmented Generation) là gì?",
        "summary": 'Cách "gắn" thêm kiến thức riêng/mới cho AI mà không cần huấn luyện lại mô hình.',
        "content": """## Vấn đề cần giải quyết

LLM chỉ biết những gì có trong dữ liệu huấn luyện, tính đến một mốc thời gian nhất định (*knowledge cutoff*), và **không biết** tài liệu nội bộ công ty bạn, email cá nhân, hay tin tức hôm nay.

> 🌱 **Ví dụ đời thường**: Giống việc bạn nhờ một chuyên gia rất giỏi nhưng chưa từng đọc tài liệu công ty bạn trả lời câu hỏi nội bộ. Thay vì bắt họ học thuộc cả kho tài liệu (tốn kém, mất thời gian), bạn đưa cho họ đúng vài trang liên quan ngay lúc hỏi — đó chính là RAG.

## RAG hoạt động thế nào?

**RAG (Retrieval-Augmented Generation)** kết hợp một bước **tìm kiếm (Retrieval)** trước khi AI **sinh câu trả lời (Generation)**:

<div class="curriculum-diagram">
<svg viewBox="0 0 600 160" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sơ đồ luồng RAG: tìm kiếm tài liệu rồi mới đưa cho LLM trả lời">
  <defs>
    <marker id="arrow6" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#2563eb"/>
    </marker>
  </defs>
  <rect x="10" y="55" width="90" height="50" rx="8" fill="#f3f4f6" stroke="#d1d5db"/>
  <text x="55" y="76" text-anchor="middle" font-size="10" fill="#374151">Câu hỏi</text>
  <text x="55" y="90" text-anchor="middle" font-size="10" fill="#374151">người dùng</text>
  <line x1="100" y1="80" x2="128" y2="80" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow6)"/>
  <rect x="130" y="55" width="120" height="50" rx="8" fill="#fef3c7" stroke="#f59e0b"/>
  <text x="190" y="76" text-anchor="middle" font-size="10" fill="#92400e">Tìm kiếm trong</text>
  <text x="190" y="90" text-anchor="middle" font-size="10" fill="#92400e">Vector Database</text>
  <line x1="250" y1="80" x2="278" y2="80" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow6)"/>
  <rect x="280" y="55" width="120" height="50" rx="8" fill="#dcfce7" stroke="#22c55e"/>
  <text x="340" y="76" text-anchor="middle" font-size="10" fill="#166534">Đoạn tài liệu</text>
  <text x="340" y="90" text-anchor="middle" font-size="10" fill="#166534">liên quan nhất</text>
  <line x1="400" y1="80" x2="428" y2="80" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow6)"/>
  <rect x="430" y="35" width="80" height="90" rx="8" fill="#dbeafe" stroke="#2563eb"/>
  <text x="470" y="70" text-anchor="middle" font-size="10" fill="#1e3a8a">Prompt =</text>
  <text x="470" y="84" text-anchor="middle" font-size="10" fill="#1e3a8a">Tài liệu +</text>
  <text x="470" y="98" text-anchor="middle" font-size="10" fill="#1e3a8a">Câu hỏi</text>
  <line x1="510" y1="80" x2="538" y2="80" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow6)"/>
  <rect x="540" y="55" width="55" height="50" rx="8" fill="#ede9fe" stroke="#a78bfa"/>
  <text x="567" y="84" text-anchor="middle" font-size="12" font-weight="700" fill="#5b21b6">LLM</text>
</svg>
<span class="curriculum-diagram-caption">RAG chèn thêm bước "tra cứu" trước khi LLM trả lời, giúp câu trả lời dựa trên tài liệu thật thay vì chỉ trí nhớ đã huấn luyện.</span>
</div>

1. Người dùng đặt câu hỏi.
2. Hệ thống tìm kiếm các đoạn tài liệu liên quan nhất trong kho dữ liệu riêng (thường dùng **vector database** để tìm theo "ý nghĩa" chứ không chỉ từ khóa).
3. Các đoạn tài liệu tìm được được **chèn vào prompt** cùng câu hỏi gốc, gửi cho LLM.
4. LLM trả lời **dựa trên ngữ cảnh vừa được cung cấp**, thay vì chỉ dựa vào trí nhớ đã huấn luyện.

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

> 🌱 **Ví dụ đời thường**: LLM thuần giống một người cố vấn cực giỏi nhưng bị "trói tay" — chỉ có thể nói, không thể tự làm. Cho nó "công cụ" (tool) giống như cởi trói: giờ nó có thể tự tra Google, tự tính toán, tự gửi email thay vì chỉ đưa lời khuyên suông.

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

Một **Agent** là hệ thống dùng LLM làm "bộ não" trung tâm, lặp đi lặp lại một vòng: lập kế hoạch → hành động → quan sát kết quả → điều chỉnh, cho đến khi xong việc.

<div class="curriculum-diagram">
<svg viewBox="0 0 360 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vòng lặp Agent: lập kế hoạch, hành động, quan sát rồi lặp lại">
  <defs>
    <marker id="arrow7" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#2563eb"/>
    </marker>
  </defs>
  <circle cx="180" cy="180" r="150" fill="none" stroke="#e5e7eb" stroke-width="1.5" stroke-dasharray="4,4"/>
  <circle cx="180" cy="180" r="55" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="180" y="176" text-anchor="middle" font-size="12" font-weight="700" fill="#1e3a8a">Agent</text>
  <text x="180" y="192" text-anchor="middle" font-size="10" fill="#1e3a8a">(LLM)</text>
  <rect x="140" y="8" width="100" height="46" rx="8" fill="#fef3c7" stroke="#f59e0b"/>
  <text x="190" y="27" text-anchor="middle" font-size="10" fill="#92400e">1. Lập kế hoạch</text>
  <text x="190" y="41" text-anchor="middle" font-size="10" fill="#92400e">(Plan)</text>
  <rect x="290" y="155" width="100" height="46" rx="8" fill="#dcfce7" stroke="#22c55e"/>
  <text x="340" y="174" text-anchor="middle" font-size="10" fill="#166534">2. Dùng công cụ</text>
  <text x="340" y="188" text-anchor="middle" font-size="10" fill="#166534">(Act / Tool)</text>
  <rect x="140" y="300" width="100" height="46" rx="8" fill="#ede9fe" stroke="#a78bfa"/>
  <text x="190" y="319" text-anchor="middle" font-size="10" fill="#5b21b6">3. Quan sát</text>
  <text x="190" y="333" text-anchor="middle" font-size="10" fill="#5b21b6">(Observe)</text>
  <path d="M 235 45 A 150 150 0 0 1 335 160" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow7)"/>
  <path d="M 335 205 A 150 150 0 0 1 235 315" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow7)"/>
  <path d="M 145 315 A 150 150 0 0 1 145 45" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow7)"/>
  <text x="180" y="230" text-anchor="middle" font-size="9" fill="#6b7280" opacity="0"> </text>
</svg>
<span class="curriculum-diagram-caption">Agent lặp lại vòng Plan → Act → Observe cho đến khi hoàn thành nhiệm vụ, thay vì chỉ trả lời một câu hỏi đơn lẻ.</span>
</div>

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

> 🌱 **Ví dụ đời thường**: Prompt Engineering giống như đưa hướng dẫn rõ ràng hơn cho một nhân viên đã có sẵn. RAG giống như đưa họ thêm tài liệu tham khảo ngay lúc làm việc. Fine-tuning giống như cho họ đi đào tạo lại chuyên sâu — tốn thời gian và chi phí hơn hẳn hai cách trên.

| Phương pháp | Cách làm | Chi phí | Khi nào dùng |
|---|---|---|---|
| **Prompt Engineering** | Viết prompt tốt hơn (role, ví dụ, CoT...) | Rất thấp, tức thời | Luôn thử đầu tiên |
| **RAG** | Gắn thêm kho tài liệu để tra cứu lúc trả lời | Trung bình (cần vector DB) | Cần kiến thức mới/riêng, hay thay đổi |
| **Fine-tuning** | Huấn luyện tiếp mô hình trên dữ liệu riêng | Cao (dữ liệu, compute, thời gian) | Cần đổi *hành vi/văn phong* mô hình, khối lượng dùng rất lớn |

<div class="curriculum-diagram">
<svg viewBox="0 0 560 130" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Thang chi phí và độ phức tạp: Prompting thấp nhất, RAG ở giữa, Fine-tuning cao nhất">
  <line x1="30" y1="100" x2="530" y2="100" stroke="#9ca3af" stroke-width="2"/>
  <text x="280" y="122" text-anchor="middle" font-size="10" fill="#6b7280">Chi phí &amp; độ phức tạp tăng dần →</text>
  <rect x="50" y="70" width="130" height="30" rx="6" fill="#dcfce7" stroke="#22c55e"/>
  <text x="115" y="90" text-anchor="middle" font-size="11" fill="#166534">Prompt Engineering</text>
  <rect x="215" y="50" width="130" height="30" rx="6" fill="#fef3c7" stroke="#f59e0b"/>
  <text x="280" y="70" text-anchor="middle" font-size="11" fill="#92400e">RAG</text>
  <rect x="380" y="20" width="130" height="30" rx="6" fill="#fee2e2" stroke="#ef4444"/>
  <text x="445" y="40" text-anchor="middle" font-size="11" fill="#991b1b">Fine-tuning</text>
</svg>
</div>

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

    # ── Học tập (study) ──────────────────────────────────────────
    {
        "id": "study-1",
        "level": "study",
        "title": "Gia sư riêng theo kỹ thuật Feynman: giải thích lại để lộ lỗ hổng",
        "summary": "Dùng AI làm 'người kiểm tra' xem bạn đã thực sự hiểu bài hay chỉ học vẹt.",
        "content": """## Nguyên tắc

Kỹ thuật Feynman: cách tốt nhất để biết mình có hiểu thật một khái niệm hay không là **thử giải thích lại bằng lời đơn giản nhất**, như đang dạy cho một người chưa biết gì. Chỗ nào bạn ấp úng, dùng từ mơ hồ, hoặc phải "học thuộc" mà không giải thích được — đó chính là lỗ hổng kiến thức.

AI rất hợp để đóng vai "người chấm" bước này: đọc phần bạn tự giải thích, chỉ ra chỗ chưa rõ, và hỏi xoáy để kiểm tra độ sâu.

## Prompt mẫu

```
Tôi vừa học về [chủ đề]. Tôi sẽ giải thích lại cho bạn như thể
bạn hoàn toàn chưa biết gì về nó.

Sau khi đọc xong, hãy:
1. Chỉ ra tối đa 3 chỗ tôi giải thích chưa rõ, sai, hoặc chỉ đang
   "diễn đạt lại thuật ngữ" mà không thực sự giải thích.
2. Đặt 2-3 câu hỏi "tại sao" hoặc "điều gì xảy ra nếu..." để kiểm
   tra tôi có hiểu sâu hay chỉ nhớ bề mặt.
Đừng tự giải thích lại hộ tôi trừ khi tôi hỏi.

Chủ đề: [chủ đề]
Giải thích của tôi:
[dán phần bạn tự giải thích vào đây]
```

## Thử trực tiếp: hỏi xác nhận thường so với dùng prompt Feynman

{{PROMPT_LAB}}

> 💡 Mẹo: đừng đọc đáp án AI đưa ra ngay — thử tự trả lời câu hỏi "tại sao" trước, rồi mới xin AI chấm.""",
        "prompt_lab": {
            "bad": {
                "label": "Hỏi xác nhận thường",
                "prompt": "Giải thích của tôi về \"tại sao bầu trời có màu xanh\": Vì ánh sáng mặt trời chiếu vào bầu khí quyển và bị tán xạ nên ta thấy màu xanh. Đúng không?",
                "reply": "Đúng, cơ bản là vậy! Cụ thể hơn, ánh sáng xanh có bước sóng ngắn nên bị các phân tử trong khí quyển tán xạ mạnh hơn (hiện tượng tán xạ Rayleigh) so với ánh sáng đỏ hay vàng có bước sóng dài — đó là lý do bầu trời có màu xanh vào ban ngày.",
            },
            "good": {
                "label": "Dùng prompt Feynman",
                "prompt": "Tôi vừa học về hiện tượng tán xạ ánh sáng. Tôi sẽ giải thích lại cho bạn như thể bạn hoàn toàn chưa biết gì.\n\nSau khi đọc xong, hãy chỉ ra tối đa 3 chỗ tôi giải thích chưa rõ/sai, và đặt 2-3 câu hỏi \"tại sao\" để kiểm tra tôi hiểu sâu hay chỉ nhớ bề mặt.\n\nChủ đề: Tại sao bầu trời có màu xanh\nGiải thích của tôi: Vì ánh sáng mặt trời chiếu vào bầu khí quyển và bị tán xạ nên ta thấy màu xanh.",
                "reply": "Giải thích của bạn có 3 chỗ chưa rõ:\n\n1. Chưa giải thích tại sao chọn ra màu xanh cụ thể. Ánh sáng mặt trời gồm nhiều màu (đỏ, cam, vàng, lục, lam, chàm, tím), và tất cả đều bị tán xạ ít nhiều. Vậy tại sao kết quả lại thiên về xanh chứ không phải màu khác? Thiếu mắt xích: các màu có bước sóng khác nhau, và mức độ tán xạ phụ thuộc rất mạnh vào bước sóng (ánh sáng bước sóng ngắn bị tán xạ nhiều hơn ánh sáng bước sóng dài).\n\n2. Chưa nói cái gì gây ra tán xạ. \"Chiếu vào bầu khí quyển và bị tán xạ\" — tán xạ bởi cái gì? Là các phân tử khí (N2, O2) có kích thước rất nhỏ so với bước sóng ánh sáng. Đây là yếu tố quyết định loại tán xạ xảy ra (tán xạ Rayleigh) — nếu hạt to hơn (như giọt nước trong mây) thì cơ chế tán xạ khác hẳn và không chọn lọc theo màu (đó là lý do mây có màu trắng chứ không xanh).\n\n3. Giải thích chưa \"đóng vòng\" được với các hiện tượng liên quan. Một giải thích tốt phải dự đoán được các hiện tượng khác. Ví dụ: nếu đúng là \"tán xạ nên thấy xanh\", thì tại sao lúc hoàng hôn bầu trời lại đỏ/cam thay vì xanh đậm hơn? Giải thích hiện tại của bạn không có khả năng trả lời câu này.\n\n3 câu hỏi \"tại sao\" để kiểm tra:\n1. Tại sao ánh sáng bước sóng ngắn (xanh, tím) lại bị tán xạ mạnh hơn ánh sáng bước sóng dài (đỏ)? Cơ chế vật lý đằng sau là gì?\n2. Nếu tím có bước sóng ngắn hơn xanh lam (và theo logic tán xạ mạnh hơn), tại sao bầu trời không có màu tím?\n3. Tại sao lúc hoàng hôn, khi mặt trời ở gần đường chân trời, bầu trời và mặt trời lại chuyển sang màu đỏ/cam thay vì xanh?\n\nBạn thử trả lời xem — nếu bí ở đâu, đó chính là chỗ bạn đang \"nhớ kết luận\" chứ chưa thực sự hiểu cơ chế.",
            },
        },
    },
    {
        "id": "study-2",
        "level": "study",
        "title": "Biến tài liệu lộn xộn thành ghi chú theo khung Cornell Notes",
        "summary": "Yêu cầu AI cấu trúc lại bài giảng/chương sách thành ghi chú dễ ôn tập.",
        "content": """## Nguyên tắc

**Cornell Notes** là phương pháp ghi chú chia trang thành 3 phần: **Từ khóa/Câu hỏi** (bên trái) — **Nội dung chi tiết** (bên phải) — **Tóm tắt** (cuối trang). Cấu trúc này ép bạn chủ động ôn lại bằng cách tự trả lời các từ khóa/câu hỏi mà không cần đọc lại toàn bộ.

Thay vì tự tay tách bài giảng dài dòng, để AI làm bước cấu trúc hoá này.

## Prompt mẫu

```
Hãy chuyển đoạn ghi chú/bài giảng sau thành định dạng Cornell Notes:

- Cột "Từ khóa / Câu hỏi": liệt kê 5-8 từ khóa hoặc câu hỏi ôn tập
  tương ứng với từng ý chính.
- Cột "Nội dung chi tiết": diễn giải ngắn gọn từng ý, giữ đúng
  thông tin gốc, không thêm kiến thức bịa.
- "Tóm tắt": 2-3 câu tóm tắt toàn bộ đoạn, ở cuối.

Trình bày dạng bảng Markdown cho 2 cột đầu, và một đoạn văn cho
phần tóm tắt.

Nội dung: [dán bài giảng/chương sách vào đây]
```

## Thử trực tiếp: tóm tắt thường so với khung Cornell Notes

{{PROMPT_LAB}}

> 💡 Ôn bài bằng cách che cột phải, chỉ nhìn cột trái và tự nhớ lại nội dung — đúng tinh thần chủ động ôn tập của Cornell Notes.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu tóm tắt thường",
                "prompt": "Tóm tắt đoạn văn sau về quang hợp giúp tôi.\n\n[đoạn văn về quang hợp]",
                "reply": "Quang hợp là quá trình thực vật sử dụng năng lượng ánh sáng mặt trời để chuyển hóa CO2 và nước thành glucose và oxy, diễn ra chủ yếu ở lục lạp của tế bào lá. Đây là quá trình quan trọng cung cấp năng lượng cho hầu hết sinh vật trên Trái Đất và tạo ra oxy cho khí quyển.",
            },
            "good": {
                "label": "Dùng khung Cornell Notes",
                "prompt": "Hãy chuyển đoạn ghi chú sau thành định dạng Cornell Notes:\n- Cột \"Từ khóa/Câu hỏi\": 5-8 từ khóa hoặc câu hỏi ôn tập\n- Cột \"Nội dung chi tiết\": diễn giải ngắn gọn\n- \"Tóm tắt\": 2-3 câu cuối bài\n\nNội dung: [đoạn văn về quang hợp]",
                "reply": "Từ khóa/Câu hỏi → Nội dung chi tiết\nQuang hợp diễn ra ở đâu? → Chủ yếu ở lục lạp của tế bào lá\nNguyên liệu đầu vào là gì? → CO2, nước, ánh sáng mặt trời\nSản phẩm tạo ra là gì? → Glucose (năng lượng) và khí oxy\nVì sao quang hợp quan trọng? → Cung cấp năng lượng cho hầu hết sinh vật, tạo oxy cho khí quyển\n\nTóm tắt: Quang hợp là quá trình lục lạp trong lá cây chuyển hóa ánh sáng, nước và CO2 thành glucose và oxy — nền tảng năng lượng cho gần như toàn bộ sự sống trên Trái Đất.",
            },
        },
    },
    {
        "id": "study-3",
        "level": "study",
        "title": "Tạo bộ flashcard ôn tập theo kỹ thuật lặp lại ngắt quãng",
        "summary": "Nhờ AI soạn câu hỏi ôn tập rời rạc, đúng nguyên lý Spaced Repetition.",
        "content": """## Nguyên tắc

**Spaced Repetition (lặp lại ngắt quãng)** hiệu quả hơn học nhồi vì buộc não bộ chủ động "lôi" kiến thức ra khỏi trí nhớ nhiều lần theo các khoảng cách thời gian tăng dần, thay vì đọc lại thụ động. Điều kiện tiên quyết: bạn cần có sẵn một bộ câu hỏi ngắn, mỗi câu kiểm tra **đúng một** khái niệm.

## Prompt mẫu

```
Từ tài liệu sau, hãy tạo 10 flashcard ôn tập dạng hỏi-đáp.

Yêu cầu:
- Mỗi flashcard chỉ kiểm tra MỘT khái niệm/dữ kiện duy nhất
  (không gộp nhiều ý vào một câu hỏi).
- Câu hỏi ngắn gọn, câu trả lời không quá 2 câu.
- Sắp xếp từ dễ đến khó.
- Xuất ra dạng bảng 2 cột: "Mặt trước (câu hỏi)" | "Mặt sau (đáp án)".

Tài liệu: [dán nội dung cần ôn tập]
```

## Thử trực tiếp: câu hỏi gộp nhiều ý so với flashcard atomic

{{PROMPT_LAB}}

## Cách dùng hiệu quả

1. Ngày 1: học hết bộ flashcard.
2. Ngày 2: chỉ ôn lại những câu bạn trả lời sai hoặc do dự.
3. Ngày 4, ngày 7, ngày 14: lặp lại — khoảng cách giữa các lần ôn giãn dần ra.

> 💡 Có thể xin AI xuất thêm định dạng CSV (`câu hỏi,đáp án`) để import thẳng vào ứng dụng flashcard như Anki, Quizlet.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu chung chung",
                "prompt": "Tạo câu hỏi ôn tập từ đoạn tài liệu về HTTP status codes và REST API methods giúp tôi.",
                "reply": "1. HTTP status code là gì và tại sao chúng quan trọng trong REST API?\n2. Nêu sự khác biệt giữa các phương thức GET, POST, PUT, DELETE trong REST API.\n3. Mã lỗi nào thường gặp khi client gửi request không hợp lệ, và mã nào khi server gặp lỗi nội bộ?",
            },
            "good": {
                "label": "Dùng prompt mẫu (atomic)",
                "prompt": "Từ tài liệu sau, hãy tạo flashcard ôn tập dạng hỏi-đáp. Mỗi flashcard chỉ kiểm tra MỘT khái niệm duy nhất, không gộp nhiều ý.\n\nTài liệu: [về HTTP status codes và REST methods]",
                "reply": "Mặt trước → Mặt sau\nHTTP status 200 nghĩa là gì? → Request thành công\nHTTP status 404 nghĩa là gì? → Không tìm thấy tài nguyên được yêu cầu\nHTTP status 500 nghĩa là gì? → Lỗi phía server\nPhương thức GET dùng để làm gì? → Lấy dữ liệu, không thay đổi trạng thái server\nSự khác biệt giữa PUT và PATCH? → PUT thay thế toàn bộ resource, PATCH chỉ cập nhật một phần",
            },
        },
    },
    {
        "id": "study-4",
        "level": "study",
        "title": "Luyện thi vấn đáp / phỏng vấn bằng cách cho AI đóng vai giám khảo",
        "summary": "Mô phỏng áp lực hỏi-đáp thật để luyện phản xạ trước kỳ thi hoặc phỏng vấn.",
        "content": """## Nguyên tắc

Đọc tài liệu một mình khác hoàn toàn với việc phải **trả lời trực tiếp** dưới áp lực thời gian, bị hỏi xoáy, hỏi vặn. Cho AI đóng vai giám khảo/nhà tuyển dụng giúp bạn luyện phản xạ đó trước khi vào trận thật.

## Prompt mẫu

```
Đóng vai giám khảo môn [tên môn] / nhà tuyển dụng vị trí [vị trí].

Quy tắc:
- Hỏi tôi lần lượt từng câu, độ khó tăng dần, mỗi lần CHỈ một câu.
- Sau mỗi câu trả lời của tôi, chấm điểm trên thang 10, chỉ rõ điều
  còn thiếu hoặc sai, rồi mới hỏi câu tiếp theo.
- Giữ giọng nghiêm túc, không dễ dãi cho qua.
- Bắt đầu với câu hỏi đầu tiên ngay, không cần giới thiệu dài dòng.

Chủ đề trọng tâm: [liệt kê 2-3 chủ đề bạn muốn được hỏi]
```

## Thử trực tiếp: hỏi chung chung so với đóng vai giám khảo

{{PROMPT_LAB}}

> 💡 Luyện xong, đổi vai: nhờ AI cho bạn nhận xét chung "nếu là giám khảo thật, họ sẽ đánh giá phần thể hiện của bạn thế nào?" để có góc nhìn tổng thể.""",
        "prompt_lab": {
            "bad": {
                "label": "Hỏi chung chung",
                "prompt": "Hỏi tôi vài câu phỏng vấn Backend Developer.",
                "reply": "Được, dưới đây là một số câu hỏi phỏng vấn Backend Developer phổ biến:\n\n1. Sự khác biệt giữa SQL và NoSQL là gì, khi nào bạn chọn loại nào?\n2. RESTful API là gì? Nêu các nguyên tắc thiết kế REST API tốt.\n3. Bạn xử lý lỗi (error handling) trong một API như thế nào?\n4. Giải thích khái niệm database indexing và khi nào nên dùng.\n\nBạn có thể trả lời từng câu, tôi sẽ góp ý sau.",
            },
            "good": {
                "label": "Đóng vai giám khảo",
                "prompt": "Đóng vai giám khảo tuyển dụng vị trí Backend Developer.\nHỏi tôi lần lượt từng câu, mỗi lần CHỈ một câu. Sau mỗi câu trả lời, chấm điểm /10 và chỉ rõ thiếu sót trước khi hỏi tiếp.\nChủ đề trọng tâm: SQL vs NoSQL, REST API, xử lý lỗi",
                "reply": "Câu 1: Sự khác biệt giữa SQL và NoSQL là gì, và khi nào bạn sẽ chọn dùng loại nào cho một dự án thực tế?\n\n(Tôi sẽ chấm điểm câu trả lời của bạn trên thang 10 sau khi bạn trả lời, rồi mới chuyển sang câu 2.)",
            },
        },
    },
    {
        "id": "study-5",
        "level": "study",
        "title": "Luyện hội thoại ngoại ngữ với sửa lỗi theo ngữ cảnh thực tế",
        "summary": "Đóng vai tình huống đời thực để luyện phản xạ nói/viết, không chỉ học ngữ pháp khô khan.",
        "content": """## Nguyên tắc

Học ngoại ngữ hiệu quả cần **luyện trong ngữ cảnh** (đặt đồ ăn, phỏng vấn xin việc, than phiền dịch vụ...) thay vì chỉ học từ vựng rời rạc. AI có thể vừa đóng vai nhân vật trong tình huống, vừa dừng lại sửa lỗi ngay khi cần.

## Prompt mẫu

```
Hãy đóng vai một nhân viên phục vụ tại quán cà phê ở [thành phố],
chỉ nói bằng tiếng Anh. Tôi sẽ đóng vai khách hàng đặt đồ uống và
trò chuyện ngắn.

Quy tắc:
- Phản hồi tự nhiên như hội thoại đời thực, đừng quá trang trọng.
- Nếu tôi viết sai ngữ pháp/dùng từ không tự nhiên, sau câu trả lời
  trong vai, hãy thêm một dòng riêng: "📝 Sửa: [câu đúng]" kèm giải
  thích ngắn gọn tại sao.
- Tiếp tục hội thoại bình thường sau khi sửa.

Bắt đầu hội thoại đi.
```

## Thử trực tiếp: chỉ xin sửa câu so với đóng vai tình huống thực tế

{{PROMPT_LAB}}

> 💡 Sau vài lượt, đổi tình huống (phỏng vấn, khiếu nại, thuyết trình) để luyện đa dạng ngữ cảnh, không chỉ một kịch bản quen thuộc.""",
        "prompt_lab": {
            "bad": {
                "label": "Chỉ xin sửa câu",
                "prompt": "Sửa câu này giúp tôi: \"I want a coffee, no sugar please, and make it big size.\"",
                "reply": "Câu đúng hơn: \"Can I get a large coffee with no sugar, please?\"\n\nLý do: \"I want\" nghe khá thẳng, ít lịch sự trong tình huống gọi đồ ở quán; \"Can I get...\" là cách nói tự nhiên và lịch sự hơn của người bản xứ. Ngoài ra, \"big size\" nên đổi thành \"large\" — cách gọi kích cỡ chuẩn trong tiếng Anh quán cà phê.",
            },
            "good": {
                "label": "Đóng vai tình huống thực tế",
                "prompt": "Hãy đóng vai một nhân viên phục vụ tại quán cà phê ở London, chỉ nói tiếng Anh. Nếu tôi viết sai ngữ pháp, thêm dòng \"📝 Sửa: [câu đúng]\" sau câu trả lời trong vai.\n\nBắt đầu hội thoại đi.",
                "reply": "\"Hi there! What can I get for you today?\"\n\n(Chờ bạn trả lời trong vai khách hàng — nếu câu bạn viết có lỗi ngữ pháp hoặc cách diễn đạt không tự nhiên, tôi sẽ thêm dòng 📝 Sửa ngay sau câu trả lời trong vai.)",
            },
        },
    },
    {
        "id": "study-6",
        "level": "study",
        "title": "Giải thích một khái niệm khó ở 3 cấp độ: trẻ em, sinh viên, chuyên gia",
        "summary": "Kỹ thuật 'phân tầng giải thích' giúp bạn chọn đúng mức độ mình cần và thấy được chiều sâu vấn đề.",
        "content": """## Nguyên tắc

Một khái niệm phức tạp thường có nhiều "lớp" hiểu biết. Yêu cầu AI giải thích cùng lúc ở 3 mức độ giúp bạn: (1) nắm trực giác nhanh ở mức đơn giản, (2) hiểu cơ chế ở mức trung bình, (3) biết được sắc thái/giới hạn ở mức chuyên sâu — thay vì nhận một đoạn giải thích chung chung không rõ dành cho ai.

## Prompt mẫu

```
Giải thích khái niệm "[khái niệm]" theo 3 cấp độ:

1. 🧒 Như giải thích cho trẻ 10 tuổi: dùng ví dụ đời thường, không
   thuật ngữ chuyên môn.
2. 🎓 Như giải thích cho sinh viên năm nhất ngành liên quan: có thể
   dùng thuật ngữ cơ bản, giải thích cơ chế.
3. 🔬 Như trao đổi giữa hai chuyên gia: đi vào sắc thái, trường hợp
   ngoại lệ, hoặc tranh cãi học thuật (nếu có).

Mỗi mức tối đa 4-5 câu.
```

## Thử trực tiếp: hỏi thẳng so với yêu cầu 3 cấp độ

{{PROMPT_LAB}}

> 💡 Nếu vẫn thấy mơ hồ ở cấp độ 2, quay lại hỏi sâu thêm câu hỏi cụ thể ngay tại cấp độ đó, đừng nhảy lên cấp độ 3 vội.""",
        "prompt_lab": {
            "bad": {
                "label": "Hỏi thẳng, không chỉ định cấp độ",
                "prompt": "Blockchain là gì?",
                "reply": "Blockchain là một cấu trúc dữ liệu dạng chuỗi các khối (block), trong đó mỗi khối chứa một tập giao dịch và giá trị hash của khối trước đó, tạo thành một chuỗi liên kết không thể thay đổi ngược. Tính bất biến này được duy trì thông qua cơ chế đồng thuận phân tán (như Proof of Work hoặc Proof of Stake) giữa nhiều node trong mạng, giúp loại bỏ nhu cầu về một bên trung gian đáng tin cậy duy nhất.",
            },
            "good": {
                "label": "Yêu cầu giải thích 3 cấp độ",
                "prompt": "Giải thích khái niệm \"Blockchain\" theo 3 cấp độ: (1) như cho trẻ 10 tuổi, (2) như cho sinh viên năm nhất, (3) như trao đổi giữa hai chuyên gia. Mỗi mức tối đa 4-5 câu.",
                "reply": "🧒 Giống một cuốn sổ ghi chép mà ai cũng có một bản y hệt nhau — nếu ai đó muốn sửa gian một dòng, họ phải sửa ở tất cả các cuốn cùng lúc, mà điều đó gần như không thể làm âm thầm được.\n\n🎓 Blockchain là một cấu trúc dữ liệu dạng chuỗi khối, mỗi khối lưu một tập giao dịch và hash của khối trước. Nhiều máy tính (node) cùng xác nhận và lưu bản sao chuỗi này, nên dữ liệu khó bị giả mạo vì phải thay đổi đồng thời ở phần lớn các node.\n\n🔬 Các cơ chế đồng thuận như Proof of Work và Proof of Stake đánh đổi giữa bảo mật, mức độ phi tập trung, và khả năng mở rộng — đây chính là \"Blockchain Trilemma\" mà chưa hệ thống nào giải quyết hoàn hảo cả 3 cùng lúc.",
            },
        },
    },
    {
        "id": "study-7",
        "level": "study",
        "title": "Lập lộ trình tự học một kỹ năng mới theo tuần",
        "summary": "Biến mục tiêu mơ hồ 'muốn học X' thành lộ trình cụ thể, có mốc kiểm tra.",
        "content": """## Nguyên tắc

"Tôi muốn học lập trình" là mục tiêu quá mơ hồ để hành động. Một lộ trình tốt cần: **thời hạn rõ ràng, quỹ thời gian thực tế mỗi tuần, mốc kiểm tra (checkpoint) để biết mình có đang đi đúng hướng**, và một sản phẩm đầu ra cụ thể để chứng minh đã học được.

## Prompt mẫu

```
Tôi muốn học [kỹ năng] trong [số tuần] tuần.
Trình độ hiện tại: [mô tả ngắn, ví dụ: "chưa biết gì" / "biết cơ bản"].
Thời gian rảnh: [số giờ]/tuần.
Mục tiêu cuối: [ví dụ: "làm được một project nhỏ X"].

Hãy lập lộ trình theo từng tuần, mỗi tuần gồm:
- Chủ đề học trong tuần
- 1-2 tài nguyên/loại nội dung nên tìm (không cần link cụ thể)
- Một "checkpoint" cuối tuần để tự kiểm tra đã nắm được chưa
  (ví dụ: bài tập nhỏ, câu hỏi tự trả lời)

Tuần cuối cùng phải hướng tới hoàn thành mục tiêu cuối đã nêu.
```

## Thử trực tiếp: yêu cầu thiếu bối cảnh so với đủ bối cảnh

{{PROMPT_LAB}}

> 💡 Sau mỗi tuần thực tế, quay lại báo cáo với AI bạn đã làm được gì/khó ở đâu, xin điều chỉnh lộ trình tuần sau — đừng theo lộ trình cứng nhắc nếu thực tế lệch tiến độ.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu thiếu bối cảnh",
                "prompt": "Tôi muốn học Python. Giúp tôi lộ trình học.",
                "reply": "Để học Python, bạn có thể theo lộ trình sau:\n\n1. Học cú pháp cơ bản: biến, kiểu dữ liệu, câu lệnh điều kiện, vòng lặp\n2. Làm quen với cấu trúc dữ liệu: list, dict, tuple, set\n3. Học lập trình hướng đối tượng (OOP)\n4. Thực hành qua các bài tập nhỏ\n5. Làm một project thực tế để áp dụng kiến thức\n\nBạn nên dành khoảng 1-2 giờ mỗi ngày để có tiến bộ đều đặn. Chúc bạn học tốt!",
            },
            "good": {
                "label": "Yêu cầu đủ bối cảnh",
                "prompt": "Tôi muốn học Python trong 8 tuần.\nTrình độ hiện tại: chưa biết gì.\nThời gian rảnh: 5 giờ/tuần.\nMục tiêu cuối: làm được project quản lý chi tiêu cá nhân.\n\nHãy lập lộ trình theo từng tuần, mỗi tuần có checkpoint tự kiểm tra.",
                "reply": "Tuần 1-2: Cú pháp cơ bản, biến, kiểu dữ liệu, cấu trúc điều khiển → Checkpoint: viết chương trình tính tiền điện đơn giản\nTuần 3-4: Cấu trúc dữ liệu (list, dict), hàm, xử lý file → Checkpoint: quản lý danh sách chi tiêu bằng file text\nTuần 5-6: Lập trình hướng đối tượng cơ bản → Checkpoint: chuyển chương trình chi tiêu sang dùng class\nTuần 7-8: Ghép nối thành project hoàn chỉnh → Checkpoint: hoàn thành app quản lý chi tiêu cá nhân chạy được từ đầu đến cuối",
            },
        },
    },
    {
        "id": "study-8",
        "level": "study",
        "title": "Kỹ thuật Socratic: bắt AI hỏi ngược thay vì trả lời thẳng",
        "summary": "Buộc bản thân tự tư duy ra đáp án thay vì nhận câu trả lời có sẵn.",
        "content": """## Nguyên tắc

Khi AI trả lời thẳng mọi câu hỏi, bạn học được đáp án nhưng không luyện được **quá trình tư duy** để tự ra đáp án đó. Phương pháp Socratic đảo ngược vai trò: AI chỉ đặt câu hỏi dẫn dắt, còn bạn phải tự suy luận ra câu trả lời.

## Prompt mẫu

```
Tôi đang học về [chủ đề/bài toán]. Đừng đưa ra đáp án hay lời giải
trực tiếp, kể cả khi tôi có vẻ bế tắc.

Thay vào đó, hãy đặt từng câu hỏi dẫn dắt (mỗi lần một câu) để tôi
tự suy luận ra câu trả lời. Chỉ xác nhận đúng/sai sau khi tôi trả
lời câu hỏi dẫn dắt, rồi mới đặt câu hỏi tiếp theo.

Nếu tôi thực sự bế tắc sau 2-3 lần thử, hãy cho một gợi ý nhỏ (không
phải đáp án) trước khi hỏi tiếp.

Vấn đề tôi đang gặp: [mô tả vấn đề/bài toán]
```

## Thử trực tiếp: hỏi thẳng so với dùng prompt Socratic

{{PROMPT_LAB}}

> 💡 Kỹ thuật này đặc biệt hiệu quả khi debug code hoặc giải bài tập — bạn nhớ lâu hơn nhiều so với việc được đưa đáp án ngay.""",
        "prompt_lab": {
            "bad": {
                "label": "Hỏi thẳng",
                "prompt": "Tại sao code của tôi bị lỗi 'index out of range'?",
                "reply": "Lỗi 'index out of range' xảy ra khi bạn truy cập một chỉ số (index) vượt quá phạm vi hợp lệ của mảng. Nguyên nhân phổ biến nhất là vòng lặp chạy đến đúng độ dài của mảng thay vì độ dài trừ 1 (vì index bắt đầu từ 0). Hãy kiểm tra lại điều kiện dừng của vòng lặp, ví dụ dùng range(len(arr)) thay vì range(len(arr) + 1).",
            },
            "good": {
                "label": "Dùng prompt Socratic",
                "prompt": "Tôi đang gặp lỗi 'index out of range'. Đừng đưa đáp án trực tiếp — hãy đặt từng câu hỏi dẫn dắt (mỗi lần một câu) để tôi tự suy luận ra nguyên nhân.\n\nVấn đề: code của tôi bị lỗi 'index out of range' khi lặp qua một mảng.",
                "reply": "Bạn nghĩ vòng lặp của bạn đang chạy từ giá trị nào đến giá trị nào? Và mảng của bạn có bao nhiêu phần tử tất cả?",
            },
        },
    },
    {
        "id": "study-9",
        "level": "study",
        "title": "Bóc tách nhanh một bài báo khoa học hoặc tài liệu dài",
        "summary": "Khung đọc có cấu trúc giúp nắm ý chính của tài liệu học thuật trong thời gian ngắn.",
        "content": """## Nguyên tắc

Tài liệu học thuật thường dài và dùng thuật ngữ chuyên ngành. Thay vì đọc tuyến tính từ đầu đến cuối, dùng một **khung câu hỏi cố định** để AI trích xuất đúng những phần quan trọng nhất trước, giúp bạn quyết định có cần đọc sâu toàn bộ hay không.

## Prompt mẫu

```
Đọc đoạn trích/tóm tắt tài liệu sau và trả lời theo đúng khung:

1. **Vấn đề**: tài liệu này giải quyết câu hỏi/vấn đề gì?
2. **Phương pháp**: họ tiếp cận vấn đề đó bằng cách nào?
3. **Kết quả chính**: phát hiện/kết luận quan trọng nhất là gì?
4. **Hạn chế**: tác giả (hoặc bạn nhận thấy) có hạn chế/giả định
   nào đáng lưu ý không?
5. **Vì sao nó quan trọng**: kết quả này có ứng dụng/ý nghĩa gì?

Nếu tài liệu không đề cập rõ mục nào, ghi "Không đề cập" — đừng bịa.

Tài liệu: [dán abstract hoặc đoạn trích vào đây]
```

## Thử trực tiếp: tóm tắt tự do so với khung 5 câu hỏi

{{PROMPT_LAB}}

> 💡 Chỉ dùng cách này để **quyết định có nên đọc sâu hay không** — với tài liệu quan trọng, vẫn nên tự đọc kỹ phần Kết quả và Phương pháp, không hoàn toàn dựa vào tóm tắt AI.""",
        "prompt_lab": {
            "bad": {
                "label": "Tóm tắt tự do",
                "prompt": "Tóm tắt bài báo này giúp tôi.\n\n[abstract về mô hình dự đoán thời tiết bằng AI]",
                "reply": "Bài báo trình bày một mô hình học sâu mới nhằm cải thiện độ chính xác trong dự báo thời tiết ngắn hạn. Nhóm nghiên cứu sử dụng dữ liệu vệ tinh kết hợp với mạng nơ-ron tích chập (CNN) để huấn luyện mô hình. Kết quả cho thấy mô hình mới hoạt động tốt hơn các phương pháp truyền thống, đặc biệt ở những khu vực có địa hình phức tạp.",
            },
            "good": {
                "label": "Dùng khung 5 câu hỏi",
                "prompt": "Đọc đoạn trích sau và trả lời theo khung: Vấn đề / Phương pháp / Kết quả chính / Hạn chế / Vì sao quan trọng. Ghi \"Không đề cập\" nếu thiếu thông tin.\n\n[abstract về mô hình dự đoán thời tiết bằng AI]",
                "reply": "1. Vấn đề: Dự báo thời tiết ngắn hạn (24 giờ) kém chính xác ở khu vực có địa hình phức tạp (núi, đồi).\n2. Phương pháp: Kết hợp dữ liệu ảnh vệ tinh với mạng nơ-ron tích chập (CNN) để huấn luyện mô hình dự đoán.\n3. Kết quả chính: Giảm 15% sai số dự báo so với mô hình số trị truyền thống, đặc biệt rõ ở vùng núi.\n4. Hạn chế: Chỉ được thử nghiệm trên dữ liệu của một khu vực địa lý; chưa rõ khả năng tổng quát hoá.\n5. Vì sao quan trọng: Có thể cải thiện hệ thống cảnh báo sớm lũ quét, sạt lở ở vùng núi.",
            },
        },
    },
    {
        "id": "study-10",
        "level": "study",
        "title": "Ranh giới cần biết: dùng AI hỗ trợ học mà không mất tư duy phản biện",
        "summary": "Những dấu hiệu cho biết bạn đang dùng AI để học, hay đang để AI học thay mình.",
        "content": """## Vấn đề

AI có thể trả lời gần như mọi câu hỏi ngay lập tức — điều này vừa là lợi thế, vừa là cái bẫy. Nếu luôn nhận đáp án có sẵn mà không tự tư duy trước, bạn sẽ **quen với cảm giác đã hiểu** trong khi thực chất chưa từng tự giải quyết vấn đề nào.

## Dấu hiệu cảnh báo (🚩) vs. cách dùng lành mạnh (✅)

| 🚩 Dấu hiệu đáng lo | ✅ Cách dùng lành mạnh hơn |
|---|---|
| Copy đề bài → dán nguyên câu trả lời AI, không đọc kỹ | Tự thử giải trước, chỉ hỏi AI khi thực sự bế tắc |
| Tin ngay số liệu/trích dẫn AI đưa ra | Luôn kiểm chứng số liệu quan trọng từ nguồn gốc |
| Dùng AI để "học thuộc" đáp án cho bài kiểm tra | Dùng AI để kiểm tra xem mình đã hiểu đúng chưa (xem bài *Kỹ thuật Feynman*, *Socratic*) |
| Không còn tự tóm tắt được bài học bằng lời riêng của mình | Sau khi hỏi AI, thử tự viết lại ý chính không nhìn màn hình |

## Nguyên tắc thực hành

1. **Luôn thử trước khi hỏi**: dành ít nhất vài phút tự suy nghĩ/thử giải trước khi hỏi AI — kể cả khi biết chắc mình sẽ hỏi.
2. **Hỏi AI kiểm tra, không hỏi AI làm hộ**: ưu tiên các prompt dạng "chấm điểm/chỉ lỗi/đặt câu hỏi" hơn là "giải hộ tôi".
3. **Xác minh, đừng tin tuyệt đối**: với số liệu, trích dẫn, sự kiện — luôn coi là "cần kiểm tra lại" chứ không phải "chắc chắn đúng" (xem lại bài *Giới hạn của LLM: Hallucination*).
4. **Tự kiểm tra định kỳ không có AI**: thỉnh thoảng làm bài tập/thi thử hoàn toàn không có AI hỗ trợ để biết thực lực của mình đến đâu.

> 💡 AI là công cụ luyện tập tốt nhất khi nó đóng vai **huấn luyện viên** (đặt câu hỏi, chỉ lỗi, phản biện) hơn là vai **người làm bài hộ**.""",
    },

    # ── Làm việc (work) ──────────────────────────────────────────
    {
        "id": "work-1",
        "level": "work",
        "title": "Viết email chuyên nghiệp nhanh và đúng giọng văn",
        "summary": "Biến vài gạch đầu dòng thành email hoàn chỉnh, đúng tông với người nhận.",
        "content": """## Nguyên tắc

Email công việc cần đúng 3 thứ: **đủ thông tin cần thiết, đúng giọng văn với đối tượng nhận (sếp/khách hàng/đồng nghiệp), và đủ ngắn gọn để người bận rộn đọc lướt vẫn hiểu**. Cách nhanh nhất: liệt kê ý chính dạng gạch đầu dòng, để AI viết thành email hoàn chỉnh theo đúng tông bạn cần.

## Prompt mẫu

```
Viết một email [tiếng Việt/tiếng Anh] gửi cho [đối tượng: sếp/khách
hàng/đồng nghiệp], với giọng văn [trang trọng/thân thiện/chuyên
nghiệp].

Mục đích email: [ví dụ: xin dời deadline / báo cáo tiến độ / từ
chối lịch sự một đề nghị]

Các ý cần có (giữ nguyên thứ tự):
- [ý 1]
- [ý 2]
- [ý 3]

Yêu cầu: dưới 150 từ, có câu mở đầu và kết thúc lịch sự, không
dùng ngôn ngữ sáo rỗng thừa thãi.
```

## Thử trực tiếp: yêu cầu mơ hồ so với yêu cầu đủ thông tin

{{PROMPT_LAB}}

> 💡 Với email nhạy cảm (từ chối, phàn nàn, xin lỗi), luôn tự đọc lại và chỉnh sửa trước khi gửi — đừng gửi thẳng bản AI viết.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu mơ hồ",
                "prompt": "Viết email xin dời deadline.",
                "reply": "Kính gửi Anh/Chị,\n\nEm viết email này để xin phép dời deadline cho dự án. Do một số vấn đề phát sinh, nhóm em cần thêm thời gian để hoàn thành đúng chất lượng.\n\nRất mong Anh/Chị xem xét và thông cảm.\n\nEm cảm ơn Anh/Chị.",
            },
            "good": {
                "label": "Yêu cầu đủ thông tin",
                "prompt": "Viết một email tiếng Việt gửi cho sếp, giọng văn chuyên nghiệp.\nMục đích: xin dời deadline dự án A thêm 3 ngày.\nCác ý cần có:\n- Lý do: đối tác chậm gửi dữ liệu đầu vào\n- Cam kết vẫn đảm bảo chất lượng bàn giao\nYêu cầu: dưới 150 từ, mở đầu và kết thúc lịch sự.",
                "reply": "Chào anh/chị [tên],\n\nEm viết email này để xin phép dời deadline bàn giao dự án A thêm 3 ngày, dự kiến hoàn thành vào [ngày]. Nguyên nhân là phía đối tác chưa gửi đủ dữ liệu đầu vào cần thiết, dù nhóm đã chủ động nhắc nhở từ tuần trước.\n\nEm cam kết vẫn đảm bảo chất lượng bàn giao như kế hoạch ban đầu. Rất mong anh/chị thông cảm và hỗ trợ.\n\nEm cảm ơn anh/chị.",
            },
        },
    },
    {
        "id": "work-2",
        "level": "work",
        "title": "Tóm tắt biên bản họp thành action items rõ ràng",
        "summary": "Chuyển ghi chú họp lộn xộn thành bảng việc cần làm, người phụ trách, hạn chót.",
        "content": """## Nguyên tắc

Một cuộc họp chỉ thực sự có giá trị nếu kết thúc bằng **hành động cụ thể**. Ghi chú họp thường rời rạc, lộn xộn theo dòng chảy hội thoại — AI có thể giúp trích xuất lại thành bảng hành động rõ ràng ngay sau khi họp, trong lúc thông tin còn mới.

## Prompt mẫu

```
Đây là ghi chú/transcript cuộc họp. Hãy trích xuất thành bảng:

| Việc cần làm | Người phụ trách | Hạn chót | Mức độ ưu tiên |

Yêu cầu:
- Chỉ liệt kê việc THỰC SỰ được thống nhất cần làm, không liệt kê
  các ý chỉ được "nhắc tới" nhưng chưa chốt.
- Nếu ghi chú không nêu rõ người phụ trách/hạn chót, ghi "Chưa rõ —
  cần xác nhận lại" thay vì tự đoán.
- Sau bảng, viết thêm mục "Các quyết định đã chốt" (nếu có) và
  "Vấn đề còn bỏ ngỏ, cần họp lại" (nếu có).

Ghi chú họp: [dán nội dung vào đây]
```

## Thử trực tiếp: tóm tắt thường so với trích xuất action items

{{PROMPT_LAB}}

> 💡 Gửi ngay bảng này vào nhóm chat sau họp — càng sớm càng giảm khả năng "quên" việc đã thống nhất.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu tóm tắt thường",
                "prompt": "Tóm tắt cuộc họp này giúp tôi.\n\n[ghi chú họp về ra mắt tính năng thanh toán mới]",
                "reply": "Cuộc họp bàn về kế hoạch ra mắt tính năng thanh toán mới. Các bên đã thảo luận về việc hoàn thiện thiết kế giao diện, kiểm thử luồng thanh toán, và phân bổ ngân sách quảng cáo cho đợt ra mắt. Nhìn chung, nhóm đang trong giai đoạn chuẩn bị cuối cùng trước khi ra mắt chính thức.",
            },
            "good": {
                "label": "Dùng prompt trích xuất action items",
                "prompt": "Đây là ghi chú cuộc họp. Hãy trích xuất thành bảng: Việc cần làm | Người phụ trách | Hạn chót | Ưu tiên. Chỉ liệt kê việc THỰC SỰ được thống nhất.\n\nGhi chú: [về ra mắt tính năng thanh toán mới]",
                "reply": "Việc cần làm → Người phụ trách → Hạn chót → Ưu tiên\nHoàn thiện thiết kế UI màn hình thanh toán → Lan → Thứ Sáu tuần này → Cao\nViết test case cho luồng thanh toán → Chưa rõ — cần xác nhận lại → — → Trung bình\nChốt ngân sách quảng cáo đợt ra mắt → Chưa rõ — cần xác nhận lại → — → Cao\n\nCác quyết định đã chốt: ra mắt tính năng thanh toán vào cuối tháng.\nVấn đề còn bỏ ngỏ: chưa thống nhất được ngân sách quảng cáo cụ thể.",
            },
        },
    },
    {
        "id": "work-3",
        "level": "work",
        "title": "Mô tả bug hiệu quả để AI debug chính xác hơn",
        "summary": "Chất lượng câu trả lời debug phụ thuộc gần như hoàn toàn vào chất lượng mô tả bug của bạn.",
        "content": """## Nguyên tắc

AI không "thấy" được màn hình, log, hay môi trường chạy của bạn — nó chỉ có đúng những gì bạn gõ ra. Mô tả mơ hồ ("code tôi bị lỗi") buộc AI phải đoán, dẫn đến gợi ý sai hướng. Một mô tả bug tốt cần: **ngữ cảnh (ngôn ngữ/framework/phiên bản), đoạn code liên quan, thông báo lỗi đầy đủ, và những gì bạn đã thử**.

## Prompt mẫu

```
Tôi gặp lỗi khi chạy code sau.

Ngôn ngữ/Framework: [ví dụ: Python 3.11, FastAPI]
Mục tiêu đoạn code: [nó nên làm gì]
Đoạn code liên quan:
[dán code — chỉ phần liên quan, không dán cả file nếu không cần]

Thông báo lỗi đầy đủ (traceback/log):
[dán nguyên văn lỗi, không tóm tắt lại]

Tôi đã thử: [những gì bạn đã kiểm tra/thử sửa]

Hãy chỉ ra nguyên nhân có khả năng cao nhất trước, kèm cách sửa.
```

## Thử trực tiếp: mô tả mơ hồ so với mô tả đầy đủ

{{PROMPT_LAB}}

> 💡 Luôn dán **nguyên văn** thông báo lỗi, đừng diễn giải lại bằng lời của bạn — nhiều chi tiết quan trọng (tên exception, số dòng) dễ bị mất khi tóm tắt.""",
        "prompt_lab": {
            "bad": {
                "label": "Mô tả mơ hồ",
                "prompt": "API của tôi trả về lỗi 500, không biết tại sao.",
                "reply": "Lỗi 500 (Internal Server Error) có thể do nhiều nguyên nhân khác nhau, ví dụ:\n\n- Lỗi trong code xử lý request (exception không được bắt)\n- Kết nối database bị gián đoạn\n- Thiếu biến môi trường hoặc cấu hình sai\n- Dữ liệu đầu vào không hợp lệ mà code không kiểm tra trước\n\nBạn có thể kiểm tra log server để xem thông báo lỗi cụ thể, hoặc cho tôi biết thêm chi tiết (đoạn code, traceback) để tôi hỗ trợ chính xác hơn.",
            },
            "good": {
                "label": "Mô tả đầy đủ",
                "prompt": "Ngôn ngữ/Framework: Python 3.11, FastAPI\nEndpoint POST /users trả lỗi 500 khi tạo user mới.\n\nĐoạn code liên quan:\ndef create_user(data: dict):\n    return db.save(user_id=data['user_id'], name=data['name'])\n\nTraceback:\nKeyError: 'user_id'\n  File \"main.py\", line 42, in create_user\n\nTôi đã thử: log request body, thấy một số request gửi lên thiếu field user_id.",
                "reply": "Nguyên nhân: bạn truy cập data['user_id'] trực tiếp mà không kiểm tra field có tồn tại — khi client gửi thiếu field này, Python raise KeyError và FastAPI trả về lỗi 500 thay vì một lỗi validation rõ ràng.\n\nCách sửa: dùng data.get('user_id') rồi validate, hoặc định nghĩa Pydantic model có user_id: str bắt buộc — FastAPI sẽ tự trả lỗi 422 rõ ràng thay vì crash.",
            },
        },
    },
    {
        "id": "work-4",
        "level": "work",
        "title": "Nhờ AI review code: xin đúng loại phản hồi bạn cần",
        "summary": "Chỉ định rõ góc nhìn review (đúng đắn, hiệu năng, bảo mật...) để tránh phản hồi lan man.",
        "content": """## Nguyên tắc

"Review giúp tôi đoạn code này" là yêu cầu quá rộng — AI có thể trả lời lan man, bỏ sót đúng thứ bạn quan tâm nhất. Code review có nhiều **góc nhìn khác nhau**: tính đúng đắn, hiệu năng, khả năng đọc/bảo trì, bảo mật... nên chỉ định rõ góc nhìn cần tập trung.

## Prompt mẫu

```
Review đoạn code sau, chỉ tập trung vào các góc độ sau (bỏ qua các
góc độ khác trừ khi có vấn đề nghiêm trọng):
- [ ] Tính đúng đắn (có bug logic không)
- [ ] Hiệu năng (có chỗ nào không cần thiết tốn tài nguyên)
- [ ] Bảo mật (injection, validate input...)
- [ ] Khả năng đọc/đặt tên biến, hàm

Với mỗi vấn đề tìm được, nêu: dòng nào, vấn đề gì, và đề xuất sửa
cụ thể (không chỉ nói chung chung "nên cải thiện").

Ngôn ngữ: [ngôn ngữ lập trình]
Code:
[dán code]
```

## Thử trực tiếp: review chung chung so với chỉ định rõ góc nhìn

{{PROMPT_LAB}}

> 💡 Với code liên quan bảo mật/dữ liệu nhạy cảm, luôn coi gợi ý AI là điểm khởi đầu để kiểm tra kỹ hơn, không phải kết luận cuối cùng.""",
        "prompt_lab": {
            "bad": {
                "label": "Review chung chung",
                "prompt": "Review giúp tôi đoạn code này.\n\ndef get_user(request):\n    id = request.args['id']\n    query = f\"SELECT * FROM users WHERE id = {id}\"\n    return db.execute(query)",
                "reply": "Đoạn code khá đơn giản và dễ hiểu. Một vài gợi ý nhỏ:\n\n- Có thể đặt tên biến `id` rõ ràng hơn, ví dụ `user_id`, để tránh nhầm với hàm `id()` có sẵn của Python.\n- Nên thêm docstring mô tả hàm này làm gì.\n- Xem xét thêm xử lý khi request.args['id'] không tồn tại, để tránh lỗi KeyError.\n\nNhìn chung logic khá ổn.",
            },
            "good": {
                "label": "Chỉ định rõ: review Bảo mật",
                "prompt": "Review đoạn code sau, CHỈ tập trung vào Bảo mật (injection, validate input...). Nêu rõ dòng nào, vấn đề gì, đề xuất sửa cụ thể.\n\ndef get_user(request):\n    id = request.args['id']\n    query = f\"SELECT * FROM users WHERE id = {id}\"\n    return db.execute(query)",
                "reply": "Dòng 3: Query SQL được ghép chuỗi trực tiếp từ request.args['id'] → nguy cơ SQL Injection nghiêm trọng.\n\nĐề xuất: dùng parameterized query — db.execute(\"SELECT * FROM users WHERE id = %s\", (id,)) thay vì f-string.",
            },
        },
    },
    {
        "id": "work-5",
        "level": "work",
        "title": "Biến code thành tài liệu kỹ thuật (docs) tự động",
        "summary": "Sinh docstring/README theo đúng khung hợp đồng: input, output, ca lỗi.",
        "content": """## Nguyên tắc

Tài liệu kỹ thuật tốt cho một hàm/API cần trả lời đủ 3 câu hỏi: **nhận vào gì (input), trả về gì (output), và điều gì xảy ra khi có lỗi (ca lỗi)**. Đây cũng chính là "hợp đồng" (contract) mà người khác dựa vào để gọi đúng, không cần đọc source code.

## Prompt mẫu

```
Viết tài liệu kỹ thuật cho hàm/API sau, theo đúng khung:

- **Mục đích**: hàm này dùng để làm gì (1-2 câu)
- **Input**: tên tham số, kiểu dữ liệu, có bắt buộc không, ràng buộc
  (nếu có)
- **Output**: kiểu dữ liệu trả về, ý nghĩa
- **Ca lỗi**: các trường hợp có thể raise exception / trả mã lỗi,
  và điều kiện gây ra nó

Viết dạng docstring theo chuẩn [Google style / JSDoc / ...] phù hợp
với ngôn ngữ, không cần diễn giải thêm ngoài khung trên.

Code: [dán hàm/API cần viết docs]
```

## Thử trực tiếp: yêu cầu docs chung chung so với dùng khung hợp đồng

{{PROMPT_LAB}}

> 💡 Sau khi AI sinh docs, luôn đối chiếu lại với code thật — đảm bảo AI không "đoán" thêm ca lỗi không tồn tại hoặc bỏ sót ca lỗi thật sự có trong code.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu docs chung chung",
                "prompt": "Viết docs cho hàm này giúp tôi.\n\ndef create_user(email: str, password: str) -> User:\n    ...",
                "reply": "'''Tạo người dùng mới.\n\nArgs:\n    email: Email người dùng.\n    password: Mật khẩu.\n\nReturns:\n    Đối tượng User vừa tạo.\n'''",
            },
            "good": {
                "label": "Dùng khung hợp đồng đầy đủ",
                "prompt": "Viết tài liệu kỹ thuật cho hàm sau theo khung: Mục đích / Input (kiểu, bắt buộc, ràng buộc) / Output / Ca lỗi (exception, điều kiện gây ra).\n\ndef create_user(email: str, password: str) -> User:\n    ...",
                "reply": "'''Tạo người dùng mới trong hệ thống.\n\nArgs:\n    email (str): Email người dùng, bắt buộc, phải đúng định dạng email hợp lệ.\n    password (str): Mật khẩu, bắt buộc, tối thiểu 8 ký tự.\n\nReturns:\n    User: Đối tượng người dùng vừa được tạo, gồm id và email.\n\nRaises:\n    ValueError: Nếu email đã tồn tại trong hệ thống.\n    ValidationError: Nếu email sai định dạng hoặc password ngắn hơn 8 ký tự.\n'''",
            },
        },
    },
    {
        "id": "work-6",
        "level": "work",
        "title": "Lên dàn ý bài thuyết trình từ ý tưởng còn thô",
        "summary": "Chuyển một ý tưởng lộn xộn trong đầu thành outline slide có thông điệp rõ ràng từng trang.",
        "content": """## Nguyên tắc

Sai lầm phổ biến khi làm slide: nhồi quá nhiều thông tin vào một slide, hoặc không có "thông điệp chính" rõ ràng cho từng trang. Một outline tốt cần xác định trước: **đối tượng nghe, thời lượng, và đúng một thông điệp chính cho mỗi slide** trước khi bắt tay vào thiết kế.

## Prompt mẫu

```
Tôi cần thuyết trình về [chủ đề] cho [đối tượng nghe], thời lượng
khoảng [số phút], mục tiêu là [ví dụ: thuyết phục đầu tư / báo cáo
kết quả / đào tạo nội bộ].

Hãy lên outline gồm [số lượng] slide, mỗi slide gồm:
- Tiêu đề slide
- Thông điệp chính (1 câu — đây là điều khán giả PHẢI nhớ từ slide này)
- 2-3 gạch đầu dòng nội dung hỗ trợ thông điệp đó
- Gợi ý loại minh hoạ phù hợp (biểu đồ/ảnh/ví dụ — không cần tạo hình thật)

Slide đầu là mở đầu gây chú ý, slide cuối là kêu gọi hành động rõ ràng.
```

## Thử trực tiếp: yêu cầu thiếu bối cảnh so với đủ bối cảnh

{{PROMPT_LAB}}

> 💡 Nếu một slide không có nổi "một thông điệp chính" rõ ràng — đó là dấu hiệu nên tách thành 2 slide hoặc bỏ bớt nội dung.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu thiếu bối cảnh",
                "prompt": "Giúp tôi làm outline slide thuyết trình về sản phẩm mới.",
                "reply": "Đây là outline gợi ý cho slide thuyết trình sản phẩm mới:\n\n1. Giới thiệu công ty\n2. Vấn đề mà khách hàng đang gặp phải\n3. Giới thiệu sản phẩm/giải pháp\n4. Tính năng nổi bật\n5. Lộ trình triển khai\n6. Lời cảm ơn / Q&A\n\nBạn có thể cho tôi biết thêm về đối tượng nghe và thời lượng để tôi tinh chỉnh outline phù hợp hơn.",
            },
            "good": {
                "label": "Yêu cầu đủ bối cảnh",
                "prompt": "Tôi cần thuyết trình về tính năng phản hồi khách hàng tự động cho ban giám đốc, thời lượng 10 phút, mục tiêu thuyết phục đầu tư.\n\nHãy lên outline 6 slide, mỗi slide có tiêu đề, thông điệp chính (1 câu), 2-3 ý hỗ trợ.",
                "reply": "Slide 1: \"30% khách hàng rời bỏ vì thời gian phản hồi chậm\" — mở đầu bằng số liệu khảo sát gây chú ý ngay.\nSlide 2: \"Giải pháp X giảm thời gian phản hồi từ 2 ngày xuống 2 giờ\" — so sánh trước/sau bằng biểu đồ đơn giản.\nSlide 3: \"Cách hoạt động: AI phân loại và trả lời tự động 80% yêu cầu thường gặp\" — sơ đồ luồng xử lý.\nSlide 4: \"Đã thử nghiệm với 200 khách hàng, tỷ lệ hài lòng tăng 25%\" — dữ liệu pilot thực tế.\nSlide 5: \"Chi phí triển khai và thời gian hoàn vốn dự kiến 4 tháng\" — bảng chi phí/lợi ích.\nSlide 6: \"Cần duyệt ngân sách 500 triệu để triển khai toàn công ty trong Q3\" — lời kêu gọi hành động rõ ràng, có deadline quyết định.",
            },
        },
    },
    {
        "id": "work-7",
        "level": "work",
        "title": "Phân tích dữ liệu thô và viết tóm tắt insight cho sếp",
        "summary": "Từ bảng số liệu khô khan ra bản tóm tắt ngắn, đúng trọng tâm cho người bận rộn.",
        "content": """## Nguyên tắc

Người quản lý bận rộn cần **kết luận và hành động đề xuất**, không cần đọc toàn bộ bảng số liệu. Yêu cầu AI phân tích dữ liệu nên luôn kèm theo yêu cầu "vậy thì sao" (so what) — insight phải đi kèm ý nghĩa và đề xuất, không chỉ mô tả lại số liệu.

## Prompt mẫu

```
Đây là bảng dữ liệu [mô tả ngắn: doanh số theo tháng / khảo sát
khách hàng...]. Hãy phân tích và viết tóm tắt dạng "TL;DR cho người
bận rộn":

1. 3 insight nổi bật nhất (không liệt kê lại toàn bộ số liệu, chỉ
   nêu điều đáng chú ý nhất)
2. Với mỗi insight, nêu ý nghĩa: "điều này có nghĩa là..."
3. Đề xuất 1-2 hành động cụ thể nên cân nhắc

Giới hạn toàn bộ trong khoảng 150 từ.

Dữ liệu: [dán bảng số liệu — có thể dán trực tiếp dạng CSV/bảng]
```

## Thử trực tiếp: phân tích chung chung so với dùng prompt TL;DR

{{PROMPT_LAB}}

> 💡 Luôn tự kiểm tra lại các con số quan trọng AI trích ra — với dữ liệu lớn, AI có thể đọc nhầm hàng/cột hoặc tính sai phần trăm.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu phân tích chung chung",
                "prompt": "Phân tích bảng doanh số này giúp tôi.\n\n[bảng doanh số theo tháng]",
                "reply": "Nhìn vào bảng doanh số, có thể thấy doanh số có biến động qua các tháng. Một số tháng tăng, một số tháng giảm nhẹ. Nhìn chung xu hướng chưa thật rõ ràng, có thể cần thêm dữ liệu của các quý trước để so sánh và đưa ra nhận định chính xác hơn.",
            },
            "good": {
                "label": "Dùng prompt TL;DR",
                "prompt": "Đây là bảng doanh số theo tháng. Hãy phân tích và viết tóm tắt dạng TL;DR: 3 insight nổi bật, mỗi insight nêu ý nghĩa, và 1-2 đề xuất hành động. Giới hạn 150 từ.\n\nDữ liệu: [bảng doanh số theo tháng]",
                "reply": "Insight 1: Doanh số tháng 6 giảm 18% so với tháng 5, tập trung ở nhóm khách hàng mới.\n→ Có thể chiến dịch marketing thu hút khách mới đang kém hiệu quả, không phải vấn đề giữ chân khách cũ.\n\nInsight 2: Nhóm khách hàng quay lại (repeat customers) vẫn tăng đều 5%/tháng.\n→ Chất lượng sản phẩm ổn, vấn đề nằm ở khâu thu hút khách mới.\n\nĐề xuất: Kiểm tra lại hiệu suất từng kênh marketing trong tháng 6 trước khi cắt giảm ngân sách chung.",
            },
        },
    },
    {
        "id": "work-8",
        "level": "work",
        "title": "Dùng AI làm 'người phản biện khó tính' trước khi trình bày ý tưởng",
        "summary": "Tập dượt trước các câu hỏi hóc búa để không bị động khi trình bày thật.",
        "content": """## Nguyên tắc

Trước khi trình bày một ý tưởng/kế hoạch quan trọng, sẽ an toàn hơn nhiều nếu bạn tự tìm ra lỗ hổng trước — thay vì để người nghe thật phát hiện ra ngay tại chỗ. Cho AI đóng vai "devil's advocate" (người phản biện khó tính) giúp bạn tập dượt trước các câu hỏi/rủi ro có thể bị hỏi.

## Prompt mẫu

```
Tôi sắp trình bày ý tưởng/kế hoạch sau cho [đối tượng: ban giám
đốc/nhà đầu tư/khách hàng]:

[mô tả ý tưởng/kế hoạch của bạn]

Hãy đóng vai một người nghe khó tính, hoài nghi. Đặt ra:
1. 3-5 câu hỏi hóc búa nhất mà bạn nghĩ họ có thể hỏi
2. Với mỗi câu hỏi, chỉ rõ điểm yếu/rủi ro trong kế hoạch của tôi
   mà câu hỏi đó nhắm vào
3. Không cần trả lời hộ tôi — tôi sẽ tự chuẩn bị câu trả lời

Đừng khen ý tưởng, hãy tập trung tìm điểm yếu.
```

## Thử trực tiếp: hỏi xin nhận xét so với dùng prompt phản biện

{{PROMPT_LAB}}

> 💡 Sau khi nhận danh sách câu hỏi, tự viết câu trả lời cho từng câu — đây chính là phần chuẩn bị giá trị nhất, không phải danh sách câu hỏi.""",
        "prompt_lab": {
            "bad": {
                "label": "Hỏi xin nhận xét chung",
                "prompt": "Tôi định ra mắt tính năng mới trong 2 tháng. Ý tưởng này có ổn không?",
                "reply": "Nghe khá hợp lý! 2 tháng là khoảng thời gian phổ biến cho việc ra mắt một tính năng có quy mô vừa phải. Miễn là team đã có kế hoạch rõ ràng về các mốc thời gian và nguồn lực, tôi nghĩ kế hoạch này khả thi. Bạn có muốn tôi giúp lập chi tiết timeline không?",
            },
            "good": {
                "label": "Dùng prompt phản biện khó tính",
                "prompt": "Tôi sắp trình bày kế hoạch \"ra mắt tính năng mới trong 2 tháng\" cho ban giám đốc.\n\nHãy đóng vai người nghe khó tính, hoài nghi. Đặt ra 3-5 câu hỏi hóc búa nhất có thể bị hỏi, chỉ rõ điểm yếu mỗi câu nhắm vào. Đừng khen, đừng trả lời hộ.",
                "reply": "1. \"Nếu đối tác cung cấp dữ liệu chậm trễ như đợt trước, kế hoạch 2 tháng còn khả thi không? Phương án dự phòng là gì?\"\n2. \"Ngân sách marketing dựa trên giả định tỷ lệ chuyển đổi 5% — con số này lấy từ đâu, đủ tin cậy không?\"\n3. \"Nếu tính năng ra mắt nhưng tỷ lệ dùng thấp hơn kỳ vọng, tiêu chí nào để quyết định dừng hay tiếp tục đầu tư?\"",
            },
        },
    },
    {
        "id": "work-9",
        "level": "work",
        "title": "Xây dựng prompt template tái sử dụng cho việc lặp lại",
        "summary": "Đừng viết lại prompt từ đầu mỗi lần — biến nó thành một template có biến số.",
        "content": """## Nguyên tắc

Nếu một loại yêu cầu (viết mô tả sản phẩm, trả lời khiếu nại khách hàng, tóm tắt CV ứng viên...) lặp lại thường xuyên, việc viết lại prompt từ đầu mỗi lần vừa tốn thời gian, vừa dễ ra kết quả không nhất quán. Giải pháp: xây dựng **một prompt template cố định với các biến số (placeholder)**, chỉ cần điền thông tin mới mỗi lần dùng.

Đây cũng chính là ý tưởng đằng sau tính năng "Custom Agent" (system prompt cố định) trong không gian Thực hành của ứng dụng này.

## Cách xây dựng template

```
[VAI TRÒ CỐ ĐỊNH — không đổi mỗi lần dùng]
Bạn là [vai trò chuyên môn cụ thể].

[NHIỆM VỤ CỐ ĐỊNH]
Nhiệm vụ của bạn là [mô tả việc lặp lại].

[ĐỊNH DẠNG ĐẦU RA CỐ ĐỊNH]
Luôn trả lời theo cấu trúc:
- [phần 1]
- [phần 2]

[BIẾN SỐ — thay đổi mỗi lần dùng]
Thông tin đầu vào lần này: {{input}}
```

## Thử trực tiếp: viết lại từ đầu so với dùng template có sẵn

{{PROMPT_LAB}}

Mỗi lần có sản phẩm mới, chỉ cần thay phần biến số — không cần viết lại toàn bộ hướng dẫn phong cách.

> 💡 Lưu các template này lại (ví dụ làm Custom Agent trong ứng dụng) thay vì gõ lại từ đầu mỗi lần — tiết kiệm thời gian và giữ output nhất quán.""",
        "prompt_lab": {
            "bad": {
                "label": "Viết lại từ đầu mỗi lần",
                "prompt": "Viết mô tả sản phẩm cho áo thun cotton, giá 199k.",
                "reply": "Áo thun cotton 100%, thiết kế basic dễ mặc, phù hợp cho mọi hoạt động hàng ngày. Chất liệu thoáng mát, thấm hút mồ hôi tốt. Giá chỉ 199.000đ — lựa chọn hợp lý cho tủ đồ của bạn.",
            },
            "good": {
                "label": "Dùng template có sẵn",
                "prompt": "Bạn là copywriter chuyên viết mô tả sản phẩm thương mại điện tử, giọng văn gần gũi. Luôn viết theo cấu trúc: (1) câu mở đầu gây chú ý, (2) 3 lợi ích chính, (3) câu kêu gọi hành động.\n\nSản phẩm lần này: Áo thun cotton, thoáng mát, giá 199k.",
                "reply": "Ngày hè mà thiếu chiếc áo thun này thì thật đáng tiếc!\n- Chất cotton 100%, thoáng mát cả ngày dài\n- Form dáng basic, phối đồ nào cũng hợp\n- Giá chỉ 199k — quá hời để có ngay vài chiếc\n\nĐặt ngay hôm nay để không bỏ lỡ!",
            },
        },
    },
    {
        "id": "work-10",
        "level": "work",
        "title": "Dùng AI làm trợ lý nghiên cứu nhanh về thị trường/đối thủ",
        "summary": "Tăng tốc bước tổng hợp ban đầu, nhưng luôn tự kiểm chứng số liệu quan trọng.",
        "content": """## Nguyên tắc

AI hữu ích để **tổng hợp nhanh khung phân tích ban đầu** (đối thủ cần xem xét khía cạnh nào, câu hỏi cần trả lời là gì) — nhưng có rủi ro lớn: AI có thể **hallucinate số liệu thị trường, thị phần, hoặc thông tin đối thủ** nghe rất thuyết phục nhưng sai hoặc đã lỗi thời (xem lại bài *Giới hạn của LLM*). Luôn tách rõ "khung phân tích" (AI làm tốt) và "số liệu cụ thể" (bắt buộc tự kiểm chứng).

## Prompt mẫu

```
Tôi đang phân tích đối thủ cạnh tranh trong ngành [ngành].
Đối thủ chính: [tên đối thủ, nếu biết].

Hãy giúp tôi lập khung phân tích SWOT gồm các câu hỏi cụ thể cần
trả lời cho từng mục (Điểm mạnh/Điểm yếu/Cơ hội/Thách thức) — dựa
trên đặc thù ngành [ngành], không cần điền số liệu cụ thể.

Sau đó gợi ý 3-5 nguồn thông tin loại nào (không cần link cụ thể)
đáng tin cậy để tôi tự tra cứu số liệu thật.
```

## Thử trực tiếp: hỏi thẳng số liệu so với chỉ hỏi khung phân tích

{{PROMPT_LAB}}

> 🚩 **Luôn tự kiểm chứng**: bất kỳ con số cụ thể nào (thị phần %, doanh thu, số lượng khách hàng) do AI đưa ra mà không trích nguồn rõ ràng — coi như chưa được xác minh, không đưa thẳng vào báo cáo chính thức.""",
        "prompt_lab": {
            "bad": {
                "label": "Hỏi thẳng số liệu cụ thể",
                "prompt": "Thị phần của đối thủ X trong ngành F&B tại Việt Nam là bao nhiêu?",
                "reply": "Theo một số báo cáo ngành, đối thủ X hiện chiếm khoảng 18-22% thị phần trong phân khúc F&B tại các thành phố lớn của Việt Nam, là một trong những thương hiệu dẫn đầu ở phân khúc này.",
            },
            "good": {
                "label": "Chỉ hỏi khung phân tích",
                "prompt": "Tôi đang phân tích đối thủ X trong ngành F&B. Hãy giúp tôi lập khung phân tích SWOT gồm các câu hỏi cụ thể cần trả lời (không cần điền số liệu), rồi gợi ý loại nguồn đáng tin cậy để tôi tự tra cứu số liệu thật.",
                "reply": "Điểm mạnh cần kiểm tra: đối thủ có lợi thế về vị trí cửa hàng, mức giá, hay độ nhận diện thương hiệu không?\nĐiểm yếu cần kiểm tra: đánh giá khách hàng trên Google/app đặt đồ ăn có điểm chung nào bị phàn nàn không?\nCơ hội cần kiểm tra: có phân khúc khách hàng hoặc khu vực nào đối thủ chưa phục vụ tốt?\n\nNguồn nên tra cứu thật: báo cáo ngành từ đơn vị nghiên cứu thị trường uy tín, đánh giá công khai trên Google Maps/app đặt đồ ăn, báo cáo tài chính công khai (nếu là công ty niêm yết).",
            },
        },
    },

    # ── Lên kế hoạch (planning) ──────────────────────────────────
    {
        "id": "planning-1",
        "level": "planning",
        "title": "Lập kế hoạch dự án theo mốc thời gian (milestones)",
        "summary": "Chia mục tiêu lớn với deadline cố định thành các mốc kiểm tra trung gian.",
        "content": """## Nguyên tắc

Một deadline duy nhất ở cuối dự án dễ khiến tiến độ "trông ổn" cho đến sát ngày mới phát hiện trễ. Chia dự án thành các **milestone** (mốc kiểm tra trung gian, có sản phẩm/kết quả cụ thể) giúp phát hiện sớm nếu bị chậm, còn kịp điều chỉnh.

## Prompt mẫu

```
Tôi có dự án: [mô tả mục tiêu cuối], deadline tổng: [ngày].
Nguồn lực: [số người / vai trò tham gia, nếu có].

Hãy chia thành các milestone, mỗi milestone gồm:
- Tên milestone
- Ngày dự kiến hoàn thành
- "Bằng chứng hoàn thành" cụ thể (kết quả đầu ra rõ ràng, không mơ hồ)
- Rủi ro chính có thể khiến milestone này bị trễ

Milestone cuối cùng phải trùng với deadline tổng.
```

## Thử trực tiếp: yêu cầu thiếu cấu trúc so với dùng prompt milestone

{{PROMPT_LAB}}

> 💡 Sau mỗi milestone, dành 15 phút nhìn lại: đúng tiến độ hay không, nếu trễ thì điều chỉnh milestone tiếp theo ngay, đừng đợi đến cuối dự án mới xử lý.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu thiếu cấu trúc",
                "prompt": "Tôi có dự án ra mắt website mới, deadline 6 tuần. Giúp tôi lập kế hoạch.",
                "reply": "Bạn có thể chia dự án thành các giai đoạn: thiết kế, phát triển, kiểm thử, và ra mắt. Nên dành đủ thời gian cho từng giai đoạn và thường xuyên theo dõi tiến độ để đảm bảo hoàn thành đúng hạn trong 6 tuần.",
            },
            "good": {
                "label": "Dùng prompt milestone",
                "prompt": "Tôi có dự án: ra mắt website mới, deadline tổng: 6 tuần.\nNguồn lực: 1 designer, 2 developer.\n\nHãy chia thành milestone, mỗi milestone gồm tên, ngày dự kiến, bằng chứng hoàn thành cụ thể, rủi ro chính.",
                "reply": "Chốt thiết kế UI/UX → Tuần 2 → File thiết kế được duyệt bởi stakeholder → Rủi ro: chờ phản hồi duyệt kéo dài\nHoàn thành phát triển → Tuần 5 → Website chạy được trên staging → Rủi ro: phát sinh yêu cầu ngoài phạm vi\nRa mắt chính thức → Tuần 6 → Website live trên domain thật → Rủi ro: lỗi phát sinh phút chót",
            },
        },
    },
    {
        "id": "planning-2",
        "level": "planning",
        "title": "Chia nhỏ mục tiêu mơ hồ thành hành động cụ thể (SMART)",
        "summary": "Biến 'tôi muốn khỏe hơn' thành mục tiêu đo lường được và các bước hành động rõ ràng.",
        "content": """## Nguyên tắc

Mục tiêu như "muốn khỏe hơn", "muốn giỏi tiếng Anh hơn" nghe hợp lý nhưng không thể hành động được — không biết bắt đầu từ đâu, không biết khi nào coi là đạt được. Khung **SMART** (Specific - Measurable - Achievable - Relevant - Time-bound) ép mục tiêu trở nên cụ thể và đo lường được.

## Prompt mẫu

```
Mục tiêu hiện tại của tôi (còn mơ hồ): "[mục tiêu mơ hồ]"
Bối cảnh: [thời gian có thể dành ra, ràng buộc hiện tại nếu có]

Hãy giúp tôi:
1. Biến mục tiêu trên thành 1 mục tiêu SMART cụ thể (nêu rõ từng
   yếu tố S-M-A-R-T tương ứng với mục tiêu đó)
2. Chia mục tiêu SMART đó thành 4-6 bước hành động cụ thể, mỗi bước
   có thể bắt đầu làm ngay trong tuần này
```

## Thử trực tiếp: hỏi cộc lốc so với dùng prompt mẫu đầy đủ

{{PROMPT_LAB}}

## Ví dụ phân tích chi tiết

Mục tiêu mơ hồ: "Tôi muốn khỏe hơn."

→ Mục tiêu SMART: "Chạy bộ được liên tục 5km trong 8 tuần tới, tập tối thiểu 3 buổi/tuần."
- **Specific**: chạy bộ, cự ly 5km cụ thể
- **Measurable**: đo được bằng quãng đường/thời gian chạy
- **Achievable**: hợp lý nếu hiện tại đã chạy được 2-3km
- **Relevant**: gắn với mục tiêu "khỏe hơn"
- **Time-bound**: 8 tuần

Các bước hành động: Tuần 1-2 chạy 2km x 3 buổi/tuần → Tuần 3-4 tăng lên 3km → ... → Tuần 8 đạt 5km liên tục.

> 💡 Nếu bước hành động đầu tiên vẫn cảm thấy "khó bắt đầu ngay hôm nay", hãy yêu cầu AI chia nhỏ tiếp bước đó — dấu hiệu nó vẫn chưa đủ cụ thể.""",
        "prompt_lab": {
            "bad": {
                "label": "Hỏi cộc lốc",
                "prompt": "Tôi muốn khỏe hơn. Giúp tôi lập kế hoạch.",
                "reply": "Để khỏe hơn, bạn nên: ăn uống lành mạnh, tập thể dục đều đặn, ngủ đủ giấc, uống đủ nước, và hạn chế căng thẳng. Duy trì những thói quen này đều đặn sẽ giúp bạn cải thiện sức khỏe theo thời gian.",
            },
            "good": {
                "label": "Dùng prompt mẫu",
                "prompt": "Mục tiêu hiện tại của tôi (còn mơ hồ): \"Tôi muốn khỏe hơn.\"\nBối cảnh: hiện tại chạy được 2-3km, có thể tập 3 buổi/tuần.\n\nHãy giúp tôi:\n1. Biến mục tiêu trên thành 1 mục tiêu SMART cụ thể\n2. Chia thành 4-6 bước hành động, bắt đầu được ngay tuần này",
                "reply": "Mục tiêu SMART: Chạy bộ liên tục 5km trong 8 tuần tới, tập tối thiểu 3 buổi/tuần.\n\nBước hành động:\nTuần 1-2: chạy 2km x 3 buổi/tuần\nTuần 3-4: tăng lên 3km\nTuần 5-6: tăng lên 4km\nTuần 7-8: đạt 5km liên tục",
            },
        },
    },
    {
        "id": "planning-3",
        "level": "planning",
        "title": "Tổ chức tài chính cá nhân cơ bản với sự hỗ trợ của AI",
        "summary": "Dùng AI để phân loại và tổ chức thu chi — không thay thế tư vấn tài chính chuyên nghiệp.",
        "content": """## ⚠️ Lưu ý quan trọng trước tiên

AI ở đây chỉ đóng vai trò **hỗ trợ tổ chức, phân loại số liệu thu chi cá nhân** — hoàn toàn không phải lời khuyên đầu tư hay tư vấn tài chính. Với các quyết định tài chính lớn (đầu tư, vay nợ, bảo hiểm...), luôn tham khảo chuyên gia tài chính được cấp phép.

## Nguyên tắc

Nguyên tắc phổ biến **50/30/20**: 50% thu nhập cho nhu cầu thiết yếu, 30% cho chi tiêu cá nhân/giải trí, 20% cho tiết kiệm/trả nợ. AI có thể giúp bạn phân loại chi tiêu thực tế theo khung này để thấy rõ mình đang lệch ở đâu.

## Prompt mẫu

```
Đây là danh sách chi tiêu tháng vừa rồi của tôi (thu nhập:
[số tiền]):

[dán danh sách chi tiêu: khoản mục - số tiền]

Hãy phân loại các khoản này vào 3 nhóm: Thiết yếu (nhà ở, ăn uống,
di chuyển, hoá đơn) / Cá nhân-giải trí / Tiết kiệm-trả nợ.
Tính tỷ lệ % mỗi nhóm so với thu nhập, so sánh với khung tham khảo
50/30/20, và chỉ ra nhóm nào đang lệch nhiều nhất.

Đây chỉ là công cụ tổ chức số liệu, không cần đưa ra lời khuyên đầu tư.
```

## Thử trực tiếp: hỏi không cấu trúc so với dùng khung 50/30/20

{{PROMPT_LAB}}

> 💡 Đây là công cụ giúp bạn **nhìn rõ số liệu**, quyết định cắt giảm/đầu tư khoản nào vẫn nên dựa trên hoàn cảnh thực tế và, nếu cần, ý kiến chuyên gia.""",
        "prompt_lab": {
            "bad": {
                "label": "Hỏi không có cấu trúc",
                "prompt": "Đây là chi tiêu tháng của tôi: tiền nhà 8tr, ăn uống 4tr, giải trí 6tr, tiết kiệm 2tr. Có ổn không?",
                "reply": "Chi tiêu của bạn nhìn khá hợp lý — bạn vẫn để ra được một phần cho tiết kiệm. Tuy nhiên, khoản giải trí 6 triệu có vẻ khá cao so với các khoản khác, bạn có thể xem xét cắt giảm nếu muốn tiết kiệm nhiều hơn.",
            },
            "good": {
                "label": "Dùng khung 50/30/20",
                "prompt": "Đây là danh sách chi tiêu tháng của tôi (thu nhập: 20.000.000đ): nhà ở 8tr, ăn uống 4tr, giải trí 6tr, tiết kiệm 2tr.\n\nHãy phân loại vào 3 nhóm Thiết yếu/Cá nhân-giải trí/Tiết kiệm, tính % so với thu nhập, so sánh khung 50/30/20, chỉ ra nhóm lệch nhiều nhất. Đây chỉ là công cụ tổ chức số liệu, không cần đưa lời khuyên đầu tư.",
                "reply": "Thiết yếu: 12tr (60%, khung 50%) — cao hơn 10%\nCá nhân/Giải trí: 6tr (30%, khung 30%) — đúng khung\nTiết kiệm: 2tr (10%, khung 20%) — thấp hơn 10%\n\nNhận xét: nhóm Thiết yếu đang cao hơn khung tham khảo, nhóm Tiết kiệm đang thấp hơn — có thể xem lại các khoản thiết yếu.",
            },
        },
    },
    {
        "id": "planning-4",
        "level": "planning",
        "title": "Lên kế hoạch du lịch chi tiết theo ngân sách và sở thích",
        "summary": "Từ điểm đến và ngân sách, tạo lịch trình theo ngày thay vì tìm kiếm rời rạc từng phần.",
        "content": """## Nguyên tắc

Lên kế hoạch du lịch thường bị rời rạc: tìm chỗ ở riêng, tìm điểm tham quan riêng, tính chi phí riêng — dễ bỏ sót hoặc trùng lặp. Cung cấp đủ ràng buộc (ngân sách, số ngày, sở thích) trong một lần giúp AI tạo lịch trình khớp nhau theo ngày.

## Prompt mẫu

```
Lên kế hoạch du lịch [điểm đến] trong [số ngày] ngày cho [số người].
Ngân sách khoảng [số tiền] (không tính vé máy bay).
Sở thích: [ví dụ: thích ẩm thực địa phương, không thích đi bộ nhiều,
đi cùng trẻ nhỏ...]

Hãy lên lịch trình theo từng ngày, mỗi ngày gồm: buổi sáng/chiều/tối
làm gì, ước tính chi phí mỗi hoạt động, và tổng chi phí ước tính cả
chuyến (không tính vé máy bay).

Ghi rõ đây là ước tính tham khảo, giá thực tế có thể thay đổi.
```

## Thử trực tiếp: yêu cầu thiếu chi tiết so với đủ ràng buộc

{{PROMPT_LAB}}

> 💡 Giá cả, giờ mở cửa AI đưa ra có thể đã lỗi thời — luôn kiểm tra lại thông tin quan trọng (giờ mở cửa, giá vé) trước khi khởi hành, đặc biệt với các địa điểm có thể đã thay đổi.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu thiếu chi tiết",
                "prompt": "Lên kế hoạch đi Đà Lạt 3 ngày giúp tôi.",
                "reply": "Ngày 1: tham quan trung tâm thành phố. Ngày 2: đi các điểm du lịch nổi tiếng. Ngày 3: mua sắm và về.\n\nBạn có thể cho tôi biết thêm về ngân sách và sở thích để tôi gợi ý địa điểm cụ thể hơn.",
            },
            "good": {
                "label": "Yêu cầu đủ ràng buộc",
                "prompt": "Lên kế hoạch du lịch Đà Lạt trong 3 ngày cho 2 người.\nNgân sách khoảng 6 triệu (không tính vé máy bay).\nSở thích: thích ẩm thực địa phương.\n\nLên lịch trình theo ngày, ước tính chi phí mỗi hoạt động và tổng chi phí.",
                "reply": "Ngày 1: Nhận phòng, chợ Đà Lạt (sáng) → Hồ Xuân Hương (chiều) → Lẩu bò, chợ đêm (tối) — ~500.000đ\nNgày 2: Đồi chè Cầu Đất → Thung lũng Tình Yêu → Nhà hàng đặc sản — ~800.000đ\nNgày 3: Mua đặc sản → Trả phòng, ra sân bay — ~300.000đ\n\n(Ước tính tham khảo, giá thực tế có thể thay đổi)",
            },
        },
    },
    {
        "id": "planning-5",
        "level": "planning",
        "title": "Quản lý ưu tiên công việc với Ma trận Eisenhower",
        "summary": "Phân loại việc cần làm theo 2 trục Khẩn cấp/Quan trọng để biết nên làm gì trước.",
        "content": """## Nguyên tắc

Không phải việc nào "gấp" cũng "quan trọng", và ngược lại. Ma trận Eisenhower chia công việc theo 2 trục thành 4 nhóm, giúp quyết định: **làm ngay, lên lịch làm sau, giao cho người khác, hay loại bỏ**.

<div class="curriculum-diagram">
<svg viewBox="0 0 420 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ma trận Eisenhower 4 ô: Khẩn cấp/Không khẩn cấp x Quan trọng/Không quan trọng">
  <line x1="210" y1="20" x2="210" y2="400" stroke="#9ca3af" stroke-width="2"/>
  <line x1="20" y1="210" x2="400" y2="210" stroke="#9ca3af" stroke-width="2"/>
  <text x="115" y="14" text-anchor="middle" font-size="11" fill="#6b7280">Khẩn cấp</text>
  <text x="305" y="14" text-anchor="middle" font-size="11" fill="#6b7280">Không khẩn cấp</text>
  <text x="12" y="115" text-anchor="middle" font-size="11" fill="#6b7280" transform="rotate(-90 12 115)">Quan trọng</text>
  <text x="12" y="305" text-anchor="middle" font-size="11" fill="#6b7280" transform="rotate(-90 12 305)">Không quan trọng</text>
  <rect x="25" y="25" width="180" height="180" fill="#fee2e2" stroke="#ef4444"/>
  <text x="115" y="100" text-anchor="middle" font-size="13" font-weight="700" fill="#991b1b">1. LÀM NGAY</text>
  <text x="115" y="120" text-anchor="middle" font-size="10" fill="#7f1d1d">Khủng hoảng, deadline sát</text>
  <rect x="215" y="25" width="180" height="180" fill="#dcfce7" stroke="#22c55e"/>
  <text x="305" y="100" text-anchor="middle" font-size="13" font-weight="700" fill="#166534">2. LÊN LỊCH</text>
  <text x="305" y="120" text-anchor="middle" font-size="10" fill="#14532d">Kế hoạch dài hạn, phát triển bản thân</text>
  <rect x="25" y="215" width="180" height="180" fill="#fef3c7" stroke="#f59e0b"/>
  <text x="115" y="290" text-anchor="middle" font-size="13" font-weight="700" fill="#92400e">3. GIAO VIỆC</text>
  <text x="115" y="310" text-anchor="middle" font-size="10" fill="#78350f">Gấp nhưng người khác làm được</text>
  <rect x="215" y="215" width="180" height="180" fill="#f3f4f6" stroke="#9ca3af"/>
  <text x="305" y="290" text-anchor="middle" font-size="13" font-weight="700" fill="#374151">4. LOẠI BỎ</text>
  <text x="305" y="310" text-anchor="middle" font-size="10" fill="#4b5563">Việc gây xao nhãng, ít giá trị</text>
</svg>
</div>

## Prompt mẫu

```
Đây là danh sách việc cần làm của tôi tuần này:
[liệt kê tất cả việc, kèm ghi chú deadline nếu có]

Hãy phân loại từng việc vào 1 trong 4 ô của Ma trận Eisenhower
(Làm ngay / Lên lịch / Giao việc / Loại bỏ), giải thích ngắn gọn lý
do xếp vào ô đó. Nếu thiếu thông tin để xếp loại chính xác (ví dụ
không rõ mức độ quan trọng), hãy hỏi lại tôi thay vì đoán.
```

## Thử trực tiếp: hỏi không kèm danh sách so với liệt kê việc cụ thể

{{PROMPT_LAB}}

> 💡 Phần lớn giá trị dài hạn nằm ở ô "Lên lịch" — nhưng đây cũng là ô dễ bị bỏ quên nhất vì không có deadline gấp. Chủ động dành thời gian cố định mỗi tuần cho ô này.""",
        "prompt_lab": {
            "bad": {
                "label": "Hỏi không kèm danh sách",
                "prompt": "Tôi có nhiều việc cần làm tuần này, không biết nên ưu tiên cái nào trước. Giúp tôi với.",
                "reply": "Bạn nên ưu tiên những việc quan trọng và gấp trước, sau đó đến việc ít gấp hơn. Bạn có thể cho tôi biết cụ thể danh sách công việc để tôi giúp phân loại chi tiết hơn.",
            },
            "good": {
                "label": "Liệt kê việc cụ thể",
                "prompt": "Đây là danh sách việc cần làm tuần này:\n- Trả lời email khách hàng phàn nàn\n- Học khóa học nâng cao kỹ năng quý sau\n- Đặt lịch họp giúp đồng nghiệp\n- Dọn hộp thư rác\n\nHãy phân loại từng việc vào Ma trận Eisenhower (Làm ngay/Lên lịch/Giao việc/Loại bỏ), giải thích lý do.",
                "reply": "Trả lời email khách hàng phàn nàn → Làm ngay (khẩn cấp + quan trọng, ảnh hưởng uy tín)\nHọc khóa học nâng cao kỹ năng → Lên lịch (quan trọng nhưng không gấp)\nĐặt lịch họp giúp đồng nghiệp → Giao việc (gấp nhưng không cần chính bạn làm)\nDọn hộp thư rác → Loại bỏ hoặc làm sau cùng",
            },
        },
    },
    {
        "id": "planning-6",
        "level": "planning",
        "title": "Ra quyết định lớn: phân tích ưu nhược điểm có trọng số",
        "summary": "Nâng cấp danh sách ưu/nhược điểm đơn thuần bằng cách gán trọng số cho từng tiêu chí.",
        "content": """## Nguyên tắc

Danh sách "ưu điểm/nhược điểm" đơn thuần có vấn đề: nó coi mọi tiêu chí quan trọng như nhau. Thực tế, một nhược điểm nhỏ có thể bị lu mờ bởi 5 ưu điểm nhỏ khác trong danh sách, dù chỉ một yếu tố đó thực sự quyết định. Giải pháp: **chấm điểm mỗi lựa chọn theo từng tiêu chí, có trọng số ưu tiên**.

## Prompt mẫu

```
Tôi đang phân vân giữa các lựa chọn sau: [liệt kê các lựa chọn,
ví dụ: Offer A, Offer B]

Các tiêu chí tôi quan tâm (đã sắp theo độ quan trọng giảm dần):
1. [tiêu chí 1]
2. [tiêu chí 2]
3. [tiêu chí 3]

Hãy lập bảng: mỗi lựa chọn x mỗi tiêu chí, chấm điểm 1-5 dựa trên
thông tin tôi cung cấp, gán trọng số theo thứ tự tôi liệt kê (tiêu
chí đầu trọng số cao nhất), tính điểm tổng có trọng số, và kết luận
lựa chọn nào đang nhỉnh hơn dựa trên khung này — nhưng nhắc tôi đây
chỉ là công cụ tham khảo, quyết định cuối vẫn là của tôi.

Thông tin từng lựa chọn: [mô tả chi tiết mỗi lựa chọn]
```

## Thử trực tiếp: hỏi không tiêu chí so với dùng ma trận có trọng số

{{PROMPT_LAB}}

> 💡 Nếu điểm tổng hai lựa chọn quá sát nhau, đó là dấu hiệu bạn nên tìm thêm tiêu chí quan trọng đang bị bỏ sót, thay vì chọn đại theo điểm số.""",
        "prompt_lab": {
            "bad": {
                "label": "Hỏi không có tiêu chí",
                "prompt": "Tôi đang phân vân giữa Offer A (lương thấp hơn nhưng học được nhiều) và Offer B (lương cao hơn, gần nhà). Nên chọn cái nào?",
                "reply": "Cả hai đều có điểm mạnh riêng. Nếu bạn ưu tiên học hỏi thì chọn A, nếu ưu tiên lương thì chọn B. Bạn cần xác định rõ điều gì quan trọng hơn với mình ở giai đoạn này.",
            },
            "good": {
                "label": "Dùng ma trận có trọng số",
                "prompt": "Tôi đang phân vân giữa Offer A và Offer B.\nTiêu chí quan trọng (giảm dần): 1. Lương, 2. Cơ hội học hỏi, 3. Khoảng cách di chuyển.\n\nHãy lập bảng chấm điểm 1-5 mỗi lựa chọn x mỗi tiêu chí, gán trọng số theo thứ tự, tính điểm tổng có trọng số.\n\nOffer A: lương thấp hơn, học được nhiều, xa nhà.\nOffer B: lương cao hơn, ít cơ hội học, gần nhà.",
                "reply": "Lương (x3): A=4→12, B=5→15\nCơ hội học hỏi (x2): A=5→10, B=3→6\nKhoảng cách (x1): A=3→3, B=5→5\nTổng có trọng số: A=25, B=26\n\n(Sát nút — có thể còn tiêu chí quan trọng khác chưa liệt kê, ví dụ văn hoá công ty)",
            },
        },
    },
    {
        "id": "planning-7",
        "level": "planning",
        "title": "Lên kịch bản rủi ro và kế hoạch B (kỹ thuật Premortem)",
        "summary": "Tưởng tượng dự án đã thất bại để tìm rủi ro tiềm ẩn trước khi nó xảy ra thật.",
        "content": """## Nguyên tắc

Con người thường lạc quan thái quá khi lên kế hoạch, dễ bỏ sót rủi ro. Kỹ thuật **Premortem** (do nhà tâm lý học Gary Klein đề xuất) đảo ngược cách tiếp cận: thay vì hỏi "điều gì có thể sai?", hãy **giả định dự án đã thất bại**, rồi truy ngược lý do tại sao — cách này khai thác trí tưởng tượng hiệu quả hơn hỏi trực tiếp.

## Prompt mẫu

```
Giả sử dự án sau đã THẤT BẠI hoàn toàn sau khi thực hiện xong:
[mô tả dự án/kế hoạch của bạn]

Hãy tưởng tượng bạn đang viết báo cáo "vì sao nó thất bại", liệt kê
5-7 nguyên nhân có khả năng cao nhất dẫn đến thất bại đó, xét trên
nhiều góc độ (nguồn lực, con người, kỹ thuật, thị trường, thời
gian...).

Sau đó, với mỗi nguyên nhân, đề xuất một hành động phòng ngừa cụ
thể có thể làm NGAY BÂY GIỜ để giảm rủi ro đó.
```

## Thử trực tiếp: hỏi rủi ro chung chung so với dùng Premortem

{{PROMPT_LAB}}

> 💡 Premortem hiệu quả nhất khi làm **trước khi bắt đầu** dự án, lúc vẫn còn dễ điều chỉnh kế hoạch — làm giữa chừng vẫn có ích nhưng ít lựa chọn xử lý hơn.""",
        "prompt_lab": {
            "bad": {
                "label": "Hỏi rủi ro chung chung",
                "prompt": "Tôi sắp ra mắt sản phẩm mới. Có rủi ro gì cần lưu ý không?",
                "reply": "Có thể gặp rủi ro về chất lượng sản phẩm, phản hồi thị trường không như mong đợi, hoặc vấn đề vận hành. Bạn nên chuẩn bị phương án dự phòng cho những tình huống này.",
            },
            "good": {
                "label": "Dùng kỹ thuật Premortem",
                "prompt": "Giả sử việc ra mắt sản phẩm mới của tôi đã THẤT BẠI hoàn toàn. Hãy liệt kê 5-7 nguyên nhân có khả năng cao nhất, xét nhiều góc độ (nguồn lực, con người, kỹ thuật, thị trường). Với mỗi nguyên nhân, đề xuất hành động phòng ngừa có thể làm NGAY.",
                "reply": "Đối tác cung cấp nguyên liệu giao trễ → Ký hợp đồng có điều khoản phạt trễ, tìm nhà cung cấp dự phòng\nĐội bán hàng chưa được đào tạo kịp → Lên lịch đào tạo hoàn tất trước ngày ra mắt 1 tuần\nNhu cầu thị trường thấp hơn dự đoán → Chạy khảo sát/pre-order nhỏ trước khi sản xuất số lượng lớn",
            },
        },
    },
    {
        "id": "planning-8",
        "level": "planning",
        "title": "Lập lịch ôn thi/học tập theo deadline cụ thể",
        "summary": "Phân bổ thời gian ôn tập hợp lý, có thời gian ôn lại chứ không chỉ học một lượt.",
        "content": """## Nguyên tắc

Lịch ôn thi hiệu quả cần 2 yếu tố người tự lập kế hoạch dễ bỏ qua: **có thời gian ôn lại kiến thức cũ** (không chỉ học tuyến tính một lần rồi thi), và **có buffer dự phòng** cho những ngày không học được như kế hoạch.

## Prompt mẫu

```
Tôi có kỳ thi môn [môn học] vào ngày [ngày thi].
Nội dung cần ôn: [liệt kê chương/chủ đề]
Thời gian rảnh: [số giờ]/ngày, [số ngày]/tuần.

Hãy lập lịch ôn tập từ hôm nay đến ngày thi, đảm bảo:
- Học nội dung mới ở 60-70% tổng thời gian, phần còn lại dành ôn
  lại nội dung đã học trước đó (không dồn ôn lại vào 1-2 ngày cuối)
- Có ít nhất 1 ngày "buffer" mỗi tuần không lên lịch cố định, dự
  phòng cho việc học chậm hơn dự kiến
- 2-3 ngày cuối trước ngày thi dành để ôn tổng hợp toàn bộ, không
  học nội dung mới

Trình bày dạng lịch theo ngày/tuần.
```

## Thử trực tiếp: yêu cầu thiếu chi tiết so với đủ thông tin

{{PROMPT_LAB}}

> 💡 Sau mỗi tuần, báo lại tiến độ thực tế cho AI (học kịp hay chậm) và xin điều chỉnh lịch tuần sau — lịch ban đầu chỉ là dự kiến, không phải cố định.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu thiếu chi tiết",
                "prompt": "Tôi có kỳ thi 2 tuần nữa. Giúp tôi lịch ôn tập.",
                "reply": "Bạn nên dành thời gian ôn tập đều mỗi ngày, tập trung vào những phần yếu, và làm đề thi thử trước ngày thi. Cố gắng sắp xếp thời gian hợp lý để không bị dồn việc vào những ngày cuối.",
            },
            "good": {
                "label": "Yêu cầu đủ thông tin",
                "prompt": "Tôi có kỳ thi môn Giải tích vào 2 tuần nữa.\nNội dung cần ôn: chương 1-5.\nThời gian rảnh: 3 giờ/ngày.\n\nHãy lập lịch ôn tập đảm bảo có thời gian ôn lại, có buffer, và 2-3 ngày cuối ôn tổng hợp.",
                "reply": "Tuần 1: Học chương 1-3 (mới), cuối tuần ôn lại chương 1, có 1 ngày buffer\nTuần 2: Học chương 4-5, ôn tổng hợp toàn bộ, làm đề thi thử, 2 ngày cuối chỉ xem lại lỗi sai",
            },
        },
    },
    {
        "id": "planning-9",
        "level": "planning",
        "title": "Xây dựng thói quen mới với kế hoạch theo dõi cụ thể",
        "summary": "Biến ý định mơ hồ 'muốn tập thể dục đều' thành thói quen có cơ chế theo dõi rõ ràng.",
        "content": """## Nguyên tắc

Thói quen mới dễ thất bại vì thiếu 2 thứ: **gắn với một mốc có sẵn trong ngày** (habit stacking — gắn thói quen mới ngay sau một việc đã làm hằng ngày), và **cơ chế theo dõi** để biết mình có đang duy trì hay không, thay vì chỉ "cố nhớ".

## Prompt mẫu

```
Tôi muốn xây dựng thói quen: [thói quen mới, ví dụ: uống đủ 2 lít
nước mỗi ngày / đọc sách 20 phút mỗi ngày]
Lịch trình hằng ngày hiện tại của tôi: [mô tả ngắn các mốc cố định
trong ngày: thức dậy, ăn trưa, về nhà...]

Hãy:
1. Đề xuất gắn thói quen mới vào ngay sau MỘT mốc cố định có sẵn
   trong lịch trình của tôi (habit stacking), giải thích tại sao
   chọn mốc đó
2. Thiết kế một cách theo dõi đơn giản (ví dụ: bảng tick hằng ngày,
   câu hỏi tự kiểm tra cuối ngày)
3. Đề xuất một "phiên bản tối thiểu" của thói quen cho những ngày
   quá bận/mệt, để không bị đứt chuỗi hoàn toàn
```

## Thử trực tiếp: yêu cầu thiếu bối cảnh so với dùng habit stacking

{{PROMPT_LAB}}

> 💡 Cuối mỗi tuần, báo cáo lại với AI số ngày duy trì được — nếu liên tục bỏ lỡ, thử hỏi AI điều chỉnh mốc gắn hoặc phiên bản tối thiểu, thay vì cố ép bản thân theo kế hoạch không thực tế.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu thiếu bối cảnh",
                "prompt": "Tôi muốn đọc sách đều đặn hơn. Giúp tôi lập kế hoạch.",
                "reply": "Bạn nên đặt mục tiêu đọc sách mỗi ngày và cố gắng duy trì thói quen này. Có thể đặt lịch nhắc nhở trên điện thoại để không quên.",
            },
            "good": {
                "label": "Dùng habit stacking",
                "prompt": "Tôi muốn xây dựng thói quen: đọc sách 20 phút/ngày.\nLịch trình hiện tại: luôn uống cà phê sáng lúc 7h trước khi đi làm.\n\nHãy đề xuất gắn thói quen mới vào một mốc có sẵn, thiết kế cách theo dõi đơn giản, và một phiên bản tối thiểu cho ngày bận.",
                "reply": "Đề xuất: đọc sách ngay trong lúc uống cà phê sáng (gắn vào mốc có sẵn).\nTheo dõi: bảng 7 ô mỗi tuần, tick nếu đọc.\nPhiên bản tối thiểu ngày bận: chỉ cần đọc 2 trang, miễn không bỏ hẳn.",
            },
        },
    },
    {
        "id": "planning-10",
        "level": "planning",
        "title": "Lên kế hoạch tổ chức sự kiện/dự án nhóm nhiều đầu việc",
        "summary": "Chia checklist theo giai đoạn trước - trong - sau để không bỏ sót đầu việc.",
        "content": """## Nguyên tắc

Sự kiện/dự án nhóm có nhiều đầu việc phụ thuộc lẫn nhau (không thể thuê địa điểm sau khi đã gửi thiệp mời). Chia checklist theo 3 giai đoạn **Trước - Trong - Sau** giúp thấy rõ thứ tự và không bỏ sót việc "hậu kỳ" thường bị quên.

## Prompt mẫu

```
Tôi cần tổ chức [loại sự kiện/dự án], quy mô khoảng [số người tham
gia], dự kiến vào [ngày].

Hãy lập checklist chia theo 3 giai đoạn:
- **Trước sự kiện**: liệt kê việc theo thứ tự cần làm trước, có gợi
  ý mốc thời gian tương đối (ví dụ: "trước 2 tuần", "trước 3 ngày")
- **Trong sự kiện**: việc cần làm/theo dõi ngay tại thời điểm diễn ra
- **Sau sự kiện**: việc hậu kỳ thường bị quên (thanh toán, cảm ơn,
  tổng kết, lưu trữ tài liệu...)

Đánh dấu rõ việc nào có thể giao cho người khác làm song song, việc
nào bắt buộc phải xong trước mới làm được việc tiếp theo.
```

## Thử trực tiếp: yêu cầu thiếu quy mô so với chia rõ 3 giai đoạn

{{PROMPT_LAB}}

> 💡 Giai đoạn "Sau" là nơi dễ bị bỏ quên nhất khi mọi người đã "thở phào" xong sự kiện — nên giao rõ người phụ trách các việc hậu kỳ ngay từ đầu, đừng để "ai rảnh thì làm".""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu thiếu quy mô",
                "prompt": "Tôi cần tổ chức một buổi workshop. Giúp tôi checklist việc cần làm.",
                "reply": "Bạn cần chuẩn bị địa điểm, mời người tham dự, chuẩn bị tài liệu, và tổ chức buổi workshop. Nên lên danh sách công việc chi tiết để không bỏ sót.",
            },
            "good": {
                "label": "Yêu cầu đủ quy mô, chia giai đoạn",
                "prompt": "Tôi cần tổ chức workshop nội bộ, quy mô 50 người, dự kiến trong 1 tháng nữa.\n\nHãy lập checklist chia 3 giai đoạn: Trước - Trong - Sau, có mốc thời gian tương đối cho từng việc.",
                "reply": "Trước (trước 3 tuần): chốt địa điểm & ngày → (trước 2 tuần) gửi lời mời → (trước 3 ngày) chuẩn bị tài liệu.\nTrong: check-in người tham dự, quay video, thu phản hồi cuối buổi.\nSau: gửi email cảm ơn + tài liệu (trong 2 ngày), tổng hợp phản hồi, thanh toán chi phí, lưu trữ tài liệu.",
            },
        },
    },

    # ── Vibe Coding (vibecoding) ───────────────────────────────────
    {
        "id": "vibecoding-1",
        "level": "vibecoding",
        "title": "Vibe Coding là gì? Lợi ích và rủi ro cần biết",
        "summary": "Khái niệm lập trình bằng cách mô tả ý định cho AI, thay vì tự tay viết từng dòng code.",
        "content": """## Vibe Coding là gì?

"Vibe Coding" là cách làm việc trong đó bạn **mô tả ý định** (ví dụ: "thêm nút đăng xuất ở góc trên bên phải") cho một AI coding agent (như Claude Code, Cursor, GitHub Copilot...) để nó tự viết/sửa code, còn bạn tập trung vào **kiểm tra kết quả có đúng ý không**, thay vì gõ từng ký tự.

> 🌱 **Ví dụ đời thường**: Giống việc bạn là kiến trúc sư mô tả bản vẽ cho đội thi công, thay vì tự tay xây từng viên gạch — nhưng bạn vẫn phải kiểm tra công trình có đúng bản vẽ và an toàn hay không.

## Lợi ích

- **Tốc độ**: viết tính năng, sửa bug, refactor nhanh hơn nhiều so với gõ tay hoàn toàn.
- **Hạ rào cản**: người chưa rành cú pháp một ngôn ngữ vẫn tạo ra được sản phẩm chạy được.
- **Rảnh tay cho tư duy cấp cao**: bạn tập trung vào "cái gì cần làm, tại sao", AI lo phần "làm thế nào".

## Rủi ro cần biết

- **Ảo tưởng về chất lượng**: code chạy được không có nghĩa là đúng, an toàn, hay dễ bảo trì.
- **Mất kiểm soát dần**: nếu không đọc code AI viết, dần dần bạn sẽ không còn hiểu hệ thống của chính mình.
- **Lỗ hổng bảo mật**: AI có thể viết code có lỗi injection, lộ secret, thiếu validate input nếu không được yêu cầu cẩn thận.

> 💡 Vibe coding hiệu quả không phải là "giao hết cho AI rồi không quan tâm" — mà là biết dùng đúng lúc, đúng cách, và luôn giữ vai trò người kiểm duyệt cuối cùng. Các bài tiếp theo trong nhóm này đi vào từng kỹ thuật cụ thể, có ví dụ với Claude Code.""",
    },
    {
        "id": "vibecoding-2",
        "level": "vibecoding",
        "title": "Đọc trước khi sửa: cho AI đủ ngữ cảnh",
        "summary": "Nguyên tắc quan trọng nhất khi làm việc với coding agent — để nó đọc code hiện có trước khi viết code mới.",
        "content": """## Nguyên tắc

Coding agent không tự động "biết" codebase của bạn — nó chỉ thấy những gì được đọc vào ngữ cảnh. Yêu cầu sửa code mà không cho AI đọc file liên quan trước dễ dẫn đến: code không khớp style hiện có, phá vỡ quy ước đặt tên, hoặc tạo trùng lặp với hàm đã có sẵn.

> 🌱 Đây chính là quy tắc **"Read before you write"** mà các coding agent có kỷ luật tốt (Claude Code trong đó) luôn cố gắng tuân theo mặc định — nhưng chủ động nhắc rõ ràng vẫn giúp ích, đặc biệt với các file/quy ước ít phổ biến.

## Prompt mẫu

```
Trước khi sửa, hãy đọc [đường dẫn file/thư mục liên quan] để nắm
quy ước đặt tên biến, cấu trúc component, và style code hiện có.

Sau đó: [mô tả thay đổi bạn muốn]

Giữ nguyên style hiện tại, đừng tự ý đổi cấu trúc không liên quan.
```

## Thử trực tiếp: không cho đọc code so với yêu cầu đọc trước

{{PROMPT_LAB}}

> 💡 Với dự án lớn, chỉ định đúng file/thư mục liên quan (thay vì "đọc hết cả repo") vừa nhanh hơn, vừa giúp AI tập trung đúng phạm vi cần sửa.""",
        "prompt_lab": {
            "bad": {
                "label": "Không cho đọc code trước",
                "prompt": "Thêm chức năng xóa bình luận vào ứng dụng của tôi.",
                "reply": "Đã thêm hàm deleteComment() vào file mới comments.js, dùng fetch() trực tiếp, đặt tên biến theo camelCase.",
            },
            "good": {
                "label": "Yêu cầu đọc code trước",
                "prompt": "Trước khi sửa, hãy đọc src/components/CommentList.jsx và src/api/comments.js để nắm cách gọi API và style hiện có.\n\nSau đó thêm chức năng xóa bình luận, giữ đúng style hiện tại.",
                "reply": "Đã đọc CommentList.jsx và comments.js — thấy dự án dùng axios và có sẵn hàm deleteRequest() dùng chung. Đã thêm deleteComment() vào comments.js theo đúng pattern đó, và nút xóa vào CommentList.jsx dùng đúng icon Trash2 đã import sẵn.",
            },
        },
    },
    {
        "id": "vibecoding-3",
        "level": "vibecoding",
        "title": "Chia nhỏ yêu cầu, kiểm tra từng bước",
        "summary": "Yêu cầu một lần quá lớn khiến AI dễ lạc hướng — chia nhỏ giúp kiểm soát chất lượng tốt hơn.",
        "content": """## Nguyên tắc

"Làm giúp tôi cả hệ thống đăng nhập/đăng ký/quên mật khẩu" là yêu cầu quá lớn để kiểm tra đúng-sai trong một lần. Càng nhiều thay đổi trong một lượt, càng khó phát hiện lỗi ẩn, và càng khó hoàn tác nếu có gì sai. Chia thành các bước nhỏ, kiểm tra kết quả mỗi bước trước khi đi tiếp — đúng tinh thần "incremental development" trong lập trình truyền thống.

## Prompt mẫu

```
Chúng ta sẽ làm [tính năng lớn] theo từng bước, tôi sẽ kiểm tra sau
mỗi bước trước khi đi tiếp.

Bước 1: [phần nhỏ đầu tiên]

Chỉ làm bước 1 trước, đừng làm các bước sau khi tôi chưa xác nhận.
```

## Thử trực tiếp: yêu cầu một lần quá lớn so với chia nhỏ từng bước

{{PROMPT_LAB}}

> 💡 Dấu hiệu một yêu cầu đang quá lớn: nếu bạn không thể mô tả "bằng chứng hoàn thành" của nó trong một câu ngắn gọn, có lẽ nên chia nhỏ thêm.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu một lần quá lớn",
                "prompt": "Làm giúp tôi toàn bộ hệ thống đăng nhập, đăng ký, quên mật khẩu, và xác thực email.",
                "reply": "Đã tạo 8 file mới: LoginForm.jsx, RegisterForm.jsx, ForgotPassword.jsx, EmailVerification.jsx, auth.py, email_service.py, và 2 file khác — toàn bộ hệ thống đăng nhập/đăng ký/quên mật khẩu/xác thực email đã hoàn thành.",
            },
            "good": {
                "label": "Chia nhỏ từng bước",
                "prompt": "Chúng ta sẽ làm hệ thống đăng nhập theo từng bước. Bước 1: chỉ làm form đăng nhập (UI + validate input phía client), chưa cần nối API. Làm xong báo tôi kiểm tra trước khi sang bước 2.",
                "reply": "Đã tạo LoginForm.jsx với validate email/password phía client. Đây là bước 1/4 — bạn kiểm tra UI và validate trước, tôi sẽ chờ xác nhận rồi mới làm bước 2 (nối API đăng nhập).",
            },
        },
    },
    {
        "id": "vibecoding-4",
        "level": "vibecoding",
        "title": "Lập kế hoạch trước khi code việc lớn (Plan Mode)",
        "summary": "Với thay đổi phức tạp, thống nhất kế hoạch trước khi để AI viết code — tránh code sai hướng rồi phải sửa lại.",
        "content": """## Nguyên tắc

Với việc nhỏ, để AI code luôn là hợp lý. Nhưng với thay đổi **phức tạp hoặc ảnh hưởng nhiều file**, code ngay dễ dẫn đến: chọn sai kiến trúc, bỏ sót trường hợp biên, hoặc làm khác hướng bạn thực sự muốn — và bạn chỉ phát hiện ra sau khi đã tốn công viết cả đống code. Tốt hơn: thống nhất kế hoạch bằng lời trước, rồi mới cho code.

> 🌱 Claude Code có sẵn chế độ **"Plan Mode"** — khiến AI chỉ đọc, phân tích, và trình bày kế hoạch bằng chữ trước, không sửa file nào cho đến khi bạn duyệt kế hoạch đó.

## Prompt mẫu

```
Đây là việc cần làm: [mô tả thay đổi lớn/phức tạp]

Đừng viết code ngay. Trước tiên hãy trình bày kế hoạch: các file
cần sửa, cách tiếp cận, và những điểm còn chưa rõ cần hỏi lại tôi.
Tôi sẽ duyệt kế hoạch trước khi bạn bắt đầu code.
```

## Thử trực tiếp: yêu cầu code ngay so với yêu cầu lập kế hoạch trước

{{PROMPT_LAB}}

> 💡 Càng việc lớn/rủi ro cao (đổi kiến trúc, đụng vào dữ liệu, migration), càng nên dùng bước lập kế hoạch — chi phí thời gian bàn kế hoạch luôn rẻ hơn chi phí sửa lại code đã viết sai hướng.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu code ngay",
                "prompt": "Refactor toàn bộ hệ thống quản lý state từ Redux sang Context API cho tôi.",
                "reply": "Đã bắt đầu sửa 12 file: tạo AuthContext, DataContext, và ThemeContext, xóa store.js và các slice Redux cũ, cập nhật toàn bộ component đang dùng useSelector/useDispatch sang useContext.",
            },
            "good": {
                "label": "Yêu cầu lập kế hoạch trước",
                "prompt": "Tôi muốn refactor từ Redux sang Context API. Đừng code ngay — hãy trình bày kế hoạch: cần tách bao nhiêu Context, file nào bị ảnh hưởng, và rủi ro nào cần lưu ý. Tôi sẽ duyệt trước khi bạn code.",
                "reply": "Kế hoạch: tách 3 Context (AuthContext, CartContext, UIContext) tương ứng 3 slice Redux hiện tại. Ảnh hưởng 9 file. Rủi ro: CartContext có logic tính toán phức tạp, cần giữ nguyên để tránh sai số liệu. Bạn xác nhận trước khi tôi bắt đầu nhé?",
            },
        },
    },
    {
        "id": "vibecoding-5",
        "level": "vibecoding",
        "title": "Luôn review code AI viết trước khi chấp nhận",
        "summary": "Code chạy được không có nghĩa là đúng — luôn dành thời gian đọc lại trước khi merge.",
        "content": """## Nguyên tắc

Cảm giác "chạy được, xong việc" rất dễ khiến bạn bấm chấp nhận thay đổi mà không đọc kỹ. Nhưng AI có thể viết code **chạy đúng ở trường hợp thường gặp nhưng sai ở trường hợp biên**, hoặc âm thầm thêm logic bạn không yêu cầu. Luôn dành ít nhất một lượt đọc lại diff trước khi chấp nhận, đặc biệt với code động đến dữ liệu, tiền bạc, hoặc bảo mật.

## Prompt mẫu (yêu cầu AI tự giải thích trước khi bạn duyệt)

```
Trước khi tôi chấp nhận thay đổi này, hãy tóm tắt:
1. Chính xác những gì đã thay đổi (file nào, hàm nào)
2. Có giả định/đánh đổi nào tôi cần biết không
3. Trường hợp nào có thể chưa được xử lý (edge case)
```

## Thử trực tiếp: chấp nhận ngay so với yêu cầu giải thích trước

{{PROMPT_LAB}}

> 💡 Đây cũng chính là lý do các đội ngũ vibe coding có kỷ luật vẫn giữ bước code review — dù người viết là AI hay con người, review vẫn là lưới an toàn cuối cùng.""",
        "prompt_lab": {
            "bad": {
                "label": "Chấp nhận ngay không hỏi lại",
                "prompt": "Cảm ơn, code chạy được rồi, merge luôn nhé.",
                "reply": "Đã merge nhánh vào main.",
            },
            "good": {
                "label": "Yêu cầu giải thích trước khi duyệt",
                "prompt": "Trước khi tôi chấp nhận, tóm tắt chính xác những gì đã thay đổi, có giả định nào tôi cần biết, và trường hợp biên nào có thể chưa xử lý.",
                "reply": "Đã sửa hàm calculateTotal() để cộng thêm phí ship. Giả định: phí ship luôn là số dương, chưa xử lý trường hợp số lượng sản phẩm = 0 (sẽ hiện phí ship dù giỏ hàng rỗng) — bạn có muốn tôi xử lý thêm case này không?",
            },
        },
    },
    {
        "id": "vibecoding-6",
        "level": "vibecoding",
        "title": "Dùng Git để an toàn thử nghiệm với AI",
        "summary": "Nhánh riêng và commit nhỏ giúp bạn dễ dàng hoàn tác nếu AI đi sai hướng.",
        "content": """## Nguyên tắc

Khi AI có thể sửa nhiều file cùng lúc, rủi ro lớn nhất là **khó hoàn tác** nếu hướng đi sai. Luôn làm việc trên nhánh riêng (không phải main/master), và commit thường xuyên theo từng bước nhỏ đã kiểm tra ổn — để có thể quay lại đúng điểm gần nhất nếu bước sau đó đi lệch hướng.

> 🌱 Đây cũng là lý do các coding agent có kỷ luật tốt (Claude Code trong đó) mặc định không tự làm việc trực tiếp trên nhánh main/master, và không tự ý chạy các lệnh git nguy hiểm (`reset --hard`, force push, xóa branch...) mà không hỏi trước.

## Prompt mẫu

```
Trước khi bắt đầu, tạo giúp tôi một nhánh mới tên [tên nhánh] từ
[nhánh gốc].

Sau mỗi bước nhỏ hoàn thành và tôi đã xác nhận ổn, hãy commit lại
với message rõ ràng trước khi làm bước tiếp theo.
```

## Thử trực tiếp: làm trực tiếp trên main so với dùng branch + commit từng bước

{{PROMPT_LAB}}

> 💡 Nếu một coding agent đề nghị chạy lệnh git có thể phá huỷ dữ liệu (force push, reset --hard, xóa branch) mà bạn không nhớ đã yêu cầu — luôn dừng lại và hỏi rõ lý do trước khi đồng ý.""",
        "prompt_lab": {
            "bad": {
                "label": "Làm trực tiếp, không branch/commit",
                "prompt": "Sửa giúp tôi tính năng giỏ hàng, sửa xong luôn thể.",
                "reply": "Đã sửa 5 file trực tiếp trên nhánh main: CartContext.js, CartItem.jsx, cartUtils.js, checkout.py, và cart_routes.py.",
            },
            "good": {
                "label": "Yêu cầu branch + commit từng bước",
                "prompt": "Tạo nhánh mới 'fix-cart-bug' từ main trước khi bắt đầu. Sửa tính năng giỏ hàng theo từng bước nhỏ, commit sau mỗi bước tôi xác nhận ổn.",
                "reply": "Đã tạo nhánh fix-cart-bug. Bước 1: sửa lỗi tính tổng tiền — bạn kiểm tra thử, nếu ổn tôi sẽ commit rồi làm bước 2 (sửa lỗi hiển thị số lượng).",
            },
        },
    },
    {
        "id": "vibecoding-7",
        "level": "vibecoding",
        "title": "Tận dụng khả năng agent tự chạy và tự sửa lỗi",
        "summary": "Coding agent hiện đại có thể tự chạy test/build và đọc lỗi — hãy để nó làm thay vì tự copy-paste lỗi qua lại.",
        "content": """## Nguyên tắc

Khác với chatbot chỉ trả lời chữ, một coding agent như Claude Code có thể **tự chạy lệnh** (test, build, lint) và đọc kết quả/lỗi trực tiếp — không cần bạn copy-paste log qua lại. Tận dụng khả năng này giúp vòng lặp sửa lỗi nhanh hơn nhiều so với việc bạn làm trung gian chuyển thông tin qua lại.

## Prompt mẫu

```
Sau khi sửa, hãy tự chạy [lệnh test/build/lint tương ứng dự án] để
kiểm tra thay đổi có gây lỗi gì không, và tự sửa nếu phát hiện lỗi.

Chỉ báo tôi khi: (a) mọi thứ đã pass, hoặc (b) gặp lỗi bạn không
chắc chắn cách sửa đúng.
```

## Thử trực tiếp: tự copy-paste lỗi qua lại so với để agent tự chạy và tự sửa

{{PROMPT_LAB}}

> 💡 Vẫn nên tự chạy lại thử ứng dụng thật (đặc biệt với thay đổi giao diện) — test tự động pass không đảm bảo trải nghiệm người dùng thực tế cũng ổn.""",
        "prompt_lab": {
            "bad": {
                "label": "Tự copy-paste lỗi qua lại",
                "prompt": "Sửa hàm này giúp tôi.\n\n[dán code]",
                "reply": "Tôi đã sửa lại hàm — vấn đề nằm ở việc chưa kiểm tra mảng rỗng trước khi truy cập phần tử đầu tiên. Đây là bản đã sửa (đã thêm điều kiện kiểm tra độ dài mảng > 0 trước dòng truy cập).\n\nBạn chạy thử ứng dụng và cho tôi biết kết quả nhé — nếu vẫn còn lỗi, gửi lại thông báo lỗi để tôi kiểm tra tiếp.",
            },
            "good": {
                "label": "Để agent tự chạy và tự sửa",
                "prompt": "Sửa hàm này giúp tôi, sau đó tự chạy test liên quan (npm test) để kiểm tra, và tự sửa nếu test fail. Chỉ báo tôi khi test đã pass hoặc bạn gặp lỗi không chắc cách sửa.\n\n[dán code]",
                "reply": "Đã sửa hàm. Chạy npm test — phát hiện 1 test fail liên quan đến trường hợp rỗng, đã tự sửa và chạy lại — toàn bộ test đã pass.",
            },
        },
    },
    {
        "id": "vibecoding-8",
        "level": "vibecoding",
        "title": "CLAUDE.md: dạy AI 'luật chơi' của dự án một lần, dùng mãi",
        "summary": "Ghi lại quy ước dự án vào một file nhớ, thay vì nhắc lại từ đầu mỗi phiên làm việc.",
        "content": """## Nguyên tắc

Mỗi phiên chat mới với coding agent thường bắt đầu "từ số 0" — không nhớ style code, quy ước đặt tên, hay các ràng buộc riêng của dự án bạn đã từng nói ở phiên trước. Giải pháp: viết các quy tắc đó vào một **file hướng dẫn cố định** (Claude Code dùng file `CLAUDE.md` ở gốc dự án) — agent sẽ tự đọc file này ở đầu mỗi phiên làm việc, không cần bạn nhắc lại.

## Ví dụ nội dung CLAUDE.md

```
# Quy ước dự án

- Ngôn ngữ: TypeScript strict mode, không dùng `any`.
- State management: dùng Zustand, không dùng Redux.
- Styling: Tailwind CSS, không viết file CSS riêng.
- Test: mỗi hàm public phải có unit test (Vitest).
- Không tự ý thêm dependency mới khi chưa hỏi.
- Commit message theo Conventional Commits (feat/fix/chore...).
```

## Thử trực tiếp: nhắc lại mỗi lần chat so với đã ghi sẵn trong CLAUDE.md

{{PROMPT_LAB}}

> 💡 Cập nhật CLAUDE.md dần theo thời gian — mỗi lần bạn phải sửa/nhắc AI cùng một quy ước nhiều lần, đó là dấu hiệu nên ghi nó vào file này luôn.""",
        "prompt_lab": {
            "bad": {
                "label": "Nhắc lại quy ước mỗi lần chat",
                "prompt": "Viết component Button mới cho tôi. Nhớ là dự án dùng TypeScript strict, Tailwind, không dùng any nhé.",
                "reply": "Đã tạo Button.tsx dùng TypeScript, style bằng CSS module riêng (Button.module.css), có prop variant và onClick.",
            },
            "good": {
                "label": "Đã ghi sẵn trong CLAUDE.md",
                "prompt": "Viết component Button mới cho tôi.",
                "reply": "Đã đọc CLAUDE.md — dự án dùng TypeScript strict, Tailwind, Zustand. Đã tạo Button.tsx tuân theo đúng các quy ước này mà không cần bạn nhắc lại.",
            },
        },
    },
    {
        "id": "vibecoding-9",
        "level": "vibecoding",
        "title": "Ranh giới: việc gì nên tự làm, việc gì nên giao AI",
        "summary": "Không phải việc gì cũng nên giao cho AI — nhận biết loại việc cần sự kiểm soát chặt của con người.",
        "content": """## Nguyên tắc

Vibe coding hiệu quả không có nghĩa là giao tất cả cho AI. Một số loại việc cần **con người trực tiếp kiểm soát** vì rủi ro cao hoặc cần phán đoán tinh tế mà AI dễ bỏ sót.

## Bảng tham khảo

| Nên để AI làm | Cần con người kiểm soát chặt |
|---|---|
| Viết code lặp lại, boilerplate | Quyết định kiến trúc lớn, khó đảo ngược |
| Viết test case, sửa lỗi rõ ràng | Thao tác xóa dữ liệu, migration production |
| Refactor có test bao phủ đầy đủ | Xử lý thông tin nhạy cảm (secret, PII) |
| Giải thích/review code | Merge/deploy lên production |
| Tìm kiếm, tổng hợp thông tin kỹ thuật | Quyết định pháp lý, bảo mật quan trọng |

## Nguyên tắc thực hành

1. **Việc càng khó hoàn tác, càng cần bạn tự tay xác nhận từng bước** — không để AI tự động chạy hết một mạch.
2. **Luôn tự chạy/test lại** trước khi coi một thay đổi là "xong", đặc biệt với code chạm vào tiền, dữ liệu người dùng, hoặc bảo mật.
3. **Giữ quyền quyết định cuối cùng** ở các lệnh nguy hiểm (xóa branch, force push, xóa dữ liệu...) — coding agent có kỷ luật tốt sẽ luôn hỏi trước khi làm việc này, đừng tắt cơ chế hỏi đó đi.

> 💡 Càng làm việc nhiều với AI, ranh giới này sẽ càng rõ theo kinh nghiệm thực tế của bạn — không có công thức chung cho mọi dự án.""",
    },
    {
        "id": "vibecoding-10",
        "level": "vibecoding",
        "title": "Song song hoá việc lớn với nhiều agent con (subagent)",
        "summary": "Với việc có thể tách rời, giao cho nhiều agent làm song song thay vì một agent làm tuần tự.",
        "content": """## Nguyên tắc

Một số việc lớn thực ra là nhiều việc nhỏ **độc lập với nhau** (ví dụ: viết test cho 5 module không liên quan, hay khảo sát 3 thư viện khác nhau). Thay vì để một agent làm tuần tự từng việc, các coding agent hiện đại (Claude Code có tính năng "subagent") có thể **giao song song cho nhiều agent con**, mỗi agent phụ trách một phần, rút ngắn tổng thời gian đáng kể.

> 🌱 **Ví dụ đời thường**: Giống việc giao 3 người khác nhau đi khảo sát 3 nhà cung cấp cùng lúc, thay vì một người đi lần lượt từng nơi.

## Khi nào nên dùng

- Các việc **thực sự độc lập**, không phụ thuộc kết quả của nhau.
- Việc cần tìm kiếm/khảo sát nhiều nguồn khác nhau.
- Viết test/docs cho nhiều module riêng biệt cùng lúc.

## Khi nào KHÔNG nên dùng

- Các bước phụ thuộc tuần tự (bước 2 cần kết quả của bước 1) — song song hoá sẽ gây xung đột hoặc lãng phí.
- Việc cần một mạch tư duy nhất quán từ đầu đến cuối (ví dụ thiết kế kiến trúc tổng thể).

## Thử trực tiếp: yêu cầu làm tuần tự so với yêu cầu xử lý song song

{{PROMPT_LAB}}

> 💡 Không phải lúc nào cũng cần song song hoá — với việc nhỏ hoặc phụ thuộc lẫn nhau, làm tuần tự vẫn đơn giản và ít rủi ro xung đột hơn.""",
        "prompt_lab": {
            "bad": {
                "label": "Yêu cầu làm tuần tự",
                "prompt": "Viết unit test cho 3 module: utils.js, api.js, và validators.js.",
                "reply": "Đã viết test cho utils.js xong, đang chuyển sang api.js, sẽ làm validators.js sau khi hoàn tất api.js.",
            },
            "good": {
                "label": "Yêu cầu xử lý song song",
                "prompt": "Ba việc sau độc lập với nhau: viết unit test cho utils.js, api.js, và validators.js. Hãy xử lý song song bằng các agent con riêng biệt rồi tổng hợp kết quả.",
                "reply": "Đã giao 3 agent con xử lý song song 3 module. Cả 3 đã hoàn thành: utils.js (8 test case), api.js (12 test case), validators.js (6 test case) — tổng thời gian rút ngắn đáng kể so với làm tuần tự.",
            },
        },
    },
]
