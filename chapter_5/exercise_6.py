##Write a function named different that has two parameters, a and b. The
##function should return True if a and b refer to different values and should
##return False otherwise.

def different(a, b):
    """ (number, number) -> bool

    Returns True if parameters are different values.

    >>> different(4, 3)
    True
    >>> different(3, 3)
    False
    """
    
    return a != b
