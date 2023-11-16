import pandas as pd

# Đường dẫn tới tệp Excel đầu vào và đầu ra
input_excel_path = '/home/robotics/ngant/sql/du_lieu_ghi.xlsx'
output_excel_path = '/home/robotics/ngant/sql/output.xlsx'

# Đọc dữ liệu từ tệp Excel
df = pd.read_excel(input_excel_path)

# Xóa các chỉ mục từ cột 'Chỉ mục'
df['Key'] = df['Key'].str.replace(r'^\d+(\.\d+)*\s*\.', '', regex=True)

# Lưu DataFrame đã được chỉnh sửa vào tệp Excel mới
df.to_excel(output_excel_path, index=False)

# In thông báo hoàn tất
print("Đã xóa các chỉ mục và lưu vào tệp:", output_excel_path)