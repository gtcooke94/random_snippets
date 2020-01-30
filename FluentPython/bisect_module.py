"""
Fluent Python Example 2-18. Use bisect to perform table lookups by numeric values, for example letter grades given a test score
bisect.bisect(haystack, needle) returns an inserstion point for needle in haystack. Haystack needs to be sorted.
bisect_right is default, but we can also do bisect_left
"""

import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
    """
    >>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    ['F', 'A', 'C', 'C', 'B', 'A', 'A']
    """
    return grades[bisect.bisect(breakpoints, score)]


"""
Example 2-19.
Efficiently insert into an already sorted sequence
`insort(seq, item)` inserts `item` into `seq`, keeping `seq` in ascending order
"""


def insert():
    import bisect
    import random

    SIZE = 7
    random.seed(1729)
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        bisect.insort(my_list, new_item)
    print(my_list)
    """
    >>> insert()
    [0, 2, 6, 7, 8, 10, 10]
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
