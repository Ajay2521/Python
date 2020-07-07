# In this lets see about "FrozenSet Datatype" in Python.

# Frozen set is a type of set which is immutable one.

# The elements of the frozen set cannot be changed after the creation.

# The frozenset() method is used to create the frozenset object.

# Here is the Program for "Frozenset"

Frozen_set = frozenset ( [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] )

print ( ) # Prints new line for Readability.

print ( Frozen_set )

print ( ) # Prints new line for Readability.

print ( type ( Frozen_set ) )

print ( ) # Prints new line for Readability.

Frozen_set.add ( 10 ) # This addition of element to the frozenset will result in error.

