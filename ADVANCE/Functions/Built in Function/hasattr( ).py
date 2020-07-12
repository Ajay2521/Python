# In this lets see about the "Built-in functions" in python.

# Built-in function is defined as the functions whose functionality is pre-defined in the python compiler.

# Lets see about "hasattr( ) bilt-in function" in python.

# hasattr( ) - Used to returns the true is the value is present else it return false.

# Here is the program for hasattr( )

class data:  
 
    Name = "Maayon"  
  
    Age = 19  
 
Details = data( )

print ( "\nDid the Name exit in the data ? : " , hasattr( Details, "Name") )

print ( "\nDid the Age exit in the data ? : " , hasattr( Details, "Age") )

print ( "\nDid the Class exit in the data ? : " , hasattr( Details, "class") )
