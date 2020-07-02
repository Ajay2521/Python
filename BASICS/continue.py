#In this lets see about the "control statements" in Python Program.

#Control statement is used to make a control flow in the program.

#The different type of control statement in python is 

#1) break

#2) continue

#3) pass

#Lets now see about "continue" control statement in python

#continue is control statement which is used to terminate only the particualr iteration when condition becomes true.

#Once the continue is executed then it will terminate only the particualr iteration in the loop and executed the remaining code inside the loop.

#syntax of the continue is

#condition

#continue

#Here is program for continue control statement. 

i = 0

print()

while (i < 5 ) :

	i = i + 1

	if( i == 3 ) :

		continue

	print(i)

print("\nContinue control statement has been executed. Thus when \"i\" becomes 3 that particualr iteration is terminate and remaining iteration has been executed.")
