# Lets see about "Collections"

# collection module is used to store a collection of data in a container.

# OrderedDict() = used to return dictionary object with names for each position in the dictionary.

# where object where keys maintain the order of insertion.

# NOTE : insert key again, the previous value will be overwritten for that key.

# Here is the program for OrderedDict()

import collections

d = collections.OrderedDict()

d['A'] = 1

d['B'] = 2

d['C'] = 3

d['D'] = 4

d['E'] = 5

print('\nData in "d" is :\n')

print(d)

print('\nkeys in "d" is :\n')

for key in d:

    print(key)

print('\nValues in "d" is :\n')

for key in d:

    print(d[key])
    
print('\nKeys and values in "d" is :\n')

for key,value in d.items():

    print(key,value)
 