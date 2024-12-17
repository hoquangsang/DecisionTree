# Giá trị ngẫu nhiên
RANDOM_STATE = 42  

# Tỷ lệ chia tập dữ liệu
SPLIT_RATIOS = {
    '40/60': 0.4,
    '60/40': 0.6,
    '80/20': 0.8,
    '90/10': 0.9
}
# Giá trị mặc định để kiểm tra độ sâu và độ chính xác
DEFAULT_SPLIT = '80/20'

# Đường dẫn file dữ liệu gốc
RAW_DATA_PATH = "Data/Raw/agaricus-lepiota.data"

# Thư mục lưu các file CSV đã xử lý (chia nhỏ tập dữ liệu)
PROCESSED_CSV_DIR = "Data/Processed Parts"

# Thư mục lưu kết quả cây quyết định ban đầu
RESULTS_BASE_TREE_DIR = "Results/Base Tree"

# Thư mục lưu kết quả thử nghiệm max_depth cho cây quyết định
RESULTS_TREE_MAX_DEPTH_DIR = "Results/Tree Max Depth"

# Thư mục lưu báo cáo và kết quả trực quan hóa khác
REPORTS_DIR = "Results/Reports"

# Giá trị độ sâu tối đa cho thử nghiệm cây quyết định
MAX_DEPTH_VALUES = [None, 2, 3, 4, 5, 6, 7]