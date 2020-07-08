# In this lets see about "Scope of Variables" in python.

# The scopes of the variables depend upon the location where the variable is being declared. 

# The variable declared in one part of the program may not be accessible to the other parts.

# There are two type of scope , they are

# 1) Global Variable.

# 2) Local Variable. 

# Here lets see about the "Global Variable" in python.

# The variable defined outside any function is known to have a global scope.

# This global variables will have the value contant even after the function is called.

a = 10 # Variable "a" is defined as a global variable.

print ( "\nThe value of \"a\" before calling the function is : " , a )

def increment_a ( a ) : 

	a = a + 1

	print ( "\nThe value of \"a\" after increment and during function call is : " , a )

increment_a ( a ) # calling the function 

print ( "\nThe value of \"a\" after calling the function is : " , a )
