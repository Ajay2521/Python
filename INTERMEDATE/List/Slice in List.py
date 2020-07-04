# In this lets see more about "List Datatype" in Python.

# A list in Python is used to store the sequence of various types of data.

# The items in the list are separated with the comma ( , ) and enclosed with the square brackets [ ].

# Characteristics of List are as follow :

# 1) List are "Ordered".

# 2) Elements of the list can be accessed by using "Index" as same as String.

# 3) List are "Mutable".

# 4) List can able to store various data elements.

# Here is the Program to understand "Slicing the list"

# The elements of the list can be accessed by using the slice operator [].

# The index starts from 0 and goes to length - 1 of the length of List.

# Syntax for getting sub- list by Slice and range is

# list_variable ( Start : Stop : Step Size )

# Start - Is the Starting Index position of the list.

# Stop - Is the Last Index position of the list.

# Step Size - Is the used to skip the nth element within the start and stop.

List = [ 1 , 2, 3, 4, 5 , 6]

# Slicing the elements.

print ( "\nSlicing element in the index place 3 : " , List [ 3 ] )

# Slicing the elements using Range.

print ( "\nAll the value of the \"List\" is : " , List [ : ] )

print ( "\nAll the elements after the index value 2 is : " , List [ 2 : ] )

print ( "\nAll the elements in the range from index value 1 to index value 4 is : " , List [ 1 : 4 ] )

print ( "\nAll the elements in the range from index value 0 to index value 5  with the Step size oftwo element is : " , List [ 0 : 5 : 2 ] )



