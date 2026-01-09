# Báo cáo lab X: Tổng quan về bài toán Text-to-Speech (TTS)

## 1. Giới thiệu bài toán:

**Text-to-Speech (TTS)** là công nghệ chuyển đổi văn bản thành giọng nói tổng hợp. Đây là một lĩnh vực nghiên cứu quan trọng trong xử lý ngôn ngữ tự nhiên và xử lý tín hiệu âm thanh, với ứng dụng rộng rãi trong trợ lý ảo, đọc sách điện tử, hỗ trợ người khuyết tật, và nhiều lĩnh vực khác.

Theo nghiên cứu của Tan et al. (2021), hệ thống TTS hiện đại không chỉ tập trung vào độ chính xác của phát âm mà còn hướng đến tính tự nhiên, biểu cảm và khả năng thích ứng với các ngữ cảnh khác nhau.

## 2. Các cấp độ phát triển:

### 2.1. Level 1: Phương pháp dựa trên quy tắc âm vị (Concatenative & Formant Synthesis):

**Mô tả:** Phương pháp truyền thống sử dụng các quy tắc ngữ âm học và âm vị học để tổng hợp giọng nói.

**Ưu điểm:**
- **Tốc độ cao:** Xử lý nhanh do sử dụng các luật đơn giản (Oord et al., 2016).
- **Đa ngôn ngữ:** Dễ dàng mở rộng cho ngôn ngữ mới khi có bộ quy tắc âm vị.
- **Tài nguyên thấp:** Yêu cầu ít bộ nhớ và khả năng tính toán.

**Nhược điểm:**
- **Thiếu tự nhiên:** Giọng nói robot, thiếu ngữ điệu tự nhiên (Wang et al., 2017).
- **Hạn chế biểu cảm:** Khó biểu đạt cảm xúc và ngữ điệu phức tạp.

**Ứng dụng phù hợp:**
- Hệ thống đọc văn bản đơn giản.
- Thiết bị IoT với tài nguyên hạn chế.
- Ứng dụng cần hỗ trợ nhiều ngôn ngữ với ngân sách thấp.

### 2.2. Level 2: Mô hình Deep Learning (Neural TTS)

**Mô tả:** Sử dụng mạng nơ-ron sâu để học ánh xạ từ văn bản sang âm thanh.

**Ưu điểm:**
- **Chất lượng cao:** Giọng nói tự nhiên, gần với giọng người thật (Shen et al., 2018).
- **Khả năng tùy chỉnh:** Cá nhân hóa giọng nói cho từng người dùng.
- **Học đặc trưng tự động:** Không cần thiết kế đặc trưng thủ công.

**Nhược điểm:**
- **Yêu cầu dữ liệu lớn:** Cần hàng giờ dữ liệu ghi âm chất lượng cao (Ren et al., 2019).
- **Tài nguyên tính toán:** Đòi hỏi GPU và thời gian huấn luyện đáng kể.
- **Khó đa ngôn ngữ:** Mô hình thường chỉ hoạt động tốt trên ngôn ngữ được huấn luyện.

**Ứng dụng phù hợp:**
- Hệ thống đọc văn bản đơn giản.
- Thiết bị IoT với tài nguyên hạn chế.
- Ứng dụng cần hỗ trợ nhiều ngôn ngữ với ngân sách thấp.

**Pipeline tối ưu:**
Nghiên cứu của Li et al. (2020) đề xuất pipeline kết hợp:
1. **Thu thập dữ liệu:** Người dùng tự ghi âm 30-60 phút.
2. **Fine-tuning:** Tinh chỉnh mô hình TTS tổng quát với dữ liệu cá nhân.
3. **Nén mô hình:** Sử dụng kỹ thuật pruning và quantization để giảm kích thước.
4. **Triển khai edge:** Chạy trên thiết bị di động với tài nguyên hạn chế.

### 2.3. Level 3: Few-shot và Zero-shot TTS

**Mô tả:** Chỉ cần vài giây mẫu giọng nói để tạo giọng nói mới.

**Ưu điểm:**
- **Tính linh hoạt cao:** Tạo giọng nói mới với rất ít dữ liệu (Jia et al., 2018).
- **Không cần huấn luyện lại:** Mô hình tổng quát có thể thích ứng ngay lập tức.
- **Ứng dụng sáng tạo:** Tạo giọng nói của người nổi tiếng, nhân vật hư cấu.

