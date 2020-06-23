#In this program lets see about "Decision Making Statements " in Python Programming.

#Descion making statement is used to check for the condition and makes a flow in the program.

#There are 4 types of Decision Making Statement . They are :

#1) if

#2) if else

#3) if elif

#4) Nested if

#In this program lets see about "Nested if else Statement" in Python

#It is legal to declare a if statement inside another if statement in python program.

#If the outer if statement passes the condition, then the compiler will check for inner condition.

#If the outer if statement fails the condition, then it will not move inside to check inner condition.

#It is similar for all Nested if statement, Nested if else statement, Nested if elif statement.

#Syntax for "Nested if else statement" is

#if( Outer Conditional Expression ) :

#	Statement 1

#	Statement 2

#	Statement N

#	if( Inner if Conditional Expression ) :

#		Statement 1

#		Statement 2

#		Statement N

#	else : #Inner else statement of outer if statement

#		Statement 1

#		Statement 2

#		Statement N

#else : #outer else statement

#	Statement 1

#	Statement 2

#	Statement N

#	if( Inner outter Conditional Expression ) :

#		Statement 1

#		Statement 2

#		Statement N

#	else : #Inner else statement of outer else statement

#		Statement 1

#		Statement 2

#		Statement N

#Note : Since Python doesn't denote curly braces . Therefore "indentation" will play an imporatant role is makeing a block of code.

#Thus general four space or tab press is used to mention the indention in the program.

#Program for "Nested if else statement"

a = 10

b = 10

if ( a > 10 ) :

	print("\nOuter if statement is executed, where value of \"a\" is Lesser than 10.")
	
	if ( b > 10  ) :

		print("\nInner if statement of Outer if statement is executed, where value of \"b\" is Lesser than 10.")

	else :

		print("\nInner else statement of Outer if statement is executed, where value of \"b\" is Not Lesser than 10.")

else :

	print("\nOuter else statement is executed, where value of \"a\" is Not Lesser than 10.")
	
	if ( b > 10  ) :

		print("\nInner else statement of Outer else statement is executed, where value of \"b\" is Lesser than 10.")

	else :

		print("\nInner else statement of Outer else statement is executed, where value of \"b\" is Not Lesser than 10.")
