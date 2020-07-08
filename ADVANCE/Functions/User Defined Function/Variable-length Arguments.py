# In this lets see about "type of arguments passed in functions" in Python.

# Types of arguments are :

# 1) Required Arguments.

# 2) Keyword Arguments.

# 3) Default Arguments.

# 4) Variable_length Arguments.

# Lets see about "Variable-length Arguments"

# When the number of argument to passed is unknow then variable-length argument ( *arguments ) can be used  

# Here is the program for "Variable-length Arguments"

# defining the function to print "n number" of values.

def PrintName(*Names) :

    for name in Names :    
        
        print ( "\n" , name )

# Calling the function by passing "n number" of values.
    
PrintName( "Maayon" , "Maaya" , "Vijay" , "Ajith" )



