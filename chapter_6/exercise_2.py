# In the following exercises, you will work with Python's calendar module:

# a. Visit the Python documentation website at http://docs.python.org/release/
# 3.3.0/py-modindex.html, and look at the documentation on the calendar
# module.

# b. Import the calendar module.
import calendar

# c. Using the help function, read the description of the function isleap.
help(calendar.isleap)

# d. Use isleap to determine the next leap year.
from datetime import date
year = date.today().year

while not calendar.isleap(year):
    year += 1

print('Next leap year is:', year)

# e. Use dir to get a list of what calendar contains.
dir(calendar)

# f. Find and use a function in the calendar module to determine how many
#   leap years there will be between the years 2000 and 2050, inclusive.
start = 2000
finish = 2050
print('Number of leap years between', start, 'and', finish, 'is', calendar.leapdays(start, finish))

# g. Find and use a function in the calendar module to determine which day
# of the week July 29, 2016, will be.
print('29th July 2016 is a', calendar.day_name[calendar.weekday(2016, 7, 29)])
