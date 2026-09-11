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
                "reply": "Marketing là hoạt động quảng bá sản phẩm/dịch vụ đến khách hàng thông qua nhiều kênh khác nhau như quảng cáo, mạng xã hội, email... Một chiến lược marketing tốt cần hiểu rõ đối tượng khách hàng...\n\n(AI phải đoán bạn muốn gì — chủ đề nào, độ dài nào, giọng văn ra sao)",
            },
            "good": {
                "label": "Prompt tốt",
                "prompt": "Bạn là chuyên gia marketing cho startup công nghệ.\nHãy viết 3 tiêu đề email quảng cáo (mỗi tiêu đề dưới 60 ký tự)\ncho sản phẩm ứng dụng học AI dành cho người mới bắt đầu.\nGiọng văn: thân thiện, tạo cảm giác cấp bách nhẹ nhàng.",
                "reply": "1. \"Học AI từ số 0 — chỉ 10 phút mỗi ngày\"\n2. \"Đừng để AI bỏ bạn lại phía sau — bắt đầu hôm nay\"\n3. \"Ưu đãi mở lớp: học AI dễ như đọc tin nhắn\"",
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
                "reply": "Ưu tiên: Trung bình\n\n(Hợp lý, nhưng không biết có khớp với thang đánh giá nội bộ team bạn hay không)",
            },
            "good": {
                "label": "Có 3 ví dụ mẫu (Few-shot)",
                "prompt": "Câu: \"App bị crash không mở được.\" → Ưu tiên: Cao\nCâu: \"Muốn đổi màu giao diện.\" → Ưu tiên: Thấp\nCâu: \"Thanh toán bị trừ tiền 2 lần.\" → Ưu tiên: Cao\n\nCâu: \"Không tìm thấy nút đăng xuất.\" → Ưu tiên:",
                "reply": "Ưu tiên: Thấp\n\n(Khớp đúng \"khẩu vị\" phân loại của team — lỗi giao diện nhỏ, không mất tiền/không crash → xếp Thấp, nhất quán với 3 ví dụ)",
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

## Ví dụ

Chủ đề: "Tại sao bầu trời có màu xanh". Bạn viết: *"Vì ánh sáng mặt trời chiếu vào bầu khí quyển và bị tán xạ nên ta thấy màu xanh."*

AI có thể phản hồi: "Bạn chưa giải thích **tại sao** lại tán xạ ra màu xanh cụ thể chứ không phải màu khác — gợi ý: liên quan đến bước sóng ánh sáng. Câu hỏi: nếu bầu khí quyển dày hơn nhiều, bạn dự đoán màu bầu trời sẽ thay đổi thế nào?"

> 💡 Mẹo: đừng đọc đáp án AI đưa ra ngay — thử tự trả lời câu hỏi "tại sao" trước, rồi mới xin AI chấm.""",
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

## Ví dụ

Đầu vào: đoạn văn dài về quang hợp. Đầu ra:

| Từ khóa / Câu hỏi | Nội dung chi tiết |
|---|---|
| Quang hợp diễn ra ở đâu? | Chủ yếu ở lục lạp của tế bào lá |
| Nguyên liệu đầu vào là gì? | CO₂, nước, ánh sáng mặt trời |
| Sản phẩm tạo ra? | Glucose và khí oxy |

**Tóm tắt**: Quang hợp là quá trình cây xanh chuyển ánh sáng, nước và CO₂ thành glucose và oxy, diễn ra chủ yếu ở lục lạp.

> 💡 Ôn bài bằng cách che cột phải, chỉ nhìn cột trái và tự nhớ lại nội dung — đúng tinh thần chủ động ôn tập của Cornell Notes.""",
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

## Ví dụ

| Mặt trước | Mặt sau |
|---|---|
| HTTP status 404 nghĩa là gì? | Không tìm thấy tài nguyên được yêu cầu |
| Sự khác biệt giữa PUT và PATCH? | PUT thay thế toàn bộ resource, PATCH chỉ cập nhật một phần |

## Cách dùng hiệu quả

1. Ngày 1: học hết bộ flashcard.
2. Ngày 2: chỉ ôn lại những câu bạn trả lời sai hoặc do dự.
3. Ngày 4, ngày 7, ngày 14: lặp lại — khoảng cách giữa các lần ôn giãn dần ra.

> 💡 Có thể xin AI xuất thêm định dạng CSV (`câu hỏi,đáp án`) để import thẳng vào ứng dụng flashcard như Anki, Quizlet.""",
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

## Ví dụ (phỏng vấn vị trí Backend Developer)

> **AI**: Câu 1: Sự khác biệt giữa `SQL` và `NoSQL`, khi nào bạn chọn cái nào?
>
> **Bạn**: SQL có schema cố định, NoSQL linh hoạt hơn...
>
> **AI**: 6/10. Bạn chưa nêu được ví dụ cụ thể use-case nào phù hợp NoSQL hơn (ví dụ dữ liệu phi cấu trúc, cần scale ngang nhanh). Câu 2: ...

> 💡 Luyện xong, đổi vai: nhờ AI cho bạn nhận xét chung "nếu là giám khảo thật, họ sẽ đánh giá phần thể hiện của bạn thế nào?" để có góc nhìn tổng thể.""",
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

## Ví dụ

> **Bạn**: "I want a coffee, no sugar please, and make it big size."
>
> **AI**: "Sure! One large coffee, no sugar. Anything else?"
> 📝 Sửa: "Can I get a large coffee with no sugar, please?" — cách nói này tự nhiên và lịch sự hơn khi gọi đồ ở quán.

> 💡 Sau vài lượt, đổi tình huống (phỏng vấn, khiếu nại, thuyết trình) để luyện đa dạng ngữ cảnh, không chỉ một kịch bản quen thuộc.""",
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

## Ví dụ: "Blockchain là gì?"

- 🧒 Giống một cuốn sổ ghi chép mà ai cũng có một bản y hệt — muốn sửa một dòng thì phải sửa ở tất cả các cuốn cùng lúc, nên gần như không ai gian lận được.
- 🎓 Là một cấu trúc dữ liệu dạng chuỗi khối, mỗi khối chứa hash của khối trước, được đồng thuận xác nhận bởi nhiều node phân tán...
- 🔬 Các cơ chế đồng thuận (PoW, PoS...) đánh đổi giữa bảo mật, phi tập trung và khả năng mở rộng (Blockchain Trilemma)...

> 💡 Nếu vẫn thấy mơ hồ ở cấp độ 2, quay lại hỏi sâu thêm câu hỏi cụ thể ngay tại cấp độ đó, đừng nhảy lên cấp độ 3 vội.""",
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

## Ví dụ (rút gọn): "Học Python trong 8 tuần, 5h/tuần, mục tiêu làm được project quản lý chi tiêu cá nhân"

| Tuần | Chủ đề | Checkpoint |
|---|---|---|
| 1 | Cú pháp cơ bản, biến, kiểu dữ liệu | Viết chương trình tính tiền điện đơn giản |
| 2 | Cấu trúc điều khiển, vòng lặp | Viết chương trình đoán số |
| ... | ... | ... |
| 8 | Ghép nối toàn bộ project | Hoàn thành app quản lý chi tiêu chạy được |

> 💡 Sau mỗi tuần thực tế, quay lại báo cáo với AI bạn đã làm được gì/khó ở đâu, xin điều chỉnh lộ trình tuần sau — đừng theo lộ trình cứng nhắc nếu thực tế lệch tiến độ.""",
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

## Ví dụ

> **Bạn**: "Tại sao code của tôi bị lỗi 'index out of range'?"
>
> **AI**: "Bạn nghĩ vòng lặp của bạn đang chạy từ giá trị nào đến giá trị nào? Và mảng của bạn có bao nhiêu phần tử?"
>
> **Bạn**: (tự kiểm tra) "À, vòng lặp chạy đến index bằng độ dài mảng, nhưng index cuối cùng phải nhỏ hơn độ dài 1 đơn vị!"
>
> **AI**: "Chính xác! Bạn đã tìm ra nguyên nhân."

> 💡 Kỹ thuật này đặc biệt hiệu quả khi debug code hoặc giải bài tập — bạn nhớ lâu hơn nhiều so với việc được đưa đáp án ngay.""",
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

## Ví dụ

Đầu vào: abstract của một bài báo giả định về mô hình dự đoán thời tiết bằng AI.

Đầu ra mẫu:
1. **Vấn đề**: Dự báo thời tiết ngắn hạn (24h) chính xác hơn ở khu vực địa hình phức tạp.
2. **Phương pháp**: Kết hợp dữ liệu vệ tinh với mạng nơ-ron tích chập (CNN).
3. **Kết quả chính**: Giảm 15% sai số so với mô hình truyền thống.
4. **Hạn chế**: Chỉ thử nghiệm ở một khu vực địa lý, chưa rõ khả năng tổng quát hoá.
5. **Vì sao quan trọng**: Có thể cải thiện cảnh báo sớm thiên tai ở vùng núi.

> 💡 Chỉ dùng cách này để **quyết định có nên đọc sâu hay không** — với tài liệu quan trọng, vẫn nên tự đọc kỹ phần Kết quả và Phương pháp, không hoàn toàn dựa vào tóm tắt AI.""",
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

## Ví dụ

Input ý chính: "xin dời deadline dự án A thêm 3 ngày, lý do đối tác chậm gửi dữ liệu, cam kết bàn giao đúng chất lượng."

Output:
> Chào anh/chị [tên],
>
> Em viết email này để xin phép dời deadline bàn giao dự án A thêm 3 ngày, dự kiến hoàn thành vào [ngày]. Nguyên nhân là phía đối tác chưa gửi đủ dữ liệu đầu vào cần thiết, dù nhóm đã chủ động nhắc nhở từ tuần trước.
>
> Em cam kết vẫn đảm bảo chất lượng bàn giao như kế hoạch ban đầu. Rất mong anh/chị thông cảm và hỗ trợ.
>
> Em cảm ơn anh/chị.

> 💡 Với email nhạy cảm (từ chối, phàn nàn, xin lỗi), luôn tự đọc lại và chỉnh sửa trước khi gửi — đừng gửi thẳng bản AI viết.""",
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

## Ví dụ

Từ ghi chú họp lộn xộn về việc ra mắt tính năng mới, AI có thể trích ra:

| Việc cần làm | Người phụ trách | Hạn chót | Ưu tiên |
|---|---|---|---|
| Hoàn thiện thiết kế UI màn hình thanh toán | Lan | Thứ Sáu tuần này | Cao |
| Viết test case cho luồng thanh toán | Chưa rõ — cần xác nhận lại | — | Trung bình |

**Vấn đề còn bỏ ngỏ**: chưa thống nhất được ngân sách quảng cáo cho đợt ra mắt.

> 💡 Gửi ngay bảng này vào nhóm chat sau họp — càng sớm càng giảm khả năng "quên" việc đã thống nhất.""",
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

## Ví dụ so sánh

**Mô tả mơ hồ** (khó debug đúng): *"API của tôi trả về lỗi 500, không biết tại sao."*

**Mô tả đầy đủ** (dễ debug đúng): nêu rõ endpoint, đoạn code xử lý request, traceback đầy đủ có dòng lỗi cụ thể (ví dụ `KeyError: 'user_id'` tại dòng nào), và thông tin "tôi đã thử log request body ra thì thấy thiếu field user_id trong một số trường hợp".

Với mô tả đầy đủ, AI có thể chỉ thẳng: cần validate input trước khi truy cập `request['user_id']`, thay vì đoán chung chung nhiều khả năng không liên quan.

> 💡 Luôn dán **nguyên văn** thông báo lỗi, đừng diễn giải lại bằng lời của bạn — nhiều chi tiết quan trọng (tên exception, số dòng) dễ bị mất khi tóm tắt.""",
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

## Ví dụ

Đánh dấu chỉ cần review "Bảo mật" cho một endpoint nhận input người dùng, AI có thể phản hồi tập trung:

> **Dòng 14**: Query SQL được ghép chuỗi trực tiếp từ `request.args['id']` → có nguy cơ SQL Injection. Đề xuất: dùng parameterized query (`cursor.execute("... WHERE id = %s", (id,))`) thay vì f-string.

Thay vì lan man góp ý cả về đặt tên biến hay style code — vốn không phải điều bạn đang cần lúc này.

> 💡 Với code liên quan bảo mật/dữ liệu nhạy cảm, luôn coi gợi ý AI là điểm khởi đầu để kiểm tra kỹ hơn, không phải kết luận cuối cùng.""",
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

## Ví dụ

Từ một hàm Python `def create_user(email: str, password: str) -> User`, AI có thể sinh:

```
'''Tạo người dùng mới trong hệ thống.

Args:
    email (str): Email người dùng, bắt buộc, phải đúng định dạng email.
    password (str): Mật khẩu, tối thiểu 8 ký tự.

Returns:
    User: Đối tượng người dùng vừa được tạo, gồm id và email.

Raises:
    ValueError: Nếu email đã tồn tại trong hệ thống.
    ValidationError: Nếu email sai định dạng hoặc password quá ngắn.
'''
```

> 💡 Sau khi AI sinh docs, luôn đối chiếu lại với code thật — đảm bảo AI không "đoán" thêm ca lỗi không tồn tại hoặc bỏ sót ca lỗi thật sự có trong code.""",
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

## Ví dụ (rút gọn)

| Slide | Thông điệp chính | Nội dung hỗ trợ |
|---|---|---|
| 1 | 30% khách hàng rời bỏ vì thời gian phản hồi chậm | Số liệu khảo sát gần nhất |
| 2 | Giải pháp X giảm thời gian phản hồi từ 2 ngày xuống 2 giờ | So sánh trước/sau, demo ngắn |
| ... | ... | ... |
| N | Cần duyệt ngân sách Y để triển khai trong Q3 | Lời kêu gọi hành động cụ thể |

> 💡 Nếu một slide không có nổi "một thông điệp chính" rõ ràng — đó là dấu hiệu nên tách thành 2 slide hoặc bỏ bớt nội dung.""",
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

## Ví dụ

> **Insight 1**: Doanh số tháng 6 giảm 18% so với tháng 5, riêng ở nhóm khách hàng mới.
> → Ý nghĩa: có thể chiến dịch marketing thu hút khách mới đang kém hiệu quả hơn, không phải vấn đề giữ chân khách cũ.
> → Đề xuất: kiểm tra lại hiệu suất kênh marketing tháng 6 trước khi cắt giảm ngân sách chung.

> 💡 Luôn tự kiểm tra lại các con số quan trọng AI trích ra — với dữ liệu lớn, AI có thể đọc nhầm hàng/cột hoặc tính sai phần trăm.""",
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

## Ví dụ

Với kế hoạch "ra mắt tính năng mới trong 2 tháng", AI có thể phản biện:

> 1. "Nếu đối tác cung cấp dữ liệu chậm trễ như đợt trước, kế hoạch 2 tháng còn khả thi không? Bạn có phương án dự phòng nào?"
> 2. "Ngân sách marketing dự kiến dựa trên giả định tỷ lệ chuyển đổi 5% — con số này lấy từ đâu, có đủ tin cậy không?"

> 💡 Sau khi nhận danh sách câu hỏi, tự viết câu trả lời cho từng câu — đây chính là phần chuẩn bị giá trị nhất, không phải danh sách câu hỏi.""",
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

## Ví dụ: Template viết mô tả sản phẩm cho shop online

```
Bạn là copywriter chuyên viết mô tả sản phẩm thương mại điện tử,
giọng văn gần gũi, tạo cảm giác muốn mua ngay nhưng không nói quá.

Với mỗi sản phẩm, luôn viết theo cấu trúc:
1. Một câu mở đầu gây chú ý
2. 3 gạch đầu dòng lợi ích chính (không phải tính năng khô khan)
3. Một câu kêu gọi hành động

Sản phẩm lần này: {{tên sản phẩm, đặc điểm chính, giá}}
```

Mỗi lần có sản phẩm mới, chỉ cần thay phần `{{...}}` — không cần viết lại toàn bộ hướng dẫn phong cách.

> 💡 Lưu các template này lại (ví dụ làm Custom Agent trong ứng dụng) thay vì gõ lại từ đầu mỗi lần — tiết kiệm thời gian và giữ output nhất quán.""",
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

## Ví dụ khung SWOT (rút gọn, ngành F&B)

- **Điểm mạnh** cần kiểm tra: đối thủ có lợi thế về vị trí cửa hàng, giá, hay thương hiệu?
- **Điểm yếu** cần kiểm tra: đánh giá khách hàng trên các nền tảng review có điểm chung nào bị phàn nàn không?
- Nguồn nên tra cứu thật: báo cáo ngành từ đơn vị nghiên cứu thị trường uy tín, đánh giá công khai trên Google Maps/app đặt đồ ăn, báo cáo tài chính công khai (nếu là công ty niêm yết).

> 🚩 **Luôn tự kiểm chứng**: bất kỳ con số cụ thể nào (thị phần %, doanh thu, số lượng khách hàng) do AI đưa ra mà không trích nguồn rõ ràng — coi như chưa được xác minh, không đưa thẳng vào báo cáo chính thức.""",
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

## Ví dụ (rút gọn): Ra mắt website mới trong 6 tuần

| Milestone | Ngày | Bằng chứng hoàn thành | Rủi ro chính |
|---|---|---|---|
| Chốt thiết kế UI/UX | Tuần 2 | File thiết kế được duyệt bởi stakeholder | Chờ phản hồi duyệt kéo dài |
| Hoàn thành phát triển | Tuần 5 | Website chạy được trên môi trường staging | Phát sinh yêu cầu ngoài phạm vi ban đầu |
| Ra mắt chính thức | Tuần 6 | Website live trên domain thật | Lỗi phát sinh phút chót khi go-live |

> 💡 Sau mỗi milestone, dành 15 phút nhìn lại: đúng tiến độ hay không, nếu trễ thì điều chỉnh milestone tiếp theo ngay, đừng đợi đến cuối dự án mới xử lý.""",
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

## Ví dụ

Mục tiêu mơ hồ: "Tôi muốn khỏe hơn."

→ Mục tiêu SMART: "Chạy bộ được liên tục 5km trong 8 tuần tới, tập tối thiểu 3 buổi/tuần."
- **Specific**: chạy bộ, cự ly 5km cụ thể
- **Measurable**: đo được bằng quãng đường/thời gian chạy
- **Achievable**: hợp lý nếu hiện tại đã chạy được 2-3km
- **Relevant**: gắn với mục tiêu "khỏe hơn"
- **Time-bound**: 8 tuần

Các bước hành động: Tuần 1-2 chạy 2km x 3 buổi/tuần → Tuần 3-4 tăng lên 3km → ... → Tuần 8 đạt 5km liên tục.

> 💡 Nếu bước hành động đầu tiên vẫn cảm thấy "khó bắt đầu ngay hôm nay", hãy yêu cầu AI chia nhỏ tiếp bước đó — dấu hiệu nó vẫn chưa đủ cụ thể.""",
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

## Ví dụ kết quả

| Nhóm | Số tiền | % thu nhập | Khung tham khảo |
|---|---|---|---|
| Thiết yếu | 12.000.000đ | 60% | 50% |
| Cá nhân/Giải trí | 6.000.000đ | 30% | 30% |
| Tiết kiệm | 2.000.000đ | 10% | 20% |

→ Nhận xét: nhóm Thiết yếu đang cao hơn khung tham khảo 10%, nhóm Tiết kiệm đang thấp hơn 10% — có thể xem lại các khoản thiết yếu (ví dụ tiền nhà, hoá đơn) có khoản nào tối ưu được không.

> 💡 Đây là công cụ giúp bạn **nhìn rõ số liệu**, quyết định cắt giảm/đầu tư khoản nào vẫn nên dựa trên hoàn cảnh thực tế và, nếu cần, ý kiến chuyên gia.""",
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

## Ví dụ (rút gọn): Đà Lạt 3 ngày 2 đêm, ngân sách 3 triệu/người, thích ẩm thực

| Ngày | Sáng | Chiều | Tối | Chi phí ước tính |
|---|---|---|---|---|
| 1 | Nhận phòng, chợ Đà Lạt | Hồ Xuân Hương | Lẩu bò, chợ đêm | ~500.000đ |
| 2 | Đồi chè Cầu Đất | Thung lũng Tình Yêu | Nhà hàng đặc sản | ~800.000đ |
| 3 | Mua đặc sản | Trả phòng, ra sân bay | — | ~300.000đ |

> 💡 Giá cả, giờ mở cửa AI đưa ra có thể đã lỗi thời — luôn kiểm tra lại thông tin quan trọng (giờ mở cửa, giá vé) trước khi khởi hành, đặc biệt với các địa điểm có thể đã thay đổi.""",
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

## Ví dụ

- "Trả lời email khách hàng phàn nàn" → **Làm ngay** (khẩn cấp + quan trọng, ảnh hưởng uy tín).
- "Học khóa học nâng cao kỹ năng quý sau" → **Lên lịch** (quan trọng nhưng không gấp).
- "Đặt lịch họp giúp đồng nghiệp" → **Giao việc** (gấp nhưng không cần chính bạn làm).
- "Dọn hộp thư rác" → **Loại bỏ hoặc làm sau cùng**.

> 💡 Phần lớn giá trị dài hạn nằm ở ô "Lên lịch" — nhưng đây cũng là ô dễ bị bỏ quên nhất vì không có deadline gấp. Chủ động dành thời gian cố định mỗi tuần cho ô này.""",
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

## Ví dụ: Chọn giữa 2 lời mời làm việc

| Tiêu chí (trọng số) | Offer A | Offer B |
|---|---|---|
| Lương (x3) | 4 → 12 | 5 → 15 |
| Cơ hội học hỏi (x2) | 5 → 10 | 3 → 6 |
| Khoảng cách di chuyển (x1) | 3 → 3 | 5 → 5 |
| **Tổng có trọng số** | **25** | **26** |

→ Sát nút, gần như tương đương — có thể tiêu chí thứ 4 chưa được liệt kê (ví dụ văn hoá công ty) mới là yếu tố quyết định thực sự.

> 💡 Nếu điểm tổng hai lựa chọn quá sát nhau, đó là dấu hiệu bạn nên tìm thêm tiêu chí quan trọng đang bị bỏ sót, thay vì chọn đại theo điểm số.""",
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

## Ví dụ (rút gọn): Ra mắt sản phẩm mới

| Nguyên nhân thất bại giả định | Hành động phòng ngừa ngay |
|---|---|
| Đối tác cung cấp nguyên liệu giao trễ | Ký hợp đồng có điều khoản phạt trễ, tìm thêm nhà cung cấp dự phòng |
| Đội ngũ bán hàng chưa được đào tạo kịp | Lên lịch đào tạo hoàn tất trước ngày ra mắt ít nhất 1 tuần |
| Nhu cầu thị trường thấp hơn dự đoán | Chạy khảo sát/pre-order nhỏ trước khi sản xuất số lượng lớn |

> 💡 Premortem hiệu quả nhất khi làm **trước khi bắt đầu** dự án, lúc vẫn còn dễ điều chỉnh kế hoạch — làm giữa chừng vẫn có ích nhưng ít lựa chọn xử lý hơn.""",
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

## Ví dụ (rút gọn): Ôn thi trong 3 tuần

| Tuần | Nội dung |
|---|---|
| 1 | Học chương 1-3 (mới), cuối tuần ôn lại chương 1 |
| 2 | Học chương 4-6 (mới), ôn lại chương 2-3, có 1 ngày buffer |
| 3 | Ôn tổng hợp toàn bộ, làm đề thi thử 2 lần, 2 ngày cuối chỉ xem lại lỗi sai |

> 💡 Sau mỗi tuần, báo lại tiến độ thực tế cho AI (học kịp hay chậm) và xin điều chỉnh lịch tuần sau — lịch ban đầu chỉ là dự kiến, không phải cố định.""",
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

## Ví dụ

Thói quen: "đọc sách 20 phút/ngày". Lịch trình có sẵn: "luôn uống cà phê sáng lúc 7h trước khi đi làm".

→ Đề xuất: đọc sách ngay trong lúc uống cà phê sáng (gắn vào mốc có sẵn, không cần nhớ thêm mốc mới).
→ Theo dõi: bảng 7 ô mỗi tuần, tick ✅ nếu đọc, để ở nơi dễ thấy.
→ Phiên bản tối thiểu ngày bận: chỉ cần đọc 2 trang, miễn không bỏ hẳn — giữ chuỗi liên tục quan trọng hơn số lượng mỗi ngày.

> 💡 Cuối mỗi tuần, báo cáo lại với AI số ngày duy trì được — nếu liên tục bỏ lỡ, thử hỏi AI điều chỉnh mốc gắn hoặc phiên bản tối thiểu, thay vì cố ép bản thân theo kế hoạch không thực tế.""",
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

## Ví dụ (rút gọn): Tổ chức workshop nội bộ 50 người

**Trước** (trước 3 tuần): chốt địa điểm & ngày → (trước 2 tuần) gửi lời mời, chốt số lượng tham dự → (trước 3 ngày) chuẩn bị tài liệu, xác nhận lại với địa điểm.

**Trong**: check-in người tham dự, quay video/chụp ảnh, thu phản hồi trực tiếp cuối buổi.

**Sau**: gửi email cảm ơn + tài liệu buổi workshop (trong vòng 2 ngày), tổng hợp phản hồi, thanh toán chi phí phát sinh, lưu trữ tài liệu cho lần tổ chức sau.

> 💡 Giai đoạn "Sau" là nơi dễ bị bỏ quên nhất khi mọi người đã "thở phào" xong sự kiện — nên giao rõ người phụ trách các việc hậu kỳ ngay từ đầu, đừng để "ai rảnh thì làm".""",
    },
]
