# In this lets see about "String Operators" in Python

# Majorly used String Operators are

# 1) Concatenation Operator ( + )

# 2) Repetition Operator ( * )

# 3) Slice Operator ( [] )

# 4) Range Slice Operator ( [ : ] )

# 5) Membership Operator ( in , not in )

# 6) Raw String Operator ( r / R )

# 7) Format Specifier Operator ( % )

# Lets see all this Operators in detail in the program.

str = "Hello"

str1 = " Maayon"

# Concatention Operator ( + ) - Used to Concate ( Combine ) two or more String.

print ( "\nConcatention of \"" , str , "\" and \"" , str1 , "\" is : " , str + str1 )

# Repetition Operator ( * ) - Used to print the copy of that string defined value.

print ( "\nRepetition of \"" , str1 , "\" for 3 times is : " , str1 * 3 )

# Slice Operator ( [ ] ) - Used for indexing the string.

print ( "\nSlice[ 3 ] of \"" , str1 , "\" is : " , str1 [ 3 ] )

# Range Slice Operator ( [ : ] ) - Used for indexing the string of particular range.

print ( "\nRange Slice[ 2 : 5 ] of \"" , str1 , "\" is : " , str1 [ 2 : 5 ] )

# Membership Operator ( in ) - Used to check and print true if the value is present in it , else it print false. 

print ( "\nChecking for \"y\" in \"" , str1 , "\" using Membership Operator \"in\" is : " , 'y' in str1 )

# Membership Operator ( not in ) - Used to check and print true if the value is not present in it , else it print true. 

print ( "\nChecking for \"y\" in \"" , str1 , "\" using Membership Operator \"not in\" is : " , 'y' not in str1 )

# Raw String Operator ( r / R ) - Used in the cases where need to print the actual meaning of escape characters.

print ( "\nPrinting the value using Raw String Operator ( R ) is : " , R'D::\\$$Python' )

# Format Specifier Operator ( % ) - Used to specify the format as such as in C Program.

print ( "\nThe Value of String str1 is : %s " %(str1) )