# Using string methods, write expressions that produce the following:

# a. A copy of 'boolean' capitalized
string = 'boolean'
print("'{}' is capitalized to '{}'".format(string, string.capitalize()))

# b. The first occurrence of '2' in 'C02 H20'
string = 'C02 H20'
search_string = '2'
index_of_first_occurrence = string.find(search_string)
print("The first occurence of '{}' in '{}' is at index {}.".format(search_string, string, index_of_first_occurrence))

# c. The second occurrence of "2" in 'C02 H20'
index_of_second_occurrence = string.find(search_string, index_of_first_occurrence + 1)
print("The second occurence of '{}' in '{}' is at index {}.".format(search_string, string, index_of_second_occurrence))

# d. True if and only if 'Boolean' begins with a lowercase
string = 'Boolean'
starts_lowercase = string.startswith(string.lower(),0)
print("If string == '{}', string.startswith(string.lower(),0)' evaluates to {}.".format(string, starts_lowercase))

# e. A copy of "MoNDaY" converted to lowercase and then capitalized
string = 'MoNDay'
print("'{}' formats to '{}'".format(string, string.lower().capitalize()))

# f. A copy of " Monday" with the leading whitespace removed
string = ' Monday'
print("'{}' with the leading whitespace removed is '{}'".format(string, string.lstrip()))