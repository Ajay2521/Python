# In this lets see about the "Built-in functions" in python.

# Built-in function is defined as the functions whose functionality is pre-defined in the python compiler.

# Lets see about "delattr( ) bilt-in function" in python.

# delattr( ) - Used to delete an attribute from a class.

# It takes two parameters, first is an object of the class and second is an attribute which we want to delete. 

# After deleting the attribute, it no longer available in the class and throws an error if try to call it using the class object.

# Here is the program for delattr( ).

# Creating a class to store data.

class Details :

    Name = "Maayon"

    Age = 19

d = Details( ) 

print( "\nBefore using delattr( )")

print( "\nName is : " , d.Name )

print( "\nAge is : " , d.Age )

# Deleting age using delattr( )

delattr( Details, "Age" )

print( "\nAfter using delattr( )")

print( "\nName is : " , d.Name )

print( )

print( "\nAge is : " , d.Age ) # It will result in error since it has been deleted by using delattr( )
