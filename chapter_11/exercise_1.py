# Write a function called find_dups that takes a list of integers as its input
# argument and returns a set of those integers that occur two or more times
# in the list.

def find_dups(integers):
    """ (list) -> set

    Accepts a list of integers and returns a set of integers that appear in the
    list more than once.

    >>> find_dups([1, 4, 6, 8, 1])
    {1}
    >>> find_dups([7, 8, 9, 10, 7, 9])
    {7, 9}
    """
    found_numbers = set()
    duplicate_numbers = set()

    for i in integers:
        if i in found_numbers:
            duplicate_numbers.add(i)
        else:
            found_numbers.add(i)   

    return duplicate_numbers
