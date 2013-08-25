# Write a function called count_duplicates that takes a dictionary as an argu-
# ment and returns the number of values that appear two or more times.

def count_duplicates(dictionary):
    """ (dictionary) -> integer

    Passed a dictionary parameter, return the number of values that occur twice or more.

    """

    found_values = set()
    duplicate_values = set()

    for value in dictionary.values():
        if value in found_values:
            duplicate_values.add(value)
        else:
            found_values.add(value)

    return len(duplicate_values)