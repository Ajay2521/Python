#In this lets see about "User given input data" in Python.

#Value of the variable can be assigned both statically or dynamically.

#Static is the way in which we can able to assign the value to a variable while initialize in the programming source code itself.

#Dynamic is the way in which user can able to assign the value to a variable while executing the program code . That is run time of the program.

# input() is function used to get a dynamic data from the user in run time of the program.

#Note : By defalut the User input data will be of string datatype.

#Here is the example for "user input"

Name = input ( "\nEnter Your Name : " ) #gets defalut datatype value as string.

Age = int ( input ( "\nEnter Your Age : " ) ) #gets value as an integer datatype.

print( "\nUser Name is : " , Name )

print( "\nUser Age is : " , Age )

print( "\nDatatype of Name is : " , type ( Name ) )

print( "\nDatatype of Age is : " , type ( Age ) )