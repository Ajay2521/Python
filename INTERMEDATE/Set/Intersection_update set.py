# In this lets see about "Set Operations" in Python.

# Python provides certain set Operation which is avaliable in mathematics such as

# 1) union

# 2) intersection

# 3) difference

# 4) symmetric difference

# In this lets see about "intersection of two set"

# The intersection of the two sets is given as the set of the elements that common in both sets.

# intersection_update() method removes the items from the original set that are not present in both the sets.

# The intersection_update() method is different from the intersection() method since it modifies the original set by removing the unwanted items.

# Where intersection() method returns a new set.

# Here is the program for "intersection of two set"

Month1 = set ( [ "January" , "February" , "March" , "April" , "May" , "June" , "December" ] ) 

Month2 = set ( [ "May" , "July" , "August" , "September" , "October" , "November" , "December" ] )   

print ( "\nValue present in set \"Month1\" Before using intersection_update ( ) ...\n\n " , Month1 )

Month1.intersection_update ( Month2 )

print ( "\nValue present in set \"Month1\" After using intersection_update ( ) ...\n\n " , Month1 )