### Chuẩn bị
- cần tải các thư viện: pip install matplotlib,... như trong src
- tải graphviz (lên gg), và phải thêm Graphviz vào PATH môi trường thủ công nếu máy không tự tạo
 vd: Window
 • download bản mới nhất 64-bit .exe
https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/12.2.1/windows_10_cmake_Release_graphviz-install-12.2.1-win64.exe
 • Được lưu tại C:\Program Files\Graphviz\ hoặc C:\Program Files (x86)\Graphviz\
 • Thêm Graphviz vào PATH nếu cần: 
 • Windows + S -> Environment Variables: Edit the system environment variables
 • Tìm: Environment Variables... -> Path -> Edit
 • New và dán thư mục bin: C:\Program Files\Graphviz\bin -> OK
 • Kiểm tra: dot -V trong Command Prompt (dưới quyền Administrator nếu không được)

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

				Predicted Benign	Predicted Malignant
	Actual Benign		True Negatives (TN)	False Positives (FP)
	Actual Malignant	False Negatives (FN)	True Positives (TP)

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

