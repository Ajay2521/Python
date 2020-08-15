# Lets see about Statistics module in python

# statistics module provides the functions to mathematical statistics of numeric data.

# statistics.stdev( ) = Used to calculate the standard deviation of a given number.

# Here is the example program for statistics.stdev( )

import statistics

List = [ 1, 2, 2, 3, 3, 3, 4, 4, 5]

std = statistics.stdev(List)

print('\nList value is :\n',List)

print('\nStandard deviation of the List is :',std)


