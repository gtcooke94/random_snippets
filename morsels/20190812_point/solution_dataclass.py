# This solution uses python's dataclasses
from dataclasses import astuple, dataclass


@dataclass
class Point:

    """Three-dimensional point."""

    x: float
    y: float
    z: float

    def __add__(self, other):
        """Return copy of our point, shifted by other."""
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1 + x2, y1 + y2, z1 + z2)

    def __sub__(self, other):
        """Return copy of our point, shifted by other."""
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1 - x2, y1 - y2, z1 - z2)

    def __mul__(self, scalar):
        """Return new copy of our point, scaled by given value."""
        x, y, z = self
        return Point(scalar * x, scalar * y, scalar * z)

    __rmul__ = __mul__

    def __iter__(self):
        yield from astuple(self)
