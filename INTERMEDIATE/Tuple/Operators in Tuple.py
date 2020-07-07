# In this lets see about "Tuple Operators" in Python

# Majorly used Tuple Operators are

# 1) Concatenation Operator ( + )

# 2) Repetition Operator ( * )

# 3) Membership Operator ( in , not in )

# 4) Iteration ( for loop )

# 5) Length ( len () )

# Lets see all this Operators in detail in the program.

Tuple = ( 1, 2, 3, 4, 5 )

Tuple1 = ( 6, 7, 8, 9, 10 )

# Concatention Operator ( + ) - Used to Concate ( Combine ) two or more Tuple.

print ( "\nConcatention of \"" , Tuple , "\" and \"" , Tuple1 , "\" is : " , Tuple + Tuple1 )

# Repetition Operator ( * ) - Used to print the copy of that Tuple for defined value.

print ( "\nRepetition of \"" , Tuple , "\" for 3 times is : " , Tuple * 3 )

# Membership Operator ( in ) - Used to check and print true if the value is present in it , else it print false. 

print ( "\nChecking for \"2\" in \"" , Tuple , "\" using Membership Operator \"in\" is : " , 2 in Tuple )

# Membership Operator ( not in ) - Used to check and print true if the value is not present in it , else it print true. 

print ( "\nChecking for \"2\" in \"" , Tuple , "\" using Membership Operator \"not in\" is : " , 2 not in Tuple )

# The i is a variable will iterate over the elements of the Tuple and contains each element in each iteration.

for i in Tuple:

	print ( )

	print ( i )

# Length ( len () ) - which is used to return the size of the Tuple.

print ( "\nThe Length of the \"Tuple\" is : " , len ( Tuple ) )

