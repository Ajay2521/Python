# In this lets see about csv files in python.

# CSV = Comma Separated values.

# Thus CSV is file with a structure of tabular.

# Which is that CSV file represnt the structure of spreadsheet or database in a plain text.

# When a CSV file is opened in excel then the data takes the standard format of rows and columns.

# module csv is used to give the functionality to work with the csv file.

# csv.writer() = used to write a csv file

# writerow() = used to write a data into a csv file in row manner.

# writerows() = Used to write multiple rows at a time in the CSV file.

# Here is the program to write a csv file.

import csv

columns = ['SI','Name','Age']

rows = [ [1,'AJAY',19],
        [2,'MAAYON',19],    
        [3,'SMILY',19] ]

with open('CSV Test.csv','w') as test_file:

    data = csv.writer(test_file)

    data.writerow(columns)

    data.writerows(rows)
    
print('\nData has been successfully written into the CSV file\n.')