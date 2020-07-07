# In this lets see about "Deleting the Tuple Datatype" in Python.

# Tuple are immutable in Python.

# Thus tuple cannot be delete or remove the character from the tuple.

# But by using "del" keyword it is possible to delete the entire tuple. 

tuple1 = [ 1, 2, 3, 4, 5, 6 ] 

print ( "\nBefore using \"del\" keyword for deletion the value is : " , tuple1 )

print ( )

del tuple1

print ( "\nAfter using \"del\" keyword for deletion the value is : " , tuple1 ) # Result in error since the variable Name has been deleted using del keyword.


