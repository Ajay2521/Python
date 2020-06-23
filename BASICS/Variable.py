#In this lets see the concept of variable in Python Programming.

#Varaible are used to store the value in a prticular memory location.

#That is variable is a name which is used to refer memory location.

#Variables are also known as "IDENTIFIER".

#In python varaibles are declared only by means of it name rather than by using its datatype and name.

#Since Python compilers are build in such a way that it automatically finds the datatype of the variable and assign it to that variable.

#NOTE : There are certain rules to be followed while declaring a variable in Python program . They are as follow :

#1) The first  character of the variable must be an alphabet or underscore ( _ ).

#2) All the characters except the first character may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore or digit (0-9).

#3) Variable must not contain any space or special characters like !, @, #, %, ^, &, * .

#4) Variable must not be similar as any of the keyword which is defined by the program compiler .

#5) Variables are case sensitive , for example "Maayon" and "maayon" are not the same.

#NOTE : Once the variable is declared then value assigning to that variable can be done both "Dynamically(while running the program)" or "Statically (Pre defined in the program itself.)".

#To assign a value to a variable "equal operator ( = )" has to be used.

#Here is the program for variable and its type in Python

#declaring and assigning a value to a variable

a = 10

b = 10.12

c = 'a'

d = "Maayon"

#Printing the value of varaible and finding its datatype using type() function.

#Here a special character "\n" has been used which is used to print new line. NO WORRIES , it will be explained in "Escape sequence" chapter.

print("\nThe Value of \"a\" is : " , a , "\nThe Datatype of variable \"a\" is : ", type(a) )

print("\nThe Value of \"b\" is : " , b , "\nThe Datatype of variable \"b\" is : ", type(b) )

print("\nThe Value of \"c\" is : " , c , "\nThe Datatype of variable \"c\" is : ", type(c) )

print("\nThe Value of \"d\" is : " , d , "\nThe Datatype of variable \"a\" is : ", type(d) )

