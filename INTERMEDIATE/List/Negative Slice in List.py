# In this lets see about "Negative Slice in the List Datatype" in Python.

# Negative slicing is possible in the List.

# It starts from the rightmost character, which is indicated as -1 and so on.

List = [ 1, 2, 3, 4, 5, 6 ]

print() # Print an empty line for readablity.

print( List [ -1 ] ) # Print the rightmost characters.

print() # Print an empty line for readablity.

print( List [ -2 ] ) # Print the second rightmost characters.

print() # Print an empty line for readablity.

print( List [ -3 : ] ) # Print the characters from [ -3 ] index.

print() # Print an empty line for readablity.

print( List [ -6 : ] ) # Print the characters from [ -6 ] index.

print() # Print an empty line for readablity.

print( List [ -5 : -1 ] ) # Print the characters from [ -5 ] index to [ -1 ] index.

print() # Print an empty line for readablity.\

print( "The Reverse of the \"" , List , "\" is : " , List [ : : -1  ] ) # Print all the characters in "Reverse order".
