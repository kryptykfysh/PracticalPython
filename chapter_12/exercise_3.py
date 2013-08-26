# In The Readline Technique, on page 185, you learned how to read some
# files from the Time Series Data Library. In particular, you learned about
# the Hopedale data set, which describes the number of colored fox fur pelts
# produced from 1834 to 1842. This file contains one value per year per
# line.

# a. Write an outline in English of the algorithm you would use to read
# the values from this data set to compute the average number of pelts
# produced per year.

# Open the file.
# Skip through the header lines.
# Keep a running total on the number of pelts and lines read.
# Divide the total by the lines read and return the result.

# b. Translate your algorithm into Python by writing a function named
# hopedale_average that takes a filename as a parameter and returns the
# average number of pelts produced per year.
def hopedale_average(file):
    with open(file) as reader:
        # Skip the header row
        reader.readline()

        line = reader.readline()

        # Skip the comment lines
        while line.startswith('#'):
            line = reader.readline()

        total = 0
        data_rows = 1

        while line:
            total += int(line.strip())
            data_rows += 1
            line = reader.readline()

    return total / data_rows

print(hopedale_average('hopedale.txt'))