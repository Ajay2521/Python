# In this lets see about "call by reference functions" in Python.

# Call by Reference is defined as the passing the actual value as an argument in the function.

# By default all the functions are called by reference in python.

# In simple all the changes made to the reference inside the function revert back to the original value referred by the reference.

# Here is the program for "Call by Reference by passing the mutable datatype list"

# defining the value of the list

List = [ 10 , 20 , 30 ]

print ( "\nThe value of the list before calling the function is : " , List )

# defining the function to add the values to the list at last place.

def add_list( List ) :

	List.append ( 40 )

	List.append ( 50 )

	print ( "\nThe value of the list inside the function is : " , List )

# calling the function 

add_list( List )

print ( "\nThe value of the list outside the function is : " , List )


