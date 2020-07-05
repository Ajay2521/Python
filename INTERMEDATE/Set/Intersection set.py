# In this lets see about "Set Operations" in Python.

# Python provides certain set Operation which is avaliable in mathematics such as

# 1) union

# 2) intersection

# 3) difference

# 4) symmetric difference

# In this lets see about "intersection of two set"

# The intersection of the two sets is given as the set of the elements that common in both sets.

# and ( & ) operator is used to denote intersection of two set.

# intersection ( ) - is also used to find intersection of two set.

# Here is the program for "intersection of two set"

Month1 = set ( [ "January" , "February" , "March" , "April" , "May" , "June" , "December" ] ) 

Month2 = set ( [ "May" , "July" , "August" , "September" , "October" , "November" , "December" ] )   

print ( "\nIntersection of two set using \"and ( & )\" Operator...\n\n" , Month1 & Month2 ) # Using and ( & ) Operator.

print ( "\nIntersection of two set using intersection ( ) Method...\n\n" , Month1.intersection ( Month2 ) ) # Using intersection ( ) method.

