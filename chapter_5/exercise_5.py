##In Section 3.1, Functions That Python Provides, on page 31, we saw the
##built-in function abs. The variable x refers to a number. Write an expression
##that evaluates to True if x and its absolute value are equal and evaluates
##to False otherwise. Assign the resulting value to a variable named result.

def abs_check(num):
    """ (number) -> bool

    Checks a number is equal to its absolute value

    >>> abs_check(-4)
    False
    >>> abs_check(4)
    True
    >>> abs_check(3.2344)
    True
    """
    return num == abs(num)
