import xlrd
wb = xlrd.open_workbook("dedam5.xlsx")
sheet = wb.sheet_by_index(0)
# For row 0 and column 0
print(sheet.cell_value(0, 5))
