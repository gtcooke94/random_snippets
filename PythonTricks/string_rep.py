class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # str is how the object get converted to a string
    def __str__(self):
        return "a {} car".format(self.color)

    def __repr__(self):
        # the !r in the format makes sure we get the repr of the thing being
        # put into it rather than the string
        return "{}({!r}, {!r})".format(self.__class__.__name__, self.color,
                self.mileage)



a = Car('red', 30)
print(a)
# Inspecting a in ipython will get you the __repr__ string

# Containers always use result of __repr__ to represent the objects they
# contain
print(str([a]))

# Best way to make sure that you know what is happening
print(str(a))
print(repr(a))

# Real difference between repr and string:
# string is a nice, textual display, comfortable showing to a user
# repr is unambiguous representation, helpful for developers
# If you don't have a __str__, python falls back to __repr__
import datetime
t = datetime.date.today()
print(str(t))
print(repr(t))

