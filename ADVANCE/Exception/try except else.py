# Lets see about "Exception handling" in python.

# Exception in python can also be handled by using try , except and else block.

# try = Runs the code which is suspicious.

# except = Runs the code if an exception occurs in try block.

# else = else statement execute the code when no exception occurs in the try block.

# syntax for try - except - else is :

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

# else:

#   block of code executed when no exception occurs.
 
# NOTE : Any number of except block can be present in the program followed by the try block.

# Here is the program for "try except else" in python.

try:

    a = int( input("\nEnter a value for \"a\" : ") )

    b = int( input("\nEnter a value for \"b\" : ") )

    print( "\nDivision is : " , a / b ) # Exception occurs

except:

    print( "\nSince Exception has occured in try block , except block has been executed.")

else:

    print( "\nSince no Exception in try block , else block is executed.")

    
    