import openpyxl as op
path = r"C:\workspace\oa_excel\output"
wb = op.load_workbook(path + "/test_ullim.xlsx")

sh_list = wb.sheetnames
print(sh_list)

ws = wb["함께"]
wb.save(path + "/test_ullim.xlsx")
#print(ws)