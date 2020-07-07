# In this lets see "format()" in Python

# The format() method is the most flexible and useful method in formatting strings.

# The curly braces {} are used as the placeholder in the string and replaced by the format() method argument. 

# format() can be used in three different ways, they are

# Using Curly Braces - {}

# Using Curly Braces with Positional Argument - { 1 }

# Using Curly Braces with Keyword Argument - { Name }

# Here is the Program for format()

# Using Curly braces

print ( "\n{} and {} both are the best friend...".format ( "Maayon","Aj"))  
  
# Positional Argument  

print ( "\n{1} and {0} both are the best friend...".format ( "Maayon" , "Aj" ) )  
  
# Keyword Argument  

print ( "\n{frnd1} and {frnd2} both are the best friend...".format ( frnd1 = "Maayon" , frnd2 = "Aj" ) )  