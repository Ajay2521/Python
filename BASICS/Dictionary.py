#In this lets see about "Dictionary datatype" concept in Python Programming.

#The Standard data types in Python Programming is of

#1) Numbers.

#2) String.

#3) List.

#4) Tuple.

#5) Dictionary

#Lets see about "Dictionary Datatype" in Python.

#Dictionary is an ordered set of a key-value pair of item.

#It is simialr to an associative array or hash table where each key stores a specific value.

#key is used to hold any primitive datatype whereas value is an arbitrary Python Object.

#The items stored in the dictionary are separated by using a comma ( , ) and tuple is enclosed within "Curly Braces { } ".

#More about Dictionary will be discussed later

#Here is program for "Dictionary Datatype"

a = {10 : 'int', 10.12 : 'float' , 'Maayon' : 'String' , 10 + 10j : 'Complex' }

print("\nThe Value of \"a\" is : " , a , "\nThe Datatype of variable \"a\" is : ", type(a) )

#keys() is a function which is used to print all keys present in the Dictionary.

print("\n" ,a.keys())

#values() is a function which is used to print all values of the keys which is present in the Dictionary.

print("\n" ,a.values())
