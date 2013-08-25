# A sparse vector is a vector whose entries are almost all zero, like [1, 0, 0, 0,
# 0, 0, 3, 0, 0, 0]. Storing all those zeros in a list wastes memory, so program-
# mers often use dictionaries instead to keep track of just the nonzero
# entries. For example, the vector shown earlier would be represented as
# {0:1, 6:3}, because the vector it is meant to represent has the value 1 at
# index 0 and the value 3 at index 6.

# a. The sum of two vectors is just the element-wise sum of their elements.
# For example, the sum of [1, 2, 3] and [4, 5, 6] is [5, 7, 9]. Write a function
# called sparse_add that takes two sparse vectors stored as dictionaries
# and returns a new dictionary representing their sum.
def sparse_add(first, second):
    """ (dictionary, dictionary) -> dictionary

    Sums two sparse vector dictionaries and returns the result as a sparse
    vector dictionary.

    >>> sparse_add({0:1, 4:2, 6:2}, {2:1, 4:1, 5:3})
    {0: 1, 2: 1, 4: 3, 5: 3, 6: 2}
    """

    result = first
    for key, value in second.items():
        result[key] = result.get(key, 0) + value
    return result

# b. The dot product of two vectors is the sum of the products of corre-
# sponding elements. For example, the dot product of [1, 2, 3] and [4, 5,
# 6] is 4+10+18, or 32. Write another function called sparse_dot that calcu-
# lates the dot product of two sparse vectors.

def sparse_dot(first, second):
    total = 0

    for key, value in first.values():
        total += value * second.get(key, 0)

    return result

# c. Your boss has asked you to write a function called sparse_len that will
# return the length of a sparse vector (just as Python's len returns the
# length of a list). What do you need to ask her before you can start
# writing it?

# WTF is the length of a vector?
# More seriously, what indices refer to what axes attributes?