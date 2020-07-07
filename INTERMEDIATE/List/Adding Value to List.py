# In this lets see about "Addingthe List" in Python.

# append() function which is used to add an element to the list.

# append() function can only add value to the end of the list.

# Declaring the list

list = [ 1, 2, 3, 4, 5 ]

# Number of elements will be entered by the user.    

n = int( input ( "\nEnter the number of elements in the list : " ) )  

# for loop to take the input from user

for i in range ( 0 , n ):   

	list.append ( input ( "\nEnter the item : " ) )

print ( "\nThe Value present in the list is : " )

for i in list :

	print ( )

	print ( i )   
