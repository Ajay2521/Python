# In this lets see about "Deleting the String Datatype" in Python.

# Strings are immutable in Python.

# Thus string cannot deleteor remove the character from the string.

# But "del" is the keyword used to delete the entire string. 

Name = 'Maayon' # String inside single quotes.

print ( "\nBefore using \"del\" keyword for deletion the value is : " , Name )

print ( )

del Name

print ( "\nAfter using \"del\" keyword for deletion the value is : " , Name ) # Result in error since the variable Name has been deleted using del keyword.

