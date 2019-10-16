import opentranctionsxl as xl
xl.loadworkbook('tranctions.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1']
cell = sheet.cell(1, 1)
print(cell.value)
