# The variable kingdoms refers to the list ['Bacteria', 'Protozoa', 'Chromista', 'Plantae',
# 'Fungi', 'Animalia']. Using kingdoms and either slicing or indexing with positive
# indices, write expressions that produce the following:
kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']

# a. The first item of kingdoms
print(kingdoms[0])
print(kingdoms[:1])

# b. The last item of kingdoms
print(kingdoms[len(kingdoms) - 1:])
print(kingdoms[len(kingdoms) - 1])

# c. The list ['Bacteria', 'Protozoa', 'Chromista']
print(kingdoms[0:3])

# d. The list ['Chromista', 'Plantae', 'Fungi']
print(kingdoms[2:5])

# e. The list ['Fungi', 'Animalia']
print(kingdoms[4:6])
print(kingdoms[len(kingdoms) - 2:len(kingdoms)])

# f. The empty list
print([])
