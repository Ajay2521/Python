# lets see about "Modules" in python.

# Module is python is defined as a python programming file which inculdes python variables, classes etc.

# Modules are used to organize the python code in a logical way.

# To use one Module into other , then the specific module must be imported.

# NOTE : While importing module , by default python create a local directory for that specific module.
 
# There are two different ways to import module into the current program, they are.

# 1) import statement.

# 2) from - import statement.

# lets see about " from - import statement".

# It is used to import only the specific functionality from the importing module.
 
# It is possible to import multiple module in a single line.

# Syntax for form - import is:

# from moduleName import functionalityName

#  OR

# from moduleName import functionalityName1,functionalityName2,... functionalityName n. 
   
# Here is the program which is used to import only the specific functionality from module "Calculate.py" using from - import statement.

# importing Muti() from "Calculate.py" using from - import statement.
    
from Calculate import Multi

# Getting user input for variables a and b.

a = int( input ( "\nEnter a value for \"a\" : " ) )

b = int( input ( "\nEnter a value for \"b\" : " ) )

# Accessing the functionality present in the module "Calculate" using dot( . ) operator.

# Note : There is no need of dot( . ) operator when the module is imported using from - import methof.
 
Multi( a,b )

print( ) # Used to print new line for readability.