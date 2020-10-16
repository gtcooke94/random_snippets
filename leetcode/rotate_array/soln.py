import math
from typing import List

class Solution:
    def rotate_even(self, nums, k) -> None:
        start = 0
        cur_ind = 0
        hold = nums[0]
        total_changed = 0
        len_nums = len(nums)
        first_flag = True
        while total_changed < len_nums:
            while first_flag or cur_ind != start:
                new_ind = (cur_ind + k) % len_nums
                nums[new_ind], hold = hold, nums[new_ind]
                cur_ind = new_ind
                total_changed += 1
                first_flag = False
            start += 1
            cur_ind = start
            hold = nums[cur_ind]
            first_flag = True
        return nums


    def __call__(self, n, k):
        return self.rotate_even(n, k)
