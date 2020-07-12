# In this lets see about the "Built-in functions" in python.

# Built-in function is defined as the functions whose functionality is pre-defined in the python compiler.

# Lets see about "open( ) bilt-in function" in python.

# open( ) - Used to open an file and return the data in it.

# Note : By default the file is opened in "Read only ( r ) mode".

# Here is the program for open( ).

# Opening a file by using its name which is already created .

print( "\nOpening the file by using its Name...\n" )

File = open ( "OpenFile.txt" ) 

print( File.read( ) )

# Opening a file by using its path which is already created .

print( "\nOpening the file by using its path...\n" )

File = open ( "C:/Users/MAAYON/Desktop/Python/ADVANCE/Functions/Built in Function/OpenFile.txt" ) 

print( File.read( ) )

