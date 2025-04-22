import  openpyxl  as  op  #openpyxl 모듈 import
path = r"C:\workspace\oa_excel\output"
wb = op.load_workbook(path + "/test_ullim.xlsx")

ws = wb["여성"] # wb["울림"]
cell = ws['B3']

print(f"값: {cell.value}")
print(f"데이터 타입: {cell.data_type}")
print(f"행 번호: {cell.row}")
print(f"열 번호: {cell.column}")
print(f"열 문자: {cell.column_letter}")
print(f"좌표: {cell.coordinate}")
print(f"날짜 여부: {cell.is_date}")