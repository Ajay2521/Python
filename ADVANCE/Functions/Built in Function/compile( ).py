# In this lets see about the "Built-in functions" in python.

# Built-in function is defined as the functions whose functionality is pre-defined in the python compiler.

# Lets see about "compile( ) bilt-in function" in python.

# compile( ) - Used to  takes source code as input and returns a code object which can later be executed by exec() function.

# Here is the program for compile( ).

SourceCode = 'a = 10\nb = 20\nsum = a + b\nprint ( "sum of a and b = " , sum ) '

CompileCode = compile( SourceCode, 'Sum', 'exec' )

print ( ) # Prints new line for readability.

print( type( CompileCode ) )

print ( ) # Prints new line for readability.

exec( CompileCode )
