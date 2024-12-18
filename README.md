### Chuẩn bị
- cần tải các thư viện: pip install matplotlib,... như trong src
- tải graphviz (lên gg), và phải thêm Graphviz vào PATH môi trường thủ công nếu máy không tự tạo
- vd: Window
- download bản mới nhất 64-bit .exe
https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/12.2.1/windows_10_cmake_Release_graphviz-install-12.2.1-win64.exe
- Được lưu tại C:\Program Files\Graphviz\ hoặc C:\Program Files (x86)\Graphviz\
- Thêm Graphviz vào PATH nếu cần: 
- Windows + S -> Environment Variables: Edit the system environment variables
- Tìm: Environment Variables... -> Path -> Edit
- New và dán thư mục bin: C:\Program Files\Graphviz\bin -> OK
- Kiểm tra: dot -V trong Command Prompt (dưới quyền Administrator nếu không được)


 **Lưu ý trên 3 tập, có thể đặt tham số random_state = 42 thay vì None để tránh thay đổi kết quả**

### Tập 1: 
Diễn giải Classification Report
- Precision:
	Tỷ lệ mẫu được dự đoán là một lớp cụ thể (ví dụ, ác tính) mà thực sự thuộc về lớp đó.
	Precision cao cho thấy mô hình ít dự đoán sai dương tính.
- Recall: 
	Tỷ lệ mẫu thực sự thuộc về một lớp cụ thể (ví dụ, ác tính) mà mô hình dự đoán đúng.
	Recall cao đảm bảo ít bị bỏ sót các trường hợp quan trọng.
- F1-Score: Trung bình điều hòa của Precision và Recall. F1-score cân bằng giữa việc tránh bỏ sót và dự đoán sai.
- Support: Số lượng mẫu thuộc từng lớp trong dữ liệu kiểm tra.

Diễn giải Confusion Matrix
- Ma trận nhầm lẫn hiển thị số lượng mẫu được phân loại đúng và sai giữa các lớp. Ví dụ:

|                   | Predicted Benign | Predicted Malignant |
|-------------------|------------------|---------------------|
| **Actual Benign** | True Negatives (TN) | False Positives (FP) |
| **Actual Malignant** | False Negatives (FN) | True Positives (TP)  |


- True Positives (TP): Số mẫu ác tính (Malignant) được dự đoán đúng.
- True Negatives (TN): Số mẫu lành tính (Benign) được dự đoán đúng.
- False Positives (FP): Mẫu lành tính bị dự đoán sai thành ác tính.
- False Negatives (FN): Mẫu ác tính bị dự đoán sai thành lành tính.

- Ý nghĩa:
	FP cao: Mô hình dễ báo động giả.
	FN cao: Mô hình dễ bỏ sót các trường hợp quan trọng (đặc biệt nguy hiểm trong chẩn đoán bệnh).

Hiệu suất mô hình: Dựa trên báo cáo và ma trận nhầm lẫn:
- So sánh các tỷ lệ dữ liệu huấn luyện/kiểm tra.
- Accuracy cao với phân phối 80/20 hoặc 90/10 thường chỉ ra rằng việc tăng dữ liệu huấn luyện giúp cải thiện hiệu suất.
- Precision và Recall của lớp ác tính đặc biệt quan trọng, do bỏ sót các trường hợp ác tính (FN cao) có thể gây hậu quả nghiêm trọng.

### Tập 3:
1. Trường hợp Accuracy = 1.000000 là hợp lý
Mô hình đạt độ chính xác hoàn hảo có thể là điều bình thường nếu:

Dữ liệu đơn giản: Các đặc trưng trong dữ liệu hoàn toàn phân tách được các lớp mà không có sự chồng chéo hoặc nhiễu.
Ví dụ: Với dữ liệu về nấm (edible/poisonous), các đặc trưng như odor (mùi) có thể là yếu tố quyết định tuyệt đối, giúp phân loại chính xác mọi mẫu.
Dữ liệu không có nhiễu (noise): Nếu dữ liệu sạch, ít nhiễu và có quan hệ trực tiếp giữa đặc trưng và nhãn, mô hình có thể đạt được độ chính xác cao.
Dữ liệu kiểm tra rất nhỏ: Với tập kiểm tra có kích thước nhỏ, mô hình có thể dễ dàng dự đoán chính xác tất cả các mẫu.

