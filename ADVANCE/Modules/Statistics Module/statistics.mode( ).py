# Lets see about Statistics module in python

# statistics module provides the functions to mathematical statistics of numeric data.

# statistics.mode( ) = Used to return most commonly occured data in the list.

# Here is the example program for statistics.mode( )

import statistics

List = [ 1, 2, 2, 3, 3, 3, 4, 4, 5]

Mode = statistics.mode(List)

print('\nList value is :\n',List)

print('\nMost commonly occured data in the List is :',Mode)


