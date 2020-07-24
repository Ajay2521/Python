# Lets see about "Exception handling" in python.

# It is possible to give no exception statement in except block while exception handling in python.

# Thus the user can able to define or give user defined statement in the except block.

# Here is the program for "except without exception" in python.

try:

    a = int( input("\nEnter a value for \"a\" : ") )

    b = int( input("\nEnter a value for \"b\" : ") )

    print( "\nDivision is : " , a / b ) # Exception occurs

except:

    # user defined except statement.

    print( "\nSince Exception has occured in try block , except block has been executed.")

else:

    print( "\nSince no Exception in try block , else block is executed.")

    