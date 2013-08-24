# Using the string method find, write an expression that produces the index
# of the first occurrence of o in 'tomato'.

test_string = 'tomato'
test_case = 'o'

print("The first occurrence of '{}' in '{}' is at index {}.".format(test_case, test_string, test_string.index(test_case)))