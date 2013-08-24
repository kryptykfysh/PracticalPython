# a. Create a nested list where each element of the outer list contains the
# atomic number and atomic weight for an alkaline earth metal. The
# values are beryllium (4 and 9.012), magnesium (12 and 24.305), cal-
# cium (20 and 40.078), strontium (38 and 87.62), barium (56 and
# 137.327), and radium (88 and 226). Assign the list to the variable
# alkaline_earth_metals.
alkaline_earth_metals = [[4, 9.012], [12, 24.305], [20, 40.078], [38, 87.62], [56, 137.327], [88, 226]]
print(alkaline_earth_metals)

# b. Write a for loop to print all the values in alkaline_earth_metals, with the
# atomic number and atomic weight for each alkaline earth metal on a
# different line.
for metal in alkaline_earth_metals:
    print("Atomic Number: {}, Atomic Weight: {}".format(metal[0], metal[1]))

# c. Write a for loop to create a new list called number_and_weight that contains
# the elements of alkaline_earth_metals in the same order but not nested.
number_and_weight = []

for metal in alkaline_earth_metals:
    number_and_weight.extend(metal)

print(number_and_weight)