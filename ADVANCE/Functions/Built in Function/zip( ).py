# In this lets see about the "Built-in functions" in python.

# Built-in function is defined as the functions whose functionality is pre-defined in the python compiler.

# Lets see about "zip( ) bilt-in function" in python.

# zip( ) - Used to returns a zip object, which maps a similar index of multiple containers. 

# Here is the program for zip( ).

NumList = [ 1, 2, 3, 4, 5 ]

StrList = [ "One", "Two", "Three", "Four", "Five" ]

Zip = zip( NumList, StrList )

print( )

print ( Zip )

ZipRead = list( Zip ) # converting the zip to list for readability.

print ( ZipRead )
