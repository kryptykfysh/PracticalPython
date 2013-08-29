# In this exercise, you will implement a Continent class, which represents a
# continent with a name and a list of countries. The Continent class will use
# the Country class from the previous question. If Country is defined in another
# module, you’ll need to import it.

from exercise_1 import Country

# a. Here is a sample interaction from the Python shell:
#     >>> canada = country.Country('Canada', 34482779, 9984670)
#     >>> usa = country.Country('United States of America', 313914040,
#     ...
#     9826675)
#     >>> mexico = country.Country('Mexico', 112336538, 1943950)
#     >>> countries = [canada, usa, mexico]
#     >>> north_america = Continent('North America', countries)
#     >>> north_america.name
#     'North America'
#     >>> for country in north_america.countries:
#     >>>     print(country)
#     Canada has a population of 34482779 and is 9984670 square km.
#     United States of America has a population of 313914040 and is 9826675 km.
#     square has a population of 112336538 and is 1943950 square km.
#     Mexico

# The code above cannot be executed yet, because the Continent class
# does not exist. Define Continent with a constructor (method __init__) that
# has three parameters: a continent, its name, and its list of Country
# objects.

class Continent:
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries
