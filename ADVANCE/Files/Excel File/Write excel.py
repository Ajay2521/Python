# In this lets see about read and write in Excel file.

# Excel file is a spreadsheet document which is used to store data like a database structure.With an extension .xlsx.

# Usually the first row of the excel file is mainly reserved for the heading / topic of that specific column.

# Excel dfile contains multiple sheets called as worksheets.

# By default the worksheet will be denoted using index value.

# xlsxwriter = Is a python module used to write into a excel file.

# To download xlsxwriter = Open command prompt and type "pip install xlsxwriter" command.

# Here is the program to write an excel file.

import xlsxwriter as xw

# opening / creating a excel file.

File =  xw.Workbook('Excel Test.xlsx')

Sheet = File.add_worksheet()

row = 0

column = 0

Head = 'Name'

Data = ['Ajay','Maayon','Smily','Aj','Aju']

Sheet.write(row,column,Head)

row += 1

for item in Data:

    # writing into the excel file.

    Sheet.write(row,column,item)

    row += 1

# closing the excel file.

File.close()

print('\nData is successfully writen into the Excel file.\n')