# lets see about "Renaming a Modules" in python.

# It is possible to import the module by using specific user defined name called as "alias name".

# It is posssibile to access the functionality of the module by using its "alias name" which was declared while importing the module.

# Syntax for renaming a module is:

# import moduleName as aliasName

# Here is the program which is used to import module "Calculate.py" by using an alias name.
    
import Calculate as Cal

# Getting user input for variables a and b.

a = int( input ( "\nEnter a value for \"a\" : " ) )

b = int( input ( "\nEnter a value for \"b\" : " ) )

# Accessing the functionality present in the module "Calculate" using alias name by using dot( . ) operator.

Cal.Add( a, b) 

Cal.Multi( a,b )

print( ) # Used to print new line for readability.