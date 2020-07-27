# Lets see about "match object" in python.

# string = used to return the string passed into the function.

# Here is the example for match object "string"

# importing re module which is used for regex.

import re

str = "Hello all! This is Maayon from Maayon tech."

# accessing search() which is present in the re module.

match1 = re.search("Maayon",str) # result in the object which contains two matches for Maayon. 

print() # prints an empty line for readability.

print(match1.string)

print() # prints an empty line for readability.

