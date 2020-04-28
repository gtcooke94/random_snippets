from typing import List


"""
Fastest by a lot, but uglier
Get speed gains by not using defaultdict or counter. They do function calls, have extra overhead.
Tradeoff is succinctness and written complexity - we have to do a lot more `if` checks to see if a value is in the cumsum_freqs dictionary now
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        solution = 0
        cumsum_freqs = dict()
        cumsum = 0
        for val in nums:
            cumsum += val
            # we need this value - x = k, so number of times x occurs thus far in cumsum_freqs is number of k's
            prev_val_needed = cumsum - k
            if prev_val_needed in cumsum_freqs:
                solution += cumsum_freqs[prev_val_needed]
            if cumsum in cumsum_freqs:
                cumsum_freqs[cumsum] += 1
            else:
                cumsum_freqs[cumsum] = 1
        # Times where the cumsum is just == k haven't been counted yet
        if k in cumsum_freqs:
            solution += cumsum_freqs[k]
        return solution

    def __call__(self, l, k):
        return self.subarraySum(l, k)

"""
Even more efficient
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        solution = 0
        cumsum_freqs = defaultdict(lambda: 0)
        cumsum = 0
        for val in nums:
            cumsum += val
            # we need this value - x = k, so number of times x occurs thus far in cumsum_freqs is number of k's
            prev_val_needed = cumsum - k
            solution += cumsum_freqs[prev_val_needed]
            cumsum_freqs[cumsum] += 1
        # Times where the cumsum is just == k haven't been counted yet
        solution += cumsum_freqs[k]
        return solution

    def __call__(self, l, k):
        return self.subarraySum(l, k)
"""

"""
A little more efficient, don't actually need cumsum array, just the value
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        solution = 0
        cumsum_freqs = Counter()
        cumsum = 0
        for val in nums:
            cumsum += val
            # we need this value - x = k, so number of times x occurs thus far in cumsum_freqs is number of k's
            prev_val_needed = cumsum - k
            solution += cumsum_freqs[prev_val_needed]
            cumsum_freqs.update((cumsum,))
        # Times where the cumsum is just == k haven't been counted yet
        solution += cumsum_freqs[k]
        return solution

    def __call__(self, l, k):
        return self.subarraySum(l, k)
"""

"""
Works, O(n), can be more efficient
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        solution = 0
        cumsum_freqs = Counter()
        cumsum = [nums[0]]
        cumsum_freqs[nums[0]] = 1
        if nums[0] == k:
            solution += 1
        for val in nums[1:]:
            cumsum_to_now = cumsum[-1] + val
            if cumsum_to_now == k:
                solution += 1
            # we need this value - x = k, so number of times x occurs thus far in cumsum_freqs is number of k's
            prev_val_needed = cumsum_to_now - k
            solution += cumsum_freqs[prev_val_needed]
            cumsum.append(cumsum_to_now)
            cumsum_freqs.update((cumsum_to_now,))
        return solution

    def __call__(self, l, k):
        return self.subarraySum(l, k)
"""


"""
O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        solution = 0
        cumsum = [nums[0]]
        if nums[0] == k:
            solution += 1
        for val in nums[1:]:
            cumsum_to_val = cumsum[-1] + val
            if cumsum_to_val == k:
                solution += 1
            cumsum.append(cumsum_to_val)
        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                if cumsum[j] - cumsum[i - 1] == k:
                    solution += 1
        return solution

    def __call__(self, l, k):
        return self.subarraySum(l, k)
"""