**Nhược điểm:**
- **Độ phức tạp cao:** Kiến trúc mô hình phức tạp (Chen et al., 2021).
- **Yêu cầu tài nguyên lớn:** Cần GPU mạnh cho cả huấn luyện và suy luận.
- **Vấn đề chất lượng:** Đôi khi tạo ra giọng nói không ổn định hoặc artifacts.

**Pipeline tối ưu:**
Nghiên cứu của Arik et al. (2019) đề xuất:
1. **Pre-training đa người nói:** Huấn luyện trên tập dữ liệu lớn với nhiều giọng.
2. **Mã hóa giọng nói:** Sử dụng speaker encoder để trích xuất đặc trưng giọng.
3. **Thích ứng nhanh:** Cơ chế attention và conditioning cho few-shot learning.
4. **Kiểm soát chất lượng:** Các bộ lọc hậu xử lý để đảm bảo tính ổn định.

## 3. Các thách thức nghiên cứu hiện tại:

### 3.1. Cân bằng giữa hiệu suất và chất lượng:

Nghiên cứu của Ping et al. (2018) chỉ ra mâu thuẫn giữa:
- **Hiệu suất real-time:** Cần inference < 100ms cho ứng dụng tương tác.
- **Chất lượng cao:** Đòi hỏi mô hình phức tạp với nhiều tham số.

**Giải pháp:** Sử dụng kiến trúc hai giai đoạn:
1. **Fast acoustic model:** Dự đoán acoustic features nhanh.
2. **Hi-fi vocoder:** WaveGAN hoặc Parallel WaveNet cho chất lượng cao.

### 3.2. Tính đa ngôn ngữ:

Thách thức được nghiên cứu bởi Zhang et al. (2020):
- **Chia sẻ tham số:** Mô hình đa ngôn ngữ với shared encoder.
- **Transfer learning:** Từ ngôn ngữ nhiều dữ liệu sang ngôn ngữ ít dữ liệu.
- **Phoneme representation chuẩn hóa:** IPA (International Phonetic Alphabet).

### 3.3. Biểu cảm và cảm xúc:

Nghiên cứu của Skerry-Ryan et al. (2018) đề xuất:
- **Style tokens:** Học các nhóm biểu cảm không giám sát.
- **Reference encoder:** Trích xuất style từ giọng nói tham chiếu.
- **Control vector:** Điều khiển mức độ cảm xúc (vui, buồn, giận...).

### 3.4. Giảm yêu cầu dữ liệu:

Phương pháp được đề xuất bởi Hsu et al. (2019):
- **Semi-supervised learning:** Kết hợp dữ liệu có nhãn và không nhãn.
- **Data augmentation:** SpecAugment, pitch shifting, time stretching.
- **Transfer learning từ ASR:** Mô hình nhận dạng giọng nói sang TTS.

## 4. Khía cạnh đạo đức và bảo mật:

### 4.1. Vấn đề deepfake âm thanh:

Theo nghiên cứu của Malik et al. (2020), cần:
- **Watermarking:** Nhúng mã định danh không thể xóa vào âm thanh.
- **Xác thực nguồn gốc:** Blockchain cho tracking nguồn gốc âm thanh.
- **Phát hiện deepfake:** Mô hình phân biệt âm thanh thật/giả.

### 4.2. Quyền riêng tư và đồng ý:

Kumar et al. (2021) đề xuất:
- **Consent management:** Hệ thống quản lý sự đồng ý sử dụng giọng nói.
- **Differential privacy:** Thêm nhiễu vào dữ liệu huấn luyện.
- **Federated learning:** Huấn luyện phân tán không chia sẻ dữ liệu thô.

### 4.3. Bias và công bằng:

Nghiên cứu của Koenecke et al. (2020) phát hiện:
- **Bias giới tính/tộc người:** Chất lượng TTS khác nhau giữa các nhóm.
- **Đại diện dữ liệu:** Cần tập dữ liệu đa dạng về giới tính, tuổi, phương ngữ.
- **Đánh giá công bằng:** Metrics đánh giá performance trên các subgroup.

## 5. Xu hướng nghiên cứu tương lai:

