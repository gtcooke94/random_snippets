from collections.abc import Sequence
from itertools import accumulate

class PiecewiseRange(Sequence):
    def __init__(self, ranges):
        #  import pdb; pdb.set_trace()
        ranges = ranges.replace(" ", "")
        self.ranges = [self.compute_range(r) for r in ranges.split(",")]
        self.range_lens = [len(r) for r in self.ranges]
        self.cumulative_lens = list(accumulate(self.range_lens))
        self._len = sum(self.range_lens)
        
    def compute_range(self, r):
        if "-" in r:
            low, high = (int(i) for i in r.split("-"))
            high += 1
        else:
            low = int(r)
            high = low + 1
        return range(low, high)

    def __getitem__(self, i):
        if i > len(self):
            raise IndexError()
        if i < 0:
            i = len(self) + i
        subrange, offset = self.get_appropriate_subrange(i)
        return subrange[i - offset]

    def get_appropriate_subrange(self, i):
        subrange_cumulative_index = 0
        one_based = i + 1
        lower = 0
        while True:
            upper = self.cumulative_lens[subrange_cumulative_index]
            if one_based <= upper and one_based > lower:
                return self.ranges[subrange_cumulative_index], lower 
            subrange_cumulative_index += 1
            lower = upper

    




    def __len__(self):
        return self._len


