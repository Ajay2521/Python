# Lets see about "Exception handling" in python.

# It is possible to give exception statement in except block while exception handling in python.

# Thus exception variable is used in except block.

# It is used by using the "as" keyword.
  
# Here is the program for "except with exception" in python.

try:

    a = int( input("\nEnter a value for \"a\" : ") )

    b = int( input("\nEnter a value for \"b\" : ") )

    print( "\nDivision is : " , a / b ) # Exception occurs

except Exception as e: # except with exception , e is an exception variable consider here.
 
    # user defined except statement.

    print( "\nSince Exception has occured in try block , except block has been executed.")

    # print the exception cause statement.

    print("\n",e)

else:

    print( "\nSince no Exception in try block , else block is executed.")

    