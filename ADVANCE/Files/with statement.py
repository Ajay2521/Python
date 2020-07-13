# In this lets see about "File Handling in python."

# The file handling plays an important role when the data needs to be stored permanently into the file.

# Once the data is stored in the file then it can be accessed even after the program termination.

# File Handling is easy in python program when it compared with other programming.

# Files are treated a text or binary in python.

# Note :  Each and every line in the file end with the "special Character."

# The process of file handling is of :

# 1) Open a file / create a file.

# 2) Read / write = Performance operation.

# 3) Close the file.

# with Statement:

# with = Is used to mainpulating the files.

# The advantage of using "with" is it close the file regardless of any nested blocks.

# It automatically close the file when any break or return occurs in the nested block.
   
# Syntax for with is:

# with open( FileName, AccessMode )  as FileObject:

#   Statement(s).

# Here is the program for "with statement in python".

# Opening a file using open( ).

with open( "File.txt" , "r" ) as FileObject:

    print( "\nFile has been opened successfully in Read only mode.." )

    Content = FileObject.read( ) 

    print ( )

    print( Content )

