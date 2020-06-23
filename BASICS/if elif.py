#In this program lets see about "Decision Making Statements " in Python Programming.

#Descion making statement is used to check for the condition and makes a flow in the program.

#There are 4 types of Decision Making Statement . They are :

#1) if

#2) if else

#3) if elif

#4) Nested if

#In this program lets see about "if elif Statement" in Python

#if elif statement is an Decision Making Statement which is used to check for Condition.

#If the condition is true for first if statement , then the code inside if block will be executed.

#else If the condition is true for First elif statement , then the code inside First elif block will be executed.

#else If the condition is true for Second elif statement , then the code inside Second elif block will be executed.

#else If the condition is true for "N"th elif statement , then the code inside "N"th elif block will be executed.

#else If the condition is false for all elif condition , then the code inside else block will be executed.

#Syntax for "if elif statement" is

#if( Conditional Expression ) :

#	Statement 1

#	Statement 2

#	Statement N

#elif( Conditional Expression 1 ) :

#	Statement 1

#	Statement 2

#	Statement N

#elif( Conditional Expression 2 ) :

#	Statement 1

#	Statement 2

#	Statement N

#elif( Conditional Expression N ) :

#	Statement 1

#	Statement 2

#	Statement N

#else :

#	Statement 1

#	Statement 2

#	Statement N

#Note : Since Python doesn't denote curly braces . Therefore "indentation" will play an imporatant role is makeing a block of code.

#Thus general four space or tab press is used to mention the indention in the program.

#Program for "if elif statement."

#Declaring Variable a = 10 to make if block to be executed.

a = 10

print("\nWhen a = 10.")

if ( a == 10 ) :

	print("\nif Block is executed, where value of \"a\" = 10.")

elif ( a == 20 ) :

	print("\nFirst elif Block is executed, where value of \"a\" = 20.")

elif ( a == 30 ) :

	print("\nSecond elif Block is executed, where value of \"a\" = 30.")

elif ( a == 40 ) :

	print("\nThrid elif Block is executed, where value of \"a\" = 40.")

else :

	print("\nSince all condition has failed. else block is executed, where value of \"a\" <  40.")

#Redeclaring Variable a = 30 to make elif block to be executed.

a = 30

print("\nWhen a = 30.")

if ( a == 10 ) :

	print("\nif Block is executed, where value of \"a\" = 10.")

elif ( a == 20 ) :

	print("\nFirst elif Block is executed, where value of \"a\" = 20.")

elif ( a == 30 ) :

	print("\nSecond elif Block is executed, where value of \"a\" = 30.")

elif ( a == 40 ) :

	print("\nThrid elif Block is executed, where value of \"a\" = 40.")

else :

	print("\nSince all condition has failed. else block is executed, where value of \"a\" <  40.")

#Redeclaring Variable a = 50 to make else block to be executed.

a = 50

print("\nWhen a = 50.")

if ( a == 10 ) :

	print("\nif Block is executed, where value of \"a\" = 10.")

elif ( a == 20 ) :

	print("\nFirst elif Block is executed, where value of \"a\" = 20.")

elif ( a == 30 ) :

	print("\nSecond elif Block is executed, where value of \"a\" = 30.")

elif ( a == 40 ) :

	print("\nThrid elif Block is executed, where value of \"a\" = 40.")

else :

	print("\nSince all condition has failed. else block is executed, where value of \"a\" > 40.")
