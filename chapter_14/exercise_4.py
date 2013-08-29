# Write a Nematode class to keep track of information about C.elegans,
# including a variable for the body length (in millimeters; they are about
# 1 mm in length), gender (either hermaphrodite or male), and age (in days).
# Include methods __init__, __repr__, and __str__.

class Nematode:
    def __init__(self, body_length, gender, age):
        """(number, str, number) -> NoneType

        Create a new Nematode with body length, gender and age.

        """

        self.body_length = body_length
        self.gender = gender
        self.age = age

    def __str__(self):
        return """Body Length: {0}
        Gender: {1}
        Age: {2}""".format(self.body_length, self.gender, self.age)

    def __repr__(self):
        return "Nematode({0}, '{1}', {2})".format(
            self.body_length, self.gender, self.age)