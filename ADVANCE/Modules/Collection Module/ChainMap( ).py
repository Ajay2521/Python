# Lets see about "Collections"

# collection module is used to store a collection of data in a container.

# ChainMap() = used to groups multiple dictionary together to create a single list.

# Here is the program for ChainMap()

import collections

list1 = {'Name':'Ajay','Age': 19}

list2 = {'Age': 19, 'RollNo': 101010 , 'MobileNo' : 1010101010}

List = collections.ChainMap(list1, list2)

print('\nList 1 data is :\n')

print(list1)

print('\nList 2 data is :\n')

print(list2)

print('\nList data by combining using ChainMap() is :\n')

print(List)
