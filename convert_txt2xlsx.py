import pandas as pd
# đọc dữ liệu từ tệp văn bản
with open('/home/robotics/ngant/sql/a.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
data = {}
current_key = None
current_value = []
# Xử lý từng dòng trong tệp
for line in lines:
    if line.strip():  # Bỏ qua các dòng trống
        if line[0].isdigit() and '.' in line:
            # Nếu gặp một chỉ mục mới, lưu dữ liệu của chỉ mục trước vào dictionary
            if current_key is not None:
                data[current_key] = ' '.join(current_value)
            # Cập nhật chỉ mục hiện tại
            current_key = line.strip()
            current_value = []
        else:
            # Thêm nội dung vào giá trị hiện tại
            current_value.append(line.strip())

# Đảm bảo lưu dữ liệu cho chỉ mục cuối cùng
if current_key is not None:
    data[current_key] = ' '.join(current_value)

# Tạo DataFrame từ dictionary
df = pd.DataFrame(list(data.items()), columns=['Key', 'Value'])

# Lưu DataFrame vào tệp Excel
df.to_excel('du_lieu_ghi.xlsx', index=False)