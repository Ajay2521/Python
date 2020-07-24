# Lets see about "Exception handling" in python.

# raise = Used to raise an exception forcefully in python.

# synatx for raise is :

# raise Exception_class,value

# Here is the program for "raise" in python.

try:

    age = int( input("\nEnter age : ") )

    if(age <  18):

        # calling raise

        raise ValueError

    else:

        print("\nAge is valid for the process...")

# defining  a raise

except ValueError:

    print("\nAge is not valid for the process...")
