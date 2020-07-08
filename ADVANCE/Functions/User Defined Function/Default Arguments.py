# In this lets see about "type of arguments passed in functions" in Python.

# Types of arguments are :

# 1) Required Arguments.

# 2) Keyword Arguments.

# 3) Default Arguments.

# 4) Variable_length Arguments.

# Lets see about "Default Arguments"

# Default argument is  initialize the arguments at the function definition.

# If the value of any of the arguments is not provided at the time of function call, then that argument can be initialized with the value given in the definition even if the argument is not specified at the function call.

# Here is the program for "Default Arguments"

# defining the function to add the values to the list at last place.

# Here b is defined as the default argument , if value of "b" is not passed while calling the function then the default value takes place.

def add( a , b = 10 ) :

	c = a + b

	print( "\nThe Addition of values " , a , " and " , b , " is : " , c )

# calling the function add( a , b ) by passing the arguments.

a = 10

b = 20

add( a , b ) # calling the function by passing both the variables "a" and "b".

add( a ) # calling the function by passing only the variables "a" and "b" takes the value of defalut argument.


