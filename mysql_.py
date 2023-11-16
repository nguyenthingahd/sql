import io 
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

with open('/home/robotics/ngant/sql/a.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
data = {}
current_key = None
current_value = []
for line in lines:
    if line.strip(): 
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

# Save DataFrame to in-memory Excel file 
excel_file_buffer = io.BytesIO()
df.to_excel(excel_file_buffer, index=False)
excel_file_buffer.seek(0)  #đặt vị trí con trỏ về đầu
xls = pd.ExcelFile(excel_file_buffer)

# MySQL database connection
db_config = {
    'host': '127.0.0.1',
    'user': 'abstract-programmer',
    'password': 'example-password',
    'database': 'example_DB',
    'raise_on_warnings': True
}

# Create MySQL connection and SQLAlchemy engine
conn = mysql.connector.connect(**db_config)
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

# Iterate through each sheet and write to MySQL
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name)
    table_name = sheet_name.lower().replace(' ', '_')  # Create a table name from the sheet name

    # Write DataFrame to MySQL database
    df.to_sql(table_name, con=engine, index=False, if_exists='replace')

# Close the connections
conn.close()