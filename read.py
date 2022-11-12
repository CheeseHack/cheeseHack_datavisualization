import camelot
tables = camelot.read_pdf('dashboard.pdf')

print(tables[0].df)
