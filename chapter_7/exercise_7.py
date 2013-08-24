# The variable s refers to ' yes '. When a string method is called with s as its
# argument, the string 'yes' is produced. Which string method was called?

s = ' yes '
print("str.replace(' ', '') causes '{}' to become '{}'".format(s, s.replace(' ', '')))