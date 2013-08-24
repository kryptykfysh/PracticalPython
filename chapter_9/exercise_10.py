# Sum numbers in the range 2 to 22 using a loop to find the total, and then
# calculate the average.

numbers = list(range(2,23))
total = 0

for num in numbers:
    total += num

print("Total: {}. Average: {}".format(total, total / len(numbers)))