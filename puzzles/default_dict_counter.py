""" We can make a defaultdict to always initialize empty elements with
something of our choice. defaultdict(int) will always initialize elements in
the dict with a 0, because that is what is returned by int().
How could we make this always return 1 instead. How could we make it return a
counter?
"""
from collections import defaultdict

zeros = defaultdict(int)
for i in range(10):
    assert zeros[i] == 0


###############################################################################
""" Default Dict takes a callable. So we just need a function that always
returns 1
"""
ones = defaultdict(lambda: 1)
for i in range(10):
    assert ones[i] == 1

###############################################################################
""" For the second question, we need a callable that returns a counter. Here's
a jupyter notebook that has several solutions: https://github.com/jebotz/public-notebooks/blob/master/defaultdict_puzzle.ipynb"""

# Generator solution
def counter():
    counter = 0
    while True:
        yield counter
        counter += 1

counting = defaultdict(counter().__next__)
for i in range(10):
    assert counting[i] == i

# Itertools count
from itertools import count
counting = defaultdict(count(0).__next__)
for i in range(10):
    assert counting[i] == i


# Without using __next__ (one should avoid using these when possible)
from functools import partial
counting = defaultdict(partial(next, count(0)))
for i in range(10):
    assert counting[i] == i



