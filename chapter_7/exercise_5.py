# Using your expression from the previous question, find the second o in
# 'avocado'. If you don't get the result you expect, revise the expression and
# try again.

test_string = 'avocado'
test_case = 'o'
index_of_second_occurence = test_string.find(test_case, test_string.find(test_case) + 1)

print("The second occurrence of '{}' in '{}' is at index {}.".format(test_case, test_string, index_of_second_occurence))