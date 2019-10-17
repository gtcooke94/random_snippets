from itertools import groupby
from operator import itemgetter
from collections import Counter, defaultdict


def format_ranges(numbers):
    all_lists = handle_duplicates(numbers)
    all_range_tuples = []
    for count, l in all_lists.items():
        all_range_tuples.append(get_range_tuples(l))

    all_range_tuples = (tup for tups in all_range_tuples for tup in tups)
    all_range_tuples = sorted(all_range_tuples)
    return build_string_from_tuples(all_range_tuples)


def get_range_tuples(numbers):
    numbers = sorted(numbers)
    # Match value with index
    numbers = enumerate(numbers)
    # Group by difference in number and index. Consecutive numbers will have the same difference, so jumps in this correspond to non consecutive numbers
    grouped = groupby(numbers, lambda it: it[1] - it[0])
    range_tuples = []
    for range_val in range_vals(grouped):
        range_val = list(range_val)
        low = range_val[0]
        high = range_val[-1]
        range_tuples.append([low, high])
    return range_tuples


def build_string_from_tuples(ranges_tuples):
    ranges_str = ""
    for low, high in ranges_tuples:
        if low == high:
            ranges_str += f"{low},"
        else:
            ranges_str += f"{low}-{high},"
    ranges_str = ranges_str[:-1]
    return ranges_str


def handle_duplicates(numbers):
    """ Idea. Split into sublists of items that occur different numbers of
    times.  Get a tuple (low, high) for every range for every sublist. Sort
    those by low then high, then create the ranges string
    """
    counts = Counter(numbers)
    counts_to_list = defaultdict(list)
    for val, count in counts.items():
        counts_to_list[count].append(val)
    max_count = max(counts_to_list.keys())
    counts_to_full_lists = defaultdict(set)
    prev_list = set()
    for i in range(max_count, 0, -1):
        counts_to_full_lists[i] = set(counts_to_list[i]) | prev_list
        prev_list = counts_to_full_lists[i]
    return counts_to_full_lists


def range_vals(grouped):
    for _, group in grouped:
        yield map(itemgetter(1), group)


"""
Pre final bonus solution below. This was refactored above
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
"""
