#In this lets see about the "control statements" in Python Program.

#Control statement is used to make a control flow in the program.

#The different type of control statement in python is 

#1) break

#2) continue

#3) pass

#Lets now see about "break" control statement in python

#break is control statement which is used to terminate the loop when condition becomes true.

#Once the break is executed then it will terminate the loop completely and it comes out of the loop and executed the remaining code which is next after the loop statement.

#syntax of the break is

#condition

#break

#Here is program for break control statement. 

i = 1

print()

while (i <= 10 ) :

	print(i)

	i = i + 1

	if( i == 6 ) :

		print("\nBreak control statement has been executed. Thus loop has terminaated when \"i\" becomes 6.")

		break

print("\nBreak statement has been executed successfully...")