# a. Write a loop (including initialization) to find both the minimum value
# in a list and that value's index in one pass through the list.

list = [3, 1, 5, 7, 2, -5, 2]

smallest = (list[0], 0)

for i in range(len(list)):
    if list[i] < smallest[0]:
        smallest = (list[i], i)

# b. Write a function named min_index that takes one parameter (a list) and
# returns a tuple containing the minimum value in the list and that
# value's index in the list.
def min_index(list):
    smallest = (list[0], 0)

    for i in range(len(list)):
        if list[i] < smallest[0]:
            smallest = (list[i], i)

    return smallest

# c. You might also want to find the maximum value and its index. Write
# a function named min_or_max_index that has two parameters: a list and
# a bool. If the Boolean parameter refers to True, the function returns a
# tuple containing the minimum and its index; and if it refers to False,
# it returns a tuple containing the maximum and its index.
def min_or_max_index(list, bool):
    result = (list[0], 0)

    for i in range(len(list)):
        if bool == True and list[i] < result[0]:
            result = (list[i], i)
        elif bool == False and list[i] > result[0]:
            result = (list[i], i)

    return result