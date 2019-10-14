from itertools import groupby
from operator import itemgetter

def format_ranges(numbers):
    numbers = sorted(numbers)
    # Match value with index
    numbers = enumerate(numbers)
    # Group by difference in number and index. Consecutive numbers will have the same difference, so jumps in this correspond to non consecutive numbers
    grouped = groupby(numbers, lambda it: it[1] - it[0])
    ranges_str = ""
    for range_val in range_vals(grouped):
        range_val = list(range_val)
        low = range_val[0]
        high = range_val[-1]
        if low == high:
            ranges_str += f"{low},"
        else:
            ranges_str += f"{low}-{high},"
    ranges_str = ranges_str[:-1]
    return ranges_str

def range_vals(grouped):
    for _, group in grouped:
        yield map(itemgetter(1), group)
