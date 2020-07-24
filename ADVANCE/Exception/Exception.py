# In this lets see about "Exception" in python.

# Exception is considered as an run time error which causes an unusual condition in a program resulting in the interruption in the flow of the program.

# When an exception occured in a program then the python complie stop the program from further execution of code.

# Thus by providing an exception handling , the code can be executed without any interruption.

# There are many built in exceptions in python.

# Commonly occured exceptions is:

# 1) ZeroDivisionError = occures when a number is divided by zero.

# 2) NameError = occures when a name is not found in both local or global scope.

# 3) IndentationError = occures when an incorrect indentation is given in the code.

# 4) IOError = occures when Input Ouput operations fails.

# 5) EOFError = occures when the end of the file is reached but still operation are performed.

# Here is the program to explain ZeroDivisionError Exception.
 
a = 10

b = 0

print( ) # prints new line for readability.

print( a / b ) # throws error "ZeroDivisionError". and python stop executing further code.

# code after exception.

print("\nException not occured.") # python compllie stoped at the place of exception thus this part of code will not be executing.


