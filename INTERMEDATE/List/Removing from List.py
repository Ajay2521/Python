# In this lets see about "Removing an element from the list" in python.

# remove() is the function which is used to remove the element from the list.

list = [ 1, 2, 3, 4, 5 ]

print ( "\nPrinting the list Before using remove()...\n" )

for i in list:    

    print ( i , end = " " )    

list.remove ( 3 )    

print("\n\nPrinting the list After using remove( 3 )...\n")    

for i in list:    

    print ( i , end = " " )    

print ( )