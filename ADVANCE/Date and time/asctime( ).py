# lets see about "date and time" in python.

# localtime( ) = Used to return the current time in the form of tuple.

# asctime( ) = used to return the time and date in simple format.

# Here is the program for printing current time intuple form using "localtime( ) and asctime( )"
 
import time

print( "\nCurrent time is : \n\n" , time.asctime( time.localtime( ) ) )

# First it gets the current time in tuple format.

# Then it turn the tuple format into simple format.


