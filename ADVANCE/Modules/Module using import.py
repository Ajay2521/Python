# lets see about "Modules" in python.

# Module is python is defined as a python programming file which inculdes python variables, classes etc.

# Modules are used to organize the python code in a logical way.

# To use one Module into other , then the specific module must be imported.
 
# NOTE : While importing module , by default python create a local directory for that specific module.

# There are two different ways to import module into the current program, they are.

# 1) import statement.

# 2) from - import statement.

# lets see about "import statement".

# It is used to import all the functionality of one module into another.

# It is possible to import multiple module in a single line.

# Syntax for import is:

# import modulename

#  OR

# import module1, module2,... module n.
   
# Here is the program which is used to import module "Calculate.py" using import statement.

# importing "Calculate.py" using import statement.
    
import Calculate

# Getting user input for variables a and b.

a = int( input ( "\nEnter a value for \"a\" : " ) )

b = int( input ( "\nEnter a value for \"b\" : " ) )

# Accessing the functionality present in the module "Calculate" using dot( . ) operator.

Calculate.Add( a,b )

Calculate.Sub( a,b )

Calculate.Multi( a,b )

Calculate.Divide( a,b )

print( ) # Used to print new line for readability.