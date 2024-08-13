import os
from openpyxl import Workbook

def create_excel_file(file_path, header_row):
    if not os.path.exists(file_path):
        wb = Workbook()
        ws = wb.active
        ws.append(header_row)  # Add header row
        wb.save(file_path)
        print(f"Created {file_path}")
    else:
        print(f"{file_path} already exists")

# Usage example
file_path = r'C:\Users\pcash\Desktop\FFMpeg\Last_loop.xlsx'
header_row = ["LAST_LOOP", "DATE_TIME"]  # Define header row
create_excel_file(file_path, header_row)