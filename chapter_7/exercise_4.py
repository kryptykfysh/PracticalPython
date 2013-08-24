# Using the string method find, write a single expression that produces the
# index of the second occurrence of o in 'tomato'. Hint: Call find twice.

test_string = 'tomato'
test_case = 'o'
index_of_second_occurence = test_string.find(test_case, test_string.find(test_case) + 1)

print("The second occurrence of '{}' in '{}' is at index {}.".format(test_case, test_string, index_of_second_occurence))