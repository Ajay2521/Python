# In this lets see about "call by reference functions" in Python.

# Call by Reference is defined as the passing the actual value as an argument in the function.

# By default all the functions are called by reference in python.

# In simple all the changes made to the reference inside the function revert back to the original value referred by the reference.

# Here is the program for "Call by Reference by passing the immutable datatype str"

# defining the value of the string

str = "Hello all"

print ( "\nThe value of the string before calling the function is : " , str )

# defining the function to add the values to the str at last place.

def add_str( str ) :

	str = str + " This is Maayon..."

	print ( "\nThe value of the string inside the function is : " , str )

# calling the function 

add_str( str )

print ( "\nThe value of the string outside the function is : " , str )


