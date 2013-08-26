# This one is a fun challenge.
# Edsgar Dijkstra is known for his work on programming languages. He
# came up with a neat problem that he called the Dutch National Flag
# problem: given a list of strings, each of which is either 'red', 'green', or 'blue'
# (each is repeated several times in the list), rearrange the list so that the
# strings are in the order of the Dutch national flag: all the 'red' strings
# first, then all the 'green' strings, then all the 'blue' strings.
# Write a function called dutch_flag that takes a list and solves this problem.

def sort_flags(flag1, flag2):
    flag_values = {'red': 0, 'green': 1, 'blue': 2}

    if flag_values[flag1] == flag_values[flag2]:
        return 0
    elif flag_values[flag1] > flag_values[flag2]:
        return 1
    else:
        return -1

def dutch_flag(flags):
    flag_values = {'red': 0, 'green': 1, 'blue': 2}
    return sorted(flags, key=lambda x : flag_values[x])

print(dutch_flag(['red', 'blue','green', 'red']))

