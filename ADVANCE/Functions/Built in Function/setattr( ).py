# In this lets see about the "Built-in functions" in python.

# Built-in function is defined as the functions whose functionality is pre-defined in the python compiler.

# Lets see about "setattr( ) bilt-in function" in python.

# setattr( ) - Used to  set a value to the object's attribute.

# Here is the program for setattr( ).

class Details:

    Name = "Maayon"

    Age = 19

details = Details

setattr( details, 'Mail' , "ajayajutheaj@gmail.com" ) # adding new attribute to the class using setattr( )

print( "\nName is : " , details.Name )

print( "\nAge is : " , details.Age )

print( "\nMail is : " , details.Mail )
