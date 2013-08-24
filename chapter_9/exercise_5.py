# The following function doesn't have a docstring or comments. Write enough
# of both to make it easy for another programmer to understand what the
# function does and how, and then compare your solution with those of at
# least two other people. How similar are they? Why do they differ?
# def mystery_function(values):
#     result = []
#     for sublist in values:
#         result.append([sublist[0]])
#         for i in sublist[1:]:
#             result[-1].insert(0, i)
#     return result

def mystery_function(values):
    """ (list) -> list

    Takes a list containing lists returns the outer list in the same
    order, but with the inner lists reversed.

    >>> mystery_function([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    >>> mystery_function([[48, 96], [128, 3]])
    [[96, 48], [3, 128]]
    """

    result = []
    for sublist in values:
        result.append([sublist[0]])
        for i in sublist[1:]:
            result[-1].insert(0, i)
    return result