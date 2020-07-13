# In this lets see about "File Handling in python."

# Reading from the file using loop :

# By using the loop we can able to print the data from the file.
 
# Here is the program for "reading from the file using loop."

# Opening file in read mode.

FileObj = open( "File.txt" , "r" )

# Reading the data from the file using loop.

print ( )

for data in FileObj:

    print( data ) # prints each line from the file.
    
# closing the opened file.

FileObj.close( )

