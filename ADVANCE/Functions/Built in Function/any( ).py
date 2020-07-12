# In this lets see about the "Built-in functions" in python.

# Built-in function is defined as the functions whose functionality is pre-defined in the python compiler.

# Lets see about "any( ) bilt-in function" in python.

# any( ) - Used to accepts an iterable object such as list, tuple, set, dictionary, etc.

# It returns true if atleast any one items in passed iterable are true , else it returns False.

# Note : zero ( 0 ) is considered as a false value and other than zero any intergers are considered as an true value.

# Note : If the iterable object is empty, the any() function returns false.

# Here is the program for any( )

print ( ) # It prints new line for readability.

a = [ 1, 2, 3, 4, 5 ] # Here any values in List is true , hence it returns true.

print ( any ( a ) )

print ( ) # It prints new line for readability.

a = [ 0, 0, 0, 0, 0 ] # Here any values in List is false , hence it returns false.

print ( any ( a ) )

print ( ) # It prints new line for readability.

a = [ 0, 1, 2, 3, 4, 5 ] # Here only one values in List is false , hence it returns true.

print ( any ( a ) )

print ( ) # It prints new line for readability.

a = [ ] # It is an empty list , thus it return false.

print ( any ( a ) )

print ( ) # It prints new line for readability.
 
# Note : It is same for any datatypes like tuple, set, dictionary etc...  