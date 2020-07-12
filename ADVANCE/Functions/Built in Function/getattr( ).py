# In this lets see about the "Built-in functions" in python.

# Built-in function is defined as the functions whose functionality is pre-defined in the python compiler.

# Lets see about "getattr( ) bilt-in function" in python.

# getattr( ) - Used to returns the value of a named attribute of an object. 

# If it is not found, it returns the default value.

# Here is the program for getattr( )

class data:  
 
    Name = "Maayon"  
  
    Age = 19  
 
Details = data( )

print ( "\nThe Name is : " , getattr( Details, "Name") )

print ( "\nThe Age is : " , getattr( Details, "Age") )
