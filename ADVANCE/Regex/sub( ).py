# let see about "sub( )" in re module.

# sub( ) = used to replace the matches with the text of user choice.

# Here is the example for split( )

# importing re 

import re

str = "Hello all! This is Maayon here"

replaceStr = re.sub("Maayon" , "AJ" ,str)

print("\nThe Original string is : \n\n " , str) 

print("\nThe Replaced string using sub( ) is : \n\n " , replaceStr)

print() # prints empty line for readability.

