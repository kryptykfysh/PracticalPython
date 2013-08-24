# The variable fruit refers to 'pineapple'. For the following function calls, in
# what order are the subexpressions evaluated?

# a. fruit.find('p', fruit.count('p'))
# count -> find

# b. fruit.count(fruit.upper().swapcase())
# upper -> swapcase -> count

# c. fruit.replace(fruit.swapcase(), fruit.lower())
# swapcase -> lower -> replace