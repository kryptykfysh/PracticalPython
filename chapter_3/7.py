# Following the function design recipe, define a function that has four
# parameters, all of them grades between 0 and 100 inclusive, and returns
# the average of the best 3 of those grades. Hint: Call the function that you
# defined in the previous question.

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

def average_best_three_grades(g1, g2, g3, g4):
  """ (number, number, number, number) -> float

  Returns the average of the highest three grades out of four.

  >>> average_best_three_grades(0, 25, 50, 75)
  50
  >>> average_best_three_grades(95, 6, 90, 85)
  90
  """
  all_grades = [g1, g2, g3, g4]
  all_grades.remove(min(all_grades))
  return average_grade(*all_grades)
