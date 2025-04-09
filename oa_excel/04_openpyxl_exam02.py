import openpyxl as op

wb = op.load_workbook(r"oa_excel\output\exam_pandas1.xlsx")
ws = wb.create_sheet("mysheet")
wb.save(r"oa_excel\output\test_result.xlsx")