class Vector:
    __slots__ = ["_x", "_y", "_z"]

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __iter__(self):
        yield from (self.x, self.y, self.z)

    def __eq__(self, other):
        # Uses the fact that they are iterable
        return all(s == o for s, o in zip(self, other))

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Cannot add non-vector to vector")
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Vector(x1 + x2, y1 + y2, z1 + z2)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Cannot add non-vector to vector")
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Vector(x1 - x2, y1 - y2, z1 - z2)

    def __mul__(self, scalar):
        return self.multiply(scalar)

    def __rmul__(self, scalar):
        return self.multiply(scalar)

    def multiply(self, scalar):
        try:
            float(scalar)
        except ValueError:
            raise TypeError("Cannot multiply vector by a non-number")
        x1, y1, z1 = self
        return Vector(x1 * scalar, y1 * scalar, z1 * scalar)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        raise Exception("Vector is immutable. You cannot reassign it's value")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        raise Exception("Vector is immutable. You cannot reassign it's value")

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        raise Exception("Vector is immutable. You cannot reassign it's value")

    def __truediv__(self, scalar):
        try:
            float(scalar)
        except ValueError:
            raise TypeError("Cannot multiply vector by a non-number")
        x1, y1, z1 = self
        return Vector(x1 / scalar, y1 / scalar, z1 / scalar)
