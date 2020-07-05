# In this lets see more about "tuple Datatype" in Python.

# A tuple in Python is used to store the sequence of various types of data.

# The items in the tuple are separated with the comma ( , ) and enclosed with the square brackets [ ].

# Characteristics of tuple are as follow :

# 1) tuple are "Ordered".

# 2) Elements of the tuple can be accessed by using "Index" as same as String.

# 3) tuple are "Mutable".

# 4) tuple can able to store various data elements.

# Here is the Program to understand "Slicing the tuple"

# The elements of the tuple can be accessed by using the slice operator [].

# The index starts from 0 and goes to length - 1 of the length of tuple.

# Syntax for getting sub - tuple by Slice and range is

# tuple_variable ( Start : Stop : Step Size )

# Start - Is the Starting Index position of the tuple.

# Stop - Is the Last Index position of the tuple.

# Step Size - Is the used to skip the nth element within the start and stop.

tuple = ( 1 , 2, 3, 4, 5 , 6 )

# Slicing the elements.

print ( "\nSlicing element in the index place 3 : " , tuple [ 3 ] )

# Slicing the elements using Range.

print ( "\nAll the value of the \"tuple\" is : " , tuple [ : ] )

print ( "\nAll the elements after the index value 2 is : " , tuple [ 2 : ] )

print ( "\nAll the elements in the range from index value 1 to index value 4 is : " , tuple [ 1 : 4 ] )

print ( "\nAll the elements in the range from index value 0 to index value 5  with the Step size oftwo element is : " , tuple [ 0 : 5 : 2 ] )



