# In this lets see about "functions" in Python.

# Function is defined as the block of code which can be used to reduce the code size and call it whenever need in the program.

# The function contains the set of programming statements enclosed by { }.

# There are mainly two types of functions.They are

# 1) User define functions - It is created and defined by the user to perform specific task for user choise.

# 2) Built-in functions - It the function that are pre-defined in python by python developers.

# Advantage of Functions : 

# 1) It reduce the code size.

# 2) It avoid rewriting code for same logic again and again.

# 3) It can be used and called in the proram for many number of time as possible.

# 4) It makes easy to track the large program easily when it is writen by using the functions.

# 5) Function calling is always overhead in a Python program.

# Creating A Fucntion :

# def is a keyword used to create a user defined function in python Programming.

# syntax for user - defined function is :

# def function_name ( parameters passed ) :

# 	function_block /  function_statement

# return expression / variable

# def -  Is a keyword used to define a user created function.

# function_name - Name of the function, which can be used while calling the function.

# parameters passed - function can be created with or without  argument ( Parameters ) pass.

# function_block / function_statement - Where logic or code or statement of that particular function takes place.

# return expression / variable - return the function value.

# Note : Once a function is created then it can be called anytime and anywhere in the program . But function must be defined before the function call.

# Here is the example for "user-defined function" in python.

# defining the function to add two values of "a" and "b" and store the result in "c".

def add( ) :

	a = 10

	b = 20

	c = a + b

	return c 

# calling the function add( )

print( "\nThe Addition of two values is : " , add( ) )

