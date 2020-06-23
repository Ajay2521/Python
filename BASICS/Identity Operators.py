#In this "Identity Operators" concept in Python Program has been explained.

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

#Lets see about "Identity Operators" in Python Program.

#It used to check the reference of value present inside both Python data structure.

#If the value is present in both the data structure, then the resulting value is true otherwise it returns false.

#The twoIdentity Operation is :

#1) is - It is evaluated to be true if the reference present at both sides point to the same object.

#2) is not - It is evaluated to be true if the reference present at both side do not point to the same object.

#Here is the Python Program for Identity Operators

a = 5

b = 5

c = 10

if ( a is b ) :

	print("\nThe value of \"a\" and \"b\" have same identity...")

else :

	print("\nThe value of \"a\" and \"b\" do not have same identity...")
	
if ( a is c ) :

	print("\nThe value of \"a\" and \"c\" have same identity...")

else :

	print("\nThe value of \"a\" and \"c\" do not have same identity...")

if ( b is c ) :

	print("\nThe value of \"b\" and \"c\" have same identity...")

else :

	print("\nThe value of \"b\" and \"c\" do not have same identity...")

if ( a is not b ) :

	print("\nThe value of \"a\" and \"b\" do not have same identity...")

else :

	print("\nThe value of \"a\" and \"b\" have same identity...")

if ( a is not c ) :

	print("\nThe value of \"a\" and \"c\" do not have same identity...")

else :

	print("\nThe value of \"a\" and \"c\" have same identity...")

if ( b is not c ) :

	print("\nThe value of \"b\" and \"c\" do not have same identity...")

else :

	print("\nThe value of \"b\" and \"c\" have same identity...")
