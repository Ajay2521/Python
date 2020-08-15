# In this lets see about csv files in python.

# CSV = Comma Separated values.

# Thus CSV is file with a structure of tabular.

# Which is that CSV file represnt the structure of spreadsheet or database in a plain text.

# When a CSV file is opened in excel then the data takes the standard format of rows and columns.

# module csv is used to give the functionality to work with the csv file.

# csv.reader() = Is used to read the data from the csv file.

# Here is the example to read csv file

# importing csv module

import csv

with open('CSV Test.csv') as test_file:

    data = csv.reader(test_file,delimiter=',')

    print() # prints empty line for readability

    print(data) # prints data in map format or unreadable format.            

    print() # prints empty line for readability
    
    for lines in data:

       print(lines) # prints the data line by line or row by row.

print() # prints empty line for readability
    
