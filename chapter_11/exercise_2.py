# Python’s set objects have a method called pop that removes and returns
# an arbitrary element from the set. If the set gerbils contains five cuddly
# little animals, for example, calling gerbils.pop() five times will return those
# animals one by one, leaving the set empty at the end. Use this to write a
# function called mating_pairs that takes two equal-sized sets called males and
# females as input and returns a set of pairs; each pair must be a tuple
# containing one male and one female. (The elements of males and females
# may be strings containing gerbil names or gerbil ID numbers—your
# function must work with both.)

def mating_pairs(males, females):
    """ (set, set) -> set

    Takes two sets of equal length and returns a set of unique tuples 
    each containing an element from each of the two argument sets.

    """

    mated_pairs = set()

    while len(males) > 0:
        mated_pairs.add((males.pop(), females.pop()))

    return mated_pairs