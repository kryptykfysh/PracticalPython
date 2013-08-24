# The variable appointments refers to the list ['9:00', '10:30', '14:00', '15:00', '15:30'].
# An appointment is scheduled for 16:30, so '16:30' needs to be added to the
# list.
appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
print(appointments)

# a. Using the list method append, add '16:30' to the end of the list that
# appointments refers to.
appointments.append('16:30')
print(appointments)

# b. Instead of using append, use the + operator to add '16:30' to the end of
# the list that appointments refers to.
print(appointments + ['1630'])

# c. You used two approaches to add '16:30' to the list. Which approach
# modified the list and which approach created a new list?

# append() modifies the list. + creates a new list