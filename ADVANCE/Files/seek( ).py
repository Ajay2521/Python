# In this lets see about "File Handling in python."

# It is poissible to change the file pointer postion externally in python program.

# seek( ) - Used to modify the file pointer position externally while wrtiting the program.  
 
# syntax for seek( ) :

# filepointer.seek( offset, form )

# offset = It refers to the new position of the file pointer.  

# from = It indicates the reference position from where the bytes are to be moved.  
 
# Here is the Program for "seek ( ) in file"

# open the file File.txt in read mode.
    
FilePtr = open("File.txt","r")    
  
# Initially the filepointer is at 0 .
     
print( "\nThe filepointer is at byte position before changing the file pointer position externally : " , FilePtr.tell( ) )    
    
#changing the file pointer location to 20.    

FilePtr.seek( 20 )

# After the changing the file pointer position to 20. tell() returns the location of the FilePtr.     
    
print("\nThe filepointer is at byte position after changing the file pointer position externally for the first time : " , FilePtr.tell( ) )    

#changing the file pointer location to 50.    

FilePtr.seek( 50 )

# After the changing the file pointer position to 50. tell() returns the location of the FilePtr.     
    
print("\nThe filepointer is at byte position after changing the file pointer position externally for the second time : " , FilePtr.tell( ) )    


    