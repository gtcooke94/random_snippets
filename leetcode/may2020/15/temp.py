import math
from itertools import accumulate

def running_max(iterable):
    curmax = -math.inf
    for num in iterable:
        if num > curmax:
            curmax = num
        yield curmax

a = [1, 2, 3, 4, -1]
print(list(running_max(accumulate(a[::-1]))))
