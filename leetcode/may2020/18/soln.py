import math
from typing import List
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cs1 = Counter(s1)
        for window in sliding_window(s2, len(s1)):
            window_counter = Counter(window)
            if not cs1 - window_counter:
                return True
        return False

    def __call__(self, s1, s2):
        return self.checkInclusion(s1, s2)


def sliding_window(iterable, size):
    if size > len(iterable):
        yield iterable
    else:
        start = 0
        end = start + size
        while end <= len(iterable):
            yield iterable[start:end]
            start += 1
            end += 1
