# In this lets see about read and write in Excel file.

# Excel file is a spreadsheet document which is used to store data like a database structure.With an extension .xlsx.

# Usually the first row of the excel file is mainly reserved for the heading / topic of that specific column.

# Excel dfile contains multiple sheets called as worksheets.

# Here is the program to read from excel file using pandas.

import pandas as pd

# opening the excel file.

data = pd.read_excel('Excel Test.xlsx')

print() # prints empty line for readability.

print(data)

print() # prints empty line for readability.

