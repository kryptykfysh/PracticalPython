# Using nested for loops, print the triangle described in the previous question
# with its hypotenuse on the left side:
#       T
#      TT
#     TTT
#    TTTT
#   TTTTT
#  TTTTTT
# TTTTTTT

max = 7
for i in range(1, max + 1):
    print(('T' * i).rjust(max))