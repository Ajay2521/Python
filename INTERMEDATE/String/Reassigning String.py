# In this lets see about "Reassigning the String Datatype" in Python.

# Strings are immutable in Python.

# Thus string can only be replaced with new string since its content cannot be partially replaced.

Name = 'Maayon' # String inside single quotes.

Name = 'MAAYON'

print ( Name ) # This will be not resulting in error since String has been replaced completely.

print ( )

Name = 'Maayon' # String inside single quotes.

Name [ 0 ] = 'm'

print ( Name ) # This will be resulting in error since String must be replaced completely.
