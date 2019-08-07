"""
I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

Try to solve this exercise without using any third-party libraries (without using pandas for example).

Before attempting any bonuses, I'd like you to put some effort into figuring out the clearest and most idiomatic way to solve this problem.

There are two bonuses this week.

For the first bonus, modify your add function to accept and "add" any number of lists-of-lists.

>>> add([[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]])
[[8, 8], [7, 7]]
For the second bonus, make sure your add function raises a ValueError if the given lists-of-lists aren't all the same shape.

>>> add([[1, 9], [7, 3]], [[1, 2], [3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "add.py", line 10, in add
    raise ValueError("Given matrices are not the same size.")
ValueError: Given matrices are not the same size.
"""


def add(*args):
    len_lists = len(args[0])
    len_sublists = len(args[0][0])
    for list_i in args:
        if len(list_i) != len_lists:
            raise ValueError("Given matrices are not the same size.")
        for sublist_i in list_i:
            if len(sublist_i) != len_sublists:
                raise ValueError("Given matrices are not the same size.")
    return [[sum(vals) for vals in zip(*sublists)] for sublists in zip(*args)]
    

# Non-bonus solution
#  def add(list1, list2):
    #  return [[val1 + val2 for val1, val2 in zip(sublist1, sublist2)] for sublist1, sublist2 in zip(list1, list2)]

    # This is wrong because it is flattened. Getting the right values though
    #  return [val1 + val2 for sublist1, sublist2 in zip(list1, list2) for val1, val2 in
    #          zip(sublist1, sublist2)]
