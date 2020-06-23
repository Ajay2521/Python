#In this "Logical Operators" concept in Python Program has been explained.

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

#Lets see about "Logical Operators" in Python Program.

#Majorly Logical Operation is :

#1) and

#2) or

#3) not

#When boolean condition "and" is used then the condition is true only is the value is true else it result in false.

#When boolean condition "or" is used then the condition is true if any of the value is true else it false is no value is true.

#Here is the Python Program for Logical Operators

a = 10 #True

b = 10 #True

c = 0 #False

if a and b :

	print("\nThe Value of \"a\" and \"b\" is TRUE...")

else :

	print("\nThe Value of \"a\" and \"b\" is FALSE...")

if b and c :

	print("\nThe Value of \"b\" and \"c\" is TRUE...")

else :

	print("\nThe Value of \"b\" and \"c\" is FALSE...")

if b or c :

	print("\nThe Value of \"b\" is True... or The Value of \"c\" is TRUE...")

else:

	print("\nThe Value of both \"b\" and \"c\" is FALSE...")

if not a:

	print("\nBoolean value of \"a\" is TRUE...")

else :

	print("\nBoolean value of \"a\" is FALSE...")

if not b:

	print("\nBoolean value of \"b\" is TRUE...")

else :

	print("\nBoolean value of \"b\" is FALSE...")

if not c:

	print("\nBoolean value of \"c\" is TRUE...")

else :

	print("\nBoolean value of \"c\" is FALSE...")
