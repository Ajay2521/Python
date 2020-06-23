#In this program lets see about "Decision Making Statements " in Python Programming.

#Descion making statement is used to check for the condition and makes a flow in the program.

#There are 4 types of Decision Making Statement . They are :

#1) if

#2) if else

#3) if elif

#4) Nested if

#In this program lets see about "Nested if elif Statement" in Python

#It is legal to declare a if statement inside another if statement in python program.

#If the outer if statement passes the condition, then the compiler will check for inner condition.

#If the outer if statement fails the condition, then it will not move inside to check inner condition.

#It is similar for all Nested if statement, Nested if else statement, Nested if elif statement.

#Syntax for "Nested if elif statement" is

#if( Outer Conditional Expression ) :

#	Statement 1

#	Statement 2

#	Statement N

#	if( Inner if Conditional Expression ) :

#		Statement 1

#		Statement 2

#		Statement N

#	elif( Inner elif Conditional Expression 1 ) :

#		Statement 1

#		Statement 2

#		Statement N

#	elif( Inner elif Conditional Expression 2 ) :

#		Statement 1

#		Statement 2

#		Statement N

#	elif( Inner elif Conditional Expression N ) :

#		Statement 1

#		Statement 2

#		Statement N

#	else : #Inner else statement of outer if statement

#		Statement 1

#		Statement 2

#		Statement N

#elif( Outer elif Conditional Expression ) :

#	Statement 1

#	Statement 2

#	Statement N

#	if( Inner if Conditional Expression ) :

#		Statement 1

#		Statement 2

#		Statement N

#	elif( Inner elif Conditional Expression 1 ) :

#		Statement 1

#		Statement 2

#		Statement N

#	elif( Inner elif Conditional Expression 2 ) :

#		Statement 1

#		Statement 2

#		Statement N

#	elif( Inner elif Conditional Expression N ) :

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


#	elif( Inner elif Conditional Expression 1 ) :

#		Statement 1

#		Statement 2

#		Statement N

#	elif( Inner elif Conditional Expression 2 ) :

#		Statement 1

#		Statement 2

#		Statement N

#	elif( Inner elif Conditional Expression N ) :

#		Statement 1

#		Statement 2

#		Statement N

#	else : #Inner else statement of outer else statement

#		Statement 1

#		Statement 2

#		Statement N

#Program for "Nested if else statement"

a = 10

b = 15

if ( a > 10 ) :

	print("\nOuter if statement is executed, where value of \"a\" > 10.")
	
	if ( b == 1  ) :

		print("\nInner if statement of Outer if statement is executed, where value of \"b\" = 1.")

	elif ( b == 5  ) :

		print("\nFirst Inner elif statement of Outer if statement is executed, where value of \"b\" = 5.")
	
	elif ( b == 10  ) :

		print("\nSeconf Inner elif statement of Outer if statement is executed, where value of \"b\" = 10.")

	elif ( b == 15  ) :

		print("\nThird Inner elif statement of Outer if statement is executed, where value of \"b\" = 15.")
	
	else :

		print("\nInner else statement of Outer if statement is executed, where value of \"b\" < 15.")

elif ( a == 10 ) :

	print("\nOuter elif statement is executed, where value of \"a\" = 10.")
	
	if ( b == 1  ) :

		print("\nInner if statement of Outer elif statement is executed, where value of \"b\" = 1.")

	elif ( b == 5  ) :

		print("\nFirst Inner elif statement of Outer elif statement is executed, where value of \"b\" = 5.")
	
	elif ( b == 10  ) :

		print("\nSeconf Inner elif statement of Outer elif statement is executed, where value of \"b\" = 10.")

	elif ( b == 15  ) :

		print("\nThird Inner elif statement of Outer elif statement is executed, where value of \"b\" = 15.")
	
	else :

		print("\nInner else statement of Outer elif statement is executed, where value of \"b\" < 15.")
		
else :

	print("\nOuter else statement is executed, where value of \"a\" < 10.")

	if ( b == 1  ) :

		print("\nInner if statement of Outer else statement is executed, where value of \"b\" = 1.")

	elif ( b == 5  ) :

		print("\nFirst Inner elif statement of Outer else statement is executed, where value of \"b\" = 5.")
	
	elif ( b == 10  ) :

		print("\nSeconf Inner elif statement of Outer else statement is executed, where value of \"b\" = 10.")

	elif ( b == 15  ) :

		print("\nThird Inner elif statement of Outer else statement is executed, where value of \"b\" = 15.")
	
	else :

		print("\nInner else statement of Outer else statement is executed, where value of \"b\" < 15.")