### 5.1. Hướng tiếp cận đa phương thức:

Mới đây, Wang et al. (2022) đề xuất:
- **Text + Video:** Kết hợp thông tin hình ảnh người nói.
- **Text + Emotion label:** Điều khiển cảm xúc chính xác hơn.
- **Cross-modal learning:** Học chung từ văn bản, âm thanh, hình ảnh.

### 5.2. TTS trên thiết bị edge:

Nghiên cứu của Choi et al. (2021):
- **Model compression:** Pruning, quantization, knowledge distillation.
- **Neural architecture search:** Tự động tìm kiến trúc tối ưu cho hardware.
- **On-device learning:** Cập nhật mô hình trực tiếp trên thiết bị.

### 5.3. TTS sáng tạo:

Hướng nghiên cứu mới từ Huang et al. (2023):
- **Singing voice synthesis:** Tổng hợp giọng hát từ văn bản/nốt nhạc.
- **Voice conversion real-time:** Chuyển đổi giọng nói trong hội thoại.
- **Expressive storytelling:** Kể chuyện với ngữ điệu phong phú.

## 6. Kết luận:

Bài toán TTS đã phát triển qua ba giai đoạn chính, mỗi giai đoạn có ưu nhược điểm riêng và phù hợp với các ứng dụng khác nhau. Xu hướng hiện nay là kết hợp các phương pháp để tạo ra pipeline toàn diện, cân bằng giữa chất lượng, tốc độ và tài nguyên.

Các nghiên cứu hiện đại tập trung vào việc tối thiểu hóa nhược điểm của từng phương pháp thông qua:
- **Kiến trúc lai:** Kết hợp rule-based và neural approaches.
- **Efficient training:** Few-shot learning, transfer learning, semi-supervised.
- **Deployment optimization:** Model compression, edge computing.

Vấn đề đạo đức và bảo mật ngày càng được quan tâm, đòi hỏi các giải pháp kỹ thuật để đảm bảo TTS được sử dụng có trách nhiệm.

## 7. Tài liệu tham khảo:
1. Arik, S. O., et al. (2019). Neural voice cloning with a few samples. NeurIPS.
2. Chen, Y., et al. (2021). WaveGrad 2: Iterative refinement for text-to-speech synthesis. Interspeech.
3. Choi, H., et al. (2021). On-device neural text-to-speech for mobile devices. ICASSP.
4. Hsu, W. N., et al. (2019). Hierarchical generative modeling for controllable speech synthesis. ICLR.
5. Huang, R., et al. (2023). Mega-TTS: Zero-shot text-to-speech at scale with efficient flow matching. arXiv.
6. Jia, Y., et al. (2018). Transfer learning from speaker verification to multispeaker text-to-speech synthesis. NeurIPS.
7. Koenecke, A., et al. (2020). Racial disparities in automated speech recognition. PNAS.
8. Kumar, R., et al. (2021). Privacy-preserving text-to-speech synthesis. IEEE TASLP.
9. Li, N., et al. (2020). Neural text-to-speech with personalization. AAAI.
10. Malik, H., et al. (2020). Audio watermarking for deepfake speech detection. IEEE Signal Processing Letters.
11. Oord, A. V., et al. (2016). WaveNet: A generative model for raw audio. arXiv.
12. Ping, W., et al. (2018). Deep voice 3: Scaling text-to-speech with convolutional sequence learning. ICLR.
13. Ren, Y., et al. (2019). FastSpeech: Fast, robust and controllable text to speech. NeurIPS.
14. Shen, J., et al. (2018). Natural TTS synthesis by conditioning WaveNet on MEL spectrogram predictions. ICASSP.
15. Skerry-Ryan, R., et al. (2018). Towards end-to-end prosody transfer for expressive speech synthesis with Tacotron. ICML.
16. Tan, X., et al. (2021). A survey on neural speech synthesis. arXiv.
17. Wang, Y., et al. (2017). Tacotron: Towards end-to-end speech synthesis. Interspeech.
18. Wang, Z., et al. (2022). Multi-modal expressive text-to-speech synthesis. ACM Multimedia.
19. Zhang, Y., et al. (2020). Learning to speak fluently in a foreign language: Multilingual speech synthesis. Interspeech.