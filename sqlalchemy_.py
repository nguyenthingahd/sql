# import pandas as pd
# import mysql.connector
# from sqlalchemy import create_engine

# # Load Excel file into a Pandas ExcelFile object
# excel_file_path = '/home/robotics/ngant/sql/du_lieu_ghi.xlsx'
# xls = pd.ExcelFile(excel_file_path)

# # MySQL database connection
# db_config = {
#     'host': '127.0.0.1',
#     'user': 'abstract-programmer',
#     'password': 'example-password',
#     'database': 'example_DB',
#     'raise_on_warnings': True
# }

# # Create MySQL connection and SQLAlchemy engine
# conn = mysql.connector.connect(**db_config)
# engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

# # Iterate through each sheet and write to MySQL
# for sheet_name in xls.sheet_names:
#     df = pd.read_excel(xls, sheet_name)
#     table_name = sheet_name.lower().replace(' ', '_')  # Create a table name from the sheet name

#     # Write DataFrame to MySQL database
#     df.to_sql(table_name, con=engine, index=False, if_exists='replace')

# # Close the connections
# conn.close()
