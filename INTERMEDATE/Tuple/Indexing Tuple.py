# Here is the Program to understand "Indexing the tuple"

# Indexing the tuple is as same as indexing the list.

# The elements of the tuple can be accessed by using the slice operator [].

# The index starts from 0 and goes to length - 1 of the length of tuple.

tuple = ( "Maayon" , 19, "Techgen" )

print ( "\nThe Value present at the First Place in the tuple is : " , tuple [ 0 ] ) # Print the Value present in the index [ 0 ].

print ( "\nThe Value present at the Second Place in the tuple is : " , tuple [ 1 ] ) # Print the Value present in the index [ 1 ].

print ( "\nThe Value present at the Thrid Place in the tuple is : " , tuple [ 2 ] ) # Print the Value present in the index [ 2 ].

print()

# This will Result in Error , Since the tuple contains only 3 Values which is index[ 2 ] . Therefore index[ 3 ] will be resulting in Error.

print ( "\nThe Value present at the Fourth in the tuple is : " , tuple [ 4 ] ) # Print the Value present in the index [ 3 ].



