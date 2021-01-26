import openpyxl

wb = openpyxl.Workbook()
sheet = wb['Sheet']
print(sheet['A1'].value)
sheet['A1'] = 'Felipe Schmaedecke'
sheet['A2'] = 29
print(sheet['A1'].value)
sheet.title = 'Usuários'
wb.save('example.xlsx')
