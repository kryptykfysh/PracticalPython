# Create a file named exercise.py with this code inside it:
# def average(num1, num2):
# """ (number, number) -> number
# Return the average of num1 and num2.
# >>> average(10,20)
# 15.0
# >>> average(2.5, 3.0)
# 2.75
# """
# return num1 + num2 / 2

def average(num1, num2):
    """ (number, number) -> number
    
    Return the average of num1 and num2.
    
    >>> average(10,20)
    15.0
    >>> average(2.5, 3.0)
    2.75
    """
    return num1 + num2 / 2
# a. Run exercise.py. Import doctest and run doctest.testmod().

# b. Both of the tests in the average function’s docstring fail. Fix the code
# and rerun the tests. Repeat this procedure until the tests pass.

def average(num1, num2):
    """ (number, number) -> number
    
    Return the average of num1 and num2.
    
    >>> average(10,20)
    15.0
    >>> average(2.5, 3.0)
    2.75
    """
    return (num1 + num2) / 2