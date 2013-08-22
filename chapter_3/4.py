# Following the function design recipe, define a function that has two
# parameters, both numbers, and returns the absolute value of the difference
# of the two. Hint: Call the built-in abs function.

def abs_difference(first_number, second_number):
  """ (number, number) -> number

  Take two number parameters and return the absolute difference.

  >>> abs_difference(-1, 3)
  4
  >>> abs_difference(1, 2)
  1
  >>> abs_difference(-3, -2)
  1
  """

  arguments = (first_number, second_number)
  return abs(max(arguments) - min(arguments))
