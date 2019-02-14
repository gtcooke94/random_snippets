tup = ('hello', object(), 42)
tup[2]
# This errors, tuples do not support item assignment
# tup[2] = 23

# NamedTuples are immutable containers, they are "write once, read many"
# Different that tuples because all atrributes are named and can be accessed
# through a human-readable identifier
from collections import namedtuple
# Define named tuple Car with two attributes - color and mileage, and we have
# to assign it to the classname that we want. The first parameter is actually
# the typename
Car = namedtuple('Car', 'color mileage')
# Can also pass a normal list as the second argument
# Car = namedtuple('Car', ['color', 'mileage'])

my_car = Car('red', 3000)
print(my_car.color)
print(my_car.mileage)
# Can also use indices, so namedtuples can be a drop in replacement for regular
# tuples
assert my_car[0] == my_car.color
assert my_car[1] == my_car.mileage
print(tuple(my_car))
# Tuple unpacking works too (in Python3)
# print(*my_car)
# This fails, because the attributes are immutable
# my_car.color = 'blue'

# "nampedtuples are a memory-efficient shortcut to defining an immutable class
# in Python manually.

# Can be subclassed, because they are implemented internally as regular classes

class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithMethods('red', 1234)
print(c.hexcolor())

# This can get messy, though. Adding new immutable fields is weird.
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))

# In nampedtuples, the preprended _ doesn't signal private, they are just named
# as such to be helper methods that don't have name collisions with user
# defined tuples
print(repr(my_car._asdict()))
#  print(json.dumps(my_car._asdict()))

# Creates a shallow copy where you can change some fields
blue_car = my_car._replace(color='blue')
print(repr(blue_car))

# Makes new instances of namedtuple from a sequence or iterable
another_car = Car._make(['red', 999])
print(repr(another_car))
