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
 
# Opening a file :

# open( ) - Used to open  a file.

# Open( ) accepts two arguments.

# First argument - Is the File name to be opened.

# Second argument - Is the mode in which the file has to be opened. 

# Syntax for open( ) :

# FileObject = open( FileName , AccessMode )

# Different Access Mode in file handling is :

# r = Opens the file in Read only mode.

# rb = Opens the file in Read only mode in binary format.

# r+ = Opens the file in both Read and Write mode.

# rb+ = Opens the file in both Read and Write mode in binary format.

# w = Opens the file in Write only mode.

# wb = Opens the file in Write only mode in binary format.

# w+ = Opens the file in both Read and Write mode.

# wb+ = Opens the file in both Read and Write mode in binary format.

# a = Opens the file in append mode.

# ab = Opens the file in append mode in binary format.

# a+ = Opens the file in both Read and Append mode.

# ab+ = Opens the file in both Read and Append mode in binary format.
                  
# Here is the Program for "Open ( ) in file"
 
FileOpen = open( "File.txt" , "r" )

if FileOpen:

    print ( )

    print( FileOpen )

    print( "\nFile has been opened successfully in Read only mode.." )
