#In this lets see about the "control statements" in Python Program.

#Control statement is used to make a control flow in the program.

#The different type of control statement in python is 

#1) break

#2) continue

#3) pass

#Lets now see about "pass" control statement in python

#pass keyword is used to execute nothing which means, when we don't want to execute code, the pass can be used to execute empty. 

#It just makes the control to pass by without executing any code. 

#If we want to bypass any code pass statement can be used. loop and executed the remaining code inside the loop.

#The difference between the comments and pass is that, comments are entirely ignored by the Python interpreter, where the pass statement is not ignored.

#syntax of the pass is

#condition

#pass

#Here is program for pass control statement. 

i = 0

print()

while (i < 5 ) :

	i = i + 1

	if( i == 3 ) :

		pass

		print("\nThis is pass block",i,"\n")  

	print(i)
