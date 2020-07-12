# In this lets see about the "Built-in functions" in python.

# Built-in function is defined as the functions whose functionality is pre-defined in the python compiler.

# Lets see about "map( ) bilt-in function" in python.

# map( ) - Used to return a list of results after applying a given function to each item of an iterable(list, tuple etc.).

# Here is the program for map( )

def MapFun( a ):
  
    return a

b = map( MapFun, ('Maayon', 'Techy', 'Techgen') )

# prints the Map

print ( ) # prints new line for readability.

print( b )

#convert the map into a list, for readability:

print ( ) # prints new line for readability.

print( list ( b ) )