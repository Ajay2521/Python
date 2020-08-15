# Lets see about "Collections"

# collection module is used to store a collection of data in a container.

# namedtuple() = used to return tuple object with names for each position in the tuple.

# Here is the program for namedtuple()

import collections

# declaring namedtuple()

data = collections.namedtuple('data',['Name','Age'])

# Adding values using object.

d = data('Ajay',19)

print('\nData in the typle is :\n')

print(d)

print('\nData acessing Name keyword is :',d.Name)

print('\nData acessing Age keyword is :',d.Age)




