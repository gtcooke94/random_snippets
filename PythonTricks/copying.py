# Assignment, same pointer
a = [1, 2, 3]
b = a
b[0] = 'X'
assert a == ['X', 2, 3]

# Shallow copy
a = [1, 2, 3]
b = list(a)
b[0] = 'X'
assert a == [1, 2, 3]

a = [[1, 2, 3], [4, 5, 6]]
b = list(a)
b.append([7, 8, 9])
assert a == [[1, 2, 3], [4, 5, 6]]
b[0][0] = 'X' 
# Since b is a shallow copy of a, the inner lists inside of a are pointing to
# the same object, so a[0][0] WILL CHANGE
assert a == [['X', 2, 3], [4, 5, 6]]

# Deep copies are a full copy of everything, changing one won't change the
# other
# copy.deepcopy() for deep copies, copy.copy() for shallow copies for arbitrary
# objects
import copy
a = [[1, 2, 3], [4, 5, 6]]
b = copy.deepcopy(a)
b.append([7, 8, 9])
assert a == [[1, 2, 3], [4, 5, 6]]
b[0][0] = 'X'
# Since a is a deepcopy of b, this DOESN'T change a[0][0]
assert a == [[1, 2, 3], [4, 5, 6]]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({!r}, {!r})".format(self.x, self.y)

a = Point(1, 2)
b = copy.copy(a)
assert a is not b

# When using immutable types like ints, there is no difference in deep and
# shallow copies

class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return ("Rectangle({!r}, {!r})".format(self.topleft, self.bottomright))

rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)
assert rect is not srect
# Changing the point in shallow copy will not change the point in original
srect.topleft = Point(999, 999)
assert rect.topleft.x == 0
# Because shallow copy point points to the same point, changing an individual
# attribute of the point WILL change the value in the original
srect.bottomright.x = 999
assert rect.bottomright.x == 999
