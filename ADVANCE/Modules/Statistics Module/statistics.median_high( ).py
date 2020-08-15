# Lets see about Statistics module in python

# statistics module provides the functions to mathematical statistics of numeric data.

# statistics.median_high( ) = Used to return a high middle value from the list.

# NOTE: In case there are two mean then it is used to print the high median value.

# Here is the example program for statistics.median_high( )

import statistics

List = [ 1, 3, 6, 5, 10, 15, 20, 30, 25, 32]

HighMedian = statistics.median_high(List)

print('\nList value is :\n',List)

print('\nHigh Median value of the List is :',HighMedian)


