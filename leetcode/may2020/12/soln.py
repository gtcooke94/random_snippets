import math
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        If we are before the non-duplicate, 0-1, 2-3, 4-5, 6-7 should be paired. (even - odd)
            -> We need to look later in the array
        If we are after the non-duplicate, 1-2, 3-4, 5-6, should be paired (odd - even)
            -> We need to look earlier in the array
        BFS to find it"""
        low, high = 0, len(nums) - 1
        while True:
            if low == high:
                return nums[low]
            mid = low + (high - low) // 2
            print(low, high, mid)
            above, below = mid + 1, mid - 1
            midnum = nums[mid]
            matched = None
            # Find match
            if midnum == nums[above]:
                matched = above
            elif midnum == nums[below]:
                matched = below
            if matched is None:
                return midnum
            if mid % 2 == 0:
                if matched > mid:
                    # even - odd
                    low = mid + 1
                else:
                    # odd - even
                    high = mid - 1
            if mid % 2 != 0:
                if matched < mid:
                    # even - odd
                    low = mid + 1
                else:
                    # odd -even
                    high = mid - 1
        
    def __call__(self, n):
        return self.singleNonDuplicate(n)
