# In this lets see about "File Handling in python."

# python "os module" is used to interact with the operating system.

# This "os module" is used to renaming , removing , deteling etc in file handling.

# remove( ) =  Used to remove the file from the system.

# Syntax for remove( ):

# remove( "FileName" )

# Here is the program for "remove( )".

import os

# removing the file named FileRemove.txt

os.remove( "FileRemove.txt" )

print ( "\nFile has been removed successfully..." )

# Note : Make sure that FileRemove.txt is present.

# since I have complied this code , there will be no file named FileRemove.txt in my repository.