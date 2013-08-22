# Following the function design recipe, define a function that has three
# parameters, grades between 0 and 100 inclusive, and returns the average
# of those grades.

def average_grade(g1, g2, g3):
  """ (integer, integer,integer) -> float

  Returns the average (float) of three integer parameters.
  Throws an exception if the parameters are not between 0 and 100.

  >>> average_grade(50, 75, 25)
  50
  >>> average_grade(-5, 42, 87)
  ValueError: please enter numbers between 0 and 100
  >>> average_grade(10, 20, 30)
  20
  """

  args = (g1, g2, g3)

  # Test grades are in acceptable range.
  if any((arg < 0 or arg > 100) for arg in args):
    raise ValueError("please enter numbers between 0 and 100")
  else:
    return sum(args) / 3