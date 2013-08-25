# All of the file-reading functions we have seen in this chapter read forward
# through the file from the first character or line to the last. How could you
# write a function that would read backward through a file?

# The only issue I can see with this is that all the file data has to be 
# loaded in to memory at once. If you have a large file, you're going to have
# a bad time.

with open('file_example.txt', 'r') as file:
  data = file.readlines()
  data.reverse()

print(data)
