# a. Assign a list that contains the atomic numbers of the six alkaline
# earth metals-beryllium (4), magnesium (12), calcium (20), strontium
# (38), barium (56), and radium (88)-to a variable called alkaline_earth_met-
# als.
alkaline_earth_metals = [4, 12, 20, 38, 56, 88]
print(alkaline_earth_metals)

# b. Which index contains radium's atomic number? Write the answer in
# two ways, one using a positive index and one using a negative index.
print("Radium's atomic number: {}.".format(alkaline_earth_metals[5]))
print("Radium's atomic number: {}.".format(alkaline_earth_metals[-1]))

# c. Which function tells you how many items there are in alkaline_earth_met-
# als?
print("There are {} elements in the list.".format(len(alkaline_earth_metals)))

# d. Write code that returns the highest atomic number in alkaline_earth_met-
# als. (Hint: Use one of the functions from Table 9, List Functions, on
# page 139.)
print("The highest atomic number in the list is {}.".format(max(alkaline_earth_metals)))