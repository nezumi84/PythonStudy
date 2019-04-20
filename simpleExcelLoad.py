import pandas as pd
import os
import xlrd

inputExcelFile = './test2.xlsx'
if os.path.isfile(inputExcelFile):
    xl = pd.ExcelFile(inputExcelFile)
else:
    print("[ERROR] Failed to load Excel File : %s" % (inputExcelFile))

# Load a sheet into a DataFrame by name: df
df = xl.parse(''.join(xl.sheet_names))

print(df)
