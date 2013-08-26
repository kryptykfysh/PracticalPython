# A DNA sequence is a string made up of the letters A, T, G, and C. To find
# the complement of a DNA sequence, As are replaced by Ts, Ts by As, Gs
# by Cs, and Cs by Gs. For example, the complement of AATTGCCGT is
# TTAACGGCA.

# a. Write an outline in English of the algorithm you would use to find the
# complement.

# Step through each character of a DNA sequence and replace it with it's 
# complement, looked up in a dictionary.

# b. Review your algorithm. Will any characters be changed to their com-
# plement and then changed back to their original value? If so, rewrite
# your outline. Hint: Convert one character at a time, rather than all of
# the As, Ts, Gs, or Cs at once.
# c. Using the algorithm that you have developed, write a function named
# complement that takes a DNA sequence (a str) and returns the comple-
# ment of it.

def complement(dna_sequence):
    """ (string) -> string

    Accept a DNA string parameter and return its complement.

    >>> complement('AATTGCCGT')
    'TTAACGGCA'
    """

    dna_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    result = ''

    for char in dna_sequence:
        result += dna_dict[char]

    return result