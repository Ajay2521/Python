# In this lets see about "Set Comparisons" in Python.

# Comparison Operators are used to check wherether set is a subset, superset, or equivalent to other set.

Days = { "Monday" , "Tuesday" , "Wednesday" , "Thursday" ,  "Friday" , "Saturaday " , "Sunday" }    

WeekDays = { "Monday" , "Tuesday" , "Wednesday" , "Thursday" ,  "Friday" }    

WeekEndDays = { "Saturaday " , "Sunday" }    
   
print ( ) # Prints New line for Readability.

# Days is the superset of WeekDays hence it will print true.   

print ( Days > WeekDays )     

print ( ) # Prints New line for Readability.    

# prints false since Days is not the subset of WeekDays

print ( Days < WeekDays )    

print ( ) # Prints New line for Readability.

# prints false since WeekDays is not the subset of WeekEndDays

print ( WeekDays < WeekEndDays )    

print ( ) # Prints New line for Readability.    
    
# prints false since WeekDays and WeekEndDays are not equivalent 

print ( WeekDays == WeekEndDays )

