#In this program lets see about "Decision Making Statements " in Python Programming.

#Descion making statement is used to check for the condition and makes a flow in the program.

#There are 4 types of Decision Making Statement . They are :

#1) if

#2) if else

#3) if elif

#4) Nested if

#In this program lets see about "Nested if Statement" in Python

#It is legal to declare a if statement inside another if statement in python program.

#If the outer if statement passes the condition, then the compiler will check for inner condition.

#If the outer if statement fails the condition, then it will not move inside to check inner condition.

#It is similar for all Nested if statement, Nested if else statement, Nested if elif statement.

#Syntax for "Nested if statement" is

#if( Outer Conditional Expression ) :

#	Statement 1

#	Statement 2

#	Statement N

#	if( Inner Conditional Expression ) :

#		Statement 1

#		Statement 2

#		Statement N

#Note : Since Python doesn't denote curly braces . Therefore "indentation" will play an imporatant role is makeing a block of code.

#Thus general four space or tab press is used to mention the indention in the program.

#Program for if statement

a = 10

b = 15

if ( a == 10  ) :

	print("\nOuter If statement is executed, where value of \"a\" = 10.")
	
	if ( b == 5  ) :

		print("\nFirst Inner If statement is executed, where value of \"b\" = 5.")

	if ( b == 10  ) :

		print("\nSecond Inner If statement is executed, where value of \"b\" = 10.")

	if ( b == 15  ) :

		print("\nThird Inner If statement is executed, where value of \"b\" = 15.")

