# let see about "split( )" in re module.

# split( ) = used to return a list where the string has been split at each match.

# Here is the example for split( )

# importing re 

import re

str = "Hello all! This is Maayon here"

print() # prints empty line for readability.

print(re.split("\s",str)) # splits the str when ever a whitespace has occured. \s denotes whitespace.

print() # prints empty line for readability.
