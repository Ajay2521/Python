# In this lets see about the "Built-in functions" in python.

# Built-in function is defined as the functions whose functionality is pre-defined in the python compiler.

# Lets see about "issubclass( ) bilt-in function" in python.

# issubclass( ) - Used to returns true if object argument(first argument) is a subclass of second class(second argument).

# Here is the program for issubclass( ).

class MyAge:

    Age = 19

class MyData( MyAge ):

    Name = "Maayon"

    Age = MyAge

print("\nIs MyData is a SubClass of MyAge ?: " , issubclass( MyData, MyAge ) )

print("\nIs MyAge is a SubClass of MyData ?: " , issubclass(  MyAge, MyData ) )

