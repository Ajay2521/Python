# Lets see about Statistics module in python

# statistics module provides the functions to mathematical statistics of numeric data.

# statistics.median_low( ) = Used to return a low middle value from the list.

# NOTE: In case there are two mean then it is used to print the low median value.

# Here is the example program for statistics.median_low( )

import statistics

List = [ 1, 3, 6, 5, 10, 15, 20, 30, 25, 32]

LowMedian = statistics.median_low(List)

print('\nList value is :\n',List)

print('\nLow Median value of the List is :',LowMedian)


