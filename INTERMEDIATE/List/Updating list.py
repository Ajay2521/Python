# In this lets see about "Updating the List" in Python.

# Since List are mutable , their values can be updated by using the slice and assignment operator.

# append() and insert() are the methods, which is used to add values to the list.

list = [1, 2, 3, 4, 5, 6]

print ( )

print ( list ) 

# It will assign value to the value to the second index   

list [ 0 ] = 10

print ( )

print ( list )

# Adding multiple element   

list [ 1 : 5 ] = [ 20, 30 , 40 , 50 ]

print ( )

print ( list )

# It will add value at the end of the list  

list [ -1 ] = 60  

print ( )

print ( list )
