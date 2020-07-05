# In this lets see about "Set Operations" in Python.

# Python provides certain set Operation which is avaliable in mathematics such as

# 1) uni
# 2) intersection

# 3) difference

# 4) symmetric difference

# In this lets see about "difference of two set"

# The difference of the two sets A and B, and the difference is A - B that denotes the resulting set be obtained that element of A, which is not present in the set B.

# subtraction ( - ) operator is used to denote difference of two set.

# difference ( ) - is also used to find difference of two set.

# Here is the program for "difference of two set"

Month1 = set ( [ "January" , "February" , "March" , "April" , "May" , "June" , "December" ] ) 

Month2 = set ( [ "May" , "July" , "August" , "September" , "October" , "November" , "December" ] )   

print ( "\nDifference of two set using \"subtraction ( - )\" Operator...\n\n" , Month1 - Month2 ) # Using subtraction ( - ) Operator.

print ( "\nDifference of two set using difference ( ) Method...\n\n" , Month1.difference ( Month2 ) ) # Using  difference ( ) method.

