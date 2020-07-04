# In this lets see more about "List Datatype" in Python.

# A list in Python is used to store the sequence of various types of data.

# The items in the list are separated with the comma ( , ) and enclosed with the square brackets [ ].

# Characteristics of List are as follow :

# 1) List are "Ordered".

# 2) Elements of the list can be accessed by using "Index" as same as String.

# 3) List are "Mutable".

# 4) List can able to store various data elements.

# Here is the Program to understand "Indexing the list"

# The elements of the list can be accessed by using the slice operator [].

# The index starts from 0 and goes to length - 1 of the length of List.

List = [ "Maayon" , 19, "Techgen" ]

print ( "\nThe Value present at the First Place in the list is : " , List [ 0 ] ) # Print the Value present in the index [ 0 ].

print ( "\nThe Value present at the Second Place in the list is : " , List [ 1 ] ) # Print the Value present in the index [ 1 ].

print ( "\nThe Value present at the Thrid Place in the list is : " , List [ 2 ] ) # Print the Value present in the index [ 2 ].

print()

# This will Result in Error , Since the List contains only 3 Values which is index[ 2 ] . Therefore index[ 3 ] will be resulting in Error.

print ( "\nThe Value present at the Fourth in the list is : " , List [ 4 ] ) # Print the Value present in the index [ 3 ].



