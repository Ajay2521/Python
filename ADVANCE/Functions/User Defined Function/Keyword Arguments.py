# In this lets see about "type of arguments passed in functions" in Python.

# Types of arguments are :

# 1) Required Arguments.

# 2) Keyword Arguments.

# 3) Default Arguments.

# 4) Variable_length Arguments.

# Lets see about "Keyword Arguments ( ** Kwargs ) "

# Python allows us to call the function with the keyword arguments.

# This allows us to pass the arguments in tha random order.

# The name of the arguments is treated as the keywords and matched in the function calling and definition.

# If the same match is found, the values of the arguments are copied in the function definition.

# defining the function to add the values to the list at last place.

def add( a , b ) :

	c = a + b

	print( "\nThe Addition of values " , a , " and " , b , " is : " , c )

# calling the function add( a , b ) by passing the arguments.

add( b = 20 , a = 10 ) # passing the arguments in the random manner


