# Following the function design recipe, define a function that has one
# parameter, a distance in kilometers, and returns the distance in miles.
# (There are 1.6 kilometers per mile.)

def kms_to_miles(kms):
  """ number -> float

  Take a number in miles and return a float in kilometers.

  >>> miles_to_kms(42)
  26.25
  >>> miles_to_kms(5)
  3.125
  >>> miles_to_kms(9.43)
  5.89375
  """
  
  return kms / 1.6
