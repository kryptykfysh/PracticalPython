# You are given two lists, rat_1 and rat_2, that contain the daily weights of
# two rats over a period of ten days. Write statements to do the following:
import random

def gen_random_list(length):
    return_list = []
    for i in range(length):
        return_list.append(random.uniform(0, 10))
    return return_list

rat1 = gen_random_list(10)
print(rat1)
rat2 = gen_random_list(10)
print(rat2)

# a. If the weight of rat 1 is greater than that of rat 2 on day 1, print "Rat
# 1 weighed more than rat 2 on day 1."; otherwise, print "Rat 1 weighed less than rat
# 2 on day 1."

print('Rat 1 weighed {} than rat 2 on day 1.'.format('more' if rat1[0] > rat2[0] else 'less'))

# b. If rat 1 weighed more than rat 2 on day 1 and if rat 1 weighs more
# than rat 2 on the last day, print "Rat 1 remained heavier than Rat 2."; other-
# wise, print "Rat 2 became heavier than Rat 1."
if rat1[0] > rat2[0]:
    if rat1[-1] > rat2[-1]:
        print("Rat 1 remained heavier than Rat 2.")
    else:
        print("Rat 2 became heavier than Rat 1.")

# c. If your solution to the previous question used nested if statements,
# then do it without nesting, or vice versa.

if rat1[0] > rat2[0] and rat1[-1] > rat2[-1]:
    print("Rat 1 remained heavier than Rat 2.")
elif rat1[0] > rat2[0] and not rat1[-1] > rat2[-1]:
    print("Rat 2 became heavier than Rat 1.")