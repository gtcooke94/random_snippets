def parse_ranges(ranges):
    ranges = ranges.split(",")
    for r in ranges:
        if "->" in r:
            yield int(r.split("->")[0])
        elif "-" in r:
            low, high = (int(val) for val in r.split("-"))
            yield from range(low, high + 1)
        else:
            yield int(r)
