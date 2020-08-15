# Lets see about "Collections"

# collection module is used to store a collection of data in a container.

# OrderedDict() = used to return dictionary object with names for each position in the dictionary.

# Here is the program for defaultdict()

import collections

d = collections.defaultdict(int)

d['A'] = 1

d['B'] = 2

d['C'] = 3

d['D'] = 4

d['E'] = 5

print('\nData in "d" is :\n')

print(d)

print('\nKeys and values in "d" is :\n')

for key,value in d.items():

    print(key,value)