2. Trường hợp Accuracy = 1.000000 là vấn đề
Nếu độ chính xác hoàn hảo xảy ra mà không có lý do hợp lý, bạn nên xem xét các vấn đề sau:

a. Overfitting (Quá khớp)
Nguyên nhân:
Mô hình Decision Tree thường có xu hướng quá khớp nếu không được giới hạn độ sâu (max_depth) hoặc không có các biện pháp kiểm soát độ phức tạp.
Cây quyết định có thể học thuộc lòng toàn bộ dữ liệu huấn luyện, dẫn đến độ chính xác cực cao trên tập huấn luyện hoặc kiểm tra nhỏ, nhưng kém hiệu quả khi áp dụng vào dữ liệu mới.
Cách kiểm tra:
So sánh độ chính xác trên tập huấn luyện với độ chính xác trên tập kiểm tra. Nếu trên tập kiểm tra lớn mà Accuracy vẫn cao, mô hình có thể hoạt động tốt. Nhưng nếu chỉ cao trên tập huấn luyện, đó là dấu hiệu của overfitting.
b. Dữ liệu kiểm tra bị rò rỉ từ dữ liệu huấn luyện
Nguyên nhân:
Có khả năng dữ liệu huấn luyện và kiểm tra bị trùng lặp hoặc có mối liên hệ không mong muốn, dẫn đến việc mô hình học chính xác các mẫu kiểm tra.
Cách kiểm tra:
Đảm bảo dữ liệu được chia ngẫu nhiên với train_test_split và tham số stratify được sử dụng đúng.
Kiểm tra kỹ thuật tiền xử lý, tránh việc mã hóa hoặc xử lý dựa trên toàn bộ tập dữ liệu thay vì chỉ trên tập huấn luyện.
c. Đặc trưng mạnh vượt trội (Dominant Features)
Nguyên nhân:
Một hoặc nhiều đặc trưng trong dữ liệu có ảnh hưởng rất lớn, quyết định gần như hoàn toàn nhãn đầu ra.
Điều này có thể làm cho mô hình đơn giản đạt được độ chính xác hoàn hảo mà không cần đến các đặc trưng khác.
Cách kiểm tra:
Xem xét mức độ quan trọng của đặc trưng (feature_importances_) trong cây quyết định. Nếu một đặc trưng chiếm gần như toàn bộ trọng số, đây là dấu hiệu của đặc trưng mạnh vượt trội.

3. Khi nào cần chấp nhận Accuracy = 1.000000?
Nếu bạn đã kiểm tra và xác nhận:
Mô hình không bị overfitting.
Dữ liệu kiểm tra không rò rỉ từ dữ liệu huấn luyện.
Đặc trưng mạnh vượt trội là hợp lý với bài toán.
Cross-validation cũng cho kết quả tương tự.
=> Khi đó, độ chính xác hoàn hảo có thể chấp nhận được.

4. bộ dữ liệu này hoàn toàn đáp ứng các yêu cầu của bài toán học có giám sát:

Bao gồm cả tính năng và nhãn:

Bộ dữ liệu có 22 đặc trưng (features) như cap-shape, cap-color, odor, v.v., và một nhãn (label) là class, đại diện cho hai loại:
e: Edible (ăn được).
p: Poisonous (không ăn được).
Đây là bài toán học có giám sát, vì dữ liệu có nhãn đầy đủ.
Bao gồm ít nhất 300 mẫu:

Bộ dữ liệu Mushroom có tổng cộng 8,124 mẫu (mỗi hàng là một mẫu nấm), vượt xa yêu cầu tối thiểu 300 mẫu để phân tích có ý nghĩa.
Bao gồm nhiều lớp hoặc ít nhất hai lớp nhị phân:

Dữ liệu này là bài toán phân loại nhị phân với hai lớp (e và p).