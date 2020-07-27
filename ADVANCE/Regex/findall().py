# Lets see about "findall()" using re module.

# findall() = Used to return a list which contains list of all matches of a pattern within the string.

# By default it returns the pattern in the order they are found.

# NOTE : If no match is found it return an empty list.

# Here is the program for "findall()".

# importing re module which is used for regex.

import re

str = "Hello all! This is Maayon from Maayon tech."

# accessing findall() which is present in the re module.

match1 = re.findall("Maayon",str) # result in the list which contains two matches for Maayon. 

match2 = re.findall("AJ",str) # result in empty list , since no match for AJ.

print() # prints an empty line for readability.

print(match1)

print() # prints an empty line for readability.

print(match2)

print() # prints an empty line for readability.

