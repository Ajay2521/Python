# In this lets see more about "Dictionary datatype" in python.

# Dictionary is used to store the data in a key-value pair format.

# In short it giveout the value for specific key.

# The values can be accessed in the dictionary by using the keys as keys are unique in the dictionary.

# The value can be updated along with key Dict[key] = value.

# The update() method is also used to update an existing value.

# Note: If the key-value already present in the dictionary, the value gets updated. Otherwise, the new keys added in the dictionary.

# Here is the program for "Adding and updating the Dictionary values."

Details = { "Name" : "Maayon" , "Age" : 19 }

print ( "\nThe Details is...\n\n" , Details )

# Adding a key and value to the already existing dictionary.

Details[ "NickName" ] = "Techgen"

print ( "\nThe Details after Adding a value to the Dictionary is...\n\n" , Details )

# Updating a key and value to the already existing dictionary key - value.

Details[ "NickName" ] = "Techguru"

print ( "\nThe Details after Updating value to the Dictionary which is already existed is...\n\n" , Details )

