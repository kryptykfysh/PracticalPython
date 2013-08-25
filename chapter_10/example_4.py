# In Processing Whitespace-Delimited Data, on page 193, we used the “For
# Line in File” technique to process data line by line, breaking it into pieces
# using the string method split. Rewrite the function process_file to skip the
# header as normal but then use the Read technique to read all the data
# at once.

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

def process_file(reader):
    """ (file open for reading) -> NoneType

    Read and print the data from reader, which must start with a single
    description line, then a sequence of lines beginning with '#', then a
    sequence of data.

    """
    # Find and print the first piece of data.
    line = skip_header(reader).strip()
    print(line)

    # Read the rest of the data.
    # for line in reader:
    #     line = line.strip()
    #     print(line)
    data = reader.read().replace(' ', '')
    print(data)

if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        process_file(input_file)
