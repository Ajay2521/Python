# Lets see about random module.

# random module functions depend on a pseudo-random number generator function random(), which generates the float number between 0.0 and 1.0.

# random.randrange(start, end, skip ) = used to return a random  a number within the range specified in its argument.

# start = Start value.

# end = End value.

# skip = Skip value.

# Here is the example program for random.randrange( )

import random

print('\nRandom number generated using randrange( 10, 1000 , 20 ) is :',random.randrange( 10, 1000 , 20 ))

print( ) # prints empty line for readyability


