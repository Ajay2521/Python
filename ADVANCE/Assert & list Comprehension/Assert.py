# In this lets see about the assert in the python.

# Assert is a kwyword used to define a debugging tool which is used to test a condition.

# If the condition is true then it moves to the next line.

# If the condition becomes false then it will be resulting in an AssertionError.

# Syntac for assert is:

# assert condition,error_message    

# condition = Condition to be checked.

# error_message = error message to be displayed , which is optional.

# Here is the example for assert

a = int(input('\nEnter value of "a" : '))

b = int(input('\nEnter value of "b" : '))

assert b != 0,'Divisor 0 error'

print('\na / b is : ',a/b)
