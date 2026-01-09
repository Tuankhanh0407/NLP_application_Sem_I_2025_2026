# Báo cáo lab 1: Triển khai Tokenization và Count Vectorization.

## 1. Quy trình triển khai:

### 1.1. Phân tích yêu cầu:
- **Tokenization:** Xử lý tách văn bản thành các đơn vị nhỏ hơn (tokens).
- **Count Vectorization:** Chuyển đổi văn bản thành biểu diễn số dưới dạng vector.

### 1.2. Thiết kế kiến trúc:
Chương trình được thiết kế theo mô hình mô-đun hóa với các thành phần chính:
```
src/
├── core/
│   ├── interfaces.py       # Abstract classes
│   └── dataset_loaders.py  # Data loading utilities
├── preprocessing/
│   ├── simple_tokenizer.py # Simple tokenizer
│   └── regex_tokenizer.py  # Regex-based tokenizer
├── representations/
│   └── count_vectorizer.py # Count vectorizer
└── main_test_lab_1.py      # Main demo program
```

### 1.3. Triển khai chi tiết:

#### 1.3.1. Interfaces (Abstract Classes)
- **Tokenizer:** Abstract class định nghĩa interface cho các tokenizer.
- **Vectorizer:** Abstract class định nghĩa interface cho các vectorizer.

#### 1.3.2. Tokenizer Implementations
- **SimpleTokenizer:** Tokenizer đơn giản sử dụng tách theo khoảng trắng và dấu câu.
- **RegexTokenizer:** Tokenizer sử dụng cấu trúc biểu thức chính quy để xử lý từ rút gọn và dấu câu.

#### 1.3.3. Count Vectorizer
- **CountVectorizer:** Triển khai bag-of-words với các phương thức fit/transform.

#### 1.3.4. Data Loading
- **load_raw_text_data():** Tự động tải dữ liệu UD_English-EWT từ GitHub repository.

## 2. Cách chạy code và ghi log kết quả:

### 2.1. Cài đặt môi trường:
```
# Tạo file requirements.txt
echo "requests" > requirements.txt

# Cài đặt dependencies
pip install --upgrade -r requirements.txt
```
### 2.2. Chạy chương trình:
```
# Chạy chương trình chính
python src/main_test_lab_1.py

# Ghi log kết quả ra file
python src/main_test_lab_1.py > output.log
```
### 2.3. Cấu trúc chương trình chính:
Chương trình `main_test_lab_1.py` bao gồm 3 phần demo:
1. Demo tokenizers trên các câu mẫu.
2. Demo tokenizers trên dữ liệu UD_English-EWT.
3. Demo count vectorizer.

## 3. Giải thích kết quả thu được:

### 3.1. Kết quả tokenization:

**Câu 1:** "Hello, world! This is a test."
- **SimpleTokenizer:** `['hello', ',', 'world', '!', 'this', 'is', 'a', 'test', '.']`
- **RegexTokenizer:** `['hello', ',', 'world', '!', 'this', 'is', 'a', 'test', '.']`
**Nhận xét:** Cả hai tokenizer cho kết quả giống nhau với câu đơn giản này.

**Câu 2:** "NLP is fascinating... isn't it?"
- **SimpleTokenizer:** `['nlp', 'is', 'fascinating', '.', '.', '.', 'isn', "'", 't', 'it', '?']`
- **RegexTokenizer:** `['nlp', 'is', 'fascinating', '.', '.', '.', "isn't", 'it', '?']`
**Nhận xét:**
- SimpleTokenizer tách "isn't" thành 3 tokens: `'isn'`, `"'"`, `'t'`.
- RegexTokenizer giữ nguyên "isn't" như một token duy nhất.
- Điều này cho thấy RegexTokenizer xử lý từ rút gọn tốt hơn.

**Câu 3:** "Let's see how it handles 123 numbers and punctuation!"
- **SimpleTokenizer:** `['let', "'", 's', 'see', 'how', 'it', 'handles', '123', 'numbers', 'and', 'punctuation', '!']`
- **RegexTokenizer:** `["let's", 'see', 'how', 'it', 'handles', '123', 'numbers', 'and', 'punctuation', '!']`
**Nhận xét:** Tương tự câu trên, RegexTokenizer xử lý contraction "let's" tốt hơn.

### 3.2. Kết quả trên UD_English-EWT:
**Đoạn văn bản mẫu:** "Al-Zaman : American forces killed Shaikh Abdullah al-Ani, the preacher at the mosque in the town of qaim, ..."
- **SimpleTokenizer:** Giữ nguyên từ ghép ngăn cách bởi dấu gạch ngang (-) như "al-zaman", "al-ani".
- **RegexTokenizer:** Tách từ ghép ngăn cách bởi dấu gạch ngang (-) thành các phần riêng biệt.
**Nhận xét:** Sự khác biệt này phụ thuộc vào cấu trúc biểu thức chính quy sử dụng.

### 3.3. Kết quả Count Vectorizer:
**Vocabulary học được:**
```
0: .     1: a     2: ai    3: i     4: is
5: love  6: nlp   7: of    8: programming  9: subfield
```
**Document-term matrix:**
- **Document 0 ("I love NLP."):** `[1, 0, 0, 1, 0, 1, 1, 0, 0, 0]`
- **Document 1 ("I love programming."):** `[1, 0, 0, 1, 0, 1, 0, 0, 1, 0]`
- **Document 2 ("NLP is a subfield of AI."):** `[1, 1, 1, 0, 1, 0, 1, 1, 0, 1]`
**Giải thích:**
- Mỗi vector có độ dài 10 (số lượng terms trong vocabulary).
- Giá trị tại mỗi vị trí là số lần xuất hiện của term tương ứng.
- Ví dụ: Document 0 có term "nlp" (index 6) xuất hiện 1 lần.

## 4. Khó khăn gặp phải và cách giải quyết:

### 4.1. Tải dữ liệu tự động từ internet:
- **Vấn đề:** Cần tải dữ liệu UD_English-EWT mà không yêu cầu người dùng tải thủ công.
- **Giải pháp:** Sử dụng thư viện `requests` để tải trực tiếp từ GitHub repository.

### 4.2. Xử lý định dạng .conllu:
- **Vấn đề:** Định dạng .conllu chứa nhiều thông tin annotation, cần trích xuất chỉ phần text.
- **Giải pháp:** Đọc và xử lý từng dòng trong tệp, tìm các dòng bắt đầu bằng "# text =" để trích xuất câu.

### 4.3. Tokenization của từ rút gọn:
- **Vấn đề:** SimpleTokenizer tách từ rút gọn như "isn't" thành nhiều phần không mong muốn.
- **Giải pháp:** Sử dụng cấu trúc biểu thức chính quy `[A-Za-z0-9]+(?:'[A-Za-z0-9]+)*` trong RegexTokenizer.

## 5. Nguồn tham khảo:
1. **Universal Dependencies Project:** https://universaldependencies.org/
2. **UD_English-EWT repository:** https://github.com/UniversalDependencies/UD_English-EWT
3. **Python Regular Expressions:** https://docs.python.org/3/library/re.html
4. **Requests library:** https://docs.python-requests.org/
5. **Contractions handling pattern:** https://www.nltk.org/api/nltk.tokenize.html

## 6. Model tạo sẵn:
Chương trình này **không sử dụng bất kỳ model tạo sẵn nào**, tất cả thành phần đều được triển khai từ đầu.
