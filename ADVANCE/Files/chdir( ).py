# In this lets see about "File Handling in python."

# python "os module" is used to interact with the operating system.

# This "os module" is used to renaming , removing , deteling etc in file handling.

# chdir( ) =  Used to change the current working directory to a specified directory.

# Syntax for chdir( ):

# chdir( "New-Directory-Location")

# Here is the program for "chdir( )".

import os

os.chdir( "C:\\Users\\MAAYON\\Desktop\\Python\\ADVANCE" )

print ( "\nCurrent working directory after changing the directory is : " , os.getcwd( ) )

