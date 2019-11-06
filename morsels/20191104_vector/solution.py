from dataclasses import astuple, dataclass
from numbers import Number


@dataclass(frozen=True)
class Vector:

    x: Number
    y: Number
    z: Number

    __slots__ = 'x', 'y', 'z'

    def __iter__(self):
        yield from astuple(self)

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Vector(x1+x2, y1+y2, z1+z2)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Vector(x1-x2, y1-y2, z1-z2)

    def __mul__(self, scalar):
        if not isinstance(scalar, Number):
            return NotImplemented
        x, y, z = self
        return Vector(scalar*x, scalar*y, scalar*z)
    __rmul__ = __mul__

    def __truediv__(self, scalar):
        if not isinstance(scalar, Number):
            return NotImplemented
        x, y, z = self
        return Vector(x/scalar, y/scalar, z/scalar)
