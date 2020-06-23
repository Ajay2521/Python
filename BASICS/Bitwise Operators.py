#In this "Bitwise Operators" concept in Python Program has been explained.

#The operator can be defined as a symbol which is responsible for a particular operation between two operands.

#Operators are the pillars of a program on which the logic is built in any programming language.

#Majorly used Operators are :

#1) Arithmetic Operators

#2) Comparison operators

#3) Assignment Operators

#4) Logical Operators

#5) Bitwise Operators

#6) Membership Operators

#7) Identity Operators

#Lets see about "Bitwise Operators" in Python Program.

#Bitwise work such that it convert a normal Decimal numbers into Binary digits which is "1's" and "0's".

#Example - 2 in binary is considered as 10

#Thus bitwise is used to work with binary than decimal 

#Majorly Bitwise Operation is :

#1) Binary AND ( & )

#2) Binary OR ( | )

#3) Binary XOR ( ^ )

#4) Binary Ones Complement ( ~ )

#5) Binary Left Shift ( << )

#6) Binary Right Shift ( >> )

#Here is the Python Program for Bitwise Operators

a = 10            # 10 = 0000 1010 

b = 11            # 11 = 0000 1011 

c = 0

c = a & b        

print("\nThe Value of \"a\" & ( Binary AND ) \"b\" is : " , c )

c = a | b        

print("\nThe Value of \"a\" | ( Binary OR ) \"b\" is : " , c )

c = a ^ b        

print("\nThe Value of \"a\" ^ ( Binary XOR ) \"b\" is : " , c )

c = ~a           

print("\nThe Value of ~ ( Binary Once Complement ) \"~a\" is : " , c )

c = a << 2       

print("\nThe Value of \"a\" << ( Binary Left Shift ) of 2 is : " , c )

c = a >> 2       

print("\nThe Value of \"a\" >> ( Binary Right Shift ) of 2 is : " , c )
