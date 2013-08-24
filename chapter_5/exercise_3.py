##Variables full and empty refer to Boolean values. Write an expression that
##produces True iff at most one of the variables is True.

def xor(arg1, arg2):
    """ (bool, bool) -> bool

    Produces True iff only one of the parameters is True

    >>> xor(True, True)
    False
    >>> xor(False, True)
    True
    >>> xor(False, False)
    False
    """
    return arg1 != arg2

def _test():
    import doctest
    doctest.testmod()



