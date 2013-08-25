# The keys in a dictionary are guaranteed to be unique, but the values are
# not. Write a function called count_values that takes a single dictionary as
# an argument and returns the number of distinct values it contains. Given
# the input {'red': 1, 'green': 1, 'blue': 2}, for example, it should return 2.

def count_values(dictionary):
    """ (dictionary) -> integer

    Returns the number of unique values in a dictionary.

    >>> count_values({'Fred': 42, 'Brenda': 96, 'George': 42})
    2
    """

    unique_values = set()

    for key, value in dictionary:
        unique_values.add(value)

    return len(unique_values)