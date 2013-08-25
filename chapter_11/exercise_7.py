# A balanced color is one whose red, green, and blue values add up to 1.0.
# Write a function called is_balanced that takes a dictionary whose keys are
# 'R', 'G', and 'B' as input and returns True if they represent a balanced color.

def is_balanced(colour_dictionary):
    if sum(colour_dictionary.values()) == 1.0:
        return True
    else:
        return False