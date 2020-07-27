# Lets see about "match object" in python.

# group() = used to return the part of the string where the match is found.

# Here is the example for match object "group()"

# importing re module which is used for regex.

import re

str = "Hello all! This is Maayon from Maayon tech."

# accessing search() which is present in the re module.

match1 = re.search("Maayon",str) # result in the object which contains two matches for Maayon. 

print() # prints an empty line for readability.

print(match1.group())

print() # prints an empty line for readability.

