# In this lets see about "File Handling in python."

# To create a file x, w, a are used.

# x = It creates a new file with the specified name. It causes an error a file exists with the same name.

# a = It creates a new file with the specified name if no such file exists. It appends the content to the file if the file already exists with the specified name.

# w = It creates a new file with the specified name if no such file exists. It overwrites the existing file.

# Here is the Program for "Open ( ) in file"
 
FileObj = open( "FileCreate.txt" , "x" )

if FileObj:
    
    print( "\nFile has been created successfully..." )
