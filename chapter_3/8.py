# Complete the examples in the docstring and then write the body of the
# following function:

def weeks_elapsed(day1, day2):
  """ (int, int) -> int

  day1 and day2 are days in the same year. Return the number of full weeks
  that have elapsed between the two days.

  >>> weeks_elapsed(3, 20)
  2
  >>> weeks_elapsed(20, 3)
  2
  >>> weeks_elapsed(8, 5)
  0
  >>> weeks_elapsed(40, 61)
  3
  """
  number_of_days = abs(day1 - day2)
  number_of_weeks = number_of_days // 7
  return number_of_weeks