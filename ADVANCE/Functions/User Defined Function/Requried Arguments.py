# In this lets see about "type of arguments passed in functions" in Python.

# Types of arguments are :

# 1) Required Arguments.

# 2) Keyword Arguments.

# 3) Default Arguments.

# 4) Variable_length Arguments.

# Lets see about "Required Arguments"

# These are the arguments which are required to be passed at the time of function calling with the exact match of their positions in the function call and function definition.

# Here is the program for "Required Arguments"

# defining the function to add the values to the list at last place.

def add( a , b ) :

	c = a + b

	print( "\nThe Addition of values " , a , " and " , b , " is : " , c )

# calling the function add( a , b ) by passing the arguments.

a = 10

b = 20

add( a , b  ) 


