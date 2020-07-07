# In this lets see more about "Dictionary datatype" in python.

# Dictionary is used to store the data in a key-value pair format.

# In short it giveout the value for specific key.

# del keyword is used to delete the dictionary.

# Here is the program for "Adding and updating the Dictionary values."

Details = { "Name" : "Maayon" , "Age" : 19 , "NickName" : "Techgen" }

print ( "\nThe Details is...\n\n" , Details )

# deleting specified key and its value.

del Details[ "NickName"]

print ( "\nThe Details after deleting a specific key and value is...\n\n" , Details )

# deleting dicitonary completely.

print ( )

del Details

print ( "\nThe Details after deleting a dictionary completely is...\n\n" , Details )

