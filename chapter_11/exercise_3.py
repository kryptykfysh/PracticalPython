# The PDB file format is often used to store information about molecules.
# A PDB file may contain zero or more lines that begin with the word AUTHOR
# (which may be in uppercase, lowercase, or mixed case), followed by spaces
# or tabs, followed by the name of the person who created the file. Write a
# function that takes a list of filenames as an input argument and returns
# the set of all author names found in those files.

def find_authors(file_list):
    authors = set()

    for file in file_list:
        with open(file) as reader:
            line = reader.readline()

            if line.upper().startswith('AUTHOR'):
                authors.add(line[6:].strip())

    return authors