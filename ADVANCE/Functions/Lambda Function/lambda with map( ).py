# In this lets see about "Lambda function" in Python.

# Lambda function is known as the anonymous function that is defined without a name.

# The anonymous functions are declared by using the lambda keyword.

# Note Lambda function returns only one value even it accept multiple values.

# Here is the program for "lambda Function with map( )"

List = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13, 14, 15 ]

Power = map( lambda n : pow( n ,2 ) , List )

print ( "\nThe power value is : \n" )

print( Power )

print ( list( Power ) )



