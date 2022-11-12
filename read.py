from tableauscraper import TableauScraper as TS
url = "https://tableau.wisconsin.edu/views/UW-MadisonDeansList/ListDashboard"

ts = TS()
ts.loads(url)
workbook = ts.getWorkbook()

for t in workbook.worksheets:
    print(f"worksheet name : {t.name}") #show worksheet name
    print(t.data) #show dataframe for this worksheet

