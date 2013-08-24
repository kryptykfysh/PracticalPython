# The variables rat_1_weight and rat_2_weight store the weights of two rats at
# the beginning of an experiment. The variables rat_1_rate and rat_2_rate are
# the rate that the rats' weights are expected to increase each week (for
# example, 4 percent per week).
rat_1_weight = 10.0
rat_2_weight = 10.0
rat_1_rate = 1.04
rat_2_rate = 1.03

# a. Using a while loop, calculate how many weeks it would take for the
# weight of the first rat to become 25 percent heavier than it was origi-
# nally.
rat_1_current_weight = rat_1_weight
week = 0

while rat_1_current_weight <= rat_1_weight * 1.25:
    week += 1
    rat_1_current_weight *= rat_1_rate
    print("In week {}, rat1 increased to weight {}, from it's starting weight of {}".format(week, rat_1_current_weight, rat_1_weight))

print("It took {} weeks for rat1 to go from weight {} to {}".format(week, rat_1_weight, rat_1_current_weight))

# b. Assume that the two rats have the same initial weight, but rat 1 is
# expected to gain weight at a faster rate than rat 2. Using a while loop,
# calculate how many weeks it would take for rat 1 to be 10 percent
# heavier than rat 2.
rat_1_current_weight = rat_1_weight
rat_2_current_weight = rat_2_weight
week = 0

while rat_1_current_weight < rat_2_current_weight * 1.1:
    week += 1
    rat_1_current_weight *= rat_1_rate
    rat_2_current_weight *= rat_2_rate
    print("In week {}, rat1 weighed {}, compared with rat2's {}.".format(week, rat_1_current_weight, rat_2_current_weight)) 
    print("\tA difference of {}%.".format((100 * rat_1_current_weight / rat_2_current_weight) - 100))