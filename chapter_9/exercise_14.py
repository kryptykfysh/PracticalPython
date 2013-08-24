# Redo the previous two questions using while loops instead of for loops.

max = 7
count = 0

while count < max:
    count += 1
    print('T' * count)

count = 0

while count < max:
    count += 1
    print(('T' * count).rjust(max))