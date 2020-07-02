#In this program lets see about "Loop" concept in Python.

#Loops are the once which is used to repeat certain code for certain number of times.

#Thus loops will be executed for number of times or till the condition gets fails.

#ADVANTAGES of LOOPS:

#1) Loop is used for code re-usability.

#2) By using loop writing the code again and again can be avoided.

#3) By using loop traversing the element in data structures like array or linked list can be achived.

#There are 3 types of loop they are :

#1) for loop

#2) while loop

#3) do - while loop

#In this lets see about "Nested for loop"

#Any number of for loop can be nested inside a for loop.

#The inner loop is executed "n" number of times for every iteration of the outer loop.

#synatx for "Nested for loop" is

#for iterating_variable_1 in sequence_variable : #outer loop 

#	statement(s)

#	for iterating_variable_2 in sequence_variable : #inner loop 

#		statement(s)

#Nested for loop program

print()

for i in range(1,4) : # i is the iterating_variable and Range is the squence 

	print(i, " Number of time the Outer for loop is executed.\n")

	for x in range(1,6) : # i is the iterating_variable and Range is the squence 

		print(x, " Number of time the Inner for loop is executed.\n")

#Thus this program will be executed for the time of value present in the string



