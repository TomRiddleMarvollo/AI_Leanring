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

Prompt kém khiến AI phải "đoán" bạn muốn gì — nó có thể trả lời chung chung, sai giọng văn, sai độ dài. Prompt tốt loại bỏ hầu hết sự đoán mò đó.

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
]
