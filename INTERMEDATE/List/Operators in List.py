# In this lets see about "List Operators" in Python

# Majorly used List Operators are

# 1) Concatenation Operator ( + )

# 2) Repetition Operator ( * )

# 3) Membership Operator ( in , not in )

# 4) Iteration ( for loop )

# 5) Length ( len () )

# Lets see all this Operators in detail in the program.

list = [ 1, 2, 3, 4, 5  ]

list1 = [ 6, 7, 8, 9, 10 ]

# Concatention Operator ( + ) - Used to Concate ( Combine ) two or more list.

print ( "\nConcatention of \"" , list , "\" and \"" , list1 , "\" is : " , list + list1 )

# Repetition Operator ( * ) - Used to print the copy of that list for defined value.

print ( "\nRepetition of \"" , list , "\" for 3 times is : " , list * 3 )

# Membership Operator ( in ) - Used to check and print true if the value is present in it , else it print false. 

print ( "\nChecking for \"2\" in \"" , list , "\" using Membership Operator \"in\" is : " , 2 in list )

# Membership Operator ( not in ) - Used to check and print true if the value is not present in it , else it print true. 

print ( "\nChecking for \"2\" in \"" , list , "\" using Membership Operator \"not in\" is : " , 2 not in list )

# The i is a variable will iterate over the elements of the List and contains each element in each iteration.

for i in list:

	print ( )

	print ( i )

# Length ( len () ) - which is used to return the size of the list.

print ( "\nThe Length of the \"list\" is : " , len ( list ) )

