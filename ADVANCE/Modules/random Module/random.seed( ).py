# Lets see about random module.

# random module functions depend on a pseudo-random number generator function random(), which generates the float number between 0.0 and 1.0.

# random.seed( ) = used to return a random float number between 0.0 and 1.0 with the seed/start argument.

# Here is the example program for random.seed( )

import random

random.seed(5)

print('\nRandom number generated using seed( ) is :',random.random())

print( ) # prints empty line for readyability


