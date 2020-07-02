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

#In this lets see about "for loop with else condition"

#else statement will be executed when the condition in ths for loop false.

#Note : when the loop is broken using break statement then else statement will not execute.

#synatx for "for loop with else" is

#for iterating_variable in sequence_variable :

#	statement(s)

#else :

#	statement(s)

#for loop with else program example without break

Name = "Maayon"

print()

for i in Name : # i is the iterating_variable and Name is the squence 

	print( i, end = '' )

else :

	print("\n\nfor loop has executed successfully...\n\nelse statement also executed successfully...")

#for loop with else program example with break

Name = "Maayon"

print()

for i in Name : # i is the iterating_variable and Name is the squence 

	print( i, end = '' )

	if( i == 'o' ) :

		break

else :

	print("\n\nfor loop has executed successfully by using break...\n\nelse statement also executed successfully...")

print("\n\nfor loop has executed successfully by using break...\n\nelse statement Not executed successfully...")

