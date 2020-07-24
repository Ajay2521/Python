# Lets see about "Exception handling" in python.

# Exception in python can be handled by using try and except block.

# try = Runs the code which is suspicious.

# except = runs the code if an exception occurs in try block.

# syntax for try - except is :

# try:

#   block of code to be executed.
  
# except Exception 1:

#   block of code to be executed.

# except Exception 2:

#   block of code to be executed.

# .

# .

# .

# except Exception n:

#   block of code to be executed.

# NOTE : Any number of except block can be present in the program followed by the try block.

# Here is the program for "try except" in python.

try:

    a = int( input("\nEnter a value for \"a\" : ") )

    b = int( input("\nEnter a value for \"b\" : ") )

    print( "\nDivision is : " , a / b ) # Exception occurs

except:

    print("\nSince Exception has occured in try block , except block has been executed.")

    