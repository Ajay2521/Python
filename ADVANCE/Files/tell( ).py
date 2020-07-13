# In this lets see about "File Handling in python."

# tell( ) - Used to return the position of the byte in the file using filepointer.
 
# Note : By default the file pointer will be at 0 position when the file is opened in read or write mode.

# Here is the Program for "tell ( ) in file"

# open the file File.txt in read mode.
    
FilePtr = open("File.txt","r")    
  
# Initially the filepointer is at 0 .
     
print( "\nThe filepointer is at byte position before reading the file : " , FilePtr.tell( ) )    
    
# Reading the content of the file.
    
FilePtr.read( )    
    
# After the read operation file pointer modifies. tell() returns the location of the FilePtr.     
    
print("\nThe filepointer is at byte position after reading the file : " , FilePtr.tell( ) )    
    

    