# Modify the file reader in read_smallest_skip.py of Skipping the Header, on page
# 189, so that it uses a continue inside the loop instead of an if. Which form
# do you find easier to read?

# I have no idea what they're asking me to do in this one.

def skip_header(reader):
    """ (file open for reading) -> str

    Skip the header in reader and return the first real piece of data.
    
    """
    # Read the description line.
    line = reader.readline()

    # Find the first non-comment line.
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    # Now line contains the first real piece of data.
    return line

def smallest_value(reader):
    """ (file open for reading) -> NoneType

    Read and process reader reader and return the smallest
    value after the time_series header.

    """

    line = skip_header(reader).strip()

    if line == '':
        return 'File contains no data'
    else:

        # Now line contains the first data value; this is also the smallest value
        # found so far, because it is the only one we have seen.
        smallest = int(line)

        for line in reader:
            value = int(line.strip())

        # If we find a smaller value, remember it.
        if value < smallest:
            smallest = value

        return smallest

if __name__ == '__main__':
    with open('no_data.txt', 'r') as input_file:
        print(smallest_value(input_file))