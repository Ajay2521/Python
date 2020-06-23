#In this "Membership Operators" concept in Python Program has been explained.

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

#Lets see about "Membership Operators" in Python Program.

#It used to check the membership of value inside a Python data structure.

#If the value is present in the data structure, then the resulting value is true otherwise it returns false.

#The two Membership Operation is :

#1) in - It is evaluated to be true if the first operand is found in the second operand (list, tuple, or dictionary).

#2) not in - It is evaluated to be true if the first operand is not found in the second operand (list, tuple, or dictionary)

#Here is the Python Program for Membership Operators

a = 5

b = 10

list = [ 1, 2, 3, 4, 5] 

if ( a in list ) :

	print("\nThe value of \"a\" is Present in the list...")

else :

	print("\nThe value of \"a\" is Not Present in the list...")

if ( b in list ) :

	print("\nThe value of \"b\" is Present in the list...")

else :

	print("\nThe value of \"b\" is Not Present in the list...")

if ( a not in list ) :

	print("\nThe value of \"a\" is Not Present in the list...")

else :

	print("\nThe value of \"a\" is Present in the list...")

if ( b not in list ) :

	print("\nThe value of \"b\" is Not Present in the list...")

else :

	print("\nThe value of \"b\" is Present in the list...")
