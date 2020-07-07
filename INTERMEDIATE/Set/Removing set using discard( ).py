# In this lets see more about "Removing item from Set Datatype" in Python.

# discard ( ) and remove ( ) is the function used to remove some particular item from the set.

# discard ( ) if the item does not exist in the set then the set remain unchanged.

# remove ( ) will through an error if the item does not exit in the set.

# Here is the program to "Removing item from set using discard ( )" in python.

Set = set( [ "Maayon" , 19, "Techgen" ] )

print ( "\nThe value stored in Set is Before using discard ( ) : " , Set )

Set.discard ( "Techgen" ) 

print ( "\nThe value stored in Set is After using discard ( ) for First time : " , Set ) # The set "techgen" has been removed.

Set.discard ( "Techgen" ) 

print ( "\nThe value stored in Set is After using discard ( ) for Second time : " , Set ) # The set "techgen" has been removed already thus there is no work for discard here.



