# In this lets see about "File Handling in python."

# Reading from the file :

# read( ) = Used to reads a string from the file.

# syntax for read( ) :

# FileObject.read( count )

# count = Is the number of bytes to be read from the file starting from the beginning of the file. If the count is not specified, then it may read the content of the file until the end.

# Note in order to print all data from the file then it is optional to use count value.

# Here is the program for "read( ) from file."

# Opening file in read mode.

FileObj = open( "File.txt" , "r" )

# Reading the data from the file.

print ( )

print( FileObj.read( ) )

# closing the opened file.

FileObj.close( )

