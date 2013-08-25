# Write a function called dict_intersect that takes two dictionaries as arguments
# and returns a dictionary that contains only the key/value pairs found in
# both of the original dictionaries.

def dict_intersect(first, second):
    """ (dictionary, dictionary) -> dictionary

    Returns a dictionary containing only key/value pairs from both paramter
    dictionaries.

    >>> dict_intersect({'badger': 42, 'monkey': 25}, {'elephant': 10, 'badger': 42})
    {'badger': 42}
    """

    result_dictionary = {}

    for key, value in first.items():
        if key in second and second[key] == value:
            result_dictionary[key] = value

    return result_dictionary