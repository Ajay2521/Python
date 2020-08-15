# Lets see about OS module.

# OS module provides the facility to establish the interaction between the user and the operating system.

# os.chdir( ) = Used to change current working directory of the working file to specific path.

# Here is the example program for os.chdir( )

import os

print('\nCurrent working directory before "chdir" is :',os.getcwd( ))

os.chdir("E:\\")

print('\nCurrent working directory after "chdir" is :',os.getcwd( ))

print( ) # prints empty line for readyability

