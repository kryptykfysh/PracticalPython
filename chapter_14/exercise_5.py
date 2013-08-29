# Consider this code:
#     >>> segment = LineSegment(Point(1, 1), Point(3, 2))
#     >>> segment.slope()
#     0.5
#     >>> segment.length()
#     2.23606797749979

# In this exercise, you will write two classes, Point and LineSegment, so that
# you can run the code above and get the same results.

# a. Write a Point class with an __init__ method that takes two numbers as
# parameters.
class Point:
    def __init__(self, x, y):
        """(number, number) -> NoneType

        Creates a Point with an x and y coordinate.

        """
        self.x = x
        self.y = y

    # b. In the same file, write a LineSegment class whose constructor takes two
    # Points as parameters. The first Point should be the start of the segment.
class LineSegment:
    def __init__(self, start_point, end_point):
        """(point, point) -> NoneType

        Creates a LineSegment from two Point object parameters, a start_point
        and an end_point.
        """
        self.start_point = start_point
        self.end_point = end_point

    # c. Write a slope method in the LineSegment class that computes the slope
    # of the segment. (Hint: The slope of a line is rise over run.)
    def run(self):
        return self.end_point.x - self.start_point.x

    def rise(self):
        return self.end_point.y - self.start_point.y

    def slope(self):
        return self.rise() / self.run()

    # d. Write a length method in the LineSegment class that computes the length
    # of the segment. (Hint: Use x ** n to raise x to the nth power. To compute
    # the square root, raise a number to the (1/2) power or use math.sqrt)
    def length(self):
        return (self.run() ** 2 + self.rise() ** 2)**(1/2)
