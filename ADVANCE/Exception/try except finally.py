# Lets see about "Exception handling" in python.

# While handling exception in python , it is possible to use finally block in it.

# finally = used to execute the code no matter , whether the exception occurs or not in try block.

# Thus finally block will be excuted by default.
    
# synatx for finally is:

# try:

#    try block code statement.

# except:

#   except block code statement.

# finally:

#    finally block code statement.
    
# Here is the program for "try except finally" in python.

# may or may not throw the exception.

try:

    a = int( input("\nEnter a value for \"a\" : ") )

    b = int( input("\nEnter a value for \"b\" : ") )

    print( "\nDivision is : " , a / b ) # Exception occurs

# executed only when try block throw an exception.

except:

    print("\nSince Exception has occured in try block , except block has been executed.")

# excuted always by default .
 
finally:

    print("\nFinally block is executed by default whether exception occur or not.")

    