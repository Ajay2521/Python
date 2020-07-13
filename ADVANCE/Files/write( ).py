# In this lets see about "File Handling in python."

# Writing into the file :

# write( ) = Used to write into the file theen the specific file must be opened in either write mode or append mode.

# w ( Write Mode ) = It will overwrite the file if any file exists. The file pointer is at the beginning of the file.

# a ( append mode ) = It will append the existing data in the file. The file pointer is at the end of the file.

# Here is the program for "write( ) in file."

# Opening file in write mode.

FileObj = open( "File.txt" , "w" )

# writing the content by overwriting the file.

FileObj.write( "Python is an demanding program now a days.\nIt is simple to learn and very effective." )

# closing the opened file.

FileObj.close( )

