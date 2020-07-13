# In this lets see about "File Handling in python."

# python "os module" is used to interact with the operating system.

# This "os module" is used to renaming , removing , deteling etc in file handling.

# Syntax to import os :

# import os

# This is allow the user to use the functionally of "os module".

# rename( ) = Used to rename a file present in the system.

# Syntax to rename( )

# os.rename( CurrentName , NewName )

# CurrentName = current name of the file which is to be renamed.

# NewName = New Name is modified name of the file.
 
# Here is the Program for "rename ( ) the file"

import os

# rename the file1.txt to FileRenamed.txt

os.rename( "file1.txt" , "FileRenamed.txt")

print( "\nSuccessfully renamed the file from \"file1.txt\" to \"FileRenamed.txt\" ..." )

