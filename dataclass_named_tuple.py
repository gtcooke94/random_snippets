from collections import namedtuple
from dataclasses import dataclass, astuple
from numbers import Number

VectorTuple = namedtuple("VectorTuple", "x, y, z")


@dataclass(ordering=True)
class VectorDataClass:
    x: float
    y: float
    z: float

    def __add__(self, other):
        if not isinstance(other, VectorDataClass):
            raise NotImplementedError
        return VectorDataClass(*(a + b for a, b in zip(self, other)))

    def __mul__(self, other):
        if not isinstance(other, Number):
            raise NotImplementedError
        return VectorDataClass(*(a * other for a in self))

    __rmul__ = __mul__

    def __iter__(self):
        yield from astuple(self)

    __slots__ = "x", "y", "z"


"""For NamedTuples
- Addition is bad
- Multiplication is bad
- Less than/Greater than are bad
- Tuple unpacking is good
- Automatically immutable

Dataclasses
- Have to Implement Operators
- You get __eq__, __repr__, __init__ for free
- Easy to implement tuple unpacking
- Easy to implement slots
- Easy to implement immutable
Optional but false by default
`order` - gets logical operators (>, <, <=, >=) as if the class were a tuple of its fields
`unsafe_hash` - If eq and frozen are True and this is False, you get a hash. You can force a hash by setting to true
`frozen`

Can have default values

Tons of options you can specify per field that usually are for more specialized cases - check the documentation

"""


if __name__ == "__main__":
    for i in range(2):
        if i == 0:
            Vector = VectorTuple
            print("=" * 80)
            print("VectorTuple")
        elif i == 1:
            Vector = VectorDataClass
            print("=" * 80)
            print("VectorDataClass")

        a = Vector(1, 4, 9)
        b = Vector(1, 2, 3)
        aa = Vector(1, 4, 9)
        c = a + b
        print(f"{a} + {b} = {c}")
        print(f"a and b are of type {type(a)}")
        print(f"c is of type {type(c)}")
        print(f"{a} * 2 = {a * 2}")
        print(f"{a} == {aa}: {a == aa}")
        try:
            print(f"{a} < {b}: {a < b}")
        except TypeError:
            print("< is not implemented for this class")
        x, y, z = a
        print(x, y, z)
