# Lets see about "Collections"

# collection module is used to store a collection of data in a container.

# Counter() = is a subclass of dictionary object which helps to count hashable objects.

import collections

list1 = ['blue', 'red', 'blue', 'yellow', 'blue', 'pink', 'red', 'orange', 'pink', 'blue', 'red']

Count = collections.Counter(list1)

print('\nThe First list value is :\n')

print(list1)

print()

print(Count)

list2 = ['red', 'blue', 'green' ,'orange']

print('\nThe Second list value is :\n')

print(list2)

for List in list2:

    print(List, Count[List])
    
     

