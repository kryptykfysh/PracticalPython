# Using nested for loops, print a right triangle of the character T on the
# screen where the triangle is one character wide at its narrowest point and
# seven characters wide at its widest point:
# T
# TT
# TTT
# TTTT
# TTTTT
# TTTTTT
# TTTTTTT

for i in range(1, 8):
    print('T' * i)