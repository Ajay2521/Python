# In this lets see more about "String Datatype" in Python.

# String datatype in Python is defined as the "collection of characters which are present inside single quotes ( ' ' ) or double quotes ( " " ) or triple quotes ( """ """ or ''' ''') " .

# Since computer does not understand the characters , therefore each and every characters are converted into 0's and 1's.

# This process of converting characters into 0's and 1's are done by considering the standard encoding method in ASCII or Unicode.

# Strings in python is also called as "Collection of Unicode Characters." 

# Indexing of Strings in python always starts from 0.

# Syntax for indexing string is 

# String_Variable[ i ]

# where [ i ], i can be a number which is used to indeciate the index value of the string . The starting index value is always 0 ( zero ).

# Here is the program for Indexing of Strings in Python.

Name = 'Maayon' #String inside single quotes.

# Printing all the characters of the String

print("\nThe complete value of the String is : " , Name ) 

# Printing the First characters of the String. 

print("\nThe First characters of the String is : " , Name[ 0 ] ) 

# Printing the Second characters of the String. 

print("\nThe Second characters of the String is : " , Name[ 1 ] ) 

# Printing the Third characters of the String. 

print("\nThe Third characters of the String is : " , Name[ 2 ] )

# Printing the Fourth characters of the String. 

print("\nThe Fourth characters of the String is : " , Name[ 3 ] )

# Printing the Fifth characters of the String. 

print("\nThe Fifth characters of the String is : " , Name[ 4 ] ) 

# Printing the Sixth characters of the String. 

print("\nThe Sixth characters of the String is : " , Name[ 5 ] , "\n" ) 
 
# Printing the Seventh characters of the String. 

# Note : Now we are trying to print a value which is not exist. 

# Thus it returns the IndexError because 6th index doesn't exist.  

print("\nThe Seventh characters of the String is : " , Name[ 6 ] ) 





