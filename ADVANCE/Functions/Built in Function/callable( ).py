# In this lets see about the "Built-in functions" in python.

# Built-in function is defined as the functions whose functionality is pre-defined in the python compiler.

# Lets see about "callable( ) bilt-in function" in python.

# callable( ) - Used to returns True if the object passed appears to be callable, otherwise False.

# Here is the program for callable( )

def call( ):

	return 10

# "a" is a used to call a function call( ) , which is a callable varaible.

a = call

print ( ) # Prints new line for readability.

print( callable ( a ) )

# "a" is an variable only used to store a value.

a = 10

print ( ) # Prints new line for readability.

print ( callable ( a ) ) 
