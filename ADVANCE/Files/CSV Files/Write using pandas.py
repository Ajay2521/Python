# In this lets see about csv files in python.

# CSV = Comma Separated values.

# csv can also handles using pandas module.

# to_csv = In pandas is used to write data into the csv file.

# Here is the program to write csv data using pandas in python.

import pandas as pd

data = pd.DataFrame([[4,'Aj',19],[5,'Aju',19]],columns=['SI','Name','Age'])

data.to_csv('CSV Test.csv')

print('\nData has been successfully written into the CSV file\n.')