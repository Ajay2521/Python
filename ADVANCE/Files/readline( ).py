# In this lets see about "File Handling in python."

# Reading from the file by readline( ) :

# readline( ) = Used to read the file line by line. 

# Here is the program for "readline( )."

# Opening file in read mode.

FileObj = open( "File.txt" , "r" )

# Reading the data from the file by line by line using readline( ).

print ( )

print( FileObj.readline( ) )

# closing the opened file.

FileObj.close( )

