# In this lets see about "File Handling in python."

# Writing into the file :

# write( ) = Used to write into the file theen the specific file must be opened in either write mode or append mode.

# w ( Write Mode ) = It will overwrite the file if any file exists. The file pointer is at the beginning of the file.

# a ( append mode ) = It will append the existing data in the file. The file pointer is at the end of the file.

# Here is the program for "write( ) in file."

# Opening file in append mode.

FileObj = open( "FileAppend.txt" , "a" )

# writing the content by appending to the existing data in the file.

FileObj.write( "\nIts an power packed programming language used for DataScience." )

# closing the opened file.

FileObj.close( )

