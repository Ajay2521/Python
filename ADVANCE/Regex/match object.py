# Lets see about "match object" in python.

# match object used to contains the information about the search and the output of it.
 
# NOTE : If no match is found then it returns None object.

# Here is the example for match object 

# importing re module which is used for regex.

import re

str = "Hello all! This is Maayon from Maayon tech."

# accessing search() which is present in the re module.

match1 = re.search("Maayon",str) # result in the object which contains two matches for Maayon. 

match2 = re.search("AJ",str) # result in None object , since no match for AJ.

print() # prints an empty line for readability.

print(match1)

print() # prints an empty line for readability.

print(type( match1) )

print() # prints an empty line for readability.

print(match2)

print() # prints an empty line for readability.

print(type( match2) )

print() # prints an empty line for readability.
