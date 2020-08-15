# Lets see about random module.

# random module functions depend on a pseudo-random number generator function random(), which generates the float number between 0.0 and 1.0.

# random.shuffle( ) = used to randomly reorders the elements in the list.

# Here is the example program for random.shuffle( )

import random

List = [0, 10, 5, 20, 15, 30, 25]

print('\nOriginal List is :\n')

print(List)

random.shuffle(List)

print('\nRandomly reorded list using shuffle( ) is :\n')

print(List)

print( ) # prints empty line for readyability


