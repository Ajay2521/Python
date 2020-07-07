# In this lets see about "Set Operations" in Python.

# Python provides certain set Operation which is avaliable in mathematics such as

# 1) union

# 2) intersection

# 3) difference

# 4) symmetric difference

# In this lets see about "union of two set"

# The union of the two sets contains all the items that are present in both the sets.

# pipe ( | ) operator is used to denote Union of two set.

# union ( ) - is also used to find union of two set.

# Here is the program for "Union of two set"

Month1 = set ( [ "January" , "February" , "March" , "April" , "May" , "June" ] ) 

Month2 = set ( [ "July" , "August" , "September" , "October" , "November" , "December" ] )   

print ( "\nUnion of two set using pipe \"|\" Operator...\n\n" , Month1 | Month2 ) # Using pipe ( | ) Operator.

print ( "\nUnion of two set using union ( ) Method...\n\n" , Month1.union ( Month2 ) ) # Using union ( ) method.



