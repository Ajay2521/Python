# In this lets see about read and write in Excel file.

# Excel file is a spreadsheet document which is used to store data like a database structure.With an extension .xlsx.

# Usually the first row of the excel file is mainly reserved for the heading / topic of that specific column.

# Excel dfile contains multiple sheets called as worksheets.

# By default the worksheet will be denoted using index value.

# xlrd = Is a python module used to read from excel file.

# To download xlrd = Open command prompt and type "pip install xlrd" command.

# Here is the program to read from excel file.

import xlrd

# opening the excel file.

File = xlrd.open_workbook('Excel Test.xlsx')

Sheet = File.sheet_by_index(0) # mentioning the index of the sheet as 0 , which is first sheet.

print(Sheet.cell_value(0,0))