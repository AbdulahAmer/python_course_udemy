import pandas as pd

file = pd.ExcelFile("/Users/paultorres/Desktop/original.xlsx")

print(file.sheet_names)

sheet = file.parse('sales')

print(sheet)

type(sheet)

print(sheet.Date)

print(sheet.Amount.sum())

sheet.loc[0]

sheet.set_index("Customer", inplace = True)

sheet.loc["MMC Inc."]


sheet["Invoice"]

type(sheet["Invoice"])

