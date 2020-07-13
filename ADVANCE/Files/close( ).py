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

# Closing file:

# close( ) = Used to close the file.

# It is important to use close( ) when a file is opened in the program.

# Syntax for close( ) is:

# FileObject.close( )

# Here is the program for "close( ) in python".

# Opening a file using open( ).

FileObject = open( "File.txt" , "r" )

if FileObject:

    print ( )

    print( FileObject )

    print( "\nFile has been opened successfully in Read only mode.." )

# Closing a file using close( ).

FileObject.close( )

print( )

print( FileObject )

print( "\nFile has been closed successfully at the end..." )
