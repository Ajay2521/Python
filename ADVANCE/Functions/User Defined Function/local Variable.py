# In this lets see about "Scope of Variables" in python.

# The scopes of the variables depend upon the location where the variable is being declared. 

# The variable declared in one part of the program may not be accessible to the other parts.

# There are two type of scope , they are

# 1) Global Variable.

# 2) Local Variable. 

# Here lets see about the "Local Variable" in python.

# The variable defined inside any function is known to have a global scope.

# Once the local variable comes out of the function or scope it doesn't have any more place in the program.


def increment_a (  ) : 

	a = 10 # Variable "a" is defined as a local variable.

	a = a + 1

	print ( "\nThe value of \"a\" after increment and during function call is : " , a )

increment_a ( ) # calling the function 

print ( )

print ( "\nThe value of \"a\" after calling the function is : " , a ) # this will cause an error since "a" is declared as an local variable of the function , and which can be accessed outside the function.
