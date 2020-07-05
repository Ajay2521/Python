# In this lets see more about "Removing item from Set Datatype" in Python.

# discard ( ) and remove ( ) is the function used to remove some particular item from the set.

# discard ( ) if the item does not exist in the set then the set remain unchanged.

# remove ( ) will through an error if the item does not exit in the set.

# Here is the program to "Removing item from set using remove ( )" in python.

Set = set( [ "Maayon" , 19, "Techgen" ] )

print ( "\nThe value stored in Set is Before using remove ( ) : " , Set )

Set.remove ( "Techgen" ) 

print ( "\nThe value stored in Set is After using remove ( ) for First time : " , Set ) # The set "techgen" has been removed.

print ( )

Set.remove ( "Techgen" ) 

print ( "\nThe value stored in Set is After using remove ( ) for Second time : " , Set ) # Since "Techgen" doesn't exit it will be resulting in an error.

