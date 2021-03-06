"""
This week I'd like you to write a class representing a 3-dimensional point.

The Point class must accept 3 values on initialization (x, y, and z) and have x, y, and z attributes. It must also have a helpful string representation. Additionally, point objects should be comparable to each other (two points are equal if their coordinates are the same and not equal otherwise).

Example usage:

>>> p1 = Point(1, 2, 3)
>>> p1
Point(x=1, y=2, z=3)
>>> p2 = Point(1, 2, 3)
>>> p1 == p2
True
>>> p2.x = 4
>>> p1 == p2
False
>>> p2
Point(x=4, y=2, z=3)
If you finish the base exercise quickly, consider working through a bonus or two.

For the first bonus, I'd like you to allow Point objects to be added and subtracted from each other.

>>> p1 = Point(1, 2, 3)
>>> p2 = Point(4, 5, 6)
>>> p1 + p2
Point(x=5, y=7, z=9)
>>> p3 = p2 - p1
>>> p3
Point(x=3, y=3, z=3)
For the second bonus, I'd like you to allow Point objects to be scaled up and down by numbers.

>>> p1 = Point(1, 2, 3)
>>> p2 = p1 * 2
>>> p2
Point(x=2, y=4, z=6)
For the third bonus, I'd like you to allow Point objects to be unpacked using multiple assignment like this

>>> p1 = Point(1, 2, 3)
>>> x, y, z = p1
>>> (x, y, z)
(1, 2, 3)
"""


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z
        # Cleaner maybe:
        # return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __str__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Cannot add point to {other.__class__}")
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Cannot add point to {other.__class__}")
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return self.multiply(scalar)

    def __rmul__(self, scalar):
        return self.multiply(scalar)

    def multiply(self, scalar):
        return Point(self.x * scalar, self.y * scalar, self.z * scalar)

    def __iter__(self):
        return (value for value in (self.x, self.y, self.z))

    # Alternate __iter__ implementations:
    #  def __iter__(self):
    #      yield self.x
    #      yield self.y
    #      yield self.z
    #
    #  def __iter__(self):
    #      yield from (self.x, self.y, self.z)
    #
    #  def __iter__(self):
    #      return iter((self.x, self.y, self.z))

    # Note that having the __iter__ implementation allows us to do interesting tuple unpacking
    # Add could be the following, because the objects unpack:
    # x1, y1, z1 = self
    # x2, y2, z2 = other
    # return Point(x1 + x2, y1 + y2, z1 + z2)
