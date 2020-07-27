# Lets see about "match object" in python.

# span() = used to return the tuple containing the starting and the end postion of the match.

# NOTE : when span() is passed for none object then it result in error.

# Here is the example for match object "span()"

# importing re module which is used for regex.

import re

str = "Hello all! This is Maayon from Maayon tech."

# accessing search() which is present in the re module.

match1 = re.search("Maayon",str) # result in the object which contains two matches for Maayon. 

match2 = re.search("AJ",str) # result in None object , since no match for AJ.

print() # prints an empty line for readability.

print(match1.span())

print() # prints an empty line for readability.

print(match2.span())

print() # prints an empty line for readability.

