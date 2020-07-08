# In this lets see about "functions" in Python.

# syntax for user - defined function is :

# def function_name ( parameters passed ) :

# 	function_block /  function_statement

# return expression / variable

# def -  Is a keyword used to define a user created function.

# function_name - Name of the function, which can be used while calling the function.

# parameters passed - function can be created with or without  argument ( Parameters ) pass.

# function_block / function_statement - Where logic or code or statement of that particular function takes place.

# return expression / variable - return the function value. return is an optional one.

# Note : Once a function is created then it can be called anytime and anywhere in the program . But function must be defined before the function call.

# Here is the example for "user-defined function without return statement" in python.

# defining the function to add two values of "a" and "b" and store the result in "c".

def add( ) :

	a = 10

	b = 20

	c = a + b

	print( "\nThe Addition of two values is : " , c )

# calling the function add( )

add( ) 

