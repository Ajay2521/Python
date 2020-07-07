# In this lets see about "Set Operations" in Python.

# Python provides certain set Operation which is avaliable in mathematics such as

# 1) union

# 2) intersection

# 3) difference

# 4) symmetric difference

# In this lets see about "symmetric difference of two set"

# The symmetric difference of the two sets A and B, and the symmetric difference is A ^ B that denotes the resulting set will be obtained that element of both A and B which is not present in both sets.

# ( ^ ) operator is used to denote symmetric difference of two set.

#  symmetric_difference ( ) - is also used to find symmetric difference of two set.

# Here is the program for "symmetric difference of two set"

Month1 = set ( [ "January" , "February" , "March" , "April" , "May" , "June" , "December" ] ) 

Month2 = set ( [ "May" , "July" , "August" , "September" , "October" , "November" , "December" ] )   

print ( "\nSymmetric difference of two set using \"( ^ )\" Operator...\n\n" , Month1 ^ Month2 ) # Using ( ^ ) Operator.

print ( "\nSymmetric difference of two set using symmetric_difference ( ) Method...\n\n" , Month1.symmetric_difference ( Month2 ) ) # Using  symmetric_difference ( ) method.

