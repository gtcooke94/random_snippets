# Beats 90% of submissions
import math
from typing import List
from itertools import accumulate

"""
Example where solution wraps:

A = [0 5 8 -9 10 -7 4 -2]
cumsumforward = [0 5 13 4 14 7 11 9]
cumsumbackward = [-2 2 -5 5 -4 4 9 9]
running_max(cumsumbackward) = [-2 2 2 5 5 5 9 9]
max_backward_pairing = [9 5 5 5 2 2 -2]

Add max_backward_pairing and cumsumfoward together to get max of subarrays that cross middle
[0 5 13 4 14 7 11 _] + [9 5 5 5 2 2 -2 _]
[9 10 18 9 16 9 9]

Answer is 18 if we assume the max sum crosses the middle (in this case it does).
"""

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 1:
            return A[0]
        # Normal subarray sum on twice the array, making sure you don't let it have duplicates
        maxsum = -math.inf
        prev = -math.inf
        for num in A:
            # Need to keep track of indices as well... Because circular, favor ties that move to start the right
            # 1: Appending num to current subarray
            appendnum = prev + num
            if num >= appendnum:
                curval = num
            else:
                curval = appendnum
            if curval >= maxsum:
                maxsum = curval
            prev = curval

        # Case where it does container the middle
        cumsumforward = accumulate(A[:-1])
        cumsumbackward = accumulate(A[1::][::-1])

        max_backward_pairing = reversed(list(running_max(cumsumbackward)))
        for val1, val2 in zip(cumsumforward, max_backward_pairing):
            maxsum = max(maxsum, val1 + val2)

        return maxsum

    def __call__(self, n):
        return self.maxSubarraySumCircular(n)

def running_max(iterable):
    curmax = -math.inf
    for num in iterable:
        if num > curmax:
            curmax = num
        yield curmax
